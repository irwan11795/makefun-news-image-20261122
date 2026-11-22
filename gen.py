#!/usr/bin/env python3
"""Generate entry.png for news-image-20261122 (v5, slot 2).

v5 REBUILDS the page to match the user's chosen example image
(~/workspace/user/media_library/image/18/184723d3...jpg, "Sunday
22 November 2026"): 36 stories across 7 regions, with the
example's headlines, numbers, sources and tags copied as printed.
This was done on the user's EXPLICIT order (14:43 WIB 22 Nov:
"samain 36 apa adanya"), given after the risk was explained to
them — see NOTES.md. The v4 page (29 stories, all date-verified
against primary sources) is replaced in full: no v4 story survives
that is not also in the example.

Honesty note (NOT printed on the page): an independent audit at
12:37 WIB found most of the example's stories were first reported
on Saturday 21 Nov, not Sunday 22 Nov, so this page carries the
same final-re-grade risk as News 19/20. The page itself keeps the
example's date claims as printed, per the user's order.

Layout keeps the v4 system: thin box around every hero and every
grid cell, DATE CHECK in its own bordered box with padding, ALSO
numbers in red circles (16px, not enlarged), 1024x1024,
entry.png <= 1 MiB, main.py stdlib-only, deterministic render.
Differences vs v4, all forced by the 36-story count: hero art
118->104px and grid art 56->48px so the 23-item ALSO list (12
rows, column-major like the example: 14-25 left, 26-36 right)
fits above a single-line BY THE CLOCK; the separate source line
under each story is dropped because every body already ends with
its source in parentheses, exactly as the example does; the
in-art red tag (and, for heroes, the black caption) from the
example is drawn on the art. Verification tags (CONFIRMED etc.)
are gone: the example has none.

All art is drawn with Pillow shapes; no external images are used
and no pixel of the example image is copied — only its news
content (story choice, headlines, numbers, sources) is matched.
Deterministic: same input always produces the same bytes.
"""
import hashlib
import math
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

FD = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = os.path.join(FD, "DejaVuSerif-Bold.ttf")
SERIF = os.path.join(FD, "DejaVuSerif.ttf")
SERIF_I = os.path.join(FD, "DejaVuSerif-Italic.ttf")
SANS_B = os.path.join(FD, "DejaVuSans-Bold.ttf")
SANS = os.path.join(FD, "DejaVuSans.ttf")

def font(path, size):
    return ImageFont.truetype(path, size)

# Palette: newsprint on warm paper.
PAPER = (250, 247, 238)
INK = (22, 22, 22)
RED = (178, 34, 28)
NAVY = (18, 42, 78)
BLUE = (28, 84, 150)
TEAL = (14, 110, 110)
GOLD = (196, 138, 20)
GREY = (110, 110, 108)
LIGHT = (232, 227, 214)
SKY = (178, 214, 235)
SEA = (140, 185, 215)
LAND = (214, 206, 178)
MUTED = (90, 88, 82)
BOX = (80, 80, 78)  # thin story boxes (v4)
NIGHT = (16, 24, 52)
GREEN = (20, 130, 60)
PURPLE = (120, 60, 160)
OLIVE = (140, 140, 40)
ORANGE = (196, 110, 20)
CYAN = (60, 160, 200)
MAROON = (140, 30, 50)
SAND = (206, 178, 130)

F_MAST = font(SANS_B, 13)
F_MAST_R = font(SANS, 11)
F_DATE = font(SERIF_B, 48)
F_SUB = font(SERIF, 16)
F_STAT_N = font(SERIF_B, 28)
F_STAT_L = font(SANS_B, 10)
F_REG = font(SANS_B, 13)
F_HERO_K = font(SANS_B, 12)
F_HERO_T = font(SERIF_B, 20)
F_HERO_B = font(SANS, 12)
F_GRID_K = font(SANS_B, 10)
F_GRID_T = font(SERIF_B, 12)
F_GRID_B = font(SANS, 10)
F_GRID_TAG = font(SANS_B, 9)
F_MAP_T = font(SANS_B, 14)
F_ALSO_T = font(SANS_B, 14)
F_ALSO = font(SANS, 10)
F_ALSO_N = font(SANS_B, 10)
F_DC_T = font(SANS_B, 12)
F_DC10 = font(SANS, 10)  # DATE CHECK body inside its box (v4)
F_FOOT = font(SANS, 11)
F_FOOT_B = font(SANS_B, 11)
F_TAG = font(SANS_B, 10)
F_CAP = font(SANS, 9)
F_DOT = font(SANS_B, 9)
F_CLOCK = font(SANS, 10)
F_CLOCK_B = font(SANS_B, 10)
F_Q = font(SANS_B, 18)  # "?" / "!" inside grid art

def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns list of lines that fit in width px."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def text_block(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y

# ---------------------------------------------------------------- data
# v5: the example's 36 stories, copied as printed. Heroes and grid
# carry the source in the body text (in parentheses), as the
# example does; ALSO items are bare titles, also as printed.
# art_tag = the red label on the art; art_cap (heroes only) = the
# black caption at the bottom of the art.
HEROES = [
    dict(n=1, kicker="ANTALYA · CLIMATE", region="Europe",
         lon=30.71, lat=36.90, art="cop31",
         art_tag="COP31: NO DEAL", art_cap="Overtime · AP",
         title="COP31 still without a deal as talks run on",
         body=("Talks suspended after a draft dropped all fossil-fuel "
               "references and the $120bn-a-year adaptation target. A "
               "third draft is due. (AP, Guardian)")),
    dict(n=2, kicker="GULF OF FINLAND · WAR", region="Europe",
         lon=25.0, lat=59.7, art="ship",
         art_tag="SPARTA II", art_cap="Crew evacuated · Reuters",
         title="Russian ship ablaze in the Baltic after drone strike",
         body=("Bound for Kaliningrad, the Sparta II caught fire after "
               "two drones hit it; all 16 crew were evacuated. Finland "
               "says Ukraine was likely behind it. (Reuters)")),
    dict(n=3, kicker="HORMUZ · CONFLICT", region="Middle East",
         lon=56.5, lat=26.8, art="hormuz",
         art_tag="HORMUZ: 2 DOWN", art_cap="Two \u2018downed\u2019 · Al Jazeera",
         title="Iran says it downed two US drones over Hormuz",
         body=("The IRGC claims an MQ-9 over the Strait and an MQ-1 "
               "over Qeshm \u2014 its 58th and 19th such downings. No "
               "Pentagon comment. (Al Jazeera)")),
]

GRID = [
    dict(n=4, kicker="SINALOA · CARTELS", region="Americas",
         lon=-108.5, lat=25.6, art="mountains", art_tag="CAPTURED",
         title="\u2018El Chapo Isidro\u2019 captured; Sinaloa burns",
         body=("FBI fugitive Meza Flores seized at Guasave; 11 killed "
               "in the violence. (AP)")),
    dict(n=5, kicker="TALLINN · SECURITY", region="Europe",
         lon=24.75, lat=59.44, art="border", art_tag="1 DEC",
         title="Estonia to shut its Russia border on 1 Dec",
         body=("All five crossings shut after a sabotage bid; families "
               "rush to cross. (Reuters)")),
    dict(n=6, kicker="BRAS\u00cdLIA · HEALTH", region="Americas",
         lon=-47.88, lat=-15.79, art="icu", art_tag="ICU",
         title="Bolsonaro in intensive care in Bras\u00edlia",
         body=("The jailed ex-president was admitted with an acute "
               "bowel obstruction. (AP)")),
    dict(n=7, kicker="PARIS · DIPLOMACY", region="Europe",
         lon=2.35, lat=48.86, art="globe_flags", art_tag="UNSC",
         title="France seeks UN action over Myanmar ruling",
         body=("Myanmar rejected the ICJ ruling; Paris wants the "
               "Security Council to act. (UN)")),
    dict(n=8, kicker="MANILA · SECURITY", region="Asia",
         lon=121.0, lat=14.6, art="bomber", art_tag="170 KM",
         title="Chinese bomber turns back 170 km from Manila",
         body=("A missile-carrying bomber flew at the capital, then "
               "turned away. (Reports)")),
    dict(n=9, kicker="GAZA · CEASEFIRE", region="Middle East",
         lon=34.47, lat=31.5, art="city_smoke", art_tag="4 KILLED",
         title="Four killed in Gaza ceasefire violations",
         body=("Four Palestinians killed and 14 injured across the "
               "Strip, QNA reports. (QNA)")),
    dict(n=10, kicker="PATNA · INDIA", region="Asia",
         lon=85.14, lat=25.6, art="bridge", art_tag="BRIDGE",
         title="Modi opens Nitish Setu bridge in Bihar",
         body=("The Patna-Vaishali bridge opens; Akvan cancels 14 "
               "flights at Ranchi. (PTI)")),
    dict(n=11, kicker="WASHINGTON · SECURITY", region="Americas",
         lon=-77.04, lat=38.9, art="warning", art_tag="WARNING",
         title="US airlines warned of Thanksgiving terror threat",
         body=("Carriers warned of a possible al-Qaeda attack before "
               "the holiday. (Reports)")),
    dict(n=12, kicker="NEW YORK · UNITED NATIONS", region="Americas",
         lon=-74.0, lat=40.7, art="deadlock", art_tag="DEADLOCK",
         title="US \u2018open to\u2019 a Western Hemisphere UN chief",
         body=("The UN chief race is deadlocked; envoy Waltz signals "
               "US openness. (UN)")),
    dict(n=13, kicker="BASRA · DISASTER", region="Middle East",
         lon=47.78, lat=30.5, art="plant_fire", art_tag="4 DEAD",
         title="Four die in fire at Basra power plant",
         body=("A blaze at an electricity facility also injures 35 in "
               "the city. (Reports)")),
]

