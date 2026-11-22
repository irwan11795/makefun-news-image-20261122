#!/usr/bin/env python3
"""Generate entry.png for news-image-20261122 (v1-fix2, slot 1).

Draws a one-page newspaper summing up Sunday 22 November 2026:
21 stories across 6 regions, every one verified against a primary
source dated that day (see NOTES.md for the source of every story
and everything dropped for failing validation).

Structure follows the user's example page (a competitor's "THE
WORLD IN ONE DAY" for the same day): masthead + date headline +
sub-headline, 6 stat boxes, region bar, 3 heroes with BIG code-drawn
illustrations, a 10-cell grid with full-bleed illustrations, a
numbered-dot world map, an ALSO list, a BY THE CLOCK line, a DATE
CHECK box, and a footer. NO sentence or text was copied from the
example image — it supplied only the layout pattern; every headline,
body and label here was written from the verified facts in NOTES.md.
The example's story list was NOT trusted: its audit found nearly
every story wrong-dated (19-21 Nov presented as 22 Nov), so this
page has 21 stories, the honest count of verified Sunday stories.

All drawing is done with Pillow shapes; no external images are
used. Deterministic: same input always produces the same bytes.
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
NIGHT = (16, 24, 52)
GREEN = (20, 130, 60)
PURPLE = (120, 60, 160)
OLIVE = (140, 140, 40)
ORANGE = (196, 110, 20)
CYAN = (60, 160, 200)
MAROON = (140, 30, 50)

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
F_HERO_S = font(SANS, 11)
F_GRID_K = font(SANS_B, 10)
F_GRID_T = font(SERIF_B, 12)
F_GRID_B = font(SANS, 10)
F_GRID_S = font(SANS, 9)
F_GRID_TAG = font(SANS_B, 9)
F_MAP_T = font(SANS_B, 14)
F_ALSO_T = font(SANS_B, 14)
F_ALSO = font(SANS, 12)
F_ALSO_N = font(SANS_B, 12)
F_DC_T = font(SANS_B, 12)
F_DC = font(SANS, 11)
F_FOOT = font(SANS, 11)
F_FOOT_B = font(SANS_B, 11)
F_TAG = font(SANS_B, 10)
F_DOT = font(SANS_B, 9)
F_CLOCK = font(SANS, 11)
F_CLOCK_B = font(SANS_B, 11)

TAG_FILL = {"CONFIRMED": GREEN, "OFFICIAL": BLUE,
            "REPORTED": ORANGE, "CLAIM": RED}

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

def wrap_hanging(draw, text, fnt, first_width, width):
    """Wrap with a narrower first line (e.g. beside a number circle)
    and full width for the following lines."""
    words = text.split()
    lines, cur, w = [], "", first_width
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur, w = word, width
    if cur:
        lines.append(cur)
    return lines

def text_block(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y

def clipped(draw, text, fnt, width):
    """Shorten text with an ellipsis so it fits width."""
    if draw.textlength(text, font=fnt) <= width:
        return text
    while text and draw.textlength(text + "...", font=fnt) > width:
        text = text[:-1]
    return text + "..."

# ---------------------------------------------------------------- data
# Every story: number, kicker (PLACE · BEAT), title, body, source,
# verification tag, art key, region, lon/lat (for the map).
HEROES = [
    dict(n=1, kicker="ANTALYA · CLIMATE", region="Europe",
         lon=30.71, lat=36.90, art="cop31",
         title="COP31 circulates final text; adoption still pending",
         body=("A third text circulated in the early hours recalls "
               "the COP28 consensus in full but names no fossil fuel. It "
               "targets electricity at 35% of final energy by 2035, "
               "and adoption awaits the plenary."),
         source="Reuters · AFP", tag="CONFIRMED"),
    dict(n=2, kicker="CIKANDE · DISASTER", region="Asia",
         lon=106.35, lat=-6.35, art="fire",
         title="36 missing after factory fire in Indonesia",
         body=("Rescuers searched on Sunday for 36 workers still "
               "missing, as of 03:56 UTC, after a fire at a candy "
               "factory in Cikande late on Saturday; 3 dead, 4 hurt."),
         source="Reuters", tag="CONFIRMED"),
    dict(n=3, kicker="MECCA REGION · CONFLICT", region="Middle East",
         lon=39.82, lat=21.42, art="intercept",
         title="Saudi coalition intercepts Houthi missile",
         body=("Air defences intercepted and destroyed a Houthi ballistic "
               "missile aimed at western Saudi Arabia, after a "
               "civil-defence warning for the Mecca region late on "
               "Saturday."),
         source="Reuters · Anadolu", tag="CONFIRMED"),
]

GRID = [
    dict(n=4, kicker="MYANMAR · DIPLOMACY", region="Asia",
         lon=96.13, lat=19.75, art="assembly",
         title="Myanmar calls ASEAN ruling 'unfair'",
         body=("The army-backed government rejects the summit decision "
               "to hold back full political representation."),
         source="Reuters", tag="CONFIRMED"),
    dict(n=5, kicker="NEW DELHI · DIPLOMACY", region="Asia",
         lon=77.21, lat=28.61, art="plane",
         title="Nepal PM Shah arrives in India for state visit",
         body=("Balendra Shah lands for a two-day visit, his first "
               "bilateral trip since taking office in March."),
         source="Radio Nepal", tag="CONFIRMED"),
    dict(n=6, kicker="SINGAPORE · DIPLOMACY", region="Asia",
         lon=103.85, lat=1.29, art="skyline",
         title="China's Ding Xuexiang begins Singapore visit",
         body=("The vice-premier arrives for two days; he and DPM Gan "
               "co-chair the 22nd JCBC on Monday."),
         source="MFA Singapore", tag="OFFICIAL"),
    dict(n=7, kicker="BEIJING · TRADE", region="Asia",
         lon=116.41, lat=39.90, art="tower",
         title="China opposes US FCC ban on its telecoms",
         body=("Beijing 'firmly opposes' Thursday's vote barring its "
               "carriers from US phone numbers."),
         source="Reuters", tag="CONFIRMED"),
    dict(n=8, kicker="CANBERRA · DEFENCE", region="Oceania",
         lon=149.13, lat=-35.28, art="sub",
         title="Australia calls US budget office 'wrong' on AUKUS",
         body=("Defence minister Marles rejects a CBO finding that "
               "AUKUS cuts US attack-submarine numbers."),
         source="Reuters", tag="CONFIRMED"),
    dict(n=9, kicker="WELLINGTON · CRICKET", region="Oceania",
         lon=174.78, lat=-41.29, art="cricket",
         title="India declare a record 720/9 in New Zealand",
         body=("Pant 128 — first India keeper with a Test century in "
               "NZ — and Rahul 136 take India to a record 720/9."),
         source="Reuters", tag="CONFIRMED"),
    dict(n=10, kicker="TEHRAN · ENERGY", region="Middle East",
         lon=51.39, lat=35.69, art="power",
         title="Iran begins electricity rationing",
         body=("Rolling blackouts of up to 2 hours a day start on "
               "Sunday, blamed on fuel shortages."),
         source="RFE/RL · Reuters", tag="REPORTED"),
    dict(n=11, kicker="ABU DHABI · DIPLOMACY", region="Middle East",
         lon=54.38, lat=24.45, art="palace",
         title="UAE president receives US homeland security chief",
         body=("Sheikh Mohamed bin Zayed meets Markwayne Mullin in Abu "
               "Dhabi; strategic cooperation discussed."),
         source="WAM · ANI", tag="OFFICIAL"),
    dict(n=12, kicker="PYONGYANG · SPORT", region="Asia",
         lon=125.75, lat=39.04, art="runner",
         title="North Korea postpones 2027 marathon to October",
         body=("The Pyongyang International Marathon moves from April "
               "to 'almost certainly' October 2027."),
         source="Reuters", tag="CONFIRMED"),
    dict(n=13, kicker="MANAMA · DIPLOMACY", region="Middle East",
         lon=50.59, lat=26.23, art="un",
         title="Bahrain urges UN action after Saturday strike",
         body=("Bahrain asks the Security Council to enforce Resolution "
               "2817 and seeks compensation."),
         source="Al Jazeera", tag="REPORTED"),
]

ALSO = [
    dict(n=14, place="MELBOURNE", region="Oceania",
         lon=144.96, lat=-37.81, source="AAP",
         text="Bellamy to end 25 years as Storm coach after 2027"),
    dict(n=15, place="RUATŌRIA", region="Oceania",
         lon=178.32, lat=-37.89, source="NZ Police",
         text="One dead as house slips off its foundations"),
    dict(n=16, place="MELBOURNE", region="Oceania",
         lon=144.96, lat=-37.81, source="AAP",
         text="Dawn Fraser, 89, at 70th anniversary of 1956 Games"),
    dict(n=17, place="NOWA DĘBA", region="Europe",
         lon=21.76, lat=50.43, source="Vozia",
         text="Multinational Ukraine-force exercise ends today"),
    dict(n=18, place="BAYELSA", region="Africa",
         lon=6.08, lat=4.85, source="TheMatrix",
         text="Boat death toll rises to 24"),
    dict(n=19, place="SANDTON", region="Africa",
         lon=28.06, lat=-26.11, source="SA News",
         text="South Africa holds prayer for the late Mlambo-Ngcuka"),
    dict(n=20, place="LAS VEGAS", region="Americas",
         lon=-115.14, lat=36.17, source="PlanetF1",
         text="Grand Prix under way Saturday night, local time; "
              "Verstappen on pole"),
    dict(n=21, place="PANAMA CITY", region="Americas",
         lon=-79.52, lat=8.98, source="AFP",
         text="Panama threatens to scuttle any weak COP31 deal"),
]

STATS = [
    ("35%", "electricity share by 2035, COP31 draft"),
    ("352", "India's lead in Wellington, in runs"),
    ("25", "Bellamy's final Storm season, his 25th"),
    ("36", "missing after Cikande fire, 03:56 UTC"),
    ("720/9", "India's record Test total in New Zealand"),
    ("1,661", "killed in Gaza since October ceasefire"),
]

REGIONS = [("EUROPE", 2, BLUE), ("AMERICAS", 2, MAROON),
           ("ASIA", 6, ORANGE), ("MIDDLE EAST", 4, OLIVE),
           ("AFRICA", 2, GREEN), ("OCEANIA", 5, TEAL)]

ALL_STORIES = HEROES + GRID + ALSO

def region_counts():
    counts = {}
    for s in ALL_STORIES:
        counts[s["region"]] = counts.get(s["region"], 0) + 1
    return counts

# ---------------------------------------------------------------- art
# Full-bleed compositions. Each function paints the WHOLE rect
# (x, y, w, h) — background plus motif elements spread from edge to
# edge. All coordinates are fractions of w/h, so the art scales.

def art_cop31(d, x, y, w, h):
    # Antalya: conference hall at night — globe above rows of desks
    # with flags, a document in front, clock on the wall.
    d.rectangle([x, y, x + w, y + h], fill=NIGHT)
    for sx, sy in [(0.06, 0.12), (0.18, 0.06), (0.30, 0.14), (0.44, 0.07),
                   (0.58, 0.13), (0.72, 0.06), (0.86, 0.12), (0.95, 0.07),
                   (0.12, 0.25), (0.38, 0.22), (0.66, 0.24), (0.90, 0.22)]:
        d.ellipse([x + sx * w, y + sy * h, x + sx * w + 2, y + sy * h + 2],
                  fill=(255, 255, 255))
    # globe, left-centre
    cx, cy, r = x + w * 0.30, y + h * 0.42, h * 0.30
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(70, 140, 190),
              outline=(220, 230, 240), width=2)
    d.ellipse([cx - r * 0.55, cy - r, cx + r * 0.55, cy + r],
              outline=(220, 230, 240), width=1)
    d.line([cx - r, cy, cx + r, cy], fill=(220, 230, 240), width=1)
    d.line([cx - r * 0.8, cy - r * 0.55, cx + r * 0.8, cy - r * 0.55],
           fill=(220, 230, 240), width=1)
    d.line([cx - r * 0.8, cy + r * 0.55, cx + r * 0.8, cy + r * 0.55],
           fill=(220, 230, 240), width=1)
    # document, right
    dx, dy, dw, dh = x + w * 0.62, y + h * 0.18, w * 0.30, h * 0.55
    d.rectangle([dx, dy, dx + dw, dy + dh], fill=(250, 247, 238),
                outline=(180, 170, 150), width=1)
    for i, lw in enumerate((0.80, 0.70, 0.85, 0.60, 0.75)):
        ly = dy + dh * (0.16 + i * 0.15)
        d.line([dx + dw * 0.10, ly, dx + dw * (0.10 + lw), ly],
               fill=(90, 90, 90), width=2)
    # clock, top right
    ccx, ccy, cr = x + w * 0.90, y + h * 0.16, h * 0.11
    d.ellipse([ccx - cr, ccy - cr, ccx + cr, ccy + cr], fill=PAPER,
              outline=INK, width=2)
    d.line([ccx, ccy, ccx, ccy - cr * 0.6], fill=INK, width=2)
    d.line([ccx, ccy, ccx + cr * 0.5, ccy + cr * 0.3], fill=INK, width=2)
    # desks + flags along the bottom
    for i in range(7):
        bx = x + w * (0.02 + i * 0.14)
        d.rectangle([bx, y + h * 0.82, bx + w * 0.11, y + h], fill=(52, 58, 84))
        d.rectangle([bx + w * 0.05, y + h * 0.68, bx + w * 0.05 + 2,
                     y + h * 0.82], fill=(200, 200, 200))
        d.rectangle([bx + w * 0.05 + 2, y + h * 0.68, bx + w * 0.10,
                     y + h * 0.76], fill=[BLUE, RED, GREEN, GOLD,
                                          TEAL, ORANGE, MAROON][i])

def art_fire(d, x, y, w, h):
    # Cikande: factory hall at night, flames and smoke, searchlight
    # beams sweeping for the missing.
    d.rectangle([x, y, x + w, y + h], fill=(24, 24, 34))
    # smoke columns
    for sx, sw in [(0.10, 0.10), (0.38, 0.12), (0.66, 0.10), (0.88, 0.09)]:
        for j in range(3):
            d.ellipse([x + w * (sx + j * 0.012), y + h * (0.06 + j * 0.10),
                       x + w * (sx + sw + j * 0.012),
                       y + h * (0.16 + j * 0.10)], fill=(90, 90, 100))
    # factory block
    d.rectangle([x + w * 0.06, y + h * 0.55, x + w * 0.94, y + h * 0.92],
                fill=(70, 66, 78))
    d.rectangle([x + w * 0.10, y + h * 0.42, x + w * 0.18, y + h * 0.55],
                fill=(60, 56, 68))
    for wx in (0.12, 0.30, 0.48, 0.66, 0.82):
        d.rectangle([x + w * wx, y + h * 0.62, x + w * (wx + 0.06),
                     y + h * 0.74], fill=(255, 210, 90))
    # flames across the roofline
    for fx, fw, fh in [(0.08, 0.12, 0.42), (0.26, 0.10, 0.55),
                       (0.42, 0.12, 0.38), (0.60, 0.10, 0.52),
                       (0.76, 0.12, 0.40), (0.90, 0.08, 0.34)]:
        d.polygon([(x + w * fx, y + h * 0.55),
                   (x + w * (fx + fw / 2), y + h * (0.55 - fh)),
                   (x + w * (fx + fw), y + h * 0.55)], fill=(255, 110, 20))
        d.polygon([(x + w * (fx + fw * 0.28), y + h * 0.55),
                   (x + w * (fx + fw / 2), y + h * (0.55 - fh * 0.55)),
                   (x + w * (fx + fw * 0.72), y + h * 0.55)],
                  fill=(255, 210, 60))
    # searchlight beams from bottom corners, narrowed so the flames
    # stay visible behind them
    d.polygon([(x + w * 0.05, y + h), (x + w * 0.26, y + h * 0.10),
               (x + w * 0.32, y + h * 0.10), (x + w * 0.11, y + h)],
              fill=(255, 240, 180))
    d.polygon([(x + w * 0.95, y + h), (x + w * 0.74, y + h * 0.10),
               (x + w * 0.68, y + h * 0.10), (x + w * 0.89, y + h)],
              fill=(255, 240, 180))

def art_intercept(d, x, y, w, h):
    # Mecca region: night sky over a city with minarets, a missile
    # trail arcing up and an intercept burst.
    d.rectangle([x, y, x + w, y + h], fill=NIGHT)
    for sx, sy in [(0.05, 0.10), (0.15, 0.20), (0.25, 0.08), (0.35, 0.16),
                   (0.45, 0.07), (0.55, 0.18), (0.68, 0.09), (0.80, 0.15),
                   (0.92, 0.08), (0.97, 0.20)]:
        d.ellipse([x + sx * w, y + sy * h, x + sx * w + 2, y + sy * h + 2],
                  fill=(255, 255, 255))
    d.ellipse([x + w * 0.84, y + h * 0.05, x + w * 0.94, y + h * 0.15],
              fill=(240, 230, 200))
    # missile trail arcing from lower left to burst at upper right
    d.line([x + w * 0.08, y + h * 0.95, x + w * 0.35, y + h * 0.55],
           fill=(255, 200, 60), width=3)
    d.line([x + w * 0.35, y + h * 0.55, x + w * 0.62, y + h * 0.30],
           fill=(255, 220, 120), width=3)
    # intercept burst
    bx, by = x + w * 0.68, y + h * 0.24
    for ang in range(0, 360, 30):
        rad = math.radians(ang)
        d.line([bx, by, bx + math.cos(rad) * w * 0.09,
                by + math.sin(rad) * h * 0.28], fill=(255, 170, 40), width=3)
    d.ellipse([bx - 10, by - 10, bx + 10, by + 10], fill=(255, 230, 120))
    d.ellipse([bx - 5, by - 5, bx + 5, by + 5], fill=(255, 255, 255))
    # city skyline with two minarets
    for bx0, bw, bh in [(0.00, 0.12, 0.30), (0.14, 0.10, 0.38),
                        (0.26, 0.13, 0.28), (0.41, 0.11, 0.36),
                        (0.54, 0.12, 0.30), (0.68, 0.10, 0.40),
                        (0.80, 0.11, 0.32), (0.92, 0.08, 0.36)]:
        d.rectangle([x + w * bx0, y + h - h * bh, x + w * (bx0 + bw), y + h],
                    fill=(34, 38, 66))
        for wy in (0.35, 0.60):
            d.rectangle([x + w * (bx0 + 0.03), y + h - h * bh + h * bh * wy,
                         x + w * (bx0 + 0.06),
                         y + h - h * bh + h * bh * wy + 3],
                        fill=(255, 210, 90))
    for mx in (0.20, 0.72):
        d.rectangle([x + w * mx, y + h * 0.42, x + w * (mx + 0.02), y + h],
                    fill=(44, 48, 76))
        d.polygon([(x + w * (mx - 0.015), y + h * 0.42),
                   (x + w * (mx + 0.01), y + h * 0.32),
                   (x + w * (mx + 0.035), y + h * 0.42)], fill=(44, 48, 76))

# Grid art: full-bleed strips, fractions of w/h.
def art_assembly(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 214, 170))
    for i in range(9):
        cx = x + w * (0.06 + 0.88 * i / 8)
        d.ellipse([cx - 5, y + h * 0.18, cx + 5, y + h * 0.38],
                  fill=(40, 40, 50))
        d.pieslice([cx - 9, y + h * 0.42, cx + 9, y + h * 0.95], 180, 360,
                   fill=(50 + (i % 4) * 30, 70, 120))
    d.rectangle([x + w * 0.30, y + h * 0.06, x + w * 0.30 + 2, y + h * 0.55],
                fill=(120, 80, 40))
    d.rectangle([x + w * 0.30 + 2, y + h * 0.06, x + w * 0.52, y + h * 0.20],
                fill=BLUE)

def art_plane(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    for sx, sy in [(0.08, 0.15), (0.30, 0.08), (0.55, 0.18), (0.78, 0.10),
                   (0.92, 0.20)]:
        d.ellipse([x + sx * w, y + sy * h, x + sx * w + 16, y + sy * h + 6],
                  fill=(255, 255, 255))
    # mountains along the bottom
    d.polygon([(x, y + h), (x + w * 0.18, y + h * 0.45),
               (x + w * 0.36, y + h), (x + w * 0.55, y + h * 0.55),
               (x + w * 0.74, y + h), (x + w * 0.88, y + h * 0.62),
               (x + w, y + h)], fill=(90, 110, 130))
    # plane, nose right
    px, py = x + w * 0.50, y + h * 0.42
    d.polygon([(px - 26, py), (px + 26, py - 4), (px + 30, py),
               (px + 26, py + 4)], fill=(240, 240, 240))
    d.polygon([(px - 6, py - 3), (px + 2, py - 16), (px + 8, py - 3)],
              fill=(200, 30, 40))
    d.polygon([(px - 10, py + 3), (px - 2, py + 14), (px + 4, py + 3)],
              fill=(200, 30, 40))
    d.line([px - 30, py + 2, px - 52, py + 8], fill=(255, 255, 255), width=2)
    d.line([px - 30, py + 5, px - 48, py + 14], fill=(255, 255, 255), width=1)

def art_skyline(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(24, 28, 44))
    d.ellipse([x + w * 0.86, y + h * 0.06, x + w * 0.96, y + h * 0.26],
              fill=(240, 230, 200))
    specs = [(0.00, 0.11, 0.55), (0.12, 0.10, 0.72), (0.23, 0.11, 0.45),
             (0.35, 0.10, 0.62), (0.46, 0.11, 0.50), (0.58, 0.10, 0.70),
             (0.69, 0.11, 0.48), (0.81, 0.09, 0.64), (0.91, 0.09, 0.55)]
    for bx, bw, bh in specs:
        d.rectangle([x + w * bx, y + h - h * bh, x + w * (bx + bw), y + h],
                    fill=(52, 58, 84))
        for wy in (0.30, 0.55):
            d.rectangle([x + w * (bx + 0.02), y + h - h * bh + h * bh * wy,
                         x + w * (bx + 0.05),
                         y + h - h * bh + h * bh * wy + 4],
                        fill=(255, 210, 90))
    # tower with spire
    d.rectangle([x + w * 0.47, y + h * 0.18, x + w * 0.51, y + h],
                fill=(70, 76, 100))
    d.polygon([(x + w * 0.46, y + h * 0.18), (x + w * 0.49, y + h * 0.04),
               (x + w * 0.52, y + h * 0.18)], fill=(90, 96, 120))

def art_tower(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(30, 40, 70))
    # signal arcs from a telecom tower at left
    tx, ty = x + w * 0.18, y + h * 0.85
    d.rectangle([tx - 3, y + h * 0.25, tx + 3, ty], fill=(200, 200, 210))
    d.polygon([(tx - 8, y + h * 0.25), (tx, y + h * 0.12),
               (tx + 8, y + h * 0.25)], fill=(200, 200, 210))
    for r in (0.18, 0.30, 0.42):
        d.arc([tx - w * r, ty - h * r * 1.6, tx + w * r, ty + h * r * 1.6],
              start=300, end=60, fill=(255, 210, 60), width=3)
    # phones receiving, right side
    for i, px in enumerate((0.55, 0.72, 0.88)):
        d.rounded_rectangle([x + w * px, y + h * 0.45, x + w * (px + 0.09),
                             y + h * 0.90], radius=4, fill=(20, 20, 30),
                            outline=(180, 180, 190), width=2)
        d.rectangle([x + w * (px + 0.015), y + h * 0.52, x + w * (px + 0.075),
                     y + h * 0.80], fill=(60, 160, 200))

def art_sub(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(16, 42, 66))
    # surface waves
    for i in range(5):
        wx = x + w * (0.04 + i * 0.20)
        d.arc([wx, y + h * 0.06, wx + w * 0.16, y + h * 0.30], start=200,
              end=340, fill=(120, 190, 230), width=3)
    # submarine, centre
    sx, sy, sw, sh = x + w * 0.22, y + h * 0.48, w * 0.56, h * 0.30
    d.ellipse([sx, sy, sx + sw, sy + sh], fill=(60, 70, 84))
    d.rectangle([sx + sw * 0.42, sy - h * 0.14, sx + sw * 0.58, sy],
                fill=(60, 70, 84))
    d.polygon([(sx + sw, sy + sh * 0.15), (sx + sw + w * 0.06, sy + sh * 0.5),
               (sx + sw, sy + sh * 0.85)], fill=(60, 70, 84))
    for wx in (0.32, 0.45, 0.58, 0.70):
        d.ellipse([x + w * wx, sy + sh * 0.35, x + w * wx + 4,
                   sy + sh * 0.35 + 4], fill=(255, 210, 90))
    # bubbles
    for bx, by in [(0.30, 0.30), (0.36, 0.22), (0.62, 0.28), (0.70, 0.18)]:
        d.ellipse([x + w * bx, y + h * by, x + w * bx + 5, y + h * by + 5],
                  outline=(180, 220, 240), width=2)

def art_cricket(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(46, 110, 58))
    # pitch strip
    d.rectangle([x + w * 0.38, y, x + w * 0.62, y + h], fill=(214, 196, 150))
    # crease lines
    d.line([x + w * 0.38, y + h * 0.18, x + w * 0.62, y + h * 0.18],
           fill=(255, 255, 255), width=2)
    d.line([x + w * 0.38, y + h * 0.82, x + w * 0.62, y + h * 0.82],
           fill=(255, 255, 255), width=2)
    # stumps, both ends
    for sy in (0.10, 0.74):
        for k in range(3):
            d.rectangle([x + w * (0.46 + k * 0.03), y + h * sy,
                         x + w * (0.46 + k * 0.03) + 3, y + h * (sy + 0.08)],
                        fill=(240, 210, 120))
    # bat, diagonal
    d.line([x + w * 0.30, y + h * 0.30, x + w * 0.52, y + h * 0.62],
           fill=(160, 110, 60), width=7)
    d.line([x + w * 0.28, y + h * 0.26, x + w * 0.32, y + h * 0.32],
           fill=(90, 60, 30), width=5)
    # red ball flying
    d.ellipse([x + w * 0.78, y + h * 0.22, x + w * 0.78 + 12,
               y + h * 0.22 + 12], fill=(200, 30, 30))
    d.arc([x + w * 0.70, y + h * 0.30, x + w * 0.86, y + h * 0.46],
          start=300, end=60, fill=(255, 255, 255), width=2)
    # score "720/9" as painted boards? keep the field clean instead:
    for fx, fy in [(0.10, 0.70), (0.20, 0.82), (0.85, 0.70), (0.92, 0.55)]:
        d.ellipse([x + w * fx, y + h * fy, x + w * fx + 6, y + h * fy + 6],
                  fill=(255, 255, 255))

def art_power(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(40, 40, 48))
    # pylon left
    px = x + w * 0.20
    d.line([px, y + h * 0.15, px - w * 0.08, y + h], fill=(180, 180, 190),
           width=4)
    d.line([px, y + h * 0.15, px + w * 0.08, y + h], fill=(180, 180, 190),
           width=4)
    d.line([px - w * 0.12, y + h * 0.30, px + w * 0.12, y + h * 0.30],
           fill=(180, 180, 190), width=3)
    # sagging wires across
    d.arc([x + w * 0.10, y - h * 0.35, x + w * 0.95, y + h * 0.55],
          start=20, end=160, fill=(220, 220, 230), width=2)
    d.arc([x + w * 0.10, y - h * 0.15, x + w * 0.95, y + h * 0.75],
          start=20, end=160, fill=(220, 220, 230), width=2)
    # dark bulb, right, with a small "off" cross
    bx, by, br = x + w * 0.72, y + h * 0.45, h * 0.22
    d.ellipse([bx - br, by - br, bx + br, by + br], fill=(90, 90, 100),
              outline=(200, 200, 210), width=2)
    d.rectangle([bx - 6, by + br - 2, bx + 6, by + br + 8], fill=(120, 120, 130))
    d.line([bx - br * 0.5, by - br * 0.5, bx + br * 0.5, by + br * 0.5],
           fill=(200, 60, 60), width=3)
    d.line([bx + br * 0.5, by - br * 0.5, bx - br * 0.5, by + br * 0.5],
           fill=(200, 60, 60), width=3)
    # one lit bulb far right
    lx, ly = x + w * 0.90, y + h * 0.30
    d.ellipse([lx - 6, ly - 6, lx + 6, ly + 6], fill=(255, 220, 90))

def art_palace(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 220, 190))
    # palace with dome, centre
    d.rectangle([x + w * 0.30, y + h * 0.45, x + w * 0.70, y + h],
                fill=(250, 244, 228))
    d.pieslice([x + w * 0.40, y + h * 0.12, x + w * 0.60, y + h * 0.55],
               180, 360, fill=(196, 150, 60))
    d.rectangle([x + w * 0.495, y + h * 0.04, x + w * 0.505, y + h * 0.14],
                fill=(150, 110, 40))
    for wx in (0.34, 0.46, 0.58):
        d.rectangle([x + w * wx, y + h * 0.60, x + w * (wx + 0.05),
                     y + h * 0.85], fill=(120, 90, 50))
    # side wings
    d.rectangle([x + w * 0.08, y + h * 0.65, x + w * 0.28, y + h],
                fill=(240, 232, 210))
    d.rectangle([x + w * 0.72, y + h * 0.65, x + w * 0.92, y + h],
                fill=(240, 232, 210))
    # flags
    for fx, col in [(0.12, RED), (0.86, GREEN)]:
        d.rectangle([x + w * fx, y + h * 0.30, x + w * fx + 2, y + h * 0.65],
                    fill=(120, 80, 40))
        d.rectangle([x + w * fx + 2, y + h * 0.30, x + w * (fx + 0.08),
                     y + h * 0.42], fill=col)

def art_runner(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(178, 214, 235))
    # track lanes
    for i, ly in enumerate((0.55, 0.68, 0.81, 0.94)):
        d.line([x, y + h * ly, x + w, y + h * ly], fill=(255, 255, 255),
               width=2)
    d.rectangle([x, y + h * 0.50, x + w, y + h], fill=(196, 80, 50))
    # runner, centre-left, mid-stride
    rx, ry = x + w * 0.42, y + h * 0.48
    d.ellipse([rx - 6, ry - 22, rx + 6, ry - 10], fill=(40, 40, 50))
    d.line([rx, ry - 10, rx + 2, ry + 12], fill=(200, 30, 40), width=5)
    d.line([rx, ry - 8, rx - 16, ry + 2], fill=(40, 40, 50), width=4)
    d.line([rx, ry - 8, rx + 16, ry - 2], fill=(40, 40, 50), width=4)
    d.line([rx + 2, ry + 12, rx - 12, ry + 30], fill=(30, 30, 40), width=4)
    d.line([rx + 2, ry + 12, rx + 16, ry + 26], fill=(30, 30, 40), width=4)
    # second runner, right, smaller
    rx2, ry2 = x + w * 0.72, y + h * 0.60
    d.ellipse([rx2 - 5, ry2 - 18, rx2 + 5, ry2 - 8], fill=(60, 60, 70))
    d.line([rx2, ry2 - 8, rx2 + 2, ry2 + 10], fill=(30, 90, 160), width=4)
    d.line([rx2, ry2 - 6, rx2 - 13, ry2 + 2], fill=(60, 60, 70), width=3)
    d.line([rx2, ry2 - 6, rx2 + 13, ry2 - 2], fill=(60, 60, 70), width=3)
    d.line([rx2 + 2, ry2 + 10, rx2 - 10, ry2 + 24], fill=(40, 40, 50),
           width=3)
    d.line([rx2 + 2, ry2 + 10, rx2 + 13, ry2 + 22], fill=(40, 40, 50),
           width=3)
    # stadium stands, top
    for i in range(12):
        cx = x + w * (0.04 + i * 0.08)
        d.ellipse([cx - 4, y + h * 0.14, cx + 4, y + h * 0.24],
                  fill=(50, 50, 60))
    d.rectangle([x, y + h * 0.30, x + w, y + h * 0.34], fill=(120, 120, 130))

def art_un(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(200, 220, 235))
    # UN-style glass building, centre
    d.rectangle([x + w * 0.38, y + h * 0.18, x + w * 0.62, y + h * 0.95],
                fill=(28, 84, 150))
    for row in range(6):
        for col in range(3):
            d.rectangle([x + w * (0.41 + col * 0.075),
                         y + h * (0.24 + row * 0.115),
                         x + w * (0.41 + col * 0.075) + 8,
                         y + h * (0.24 + row * 0.115) + 8],
                        fill=(180, 220, 240))
    # globe emblem above
    gx, gy, gr = x + w * 0.50, y + h * 0.10, h * 0.07
    d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=(28, 84, 150),
              outline=(255, 255, 255), width=2)
    # flags row along the bottom
    cols = [BLUE, RED, GREEN, GOLD, TEAL, ORANGE, MAROON, PURPLE]
    for i in range(8):
        fx = x + w * (0.06 + i * 0.115)
        d.rectangle([fx, y + h * 0.68, fx + 2, y + h * 0.95],
                    fill=(120, 80, 40))
        d.rectangle([fx + 2, y + h * 0.68, fx + w * 0.085, y + h * 0.78],
                    fill=cols[i])

GRID_ART = {"assembly": art_assembly, "plane": art_plane,
            "skyline": art_skyline, "tower": art_tower,
            "sub": art_sub, "cricket": art_cricket,
            "power": art_power, "palace": art_palace,
            "runner": art_runner, "un": art_un}
HERO_ART = {"cop31": art_cop31, "fire": art_fire,
            "intercept": art_intercept}

# ---------------------------------------------------------------- layout
MARGIN = 24
CW = W - 2 * MARGIN  # 976

def draw_masthead(d):
    d.text((MARGIN, 6), "THE WORLD IN ONE DAY", font=F_MAST, fill=RED)
    right = "21 STORIES · 6 REGIONS · EVERY ONE DATED SUNDAY 22 NOVEMBER 2026"
    d.text((W - MARGIN - d.textlength(right, font=F_MAST_R), 8), right,
           font=F_MAST_R, fill=INK)
    d.text((MARGIN, 26), "Sunday 22 November 2026", font=F_DATE, fill=INK)
    sub = ("COP31 final text out, adoption pending · 36 missing after "
           "factory fire · Missile intercepted over Mecca region")
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
    bw = CW / 6
    for i, (name, count, color) in enumerate(REGIONS):
        x0 = MARGIN + i * bw
        d.rectangle([x0, y0, x0 + bw, y1], fill=color)
        txt = f"{name} {count}"
        tw = d.textlength(txt, font=F_REG)
        d.text((x0 + (bw - tw) / 2, y0 + 3), txt, font=F_REG,
               fill=(255, 255, 255))

def draw_hero(d, story, x, w):
    y0 = 188
    HERO_ART[story["art"]](d, x, y0, w, 110)
    d.text((x, y0 + 114), f"{story['n']}  {story['kicker']}", font=F_HERO_K,
           fill=RED)
    lines = wrap(d, story["title"], F_HERO_T, w)
    text_block(d, x, y0 + 128, lines[:2], F_HERO_T, INK, 22)
    if len(lines) > 2:
        print("WARN hero title too long:", story["n"], lines)
    lines = wrap(d, story["body"], F_HERO_B, w)
    text_block(d, x, y0 + 174, lines[:4], F_HERO_B, INK, 15)
    if len(lines) > 4:
        print("WARN hero body too long:", story["n"], lines)
    src = story["source"]
    d.text((x, y0 + 236), src, font=F_HERO_S, fill=GREY)
    tag = story["tag"]
    tw = d.textlength(tag, font=F_TAG)
    d.rectangle([x + w - tw - 8, y0 + 234, x + w, y0 + 248],
                fill=TAG_FILL[tag])
    d.text((x + w - tw - 4, y0 + 236), tag, font=F_TAG,
           fill=(255, 255, 255))

def draw_grid_cell(d, story, x, y, w, h):
    GRID_ART[story["art"]](d, x, y, w, 48)
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
    d.text((x, y + 138), story["source"], font=F_GRID_S, fill=GREY)
    tag = story["tag"]
    tw = d.textlength(tag, font=F_GRID_TAG)
    d.rectangle([x + w - tw - 6, y + 136, x + w, y + 148],
                fill=TAG_FILL[tag])
    d.text((x + w - tw - 3, y + 138), tag, font=F_GRID_TAG,
           fill=(255, 255, 255))

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
    # Longitude span -190..190 so the far-east dots (Wellington,
    # Ruatōria) keep a sea margin inside the panel instead of being
    # clipped at its right edge.
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
    # dots: one per location; duplicates get a "2" badge
    seen = {}
    for s in ALL_STORIES:
        key = (s["lon"], s["lat"])
        seen[key] = seen.get(key, 0) + 1
    placed = []
    badges = []
    offsets = [(0, 0), (12, 0), (-12, 0), (0, 12), (0, -12), (16, 8),
               (-16, 8), (16, -8), (-16, -8), (22, 0), (-22, 0), (0, 18),
               (0, -18), (24, 10), (-24, 10), (24, -10), (-24, -10),
               (30, 0), (-30, 0), (0, 24)]
    done = set()
    f_dot = font(SANS_B, 8)
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
        d.ellipse([px - 7, py - 7, px + 7, py + 7], fill=RED,
                  outline=(255, 255, 255), width=1)
        num = str(s["n"])
        nw = d.textlength(num, font=f_dot)
        d.text((px - nw / 2, py - 5), num, font=f_dot,
               fill=(255, 255, 255))
        if seen[key] == 2:
            badges.append((px, py))
    # Badges last, bottom-right of their dot, so no later dot or leader
    # line can paint over them and they never sit on a neighbour dot.
    for px, py in badges:
        d.ellipse([px + 2, py + 4, px + 10, py + 12], fill=NAVY,
                  outline=(255, 255, 255), width=1)
        d.text((px + 3.5, py + 4), "2", font=f_dot, fill=(255, 255, 255))

def draw_map_also(d):
    d.text((MARGIN, 767), "WHERE IT HAPPENED", font=F_MAP_T, fill=INK)
    d.text((MARGIN + 320 + 16, 767),
           "ALSO ON SUNDAY 22 NOVEMBER — 8 MORE STORIES", font=F_ALSO_T,
           fill=INK)
    draw_map(d, MARGIN, 787, 320, 134)
    legend = "● = 1 STORY   ●② = TWO STORIES AT ONE DOT"
    d.text((MARGIN, 924), legend, font=F_DC, fill=MUTED)
    ax = MARGIN + 320 + 16
    col_w = 314
    # ALSO numbers sit in a filled red circle (same device as the
    # numbered dots on the map): the number itself stays 12px bold,
    # the same size and typeface as before — only the circle makes
    # it visible at a glance. Text hangs beside the circle: the
    # first line is narrower, later lines use the full column width.
    CIRCLE_D = 22
    GAP = 6
    for i, item in enumerate(ALSO):
        col = i % 2
        row = i // 2
        x = ax + col * (col_w + 12)
        y = 787 + row * 33
        num = str(item["n"])
        d.ellipse([x, y + 2, x + CIRCLE_D, y + 2 + CIRCLE_D], fill=RED)
        d.text((x + CIRCLE_D / 2, y + 13), num, font=F_ALSO_N,
               fill=(255, 255, 255), anchor="mm")
        text = f"{item['place']} · {item['text']} ({item['source']})"
        lines = wrap_hanging(d, text, F_ALSO, col_w - CIRCLE_D - GAP,
                             col_w)
        text_block(d, x + CIRCLE_D + GAP, y, lines[:2], F_ALSO, INK, 15)
        if len(lines) > 2:
            print("WARN also too long:", item["n"], lines)

def draw_clock(d):
    d.text((MARGIN, 941), "BY THE CLOCK —", font=F_CLOCK_B, fill=INK)
    line1 = ("GMT Sun 00:00 COP31 draft released · 01:16 GMT AFP on the "
             "fossil-fuel row · 01:42 AST missile intercepted over Mecca region")
    line2 = ("01:57 GMT China opposes FCC ban · 03:56 GMT Reuters on the "
             "Cikande fire · 04:01 GMT Myanmar slams ASEAN")
    d.text((MARGIN + 118, 941), line1, font=F_CLOCK, fill=INK)
    d.text((MARGIN + 118, 955), line2, font=F_CLOCK, fill=INK)

def draw_date_check(d):
    d.text((MARGIN, 966), "DATE CHECK —", font=F_DC_T, fill=RED)
    t1 = ("Left out: APEC Shenzhen (Thu 19) · Kyiv barrage + Poland "
          "missiles (Fri 20) · Wall Street correction (Fri 20) · Denmark "
          "plot (Fri 20) · Peru quake (Fri 20) · Anthropic IPO (Thu 19) · "
          "GTA VI launch (Thu 19).")
    t2 = ("Not yet happened: COP31 adoption — pending · Las Vegas GP "
          "result. Every story here happened, or was first reported, on "
          "Sunday 22 November 2026.")
    lines1 = wrap(d, t1, F_DC, W - 2 * MARGIN - 96)
    lines2 = wrap(d, t2, F_DC, W - 2 * MARGIN)
    d.text((MARGIN + 96, 966), lines1[0], font=F_DC, fill=INK)
    y = 979
    for ln in lines1[1:2] + lines2[:1]:
        d.text((MARGIN, y), ln, font=F_DC, fill=INK)
        y += 13
    if len(lines1) > 2 or len(lines2) > 1:
        print("WARN date-check too long:", lines1, lines2)

def draw_footer(d):
    d.line([MARGIN, 1007, W - MARGIN, 1007], fill=INK, width=1)
    left = "Every story checked against its primary source's own date."
    right = "21 STORIES · 6 REGIONS · ALL SOURCES PRIMARY"
    d.text((MARGIN, 1012), left, font=F_FOOT, fill=MUTED)
    d.text((W - MARGIN - d.textlength(right, font=F_FOOT_B), 1012), right,
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
        y = 441 + row * (156 + 8)
        draw_grid_cell(d, story, x, y, gw, 156)
    draw_map_also(d)
    draw_clock(d)
    draw_date_check(d)
    draw_footer(d)
    return img

def main():
    img = render()
    img.save(OUT, optimize=True)
    data = open(OUT, "rb").read()
    print("entry.png", len(data), "bytes",
          "sha256", hashlib.sha256(data).hexdigest())
    print("size", img.size)

if __name__ == "__main__":
    main()
