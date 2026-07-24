#!/usr/bin/env python3
"""Generate the missing Sleipnir portrait set + pantheon hero banner via pollinations.ai (on-device).
Accepts JPEG or PNG from pollinations, resizes to exact convention dims, saves as PNG.
Portrait convention: 1080x1350. Banner: 1600x900. Hero: 900x1200.
"""
import os, sys, urllib.parse, urllib.request, time
from PIL import Image
from io import BytesIO

BASE = "/data/data/com.termux/files/home/storage/downloads/hermes-output"
PORTRAITS = os.path.join(BASE, "lokis-mischief-assets/portraits")
BANNERS = os.path.join(BASE, "lokis-mischief-assets/banners")
HERO = os.path.join(BASE, "lokis-assets/sleipnir")
os.makedirs(PORTRAITS, exist_ok=True)
os.makedirs(BANNERS, exist_ok=True)

VARIANTS = {
    "gold-purple": "gold (#f59e0b) rim-light and accents, deep purple (#1a1230) shadows, warm luxe palette",
    "ice-blue":    "cold ice-blue and steel palette, frost-lit, glacial highlights, silver rim-light",
    "ember-red":   "ember-red and burnt-orange fire-lit palette, glowing embers, warm infernal light",
    "verdant":     "verdant green and moss palette, natural forest light, living earth tones",
    "platinum":    "platinum and moonlight silver palette, cool luminous, pearlescent highlights",
}

COMMON = ("Sleipnir, the eight-legged horse of Odin from Norse mythology — grey otherworldly stallion "
          "with eight legs, son of Loki, the best and fastest of all horses, who carries Odin between the worlds "
          "and rides to Hel. Majestic, mythic, premium. Norse pagan, no religious iconography, no Christian or saint imagery, no halo.")

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
            im = Image.open(BytesIO(data)).convert("RGB")
            im = im.resize((w, h), Image.LANCZOS)
            im.save(path, "PNG")
            return True, os.path.getsize(path)
        except Exception as e:
            print(f"   retry {i+1}: {e}")
            time.sleep(5)
    return False, 0

def main():
    results = []
    for n, (variant, pal) in enumerate(VARIANTS.items(), 1):
        prompt = (f"Cinematic photorealistic CLOSE-UP portrait of {COMMON} "
                  f"{pal}. Dramatic volumetric lighting, shallow depth of field, film-still quality, "
                  f"hyperdetailed coat and musculature, 85mm lens, dark moody northern background. "
                  f"Luxury brand crest aesthetic.")
        out = os.path.join(PORTRAITS, f"sleipnir-{n}-{variant}.png")
        ok, sz = fetch(prompt, out, 1080, 1350, seed=7000 + n)
        results.append((out, ok, sz)); print(f"[{'OK' if ok else 'FAIL'}] {os.path.basename(out)} {sz//1024}KB")

    banner_prompt = ("Cinematic wide hero banner: Odin the Allfather astride Sleipnir, the eight-legged horse, "
                     "crossing the rainbow bridge Bifrost into Asgard at dusk. Golden light, deep purple storm sky, "
                     "mythic, premium, atmospheric, film-still quality, hyperdetailed, 24mm wide lens. "
                     "Norse pagan, no religious iconography. Gold (#f59e0b) and deep purple (#1a1230) palette.")
    out = os.path.join(BANNERS, "pantheon-hero.png")
    ok, sz = fetch(banner_prompt, out, 1600, 900, seed=8100)
    results.append((out, ok, sz)); print(f"[{'OK' if ok else 'FAIL'}] {os.path.basename(out)} {sz//1024}KB")

    hero_prompt = (f"Dark-fantasy oil painting full figure of {COMMON} "
                   "standing proud in a misty northern glade, eight legs visible, "
                   "chiaroscuro lighting, gold rim-light, rich impasto brushwork, "
                   "muted earthy palette with gold and deep purple. Premium, mythic, atmospheric.")
    out = os.path.join(HERO, "sleipnir-hero-painted.png")
    ok, sz = fetch(hero_prompt, out, 900, 1200, seed=8200)
    results.append((out, ok, sz)); print(f"[{'OK' if ok else 'FAIL'}] {os.path.basename(out)} {sz//1024}KB")

    okc = sum(1 for _, ok, _ in results if ok)
    print(f"\nDONE: {okc}/{len(results)} generated.")
    return 0 if okc == len(results) else 1

if __name__ == "__main__":
    sys.exit(main())