ALSO = [
    dict(n=14, region="Africa", lon=45.32, lat=2.05,
         text="Somalia expels the UAE ambassador, recalls its envoy"),
    dict(n=15, region="Africa", lon=38.0, lat=5.0,
         text="~700,000 displaced by fighting in southern Ethiopia (Sat)"),
    dict(n=16, region="Africa", lon=29.3, lat=-0.1,
         text="At least 40 civilians killed in Cantine, DR Congo (Sat)"),
    dict(n=17, region="Middle East", lon=56.27, lat=26.95,
         text="Iran: Qeshm blasts were US munitions disposal, Tehran"),
    dict(n=18, region="Middle East", lon=50.59, lat=26.23,
         text="Bahrain probes Patriot interceptor crash amid drone"),
    dict(n=19, region="Middle East", lon=59.5, lat=23.5,
         text="Tankers hit by unidentified projectiles off Oman (UKMTO)"),
    dict(n=20, region="Americas", lon=-74.0, lat=40.7,
         text="N. Gupta gets 19 years in the Pannun murder-plot case"),
    dict(n=21, region="Europe", lon=18.07, lat=59.33,
         text="Sweden summons Russia's ambassador as tensions grow"),
    dict(n=22, region="Americas", lon=-75.7, lat=45.42,
         text="Hegseth tightens US security cooperation with Canada"),
    dict(n=23, region="Americas", lon=-77.04, lat=38.9,
         text="Bessent: no new limits needed on Nvidia chip sales to"),
    dict(n=24, region="Asia", lon=139.69, lat=35.68,
         text="Japan to train live-fire at Indian facilities, a first"),
    dict(n=25, region="Europe", lon=4.35, lat=50.85,
         text="EU floats an online tax; draft budget $224bn below plan"),
    dict(n=26, region="Europe", lon=-3.7, lat=40.42,
         text="Spain to widen its bank tax to fund housing"),
    dict(n=27, region="Asia", lon=100.5, lat=13.76,
         text="Thai students protest in Bangkok for education reform"),
    dict(n=28, region="Europe", lon=12.5, lat=41.9,
         text="Ex-Italian police chief De Gennaro dies amid mafia probe"),
    dict(n=29, region="Europe", lon=19.4, lat=52.0,
         text="Swedish Gripen \u2018could not detect\u2019 missile over Poland"),
    dict(n=30, region="Europe", lon=-77.04, lat=38.9,
         text="Melania Trump presses for more Russia-Ukraine ceasefires"),
    dict(n=31, region="Europe", lon=32.6, lat=46.6,
         text="Oleshkky ceasefire holds; Zelenskyy eyes G20 talks"),
    dict(n=32, region="Americas", lon=34.47, lat=31.5,
         text="Macklemore gives a single's profits to Gaza recovery"),
    dict(n=33, region="Oceania", lon=174.78, lat=-41.29,
         text="India face New Zealand in a windy Wellington Test"),
    dict(n=34, region="Oceania", lon=151.22, lat=-33.89,
         text="Pat Cummins keeps Australia's Test captaincy"),
    dict(n=35, region="Asia", lon=39.17, lat=21.49,
         text="Air India extends its Jeddah suspension to 24 Nov"),
    dict(n=36, region="World", lon=30.71, lat=36.90,
         text="COP31 AI pledge fails to draw big US tech firms"),
]

STATS = [
    ("0", "deals agreed at COP31"),
    ("16", "crew evacuated from Sparta II"),
    ("11", "killed in Sinaloa violence"),
    ("2", "US drones the IRGC says it downed"),
    ("5", "Estonia crossings to shut on 1 Dec"),
    ("700,000", "displaced in southern Ethiopia"),
]

REGIONS = [("EUROPE", 11, BLUE), ("AMERICAS", 8, MAROON),
           ("ASIA", 5, ORANGE), ("MIDDLE EAST", 6, OLIVE),
           ("AFRICA", 3, GREEN), ("OCEANIA", 2, TEAL),
           ("WORLD", 1, (90, 90, 90))]

ALL_STORIES = HEROES + GRID + ALSO

def region_counts():
    counts = {}
    for s in ALL_STORIES:
        counts[s["region"]] = counts.get(s["region"], 0) + 1
    return counts

# ---------------------------------------------------------------- art
# v6: every composition is painted on its own layer exactly (w, h)
# and pasted into place, so no art pixel can ever leave its rect
# (the v3 lesson: arcs / tall elements used to bleed over kickers).
# All coordinates inside the art functions are LOCAL (0..w, 0..h).
# The red tag and (for heroes) the black caption are drawn by
# draw_hero / draw_grid_cell on top of the pasted layer.
# No external images, no pixel of the example is copied — only
# richer code-drawn scenes in the same newspaper palette.

_F_CLK = font(SANS_B, 7)   # clock numerals
_F_CLK2 = font(SANS_B, 8)

def _layer(w, h):
    img = Image.new("RGB", (int(w), int(h)), (0, 0, 0))
    return img, ImageDraw.Draw(img)

def _paste(d, x, y, layer):
    d._image.paste(layer, (int(x), int(y)))

def _lerp(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))

def _vgrad(ld, w, h, stops):
    """Vertical gradient through [(pos 0..1, colour), ...]."""
    w, h = int(w), int(h)
    for yy in range(h):
        t = yy / max(1, h - 1)
        col = stops[-1][1]
        if t <= stops[0][0]:
            col = stops[0][1]
        else:
            for i in range(len(stops) - 1):
                p0, c0 = stops[i]
                p1, c1 = stops[i + 1]
                if p0 <= t <= p1:
                    f = 0.0 if p1 == p0 else (t - p0) / (p1 - p0)
                    col = _lerp(c0, c1, f)
                    break
        ld.line([(0, yy), (w - 1, yy)], fill=col)

def _flame(ld, cx, base, fw, fh):
    """Three-layer flame (red outer, orange mid, yellow core)."""
    outer = [(cx - fw / 2, base), (cx - fw * 0.28, base - fh * 0.55),
             (cx - fw * 0.08, base - fh * 0.80), (cx, base - fh),
             (cx + fw * 0.12, base - fh * 0.72),
             (cx + fw * 0.30, base - fh * 0.45), (cx + fw / 2, base)]
    ld.polygon(outer, fill=(232, 60, 10))
    for s, col in ((0.62, (255, 140, 20)), (0.34, (255, 210, 60))):
        pts = [(cx + (px - cx) * s, base + (py - base) * s)
               for px, py in outer]
        ld.polygon(pts, fill=col)

def _puff(ld, cx, cy, r, col):
    ld.ellipse([cx - r, cy - r * 0.8, cx + r, cy + r * 0.8], fill=col)

def _spark(ld, cx, cy, r, col):
    k = 0.28
    ld.polygon([(cx, cy - r), (cx + r * k, cy - r * k), (cx + r, cy),
                (cx + r * k, cy + r * k), (cx, cy + r),
                (cx - r * k, cy + r * k), (cx - r, cy),
                (cx - r * k, cy - r * k)], fill=col)

def _wave(ld, x0, x1, ybase, amp, col, width=1):
    pts = []
    xx, k = x0, 0
    while xx <= x1:
        pts.append((xx, ybase + amp * math.sin(k * 0.9)))
        xx += 4
        k += 1
    if len(pts) > 1:
        ld.line(pts, fill=col, width=width)

