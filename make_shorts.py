#!/usr/bin/env python3
"""Make a 9:16 still+audio short from the quiz/last scene of a lesson."""
import argparse, json, subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import imageio_ffmpeg

ROOT = Path(__file__).resolve().parent
FONTS = ROOT / "assets/fonts"


def ar(t):
    return get_display(arabic_reshaper.reshape(str(t)))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--lesson", required=True)
    args = p.parse_args()
    lesson = Path(args.lesson)
    data = json.loads(lesson.read_text(encoding="utf-8"))
    sc = data["scenes"][-1]
    w, h = 1080, 1920
    img = Image.new("RGB", (w, h), (250, 247, 240))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((40, 80, w - 40, 280), 30, fill=(255, 199, 44), outline=(30, 34, 44), width=6)
    f = ImageFont.truetype(str(FONTS / "NotoKufiArabic.ttf"), 48)
    d.text((w // 2, 180), ar(data.get("title", "")), font=f, fill=(30, 34, 44), anchor="mm")
    # حلّ مسار الصورة بمرونة (يدعم ../img/.. أو مسار نسبي)
    raw_img = sc.get("image", "")
    photo = None
    if raw_img:
        candidate = (lesson.parent / raw_img).resolve()
        if candidate.exists():
            photo = candidate
        else:
            # fallback للتوافق مع البناء القديم: levels/g3/<subject>/img/..
            alt = (lesson.parent.parent / raw_img.replace("../", "")).resolve()
            if alt.exists():
                photo = alt
    if photo and photo.exists():
        ph = Image.open(photo).convert("RGB").resize((900, 700), Image.LANCZOS)
        img.paste(ph, (90, 340))
    y = 1120
    f2 = ImageFont.truetype(str(FONTS / "NotoSansArabic.ttf"), 40)
    for line in sc.get("lines", []):
        t = line.get("text", "")
        shown = ar(t) if any("\u0600" <= c <= "\u06FF" for c in t) else t
        d.text((w // 2, y), shown, font=f2, fill=(30, 34, 44), anchor="mm")
        y += 70
    tmp = Path("/tmp/short_frame.png")
    img.save(tmp)
    out = lesson.parent.parent / "out" / "shorts" / f"{lesson.stem}_short.mp4"
    out.parent.mkdir(parents=True, exist_ok=True)
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    raw_audio = sc.get("audio", "")
    audio = (lesson.parent / raw_audio).resolve() if raw_audio else None
    has_audio = audio and audio.exists()
    cmd = [ff, "-y", "-loop", "1", "-i", str(tmp), "-t", "12", "-vf", "format=yuv420p", "-c:v", "libx264"]
    if has_audio:
        cmd = [ff, "-y", "-loop", "1", "-i", str(tmp), "-i", str(audio), "-shortest", "-vf", "format=yuv420p", "-c:v", "libx264", "-c:a", "aac"]
    cmd.append(str(out))
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(out)


if __name__ == "__main__":
    main()
