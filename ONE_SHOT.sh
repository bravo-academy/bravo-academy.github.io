#!/bin/bash
# برافو أكاديمي - سكريبت الشات الواحد: ينجز كل المطلوب في أمر واحد
set -e
ROOT=$(pwd)
echo "🎓 برافو أكاديمي - One-Shot g3 expansion"
pip install --quiet arabic-reshaper python-bidi pillow numpy imageio-ffmpeg gTTS
python3 expand_g3.py
python3 gen_audio.py
# رندر كل الدروس (HD 1080p + تزامن تدريجي + فجوة ماسكت 130px + وقفات)
for lp in levels/g3/*/lessons/*.json; do
  out=$(dirname $(dirname $lp))/out/$(basename ${lp%.json}).mp4
  echo "⏳ رندر $lp -> $out"
  python3 render.py --lesson "$lp" --out "$out"
done
python3 make_thumbs.py
for lp in levels/g3/*/lessons/*.json; do
  python3 make_shorts.py --lesson "$lp"
done
python3 build_catalog.py
echo "✅ تم: 25 درس × 6 مشاهد = 90-120ث، تزامن كامل، SRT+thumbs+shorts، catalog محدث"
ls -lh levels/g3/*/out/*.mp4 | head -n 5
cat catalog.json | grep -o '"status": "ready"' | wc -l
echo "للرفع:"
echo "  git add -A && git commit -m 'feat(g3): expanded' && git push -u origin \$(git branch --show-current)"
echo "  ثم افتح PR عبر: gh pr create --fill --base main  && gh pr merge --merge --auto"
