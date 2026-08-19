#!/usr/bin/env python3
import json, os, subprocess
from pathlib import Path
import imageio_ffmpeg

ROOT=Path("/tmp/repo")
FF=imageio_ffmpeg.get_ffmpeg_exe()

def generate_tts(text, lang, out_path):
    out_path=Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # try gTTS
    try:
        from gtts import gTTS
        tts=gTTS(text=text, lang=lang, slow=False)
        tmp=str(out_path.with_suffix(".tmp.mp3"))
        tts.save(tmp)
        # convert to consistent format via ffmpeg (normalize)
        subprocess.check_call([FF,"-y","-i",tmp,"-ar","24000","-ac","1","-b:a","64k",str(out_path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.remove(tmp)
        print(f"tts ok {out_path} lang={lang} chars={len(text)}")
        return True
    except Exception as e:
        print(f"gtts failed {out_path} {e} -> fallback silence")
        # fallback silence duration estimated
        dur=max(3.5, len(text)/13.0 + 0.8)  # approximate
        # generate silent mp3
        subprocess.check_call([FF,"-y","-f","lavfi","-i","anullsrc=r=24000:cl=mono","-t",f"{dur:.2f}","-q:a","9","-acodec","libmp3lame",str(out_path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return False

# iterate over lessons
for lesson_path in sorted(ROOT.glob("levels/g3/*/lessons/*.json")):
    data=json.loads(lesson_path.read_text(encoding="utf-8"))
    subj=data.get("subject","")
    # language: french if subject french else arabic
    lang="fr" if subj=="french" else "ar"
    # For French, gTTS fr, for Arabic ar
    for scene in data["scenes"]:
        ap=scene.get("audio")
        if not ap: continue
        # resolve path
        full=(lesson_path.parent / ap).resolve()
        # also handle base/../
        if not str(full).startswith(str(ROOT)):
            # try base
            full=(lesson_path.parent.parent / ap.replace("../","")).resolve()
        text=scene.get("narration","")
        if not text: continue
        generate_tts(text, lang, full)
print("done audio generation")

# also generate placeholder images for missing
from PIL import Image, ImageDraw, ImageFont
FONTS=ROOT/"assets/fonts"
def ar(t):
    import arabic_reshaper
    from bidi.algorithm import get_display
    if any("\u0600" <= c <= "\u06FF" for c in t):
        return get_display(arabic_reshaper.reshape(t))
    return t
def make_placeholder(path, title, caption):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    if Path(path).exists():
        return
    img=Image.new("RGB",(1280,720),(250,247,240))
    d=ImageDraw.Draw(img)
    # grid
    for x in range(0,1280,64):
        d.line([(x,0),(x,720)], fill=(233,227,214))
    f1=ImageFont.truetype(str(FONTS/"NotoKufiArabic.ttf"),48)
    f2=ImageFont.truetype(str(FONTS/"NotoSansArabic.ttf"),32)
    d.rounded_rectangle((40,40,1240,180),20,fill=(255,199,44), outline=(30,34,44), width=4)
    d.text((640,110), ar(title), font=f1, fill=(30,34,44), anchor="mm")
    d.text((640,360), ar(caption or "برافو أكاديمي"), font=f2, fill=(16,138,141), anchor="mm")
    # mascot
    d.ellipse((1140-130,720-150,1140,720-20), fill=(255,199,44), outline=(30,34,44), width=4)
    d.text((1140-65,720-85), "★", font=ImageFont.truetype(str(FONTS/"Fredoka.ttf"),48), fill=(30,34,44), anchor="mm")
    img.save(path, quality=90)
    print(f"placeholder img {path}")

for lesson_path in sorted(ROOT.glob("levels/g3/*/lessons/*.json")):
    data=json.loads(lesson_path.read_text(encoding="utf-8"))
    for scene in data["scenes"]:
        ip=scene.get("image")
        if not ip: continue
        full=(lesson_path.parent / ip).resolve()
        if not full.exists():
            # create placeholder
            make_placeholder(full, data.get("title",""), scene.get("caption",""))
print("image placeholders done")
