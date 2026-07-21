# -*- coding: utf-8 -*-
"""
Генератор index.html — каталог «Конструктивные решения».
Концепция 1 «Инженерный лист» (см. concepts.html). Один файл, без внешних библиотек.
Этап 3: каркас + раздел «Для дачи и участка» целиком.
"""
from string import Template

# ── DATA (владелец редактирует числа/ссылки здесь) ────────────────────
BRAND = {
    "phone_tel": "tel:+74950855990",
    "phone_text": "+7 (495) 085-59-90",
    "hours": "с 9:00 до 21:00",
}
LINKS = {
    "whatsapp": "https://wa.me/79939575790",
    "telegram": "https://t.me/teplicy_pk",
    "max": "https://max.ru/u/f9LHodD0cOIr3NM5nk0Boxc8e_KYjob089U-QtWch7iXesvuAjsakWHkcMA",
}

# ── Палитра и типографика концепции 1 ──────────────────────────────────
BG = "#F6F7F9"; INK = "#1B2430"; MUTED = "#59616E"; HAIR = "#DBE0E7"
PRIMARY = "#1E3A5A"; ON_PRIMARY = "#FFFFFF"; SURFACE = "#FFFFFF"
FONT_HEAD = '"Helvetica Neue", Helvetica, Arial, sans-serif'
FONT_BODY = '"PT Sans", "Helvetica Neue", Arial, sans-serif'
FONT_MONO = '"PT Mono", Menlo, monospace'

ACCENTS = {
    "dacha":    ("#2F7A55", "Для дачи и участка"),
    "bani":     ("#7A3F52", "Бани"),
    "stroyka":  ("#B4531F", "Для стройки и вахты"),
    "san":      ("#17788B", "Санитария"),
    "torg":     ("#A6792A", "Торговля и бизнес"),
    "small":    ("#566173", "Малые формы"),
}

TOTAL_FAMILIES = 18
DOPOLNITELNO = ("Дополнительно комплектуем электрикой, утеплением 100 мм, дополнительными окнами "
                "и дверями, перегородками, линолеумом, конвекторами, ступенями. Стоимость назовём при расчёте.")

# ── Навигатор (задача → семейство), все 18 строк ───────────────────────
NAV_ROWS = [
    ("домик на дачу, чтобы ночевать", 1), ("хозблок, сарай, хранить инструмент", 1),
    ("домик с душем и туалетом", 2), ("современный дом-модуль, лофт", 3),
    ("два модуля, большая площадь", 4), ("металлический для дачи, дерево внутри", 5),
    ("баню на участок", 6), ("бытовку на стройку для бригады", 7),
    ("прорабскую с раздевалкой", 7), ("металлическую, которая переезжает", 8),
    ("поставить в два этажа", 9), ("большой модуль из двух корпусов", 10),
    ("сушилку для рабочей одежды", 11), ("северное исполнение", 12),
    ("душ и туалет на объект", 13), ("полностью санитарный модуль", 14),
    ("торговый павильон, киоск", 15), ("мобильный офис, пункт выдачи", 16),
    ("КПП, пост охраны, кафе, магазин", 17), ("беседку, будку, туалет", 18),
]

FAM_NAMES = {
    1: "Дачные бытовки", 2: "Дачные с душем и туалетом", 3: "ЛОФТ",
    4: "Стыкованные дачные", 5: "Металлические для дачи", 6: "Бани",
    7: "Строительные бытовки", 8: "Блок-контейнеры Стандарт", 9: "Блок-контейнеры Усиленный",
    10: "Стыкованные блок-контейнеры", 11: "Сушилка", 12: "Сэндвич-панели",
    13: "С сантехническим отсеком", 14: "Сантехнические модули", 15: "Торговые павильоны",
    16: "Мобильные офисы", 17: "Модульные здания", 18: "Малые формы",
}

