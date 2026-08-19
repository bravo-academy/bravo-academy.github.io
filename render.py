#!/usr/bin/env python3
"""Bravo Academy lesson renderer — 1920×1080, Latin digits, RTL board + photo."""
from __future__ import annotations

import argparse, json, os, subprocess, tempfile, wave
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display

ROOT = Path(__file__).resolve().parent
FONTS = ROOT / "assets" / "fonts"
INK = (30, 34, 44)
PAPER = (250, 247, 240)
BLUE = (36, 99, 235)
SUN = (255, 199, 44)
CORAL = (235, 87, 74)
GREEN = (34, 168, 96)
TEAL = (16, 138, 141)
WHITE = (255, 255, 255)
STYLES = {
    "eq": dict(fill=INK, size=56),
    "op": dict(fill=CORAL, size=50),
    "ask": dict(fill=(124, 92, 214), size=46),
    "answer": dict(fill=GREEN, size=52),
    "label": dict(fill=TEAL, size=34),
    "small": dict(fill=INK, size=36),
}


def ar(t: str) -> str:
    return get_display(arabic_reshaper.reshape(str(t)))


def vfont(name: str, size: int, wght: int = 700) -> ImageFont.FreeTypeFont:
    f = ImageFont.truetype(str(FONTS / name), size)
    try:
        axes = f.get_variation_axes()
        vals = []
        for a in axes:
            nm = a["name"].decode() if isinstance(a["name"], bytes) else a["name"]
            if nm == "Weight":
                vals.append(float(wght))
            elif nm == "Slant":
                vals.append(0.0)
            elif nm == "Width":
                vals.append(100.0)
            else:
                vals.append(0.0)
        f.set_variation_by_axes(vals)
    except Exception:
        pass
    return f


def font_fit(draw, text, font_name, max_w, start, min_size=22, wght=700):
    size = start
    while size >= min_size:
        f = vfont(font_name, size, wght)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return vfont(font_name, min_size, wght)


def wav_duration(path: str) -> float:
    if path.lower().endswith(".wav"):
        with wave.open(path, "rb") as w:
            return w.getnframes() / float(w.getframerate())
    # mp3 via ffprobe
    try:
        import imageio_ffmpeg
        ff = imageio_ffmpeg.get_ffmpeg_exe()
        out = subprocess.check_output(
            [ff, "-i", path], stderr=subprocess.STDOUT, text=True
        )
    except Exception as e:
        out = str(e)
    import re
    m = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", out)
    if not m:
        return 4.0
    h, mi, s = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(s)


def rounded(im, r=28):
    mask = Image.new("L", im.size, 0)
    d = ImageDraw.Draw(mask)
    d.rounded_rectangle((0, 0, im.size[0] - 1, im.size[1] - 1), r, fill=255)
    out = im.convert("RGBA")
    out.putalpha(mask)
    return out


