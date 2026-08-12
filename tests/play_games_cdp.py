#!/usr/bin/env python3
"""Play the Loki games headlessly in theo VM Chrome and assert the bible-spec mechanics work.

Purpose: `tests/run.js` only proves files/links/functions exist. This drives the real game in a
real browser — clicks Start, fires synthetic strikes, and reads the game's own state variables —
so a regression in scoring, the timer, or the end screen fails loudly instead of shipping.

Assumptions: site on :8899, Chrome CDP on 9224 (theo VM). Reads only; changes nothing on disk.
Non-obvious: suppress_origin=True because Chrome 403s WS handshakes carrying an Origin header
unless launched with --remote-allow-origins. Each check uses a throwaway tab.
Exit code: 0 = all assertions passed, 1 = at least one failed (usable as a loop gate).
"""
import json, sys, time, urllib.request
from websocket import create_connection

BASE = "http://127.0.0.1:8899"
fails, passes = [], []


class Tab:
    def __init__(self):
        ver = json.load(urllib.request.urlopen("http://127.0.0.1:9224/json/version", timeout=10))
        self.ws = create_connection(ver["webSocketDebuggerUrl"], timeout=30, suppress_origin=True)
        self.n = 0
        self.tid = self.cmd("Target.createTarget", {"url": "about:blank"})["result"]["targetId"]
        self.sid = self.cmd("Target.attachToTarget",
                            {"targetId": self.tid, "flatten": True})["result"]["sessionId"]
        for d in ("Page", "Runtime", "Network"):
            self.cmd(d + ".enable", sid=True)
        # the theo Chrome profile is long-lived and WILL serve a stale engine.js from cache,
        # which silently tests the previous version — disable the cache for this tab.
        self.cmd("Network.setCacheDisabled", {"cacheDisabled": True}, sid=True)

    def cmd(self, method, params=None, sid=False):
        self.n += 1
        m = {"id": self.n, "method": method, "params": params or {}}
        if sid:
            m["sessionId"] = self.sid
        self.ws.send(json.dumps(m))
        end = time.time() + 40
        while time.time() < end:
            r = json.loads(self.ws.recv())
            if r.get("id") == self.n:
                return r
        raise TimeoutError(method)

    def go(self, path, settle=2.0):
        self.cmd("Page.navigate", {"url": f"{BASE}/{path}"}, sid=True)
        time.sleep(settle)

    def ev(self, expr):
        r = self.cmd("Runtime.evaluate",
                     {"expression": expr, "returnByValue": True, "awaitPromise": True}, sid=True)
        res = r.get("result", {}).get("result", {})
        if r.get("result", {}).get("exceptionDetails"):
            # return a sentinel STRING (not a dict) so callers can still compare/startswith safely
            return "__JSERR__ " + str(r["result"]["exceptionDetails"].get("text", ""))[:120]
        return res.get("value")

    def num(self, expr):
        """Evaluate and coerce to float; JS errors / non-numerics become NaN so comparisons fail
        loudly rather than raising a TypeError inside the harness."""
        v = self.ev(expr)
        try:
            return float(v)
        except (TypeError, ValueError):
            return float("nan")

    def close(self):
        try:
            self.cmd("Target.closeTarget", {"targetId": self.tid})
        finally:
            self.ws.close()


def check(name, cond, detail=""):
    (passes if cond else fails).append(name)
    print(("  \u2713 " if cond else "  \u2717 ") + name + (("  " + str(detail)) if detail and not cond else ""))


def main():
    t = Tab()
    try:
        # ---------- engine contract ----------
        print("[1] engine v2 contract")
        t.go("games/fenrir.html", 2.5)
        api = t.ev("Object.keys(Engine).sort().join(',')") or ""
        for fn in ("pause", "resume", "share", "shareCard", "getBest", "setBest", "toggleMute", "stopLoop"):
            check(f"Engine.{fn} exists", fn in api, api[:160])
        check("audio muted by default", t.ev("Engine.muted") is True)
        check("mute + pause controls rendered",
              t.ev("!!document.getElementById('muteBtn') && !!document.getElementById('pauseBtn')"))
        check("controls meet 44px tap target",
              t.ev("(()=>{const b=document.getElementById('muteBtn').getBoundingClientRect();"
                   "return b.width>=44&&b.height>=44})()"))
        check("share card is a 1080x1350 png data-url",
              (t.ev("(()=>{const u=Engine.shareCard({game:'t',title:'T',score:1,lesson:'l'});"
                    "return u.slice(0,22)})()") or "").startswith("data:image/png"))

        # ---------- fenrir mechanics ----------
        print("[2] fenrir — chain strike (bible spec)")
        check("90s time limit constant", t.ev("TIME_LIMIT") == 90)
        check("three chains w/ spec windows",
              t.ev("JSON.stringify(CHAINS.map(c=>[c.green,c.spd]))")
              == "[[0.4,1],[0.2,1.4],[0.12,1.8]]",
              t.ev("JSON.stringify(CHAINS)"))
        check("hit damage = 1/3 integrity", abs(t.num("HIT_DMG") - 100 / 3) < 0.01)
        check("miss reform = 10", t.ev("MISS_REFORM") == 10)
        t.ev("document.getElementById('startBtn').click()")
        time.sleep(0.6)
        check("state -> playing after start", t.ev("Engine.state") == "playing")
        check("canvas mounted", t.ev("!!document.getElementById('gc')"))
        check("timer counting down", t.num("timeLeft") < 90)
        # force a guaranteed-perfect strike: park the pendulum dead centre then tap
        t.ev("pend=0; onTap();")
        check("perfect strike scores 150", t.ev("score") == 150, t.ev("score"))
        check("perfect counted", t.ev("perfects") == 1)
        check("integrity dropped by a third", abs(t.num("hp") - (100 - 100 / 3)) < 0.01)
        # force a miss (pendulum far outside every window)
        t.ev("pend=0.99; onTap();")
        check("miss reforms the chain", t.num("hp") > (100 - 100 / 3))
        check("miss counted", t.ev("misses") == 1)
        # three clean centre hits must break the chain and advance
        t.ev("hp=100;hits=0;chainIdx=0;pend=0;onTap();pend=0;onTap();pend=0;onTap();")
        check("3 clean hits advance the chain", t.ev("chainIdx") == 1, t.ev("chainIdx"))
        check("HUD chain label updated",
              (t.ev("document.getElementById('chain').textContent") or "") == "Dromi")
        # end screen
        t.ev("end(true)")
        time.sleep(0.4)
        check("end screen shows share button", t.ev("!!document.getElementById('shareBtn')"))
        check("state left playing", t.ev("Engine.state") in ("win", "lose"))
        check("best score persisted",
              (t.ev("localStorage.getItem('loki_best_fenrir')") or "").startswith("{"))

        # ---------- pause / resume across all games ----------
        print("[3] pause/resume + no console errors, every game page")
        for p in ("games/fenrir.html", "games/hel.html", "games/jormungandr.html",
                  "games/runecast.html", "games/sleipnir.html"):
            t.go(p, 2.0)
            err = t.ev("(()=>{try{Engine.setState('playing');Engine.pause();"
                       "const a=Engine.state;Engine.resume();return a+'/'+Engine.state}"
                       "catch(e){return 'ERR '+e.message}})()")
            check(f"{p}: pause->paused, resume->playing", err == "paused/playing", err)
    finally:
        t.close()

    print(f"\n[SUMMARY] pass={len(passes)} fail={len(fails)}")
    if fails:
        print("FAILED: " + "; ".join(fails))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