# ── Семейства раздела «Для дачи и участка» (данные — из dannye.md/teksty.md) ──
FAMILIES = [
    {
        "num": 1, "slug": "dacha-bytovki", "accent": "dacha",
        "name": "Дачные бытовки",
        "audience": "Дача, куда ездят по выходным, — переодеться, попить чаю, "
                    "сложить садовый инвентарь, без стройки и лишних трат.",
        "differ": "От «Металлических для дачи» это семейство отличает более доступная цена — "
                  "каркас деревянный, а не металлический: собирается быстрее и дешевле, но со "
                  "временем требует чуть больше ухода, чем металл.",
        "kit": [
            "Деревянный каркас на брусовом основании 150×100 мм",
            "Утепление минватой 50 мм — пол, стены, потолок",
            "Вагонка хвои класса А/В внутри (не ДВП) — тепло и опрятно, как в доме; "
            "наружная отделка на выбор — та же вагонка или оцинкованный профлист",
            "Окна и утеплённая входная дверь; там, где есть перегородка — ещё и внутренние двери",
            "Кровля из оцинкованного листа, не требует ухода первые годы",
            "Перенос дверей, окон и перегородок под ваш участок — бесплатно, цена не меняется",
        ],
        "models": [
            ("Бытовка - 3м ДЭк", "3 м", "Эконом, без перегородки", 111000),
            ("Бытовка - 4м ДЭк", "4 м", "Эконом, без перегородки", 126000),
            ("Бытовка - 4м, с перегородкой ДЭк", "4 м", "Эконом, 1 перегородка", 142000),
            ("Бытовка - 5м ДЭк", "5 м", "Эконом, без перегородки", 142000),
            ("Бытовка - 5м, с перегородкой ДЭк", "5 м", "Эконом, 1 перегородка", 158000),
            ("Бытовка - 6м ДЭк", "6 м", "Эконом, без перегородки", 158000),
            ("Бытовка - 6м, с перегородкой ДЭк", "6 м", "Эконом, 1 перегородка", 174000),
            ("Бытовка - 6м, с двумя перегородками ДЭк", "6 м", "Эконом, 2 перегородки", 195000),
            ("Бытовка - 7м ДЭк", "7 м", "Эконом, без перегородки", 179000),
            ("Бытовка - 3м ДСт", "3 м", "Стандарт, без перегородки", 137000),
            ("Бытовка - 4м ДСт", "4 м", "Стандарт, без перегородки", 153000),
            ("Бытовка - 4м, с перегородкой ДСт", "4 м", "Стандарт, 1 перегородка", 168000),
            ("Бытовка - 5м ДСт", "5 м", "Стандарт, без перегородки", 168000),
            ("Бытовка - 5м, с перегородкой ДСт", "5 м", "Стандарт, 1 перегородка", 184000),
            ("Бытовка - 6м ДСт", "6 м", "Стандарт, без перегородки", 184000),
            ("Бытовка - 6м, с перегородкой ДСт", "6 м", "Стандарт, 1 перегородка", 200000),
            ("Бытовка - 6м, с двумя перегородками ДСт", "6 м", "Стандарт, 2 перегородки", 221000),
            ("Бытовка - 7м ДСт", "7 м", "Стандарт, без перегородки", 205000),
        ],
    },
    {
        "num": 2, "slug": "dush-tualet", "accent": "dacha",
        "name": "Дачные с душем и туалетом",
        "audience": "Дача без централизованной воды, где хочется помыться после огорода "
                    "и не бегать в дачный туалет через весь участок.",
        "differ": "В отличие от обычных «Дачных бытовок» сюда уже встроен санузел — "
                  "не приходится отдельно ставить бак с душем или бегать в дачный туалет.",
        "kit": [
            "Санблок в комплекте: душевая (поддон, линолеум, шторка) и туалет — строить отдельно не нужно",
            "Утепление минватой 50 мм",
            "Внутренняя отделка жилой части — вагонка или ДВП, по модели",
            "3 двери — свой вход в жилую часть и в санблок, наружная дверь утеплённая",
            "Одно окно 0,8×0,8 м и два окна 0,4×0,4 м",
            "Наружная отделка на выбор — профлист или вагонка",
        ],
        "models": [
            ("Бытовка с душем и туалетом (отделка ДВП) ДТСт", "6 м", "Внутр. отделка ДВП", 205000),
            ("Бытовка с душем и туалетом (отделка вагонка) ДТД", "6 м", "Внутр. отделка вагонка", 242000),
        ],
    },
    {
        "num": 3, "slug": "loft", "accent": "dacha",
        "name": "ЛОФТ",
        "audience": "Тем, кому на участке или в городе важен не только метраж, но и вид, — офис, шоурум, студия.",
        "differ": "От «Металлических для дачи» это семейство отличают готовые ПВХ-окна и уже "
                  "разведённая электрика в базовой цене — это модуль под интерьер и работу, "
                  "а не жильё для дачного сезона.",
        "kit": [
            "Цельнометаллический каркас (швеллер и уголок) — жёстче дерева, не ведёт со временем",
            "Окна ПВХ, а не деревянные, как в обычных бытовках",
            "Электрика уже разведена: розетки, светильники, автомат, уличный свет — часть цены, а не отдельная опция",
            "Утепление 50 мм, вагонка хвои внутри",
            "Металлическая утеплённая входная дверь с замком",
            "Открытая планировка без перегородок — пространство организуете под себя",
        ],
        "models": [
            ("БКТ - 6м Л1 (ЛОФТ)", "6 м", "1 окно ПВХ поворотно-откидное", 322000),
            ("БКТ - 6м Л2 (ЛОФТ)", "6 м", "2 окна ПВХ (одно глухое), опций докупить нельзя", 371000),
        ],
    },
    {
        "num": 4, "slug": "stykovannye-dachnye", "accent": "dacha",
        "name": "Стыкованные дачные",
        "audience": "Семье, которой нужен не один отдельный модуль, а маленький дом с комнатами — "
                    "кухня, спальня, прихожая под одной крышей.",
        "differ": "В отличие от одиночной «Дачной бытовки» это уже дом с планировкой — "
                  "прихожая и отдельные комнаты вместо одного отсека.",
        "kit": [
            "Две состыкованные бытовки — 6,0×4,6 м жилой площади вместо площади одной",
            "Утепление минватой 50 мм, вагонка хвои класса А/В внутри и снаружи",
            "Планировка на выбор: закрытый дом с кухней и 2 комнатами (БС-1), с крыльцом (БС-2) "
            "или с открытой террасой (БС-3)",
            "Утеплённая входная дверь, окна по числу комнат",
            "Двускатная кровля из оцинкованного профлиста",
            "Монтаж на участке уже включён в цену (доставка и работа крана — отдельно)",
        ],
        "models": [
            ("Стыкованная дачная бытовка с террасой БС-3", "6,0×4,6×2,55 м", "С открытой террасой", 395000),
            ("Стыкованная дачная бытовка с крыльцом БС-2", "6,0×4,6×2,55 м", "С крыльцом", 449000),
            ("Стыкованная дачная бытовка БС-1", "6,0×4,6×2,55 м",
             "Полная закрытая планировка: кухня, прихожая, 2 комнаты — без крыльца/террасы, "
             "поэтому больше жилой площади под крышей", 462000),
        ],
    },
    {
        "num": 5, "slug": "metall-dacha", "accent": "dacha",
        "name": "Металлические для дачи",
        "audience": "Дача на много лет вперёд или участок, который стоит без присмотра "
                    "большую часть сезона, — сварной каркас не гниёт и не ведёт геометрию со временем.",
        "differ": "От «Блок-контейнеры Стандарт» это семейство отличает то, что отделка вагонкой "
                  "здесь уже выбрана за вас — специально для уютной дачи, а не под рабочие задачи стройки.",
        "kit": [
            "Сварной металлический каркас — не гниёт и не ведётся от сырости",
            "Утепление минватой 50 мм — пол, стены, потолок",
            "Внутренняя отделка вагонкой — не голый металл, уютно как в деревянном доме",
            "Окно и дверь крупнее, чем у деревянных бытовок, — светлее внутри",
            "Входная утеплённая дверь с врезным замком",
            "Перенос дверей, окон и перегородок — бесплатно",
        ],
        "models": [
            ("БКТ - 3м ПД", "3 м", "Отделка вагонка, без перегородки", 153000),
            ("БКТ - 4м ПД", "4 м", "Отделка вагонка, без перегородки", 168000),
            ("БКТ - 4м, с перегородкой ПД", "4 м", "Отделка вагонка, 1 перегородка", 184000),
            ("БКТ - 5м ПД", "5 м", "Отделка вагонка, без перегородки", 184000),
            ("БКТ - 5м с перегородкой ПД", "5 м", "Отделка вагонка, 1 перегородка", 200000),
            ("БКТ - 6м ПД", "6 м", "Отделка вагонка, без перегородки", 200000),
            ("БКТ - 6м, с перегородкой ПД", "6 м", "Отделка вагонка, 1 перегородка", 216000),
            ("БКТ - 6м, с двумя перегородками ПД", "6 м", "Отделка вагонка, 2 перегородки", 238000),
            ("БКТ - 7м ПД", "7 м", "Отделка вагонка, без перегородки", 221000),
        ],
    },
]

