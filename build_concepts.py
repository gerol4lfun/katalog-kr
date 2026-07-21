# -*- coding: utf-8 -*-
"""
Генератор трёх концепций дизайна каталога.
Каждая концепция — один вертикальный лист (koncepciya-N.html).
Общий шаблон, отличается только палитрой, шрифтовой парой и характером.
Все шрифты — системные (macOS), с подтверждённой кириллицей (fc-list :lang=ru).
Никаких упоминаний производителя. Ничего из интернета не тянется.
"""
from string import Template

# ── 5 разделов (общие для всех концепций) ─────────────────────────────
SECTIONS = [
    ("dacha",  "Для дачи и участка"),
    ("stroyka", "Для стройки и вахты"),
    ("san",    "Санитария"),
    ("torg",   "Торговля и бизнес"),
    ("small",  "Малые формы"),
]

# ── Контурные иконки мессенджеров (обобщённые, не логотипы брендов) ────
ICON_TG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
           'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
           '<path d="M21 4 3 11l5 2 2 6 3-4 5 4 3-15Z"/><path d="m8 13 8-6"/></svg>')
ICON_WA = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
           'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
           '<path d="M4 20l1.4-4A8 8 0 1 1 9 19.2L4 20Z"/>'
           '<path d="M9 9.5c0 3 2.5 5.5 5.5 5.5.6 0 1-.5 1-1l-1.6-.8-1 .9c-1-.4-2-1.4-2.4-2.4l.9-1L10.5 8.5c-.5 0-1 .4-1 1Z"/></svg>')
ICON_MSG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="M4 5h16v11H9l-4 3v-3H4Z"/><path d="M8 10h.01M12 10h.01M16 10h.01"/></svg>')

ICON_PHONE = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
              'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
              '<path d="M6 3h3l1.5 4-2 1.4a11 11 0 0 0 5.1 5.1l1.4-2 4 1.5v3a2 2 0 0 1-2.2 2A16 16 0 0 1 4 5.2 2 2 0 0 1 6 3Z"/></svg>')


def button_cluster(cfg, in_dark=False):
    """Связка: главная кнопка «Позвонить» + 3 приглушённые контурные иконки."""
    msgr_border = "rgba(255,255,255,.34)" if in_dark else cfg["hairline"]
    msgr_color  = "rgba(255,255,255,.86)" if in_dark else cfg["muted"]
    return f'''<div class="cluster">
      <a class="btn-call">{ICON_PHONE}<span>Позвонить</span></a>
      <div class="msgrs" style="--mb:{msgr_border};--mc:{msgr_color}">
        <span class="msgr">{ICON_TG}</span>
        <span class="msgr">{ICON_WA}</span>
        <span class="msgr">{ICON_MSG}</span>
      </div>
    </div>'''


def swatch(color, name, code, role, ink):
    return f'''<div class="sw">
      <div class="chip" style="background:{color}"></div>
      <div class="sw-t"><b>{name}</b><span class="mono">{code}</span><i>{role}</i></div>
    </div>'''


def palette_block(cfg):
    ink = cfg["ink"]
    base = (
        swatch(cfg["bg"],      "Фон",     cfg["bg"].upper(),      "полотно листа", ink)
        + swatch(cfg["ink"],   "Текст",   cfg["ink"].upper(),     "основной ink",  ink)
        + swatch(cfg["primary"], "Основной", cfg["primary"].upper(), "шапка · кнопка", ink)
    )
    acc = ""
    for key, label in SECTIONS:
        acc += swatch(cfg[key], label, cfg[key].upper(), "акцент раздела", ink)
    return f'''<div class="pal-base">{base}</div>
      <div class="pal-note">Пять акцентов — по числу разделов. На экране работает один: полоса слева + метка раздела.</div>
      <div class="pal-acc">{acc}</div>'''


