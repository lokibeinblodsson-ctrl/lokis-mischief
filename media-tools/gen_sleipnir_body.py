#!/usr/bin/env python3
"""Generate a clean side-profile Sleipnir body (4 legs) meant as a base for SVG 8-leg compositing.
Plain dark background, full side view, legs clearly separated, no text, no extra limbs.
"""
import os, urllib.parse, urllib.request, time
from PIL import Image
from io import BytesIO

BASE = "/data/data/com.termux/files/home/storage/downloads/hermes-output"
OUT = os.path.join(BASE, "lokis-assets/sleipnir")
os.makedirs(OUT, exist_ok=True)

def url(prompt, w, h, seed):
    p = urllib.parse.quote(prompt, safe="")
    return f"https://image.pollinations.ai/prompt/{p}?width={w}&height={h}&seed={seed}&nologo=true&model=flux&enhance=false"

def fetch(prompt, path, w, h, seed, tries=6):
    for i in range(tries):
        try:
            req = urllib.request.Request(url(prompt, w, h, seed), headers={"User-Agent": "Mozilla/5.0"})
            data = urllib.request.urlopen(req, timeout=180).read()
            if len(data) < 4000:
                time.sleep(3); continue
            im = Image.open(BytesIO(data)).convert("RGB").resize((w, h), Image.LANCZOS)
            im.save(path, "PNG")
            return True, os.path.getsize(path)
        except Exception as e:
            print(f"   retry {i+1}: {e}"); time.sleep(5)
    return False, 0

# Side profile, plain flat background, legs spread for clarity
prompt = ("Full side-profile view of a single grey draft horse standing still on a PLAIN SOLID DARK GREY "
          "studio background, legs slightly apart so all four are clearly separated, head turned slightly toward "
          "viewer. Clean product-shot lighting, neutral, no props, no text, no harness, no extra limbs. "
          "Photorealistic, sharp, high detail.")
path = os.path.join(OUT, "sleipnir-body-base.png")
ok, sz = fetch(prompt, path, 1200, 1200, seed=5500)
print(f"[{'OK' if ok else 'FAIL'}] {os.path.basename(path)} {sz//1024}KB")