# ── иконки (реальные, локальные файлы — foto/icons/) ───────────────────
ICON_PHONE = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
              'stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h3l1.5 4-2 1.4a11 11 0 0 0 '
              '5.1 5.1l1.4-2 4 1.5v3a2 2 0 0 1-2.2 2A16 16 0 0 1 4 5.2 2 2 0 0 1 6 3Z"/></svg>')
ICON_UP = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
           'stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>')


def fmt_price(n):
    return "{:,}".format(n).replace(",", " ") + " ₽"


def photo_ph(label, w, h):
    return f'<div class="ph" style="width:{w}px;height:{h}px"><span class="lbl">{label}<br>{w} × {h}</span></div>'


def button_cluster():
    return f'''<div class="cluster">
      <a class="btn-call" href="{BRAND['phone_tel']}">{ICON_PHONE}<span>Позвонить</span></a>
      <div class="msgrs">
        <a class="msgr" href="{LINKS['whatsapp']}" target="_blank" rel="noopener"><img src="foto/icons/whatsapp.svg" alt="WhatsApp"></a>
        <a class="msgr" href="{LINKS['telegram']}" target="_blank" rel="noopener"><img src="foto/icons/telegram.svg" alt="Telegram"></a>
        <a class="msgr" href="{LINKS['max']}" target="_blank" rel="noopener"><img src="foto/icons/max.png" alt="Max"></a>
      </div>
    </div>'''