def draw_scene(lesson, scene, w, h):
    img = Image.new("RGB", (w, h), PAPER)
    d = ImageDraw.Draw(img)
    # grid
    for x in range(0, w, 64):
        d.line([(x, 0), (x, h)], fill=(233, 227, 214))
    for y in range(0, h, 64):
        d.line([(0, y), (w, y)], fill=(233, 227, 214))
    # top bar
    d.rounded_rectangle((24, 18, w - 24, 100), 28, fill=SUN, outline=INK, width=4)
    title = ar(lesson.get("title", ""))
    brand = ar(lesson.get("brand", "برافو أكاديمي"))
    ft = font_fit(d, title, "NotoKufiArabic.ttf", w - 280, 40, wght=900)
    d.text((w // 2, 50), title, font=ft, fill=INK, anchor="mm")
    d.rounded_rectangle((40, 32, 140, 86), 14, fill=BLUE, outline=INK, width=3)
    d.text((90, 59), f"EP {lesson.get('episode','')}", font=vfont("Fredoka.ttf", 22, 800), fill=WHITE, anchor="mm")
    # photo
    img_path = scene.get("image")
    px, py, pw, ph = 1040, 140, 840, 720
    d.rounded_rectangle((px - 8, py - 8, px + pw + 8, py + ph + 8), 32, fill=WHITE, outline=INK, width=4)
    if img_path and Path(img_path).exists():
        photo = Image.open(img_path).convert("RGB")
        photo = photo.resize((pw, ph), Image.LANCZOS)
        img.paste(rounded(photo, 24), (px, py), rounded(photo, 24))
    else:
        d.rounded_rectangle((px, py, px + pw, py + ph), 24, fill=(220, 230, 250))
    cap = scene.get("caption")
    if cap:
        d.rounded_rectangle((px, py + ph - 70, px + pw, py + ph), 0, fill=(30, 34, 44, ))
        d.rectangle((px, py + ph - 70, px + pw, py + ph), fill=INK)
        cf = font_fit(d, ar(cap), "NotoSansArabic.ttf", pw - 24, 28)
        d.text((px + pw // 2, py + ph - 35), ar(cap), font=cf, fill=WHITE, anchor="mm")
    # board
    bx, by, bw, bh = 40, 140, 960, 800
    d.rounded_rectangle((bx, by, bx + bw, by + bh), 28, fill=WHITE, outline=INK, width=4)
    bt = scene.get("board_title", "")
    if bt:
        d.rounded_rectangle((bx + 24, by + 20, bx + 420, by + 78), 18, fill=TEAL, outline=INK, width=3)
        d.text((bx + 222, by + 49), ar(bt), font=vfont("NotoKufiArabic.ttf", 26, 800), fill=WHITE, anchor="mm")
    y = by + 110
    for line in scene.get("lines", []):
        text = str(line.get("text", ""))
        style = STYLES.get(line.get("style", "small"), STYLES["small"])
        # keep Latin digits as-is; reshape if Arabic letters present
        shown = ar(text) if any("\u0600" <= c <= "\u06FF" for c in text) else text
        fname = "Amiri-Bold.ttf" if line.get("style") == "eq" else "NotoSansArabic.ttf"
        f = font_fit(d, shown, fname, bw - 80, style["size"])
        d.text((bx + bw // 2, y), shown, font=f, fill=style["fill"], anchor="mm")
        if line.get("style") == "answer":
            d.ellipse((bx + 80, y - 40, bx + bw - 80, y + 40), outline=GREEN, width=5)
        y += 78
    # footer brand
    d.text((w // 2, h - 36), brand, font=vfont("NotoSansArabic.ttf", 24, 700), fill=BLUE, anchor="mm")
    if scene.get("confetti"):
        import random
        rnd = random.Random(7)
        cols = [SUN, CORAL, GREEN, BLUE, TEAL]
        for _ in range(80):
            x = rnd.randint(0, w)
            yy = rnd.randint(0, h)
            d.ellipse((x, yy, x + 14, yy + 14), fill=rnd.choice(cols))
    return img


def write_srt(scenes_meta, path):
    def ts(t):
        h = int(t // 3600)
        m = int((t % 3600) // 60)
        s = t % 60
        return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")

    t = 0.0
    lines = []
    i = 1
    for sc, dur in scenes_meta:
        narr = sc.get("narration", "").strip()
        if narr:
            lines.append(f"{i}\n{ts(t)} --> {ts(t + dur)}\n{narr}\n")
            i += 1
        t += dur
    Path(path).write_text("\n".join(lines), encoding="utf-8")


def concat_audio(paths, dest, ffmpeg):
    lst = dest + ".txt"
    with open(lst, "w") as f:
        for p in paths:
            f.write(f"file '{os.path.abspath(p)}'\n")
    subprocess.check_call(
        [ffmpeg, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", dest],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def render(lesson_path: Path, out_mp4: Path, intro=False):
    import imageio_ffmpeg
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    lesson = json.loads(lesson_path.read_text(encoding="utf-8"))
    w, h, fps = lesson.get("width", 1920), lesson.get("height", 1080), lesson.get("fps", 24)
    base = lesson_path.parent.parent
    # resolve relative media
    for sc in lesson["scenes"]:
        for key in ("image", "audio"):
            if sc.get(key) and not os.path.isabs(sc[key]):
                cand = (lesson_path.parent / sc[key]).resolve()
                if cand.exists():
                    sc[key] = str(cand)
                else:
                    sc[key] = str((base / sc[key]).resolve()) if (base / sc[key]).exists() else str(cand)

    tmp = Path(tempfile.mkdtemp(prefix="bravo_"))
    frames_dir = tmp / "frames"
    frames_dir.mkdir()
    audios = []
    meta = []
    n = 0
    if intro:
        intro_img = Image.new("RGB", (w, h), PAPER)
        logo = ROOT / "assets/brand/logo.png"
        if logo.exists():
            L = Image.open(logo).convert("RGB").resize((420, 420), Image.LANCZOS)
            intro_img.paste(L, ((w - 420) // 2, 180))
        d = ImageDraw.Draw(intro_img)
        d.text((w // 2, 680), ar(lesson.get("brand", "برافو أكاديمي")), font=vfont("NotoKufiArabic.ttf", 48, 900), fill=BLUE, anchor="mm")
        d.text((w // 2, 760), ar(lesson.get("title", "")), font=vfont("NotoSansArabic.ttf", 36, 700), fill=INK, anchor="mm")
        p = frames_dir / f"{n:05d}.png"
        intro_img.save(p)
        n += 1
        # 3.2s silence
        sil = tmp / "sil.wav"
        subprocess.check_call(
            [ffmpeg, "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", "3.2", sil],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        audios.append(str(sil))
        meta.append(({"narration": ""}, 3.2))

    for sc in lesson["scenes"]:
        frame = draw_scene(lesson, sc, w, h)
        fp = frames_dir / f"{n:05d}.png"
        frame.save(fp)
        n += 1
        ap = sc.get("audio")
        if ap and Path(ap).exists():
            dur = wav_duration(ap)
            audios.append(ap)
        else:
            dur = 5.0
            sil = tmp / f"sil{n}.wav"
            subprocess.check_call(
                [ffmpeg, "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", str(dur), sil],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            audios.append(str(sil))
        meta.append((sc, dur))

    # expand frames by duration using concat demuxer of stills
    concat = tmp / "slides.txt"
    with open(concat, "w") as f:
        idx = 0
        for sc, dur in meta:
            f.write(f"file '{frames_dir / f'{idx:05d}.png'}'\n")
            f.write(f"duration {dur:.3f}\n")
            idx += 1
        f.write(f"file '{frames_dir / f'{idx-1:05d}.png'}'\n")

    audio_all = tmp / "all.wav"
    # re-encode concat audio to wav
    lst = tmp / "alist.txt"
    with open(lst, "w") as f:
        for p in audios:
            f.write(f"file '{os.path.abspath(p)}'\n")
    subprocess.check_call(
        [ffmpeg, "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c:a", "pcm_s16le", str(audio_all)],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    out_mp4.parent.mkdir(parents=True, exist_ok=True)
    subprocess.check_call(
        [
            ffmpeg, "-y", "-f", "concat", "-safe", "0", "-i", str(concat),
            "-i", str(audio_all), "-r", str(fps), "-pix_fmt", "yuv420p",
            "-c:v", "libx264", "-c:a", "aac", "-shortest", str(out_mp4),
        ],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    srt = out_mp4.with_suffix(".srt")
    write_srt(meta, srt)
    print("wrote", out_mp4, srt)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--lesson", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--intro", action="store_true")
    args = p.parse_args()
    render(Path(args.lesson), Path(args.out), intro=args.intro)


if __name__ == "__main__":
    main()
