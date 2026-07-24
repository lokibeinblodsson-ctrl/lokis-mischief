#!/usr/bin/env python3
"""Regenerate pantheon hero banner + painted Sleipnir hero with correct 8 legs, rainbow Bifrost,
and a text-safe dark top zone for headline overlay."""
import os, sys, urllib.parse, urllib.request, time
from PIL import Image
from io import BytesIO

BASE = "/data/data/com.termux/files/home/storage/downloads/hermes-output"
BANNERS = os.path.join(BASE, "lokis-mischief-assets/banners")
HERO = os.path.join(BASE, "lokis-assets/sleipnir")
os.makedirs(BANNERS, exist_ok=True); os.makedirs(HERO, exist_ok=True)

def url(prompt, w, h, seed):
    p = urllib.parse.quote(prompt, safe="")
    return f"https://image.pollinations.ai/prompt/{p}?width={w}&height={h}&seed={seed}&nologo=true&model=flux&enhance=false"

def fetch(prompt, path, w, h, seed, tries=5):
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

results = []

# Banner: rainbow Bifrost, eight-legged Sleipnir, Odin, text-safe dark top
banner_prompt = ("Ultra-wide cinematic fantasy hero banner. ODIN, a one-eyed bearded Norse king in a wide-brimmed "
                 "hat and raven-feather cloak, rides SLEIPNIR — a massive grey horse with EIGHT clearly visible legs "
                 "(four pairs) — across the BIFROST, a glowing RAINBOW bridge of shimmering spectral light into Asgard. "
                 "Deep purple (#1a1230) storm sky. The UPPER THIRD of the image is mostly empty dark purple sky with "
                 "minimal detail for a headline. Subject sits in the lower two-thirds. Gold (#f59e0b) volumetric light, "
                 "hyperdetailed, film-still, 24mm lens. Norse pagan, no text, no religious iconography.")
out = os.path.join(BANNERS, "pantheon-hero.png")
ok, sz = fetch(banner_prompt, out, 1600, 900, seed=9100)
results.append((out, ok, sz)); print(f"[{'OK' if ok else 'FAIL'}] {os.path.basename(out)} {sz//1024}KB")

# Painted full-figure Sleipnir with eight legs
hero_prompt = ("Dark-fantasy oil painting FULL FIGURE of Sleipnir, the eight-legged horse of Odin from Norse mythology "
               "— a majestic grey stallion with EIGHT clearly visible legs (four pairs), standing proud in a misty "
               "northern glade at dusk. Chiaroscuro lighting, gold (#f59e0b) rim-light, rich impasto brushwork, deep "
               "purple (#1a1230) shadows, muted earthy palette. Premium, mythic, atmospheric. No text.")
out = os.path.join(HERO, "sleipnir-hero-painted.png")
ok, sz = fetch(hero_prompt, out, 900, 1200, seed=9200)
results.append((out, ok, sz)); print(f"[{'OK' if ok else 'FAIL'}] {os.path.basename(out)} {sz//1024}KB")

okc = sum(1 for _, ok, _ in results if ok)
print(f"\nDONE: {okc}/{len(results)}")
sys.exit(0 if okc == len(results) else 1)
