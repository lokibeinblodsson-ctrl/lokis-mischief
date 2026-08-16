#!/usr/bin/env python3
"""llm_fallback.py — resilient multi-provider LLM client for Loki's Mischief.

FAILSAFE DESIGN (why this exists):
The blog pipeline previously fell back to a STUB ("Research pass unavailable") whenever
the single cloud model 403'd/rate-limited. Groq is 403-blocked from this host, so every
post became a stub and the daily cron published garbage. This module removes that failure
mode entirely:

CHAIN (ordered, tried until one returns usable text):
  1. Mistral  (cloud, verified 200 from this host)
  2. Gemini   (cloud, verified 200 — gemini-flash-latest)
  3. Ollama   (LOCAL, offline-proof — deepseek-coder:latest via /api/generate)

Each provider is retried with exponential backoff on 429/5xx/timeout. A 4xx auth error
(401/403) skips straight to the next provider (no point retrying a dead key). If the whole
chain fails, llm_chat returns None and the CALLER must refuse to publish (no stub ever).

Keys are read from /root/.hermes/secrets/api_keys.env (never printed/logged).
"""
import os, json, time, urllib.request, urllib.error

_ENV = {}
try:
    for line in open("/root/.hermes/secrets/api_keys.env"):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1); _ENV[k] = v
except FileNotFoundError:
    pass

MISTRAL_KEY = _ENV.get("MISTRAL_LOKI") or _ENV.get("MISTRAL_LOKI_ALT")
GEMINI_KEY  = _ENV.get("GEMINI_LOKI") or _ENV.get("GEMINI_LOKI_ALT")
OLLAMA_URL  = "http://127.0.0.1:11434/api/generate"
OLLAMA_MODEL = "deepseek-coder:latest"  # small+fast, always available offline


def _post(url, body, headers, timeout=45):
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, json.loads(r.read().decode())


def _mistral(system, user, retries=2):
    if not MISTRAL_KEY:
        return None, "no_key"
    body = json.dumps({"model": "mistral-large-latest",
                       "messages": [{"role": "system", "content": system},
                                    {"role": "user", "content": user}],
                       "temperature": 0.7, "max_tokens": 1600}).encode()
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + MISTRAL_KEY}
    for attempt in range(retries + 1):
        try:
            s, j = _post("https://api.mistral.ai/v1/chat/completions", body, headers)
            if s == 200 and j.get("choices"):
                return j["choices"][0]["message"]["content"], "ok"
            if s in (401, 403):
                return None, f"auth_{s}"
            if attempt < retries:
                time.sleep(2 ** attempt); continue
            return None, f"status_{s}"
        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                return None, f"auth_{e.code}"
            if e.code == 429 and attempt < retries:
                time.sleep(2 ** attempt); continue
            return None, f"http_{e.code}"
        except Exception:
            if attempt < retries:
                time.sleep(2 ** attempt); continue
            return None, "err"
    return None, "exhausted"


def _gemini(system, user, retries=2):
    if not GEMINI_KEY:
        return None, "no_key"
    body = json.dumps({"contents": [{"parts": [{"text": f"{system}\n\n{user}"}]}]}).encode()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={GEMINI_KEY}"
    headers = {"Content-Type": "application/json"}
    for attempt in range(retries + 1):
        try:
            s, j = _post(url, body, headers)
            if s == 200 and j.get("candidates"):
                return j["candidates"][0]["content"]["parts"][0]["text"], "ok"
            if s in (401, 403):
                return None, f"auth_{s}"
            if attempt < retries:
                time.sleep(2 ** attempt); continue
            return None, f"status_{s}"
        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                return None, f"auth_{e.code}"
            if e.code == 429 and attempt < retries:
                time.sleep(2 ** attempt); continue
            return None, f"http_{e.code}"
        except Exception:
            if attempt < retries:
                time.sleep(2 ** attempt); continue
            return None, "err"
    return None, "exhausted"


def _ollama(system, user, retries=1):
    """Local last-resort — works even with zero internet."""
    body = json.dumps({"model": OLLAMA_MODEL,
                       "prompt": f"{system}\n\n{user}",
                       "stream": False,
                       "options": {"temperature": 0.7, "num_predict": 1600}}).encode()
    headers = {"Content-Type": "application/json"}
    for attempt in range(retries + 1):
        try:
            s, j = _post(OLLAMA_URL, body, headers, timeout=120)
            if s == 200 and j.get("response"):
                return j["response"], "ok"
            if attempt < retries:
                time.sleep(3); continue
            return None, f"status_{s}"
        except Exception:
            if attempt < retries:
                time.sleep(3); continue
            return None, "err"
    return None, "exhausted"


# Ordered failover chain. Each entry: (name, callable).
_CHAIN = [
    ("mistral", _mistral),
    ("gemini", _gemini),
    ("ollama_local", _ollama),
]


def llm_chat(system, user, timeout_per_call=45):
    """Try providers in order until one yields text. Returns (text, provider_used) or (None, 'all_failed').

    The CALLER is responsible for refusing to publish if text is None (no stub fallback here).
    """
    last_reason = "none"
    for name, fn in _CHAIN:
        try:
            text, reason = fn(system, user)
        except Exception as e:
            text, reason = None, f"exception:{e}"
        if text and text.strip():
            return text, name
        last_reason = f"{name}:{reason}"
        # auth failures: skip immediately (don't burn retries on a dead key)
        if reason.startswith("auth_"):
            continue
    return None, f"all_failed ({last_reason})"


if __name__ == "__main__":
    # quick self-test
    t, who = llm_chat("You are terse.", "Reply with exactly: FALLBACK_OK")
    print("result:", repr(t[:40]) if t else None, "| provider:", who)
