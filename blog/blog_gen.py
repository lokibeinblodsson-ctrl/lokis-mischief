#!/usr/bin/env python3
# blog/blog_gen.py — Loki's Mischief daily business-automation blog generator.
# Purpose: every run, (1) if remaining ideas < 5, generate 100 NEW non-redundant ideas via LLM,
# (2) pop one idea, research it with Tavily, draft an HTML post via a free LLM (Groq/Mistral),
# (3) inject internal links (site pages) + external citations (research URLs), (4) write blog/<slug>.html,
# (5) update blog/index.json + blog.html. Idempotent: skips if a post already exists for today.
# Source of truth: blog-ideas.json (seed pool) + blog/index.json (published log).
import json, os, sys, re, datetime, urllib.request, urllib.parse, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDEAS = os.path.join(ROOT, "blog-ideas.json")
BLOG = os.path.join(ROOT, "blog")
IDX = os.path.join(BLOG, "index.json")
SITE = "https://lokis-mischief.example"  # replace with real domain when known; internal links use relative paths

# ---- load creds from local store (never echo) ----
ENV = {}
for line in open("/root/.hermes/secrets/api_keys.env"):
    line = line.strip()
    if line and not line.startswith("#") and "=" in line:
        k, v = line.split("=", 1); ENV[k] = v
TAVILY = ENV.get("TAVILY_FREETIER") or ENV.get("TAVILY_WILDJAZMINE_CA")
GROQ = ENV.get("GROQ_LOKI_ALT") or ENV.get("GROQ_JAYSHERMANN")
MISTRAL = ENV.get("MISTRAL_LOKI") or ENV.get("MISTRAL_WILDJAZMINE_CA")

def http_json(url, data=None, headers=None, method="GET", timeout=40):
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return {"_error": e.code, "_body": e.read().decode()[:300]}
    except Exception as e:
        return {"_error": str(e)}

def tavily_search(q):
    if not TAVILY: return []
    # Tavily expects the key as a Bearer Authorization header, NOT in the body.
    body = json.dumps({"query": q, "max_results": 5,
                       "search_depth": "basic", "topic": "general"}).encode()
    j = http_json("https://api.tavily.com/search", data=body,
                  headers={"Content-Type": "application/json", "Authorization": "Bearer " + TAVILY},
                  method="POST")
    return j.get("results", []) if isinstance(j, dict) else []

# NOTE: Groq is 403-blocked from this host, so Mistral is the primary model. We still try
# Groq as a secondary only if a working key is present, but never fall back to a STUB.
def llm_chat(system, user, model="mistral"):
    # Primary = Mistral (verified working on this host). Secondary = Groq if available.
    order = [("mistral", MISTRAL)] if model == "mistral" else [("groq", GROQ), ("mistral", MISTRAL)]
    for name, key in order:
        if not key:
            continue
        url = "https://api.mistral.ai/v1/chat/completions" if name == "mistral" else "https://api.groq.com/openai/v1/chat/completions"
        mdl = "mistral-large-latest" if name == "mistral" else "llama-3.3-70b-versatile"
        body = json.dumps({"model": mdl,
                           "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
                           "temperature": 0.7, "max_tokens": 1600}).encode()
        j = http_json(url, data=body, headers={"Content-Type": "application/json",
                      "Authorization": "Bearer " + key})
        if isinstance(j, dict) and j.get("choices"):
            return j["choices"][0]["message"]["content"]
    return None

def slugify(s):
    s = re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()
    return "-".join(s.split()[:8]) or "post"

def load_ideas():
    d = json.load(open(IDEAS))
    return d

def save_ideas(d):
    json.dump(d, open(IDEAS, "w"), indent=2)

def load_index():
    if os.path.exists(IDX):
        return json.load(open(IDX))
    return {"posts": [], "published": [], "ideasUsed": []}

def save_index(d):
    json.dump(d, open(IDX, "w"), indent=2)

