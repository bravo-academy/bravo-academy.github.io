#!/usr/bin/env python3
"""Build catalog.json for Bravo Academy studio."""
import glob, json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
CUR_DIR = os.path.join(ROOT, "curriculum")
LEVELS_DIR = os.path.join(ROOT, "levels")

HASHTAGS_SUB = {
    "math": "رياضيات",
    "arabic": "لغة_عربية",
    "science": "إيقاظ_علمي",
    "french": "لغة_فرنسية",
    "islamic": "تربية_إسلامية",
    "civic": "تربية_مدنية",
    "history-geo": "تاريخ_وجغرافيا",
}

HASHTAGS_LVL = {
    "g1": "السنة_الأولى",
    "g2": "السنة_الثانية",
    "g3": "السنة_الثالثة",
    "g4": "السنة_الرابعة",
    "g5": "السنة_الخامسة",
    "g6": "السنة_السادسة",
}

catalog = {
    "channel": {
        "name": "برافو أكاديمي – Bravo Academy",
        "handle": "@BravoAcademyTN",
        "country": "🇹🇳 تونس",
        "made_for_kids": True,
        "email": "bravoacademy.tn@gmail.com",
    },
    "levels": [],
}

# Scan all curriculum files
cur_files = sorted(glob.glob(os.path.join(CUR_DIR, "g*.json")))

levels_data = {}

for cf in cur_files:
    with open(cf, "r", encoding="utf-8") as f:
        data = json.load(f)
    lvl_id = data["level"]
    lvl_ar = data["level_ar"]
    sub_id = data["subject"]
    sub_ar = data["subject_ar"]

    if lvl_id not in levels_data:
        levels_data[lvl_id] = {
            "id": lvl_id,
            "title_ar": lvl_ar,
            "subjects": [],
        }

    # check actual level directory for rendered lessons
    sub_lessons = []
    level_sub_dir = os.path.join(LEVELS_DIR, lvl_id, sub_id)
    lessons_json_dir = os.path.join(level_sub_dir, "lessons")

    for l_item in data.get("lessons", []):
        lid = l_item["id"]
        ltitle = l_item["title"]
        
        # search for matching lesson json in level_sub_dir/lessons
        lesson_json_path = None
        if os.path.exists(lessons_json_dir):
            for candidate in sorted(os.listdir(lessons_json_dir)):
                if candidate.startswith(lid) and candidate.endswith(".json"):
                    lesson_json_path = os.path.join(lessons_json_dir, candidate)
                    break

        sc_narrations = []
        if lesson_json_path and os.path.exists(lesson_json_path):
            with open(lesson_json_path, "r", encoding="utf-8") as ljf:
                lj_data = json.load(ljf)
                for sc in lj_data.get("scenes", []):
                    if sc.get("narration"):
                        sc_narrations.append(sc["narration"])

        stem = os.path.basename(lesson_json_path)[:-5] if lesson_json_path else f"{lid}_lesson"
        out_mp4 = os.path.join(level_sub_dir, "out", f"{stem}.mp4")
        out_short = os.path.join(level_sub_dir, "out", "shorts", f"{stem}_short.mp4")
        out_thumb = os.path.join(level_sub_dir, "out", "thumbs", f"{stem}.jpg")
        out_srt = os.path.join(level_sub_dir, "out", f"{stem}.srt")

        is_ready = os.path.exists(out_mp4)

        video_url = os.path.relpath(out_mp4, ROOT) if is_ready else ""
        short_url = os.path.relpath(out_short, ROOT) if os.path.exists(out_short) else ""
        thumb_url = os.path.relpath(out_thumb, ROOT) if os.path.exists(out_thumb) else ""
        srt_url = os.path.relpath(out_srt, ROOT) if os.path.exists(out_srt) else ""

        srt_content = ""
        if os.path.exists(out_srt):
            with open(out_srt, "r", encoding="utf-8") as sf:
                srt_content = sf.read()

        summary_text = "\n• ".join(sc_narrations) if sc_narrations else ltitle

        ht_sub = HASHTAGS_SUB.get(sub_id, sub_id)
        ht_lvl = HASHTAGS_LVL.get(lvl_id, lvl_id)

        yt_title = f"درس {sub_ar}: {ltitle} — {lvl_ar} | برافو أكاديمي"
        yt_desc = (
            f"🎓 درس {sub_ar}: {ltitle} — {lvl_ar}\n"
            f"قناة برافو أكاديمي · Bravo Academy (@BravoAcademyTN)\n\n"
            f"📌 محتوى الدرس:\n• {summary_text}\n\n"
            f"🗓️ رزنامة النشر اليومية (18:00 بتوقيت تونس):\n"
            f"📐 الأحد: رياضيات | ✍️ الإثنين: لغة عربية | 🔬 الثلاثاء: إيقاظ علمي\n"
            f"🇫🇷 الأربعاء: فرنسية | 🕌 الخميس: إسلامية ومدنية | 🗺️ الجمعة: تاريخ وجغرافيا | 🏆 السبت: مراجعة وكويز\n\n"
            f"شجّعوا أطفالكم واشتركوا في القناة! برافو! 👏\n\n"
            f"#{ht_lvl} #{ht_sub} #برافو_أكاديمي #تعليم_تونس #ابتدائي #BravoAcademy"
        )
        yt_tags = f"{lvl_ar}, {sub_ar}, {ltitle}, تعليم تونس, برافو أكاديمي, Bravo Academy, @BravoAcademyTN, ابتدائي تونس"

        fb_title = f"🎓 {sub_ar} — {lvl_ar}: {ltitle}"
        fb_desc = (
            f"🎓 درس {sub_ar}: {ltitle} ({lvl_ar}) 🇹🇳\n\n"
            f"أهلاً بأبطال برافو أكاديمي! 👋\n"
            f"شاهدوا درس اليوم وتدرّبوا معنا:\n"
            f"• {summary_text}\n\n"
            f"لا تنسوا المتابعة ليصلكم كل جديد يومياً! @BravoAcademyTN\n\n"
            f"#{ht_lvl} #{ht_sub} #برافو_أكاديمي #تعليم_تونس"
        )
        fb_tags = f"#{ht_lvl} #{ht_sub} #برافو_أكاديمي #تعليم_تونس"

        sub_lessons.append({
            "id": lid,
            "stem": stem,
            "title": ltitle,
            "status": "ready" if is_ready else "planned",
            "video_url": video_url,
            "short_url": short_url,
            "thumb_url": thumb_url,
            "srt_url": srt_url,
            "srt_content": srt_content,
            "youtube": {
                "title": yt_title,
                "description": yt_desc,
                "tags": yt_tags,
            },
            "facebook": {
                "title": fb_title,
                "description": fb_desc,
                "tags": fb_tags,
            },
        })

    levels_data[lvl_id]["subjects"].append({
        "id": sub_id,
        "title_ar": sub_ar,
        "lessons": sub_lessons,
    })

catalog["levels"] = list(levels_data.values())

with open(os.path.join(ROOT, "catalog.json"), "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

print("Built catalog.json successfully with", len(catalog["levels"]), "levels.")
