#!/usr/bin/env python3
"""Apply OGP metadata to the static tablet-making game without touching gameplay."""
from pathlib import Path

path = Path("index.html")
src = path.read_text(encoding="utf-8")
anchor = "<title>楽しい錠剤づくりゲーム</title>"
if 'property="og:image"' in src:
    print("OGP image metadata is already present; no change.")
elif src.count(anchor) != 1:
    raise SystemExit("Unexpected title marker count; refusing to modify index.html")
else:
    tags = """<meta name="description" content="混ぜて、固めて、失敗して学ぶ！製剤工程のパラメーターを自分で調整しながら、薬づくりを体験できる教育ゲーム。" />
<link rel="canonical" href="https://enjoytabletmaking.vercel.app/" />
<meta property="og:type" content="website" />
<meta property="og:locale" content="ja_JP" />
<meta property="og:site_name" content="よこぼのAIラボ" />
<meta property="og:title" content="楽しい錠剤づくりゲーム" />
<meta property="og:description" content="遊んで学べる くすりづくり体験。混ぜて、固めて、失敗して学ぶ！" />
<meta property="og:url" content="https://enjoytabletmaking.vercel.app/" />
<meta property="og:image" content="https://enjoytabletmaking.vercel.app/assets/ogp.png" />
<meta property="og:image:secure_url" content="https://enjoytabletmaking.vercel.app/assets/ogp.png" />
<meta property="og:image:type" content="image/png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="ニャビットと楽しい錠剤づくりゲーム。粉から錠剤へ、遊んで学べるくすりづくり体験。" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="楽しい錠剤づくりゲーム" />
<meta name="twitter:description" content="遊んで学べる くすりづくり体験。混ぜて、固めて、失敗して学ぶ！" />
<meta name="twitter:image" content="https://enjoytabletmaking.vercel.app/assets/ogp.png" />"""
    updated = src.replace(anchor, anchor + "\n" + tags, 1)
    assert updated.count('property="og:image"') == 1
    path.write_text(updated, encoding="utf-8")
    print("Inserted OGP metadata; gameplay content preserved.")