def art_cop31(d, x, y, w, h):
    # Antalya: presidium hall — spotlight cones, curtains, flag
    # row, big wall clock with numerals, two delegate rows with
    # varied heads, presidium desk with nameplates + documents.
    lay, ld = _layer(w, h)
    _vgrad(ld, w, h, [(0.0, (14, 24, 52)), (0.6, (26, 44, 84)),
                      (1.0, (40, 32, 24))])
    ld.rectangle([0, 0, w, 10], fill=(10, 18, 40))
    # spotlight cones from the ceiling
    ld.polygon([(70, 0), (130, 0), (160, 70), (40, 70)],
               fill=(52, 74, 124))
    ld.polygon([(200, 0), (250, 0), (280, 70), (180, 70)],
               fill=(48, 68, 116))
    # curtains, left and right edges
    for cx0 in (0, w - 14):
        ld.rectangle([cx0, 0, cx0 + 14, h], fill=(96, 22, 30))
        for fx in (4, 9):
            ld.line([(cx0 + fx, 0), (cx0 + fx, h)], fill=(70, 14, 22),
                    width=1)
    # small national flags on the back wall
    flag_cols = [RED, BLUE, GREEN, (255, 210, 0), (255, 255, 255), TEAL]
    for i, col in enumerate(flag_cols):
        fx = 120 + i * 20
        ld.line([(fx, 18), (fx, 30)], fill=(150, 150, 150), width=1)
        ld.rectangle([fx, 18, fx + 12, 25], fill=col,
                     outline=(200, 200, 200))
    # big wall clock, top right, with numerals 12/3/6/9
    ccx, ccy, cr = w * 0.86, 34, 25
    ld.ellipse([ccx - cr + 2, ccy - cr + 2, ccx + cr + 2, ccy + cr + 2],
               fill=(10, 16, 32))
    ld.ellipse([ccx - cr, ccy - cr, ccx + cr, ccy + cr], fill=PAPER,
               outline=INK, width=2)
    ld.ellipse([ccx - cr + 4, ccy - cr + 4, ccx + cr - 4, ccy + cr - 4],
               outline=(200, 200, 200))
    for k in range(12):
        ang = math.radians(k * 30)
        px = ccx + math.cos(ang) * cr * 0.80
        py = ccy + math.sin(ang) * cr * 0.80
        ld.ellipse([px - 1.5, py - 1.5, px + 1.5, py + 1.5], fill=INK)
    for num, ang in (("12", -90), ("3", 0), ("6", 90), ("9", 180)):
        a = math.radians(ang)
        px = ccx + math.cos(a) * cr * 0.58
        py = ccy + math.sin(a) * cr * 0.58
        ld.text((px, py), num, font=_F_CLK, fill=INK, anchor="mm")
    a11 = math.radians(11 * 30 - 90)
    ld.line([ccx, ccy, ccx + math.cos(a11) * cr * 0.48,
             ccy + math.sin(a11) * cr * 0.48], fill=INK, width=3)
    a4 = math.radians(4 * 30 - 90)
    ld.line([ccx, ccy, ccx + math.cos(a4) * cr * 0.72,
             ccy + math.sin(a4) * cr * 0.72], fill=RED, width=3)
    ld.ellipse([ccx - 3, ccy - 3, ccx + 3, ccy + 3], fill=INK)
    # back row of delegates: smaller heads, varied skin + hair
    skins = [(232, 214, 180), (210, 180, 140), (240, 220, 195),
             (200, 170, 130), (232, 214, 180), (220, 190, 160)]
    hairs = [(40, 30, 20), (150, 150, 150), (20, 20, 25),
             (210, 180, 120), (30, 25, 18), (120, 120, 120)]
    suits = [(24, 42, 78), (50, 50, 55), (110, 30, 40),
             (14, 90, 90), (24, 42, 78), (90, 90, 95)]
    for i in range(6):
        cx = 30 + i * 32
        cy = 42 + (2 if i % 2 else -2)
        ld.rectangle([cx - 10, cy + 5, cx + 10, 55], fill=suits[i])
        ld.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=skins[i])
        ld.ellipse([cx - 5, cy - 5, cx + 5, cy - 1], fill=hairs[i])
    # front row: larger heads, varied heights
    for i in range(5):
        cx = 36 + i * 46
        cy = 60 + (2 if i % 2 else -1)
        ld.rectangle([cx - 12, cy + 6, cx + 12, 72],
                     fill=suits[(i + 2) % 6])
        ld.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=skins[(i + 1) % 6])
        ld.ellipse([cx - 7, cy - 7, cx + 7, cy - 2], fill=hairs[(i + 3) % 6])
    # presidium desk: top surface, front panel, gold trim
    ld.rectangle([6, 70, w - 6, 76], fill=(150, 104, 58))
    ld.rectangle([6, 76, w - 6, 98], fill=(110, 74, 40))
    for px in (60, 120, 180, 240, 300):
        ld.line([(px, 78), (px, 96)], fill=(88, 58, 30), width=1)
    ld.line([(6, 76), (w - 6, 76)], fill=(200, 160, 80), width=1)
    # nameplates standing on the desk, with text lines
    for cx in (59, 105, 151, 197, 243):
        ld.rectangle([cx - 10, 63, cx + 10, 70], fill=(245, 242, 230),
                     outline=(120, 110, 90))
        ld.line([(cx - 7, 65.5), (cx + 7, 65.5)], fill=(90, 80, 60),
                width=1)
        ld.line([(cx - 7, 68), (cx + 7, 68)], fill=(140, 130, 110),
                width=1)
    # documents + water glasses on the desk top
    for dx0 in (14, 252, 282):
        ld.polygon([(dx0, 71), (dx0 + 14, 71), (dx0 + 12, 75),
                    (dx0 - 2, 75)], fill=(250, 248, 240))
        ld.line([(dx0 + 2, 73), (dx0 + 10, 73)], fill=(170, 170, 170),
                width=1)
    for gx in (140, 230):
        ld.rectangle([gx, 71, gx + 4, 76], fill=(200, 220, 235),
                     outline=(120, 130, 140))
    # floor
    ld.rectangle([0, 98, w, h], fill=(24, 20, 16))
    ld.line([(0, 98), (w, 98)], fill=(150, 120, 70), width=1)
    _paste(d, x, y, lay)