TEMPLATE = Template('''<!doctype html><html lang="ru"><head><meta charset="utf-8">
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  :root{
    --bg:$bg; --ink:$ink; --muted:$muted; --hair:$hairline;
    --primary:$primary; --onp:$on_primary; --surface:$surface;
    --accent:$demo_accent;
    --fh:$font_head; --fb:$font_body; --fm:$font_mono;
  }
  html,body{ background:#c8ccd2; }
  body{ font-family:var(--fb); color:var(--ink); }
  .sheet{
    width:1240px; min-height:$sheet_h; background:var(--bg);
    padding:80px 80px 96px; position:relative;
    -webkit-font-smoothing:antialiased;
  }
  .mono{ font-family:var(--fm); font-feature-settings:"tnum" 1; }

  /* ── masthead ── */
  .kicker{ font-family:var(--fb); font-size:19px; letter-spacing:.32em;
    text-transform:uppercase; color:var(--muted); }
  .title{ font-family:var(--fh); font-size:72px; line-height:1.02; font-weight:700;
    color:var(--ink); margin:14px 0 16px; letter-spacing:$title_ls; }
  .character{ font-size:25px; line-height:1.45; color:var(--muted); max-width:940px; }
  .reco{ position:absolute; top:64px; right:64px; background:var(--primary);
    color:var(--onp); font-family:var(--fb); font-weight:700; font-size:18px;
    letter-spacing:.22em; padding:12px 22px; text-transform:uppercase; }

  /* ── section rule ── */
  .rule{ display:flex; align-items:baseline; gap:20px; margin:64px 0 30px;
    padding-bottom:16px; border-bottom:1px solid var(--hair); }
  .rule b{ font-family:var(--fb); font-size:17px; letter-spacing:.26em;
    text-transform:uppercase; color:var(--muted); font-weight:700; }
  .rule span{ font-size:17px; color:var(--muted); }

  /* ── palette ── */
  .pal-base{ display:flex; gap:22px; }
  .pal-acc{ display:flex; gap:18px; margin-top:22px; }
  .sw{ flex:1; }
  .chip{ height:104px; border:1px solid var(--hair); }
  .sw-t{ margin-top:12px; display:flex; flex-direction:column; gap:3px; }
  .sw-t b{ font-size:20px; font-weight:700; }
  .sw-t .mono{ font-size:17px; color:var(--muted); }
  .sw-t i{ font-style:normal; font-size:15px; color:var(--muted); }
  .pal-note{ font-size:18px; color:var(--muted); margin-top:22px; }

  /* ── typography specimen ── */
  .ty-h{ font-family:var(--fh); font-size:60px; font-weight:700; letter-spacing:$title_ls;
    line-height:1.05; }
  .ty-sub{ font-family:var(--fh); font-size:29px; font-weight:$sub_weight; color:var(--ink);
    margin-top:18px; }
  .ty-p{ font-size:23px; line-height:1.62; color:var(--ink); max-width:980px; margin-top:16px; }
  table.spec{ margin-top:28px; border-collapse:collapse; width:760px; }
  table.spec td{ padding:15px 4px; border-bottom:1px solid var(--hair); font-size:22px; }
  table.spec td.k{ color:var(--muted); }
  table.spec td.v{ text-align:right; }

  /* ── button cluster (specimen) ── */
  .cluster{ display:flex; align-items:center; gap:26px; }
  .btn-call{ display:inline-flex; align-items:center; gap:16px; background:var(--primary);
    color:var(--onp); font-family:var(--fb); font-weight:700; font-size:30px;
    padding:26px 46px; border-radius:$radius; letter-spacing:.01em; }
  .btn-call svg{ width:34px; height:34px; }
  .msgrs{ display:flex; gap:16px; }
  .msgr{ width:76px; height:76px; border:1.5px solid var(--mb); border-radius:$radius;
    display:flex; align-items:center; justify-content:center; color:var(--mc); }
  .msgr svg{ width:38px; height:38px; }
  .cl-note{ font-size:18px; color:var(--muted); margin-top:18px; }

  /* ── phone mockup 1080×1920 ── */
  .screen-cap{ display:flex; align-items:baseline; gap:18px; margin:66px 0 22px;
    padding-bottom:16px; border-bottom:1px solid var(--hair); }
  .screen-cap b{ font-family:var(--fb); font-size:17px; letter-spacing:.26em;
    text-transform:uppercase; color:var(--muted); }
  .screen-cap span{ font-size:17px; color:var(--muted); }
  .phone{ width:1080px; height:1920px; background:var(--surface); position:relative;
    overflow:hidden; border:1px solid var(--hair); display:flex; flex-direction:column; }
  .stripe{ position:absolute; left:0; top:0; width:$stripe_w; height:100%;
    background:var(--accent); z-index:3; }
  .p-pad{ padding:64px $content_left; display:flex; flex-direction:column;
    flex:1; }
  .p-head{ display:flex; align-items:center; justify-content:space-between;
    padding-bottom:30px; border-bottom:1px solid var(--hair); $head_extra }
  .p-tag{ display:flex; align-items:center; gap:16px; }
  .p-square{ width:30px; height:30px; background:var(--accent); }
  .p-tag b{ font-family:var(--fb); font-weight:700; font-size:23px; letter-spacing:.16em;
    text-transform:uppercase; color:$head_ink; }
  .p-idx{ font-family:var(--fm); font-size:23px; color:$head_muted; }
  .p-title{ font-family:var(--fh); font-size:82px; font-weight:700; line-height:1.02;
    letter-spacing:$title_ls; margin:44px 0 0; color:var(--ink); }
  .p-aud{ font-size:26px; line-height:1.4; color:var(--muted); margin-top:22px;
    max-width:900px; }
  .p-aud u{ text-decoration:none; box-shadow:inset 0 -2px 0 var(--accent); }
  .ph{ background:#EDEFF2; border:1px solid var(--hair); display:flex;
    align-items:center; justify-content:center; }
  .ph .lbl{ font-family:var(--fm); font-size:22px; color:#9AA1AB; letter-spacing:.06em; }
  .p-photo{ width:960px; height:820px; margin:40px auto 0; }
  .p-thumbs{ display:flex; gap:20px; justify-content:center; margin-top:20px; }
  .p-thumbs .ph{ width:320px; height:320px; }
  .p-spacer{ flex:1; min-height:24px; }
  .p-foot{ border-top:1px solid var(--hair); padding-top:34px; }
  .p-foot .phone-no{ font-family:var(--fm); font-size:24px; color:var(--muted);
    margin-top:22px; letter-spacing:.04em; }
</style></head>
<body>
<div class="sheet">
  $reco
  <div class="kicker">Концепция $num — Каталог строений</div>
  <div class="title">$concept_name</div>
  <div class="character">$character</div>

  <div class="rule"><b>Палитра</b><span>фон · текст · основной + пять акцентов разделов</span></div>
  $palette

  <div class="rule"><b>Типографика</b><span>$font_pair_label</span></div>
  <div class="ty-h">Дачные бытовки</div>
  <div class="ty-sub">Утеплённый корпус, готов к зимовке</div>
  <p class="ty-p">Каждое семейство — на двух экранах: сначала объём и материал, затем полные
    данные. Спокойный набор, крупные поля и одна таблица характеристик, которую видно
    без лупы. Так документ читается как паспорт изделия, а не как листовка.</p>
  <table class="spec">
    <tr><td class="k">Габариты корпуса</td><td class="v mono">6,0 × 2,3 м</td></tr>
    <tr><td class="k">Утепление стен</td><td class="v mono">100 мм</td></tr>
    <tr><td class="k">Срок изготовления</td><td class="v mono">7–10 дней</td></tr>
  </table>

  <div class="rule"><b>Кнопки</b><span>одна главная + три приглушённые иконки мессенджеров</span></div>
  $cluster_specimen
  <div class="cl-note">Иерархия обязательна: главная кнопка тяжёлая, мессенджеры — тихие контуры. Область нажатия ≥ 44×44.</div>

  <div class="screen-cap"><b>Готовый экран</b><span>«Дачные бытовки», визуальная половина разворота · 1080 × 1920</span></div>
  <div class="phone">
    <div class="stripe"></div>
    <div class="p-pad">
      <div class="p-head">
        <div class="p-tag"><span class="p-square"></span><b>Для дачи и участка</b></div>
        <div class="p-idx">01 / 17</div>
      </div>
      <div class="p-title">Дачные бытовки</div>
      <div class="p-aud">Кому подходит: <u>летний дом</u>, приём гостей, хранение инвентаря, бытовка на время стройки.</div>
      <div class="ph p-photo"><span class="lbl">ФОТО · 960 × 820</span></div>
      <div class="p-thumbs">
        <div class="ph"><span class="lbl">320 × 320</span></div>
        <div class="ph"><span class="lbl">320 × 320</span></div>
        <div class="ph"><span class="lbl">320 × 320</span></div>
      </div>
      <div class="p-spacer"></div>
      <div class="p-foot">
        $cluster_phone
        <div class="phone-no">+7 ___ ___-__-__ · с 9:00 до 21:00</div>
      </div>
    </div>
  </div>
</div>
</body></html>''')