def footer_block():
    return f'''<div class="p-foot">
      {button_cluster()}
      <div class="foot-row">
        <span class="phone-no">{BRAND['phone_text']} · {BRAND['hours']}</span>
        <a class="nav-up" href="#navigator">{ICON_UP}<span>к навигатору</span></a>
      </div>
    </div>'''


def header_block(accent_key, num=None):
    color, label = ACCENTS[accent_key]
    idx = f'<div class="p-idx mono">{num:02d} / {TOTAL_FAMILIES}</div>' if num else ""
    return f'''<div class="p-head">
      <div class="p-tag"><span class="p-square" style="background:{color}"></span><b>{label}</b></div>
      {idx}
    </div>'''


def screen_open(screen_id, extra_class=""):
    return f'<section class="screen {extra_class}" id="{screen_id}">'


def screen_close():
    return '</section>'


def family_visual(fam):
    color, _ = ACCENTS[fam["accent"]]
    s = fam["slug"]
    html = screen_open(f'fam-{fam["num"]}-visual', "phone-screen")
    html += f'<div class="stripe" style="background:{color}"></div>'
    html += '<div class="p-pad">'
    html += header_block(fam["accent"], fam["num"])
    html += f'<div class="p-title">{fam["name"]}</div>'
    html += f'<div class="p-aud">Кому подходит: {fam["audience"]}</div>'
    html += f'<div class="p-photo">{photo_ph(f"{s}-main.jpg", 960, 820)}</div>'
    html += '<div class="p-thumbs">'
    for i in (1, 2, 3):
        html += photo_ph(f"{s}-{i}.jpg", 320, 320)
    html += '</div>'
    html += f'<div class="p-differ">{fam["differ"]}</div>'
    html += '<div class="p-spacer"></div>'
    html += footer_block()
    html += '</div>'
    html += screen_close()
    return html


