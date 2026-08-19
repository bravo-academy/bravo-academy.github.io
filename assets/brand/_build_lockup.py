#!/usr/bin/env python3
"""Build Bravo Academy vertical lockup — small mascot, BIG name, gap ≥130px."""
import os, math
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import arabic_reshaper
from bidi.algorithm import get_display

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "..", "fonts")
BLUE = (31, 78, 140)
BLUE_B = (46, 123, 214)
GOLD = (255, 179, 0)
RED = (232, 69, 60)
GREEN = (43, 182, 115)
PURPLE = (123, 94, 167)
INK = (28, 34, 54)
WHITE = (255, 255, 255)
BRAVO_COLORS = [BLUE_B, RED, GOLD, GREEN, PURPLE]


def vfont(name, size, wght=None):
    f = ImageFont.truetype(os.path.join(FONTS, name), size)
    try:
        axes = f.get_variation_axes()
        vals = []
        for a in axes:
            nm = a["name"].decode() if isinstance(a["name"], bytes) else a["name"]
            if nm == "Weight":
                vals.append(float(wght if wght else 700))
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


def ar(t):
    return get_display(arabic_reshaper.reshape(t))


def trim_white(im, pad=0, thresh=245):
    a = np.asarray(im.convert("RGB"))
    mask = (a < thresh).any(axis=2)
    ys, xs = np.where(mask)
    x0, x1 = max(xs.min() - pad, 0), min(xs.max() + pad, im.width)
    y0, y1 = max(ys.min() - pad, 0), min(ys.max() + pad, im.height)
    return im.crop((x0, y0, x1, y1))