# internal link map: keyword -> relative page (brand-consistent cross-links)
INTERNAL = [
    ("rune", "lore.html"), ("elder futhark", "lore.html"), ("norse", "lore.html"),
    ("myth", "lore.html"), ("odin", "odin.html"), ("loki", "loki.html"), ("thor", "thor.html"),
    ("freyr", "freyr.html"), ("freya", "freya.html"), ("tyr", "tyr.html"), ("heimdall", "heimdall.html"),
    ("bragi", "bragi.html"), ("hel", "hel.html"), ("sigyn", "sigyn.html"), ("fenrir", "fenrir.html"),
    ("jormungandr", "jormungandr.html"), ("gerd", "gerd.html"), ("hermod", "hermod.html"),
    ("hymir", "hymir.html"), ("angrboda", "angrboda.html"), ("utgardaloki", "utgardaloki.html"),
    ("service", "services.html"), ("design", "services.html"), ("brand", "services.html"),
    ("automation", "directory.html"), ("workflow", "directory.html"), ("directory", "directory.html"),
    ("game", "rune-cast.html"), ("cast", "rune-cast.html"),
]

def refill_ideas(d, used):
    # Generate 100 fresh ideas avoiding any already used/published
    prompt = ("You are the editor of 'Loki's Mischief', a brand that teaches business automation and agency "
              "ops through Norse mythology. Generate exactly 100 SHORT blog post titles (under 12 words each), "
              "one per line, no numbering, no quotes. Topics: business automation, Make.com/n8n/Windmill/Node-RED "
              "workflows, agency operations, pricing, branding, Norse-myth business lessons, AI tools, lean hosting. "
              "Avoid these already-used titles:\n" + "\n".join(used[:60]) +
              "\nReturn ONLY the list, no preamble.")
    txt = llm_chat("You output tight lists.", prompt) or ""
    new = [l.strip("-•0123456789. ").strip() for l in txt.splitlines() if l.strip()]
    new = [n for n in new if n and n not in used][:100]
    # pad if LLM under-delivered
    while len(new) < 100:
        new.append(f"Mischief note #{len(new)+1}: a small automation that compounds")
    d["ideas"] = new
    return d

def main():
    today = datetime.date.today().isoformat()
    d = load_ideas()
    idx = load_index()
    used = set(idx.get("ideasUsed", [])) | {p["title"] for p in idx.get("posts", [])}

    # Refill when pool is low
    if len(d.get("ideas", [])) < 5:
        print(f"[{today}] idea pool low ({len(d['ideas'])}); refilling 100...")
        d = refill_ideas(d, list(used))
        save_ideas(d)
        print(f"[{today}] refilled to {len(d['ideas'])} ideas")

    # Idempotent: skip if a post exists for today
    if any(p.get("date") == today for p in idx.get("posts", [])):
        print(f"[{today}] post already exists for today — skipping"); return

    if not d.get("ideas"):
        print(f"[{today}] no ideas left"); return
    idea = d["ideas"].pop(0)
    save_ideas(d)

    # Research
    results = tavily_search(idea)
    cites = [r.get("url") for r in results if r.get("url")][:4]
    ctx = "\n".join(f"- {r.get('title','')}: {r.get('content','')[:240]}" for r in results[:4])

    # Draft
    sys_p = ("You write for 'Loki's Mischief' — a brand that teaches business automation and agency ops through "
             "Norse mythology. Voice: confident, plain-spoken, a little mischievous. Never fake data. If unsure, say "
             "'consider' not 'proves'. Write clean HTML (h2/h3/p/ul), 350-500 words, NO outer <html> wrapper.")
    usr = (f"Write a blog post titled: \"{idea}\".\nResearch context:\n{ctx}\n\n"
           f"End with a 2-line takeaway tying it to a Norse figure. Use 1-2 Markdown-style internal references "
           f"like (see our lore page) but we will link them. Keep it useful, not clickbait.")
    html = llm_chat(sys_p, usr) or llm_chat(sys_p, usr, model="mistral")
    # QUALITY GATE: never publish a stub. If the draft failed OR is too thin OR lacks research,
    # bail out WITHOUT writing a file. The caller (blog_daily.sh) treats non-zero exit as "skip".
    STUB_MARKERS = ["unavailable this run", "draft queued", "consider tomorrow",
                    "generation skipped", "lorem ipsum"]
    words = len(re.findall(r"\b\w+\b", html or ""))
    bad = any(m in (html or "").lower() for m in STUB_MARKERS)
    if not html or bad or words < 280 or len(cites) == 0:
        print(f"[{today}] QUALITY_GATE_FAIL words={words} cites={len(cites)} bad={bad} — NOT publishing, skipping")
        sys.exit(2)

    # Inject internal links (body only; protect existing anchors so we never nest <a> in <a>)
    protected = []
    def _prot(m):
        protected.append(m.group(0)); return f"\x00{len(protected)-1}\x00"
    html_safe = re.sub(r"<a\b[^>]*>.*?</a>", _prot, html, flags=re.S)
    for kw, page in INTERNAL:
        if kw in html_safe.lower():
            html_safe = re.sub(rf"(\b{kw}[\w'-]*\b)(?![^<]*</a>)", rf'<a href="../{page}">\1</a>',
                               html_safe, count=1, flags=re.I)
    for i, p in enumerate(protected):
        html_safe = html_safe.replace(f"\x00{i}\x00", p)
    html = html_safe
    # External citations
    ext = ""
    for u in cites:
        ext += f'<li><a href="{u}" target="_blank" rel="noopener">{u}</a></li>'

    slug = slugify(idea)
    out = os.path.join(BLOG, slug + ".html")
    page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{idea} — Loki's Mischief</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;900&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