def family_data(fam):
    color, _ = ACCENTS[fam["accent"]]
    html = screen_open(f'fam-{fam["num"]}-data', "phone-screen")
    html += f'<div class="stripe" style="background:{color}"></div>'
    html += '<div class="p-pad">'
    html += header_block(fam["accent"], fam["num"])
    html += f'<div class="p-title small">{fam["name"]}</div>'
    html += '<div class="p-sub">Размеры и цены</div>'

    def render_table(rows):
        t = '<table class="data-table"><thead><tr><th>Модель</th><th>Размер</th><th>Особенности</th><th>Цена</th></tr></thead><tbody>'
        for name, size, feat, price in rows:
            t += f'<tr><td>{name}</td><td>{size}</td><td>{feat}</td><td class="mono price">{fmt_price(price)}</td></tr>'
        return t + '</tbody></table>'

    models = fam["models"]
    if len(models) > 10:
        mid = -(-len(models) // 2)  # ceil half
        html += ('<div class="data-table-split">'
                 + render_table(models[:mid]) + render_table(models[mid:]) + '</div>')
    else:
        html += render_table(models)
    html += '<div class="kit-title">Что входит в цену</div>'
    html += '<ul class="kit-list">' + "".join(f"<li>{k}</li>" for k in fam["kit"]) + '</ul>'
    html += f'<div class="dop-line">{DOPOLNITELNO}</div>'
    html += '<div class="p-spacer"></div>'
    html += footer_block()
    html += '</div>'
    html += screen_close()
    return html


def divider(accent_key, title, tagline):
    color, _ = ACCENTS[accent_key]
    html = screen_open(f'razdel-{accent_key}', "divider-screen")
    html += f'<div class="divider-inner" style="background:{color}">'
    html += f'<div class="divider-title">{title}</div>'
    html += f'<div class="divider-tag">{tagline}</div>'
    html += '</div>'
    html += screen_close()
    return html


# ── Входные экраны ──────────────────────────────────────────────────────
def screen_cover():
    html = screen_open("cover", "entry-screen")
    html += '<div class="p-pad cover-pad">'
    html += '<div class="cover-kicker">Конструктивные решения</div>'
    html += '<div class="cover-title">Готовые строения<br>под ключ</div>'
    html += '<div class="cover-sub">Привезём собранным — поставим за день</div>'
    html += photo_ph("hero-cover.jpg", 960, 900)
    html += '<div class="cover-stat mono">159 моделей · от 95 000 ₽</div>'
    html += '<div class="p-spacer"></div>'
    html += footer_block()
    html += '</div>'
    html += screen_close()
    return html


def screen_three_steps():
    steps = [
        ("1", "Определите, зачем нужно",
         "Дача, стройка, вахта, торговля или бизнес-задача — от этого зависит семейство."),
        ("2", "Дерево или металл",
         "Дерево теплее и дешевле для одного места. Металл держит переезды и штабелирование."),
        ("3", "Выберите размер по таблице",
         "В каждом семействе — таблица всех вариантов длины и цены рядом."),
    ]
    html = screen_open("tri-shaga", "entry-screen")
    html += '<div class="p-pad">'
    html += header_block("dacha")
    html += '<div class="p-title small">Как выбрать за три шага</div>'
    for num, title, text in steps:
        html += f'''<div class="step-row">
          <div class="step-num mono">{num}</div>
          <div><div class="step-title">{title}</div><div class="step-text">{text}</div></div>
        </div>'''
    html += '<div class="step-note">Не уверены — позвоните, подберём за пять минут.</div>'
    html += '<div class="p-spacer"></div>'
    html += footer_block()
    html += '</div>'
    html += screen_close()
    return html


def screen_navigator():
    html = screen_open("navigator", "entry-screen")
    html += '<div class="p-pad">'
    html += header_block("dacha")
    html += '<div class="p-title small">Навигатор</div>'
    html += '<div class="p-sub">Мне нужно… → откройте раздел</div>'
    html += '<table class="nav-table"><tbody>'
    for need, fam_num in NAV_ROWS:
        anchor = f'fam-{fam_num}-visual' if fam_num <= 5 else f'fam-{fam_num}-visual'
        html += (f'<tr><td>{need}</td>'
                 f'<td><a href="#{anchor}">{FAM_NAMES[fam_num]} →</a></td></tr>')
    html += '</tbody></table>'
    html += '<div class="p-spacer"></div>'
    html += footer_block()
    html += '</div>'
    html += screen_close()
    return html


def screen_wood_or_metal():
    html = screen_open("derevo-metall", "entry-screen")
    html += '<div class="p-pad">'
    html += header_block("dacha")
    html += '<div class="p-title small">Дерево или металл</div>'
    html += '''<div class="two-col">
      <div class="col">
        <div class="col-title">Дерево</div>
        <div class="col-text">Теплее на вид, дешевле вход. Для постоянного места на участке —
        дача, куда вы не планируете переезжать.</div>
      </div>
      <div class="col">
        <div class="col-title">Металл</div>
        <div class="col-text">Сварной каркас, переносит многократные переезды между объектами,
        не ведёт геометрию, можно ставить в два этажа. Служит около 20 лет.</div>
      </div>
    </div>'''
    html += '<div class="step-note">Не уверены, что подойдёт, — позвоните, поможем выбрать.</div>'
    html += '<div class="p-spacer"></div>'
    html += footer_block()
    html += '</div>'
    html += screen_close()
    return html


def screen_we_are_pricier():
    points = [
        ("Приезжает готовым.",
         "Многие боятся не самой бытовки или бани, а месяца грязной стройки на участке: "
         "чужая бригада, доски и утеплитель до заморозков. У нас наоборот — строение собирают "
         "и проверяют на производстве, а к вам оно приезжает уже готовым. Привезли, поставили "
         "на блоки — и в тот же день можно заезжать или топить печь."),
        ("Цена настоящая.",
         "На рынке принято писать цену за самый маленький размер, а по факту она подрастает на "
         "доставку, отделку и сборку — узнаёте об этом уже после звонка. Мы называем цену за то, "
         "что реально входит в комплектацию, без «от» и без сюрпризов в конце разговора."),
        ("Договор и гарантия 12 месяцев.",
         "Переводить деньги незнакомой компании страшно, и это нормально. Договор фиксирует "
         "размер, комплектацию и цену до копейки, а на изделие действует гарантия 12 месяцев."),
        ("Материалы, за которые не стыдно.",
         "Внутри — вагонка класса А/В, а не класс С, которым обшивает большинство рынка. "
         "Утепляем весь контур — пол, стены и потолок. Кровля — оцинкованный лист с фальцевым "
         "соединением, а не что придётся."),
        ("Мы отвечаем быстро.",
         "Знакомо, когда продавец читает сообщение и молчит днями? У нас с первого сообщения "
         "говорит менеджер — пишите в чат, вопросы по расчёту, доставке и монтажу решаются там же."),
    ]
    html = screen_open("my-dorozhe", "entry-screen")
    html += '<div class="p-pad">'
    html += header_block("dacha")
    html += '<div class="p-title small">Мы дороже. И вот за что.</div>'
    for title, text in points:
        html += f'<div class="pricier-point"><b>{title}</b> {text}</div>'
    html += '<div class="p-spacer"></div>'
    html += footer_block()
    html += '</div>'
    html += screen_close()
    return html


# ── Сборка страницы ─────────────────────────────────────────────────────
CSS = Template('''
* { margin:0; padding:0; box-sizing:border-box; }
:root {
  --bg:$bg; --ink:$ink; --muted:$muted; --hair:$hair;
  --primary:$primary; --onp:$onp; --surface:$surface;
  --fh:$fh; --fb:$fb; --fm:$fm;
}
html,body{ background:#c8ccd2; }
body{ font-family:var(--fb); color:var(--ink); -webkit-font-smoothing:antialiased; }
.mono{ font-family:var(--fm); font-feature-settings:"tnum" 1; }

.screens{ display:flex; flex-direction:column; align-items:center; gap:40px; padding:40px 0; }
.screen{ width:1080px; height:1920px; background:var(--surface); position:relative;
  overflow:hidden; box-shadow:0 2px 10px rgba(0,0,0,.15); }

.stripe{ position:absolute; left:0; top:0; width:12px; height:100%; z-index:3; }
.p-pad{ padding:64px 72px; display:flex; flex-direction:column; height:100%; }

.p-head{ display:flex; align-items:center; justify-content:space-between;
  padding-bottom:30px; border-bottom:1px solid var(--hair); }
.p-tag{ display:flex; align-items:center; gap:16px; }
.p-square{ width:30px; height:30px; }
.p-tag b{ font-family:var(--fb); font-weight:700; font-size:23px; letter-spacing:.16em;
  text-transform:uppercase; color:var(--ink); }
.p-idx{ font-size:23px; color:var(--muted); }

.p-title{ font-family:var(--fh); font-size:82px; font-weight:700; line-height:1.02;
  letter-spacing:-.01em; margin:44px 0 0; color:var(--ink); }
.p-title.small{ font-size:60px; margin-top:36px; }
.p-sub{ font-family:var(--fh); font-size:28px; color:var(--muted); margin-top:14px; }
.p-aud{ font-size:26px; line-height:1.4; color:var(--muted); margin-top:22px; max-width:900px; }
.p-differ{ font-size:24px; line-height:1.5; color:var(--muted); margin-top:20px; max-width:920px; }

.ph{ background:#EDEFF2; border:1px solid var(--hair); display:flex; align-items:center;
  justify-content:center; text-align:center; }
.ph .lbl{ font-family:var(--fm); font-size:20px; color:#9AA1AB; line-height:1.5; }
.p-photo{ margin:40px auto 0; }
.p-thumbs{ display:flex; gap:20px; justify-content:center; margin-top:20px; }
.p-spacer{ flex:1; min-height:16px; }

.p-foot{ border-top:1px solid var(--hair); padding-top:34px; }
.cluster{ display:flex; align-items:center; gap:26px; }
.btn-call{ display:inline-flex; align-items:center; gap:16px; background:var(--primary);
  color:var(--onp); font-family:var(--fb); font-weight:700; font-size:30px; padding:26px 46px;
  border-radius:6px; text-decoration:none; }
.btn-call svg{ width:34px; height:34px; }
.msgrs{ display:flex; gap:16px; }
.msgr{ width:76px; height:76px; border:1.5px solid var(--hair); border-radius:6px;
  display:flex; align-items:center; justify-content:center; }
.msgr img{ width:38px; height:38px; object-fit:contain; }
.foot-row{ display:flex; align-items:center; justify-content:space-between; margin-top:22px; }
.phone-no{ font-family:var(--fm); font-size:24px; color:var(--muted); letter-spacing:.02em; }
.nav-up{ display:flex; align-items:center; gap:8px; color:var(--muted); font-size:18px;
  text-decoration:none; }
.nav-up svg{ width:18px; height:18px; }

/* data screen table */
table.data-table{ margin-top:22px; border-collapse:collapse; width:100%; }
table.data-table th{ text-align:left; font-family:var(--fb); font-size:16px; letter-spacing:.1em;
  text-transform:uppercase; color:var(--muted); font-weight:700; padding:0 4px 10px; border-bottom:1px solid var(--hair); }
table.data-table th:last-child, table.data-table td.price{ text-align:right; }
table.data-table td{ padding:10px 4px; border-bottom:1px solid var(--hair); font-size:18px; vertical-align:top; line-height:1.3; }
table.data-table td.price{ font-size:19px; white-space:nowrap; padding-left:14px; }
.data-table-split{ display:flex; gap:36px; }
.data-table-split table.data-table{ flex:1; min-width:0; }
.data-table-split td, .data-table-split th{ font-size:16px; }
.data-table-split td.price{ font-size:17px; }
.kit-title{ font-family:var(--fb); font-size:17px; letter-spacing:.16em; text-transform:uppercase;
  color:var(--muted); font-weight:700; margin-top:30px; }
.kit-list{ list-style:none; margin-top:14px; display:flex; flex-direction:column; gap:10px; }
.kit-list li{ font-size:20px; line-height:1.4; padding-left:22px; position:relative; }
.kit-list li::before{ content:"—"; position:absolute; left:0; color:var(--muted); }
.dop-line{ font-size:17px; color:var(--muted); margin-top:22px; line-height:1.5; }

/* divider */
.divider-screen{ padding:0; }
.divider-inner{ width:100%; height:100%; display:flex; flex-direction:column; align-items:flex-start;
  justify-content:center; padding:0 90px; }
.divider-title{ font-family:var(--fh); font-size:96px; font-weight:700; color:#fff; line-height:1.02; }
.divider-tag{ font-family:var(--fb); font-size:30px; color:rgba(255,255,255,.86); margin-top:24px; max-width:820px; }

/* entry screens */
.cover-pad{ align-items:flex-start; }
.cover-kicker{ font-size:19px; letter-spacing:.32em; text-transform:uppercase; color:var(--muted); }
.cover-title{ font-family:var(--fh); font-size:88px; font-weight:700; line-height:1.04; margin-top:18px; }
.cover-sub{ font-size:28px; color:var(--muted); margin-top:18px; }
.cover-stat{ font-size:26px; margin-top:26px; color:var(--ink); }
.cover-pad .ph{ margin-top:36px; width:960px; height:900px; }

.step-row{ display:flex; gap:26px; margin-top:40px; align-items:flex-start; }
.step-num{ width:64px; height:64px; border-radius:50%; border:1.5px solid var(--primary);
  color:var(--primary); display:flex; align-items:center; justify-content:center; font-size:28px;
  flex-shrink:0; }
.step-title{ font-family:var(--fh); font-size:30px; font-weight:700; }
.step-text{ font-size:22px; color:var(--muted); margin-top:8px; max-width:820px; line-height:1.4; }
.step-note{ margin-top:44px; font-size:22px; color:var(--muted); border-top:1px solid var(--hair);
  padding-top:26px; }

.nav-table{ margin-top:26px; border-collapse:collapse; width:100%; }
.nav-table td{ padding:16px 4px; border-bottom:1px solid var(--hair); font-size:22px; }
.nav-table td:first-child{ color:var(--ink); }
.nav-table td:last-child{ text-align:right; }
.nav-table a{ color:var(--primary); text-decoration:none; font-weight:700; }

.two-col{ display:flex; gap:50px; margin-top:40px; }
.col{ flex:1; }
.col-title{ font-family:var(--fh); font-size:34px; font-weight:700; }
.col-text{ font-size:23px; line-height:1.5; color:var(--muted); margin-top:16px; }

.pricier-point{ font-size:23px; line-height:1.55; color:var(--ink); margin-top:26px; }
.pricier-point b{ font-family:var(--fh); font-size:25px; }

@media print {
  html,body{ background:#fff; }
  .screens{ padding:0; gap:0; }
  .screen{ box-shadow:none; page-break-after:always; }
  @page{ size:1080px 1920px; margin:0; }
}
''')


def build():
    parts = []
    parts.append(screen_cover())
    parts.append(screen_three_steps())
    parts.append(screen_navigator())
    parts.append(screen_wood_or_metal())
    parts.append(screen_we_are_pricier())
    parts.append(divider("dacha", "Для дачи и участка",
                          "Дом или хозблок, который привозят собранным и ставят за один день."))
    for fam in FAMILIES:
        parts.append(family_visual(fam))
        parts.append(family_data(fam))

    css = CSS.substitute(bg=BG, ink=INK, muted=MUTED, hair=HAIR, primary=PRIMARY,
                          onp=ON_PRIMARY, surface=SURFACE, fh=FONT_HEAD, fb=FONT_BODY, fm=FONT_MONO)

    html = f'''<!doctype html><html lang="ru"><head><meta charset="utf-8">
<title>Конструктивные решения — каталог готовых строений</title>
<style>{css}</style></head><body>
<div class="screens">
{"".join(parts)}
</div>
</body></html>'''

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("OK: index.html —", len(parts), "экранов")


if __name__ == "__main__":
    build()
