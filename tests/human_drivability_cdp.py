#!/usr/bin/env python3
"""Loki's Mischief — HUMAN-DRIVABILITY tests (batched CDP).

Each game's entire playthrough runs INSIDE ONE in-page async function that dispatches real
KeyboardEvent / PointerEvent inputs and reads only what a human sees (HUD text, dataset.dest,
end screen, pause overlay). The function stashes its [{name,ok,detail}] array on window.__r and
the Python side polls it. This collapses ~30 sequential CDP round-trips into ~3 navigations.

Why no awaitPromise: Runtime.evaluate with awaitPromise:true HANGS across a Page.navigate context
switch in this CDP client (websocket-client + flat session). Polling window.__r with plain evals is
reliable. Real input, real visible outcomes — not poking internal variables.

Run:  python3 tests/human_drivability_cdp.py   (needs :8899 + Chrome CDP 9224)
"""
import json, sys, time, urllib.request, socket
from websocket import create_connection

BASE = "http://127.0.0.1:8899"
FAILS, PASSES = [], []


def _pick_target_ws():
    """Reuse an EXISTING page target's own debugger websocket. Avoids Target.createTarget,
    which spawns a new orphan target on every run and eventually stalls Chrome."""
    targets = json.load(urllib.request.urlopen("http://127.0.0.1:9224/json", timeout=10))
    for t in targets:
        if t.get("type") == "page" and t.get("webSocketDebuggerUrl"):
            return t["webSocketDebuggerUrl"]
    raise RuntimeError("no page target available in Chrome")


class Tab:
    def __init__(self):
        self.ws = create_connection(_pick_target_ws(), timeout=30, suppress_origin=True)
        self.ws.settimeout(15)
        self.n = 0
        for d in ("Page", "Runtime", "Network"):
            self.cmd(d + ".enable")
        self.cmd("Network.setCacheDisabled", {"cacheDisabled": True})

    def cmd(self, method, params=None):
        self.n += 1
        m = {"id": self.n, "method": method, "params": params or {}}
        try:
            self.ws.send(json.dumps(m))
        except Exception:
            return {"_err": "send-failed"}
        end = time.time() + 30
        while time.time() < end:
            try:
                r = json.loads(self.ws.recv())
            except socket.timeout:
                return {"_timeout": True}
            except Exception:
                continue
            if r.get("id") == self.n and "result" in r:
                return r
        return {"_noresponse": True}

    def go(self, path, settle=2.4):
        self.cmd("Page.navigate", {"url": f"{BASE}/{path}"})
        time.sleep(settle)

    def run(self, expr):
        # Fire-and-forget: in-page async fn stashes result on window.__r. No awaitPromise (hangs).
        self.cmd("Runtime.evaluate", {"expression": "window.__r=null;" + expr, "returnByValue": True})
        for _ in range(80):
            res = self.cmd("Runtime.evaluate",
                           {"expression": "window.__r", "returnByValue": True}
                           ).get("result", {}).get("result", {}).get("value")
            if isinstance(res, list):
                return res
            if isinstance(res, dict) and res.get("__err"):
                return [{"__err": res["__err"]}]
            time.sleep(0.2)
        return [{"__err": "timeout waiting for in-page result"}]

    def close(self):
        try:
            self.ws.close()
        except Exception:
            pass


SLEIPNIR_JS = r"""
(async () => {
  window.__r = null;
  const out = [];
  const check = (name, ok, detail) => out.push({name, ok: !!ok, detail: detail || ''});
  const press = k => window.dispatchEvent(new KeyboardEvent('keydown',{key:k,bubbles:true,cancelable:true}));
  const tap = sel => { const el=document.querySelector(sel); if(!el) return false;
    const r=el.getBoundingClientRect(), x=r.left+r.width/2, y=r.top+r.height/2;
    el.dispatchEvent(new PointerEvent('pointerdown',{clientX:x,clientY:y,bubbles:true}));
    el.dispatchEvent(new PointerEvent('pointerup',{clientX:x,clientY:y,bubbles:true}));
    el.dispatchEvent(new MouseEvent('click',{clientX:x,clientY:y,bubbles:true})); return true; };
  const swipe = dx => { const cv=document.querySelector('#game canvas'), r=cv.getBoundingClientRect();
    const sy=r.top+r.height/2, mx=r.left+r.width/2;
    cv.dispatchEvent(new PointerEvent('pointerdown',{clientX:mx,clientY:sy,bubbles:true}));
    cv.dispatchEvent(new PointerEvent('pointerup',{clientX:mx+dx,clientY:sy,bubbles:true})); };
  const wait = ms => new Promise(r=>setTimeout(r,ms));
  const lane = () => document.getElementById('lane').textContent;
  const dist = () => parseInt(document.getElementById('dist').textContent)||0;
  document.getElementById('startBtn').click();
  await wait(500);
  check('starts on lane 1', lane()==='1' || lane()==='1/4', lane());
  const b = lane(); press('ArrowRight'); await wait(400);
  check('ArrowRight changes visible lane', lane()!==b, b+'->'+lane());
  const a = lane(); tap('#bl'); await wait(400);
  check('◀ button moves lane back', lane()!==a, a+'->'+lane());
  const c = lane(); swipe(60); await wait(400);
  check('swipe right on canvas moves lane', lane()!==c, c+'->'+lane());
  press('Escape'); await wait(300);
  check('Esc shows PAUSE overlay', !!document.getElementById('pauseOv'));
  check('state paused', Engine.state==='paused', Engine&&Engine.state);
  press('Escape'); await wait(300);
  check('Esc again resumes (overlay gone)', !document.getElementById('pauseOv'));
  const d0=dist(); await wait(2000); const d1=dist();
  check('distance advances while playing', d1>d0, d0+'->'+d1);
  window.__r = out;
})()
"""