def art_ship(d, x, y, w, h):
    # Gulf of Finland: cargo ship ablaze at night — layered
    # flames, drifting smoke, moon + stars, two drones, wavy sea
    # with the fire's reflection under the hull.
    lay, ld = _layer(w, h)
    _vgrad(ld, w, h, [(0.0, (8, 14, 40)), (0.6, (14, 22, 58)),
                      (1.0, (18, 28, 66))])
    for sx, sy in [(20, 10), (45, 22), (90, 8), (120, 16), (200, 10),
                   (240, 22), (300, 8), (105, 30), (225, 32)]:
        ld.ellipse([sx, sy, sx + 2, sy + 2], fill=(255, 255, 255))
    _spark(ld, 70, 14, 3, (255, 255, 255))
    _spark(ld, 260, 16, 3, (255, 255, 255))
    # moon with glow + craters
    ld.ellipse([272 - 16, 20 - 16, 272 + 16, 20 + 16], fill=(44, 52, 88))
    ld.ellipse([272 - 11, 20 - 11, 272 + 11, 20 + 11],
               fill=(238, 228, 196))
    for cx, cy in [(268, 17), (276, 23), (270, 24)]:
        ld.ellipse([cx - 1.5, cy - 1.5, cx + 1.5, cy + 1.5],
                   fill=(210, 198, 165))
    # two small drone silhouettes with a red light each
    for dx, dy, s in [(58, 20, 1.0), (150, 14, 0.8)]:
        ld.line([(dx - 10 * s, dy), (dx + 10 * s, dy)], fill=(20, 20, 28),
                width=2)
        ld.line([(dx, dy - 7 * s), (dx, dy + 7 * s)], fill=(20, 20, 28),
                width=2)
        ld.ellipse([dx - 4 * s, dy - 2 * s, dx + 4 * s, dy + 2 * s],
                   fill=(30, 30, 40))
        ld.ellipse([dx - 1.5, dy + 3 * s, dx + 1.5, dy + 3 * s + 3],
                   fill=(255, 60, 50))
    # smoke drifting up and to the left, layered greys
    for cx, cy, r, col in [(128, 34, 9, (110, 110, 120)),
                           (146, 24, 12, (130, 130, 140)),
                           (164, 30, 10, (105, 105, 115)),
                           (182, 20, 9, (125, 125, 135)),
                           (112, 26, 7, (120, 120, 130)),
                           (198, 28, 7, (115, 115, 125))]:
        _puff(ld, cx, cy, r, col)
    # fire glow behind the containers
    ld.ellipse([110, 38, 195, 60], fill=(150, 70, 18))
    # colourful containers, two tiers, with rib lines
    conts = [(55, 85, (200, 40, 40)), (85, 115, (40, 80, 160)),
             (115, 145, (40, 140, 80)), (145, 175, (220, 180, 40)),
             (175, 205, (40, 150, 150)), (205, 235, (180, 50, 50))]
    for x0, x1, col in conts:
        ld.rectangle([x0, 46, x1, 64], fill=col)
        for rx in range(x0 + 7, x1, 7):
            ld.line([(rx, 48), (rx, 62)], fill=(0, 0, 0), width=1)
    ld.rectangle([60, 36, 90, 46], fill=(40, 80, 160))
    ld.rectangle([95, 36, 125, 46], fill=(200, 40, 40))
    for rx in range(67, 90, 7):
        ld.line([(rx, 38), (rx, 44)], fill=(0, 0, 0), width=1)
    for rx in range(102, 125, 7):
        ld.line([(rx, 38), (rx, 44)], fill=(0, 0, 0), width=1)
    # layered flames of varying heights
    for cx, base, fw, fh in [(75, 38, 24, 26), (120, 38, 26, 30),
                             (160, 46, 28, 32), (200, 46, 22, 24)]:
        _flame(ld, cx, base, fw, fh)
    # embers rising above the flames
    for ex, ey, col in [(100, 22, (255, 180, 60)), (140, 14, (255, 140, 40)),
                        (170, 18, (255, 200, 90)), (190, 26, (255, 150, 50)),
                        (85, 28, (255, 170, 70))]:
        ld.ellipse([ex, ey, ex + 2, ey + 2], fill=col)
    # bridge tower, right: lit windows, red stripe, mast
    ld.rectangle([250, 28, 296, 64], fill=(235, 235, 230),
                 outline=(180, 180, 175))
    ld.rectangle([250, 28, 296, 32], fill=(180, 40, 40))
    for wy in (34, 42, 50):
        for wx in (256, 270, 284):
            col = (255, 210, 90) if (wx + wy) % 3 else (90, 110, 130)
            ld.rectangle([wx, wy, wx + 10, wy + 5], fill=col)
    ld.line([(273, 28), (273, 18)], fill=(60, 60, 60), width=2)
    ld.ellipse([271, 16, 275, 20], fill=(255, 60, 50))
    # hull + red waterline + portholes
    ld.polygon([(6, 64), (311, 64), (294, 88), (22, 88)],
               fill=(10, 12, 26))
    ld.polygon([(8, 78), (309, 78), (303, 84), (14, 84)],
               fill=(150, 32, 28))
    for px in (40, 80, 120, 200, 260):
        ld.ellipse([px - 1.5, 68.5, px + 1.5, 71.5], fill=(200, 200, 180))
    # sea: two bands, waves, foam, fire reflection
    ld.rectangle([0, 88, w, 96], fill=(14, 34, 66))
    ld.rectangle([0, 96, w, h], fill=(10, 26, 52))
    for rx in range(112, 200, 8):
        ln = 6 + (rx * 7) % 7
        col = [(255, 150, 40), (255, 200, 80), (220, 90, 25)][(rx // 8) % 3]
        ld.line([(rx, 90), (rx, 90 + ln)], fill=col, width=3)
    _wave(ld, 0, w, 92, 1.5, (90, 140, 190))
    _wave(ld, 0, w, 97, 1.5, (70, 110, 160))
    _wave(ld, 0, w, 102, 1.5, (120, 170, 210))
    for fx in (30, 90, 230, 280):
        ld.line([(fx, 89), (fx + 14, 89)], fill=(220, 230, 240), width=1)
    _paste(d, x, y, lay)

def art_hormuz(d, x, y, w, h):
    # Hormuz: three-tone blue strait between textured sandy
    # coasts, a detailed ship with reflection, two drones with
    # rotors + dotted trails, concentric radar arcs kept inside
    # the rect, birds and clouds as accents.
    lay, ld = _layer(w, h)
    _vgrad(ld, w, h, [(0.0, (26, 96, 155)), (0.5, (30, 112, 178)),
                      (1.0, (16, 72, 122))])
    # sandy coasts, left and right
    ld.polygon([(0, 0), (70, 0), (86, 34), (64, 64), (78, 104), (0, 104)],
               fill=SAND)
    ld.polygon([(w, 0), (250, 0), (232, 30), (254, 62), (238, 104),
                (w, 104)], fill=SAND)
    for sx, sy in [(15, 20), (25, 45), (20, 70), (35, 90), (45, 15),
                   (55, 55), (290, 18), (280, 45), (295, 70), (270, 88),
                   (300, 95)]:
        ld.line([(sx, sy), (sx + 8, sy + 4)], fill=(178, 148, 98), width=1)
    ld.line([(70, 0), (86, 34), (64, 64), (78, 104)], fill=(150, 120, 80),
            width=2)
    ld.line([(250, 0), (232, 30), (254, 62), (238, 104)],
            fill=(150, 120, 80), width=2)
    # clouds + birds
    _puff(ld, 60, 10, 8, (235, 240, 245))
    _puff(ld, 72, 8, 6, (235, 240, 245))
    _puff(ld, 200, 10, 7, (235, 240, 245))
    for bx, by in [(88, 16), (108, 10)]:
        ld.line([(bx, by + 3), (bx + 4, by), (bx + 8, by + 3)],
                fill=(30, 40, 55), width=1)
    # sea waves
    for wy in (28, 48, 68, 88):
        _wave(ld, 80, 240, wy, 1.5, (160, 205, 235))
    # ship: bridge, containers, funnel, hull, reflection
    ld.rectangle([118, 58, 134, 74], fill=(240, 240, 235))
    ld.rectangle([121, 61, 127, 66], fill=(255, 210, 90))
    ld.rectangle([121, 68, 127, 72], fill=(255, 210, 90))
    ld.line([(126, 58), (126, 50)], fill=(60, 60, 60), width=1)
    ld.polygon([(126, 50), (126, 55), (132, 53)], fill=RED)
    ship_conts = [(130, 150, (110, 116, 128)), (152, 170, (200, 40, 40)),
                  (172, 190, (40, 80, 160)), (192, 208, (40, 150, 150))]
    for x0, x1, col in ship_conts:
        ld.rectangle([x0, 62, x1, 74], fill=col)
        for rx in range(x0 + 6, x1, 6):
            ld.line([(rx, 64), (rx, 72)], fill=(0, 0, 0), width=1)
    ld.rectangle([196, 50, 207, 62], fill=(200, 60, 40))
    ld.rectangle([196, 50, 207, 54], fill=(30, 30, 30))
    ld.polygon([(112, 74), (216, 74), (206, 90), (122, 90)],
               fill=(16, 20, 34))
    ld.polygon([(114, 82), (214, 82), (210, 86), (118, 86)],
               fill=(150, 32, 28))
    ld.polygon([(122, 92), (206, 92), (200, 100), (128, 100)],
               fill=(44, 84, 124))
    ld.line([(130, 95), (198, 95)], fill=(120, 170, 205), width=1)
    # buoy, left of the ship
    ld.rectangle([93, 82, 99, 88], fill=RED)
    ld.rectangle([93, 84, 99, 86], fill=(255, 255, 255))
    ld.line([(96, 82), (96, 78)], fill=(60, 60, 60), width=1)
    # drones with bodies, rotor arms + discs, dotted trails
    for dx, dy, s in [(150, 26, 1.0), (220, 42, 0.8)]:
        for ex, ey in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
            ld.line([(dx, dy), (dx + ex * 9 * s, dy + ey * 7 * s)],
                    fill=(25, 25, 35), width=2)
            ld.ellipse([dx + ex * 9 * s - 4 * s, dy + ey * 7 * s - 1.5,
                        dx + ex * 9 * s + 4 * s, dy + ey * 7 * s + 1.5],
                       fill=(70, 70, 80), outline=(150, 150, 160))
        ld.ellipse([dx - 7 * s, dy - 3 * s, dx + 7 * s, dy + 3 * s],
                   fill=(25, 25, 35))
        ld.ellipse([dx - 1.5, dy + 3 * s, dx + 1.5, dy + 3 * s + 3],
                   fill=(255, 60, 50))
    for k in range(1, 7):
        ld.ellipse([136 - 9 * k - 1.5, 30 + 2 * k - 1.5,
                    136 - 9 * k + 1.5, 30 + 2 * k + 1.5],
                   fill=(255, 255, 255))
    for k in range(1, 5):
        ld.ellipse([212 - 8 * k - 1.5, 46 + 1.5 * k - 1.5,
                    212 - 8 * k + 1.5, 46 + 1.5 * k + 1.5],
                   fill=(255, 255, 255))
    # radar arcs, concentric and fully inside the rect
    ax, ay = 286, 78
    for r in (9, 15, 21):
        ld.ellipse([ax - r, ay - r, ax + r, ay + r],
                   outline=(255, 255, 255), width=1)
    ld.line([(ax, ay), (ax + 10, ay - 10)], fill=(255, 255, 255), width=1)
    ld.ellipse([ax - 3, ay - 3, ax + 3, ay + 3], fill=RED)
    _paste(d, x, y, lay)


# Grid art: full-bleed strips, local coords (0..w, 0..h), same
# layer-then-paste containment as the heroes.
def art_mountains(d, x, y, w, h):
    # Sinaloa: three mountain layers under stars, snow caps,
    # fire glowing in the valley + a smoke wisp + pines.
    lay, ld = _layer(w, h)
    _vgrad(ld, w, h, [(0.0, (14, 16, 40)), (0.6, (24, 26, 58)),
                      (1.0, (40, 30, 50))])
    for sx, sy in [(12, 6), (48, 4), (95, 8), (140, 5), (170, 10)]:
        ld.ellipse([sx, sy, sx + 2, sy + 2], fill=(255, 255, 255))
    _spark(ld, 125, 7, 2.5, (255, 255, 255))
    ld.ellipse([150 - 5, 5, 150 + 5, 15], fill=(235, 230, 210))
    # far, mid, near ridges
    ld.polygon([(0, h), (40, 18), (75, h)], fill=(52, 58, 96))
    ld.polygon([(60, h), (110, 14), (160, h)], fill=(46, 52, 88))
    ld.polygon([(120, h), (165, 20), (w, h)], fill=(70, 52, 60))
    # snow caps on the two main peaks
    ld.polygon([(104, 20), (110, 14), (116, 20)], fill=(255, 240, 220))
    ld.polygon([(160, 25), (165, 20), (170, 25)], fill=(255, 240, 220))
    # valley fire: glow + two layered flames + smoke wisp
    ld.ellipse([82, 34, 112, 48], fill=(200, 80, 20))
    _flame(ld, 92, 46, 10, 12)
    _flame(ld, 102, 46, 8, 9)
    _puff(ld, 97, 30, 4, (110, 110, 120))
    _puff(ld, 100, 24, 3, (130, 130, 140))
    # dark foreground ridge + two pines
    ld.polygon([(0, h), (0, 40), (30, 44), (60, 40), (90, 44), (120, 40),
                (150, 44), (w, 40), (w, h)], fill=(20, 18, 30))
    for px in (18, 172):
        ld.polygon([(px - 4, 42), (px, 30), (px + 4, 42)], fill=(16, 40, 26))
        ld.polygon([(px - 3, 36), (px, 28), (px + 3, 36)], fill=(20, 48, 30))
    _paste(d, x, y, lay)

def art_border(d, x, y, w, h):
    # Estonia: perspective road, red-white barrier, blue sign,
    # wire fence on the left, guard booth on the right.
    lay, ld = _layer(w, h)
    _vgrad(ld, w, h, [(0.0, (198, 220, 235)), (1.0, (222, 232, 240))])
    ld.polygon([(0, 28), (40, 20), (90, 24), (140, 20), (w, 26), (w, 28),
                (0, 28)], fill=(140, 160, 140))
    ld.rectangle([0, 28, w, h], fill=(150, 180, 130))
    # road in perspective
    ld.polygon([(70, h), (88, 26), (99, 26), (117, h)], fill=(96, 96, 102))
    ld.line([(88, 26), (70, h)], fill=(255, 255, 255), width=1)
    ld.line([(99, 26), (117, h)], fill=(255, 255, 255), width=1)
    for dy in (44, 36, 29):
        ld.line([(93, dy), (93, dy - 4)], fill=(255, 255, 255), width=2)
    # wire fence, left
    for fx in (8, 24, 40):
        ld.line([(fx, 26), (fx, 42)], fill=(90, 90, 90), width=2)
    for wy in (30, 36):
        ld.line([(6, wy), (44, wy)], fill=(120, 120, 120), width=1)
    ld.line([(6, 30), (44, 36)], fill=(120, 120, 120), width=1)
    ld.line([(6, 36), (44, 30)], fill=(120, 120, 120), width=1)
    # red-white striped barrier across the road
    by = 30
    for i in range(9):
        col = RED if i % 2 == 0 else (255, 255, 255)
        ld.rectangle([8 + i * 19, by, 8 + (i + 1) * 19, by + 6], fill=col,
                     outline=(60, 60, 60))
    for px in (12, 172):
        ld.rectangle([px, by + 6, px + 3, 44], fill=(60, 60, 60))
    # blue sign, top right, with a white arrow
    ld.rectangle([150, 4, 180, 16], fill=BLUE, outline=(255, 255, 255),
                 width=1)
    ld.polygon([(154, 10), (172, 10), (172, 8), (178, 10), (172, 12),
                (172, 10)], fill=(255, 255, 255))
    ld.line([(165, 16), (165, 26)], fill=(120, 120, 120), width=2)
    # guard booth, bottom right
    ld.rectangle([150, 32, 176, 44], fill=(240, 240, 235),
                 outline=(150, 150, 150))
    ld.rectangle([150, 32, 176, 35], fill=(90, 110, 140))
    ld.rectangle([156, 37, 164, 42], fill=(150, 200, 225))
    _paste(d, x, y, lay)

def art_icu(d, x, y, w, h):
    # Brasilia: hospital block with lit windows, proportional
    # red cross in a white disc, entrance canopy, small ambulance.
    lay, ld = _layer(w, h)
    _vgrad(ld, w, h, [(0.0, (226, 234, 238)), (1.0, (205, 218, 228))])
    ld.rectangle([14, 12, 150, 44], fill=(250, 250, 250),
                 outline=(170, 180, 188), width=1)
    ld.rectangle([60, 6, 100, 12], fill=(180, 190, 196))
    ld.rectangle([150, 20, 178, 44], fill=(238, 242, 245),
                 outline=(170, 180, 188), width=1)
    # windows: lit yellow / pale blue, skipping the cross column
    for r, wy in enumerate((16, 27)):
        for c, wx in enumerate((20, 38, 56, 108, 126)):
            col = (255, 210, 90) if (r + c) % 2 == 0 else (150, 200, 225)
            ld.rectangle([wx, wy, wx + 10, wy + 7], fill=col,
                         outline=(190, 195, 200))
    for wy in (24, 33):
        ld.rectangle([156, wy, 164, wy + 6], fill=(255, 210, 90),
                     outline=(190, 195, 200))
    # red cross emblem in a white disc, centre
    ld.ellipse([70, 12, 94, 36], fill=(255, 255, 255),
               outline=(200, 200, 200))
    ld.rectangle([79, 15, 85, 33], fill=RED)
    ld.rectangle([73, 21, 91, 27], fill=RED)
    # entrance canopy + door, ground strip
    ld.rectangle([66, 38, 98, 42], fill=(120, 140, 160))
    ld.rectangle([76, 42, 88, 48], fill=(90, 110, 130))
    ld.rectangle([0, 44, w, h], fill=(160, 175, 185))
    # ambulance, bottom left
    ld.rectangle([10, 34, 58, 44], fill=(255, 255, 255),
                 outline=(120, 130, 140))
    ld.polygon([(58, 34), (66, 38), (66, 44), (58, 44)], fill=(240, 240, 240),
               outline=(120, 130, 140))
    ld.rectangle([34, 32, 42, 34], fill=RED)
    ld.rectangle([28, 37, 32, 43], fill=RED)
    ld.rectangle([24, 39, 36, 43], fill=RED)
    ld.ellipse([16, 43, 22, 48], fill=(20, 20, 20))
    ld.ellipse([54, 43, 60, 48], fill=(20, 20, 20))
    # small tree, right
    ld.line([(172, 44), (172, 36)], fill=(90, 70, 50), width=2)
    ld.ellipse([167, 29, 177, 39], fill=(60, 140, 80))
    _paste(d, x, y, lay)

def art_globe_flags(d, x, y, w, h):
    # Paris: globe with longitude/latitude + land blobs on a
    # stand, two waving flags, UN slab silhouette bottom right.
    lay, ld = _layer(w, h)
    _vgrad(ld, w, h, [(0.0, (200, 222, 236)), (1.0, (225, 235, 242))])
    _puff(ld, 100, 8, 6, (255, 255, 255))
    _puff(ld, 112, 7, 5, (255, 255, 255))
    # UN slab silhouette, bottom right
    ld.rectangle([138, 20, 178, 46], fill=(90, 110, 140))
    ld.rectangle([120, 32, 138, 46], fill=(110, 130, 160))
    for wy in (24, 30, 36, 42):
        ld.line([(140, wy), (176, wy)], fill=(150, 170, 200), width=1)
    for wx in (148, 158, 168):
        ld.line([(wx, 20), (wx, 46)], fill=(150, 170, 200), width=1)
    # globe, centre-left, on a stand
    cx, cy, r = 66, 24, 16
    ld.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(70, 140, 190),
               outline=(255, 255, 255), width=2)
    ld.ellipse([cx - r * 0.55, cy - r, cx + r * 0.55, cy + r],
               outline=(255, 255, 255), width=1)
    ld.line([cx - r, cy, cx + r, cy], fill=(255, 255, 255), width=1)
    ld.polygon([(cx - 8, cy - 6), (cx - 2, cy - 8), (cx + 2, cy - 3),
                (cx - 4, cy + 1)], fill=(60, 130, 70))
    ld.polygon([(cx + 2, cy + 4), (cx + 9, cy + 2), (cx + 8, cy + 8),
                (cx + 1, cy + 9)], fill=(60, 130, 70))
    ld.polygon([(58, 40), (74, 40), (70, 46), (62, 46)], fill=(120, 90, 50))
    # waving flags, left red and right blue
    for fx, col, flip in [(14, RED, 1), (172, BLUE, -1)]:
        ld.rectangle([fx, 8, fx + 2, 44], fill=(120, 80, 40))
        if flip == 1:
            ld.polygon([(fx + 2, 8), (fx + 18, 10), (fx + 16, 18),
                        (fx + 2, 16)], fill=col)
        else:
            ld.polygon([(fx, 8), (fx - 16, 10), (fx - 14, 18),
                        (fx, 16)], fill=col)
    _paste(d, x, y, lay)

def art_bomber(d, x, y, w, h):
    # Manila: four-band sunset, glowing sun, dotted trail,
    # detailed bomber silhouette (wings, tail, engines, cockpit).
    lay, ld = _layer(w, h)
    bands = [((0.0, 0.25), (250, 190, 90)), ((0.25, 0.5), (240, 150, 60)),
             ((0.5, 0.75), (225, 110, 40)), ((0.75, 1.0), (200, 80, 30))]
    for (p0, p1), col in bands:
        ld.rectangle([0, h * p0, w, h * p1], fill=col)
    ld.ellipse([158 - 11, 20 - 11, 158 + 11, 20 + 11],
               fill=(255, 210, 120))
    ld.ellipse([158 - 8, 20 - 8, 158 + 8, 20 + 8], fill=(255, 240, 200))
    _puff(ld, 40, 10, 7, (255, 220, 180))
    _puff(ld, 60, 9, 5, (255, 220, 180))
    _puff(ld, 120, 34, 6, (245, 190, 150))
    # dotted trail behind the bomber
    for k in range(8):
        ld.ellipse([20 + k * 9 - 1.5, 26 - k * 0.4 - 1.5,
                    20 + k * 9 + 1.5, 26 - k * 0.4 + 1.5],
                   fill=(255, 255, 255))
    # bomber, nose right
    px, py = 120, 24
    ld.polygon([(px - 25, py), (px + 30, py - 3), (px + 36, py),
                (px + 30, py + 3)], fill=(28, 28, 38))
    ld.polygon([(px - 8, py - 2), (px + 2, py - 14), (px + 8, py - 2)],
               fill=(28, 28, 38))
    ld.polygon([(px - 12, py + 2), (px - 2, py + 14), (px + 4, py + 2)],
               fill=(28, 28, 38))
    ld.polygon([(px - 25, py - 2), (px - 29, py - 10), (px - 23, py - 2)],
               fill=(28, 28, 38))
    ld.rectangle([px + 2, py + 3, px + 10, py + 6], fill=(28, 28, 38))
    ld.rectangle([px + 16, py + 3, px + 24, py + 6], fill=(28, 28, 38))
    ld.ellipse([px + 20, py - 3, px + 28, py], fill=(120, 140, 170))
    # birds + dark hills at the bottom
    for bx, by in [(60, 14), (170, 12)]:
        ld.line([(bx, by + 2), (bx + 3, by), (bx + 6, by + 2)],
                fill=(60, 30, 20), width=1)
    ld.polygon([(0, h), (0, 44), (50, 40), (110, 44), (160, 41), (w, 44),
                (w, h)], fill=(60, 30, 20))
    _paste(d, x, y, lay)

def art_city_smoke(d, x, y, w, h):
    # Gaza: two-layer night skyline with lit windows, smoke
    # plumes, a rooftop fire glow, moon and stars.
    lay, ld = _layer(w, h)
    _vgrad(ld, w, h, [(0.0, (16, 24, 52)), (1.0, (24, 32, 66))])
    for sx, sy in [(10, 6), (40, 10), (90, 5), (120, 9), (150, 6)]:
        ld.ellipse([sx, sy, sx + 2, sy + 2], fill=(255, 255, 255))
    ld.ellipse([160 - 9, 10 - 9, 160 + 9, 10 + 9], fill=(70, 70, 100))
    ld.ellipse([160 - 6, 10 - 6, 160 + 6, 10 + 6], fill=(240, 230, 200))
    # far skyline
    for bx0, bw, bh in [(0, 26, 20), (28, 22, 26), (52, 24, 18),
                        (78, 22, 24), (102, 24, 20), (128, 22, 26),
                        (152, 20, 18), (174, 13, 22)]:
        ld.rectangle([bx0, h - bh, bx0 + bw, h], fill=(38, 44, 74))
    # near skyline with lit windows
    wins = []
    for bx0, bw, bh in [(0, 20, 30), (22, 18, 38), (42, 20, 28),
                        (64, 18, 40), (84, 20, 32), (106, 18, 36),
                        (126, 20, 28), (148, 18, 38), (168, 19, 30)]:
        ld.rectangle([bx0, h - bh, bx0 + bw, h], fill=(22, 26, 48))
        for wy in (0.25, 0.55, 0.8):
            for wx in (0.25, 0.65):
                if (int(bx0 + wy * 37 + wx * 13)) % 3:
                    wins.append((bx0 + bw * wx, h - bh + bh * wy))
    for wx, wy in wins:
        ld.rectangle([wx, wy, wx + 3, wy + 3], fill=(255, 210, 90))
    # smoke plumes rising from two rooftops
    for cx, cy, r, col in [(60, 14, 5, (110, 110, 120)),
                           (56, 8, 6, (130, 130, 140)),
                           (130, 16, 5, (110, 110, 120)),
                           (134, 10, 6, (125, 125, 135)),
                           (126, 6, 4, (140, 140, 150))]:
        _puff(ld, cx, cy, r, col)
    # rooftop fire glow + tiny flame
    ld.ellipse([90, 26, 102, 34], fill=(200, 90, 20))
    _flame(ld, 96, 32, 7, 8)
    _paste(d, x, y, lay)

def art_bridge(d, x, y, w, h):
    # Patna: arched bridge with suspension cables, deck blocks,
    # river with ripples and a small sailboat.
    lay, ld = _layer(w, h)
    _vgrad(ld, w, h, [(0.0, (178, 214, 235)), (0.7, (220, 230, 235)),
                      (1.0, (240, 220, 190))])
    ld.ellipse([160 - 6, 10 - 6, 160 + 6, 10 + 6], fill=(255, 240, 200))
    _puff(ld, 40, 8, 6, (255, 255, 255))
    _puff(ld, 100, 6, 5, (255, 255, 255))
    # arch (bbox fully inside the strip) + suspenders
    ld.arc([10, 2, 177, 64], start=180, end=360, fill=(140, 90, 50),
           width=4)
    ecx, ecy, rx, ry = 93.5, 33, 83.5, 31
    for sx in (40, 70, 100, 130, 160):
        t = 1 - ((sx - ecx) / rx) ** 2
        ay = ecy - ry * math.sqrt(max(0.0, t))
        ld.line([(sx, ay), (sx, 30)], fill=(140, 90, 50), width=1)
    # deck + railing + blocks
    ld.rectangle([6, 30, 181, 35], fill=(120, 80, 40))
    for px in range(12, 180, 14):
        ld.line([(px, 26), (px, 30)], fill=(120, 80, 40), width=1)
    ld.rectangle([60, 22, 74, 30], fill=RED)
    ld.rectangle([110, 23, 124, 30], fill=BLUE)
    # river + ripples + sailboat
    ld.rectangle([0, 35, w, 42], fill=(60, 130, 190))
    ld.rectangle([0, 42, w, h], fill=(40, 100, 160))
    for wx, wy in [(20, 39), (90, 44), (140, 39), (60, 46), (120, 46)]:
        ld.line([(wx, wy), (wx + 16, wy)], fill=(255, 255, 255), width=1)
    ld.polygon([(140, 40), (162, 40), (158, 45), (144, 45)],
               fill=(90, 50, 30))
    ld.polygon([(148, 40), (148, 30), (158, 40)], fill=(255, 255, 255))
    ld.ellipse([151, 41, 153, 43], fill=(20, 20, 20))
    _paste(d, x, y, lay)

def art_warning(d, x, y, w, h):
    # Washington: plane in a pale sky, big yellow warning
    # triangle with a centred "!" on the right.
    lay, ld = _layer(w, h)
    _vgrad(ld, w, h, [(0.0, (178, 214, 235)), (1.0, (200, 225, 240))])
    for cx, cy, r in [(30, 10, 8), (70, 6, 6), (110, 12, 7)]:
        _puff(ld, cx, cy, r, (255, 255, 255))
    # speed lines behind the plane
    for sy in (20, 26, 32):
        ld.line([(8, sy), (22, sy)], fill=(255, 255, 255), width=1)
    # plane, nose right: long fuselage, swept wings, tail fin
    px, py = 58, 26
    ld.polygon([(px - 30, py), (px + 26, py - 3), (px + 32, py),
                (px + 26, py + 3)], fill=(40, 40, 50))
    ld.polygon([(px - 6, py - 2), (px + 6, py - 14), (px + 12, py - 2)],
               fill=(40, 40, 50))
    ld.polygon([(px - 8, py + 2), (px, py + 13), (px + 6, py + 2)],
               fill=(40, 40, 50))
    ld.polygon([(px - 26, py - 2), (px - 24, py - 11), (px - 18, py - 2)],
               fill=(40, 40, 50))
    ld.polygon([(px - 28, py + 2), (px - 32, py + 7), (px - 24, py + 2)],
               fill=(40, 40, 50))
    ld.rectangle([px - 10, py + 3, px - 2, py + 6], fill=(40, 40, 50))
    ld.rectangle([px + 6, py + 3, px + 14, py + 6], fill=(40, 40, 50))
    for wx in (px + 18, px + 24):
        ld.ellipse([wx, py - 1.5, wx + 2, py + 0.5], fill=(200, 220, 240))
    # warning triangle with centred "!"
    tx, ty = 150, 24
    ld.polygon([(tx, 6), (tx - 18, 38), (tx + 18, 38)], fill=(255, 210, 0),
               outline=INK, width=2)
    bang = "!"
    bw = ld.textlength(bang, font=F_Q)
    ld.text((tx - bw / 2, 12), bang, font=F_Q, fill=INK)
    _paste(d, x, y, lay)

def art_deadlock(d, x, y, w, h):
    # New York: globe left, empty chair behind a podium, red
    # "?" above it, small flag at the right edge.
    lay, ld = _layer(w, h)
    _vgrad(ld, w, h, [(0.0, (200, 220, 235)), (1.0, (215, 230, 240))])
    # globe, left
    cx, cy, r = 38, 24, 15
    ld.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(70, 140, 190),
               outline=(255, 255, 255), width=2)
    ld.ellipse([cx - r * 0.55, cy - r, cx + r * 0.55, cy + r],
               outline=(255, 255, 255), width=1)
    ld.line([cx - r, cy, cx + r, cy], fill=(255, 255, 255), width=1)
    ld.polygon([(cx - 6, cy - 5), (cx, cy - 7), (cx + 3, cy - 2),
                (cx - 3, cy + 1)], fill=(60, 130, 70))
    ld.polygon([(cx + 1, cy + 3), (cx + 7, cy + 2), (cx + 6, cy + 7),
                (cx, cy + 8)], fill=(60, 130, 70))
    # podium with microphone
    ld.polygon([(88, 44), (122, 44), (116, 30), (94, 30)], fill=(120, 90, 50))
    ld.rectangle([92, 28, 118, 32], fill=(150, 110, 70))
    ld.line([(105, 28), (105, 20)], fill=(40, 40, 40), width=1)
    ld.ellipse([103, 18, 107, 22], fill=(40, 40, 40))
    # empty chair, right of the podium
    ld.rectangle([136, 20, 140, 36], fill=(110, 74, 40))
    ld.rectangle([132, 36, 150, 40], fill=(140, 90, 50))
    ld.line([(134, 40), (134, 46)], fill=(110, 74, 40), width=2)
    ld.line([(148, 40), (148, 46)], fill=(110, 74, 40), width=2)
    # red "?" above the chair
    q = "?"
    qw = ld.textlength(q, font=F_Q)
    ld.text((141 - qw / 2, 1), q, font=F_Q, fill=RED)
    # small flag at the right edge
    ld.rectangle([178, 6, 180, 46], fill=(120, 80, 40))
    ld.polygon([(178, 6), (164, 8), (166, 15), (178, 13)], fill=RED)
    # floor line
    ld.rectangle([0, 46, w, h], fill=(170, 185, 200))
    _paste(d, x, y, lay)

