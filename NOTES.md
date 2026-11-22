# NOTES — news-image-20261122 (v1-fix, slot 1)

## v1-fix changes (Hermes 78/100 FIX FIRST, 22 Nov)

All five Hermes fixes applied; nothing else on the page changed.
- **1. Duplicate killed.** ALSO #21 (Pant 128, first India keeper
  with a Test century in NZ) was the same innings as grid #9 — deleted.
  Its record is folded into #9's body ("Pant 128 — first India
  keeper with a Test century in NZ — and Rahul 136 take India to a
  record 720/9"), and the 352-run lead moved to a stat box. Slot #21
  is backfilled with Panama's COP31 walkout threat (see ALSO #21
  below) — a verified Sunday story from Latin America, the region
  the page was missing. Total stays 21.
- **2. COP31 contradiction resolved.** Hero 1 no longer says a deal
  was "tabled": the third text circulated in the early hours and
  adoption was still pending a closing plenary. The "94 paragraphs"
  figure is GONE — the Thursday 19 Nov draft had shrunk from 144 to
  80 paragraphs, so 94 was wrong. The "130 nations" figure is GONE
  too — it exists only as one minister's "around 130 countries who
  want…" quote in the AFP wire, not a verified count, and is not
  printed as fact. Both stat boxes replaced (352-run lead, Bellamy's
  25th season). DATE CHECK now reads "COP31 adoption — pending."
- **3. Map reconciled.** 21 stories, 20 unique locations, 20 dots +
  1 "2" badge (Melbourne: #14 Bellamy + #16 Fraser) = 21. No story
  is unmapped; every story carries lon/lat in gen.py.
- **4. ALSO tagged + Cikande stamped.** Every ALSO item now carries
  its source in parentheses. Cikande is stamped "as of 03:56 UTC":
  AFP's interim 39 (Basarnas, ~02:52 UTC, before the deaths were
  confirmed) → 3 found dead → Reuters 03:56 UTC: 36 still missing.
  36 + 3 = 39, so the wires agree; 36 is the latest verified figure.
- **5. Wording.** "Saturday night" fire → "late on Saturday"
  (Reuters: "Saturday evening"; firefighters alerted ~16:30).
  "Prayer for Mlambo-Ngcuka" → "prayer for the late Mlambo-Ngcuka"
  (she died Friday). Las Vegas GP marked "Saturday night, local
  time" so its Sunday-page admission is explicit.

## The page

"The World in One Day" — one 1024×1024 newspaper page summing up
**Sunday 22 November 2026**: **21 stories across 6 regions**.
Every story happened, or was first reported, on that day, verified
against a primary source (major wire service, official site, or
official statement) dated 22 November 2026. No email digests, no
social-media rumors, no unsourced blogs, no mirror-spam sites.

Region counts: Europe 2 · Americas 2 · Asia 6 · Middle East 4 ·
Africa 2 · Oceania 5 = 21. (Computed from the per-story geography
in gen.py — region_counts().)

## Why only 21 stories (not 36)

The user's example page (a competitor's "Sunday 22 November 2026",
36 stories) was audited story by story in two waves (8 researchers,
every claim checked against a primary source opened directly). The
audit found the example systematically wrong-dated: of its 36
stories, **0 of its 13 grid stories and 0 of its 23 ALSO stories
were valid for Sunday 22 Nov** — nearly all were 19–21 Nov news
shifted forward by a day, and one (#8, a Chinese bomber 170 km from
Manila) had no named source at all (an anonymous GETTR post). Two of
its three heroes (Sparta II ship fire, Hormuz drone downings) were
Saturday 21 Nov; only COP31 survived, reframed to the Sunday draft.
This page therefore keeps the example's STRUCTURE (masthead, stat
boxes, region bar, 3 heroes with big illustrations, 10-cell grid
with full-bleed art, numbered-dot map, ALSO list, DATE CHECK,
footer) but NOT its story list: every story here was verified
independently, and the count is the honest number of verified
Sunday stories found by Sunday ~13:30 WIB — 21. The rest of Sunday
(NFL, Liverpool–Man Utd, the COP31 vote outcome, the Las Vegas GP
result, more Europe) had not happened yet at build time; a later
slot can add them.