def build(num, cfg):
    demo_accent = cfg["dacha"]
    # C3: тёмная шапка внутри экрана — её фирменный приём
    if cfg.get("dark_head"):
        cl = cfg["content_left"]
        head_extra = "background:#14181D; margin:-64px -%dpx 0 -%dpx; padding:64px %dpx 30px %dpx;" % (
            cl, cl, cl, cl)
        head_ink, head_muted = "#FFFFFF", "rgba(255,255,255,.62)"
    else:
        head_extra, head_ink, head_muted = "", cfg["ink"], cfg["muted"]

    html = TEMPLATE.substitute(
        bg=cfg["bg"], ink=cfg["ink"], muted=cfg["muted"], hairline=cfg["hairline"],
        primary=cfg["primary"], on_primary=cfg["on_primary"], surface=cfg["surface"],
        demo_accent=demo_accent,
        font_head=cfg["font_head"], font_body=cfg["font_body"], font_mono=cfg["font_mono"],
        title_ls=cfg["title_ls"], sub_weight=cfg["sub_weight"], radius=cfg["radius"],
        stripe_w="%dpx" % cfg["stripe_w"], content_left="%dpx" % cfg["content_left"],
        sheet_h=cfg["sheet_h"],
        num=num, concept_name=cfg["name"], character=cfg["character"],
        font_pair_label=cfg["font_pair_label"],
        palette=palette_block(cfg),
        cluster_specimen=button_cluster(cfg, in_dark=False),
        cluster_phone=button_cluster(cfg, in_dark=False),
        head_extra=head_extra, head_ink=head_ink, head_muted=head_muted,
        reco=('<div class="reco">Рекомендованная</div>' if cfg.get("reco") else ""),
    )
    with open("koncepciya-%d.html" % num, "w", encoding="utf-8") as f:
        f.write(html)