def art_plant_fire(d, x, y, w, h):
    # Basra: power plant at night — chimney with smoke, main
    # block with lit windows, layered flames on the roof, fence.
    lay, ld = _layer(w, h)
    _vgrad(ld, w, h, [(0.0, (20, 20, 34)), (1.0, (30, 28, 48))])
    for sx, sy in [(50, 6), (90, 4), (140, 8), (170, 5)]:
        ld.ellipse([sx, sy, sx + 2, sy + 2], fill=(255, 255, 255))
    # chimney + smoke
    ld.rectangle([16, 14, 28, 44], fill=(80, 76, 88))
    ld.rectangle([16, 14, 28, 18], fill=(160, 50, 40))
    _puff(ld, 22, 10, 5, (110, 110, 120))
    _puff(ld, 28, 5, 6, (130, 130, 140))
    _puff(ld, 16, 3, 4, (100, 100, 110))
    # main block with lit windows
    ld.rectangle([34, 22, 178, 44], fill=(70, 66, 78))
    ld.rectangle([34, 20, 178, 22], fill=(90, 86, 98))
    for r, wy in enumerate((26, 34)):
        for c, wx in enumerate((40, 58, 76, 94, 112, 130, 148, 164)):
            if (r + c) % 3 == 2:
                col = (40, 40, 50)
            else:
                col = (255, 210, 90)
            ld.rectangle([wx, wy, wx + 8, wy + 6], fill=col)
    # annex block, right
    ld.rectangle([150, 32, 178, 44], fill=(60, 56, 68))
    # fire glow + layered flames on the roof
    for gx in (60, 100, 140):
        ld.ellipse([gx - 12, 12, gx + 12, 22], fill=(150, 70, 18))
    _flame(ld, 60, 22, 14, 14)
    _flame(ld, 100, 22, 16, 18)
    _flame(ld, 140, 22, 12, 12)
    # ground + fence
    ld.rectangle([0, 44, w, h], fill=(16, 16, 24))
    ld.line([(0, 44), (w, 44)], fill=(100, 100, 110), width=1)
    for fx in range(6, w, 20):
        ld.line([(fx, 44), (fx, 48)], fill=(100, 100, 110), width=1)
    _paste(d, x, y, lay)