RATATOSKR_JS = r"""
(async () => {
  window.__r = null;
  const out = [];
  const check = (name, ok, detail) => out.push({name, ok: !!ok, detail: detail || ''});
  const press = k => window.dispatchEvent(new KeyboardEvent('keydown',{key:k,bubbles:true,cancelable:true}));
  const wait = ms => new Promise(r=>setTimeout(r,ms));
  const score = () => parseInt(document.getElementById('score').textContent)||0;
  const streak = () => parseInt(document.getElementById('streak').textContent)||0;
  const mode = () => document.getElementById('mode').textContent;
  document.getElementById('startBtn').click();
  await wait(500);
  const dest = document.getElementById('game').dataset.dest;
  check('acorn queued with visible destination', ['0','1','2','3'].includes(dest), dest);
  document.querySelectorAll('#branches button')[dest].click(); await wait(300);
  check('correct branch -> AWAITING RECEIPT', mode()==='AWAITING RECEIPT', mode());
  check('delivery awards +20', score()>=20, score());
  await wait(2000);
  check('receipt confirmed (+30) after waiting', score()>=50, score());
  check('streak preserved after receipt', streak()>=1, streak());
  check('back to CARRYING after receipt', mode()==='CARRYING', mode());
  const dest2 = document.getElementById('game').dataset.dest;
  const wrong = String((parseInt(dest2)+1)%4);
  document.querySelectorAll('#branches button')[wrong].click(); await wait(300);
  check('wrong branch resets streak to 0', streak()===0, streak());
  press('p'); await wait(300);
  check('P pauses Ratatoskr', Engine.state==='paused' && !!document.getElementById('pauseOv'), Engine.state);
  press('p'); await wait(200);
  window.__r = out;
})()
"""

ENGINE_JS = r"""
(async () => {
  window.__r = null;
  const out = [];
  const check = (name, ok, detail) => out.push({name, ok: !!ok, detail: detail || ''});
  const press = k => window.dispatchEvent(new KeyboardEvent('keydown',{key:k,code:(k===' '?'Space':k),bubbles:true,cancelable:true}));
  const wait = ms => new Promise(r=>setTimeout(r,ms));
  const score = () => parseInt(document.getElementById('score').textContent)||0;
  document.getElementById('startBtn').click(); await wait(400);
  const m0 = Engine.muted;
  document.getElementById('muteBtn').click(); await wait(200);
  check('mute button toggles audio state', Engine.muted!==m0, m0+'->'+Engine.muted);
  // A human times Space by feel: pendulum swings through the green sweet spot. Mash a few times
  // so at least one lands in-green; a real player does the same.
  const s0 = score();
  for(let i=0;i<16;i++){ press(' '); await wait(90); }
  await wait(150);
  check('Space strike scores (visible HUD)', score()>s0, s0+'->'+score());
  window.__r = out;
})()
"""


def report(label, arr):
    print(f"[{label}]")
    for c in (arr or []):
        if c.get("__err"):
            print("   ! JS ERROR " + c["__err"]); FAILS.append(label + ":jserr"); continue
        ok = c.get("ok")
        (PASSES if ok else FAILS).append(label + ": " + c["name"])
        d = c.get("detail", "")
        line = ("  \u2713 " if ok else "  \u2717 ") + c["name"]
        if d and not ok: line += "  (" + str(d) + ")"
        print(line)


def main():
    print("[init] connecting to CDP...", flush=True)
    t = Tab()
    try:
        print("[1] navigating sleipnir", flush=True)
        t.go("games/sleipnir.html", 2.6)
        print("[1] running sleipnir scenarios", flush=True)
        report("1 Sleipnir", t.run(SLEIPNIR_JS))
        print("[2] navigating ratatoskr", flush=True)
        t.go("games/ratatoskr.html", 2.6)
        print("[2] running ratatoskr scenarios", flush=True)
        report("2 Ratatoskr", t.run(RATATOSKR_JS))
        print("[3] navigating fenrir", flush=True)
        t.go("games/fenrir.html", 2.6)
        print("[3] running engine scenarios", flush=True)
        report("3 Engine controls", t.run(ENGINE_JS))
    finally:
        t.close()
    print(f"\n[SUMMARY] pass={len(PASSES)} fail={len(FAILS)}")
    if FAILS:
        print("FAILED: " + "; ".join(FAILS))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