<style>body{{font-family:Inter,system-ui,sans-serif;background:#05060b;color:#e4e4e7;line-height:1.7;max-width:760px;margin:0 auto;padding:24px 18px}}
h1,h2,h3{{font-family:Cinzel,serif;color:#f59e0b}}a{{color:#f59e0b}}nav a{{margin-right:14px;font-size:13px;color:#94a3b8}}
.meta{{color:#64748b;font-size:13px;margin:8px 0 20px}}ul{{padding-left:20px}}</style></head>
<body>
<nav><a href="../index.html">Home</a><a href="../directory.html">Directory</a><a href="../services.html">Services</a><a href="../blog.html">Blog</a></nav>
<h1>{idea}</h1>
<div class="meta">Loki's Mischief · {today} · business automation research</div>
{html}
<hr style="border-color:#1a1a24;margin:28px 0">
<p style="font-size:13px;color:#94a3b8">Related: <a href="../lore.html">Lore</a> · <a href="../directory.html">Automation directory</a> · <a href="../services.html">Services</a></p>
<p style="font-size:13px;color:#64748b">Sources:</p><ul style="font-size:12px;color:#94a3b8">{ext or '<li>Internal research</li>'}</ul>
</body></html>"""
    open(out, "w").write(page)

    idx.setdefault("posts", []).append({"slug": slug, "title": idea, "date": today,
                                         "file": f"blog/{slug}.html", "cites": len(cites)})
    idx.setdefault("ideasUsed", []).append(idea)
    save_index(idx)
    # refresh blog.html index
    render_index(idx)
    print(f"[{today}] POSTED: {idea} -> blog/{slug}.html (cites={len(cites)})")

def render_index(idx):
    items = sorted(idx.get("posts", []), key=lambda p: p["date"], reverse=True)
    rows = "\n".join(f'<li><a href="{p["file"].split("/",1)[-1]}">{p["title"]}</a> <span style="color:#64748b">· {p["date"]}</span></li>' for p in items)
    html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Blog — Loki's Mischief</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;900&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
<style>body{{font-family:Inter,system-ui,sans-serif;background:#05060b;color:#e4e4e7;line-height:1.7;max-width:820px;margin:0 auto;padding:24px 18px}}
h1{{font-family:Cinzel,serif;color:#f59e0b}}a{{color:#f59e0b}}nav a{{margin-right:14px;font-size:13px;color:#94a3b8}}li{{margin:8px 0}}</style></head>
<body><nav><a href="../index.html">Home</a><a href="../directory.html">Directory</a><a href="../services.html">Services</a></nav>
<h1>📰 Loki's Mischief — Blog</h1><p style="color:#94a3b8">Daily business-automation research, written by our own pipeline.</p>
<ul>{rows}</ul></body></html>"""
    open(os.path.join(BLOG, "index.html"), "w").write(html)

if __name__ == "__main__":
    main()
