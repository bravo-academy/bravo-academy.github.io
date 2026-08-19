# برافو أكاديمي · Bravo Academy

قناة تعليمية لكل الابتدائي التونسي (**g1→g6**). مستودع مستقل: `bravo-academy/bravo-academy.github.io`.

## التشغيل

```bash
pip install --break-system-packages pillow arabic-reshaper python-bidi numpy imageio-ffmpeg
python3 assets/brand/_build_lockup.py
python3 render.py --lesson levels/g3/math/lessons/01_numbers.json --out levels/g3/math/out/01_numbers.mp4 --intro
python3 make_thumbs.py
python3 make_shorts.py --lesson levels/g3/math/lessons/01_numbers.json
python3 -m http.server 8080
```

القاعدة: [`BRAVO_PROJECT_PROMPT.md`](BRAVO_PROJECT_PROMPT.md) · القناة: [`CHANNEL.md`](CHANNEL.md) · الرزنامة: [`SCHEDULE.md`](SCHEDULE.md)
