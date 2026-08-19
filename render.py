#!/usr/bin/env python3
"""Bravo Academy lesson renderer — 1920×1080, step-by-step reveal, mascot gap ≥130px, pauses."""
from __future__ import annotations
import argparse, json, os, subprocess, tempfile, wave, re
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
# mascot gap
MASCOT_GAP = 140
# extra bottom safe zone for watermark
BOTTOM_SAFE = 140
STYLES = {
    "eq": dict(fill=INK, size=56),
    "op": dict(fill=CORAL, size=50),
    "ask": dict(fill=(124, 92, 214), size=44),
    "answer": dict(fill=GREEN, size=50),
    "label": dict(fill=TEAL, size=34),
    "small": dict(fill=INK, size=36),
}

def ar(t: str) -> str:
    s=str(t)
    # if contains Arabic, reshape
    if any("\u0600" <= c <= "\u06FF" for c in s):
        return get_display(arabic_reshaper.reshape(s))
    return s

def vfont(name: str, size: int, wght: int = 700) -> ImageFont.FreeTypeFont:
    f = ImageFont.truetype(str(FONTS / name), size)
    try:
        axes = f.get_variation_axes()
        vals=[]
        for a in axes:
            nm=a["name"].decode() if isinstance(a["name"], bytes) else a["name"]
            if nm=="Weight": vals.append(float(wght))
            elif nm=="Slant": vals.append(0.0)
            elif nm=="Width": vals.append(100.0)
            else: vals.append(0.0)
        f.set_variation_by_axes(vals)
    except Exception:
        pass
    return f

def font_fit(draw, text, font_name, max_w, start, min_size=22, wght=700):
    size=start
    while size>=min_size:
        f=vfont(font_name,size,wght)
        if draw.textlength(text,font=f) <= max_w:
            return f
        size-=2
    return vfont(font_name,min_size,wght)

