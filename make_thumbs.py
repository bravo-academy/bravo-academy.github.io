#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import json

ROOT = Path(__file__).resolve().parent
FONTS = ROOT / "assets/fonts"


def ar(t):
    return get_display(arabic_reshaper.reshape(t))


def main():
    for lesson in ROOT.glob("levels/*/*/lessons/*.json"):
        data = json.loads(lesson.read_text(encoding="utf-8"))
        out = lesson.parent.parent / "out" / "thumbs" / f"{lesson.stem}.jpg"
        out.parent.mkdir(parents=True, exist_ok=True)
        img = Image.new("RGB", (1280, 720), (255, 199, 44))
        d = ImageDraw.Draw(img)
        d.rounded_rectangle((30, 30, 1250, 690), 28, outline=(30, 34, 44), width=8)
        f = ImageFont.truetype(str(FONTS / "NotoKufiArabic.ttf"), 64)
        d.text((640, 280), ar(data.get("title", "")), font=f, fill=(31, 78, 140), anchor="mm")
        f2 = ImageFont.truetype(str(FONTS / "NotoSansArabic.ttf"), 36)
        d.text((640, 420), ar(data.get("brand", "")), font=f2, fill=(30, 34, 44), anchor="mm")
        img.save(out, quality=90)
        print(out)


if __name__ == "__main__":
    main()