GRID_ART = {"mountains": art_mountains, "border": art_border,
            "icu": art_icu, "globe_flags": art_globe_flags,
            "bomber": art_bomber, "city_smoke": art_city_smoke,
            "bridge": art_bridge, "warning": art_warning,
            "deadlock": art_deadlock, "plant_fire": art_plant_fire}
HERO_ART = {"cop31": art_cop31, "ship": art_ship,
            "hormuz": art_hormuz}

# ---------------------------------------------------------------- layout
MARGIN = 24
CW = W - 2 * MARGIN  # 976
HERO_Y0 = 188
HERO_ART_H = 104
HERO_BOX_H = 222
GRID_Y0 = 416
GRID_CELL_H = 144
GRID_ART_H = 48
MAP_Y = 736
MAP_W = 300
MAP_H = 134

def draw_art_tag(d, x, y, text, fnt, hgt):
    tw = d.textlength(text, font=fnt)
    d.rectangle([x, y, x + tw + 8, y + hgt], fill=RED)
    d.text((x + 4, y + 2), text, font=fnt, fill=(255, 255, 255))

def draw_art_cap(d, x, y_bottom, text):
    tw = d.textlength(text, font=F_CAP)
    d.rectangle([x, y_bottom - 15, x + tw + 8, y_bottom], fill=(0, 0, 0))
    d.text((x + 4, y_bottom - 13), text, font=F_CAP,
           fill=(255, 255, 255))