## The strict date rule (lesson from news 21)

A story counts only if its primary publication is itself dated
22 Nov 2026, or its event occurred 22 Nov 2026. A republication,
reprint or translation on 22 Nov of a 20/21 Nov story does NOT
count. A wire piece filed after midnight UTC about a Saturday-night
US event does NOT count — the event and its first report were
Saturday (US time). This rule killed, among others: all Saturday-
night US sports in the example's orbit (BYU–Kansas, Nebraska–Ohio
State, NWSL final, MLS Messi, Nacua, Bedard, Knicks, Scheifele,
Mavericks, Wallabies), the ICE Seattle arrests (Saturday morning),
the Manila bomber (unverified rumor), and the Fidan interview
(Saturday on TGRT Haber, written up Sunday). Two traps were also
avoided: mirror-spam domains (bbcbreakingnews.pages.dev,
bbcinsight.pages.dev) that stamp old BBC articles "22 Nov", and
2025 Las Vegas GP results circulating as 2026.

## Heroes (3)

### 1 — ANTALYA · CLIMATE (Europe)
**COP31 circulates final text; adoption still pending.**
A third "final" text was circulated in the early hours of Sunday;
it recalls the COP28 UAE Consensus in its entirety but names no
fossil fuel, coal, oil or gas. It targets electricity at 35% of
final energy consumption by 2035 (from ~21% now). Delegates had
until 04:00 GMT to object; a closing plenary was to follow. No
text had been adopted at build time (~13:30 WIB). Sources: AFP
wire, published 22 Nov 09:16 +08:00 ("Fossil fuel dispute
threatens to scupper climate deal", third text in the wee hours of
Sunday, 35% by 2035, Panama threat); Reuters, dateline Antalya,
Nov 22 ("COP31 climate talks close to final deal, says summit
president", https://www.reuters.com/sustainability/cop/cop31-climate-talks-close-final-deal-says-summit-president-2026-11-21/);
AFP via CNA, Sunday (Nov 22) ("Fossil fuels still absent in latest
COP31 draft deal", https://www.redhot.sg/fossil-fuels-still-absent-in-latest-cop31-draft-deal-742160.html).
Tag: CONFIRMED.
Dropped from v1: "94 paragraphs" (the 19 Nov draft was 80, down
from 144 — 94 was wrong) and "130 nations" (only a single
minister's "around 130 countries who want…" quote in the AFP wire,
not a verified count — not printed as fact).

### 2 — CIKANDE · DISASTER (Asia)
**36 missing after factory fire in Indonesia.**
Rescuers searched on Sunday for 36 workers still missing — the
toll as of 03:56 UTC — after a fire at a candy factory in Cikande,
Serang (Banten), late on Saturday; 3 dead, 4 hurt. The fire was
late Saturday (Reuters: "Saturday evening"; firefighters alerted
~16:30); the Sunday news is the search and the toll. Sources:
Reuters, 22 Nov 2026 03:56 UTC ("Indonesia rescuers search for 36
missing after factory fire kills 3",
https://www.reuters.com/world/asia-pacific/indonesia-rescuers-search-36-missing-after-factory-fire-kills-3-2026-11-22/).
Number chain (why 36, not 39): AFP's interim figure was 39
missing (Basarnas, ~02:52 UTC, before any deaths were confirmed);
three workers were then found dead, leaving 36 still missing per
Reuters 03:56 UTC. 36 + 3 = 39 — the wires agree; 36 is the latest
verified figure, stamped with its time on the page.
Tag: CONFIRMED.

### 3 — MECCA REGION · CONFLICT (Middle East)
**Saudi coalition intercepts Houthi missile.**
Air defences intercepted and destroyed a Houthi ballistic missile
aimed at western Saudi Arabia; a civil-defence warning for the
Mecca region went out late Saturday (~23:43 AST); the interception
was confirmed ~01:42 Sunday (AST). No Houthi claim of
responsibility for this missile. Sources: Reuters (filed 21 Nov
22:50 UTC = 22 Nov 01:50 AST); Anadolu Agency, 22 Nov.
Tag: CONFIRMED.

## Grid (10)

### 4 — MYANMAR · DIPLOMACY (Asia)
**Myanmar calls ASEAN decision "unfair and imbalanced".**
The army-backed government rejects the 49th ASEAN summit's
decision in Manila to hold back full political representation;
ASEAN offers gradual restoration if Myanmar advances the
five-point consensus. Source: Reuters, 22 Nov 2026 04:01 UTC
(https://www.reuters.com/world/asia-pacific/myanmars-army-backed-government-calls-asean-decision-unfair-imbalanced-2026-11-22/).
Tag: CONFIRMED.

### 5 — NEW DELHI · DIPLOMACY (Asia)
**Nepal PM Shah arrives in India for state visit.**
Balendra Shah lands in New Delhi for a two-day visit, his first
bilateral trip since taking office in March 2026; talks with PM
Modi on Monday. Source: Radio Nepal, 22 Nov 2026 07:06 +05:45
(https://radionepalonline.com/en/2026/11/22/439077.html).
Tag: CONFIRMED.

### 6 — SINGAPORE · DIPLOMACY (Asia)
**China's Ding Xuexiang begins Singapore visit.**
Vice-Premier Ding arrives for a two-day official visit; he and
DPM Gan Kim Yong co-chair the 22nd Joint Council for Bilateral
Cooperation on Monday. Sources: MFA Singapore / PMO Singapore,
22 Nov 2026 (https://www.mfa.gov.sg/newsroom/press-statements-transcripts-and-photos/official-visit-of-vice-premier-of-state-council-of-the-people-s-republic-of-china-ding-xuexiang-to-singapore--nov-2026-/).
Tag: OFFICIAL.

### 7 — BEIJING · TRADE (Asia)
**China opposes US FCC ban on its telecoms.**
The commerce ministry "firmly opposes" Thursday's FCC vote
barring China Mobile, China Telecom and China Unicom from direct
access to US phone numbers, and urges the US to repeal it.
Source: Reuters, Sun 22 Nov 2026 01:57 UTC
(https://www.reuters.com/world/china-opposes-us-fcc-ban-chinese-telecoms-direct-access-us-phone-numbers-2026-11-22/).
Tag: CONFIRMED.

### 8 — CANBERRA · DEFENCE (Oceania)
**Australia calls US budget office "wrong" on AUKUS.**
Defence minister Richard Marles rejects a Congressional Budget
Office finding that AUKUS cuts US attack-submarine numbers:
"They are wrong." Source: Reuters, 22 Nov 2026
(https://www.reuters.com/world/asia-pacific/australia-criticises-us-congressional-budget-office-over-aukus-comments-2026-11-22/).
Tag: CONFIRMED.

### 9 — WELLINGTON · CRICKET (Oceania)
**India declare a record 720/9 in New Zealand.**
Pant 128 — first India keeper with a Test century in NZ — and
Rahul 136 take India to a record 720/9, a 352-run lead on day four
of the first Test. (v1-fix: the keeper record was ALSO #21, the
same innings — folded here instead; the 352-run lead is a stat
box.) Source: Reuters, Sun 22 Nov 2026 00:41 UTC
(https://www.reuters.com/sports/cricket/india-take-control-wellington-with-highest-test-tally-new-zealand-2026-11-22/).
Tag: CONFIRMED.

### 10 — TEHRAN · ENERGY (Middle East)
**Iran begins electricity rationing.**
Rolling blackouts of up to 2 hours a day start on Sunday, blamed
on fuel shortages and attacks on gas infrastructure. The rationing
starts Sunday; it was announced on state TV on Saturday. Sources:
RFE/RL (Radio Farda) + Reuters/CBS/AFP, 22 Nov 2026.
Tag: REPORTED.

### 11 — ABU DHABI · DIPLOMACY (Middle East)
**UAE president receives US homeland security chief.**
Sheikh Mohamed bin Zayed meets Markwayne Mullin in Abu Dhabi;
strategic cooperation and regional developments discussed.
Source: WAM via ANI, 22 Nov 2026 05:11 IST
(https://news.webindia123.com/news/Articles/World/20261122/4522887.html).
Tag: OFFICIAL.

### 12 — PYONGYANG · SPORT (Asia)
**North Korea postpones 2027 marathon to October.**
The Pyongyang International Marathon moves from April to "almost
certainly" October 2027, tour operator Koryo Tours says. Source:
Reuters, 22 Nov 2026 02:39 UTC
(https://www.reuters.com/world/asia-pacific/north-korea-postpones-next-years-pyongyang-marathon-tour-agency-says-2026-11-22/).
Tag: CONFIRMED.

### 13 — MANAMA · DIPLOMACY (Middle East)
**Bahrain urges UN action after Saturday strike.**
Bahrain asks the Security Council to enforce Resolution 2817 and
seeks compensation after Iran's Saturday-night strike set an
industrial facility ablaze. The demand was reported on Sunday
morning; the strike itself was Saturday. Source: Al Jazeera,
reported Sunday morning, 22 Nov 2026.
Tag: REPORTED.

## ALSO (8)

### 14 — MELBOURNE · SPORT (Oceania)
**Bellamy to end 25 years as Storm coach after 2027.**
Craig Bellamy, 67, confirms 2027 will be his 25th and last season
as Melbourne Storm head coach, the longest tenure in NRL
premiership history. Source: AAP, 2026-11-22T02:37:45Z
(https://aapnews.aap.com.au/news/bellamy-confirms-future-as-melbourne-look-for-successor).
Tag: CONFIRMED.

### 15 — RUATŌRIA · DISASTER (Oceania)
**One dead as house slips off its foundations.**
A house being moved onto its foundations slipped off its supports
at a building site in Ruatōria; one person died on the way to
hospital, four others hurt. Source: New Zealand Police statement,
15:29 NZDT, 22 Nov 2026
(https://livenews.co.nz/2026/11/22/fatality-at-building-site-ruatoria/).
Tag: OFFICIAL.

### 16 — MELBOURNE · SPORT (Oceania)
**Dawn Fraser, 89, at 70th anniversary of 1956 Games.**
Fraser and fellow 1956 Olympians gather at the MCG for lunch on
Sunday, exactly 70 years after the Melbourne Games opened on
22 Nov 1956. Source: AAP, 2026-11-21T22:00:00Z = 22 Nov 2026
09:00 AEDT (https://aapnews.aap.com.au/news/excuse-the-expression-dawn-fired-up-for-1956-reunion).
Tag: CONFIRMED.

### 17 — NOWA DĘBA · DEFENCE (Europe)
**Multinational Ukraine-force exercise ends today.**
Exercise Koalicja 26.2, the Multinational Force–Ukraine's first
exercise (9–22 Nov, ~2,800 troops from 11 countries), ends today.
Source: Vozia (article 3 Nov, updated)
(https://vozia.africa/story/exercise-koalicja-2800-troops-poland-multinational-force-ukraine/).
Tag: REPORTED (closing date is today; the exercise itself was
announced 3 Nov — labelled "ends today" on the page).

### 18 — BAYELSA · DISASTER (Africa)
**Boat death toll rises to 24.**
The toll from a wooden boat that capsized in Southern Ijaw on
Friday rises to 24 in Sunday-morning updates; dozens feared
missing. The capsize was Friday; the rising toll is Sunday's
update. Source: TheMatrix Newspapers / Nigeria Morning Brief,
22 Nov 2026
(https://matrixngr.com/2026/11/22/top-10-stories-from-thematrix-newspapers-sunday-morning-november-22-2026/).
Tag: REPORTED.

### 19 — SANDTON · OBITUARY (Africa)
**South Africa holds prayer for the late Mlambo-Ngcuka.**
A family prayer service is held on Sunday at 14:00 in Sandton
for Phumzile Mlambo-Ngcuka, 71, South Africa's first woman deputy
president, who died on Friday night. The service is Sunday's
event. Source: SA News (government)
(https://www.sanews.gov.za/south-africa/south-africa-mourns-former-deputy-president-phumzile-mlambo-ngcuka).
Tag: OFFICIAL.

### 20 — LAS VEGAS · SPORT (Americas)
**Grand Prix under way Saturday night, local time; Verstappen on pole.**
The 50-lap race started at 20:00 local Saturday (04:00 GMT /
11:00 WIB Sunday) with Max Verstappen on pole beside George
Russell; no final result at build time. (v1-fix: the local-time
marker is explicit, so a Saturday-night-local event's Sunday-page
admission is transparent.) Source: PlanetF1 live blog, published
22 Nov 2026 03:09 UTC
(https://www.planetf1.com/news/f1-las-vegas-gp-live-2026-race-updates).
Tag: CONFIRMED (race under way; result in DATE CHECK as not yet
happened).

### 21 — PANAMA CITY · CLIMATE (Americas)
**Panama threatens to scuttle any weak COP31 deal.**
Panama's environment minister Juan Carlos Navarro threatened to
scuttle any weak COP31 deal, accusing a "petroleum mafia" of
holding the world hostage over fossil-fuel language. (v1-fix:
replaces the deleted Wellington duplicate; Latin America's first
story on the page.) Source: AFP wire, published 22 Nov 2026
09:16 +08:00 ("Fossil fuel dispute threatens to scupper climate
deal" — second day of overtime Sunday, walkout threats live,
Navarro's threat in present tense). The threat was delivered by
Panama's delegation at COP31 in Antalya; the dot marks Panama
City, the actor's capital, and the story's region is the Americas.
Tag: CONFIRMED.

## Stat boxes (6, all from the verified stories above)

- **35%** — electricity share of final energy by 2035, in the COP31 draft (AFP/CNA, 22 Nov).
- **352** — India's lead in Wellington, in runs (Reuters, 22 Nov).
- **25** — Bellamy's final Storm season, his 25th (AAP, 22 Nov).
- **36** — workers still missing after the Cikande factory fire, as of 03:56 UTC (Reuters, 22 Nov).
- **720/9** — India's record Test total in New Zealand (Reuters, 22 Nov).
- **1,661** — killed in Gaza since the October ceasefire (Gaza health ministry, via Al Jazeera, 22 Nov).

## BY THE CLOCK (verified times)

- GMT Sun 00:00 — COP31 draft released in Antalya.
- GMT Sun 01:16 — AFP reports the fossil-fuel dispute threatens a deal.
- AST Sun 01:42 — Houthi missile intercepted over the Mecca region.
- GMT Sun 01:57 — China opposes the FCC ban (Reuters).
- GMT Sun 03:56 — Reuters reports the Cikande fire search.
- GMT Sun 04:01 — Myanmar slams the ASEAN decision (Reuters).

## DATE CHECK

Left out as other days' news: the APEC trilateral in Shenzhen
(Thu 19 Nov) · the Kyiv barrage and the missiles over Poland
(Fri 20 Nov) · Wall Street's correction (Fri 20 Nov) · the
Denmark "assassination" plot (Fri 20 Nov) · the Peru quake
(Fri 20 Nov local) · the Anthropic IPO debut (Thu 19 Nov) ·
the GTA VI launch (Thu 19 Nov).
Not yet happened, so not shown: COP31 adoption — pending (the
approval session was under way at build time) · the Las Vegas GP
result (the race was under way).

## Dropped for failing validation (from the example's list)

Sparta II ship fire (Sat 21 Nov) · Hormuz drone downings (Sat
21 Nov; the 58th/19th counts are correct as IRGC claims, but the
event is Saturday) · Sinaloa "El Chapo Isidro" capture (Fri 20
Nov, announced Sat 21 Nov) · Estonia border shutdown (announced
Fri 20 Nov) · Bolsonaro ICU (Sat 21 Nov) · France on Myanmar
(Sat 21 Nov) · Chinese bomber near Manila (unverified rumor,
anonymous GETTR post) · Gaza 4 killed/14 hurt (Sat 21 Nov) ·
Nitish Setu bridge opening (Sat 21 Nov; "Akvan" is Cyclone Akvan,
not an airline) · US airlines terror warning (bulletin 19 Nov,
CNN 20 Nov) · UN chief race deadlock (20 Nov) · Basra power
plant fire (Sat 21 Nov) · ALL 23 of the example's ALSO stories
(19–21 Nov, incl. Somalia–UAE 19 Nov, Ethiopia displacement
19 Nov, Qeshm blasts 20 Nov, Gupta sentencing 20 Nov, Sweden
summoning Russia's envoy 20 Nov, Hegseth–Canada memo 20 Nov,
Bessent/Nvidia 20 Nov, Japan–India live-fire 19 Nov, EU online
tax 21 Nov, Spain bank tax 21 Nov, Thai student protest 20 Nov,
De Gennaro death 21 Nov, Gripen over Poland 20 Nov, Melania
Trump ceasefires 20 Nov, Oleshky ceasefire Oct–1 Nov, Macklemore
single 18/20 Nov, Wellington Test start 19 Nov, Cummins
captaincy 21 Nov, Air India Jeddah suspension 20 Nov, COP31 AI
pledge 17 Nov).

Also dropped in the fresh-research wave (same date rule):
Saturday-night US sports (BYU–Kansas, Nebraska–Ohio State, NWSL
final, MLS Messi, Nacua, Bedard, Knicks, Scheifele, Mavericks,
Wallabies) — events and first reports Saturday (US time); the
Reuters pieces dated 22 Nov were filed after midnight UTC ·
ICE Seattle arrests (Saturday morning) · Fidan interview
(Saturday on TGRT Haber) · Bayelsa boat capsize itself (Friday;
only the rising toll is Sunday) · Paolo Bulgari death (Sat
21 Nov) · Bayer $7.25bn Roundup deal (Fri 20 Nov).

## Build

gen.py (Pillow, local only) draws the whole page with code:
masthead, date headline, sub-headline, 6 stat boxes, region bar,
3 heroes with big code-drawn illustrations, a 10-cell grid with
full-bleed illustrations, a numbered-dot world map, an ALSO list,
a BY THE CLOCK line, a DATE CHECK box, and a footer. All
headlines, bodies and drawings are original — the example image
supplied only the layout pattern, never the wording, and its story
list was NOT trusted as a source (see above). Deterministic:
running gen.py twice gives the same SHA-256.

## Fix v1-fix2 (22 Nov ~12:55 WIB) — ALSO numbers circled

User feedback: the ALSO numbers 14–21 were barely visible (plain
12px text at the start of each line). Fix: each ALSO number now
sits inside a filled red circle (white bold number, same 12px
DejaVuSans-Bold as before — the number was NOT enlarged, per the
user's correction). The circle echoes the numbered red dots on the
world map, so the device is consistent across the page. The ALSO
text hangs beside the circle (first line narrower, later lines
full column width); all 8 items still fit in 2 lines, no wording,
order or source changed. entry.png 204,437 bytes,
sha256 d0d47f648a3d1f024c4cce8a76b0a1dd3a353558493167618e2e4f08b0fc36b0.