def wordmark(text, size, spacing=0.05, stroke=0, per_letter=True):
    letters = list(text)
    f = vfont("Fredoka.ttf", size, wght=700)
    meas = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    widths = [meas.textlength(L, font=f) for L in letters]
    adv = max(widths) * spacing
    total_w = sum(widths) + adv * (len(letters) - 1)
    h = f.size
    img = Image.new("RGBA", (int(total_w) + stroke * 2 + 6, h + stroke * 2 + 6), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    x = 0
    for i, L in enumerate(letters):
        col = BRAVO_COLORS[i % len(BRAVO_COLORS)] if (per_letter and L != " ") else BLUE
        d.text((x, stroke), L, font=f, fill=col, anchor="lm", stroke_width=stroke, stroke_fill=INK)
        x += widths[i] + adv
    bb = img.getbbox()
    return img.crop(bb) if bb else img


def draw_text(d, xy, txt, font, fill, anchor="mm", stroke=0, stroke_fill=INK, shadow=0):
    x, y = xy
    if shadow:
        d.text((x + shadow, y + shadow + 1), txt, font=font, fill=(0, 0, 0),
               anchor=anchor, stroke_width=stroke, stroke_fill=(0, 0, 0))
    d.text((x, y), txt, font=font, fill=fill, anchor=anchor,
           stroke_width=stroke, stroke_fill=stroke_fill)


def star(size, col):
    s = Image.new("RGBA", (size * 2, size * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(s)
    pts = []
    for k in range(10):
        ang = -math.pi / 2 + k * math.pi / 5
        rr = size if k % 2 == 0 else size * 0.45
        pts.append((size + rr * math.cos(ang), size + rr * math.sin(ang)))
    d.polygon(pts, fill=col + (235,))
    return s


def measure_gap(path):
    im = Image.open(path).convert("RGB")
    a = np.asarray(im)
    gold = (a[:, :, 0] > 180) & (a[:, :, 1] > 120) & (a[:, :, 1] < 220) & (a[:, :, 2] < 80)
    blue = (a[:, :, 2] > 90) & (a[:, :, 0] < 80) & (a[:, :, 1] < 140)
    gold_rows = np.where(gold.any(axis=1))[0]
    blue_rows = np.where(blue.any(axis=1))[0]
    if len(gold_rows) == 0 or len(blue_rows) == 0:
        return None
    mascot_max = gold_rows[gold_rows < 700].max() if (gold_rows < 700).any() else gold_rows.max()
    name_min = blue_rows[blue_rows > mascot_max].min() if (blue_rows > mascot_max).any() else blue_rows.min()
    return int(name_min - mascot_max), int(mascot_max), int(name_min)


def build_lockup():
    W = H = 1024
    canvas = Image.new("RGB", (W, H), WHITE)
    cx = W // 2
    masc = trim_white(Image.open(os.path.join(HERE, "_mascot.png")).convert("RGB"), pad=8)
    mw = 320
    mh = int(masc.height * mw / masc.width)
    masc = masc.resize((mw, mh), Image.LANCZOS)
    title = "برافو أكاديمي"
    f_title = vfont("NotoKufiArabic.ttf", 168, wght=900)
    arabic_h = 180
    div_h = 12
    wm = wordmark("BRAVO ACADEMY", size=62, spacing=0.06, stroke=5, per_letter=True)
    lat_h = wm.height
    gap_mascot_arabic = 150
    gap_arabic_div = 28
    gap_div_lat = 24
    group_h = mh + gap_mascot_arabic + arabic_h + gap_arabic_div + div_h + gap_div_lat + lat_h
    y = max(24, (H - group_h) // 2)
    canvas.paste(masc, (cx - mw // 2, y))
    mascot_bottom = y + mh
    y += mh + gap_mascot_arabic
    name_top = y
    d = ImageDraw.Draw(canvas)
    draw_text(d, (cx, y + arabic_h / 2), ar(title), f_title, BLUE,
              anchor="mm", stroke=9, stroke_fill=WHITE, shadow=3)
    y += arabic_h + gap_arabic_div
    divw = 300
    d.rounded_rectangle((cx - divw / 2, y, cx + divw / 2, y + div_h), radius=6, fill=GOLD)
    ls = star(18, RED)
    canvas.paste(ls, (int(cx - divw / 2 - 40), int(y - 12)), ls)
    rs = star(18, GREEN)
    canvas.paste(rs, (int(cx + divw / 2 + 4), int(y - 12)), rs)
    y += div_h + gap_div_lat
    canvas.paste(wm, (cx - wm.width // 2, int(y)), wm)
    out = os.path.join(HERE, "logo_bravo.png")
    canvas.save(out)
    planned = name_top - mascot_bottom
    print(f"planned gap={planned}px mascot_bottom={mascot_bottom} name_top={name_top}")
    print(f"layout gap (name_top - mascot_bottom) = {planned}px  [accept ≥130]")
    if planned < 130:
        raise SystemExit(f"FAIL layout gap {planned} < 130")


def build_mark():
    S = 1024
    canvas = Image.new("RGB", (S, S), WHITE)
    masc = trim_white(Image.open(os.path.join(HERE, "_mascot.png")).convert("RGB"), pad=8)
    mw = 640
    mh = int(masc.height * mw / masc.width)
    masc = masc.resize((mw, mh), Image.LANCZOS)
    mx = (S - mw) // 2
    my = 80
    canvas.paste(masc, (mx, my))
    wm = wordmark("BRAVO", size=160, spacing=0.03, stroke=10, per_letter=True)
    wx = (S - wm.width) // 2
    wy = my + mh + 8
    canvas.paste(wm, (wx, wy), wm)
    d = ImageDraw.Draw(canvas)
    draw_text(d, (S // 2, wy + wm.height + 20), "A C A D E M Y",
              vfont("Fredoka.ttf", 52, wght=600), BLUE, anchor="mm")
    canvas.save(os.path.join(HERE, "logo.png"))


def build_banner():
    W, H = 2560, 1440
    img = Image.new("RGB", (W, H), (255, 247, 230))
    d = ImageDraw.Draw(img)
    for i in range(H):
        t = i / H
        r = int(255 - 20 * t)
        g = int(247 - 40 * t)
        b = int(230 + 10 * t)
        d.line([(0, i), (W, i)], fill=(r, g, b))
    # TV-safe box visualization not drawn as UI — content centered in x[507–2053] y[508–931]
    masc = trim_white(Image.open(os.path.join(HERE, "_mascot.png")).convert("RGB"), pad=6)
    mw = 280
    mh = int(masc.height * mw / masc.width)
    safe_cx, safe_cy = (507 + 2053) // 2, (508 + 931) // 2
    img.paste(masc.resize((mw, mh), Image.LANCZOS), (safe_cx - 620, safe_cy - mh // 2))
    f1 = vfont("NotoKufiArabic.ttf", 92, wght=900)
    f2 = vfont("NotoSansArabic.ttf", 42, wght=700)
    f3 = vfont("Fredoka.ttf", 40, wght=700)
    draw_text(d, (safe_cx + 80, safe_cy - 70), ar("برافو أكاديمي"), f1, BLUE,
              stroke=6, stroke_fill=WHITE, shadow=3)
    draw_text(d, (safe_cx + 80, safe_cy + 20), ar("كل الابتدائي · 6 مستويات"), f2, (232, 69, 60))
    draw_text(d, (safe_cx + 80, safe_cy + 80), "@BravoAcademyTN", f3, BLUE)
    draw_text(d, (safe_cx + 80, safe_cy + 140), ar("رياضيات · عربية · إيقاظ · فرنسية · إسلامية · مدنية"), f2, (31, 78, 140))
    img.save(os.path.join(HERE, "banner_bravo.jpg"), quality=92)
    print("saved banner", img.size)


if __name__ == "__main__":
    build_lockup()
    build_mark()
    build_banner()
    print("DONE")