# ── КОНФИГИ ТРЁХ КОНЦЕПЦИЙ ────────────────────────────────────────────
C1 = {  # Инженерный лист
    "name": "Инженерный лист",
    "character": "Точность как аргумент. Холодная нейтральная палитра, моноширинные цифры "
                 "в данных и жёсткая сетка. Так выглядит паспорт оборудования — им же и объясняется цена.",
    "font_pair_label": "Заголовок Helvetica Neue · текст PT Sans · цифры PT Mono",
    "font_head": '"Helvetica Neue", Helvetica, Arial, sans-serif',
    "font_body": '"PT Sans", "Helvetica Neue", Arial, sans-serif',
    "font_mono": '"PT Mono", Menlo, monospace',
    "bg": "#F6F7F9", "surface": "#FFFFFF", "ink": "#1B2430", "muted": "#59616E",
    "hairline": "#DBE0E7", "primary": "#1E3A5A", "on_primary": "#FFFFFF",
    "dacha": "#2F7A55", "stroyka": "#B4531F", "san": "#17788B", "torg": "#A6792A", "small": "#566173",
    "title_ls": "-0.01em", "sub_weight": "400", "radius": "6px",
    "stripe_w": 12, "content_left": 40, "sheet_h": "3980px", "reco": True,
}
C2 = {  # Спокойный документ
    "name": "Спокойный документ",
    "character": "Тон добротного издания. Тёплая бумага, антиква в заголовках и широкие поля. "
                 "Документ выглядит так, будто его делали не спеша — и так же делают строения.",
    "font_pair_label": "Заголовок PT Serif · текст PT Sans · цифры PT Mono",
    "font_head": '"PT Serif", Georgia, serif',
    "font_body": '"PT Sans", "Helvetica Neue", Arial, sans-serif',
    "font_mono": '"PT Mono", Menlo, monospace',
    "bg": "#F3F2EE", "surface": "#FBFAF7", "ink": "#23272C", "muted": "#5B5F65",
    "hairline": "#DEDBD3", "primary": "#2B3A33", "on_primary": "#FFFFFF",
    "dacha": "#3A6B4A", "stroyka": "#8C5A2B", "san": "#2E6E78", "torg": "#8A6D3B", "small": "#55606A",
    "title_ls": "0em", "sub_weight": "400", "radius": "4px",
    "stripe_w": 14, "content_left": 40, "sheet_h": "3980px", "reco": False,
}
C3 = {  # Промышленный модерн
    "name": "Промышленный модерн",
    "character": "Уверенность через контраст. Тёмная шапка, крупная геометрия и один "
                 "насыщенный акцент на экран. Современно и решительно, без премиального глянца.",
    "font_pair_label": "Заголовок Avenir Next · текст PT Sans",
    "font_head": '"Avenir Next", "Helvetica Neue", Arial, sans-serif',
    "font_body": '"PT Sans", "Helvetica Neue", Arial, sans-serif',
    "font_mono": '"PT Sans", "Helvetica Neue", Arial, sans-serif',
    "bg": "#FFFFFF", "surface": "#FFFFFF", "ink": "#14181D", "muted": "#616872",
    "hairline": "#E4E7EB", "primary": "#14181D", "on_primary": "#FFFFFF",
    "dacha": "#1F8A5B", "stroyka": "#E06A17", "san": "#0E8FA8", "torg": "#C99117", "small": "#4B5563",
    "title_ls": "-0.02em", "sub_weight": "600", "radius": "2px",
    "stripe_w": 22, "content_left": 40, "sheet_h": "3980px", "reco": False,
    "dark_head": True,
}

for i, c in enumerate((C1, C2, C3), start=1):
    build(i, c)

# индекс для быстрого просмотра всех трёх
with open("concepts.html", "w", encoding="utf-8") as f:
    f.write('<!doctype html><meta charset="utf-8"><title>Концепции</title>'
            '<style>body{margin:0;background:#c8ccd2;display:flex;gap:40px;padding:40px;align-items:flex-start}'
            'iframe{width:1240px;height:3980px;border:0;background:#fff;box-shadow:0 2px 8px rgba(0,0,0,.15)}</style>'
            '<iframe src="koncepciya-1.html"></iframe>'
            '<iframe src="koncepciya-2.html"></iframe>'
            '<iframe src="koncepciya-3.html"></iframe>')

print("OK: koncepciya-1.html, koncepciya-2.html, koncepciya-3.html, concepts.html")