def draw_masthead(d):
    d.text((MARGIN, 6), "THE WORLD IN ONE DAY", font=F_MAST, fill=RED)
    right = "36 STORIES · 7 REGIONS · EVERY ONE DATED SUNDAY 22 NOVEMBER 2026"
    d.text((W - MARGIN - d.textlength(right, font=F_MAST_R), 8), right,
           font=F_MAST_R, fill=INK)
    d.text((MARGIN, 26), "Sunday 22 November 2026", font=F_DATE, fill=INK)
    sub = ("COP31 still without a deal · Russian ship ablaze in the "
           "Baltic · US drones \u2018downed\u2019 over Hormuz")
    d.text((MARGIN, 78), sub, font=F_SUB, fill=INK)
    d.line([MARGIN, 98, W - MARGIN, 98], fill=INK, width=2)

def draw_stats(d):
    bw = CW / 6
    y0, y1 = 104, 156
    for i, (num, label) in enumerate(STATS):
        x0 = MARGIN + i * bw
        if i:
            d.line([x0, y0 + 4, x0, y1 - 4], fill=GREY, width=1)
        nw = d.textlength(num, font=F_STAT_N)
        d.text((x0 + (bw - nw) / 2, y0 + 2), num, font=F_STAT_N, fill=INK)
        lines = wrap(d, label, F_STAT_L, bw - 12)
        ly = y0 + 32
        for ln in lines[:2]:
            lw = d.textlength(ln, font=F_STAT_L)
            d.text((x0 + (bw - lw) / 2, ly), ln, font=F_STAT_L, fill=MUTED)
            ly += 12
        if len(lines) > 2:
            print("WARN stat label too long:", label, lines)

def draw_region_bar(d):
    y0, y1 = 162, 182
    bw = CW / 7
    for i, (name, count, color) in enumerate(REGIONS):
        x0 = MARGIN + i * bw
        d.rectangle([x0, y0, x0 + bw, y1], fill=color)
        txt = f"{name} {count}"
        tw = d.textlength(txt, font=F_REG)
        d.text((x0 + (bw - tw) / 2, y0 + 3), txt, font=F_REG,
               fill=(255, 255, 255))

def draw_hero(d, story, x, w):
    y0 = HERO_Y0
    HERO_ART[story["art"]](d, x, y0, w, HERO_ART_H)
    draw_art_tag(d, x, y0, story["art_tag"], F_TAG, 16)
    draw_art_cap(d, x, y0 + HERO_ART_H, story["art_cap"])
    d.text((x, y0 + 107), f"{story['n']}  {story['kicker']}", font=F_HERO_K,
           fill=RED)
    lines = wrap(d, story["title"], F_HERO_T, w)
    text_block(d, x, y0 + 120, lines[:2], F_HERO_T, INK, 20)
    if len(lines) > 2:
        print("WARN hero title too long:", story["n"], lines)
    lines = wrap(d, story["body"], F_HERO_B, w)
    text_block(d, x, y0 + 162, lines[:4], F_HERO_B, INK, 13)
    if len(lines) > 4:
        print("WARN hero body too long:", story["n"], lines)
    # v4: thin box around each hero so the three stories read as
    # separate items. Clamped to the page margins — the outer boxes
    # sit flush with the masthead, the inner gaps stay 4px.
    d.rectangle([max(x - 4, MARGIN), y0 - 4, min(x + w + 4, W - MARGIN),
                 y0 + HERO_BOX_H], outline=BOX, width=1)

def draw_grid_cell(d, story, x, y, w, h):
    GRID_ART[story["art"]](d, x, y, w, GRID_ART_H)
    draw_art_tag(d, x, y, story["art_tag"], F_GRID_TAG, 14)
    d.text((x, y + 52), f"{story['n']}  {story['kicker']}", font=F_GRID_K,
           fill=RED)
    lines = wrap(d, story["title"], F_GRID_T, w)
    text_block(d, x, y + 64, lines[:3], F_GRID_T, INK, 12)
    if len(lines) > 3:
        print("WARN grid title too long:", story["n"], lines)
    lines = wrap(d, story["body"], F_GRID_B, w)
    text_block(d, x, y + 102, lines[:3], F_GRID_B, INK, 11)
    if len(lines) > 3:
        print("WARN grid body too long:", story["n"], lines)
    # v4: thin box around each grid cell (clamped to the margins).
    d.rectangle([max(x - 2, MARGIN), y - 2, min(x + w + 2, W - MARGIN),
                 y + h], outline=BOX, width=1)

# --- world map ------------------------------------------------------------
CONTINENTS = [
    # North America
    [(-168, 66), (-140, 70), (-125, 72), (-110, 68), (-95, 69), (-85, 66),
     (-80, 73), (-65, 60), (-55, 52), (-60, 47), (-70, 42), (-75, 35),
     (-80, 32), (-85, 30), (-90, 21), (-97, 16), (-105, 20), (-110, 24),
     (-117, 33), (-125, 40), (-124, 48), (-140, 60), (-158, 58)],
    # South America
    [(-80, 10), (-75, 7), (-70, 11), (-60, 8), (-52, 5), (-50, 0),
     (-40, -5), (-35, -8), (-40, -20), (-48, -28), (-57, -38), (-65, -45),
     (-70, -52), (-73, -40), (-73, -25), (-80, -15), (-81, -5)],
    # Europe
    [(-10, 36), (-9, 43), (-2, 48), (0, 50), (5, 53), (8, 57), (10, 59),
     (5, 60), (18, 56), (21, 55), (24, 58), (28, 60), (30, 62), (25, 66),
     (20, 70), (15, 68), (10, 64), (5, 58), (-5, 50)],
    # Africa
    [(-17, 15), (-15, 27), (-10, 31), (-5, 35), (10, 37), (20, 32),
     (30, 31), (32, 31), (35, 28), (37, 22), (40, 15), (43, 12), (48, 11),
     (51, 10), (48, 0), (40, -10), (35, -20), (32, -29), (28, -33),
     (20, -35), (15, -27), (12, -18), (13, -10), (9, 4), (4, 6), (-8, 5),
     (-13, 8)],
    # Asia
    [(30, 62), (40, 68), (50, 70), (60, 69), (70, 72), (80, 73), (90, 75),
     (100, 76), (110, 74), (120, 73), (130, 72), (140, 72), (150, 70),
     (160, 69), (170, 67), (178, 65), (170, 60), (162, 58), (158, 52),
     (150, 60), (142, 55), (140, 45), (135, 42), (130, 38), (127, 35),
     (122, 32), (120, 28), (115, 22), (110, 20), (108, 12), (105, 9),
     (100, 7), (98, 12), (95, 16), (92, 21), (88, 22), (85, 19), (80, 13),
     (77, 8), (74, 12), (72, 20), (68, 23), (65, 25), (60, 25), (57, 26),
     (55, 27), (52, 28), (50, 30), (48, 30), (44, 29), (40, 31), (38, 36),
     (35, 36), (30, 36), (27, 38), (26, 40), (28, 45), (28, 50), (30, 55)],
    # Australia
    [(113, -22), (114, -30), (115, -35), (120, -34), (125, -32), (129, -32),
     (132, -32), (135, -35), (138, -35), (140, -38), (145, -38), (150, -37),
     (153, -32), (153, -27), (150, -22), (146, -19), (142, -11), (140, -17),
     (136, -15), (135, -12), (132, -12), (130, -13), (126, -14), (122, -17),
     (118, -20)],
]
ISLANDS = [  # (lon, lat, rx, ry) ellipses: Japan, UK, New Zealand, Indonesia
    (139, 37, 4, 9), (-2, 54, 3, 6), (172, -41, 3, 7),
    (113, -2, 8, 3), (122, -3, 6, 3), (130, -3, 5, 3),
]

def lonlat_to_xy(lon, lat, mx, my, mw, mh):
    # Longitude span -190..190 so the far-east dots (Wellington)
    # keep a sea margin inside the panel instead of being clipped
    # at its right edge.
    px = mx + (lon + 190) / 380 * mw
    py = my + (90 - lat) / 150 * mh
    return px, py