def wav_duration(path: str) -> float:
    p=str(path)
    if p.lower().endswith(".wav"):
        try:
            with wave.open(p,"rb") as w:
                return w.getnframes()/float(w.getframerate())
        except: return 4.0
    # mp3 via ffmpeg probe
    try:
        import imageio_ffmpeg
        ff=imageio_ffmpeg.get_ffmpeg_exe()
        try:
            out=subprocess.check_output([ff,"-i",p], stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            out=e.output
    except Exception as e:
        out=str(e)
    m=re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", out)
    if not m: return 4.0
    h,mi,s=m.groups()
    return int(h)*3600+int(mi)*60+float(s)

def rounded(im, r=28):
    mask=Image.new("L", im.size,0)
    d=ImageDraw.Draw(mask)
    d.rounded_rectangle((0,0,im.size[0]-1,im.size[1]-1),r,fill=255)
    out=im.convert("RGBA")
    out.putalpha(mask)
    return out

def draw_geometry(draw, bx, by, bw, bh, shape):
    # shape examples: parallel lines, rectangle, etc.
    # we draw simple illustration for math geometry scenes
    if shape=="parallel":
        y1=by+bh//2-20
        y2=by+bh//2+20
        draw.line([(bx+80,y1),(bx+bw-80,y1)], fill=BLUE, width=6)
        draw.line([(bx+80,y2),(bx+bw-80,y2)], fill=BLUE, width=6)
        # arrows
        draw.polygon([(bx+bw-80,y1-8),(bx+bw-60,y1),(bx+bw-80,y1+8)], fill=BLUE)
    elif shape=="perp":
        cx=bx+bw//2; cy=by+bh//2
        draw.line([(cx-120,cy),(cx+120,cy)], fill=CORAL, width=6)
        draw.line([(cx,cy-120),(cx,cy+120)], fill=CORAL, width=6)
        # right angle
        draw.rectangle((cx,cy,cx+30,cy+30), outline=TEAL, width=4)
    elif shape=="rect":
        draw.rectangle((bx+200,by+bh//2-80,bx+bw-200,by+bh//2+80), outline=GREEN, width=5)
        # label L and l
        draw.text((bx+bw//2, by+bh//2-100), ar("الطول L"), font=vfont("NotoSansArabic.ttf",22), fill=INK, anchor="mm")
    return

def draw_scene_partial(lesson, scene, visible, w, h):
    # visible = number of lines to show (1..len). 0 = header only
    img=Image.new("RGB",(w,h),PAPER)
    d=ImageDraw.Draw(img)
    # grid
    for x in range(0,w,64):
        d.line([(x,0),(x,h)], fill=(233,227,214))
    for y in range(0,h,64):
        d.line([(0,y),(w,y)], fill=(233,227,214))
    # top bar
    d.rounded_rectangle((24,18,w-24,100),28,fill=SUN, outline=INK, width=4)
    title=ar(lesson.get("title",""))
    brand=ar(lesson.get("brand","برافو أكاديمي"))
    ft=font_fit(d,title,"NotoKufiArabic.ttf",w-280,38,wght=900)
    d.text((w//2,50),title,font=ft, fill=INK, anchor="mm")
    d.rounded_rectangle((40,32,140,86),14,fill=BLUE, outline=INK, width=3)
    d.text((90,59), f"EP {lesson.get('episode','')}", font=vfont("Fredoka.ttf",22,800), fill=WHITE, anchor="mm")
    # layout with mascot gap: reserve bottom 140 and keep right gap for mascot
    # board and photo heights reduced to leave BOTTOM_SAFE
    bw=960; bh= h - 140 - BOTTOM_SAFE  # 1080-140-140=800
    bx=40; by=120
    pw=840; ph=bh
    px=1040; py=by
    # photo frame
    d.rounded_rectangle((px-8,py-8,px+pw+8,py+ph+8),32,fill=WHITE, outline=INK, width=4)
    img_path=scene.get("image")
    if img_path and Path(img_path).exists():
        try:
            photo=Image.open(img_path).convert("RGB")
            photo=photo.resize((pw,ph), Image.LANCZOS)
            img.paste(rounded(photo,24),(px,py), rounded(photo,24))
        except:
            d.rounded_rectangle((px,py,px+pw,py+ph),24,fill=(220,230,250))
    else:
        d.rounded_rectangle((px,py,px+pw,py+ph),24,fill=(220,230,250))
        # placeholder text
        d.text((px+pw//2, py+ph//2), ar("صورة تعليمية"), font=vfont("NotoKufiArabic.ttf",28), fill=TEAL, anchor="mm")
    cap=scene.get("caption")
    if cap:
        d.rectangle((px, py+ph-70, px+pw, py+ph), fill=INK)
        cf=font_fit(d, ar(cap), "NotoSansArabic.ttf", pw-24, 26)
        d.text((px+pw//2, py+ph-35), ar(cap), font=cf, fill=WHITE, anchor="mm")
    # board
    d.rounded_rectangle((bx,by,bx+bw,by+bh),28,fill=WHITE, outline=INK, width=4)
    bt=scene.get("board_title","")
    if bt:
        d.rounded_rectangle((bx+24,by+20,bx+420,by+78),18,fill=TEAL, outline=INK, width=3)
        d.text((bx+222,by+49),ar(bt),font=vfont("NotoKufiArabic.ttf",26,800),fill=WHITE,anchor="mm")
    # lines with reveal: show only first visible
    lines=scene.get("lines",[])
    # choose fonts per line; handle RTL align: centered
    y=by+110
    for idx,line in enumerate(lines):
        if idx >= visible:
            break
        text=str(line.get("text",""))
        style=STYLES.get(line.get("style","small"), STYLES["small"])
        shown=ar(text) if any("\u0600" <= c <= "\u06FF" for c in text) else text
        fname="Amiri-Bold.ttf" if line.get("style")=="eq" else "NotoSansArabic.ttf"
        # fallback to appropriate font for French
        if line.get("style")=="eq" and not any("\u0600" <= c <= "\u06FF" for c in text):
            fname="Fredoka.ttf"
        f=font_fit(d, shown, fname, bw-80, style["size"])
        # highlight animation for newly revealed line: light yellow bg for last revealed
        if idx==visible-1 and visible>0:
            # subtle highlight rectangle
            tx_w=d.textlength(shown,font=f)
            x0=bx+bw//2 - tx_w//2 -12
            x1=bx+bw//2 + tx_w//2 +12
            y0=y-34; y1=y+34
            d.rounded_rectangle((x0,y0,x1,y1),12,fill=(255,247,200), outline=None)
        d.text((bx+bw//2, y), shown, font=f, fill=style["fill"], anchor="mm")
        # if answer, ellipse highlight but only when revealed
        if line.get("style")=="answer":
            # don't draw until after pause: but we are revealing, so draw
            d.rounded_rectangle((bx+60, y-36, bx+bw-60, y+36),14, outline=GREEN, width=4)
        # shape if any
        if line.get("shape"):
            draw_geometry(d, bx, y+50, bw, 120, line["shape"])
            y+=130
            continue
        y+=78
    # mascot safe zone visual hint: empty gap 130px at bottom-right
    # ensure no content overlaps: we already reserved bottom safe; draw mascot placeholder
    mx,my,mw,mh = w-150, h-150, 130,130
    # do not draw solid cover, just outline dashed area to indicate gap
    # draw small mascot circle (if exists) else star placeholder
    mascot_path = ROOT/"assets/brand/_mascot.png"
    if mascot_path.exists():
        try:
            masc=Image.open(mascot_path).convert("RGBA").resize((mw,mh), Image.LANCZOS)
            img.paste(masc, (mx,my), masc)
        except:
            d.ellipse((mx,my,mx+mw,my+mh), fill=SUN, outline=INK, width=4)
            d.text((mx+mw//2, my+mh//2), "★", font=vfont("Fredoka.ttf",64,800), fill=INK, anchor="mm")
    else:
        d.ellipse((mx,my,mx+mw,my+mh), fill=SUN, outline=INK, width=4)
        d.text((mx+mw//2, my+mh//2), "★", font=vfont("Fredoka.ttf",64,800), fill=INK, anchor="mm")
    # watermark gap: ensure no text overlaps mascot: already cleared
    # footer brand centered but offset to keep away from mascot
    d.text((w//2, h-36), brand, font=vfont("NotoSansArabic.ttf",22,700), fill=BLUE, anchor="mm")
    # subtle page number
    d.text((bx+30, h-36), f"{visible}/{len(lines)}", font=vfont("Fredoka.ttf",18), fill=(120,120,120), anchor="lm")
    if scene.get("confetti"):
        import random
        rnd=random.Random(7)
        cols=[SUN,CORAL,GREEN,BLUE,TEAL]
        for _ in range(60):
            x=rnd.randint(0,w); yy=rnd.randint(0,h-200)
            d.ellipse((x,yy,x+14,yy+14), fill=rnd.choice(cols))
    return img

def draw_scene(lesson, scene, w, h):
    return draw_scene_partial(lesson, scene, len(scene.get("lines",[])), w,h)

def write_srt_wordlevel(entries, path):
    # entries: list of (start,end,text)
    def ts(t):
        h=int(t//3600); m=int((t%3600)//60); s=t%60
        return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".",",")
    lines=[]
    for i,(s,e,txt) in enumerate(entries,1):
        lines.append(f"{i}\n{ts(s)} --> {ts(e)}\n{txt}\n")
    Path(path).write_text("\n".join(lines), encoding="utf-8")

def render(lesson_path: Path, out_mp4: Path, intro=False):
    import imageio_ffmpeg
    ffmpeg=imageio_ffmpeg.get_ffmpeg_exe()
    lesson=json.loads(lesson_path.read_text(encoding="utf-8"))
    w,h,fps=lesson.get("width",1920),lesson.get("height",1080),lesson.get("fps",24)
    base=lesson_path.parent.parent
    # resolve media
    for sc in lesson["scenes"]:
        for key in ("image","audio"):
            if sc.get(key) and not os.path.isabs(sc[key]):
                cand=(lesson_path.parent/sc[key]).resolve()
                if cand.exists():
                    sc[key]=str(cand)
                else:
                    sc[key]=str((base/sc[key]).resolve()) if (base/sc[key]).exists() else str(cand)
    tmp=Path(tempfile.mkdtemp(prefix="bravo_"))
    frames_dir=tmp/"frames"; frames_dir.mkdir()
    audios=[]
    meta_segments=[] # list of (scene, line_idx, dur) for SRT
    n=0
    srt_entries=[]
    current_time=0.0
    if intro:
        intro_img=Image.new("RGB",(w,h),PAPER)
        logo=ROOT/"assets/brand/logo.png"
        if logo.exists():
            L=Image.open(logo).convert("RGB").resize((420,420), Image.LANCZOS)
            intro_img.paste(L,((w-420)//2,180))
        d=ImageDraw.Draw(intro_img)
        d.text((w//2,680), ar(lesson.get("brand","برافو أكاديمي")), font=vfont("NotoKufiArabic.ttf",48,900), fill=BLUE, anchor="mm")
        d.text((w//2,760), ar(lesson.get("title","")), font=vfont("NotoSansArabic.ttf",32,700), fill=INK, anchor="mm")
        p=frames_dir/f"{n:05d}.png"; intro_img.save(p); n+=1
        sil=tmp/"sil.wav"
        subprocess.check_call([ffmpeg,"-y","-f","lavfi","-i","anullsrc=r=24000:cl=mono","-t","3.2",sil], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        audios.append(str(sil))
        srt_entries.append((current_time, current_time+3.2, lesson.get("title","")))
        current_time+=3.2
        meta_segments.append((None,0,3.2))
    for sc in lesson["scenes"]:
        ap=sc.get("audio")
        if ap and Path(ap).exists():
            total_dur=wav_duration(ap)
        else:
            # estimate from narration length ~ 13 chars per sec
            txt=sc.get("narration","")
            total_dur=max(3.5, len(txt)/13.0)
            # create silence of that length
            ap_tmp=tmp/f"sil{n}_{hash(ap)}.wav"
            subprocess.check_call([ffmpeg,"-y","-f","lavfi","-i","anullsrc=r=24000:cl=mono","-t",f"{total_dur:.2f}",str(ap_tmp)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            ap=str(ap_tmp)
            # keep audios list with generated silence; but if real audio exists elsewhere, use it
        # handle pause_after (pedagogical pause after question)
        pause_extra=float(sc.get("pause_after",0))
        # if any line is ask and not already pause, add 1.8s for thinking
        has_ask=any(l.get("style")=="ask" for l in sc.get("lines",[]))
        if has_ask and pause_extra==0:
            # quiz scene: add thinking pause before answer reveals
            # we will split pause before last answer line
            pause_extra=1.8
        # total segment time includes pause
        total_with_pause=total_dur+pause_extra
        audios.append(ap)
        if pause_extra>0:
            sil2=tmp/f"pause_{n}.wav"
            subprocess.check_call([ffmpeg,"-y","-f","lavfi","-i","anullsrc=r=24000:cl=mono","-t",f"{pause_extra:.2f}",sil2], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            audios.append(str(sil2))
        # per-line reveal timing: split total_dur among lines (ignore pause for line timing, pause is hold on penultimate frame)
        lines=sc.get("lines",[])
        if not lines:
            # single frame for empty
            frame=draw_scene_partial(lesson, sc, 0, w,h)
            fp=frames_dir/f"{n:05d}.png"; frame.save(fp); n+=1
            # duration handling will be via concat file later
            srt_entries.append((current_time, current_time+total_with_pause, sc.get("narration","")))
            meta_segments.append((sc, total_with_pause))
        else:
            # weight by text length
            lens=[max(1,len(l.get("text",""))) for l in lines]
            tot=sum(lens)
            line_durs=[ total_dur * (ll/tot) for ll in lens ]
            # ensure min 0.8s per line
            for i in range(len(line_durs)):
                if line_durs[i]<0.9: line_durs[i]=0.9
            # renormalize to total_dur
            scale= total_dur / sum(line_durs) if sum(line_durs)>0 else 1
            line_durs=[d*scale for d in line_durs]
            # create frames for each line reveal incrementally
            acc=0.0
            for idx, ld in enumerate(line_durs):
                visible=idx+1
                frame=draw_scene_partial(lesson, sc, visible, w,h)
                fp=frames_dir/f"{n:05d}.png"; frame.save(fp); n+=1
                # if this is the ask line and we have pause, we extend its hold
                hold=ld
                if has_ask and idx==len(lines)-2 and pause_extra>0:
                    # penultimate ask hold includes pause
                    hold+=pause_extra
                meta_segments.append((sc, hold))
                srt_entries.append((current_time+acc, current_time+acc+hold, sc.get("narration","") if idx==0 else "")) # only first line gets narration? better duplicate
                # for SRT we want per-scene narration, so accumulate
                acc+=ld
            # need to adjust srt: we actually want one SRT entry per scene covering its total time, not per line fragments with empty text
            # so remove per-line empty entries and replace with scene entry
            # remove last len(lines) entries and add one scene entry
            for _ in range(len(lines)):
                srt_entries.pop()
            srt_entries.append((current_time, current_time+total_with_pause, sc.get("narration","").strip()))
            # if we added pause, acc already includes it? we handled hold extension: so current_time advance = total_with_pause
        current_time+=total_with_pause
    # now we have n frames, but need to map each frame to its duration (meta_segments)
    # meta_segments length should equal n (excluding intro maybe)
    # Build concat file for ffmpeg
    concat=tmp/"slides.txt"
    # meta_segments order matches frames_dir order 0..n-1
    # If intro included, first segment is intro
    with open(concat,"w") as f:
        for idx,seg in enumerate(meta_segments):
            # seg is (sc, dur) or tuple with dur as second element? second case we stored (sc, dur)
            # for line-level segments we stored (sc, dur)
            # need to extract dur
            if isinstance(seg, tuple) and len(seg)==2:
                dur=seg[1]
            elif isinstance(seg, tuple) and len(seg)==3:
                dur=seg[2]
            else:
                dur=4.0
            f.write(f"file '{frames_dir / f'{idx:05d}.png'}'\n")
            f.write(f"duration {dur:.3f}\n")
        f.write(f"file '{frames_dir / f'{n-1:05d}.png'}'\n")
    audio_all=tmp/"all.wav"
    lst=tmp/"alist.txt"
    with open(lst,"w") as f:
        for p in audios:
            f.write(f"file '{os.path.abspath(p)}'\n")
    subprocess.check_call([ffmpeg,"-y","-f","concat","-safe","0","-i",str(lst),"-c:a","pcm_s16le",str(audio_all)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    out_mp4.parent.mkdir(parents=True, exist_ok=True)
    subprocess.check_call([ffmpeg,"-y","-f","concat","-safe","0","-i",str(concat),"-i",str(audio_all),"-r",str(fps),"-pix_fmt","yuv420p","-c:v","libx264","-c:a","aac","-shortest",str(out_mp4)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    srt=out_mp4.with_suffix(".srt")
    # write srt using srt_entries (scene level)
    write_srt_wordlevel(srt_entries, srt)
    print(f"wrote {out_mp4} duration {current_time:.1f}s srt {srt}")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--lesson", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--intro", action="store_true")
    args=p.parse_args()
    render(Path(args.lesson), Path(args.out), intro=args.intro)

if __name__=="__main__":
    main()