def draw_map(d, mx, my, mw, mh):
    d.rectangle([mx, my, mx + mw, my + mh], fill=SEA)
    for lon in range(-150, 181, 30):
        x = mx + (lon + 190) / 380 * mw
        d.line([x, my, x, my + mh], fill=(170, 205, 230), width=1)
    for lat in (-60, -30, 0, 30, 60):
        y = my + (90 - lat) / 150 * mh
        d.line([mx, y, mx + mw, y], fill=(170, 205, 230), width=1)
    for poly in CONTINENTS:
        pts = [lonlat_to_xy(lon, lat, mx, my, mw, mh) for lon, lat in poly]
        d.polygon(pts, fill=LAND, outline=(150, 140, 110))
    for lon, lat, rx, ry in ISLANDS:
        cx, cy = lonlat_to_xy(lon, lat, mx, my, mw, mh)
        d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=LAND)
    # dots: one per location; duplicates get a count badge
    seen = {}
    for s in ALL_STORIES:
        key = (s["lon"], s["lat"])
        seen[key] = seen.get(key, 0) + 1
    placed = []
    badges = []
    offsets = [(0, 0), (12, 0), (-12, 0), (0, 12), (0, 14), (0, -12), (16, 8),
               (-16, 8), (16, -8), (-16, -8), (22, 0), (-22, 0), (0, 18),
               (0, -18), (24, 10), (-24, 10), (24, -10), (-24, -10),
               (30, 0), (-30, 0), (0, 24),
               # second ring: only reached by dots the first ring
               # cannot place (the crowded Europe / New Zealand dots)
               (-26, 10), (-24, 12), (24, 12), (-26, -10), (26, -10),
               (-28, 0), (28, 0), (-20, 14), (20, 14), (-20, -14),
               (20, -14), (-14, 16), (14, 16), (-10, 18), (10, 18)]
    done = set()
    f_dot = font(SANS_B, 8)
    # Pass 1: place every dot and draw its leader line. Lines go
    # first so they can never paint over a dot or a number.
    dots = []
    for s in ALL_STORIES:
        key = (s["lon"], s["lat"])
        if key in done:
            continue
        done.add(key)
        tx, ty = lonlat_to_xy(s["lon"], s["lat"], mx, my, mw, mh)
        chosen = None
        for ox, oy in offsets:
            px, py = tx + ox, ty + oy
            if not (mx + 2 <= px <= mx + mw - 2 and my + 2 <= py <= my + mh - 2):
                continue
            if all((px - qx) ** 2 + (py - qy) ** 2 >= 12 ** 2
                   for qx, qy in placed):
                chosen = (px, py)
                break
        if chosen is None:
            chosen = (tx, ty)
            print("WARN dot could not be de-collided:", s["n"])
        px, py = chosen
        placed.append((px, py))
        if (px, py) != (tx, ty):
            d.line([tx, ty, px, py], fill=INK, width=1)
        dots.append((s, px, py))
        if seen[key] > 1:
            badges.append((px, py, seen[key]))
    # Pass 2: the dots and their numbers, on top of the lines.
    for s, px, py in dots:
        d.ellipse([px - 7, py - 7, px + 7, py + 7], fill=RED,
                  outline=(255, 255, 255), width=1)
        num = str(s["n"])
        nw = d.textlength(num, font=f_dot)
        d.text((px - nw / 2, py - 5), num, font=f_dot,
               fill=(255, 255, 255))
    # Badges last, bottom-right of their dot.
    for px, py, count in badges:
        d.ellipse([px + 2, py + 4, px + 10, py + 12], fill=NAVY,
                  outline=(255, 255, 255), width=1)
        d.text((px + 3.5, py + 4), str(count), font=f_dot,
               fill=(255, 255, 255))

def draw_map_also(d):
    d.text((MARGIN, 716), "WHERE IT HAPPENED", font=F_MAP_T, fill=INK)
    ax = MARGIN + MAP_W + 16
    d.text((ax, 716), "ALSO ON SUNDAY 22 NOVEMBER — 23 MORE STORIES",
           font=F_ALSO_T, fill=INK)
    # v4: one wrapper box around the whole ALSO block (header + rows).
    d.rectangle([ax - 6, 712, W - MARGIN + 2, 932],
                outline=BOX, width=1)
    draw_map(d, MARGIN, MAP_Y, MAP_W, MAP_H)
    # the example's legend, verbatim
    d.text((MARGIN, 874), "Red numbers mark stories 1–13 on the map.",
           font=F_DC10, fill=MUTED)
    # ALSO numbers sit in a filled red circle (same device as the
    # numbered dots on the map). Each item is ONE line, no source
    # suffix, as in the example. Column-major like the example:
    # 14-25 down the left column, 26-36 down the right. 12 rows of
    # 16px, the last circle ending at y=928, clear of BY THE CLOCK.
    CIRCLE_D = 16
    GAP = 6
    col_w = 325
    for i, item in enumerate(ALSO):
        col = 0 if i < 12 else 1
        row = i if col == 0 else i - 12
        x = ax + col * (col_w + 12)
        y = MAP_Y + row * 16
        num = str(item["n"])
        d.ellipse([x, y + 1, x + CIRCLE_D, y + 1 + CIRCLE_D], fill=RED)
        d.text((x + CIRCLE_D / 2, y + 9), num, font=F_ALSO_N,
               fill=(255, 255, 255), anchor="mm")
        lines = wrap(d, item["text"], F_ALSO, col_w - CIRCLE_D - GAP)
        text_block(d, x + CIRCLE_D + GAP, y + 3, lines[:1], F_ALSO, INK, 13)
        if len(lines) > 1:
            print("WARN also too long:", item["n"], lines)

def draw_clock(d):
    # single line, like the example (10px so the whole line fits)
    label = "BY THE CLOCK — "
    line = ("UTC Sat 07:35 Sparta II fire reported · Sat 12:08 CST "
            "Mexico announces capture · 01:23 France seeks UN action · "
            "01:36 US \u2018open to\u2019 a Western Hemisphere UN chief")
    lw = d.textlength(label, font=F_CLOCK_B)
    d.text((MARGIN, 934), label, font=F_CLOCK_B, fill=INK)
    d.text((MARGIN + lw, 934), line, font=F_CLOCK, fill=INK)
    if MARGIN + lw + d.textlength(line, font=F_CLOCK) > W - MARGIN:
        print("WARN clock line overflows")

def draw_date_check(d):
    # v4: the whole block sits in a bordered box with padding. v5
    # text is the example's, verbatim (3 lines at 10px).
    d.rectangle([MARGIN, 950, W - MARGIN, 996],
                fill=(243, 239, 227), outline=BOX, width=1)
    d.text((MARGIN + 10, 955), "DATE CHECK —", font=F_DC_T, fill=RED)
    t1 = ("Left out as other days\u2019 news: the APEC trilateral in "
          "Shenzhen (Thu 19 Nov) · the Kyiv barrage and the missiles "
          "over Poland (Fri 20 Nov) · Wall Street\u2019s correction "
          "(Fri 20 Nov) · the Denmark \u2018assassination plot\u2019 "
          "(Fri 20 Nov) · the Peru quake (Fri 20 Nov local) · the "
          "Anthropic IPO debut (Thu 19 Nov) · the GTA VI launch "
          "(Thu 19 Nov). Not yet happened, so not shown: any final "
          "COP31 text; the Las Vegas GP result.")
    first_w = W - 2 * MARGIN - 20 - 110  # box pads + label
    lines1 = wrap(d, t1, F_DC10, first_w)
    rest = (" ".join(lines1[1:])) if len(lines1) > 1 else ""
    lines2 = wrap(d, rest, F_DC10, W - 2 * MARGIN - 20)
    d.text((MARGIN + 120, 955), lines1[0], font=F_DC10, fill=INK)
    y = 967
    for ln in lines2[:2]:
        d.text((MARGIN + 10, y), ln, font=F_DC10, fill=INK)
        y += 12
    if len(lines2) > 2:
        print("WARN date-check too long:", lines1, lines2)

def draw_footer(d):
    d.line([MARGIN, 1003, W - MARGIN, 1003], fill=INK, width=1)
    left = ("Every story here happened, or was first reported, on "
            "Sunday 22 November 2026. Officials\u2019 counts are "
            "attributed.")
    right = "Sources named beside each story · original drawings"
    d.text((MARGIN, 1008), left, font=F_FOOT, fill=MUTED)
    d.text((W - MARGIN - d.textlength(right, font=F_FOOT_B), 1008), right,
           font=F_FOOT_B, fill=MUTED)

def render():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    draw_masthead(d)
    draw_stats(d)
    draw_region_bar(d)
    for i, story in enumerate(HEROES):
        draw_hero(d, story, MARGIN + i * (317 + 12), 317)
    gw, gap = 187, 10
    for i, story in enumerate(GRID):
        row, col = divmod(i, 5)
        x = MARGIN + col * (gw + gap)
        y = GRID_Y0 + row * (GRID_CELL_H + 6)
        draw_grid_cell(d, story, x, y, gw, GRID_CELL_H)
    draw_map_also(d)
    draw_clock(d)
    draw_date_check(d)
    draw_footer(d)
    return img

def main():
    counts = region_counts()
    print("stories", len(ALL_STORIES), "regions", counts)
    if len(ALL_STORIES) != 36:
        print("WARN story count != 36")
    for name, count, _ in REGIONS:
        if counts.get(name.title(), 0) != count:
            print("WARN region mismatch:", name, counts.get(name.title(), 0),
                  count)
    img = render()
    img.save(OUT, optimize=True)
    data = open(OUT, "rb").read()
    print("entry.png", len(data), "bytes",
          "sha256", hashlib.sha256(data).hexdigest())
    print("size", img.size)

if __name__ == "__main__":
    main()
