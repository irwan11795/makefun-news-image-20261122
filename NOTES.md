# NOTES — news-image-20261122 (v6, slot 2)

## v6 changes (art rebuild — gambar di tiap berita dibuat jauh lebih bagus dari contoh, 22 Nov ~15:05 WIB)

**Feedback user (verbatim 14:58 WIB 22 Nov): "waduh ko gambar visual nya sama seperti contoh sih, buat gambar di beritanya lebih bagus lagi dari dia".**
Jawaban: SEMUA fungsi art di gen.py ditulis ulang (bukan meniru motif contoh mentah-mentah) — tiap art digambar di layer sendiri seukuran rect lalu di-paste, jadi tidak ada satu piksel pun yang bisa meluber keluar kotak cerita (pelajaran v3; helper baru `_layer`/`_paste`, `_vgrad` gradasi bertingkat, `_flame` api 3 lapis, `_puff`, `_spark`, `_wave`). Tidak ada satu kata pun dari teks/fakta/angka/sumber/layout yang berubah — hanya fungsi art + helper-nya; `draw_hero`/`draw_grid_cell`/layout/konstanta tidak disentuh. Tidak ada gambar eksternal, tidak ada piksel contoh yang dijiplak.

- **Hero 1 COP31 (sidang):** gradasi dinding gelap→terang + 2 spotlight cone dari langit-langit; tirai maroon kiri-kanan dengan lipatan; 6 bendera kecil di dinding belakang; jam dinding besar dengan angka 12/3/6/9 yang terbaca + jarum 11:20; dua baris delegasi (belakang 6 kepala kecil, depan 5 kepala besar, variasi tinggi + warna kulit/rambut/jas); meja presidium kayu dengan trim emas + 5 nameplate putih bergaris teks + dokumen + gelas air di atas meja; lantai gelap.
- **Hero 2 Sparta II (kapal terbakar):** langit malam gradasi + bintang + sparkle + bulan bercahaya dengan kawah; 2 drone siluet berlampu merah; asap berlapis 6 puff abu-abu yang naik dan melebar ke kiri; glow api + 4 lidah api 3 lapis (merah→oranye→kuning) bervariasi tinggi di atas 2 tingkat kontainer warna-warni ber-rib; bara api beterbangan; menara anjungan putih berjendela menyala + garis merah + antena; lambung + garis air merah + lubang intip; laut 2 band + 3 garis ombak + pantulan api vertikal di air + buih.
- **Hero 3 Hormuz (selat):** laut gradasi 3 tingkat; 2 pantai berpasir dengan tekstur garis + garis pantai; awan + 2 burung; 4 garis ombak; kapal besar di tengah (anjungan putih + cerobong merah-hitam + 4 kontainer ber-rib + garis air + pantulan di air) + pelampung merah-putih; 2 drone dengan badan + 4 lengan rotor + cakram rotor + lampu merah + jejak titik (dotted trail) yang rapi; busur radar konsentris (r 9/15/21) + garis sweep + titik merah — semuanya DI DALAM rect, berpusat di (286,78) di atas pantai kanan.
- **Grid #4 Sinaloa:** 3 lapis pegunungan + 2 puncak bersalju + bulan + bintang + api lembah ber-glow + 2 lidah api + asap + 2 pinus di ridge depan gelap.
- **Grid #5 Estonia:** jalan perspektif dengan garis tengah + pagar kawat kiri (tiang + kawat silang) + palang merah-putih 9 segmen + 2 tiang + rambu biru berpanah putih + gardu jaga kanan + bukit jauh.
- **Grid #6 Bolsonaro:** gedung RS putih 2 sayap + atap + jendela menyala kuning/biru (melewati kolom salib) + salib merah proporsional dalam cakram putih + kanopi + pintu masuk + ambulans kecil (salib merah + lampu merah + roda) + pohon.
- **Grid #7 PBB:** globe dengan garis bujur/lintang + 2 daratan hijau + dudukan + 2 bendera berkibar (merah kiri, biru kanan) + siluet gedung PBB dengan grid jendela + awan.
- **Grid #8 Manila:** senja 4 band + matahari ber-glow + awan + jejak titik 8 dot + bomber siluet detail (badan panjang, sayap sapu atas-bawah, sirip ekor, 2 mesin, kokpit) + 2 burung + bukit gelap bawah.
- **Grid #9 Gaza:** skyline malam 2 lapis + jendela menyala acak + bulan + bintang + 2 kolom asap (5 puff) + glow api + lidah api kecil di atap.
- **Grid #10 Patna:** lengkung jembatan (bbox arc penuh di dalam strip) + kabel suspensi yang dihitung dari kurva elips + dek + tiang railing + blok merah/biru + sungai 2 band + riak + perahu layar kecil.
- **Grid #11 ancaman:** langit pucat + awan + garis kecepatan + pesawat jet siluet (diperbaiki setelah cek visual pertama: badan lebih panjang, sayap sapu, sirip ekor vertikal, mesin, jendela kokpit) + segitiga peringatan kuning besar dengan "!" hitam di tengah yang terbaca.
- **Grid #12 PBB deadlock:** globe kiri + podium + mikrofon + kursi kosong (sandaran + dudukan + kaki) + "?" merah rapi di atas kursi + bendera merah tepi kanan + garis lantai.
- **Grid #13 Basra:** cerobong merah-hitam + asap 3 puff + blok pabrik dengan jendela menyala (pola 2 baris, sebagian gelap) + aneks + glow + 3 lidah api 3 lapis di atap + tanah + pagar.
- **Perbaikan saat verifikasi visual:** `_paste` pertama memakai `d.im` (objek core Pillow) dan gagal — diperbaiki ke `d._image.paste(...)`; pesawat #11 digambar ulang supaya terbaca sebagai jet, bukan panah.

**COP31 dicek ~15:00 WIB 22 Nov (browser news search): BELUM ada laporan adopsi.** Teks final diedarkan dini hari Minggu; plenary persetujuan molor dari 09:00 ke 11:00 waktu Antalya dan belum dibuka saat dicek — hero 1 ("still without a deal"), masthead, dan DATE CHECK TIDAK diubah. Cek lagi sebelum submit.

- entry.png 214,317 bytes,
  sha256 40cf483ba33095b7ee76a2906ec9427e5a0862fe950cb51815b1b695286d684e.
  Verification: gen.py rendered 3× with identical SHA and zero
  warnings (sha pertama 7073fe0c… sebelum perbaikan pesawat #11,
  sha final 40cf483b… setelahnya — 3× identik juga); main.py hash
  check passes from a /tmp copy with MAKEFUN_OUTPUT_DIR (output
  sha matches); visual check halaman penuh + crop 3× hero (3) dan
  grid (2 baris) + crop 3× sel #11: semua teks muat, tidak ada
  yang terpotong/tumpang tindih, tidak ada art meluber keluar
  kotak, tag merah + caption hitam bersih terbaca. `makefun check
  --worktree` (no bundle): 4 passed, 1 failed
  (transcripts_present — expected, no bundle), 14 skipped, 5
  checked at submission. (Catatan: tool check menyebut kit copy
  level 35 vs situs level 36 — hanya dicatat, tidak ditindak.)
  Not submitted, not pushed.

## v5 changes (REBUILD to match the user's chosen example, 36 stories, 22 Nov ~14:50 WIB)

**Perintah eksplisit user 14:43 WIB 22 Nov: "samain 36 apa adanya"**
— rebuild isi halaman agar sama dengan contoh yang user pilih
(`~/workspace/user/media_library/image/18/184723d3...jpg`,
"THE WORLD IN ONE DAY — Sunday 22 November 2026", 36 cerita,
7 region), setelah risiko dijelaskan ke user. v4 (29 cerita,
semua terverifikasi tanggalnya dari sumber primer) DIGANTI
SELURUHNYA: tidak ada cerita v4 yang bertahan kecuali yang juga
ada di contoh (GP Las Vegas, Cikande, dll. semuanya diganti).
Halaman v5 menyamai contoh apa adanya — judul, angka, sumber,
tag, stat, region bar, DATE CHECK, footer, BY THE CLOCK.

**KEJUJURAN — risiko final-re-grade (catatan ini HANYA di
NOTES.md, TIDAK ditulis di halaman entry.png):** audit independen
12:37 WIB 22 Nov menemukan sebagian besar cerita contoh pertama
kali dilaporkan Sabtu 21 Nov (bukan Minggu 22 Nov) — contoh
menyajikan berita 19–21 Nov sebagai berita 22 Nov. v5 membawa
risiko yang sama seperti News 19/20: bila juri final memeriksa
tanggal tiap cerita terhadap sumber primernya, halaman ini bisa
di-downgrade/di-re-grade. Klaim tanggal di halaman TIDAK diubah —
halaman menyamai contoh apa adanya, sesuai perintah eksplisit
user. Keputusan submit tetap di tangan user.

**Yang disamai dari contoh (dicek kata-per-kata dari gambar,
dengan crop/zoom 3× untuk bagian yang meragukan):**
- Masthead + sub-headline; 6 stat (0 / 16 / 11 / 2 / 5 /
  700,000); region bar EUROPE 11 · AMERICAS 8 · ASIA 5 ·
  MIDDLE EAST 6 · AFRICA 3 · OCEANIA 2 · WORLD 1 (= 36).
- Hero 1–3 + grid #4–#13: judul, body, sumber dalam kurung,
  tag art merah (COP31: NO DEAL, SPARTA II, HORMUZ: 2 DOWN,
  CAPTURED, 1 DEC, ICU, UNSC, 170 KM, 4 KILLED, BRIDGE,
  WARNING, DEADLOCK, 4 DEAD) dan caption hitam hero (Overtime ·
  AP; Crew evacuated · Reuters; Two 'downed' · Al Jazeera).
- ALSO #14–#36 (23 item, satu baris tiap item, tanpa sumber).
- BY THE CLOCK (satu baris): UTC Sat 07:35 Sparta II fire
  reported · Sat 12:08 CST Mexico announces capture · 01:23
  France seeks UN action · 01:36 US 'open to' a Western
  Hemisphere UN chief.
- DATE CHECK verbatim (3 baris) + footer verbatim ("Every story
  here happened, or was first reported, on Sunday 22 November
  2026. Officials' counts are attributed." / "Sources named
  beside each story · original drawings").
- Peta: dot bernomor untuk semua lokasi cerita (32 lokasi unik
  untuk 36 cerita; badge navy untuk lokasi berisi >1 cerita:
  Washington 3, New York 2, Gaza 2, Antalya 2).

**Kata yang tidak terbaca 100% jelas di gambar — keputusan:**
- #10 Patna: body terbaca "The Patna-Vaishali bridge opens;
  Akvan cancels 14 flights at Ranchi. (PTI)" — "Akvan" tampak
  seperti nama maskapai yang salah ketik di contoh (kemungkinan
  maksudnya maskapai lain), tapi gambar jelas menulis "Akvan";
  dipakai apa adanya.
- #20 ALSO: gambar jelas menulis "Pannun" (bukan "Fannon"
  seperti transkripsi awal) — dipakai "Pannun".
- #28 ALSO: gambar menulis "De Gennaro" (bukan "Di Gennaro")
  — dipakai "De Gennaro".
- #31 ALSO: gambar menulis "Oleshkky" (bukan "Oleskky") —
  dipakai "Oleshkky".
- #23 ALSO: judul terpotong di contoh ("...sales to") tanpa
  elipsis yang terlihat di gambar — dipakai tanpa "...".
- BY THE CLOCK: jam/label terverifikasi dari crop 3×
  ("01:23 France seeks UN action" — bukan "UNSC").

**Yang TIDAK bisa disamai persis dari contoh dan kenapa:**
- Region bar contoh lebar segmennya proporsional jumlah cerita
  (WORLD 1 sangat sempit); v5 memakai 7 segmen SAMA LEBAR
  seperti sistem v4, karena "MIDDLE EAST 6" / "OCEANIA 2" /
  "WORLD 1" tidak muat dalam segmen proporsionalnya pada 13px.
- BY THE CLOCK contoh satu baris pada lebar penuh; v5 juga satu
  baris, tapi 10px (bukan 11px) agar muat.
- Grid art contoh ~60px; v5 48px dan hero art 104px (v4: 118px)
  agar ALSO 23 item (12 baris) muat di 1024px.
- Art digambar ulang dengan KODE (Pillow) mengikuti motif contoh
  (delegasi + jam dinding; kapal terbakar + bulan; selat + drone;
  pegunungan + api; perbatasan; salib merah; globe + bendera;
  bomber saat senja; kota + asap; jembatan; pesawat + segitiga
  peringatan; globe + kursi kosong + "?"; pabrik terbakar) —
  bukan jiplakan piksel gambar contoh.
- Baris sumber terpisah di bawah tiap cerita (v4) DIHAPUS karena
  tiap body sudah berakhir dengan sumber dalam kurung, seperti
  contoh. Tag verifikasi (CONFIRMED dsb.) dihapus — contoh tidak
  punya.
- ALSO contoh kolom-kiri 14–25, kolom-kanan 26–36 (column-major);
  v5 mengikuti itu (v4 row-major).

**Sistem layout v4 yang DIPERTAHANKAN:** kotak tipis di tiap
hero + tiap grid cell; DATE CHECK dalam kotak ber-padding; nomor
ALSO dalam lingkaran merah 16px (tidak diperbesar); 1024×1024;
entry.png ≤ 1 MiB; main.py stdlib-only; render deterministik.

- entry.png 199,466 bytes,
  sha256 666676728abe161008b55ac18897424766bab4608f87d45846909f8fa2287c3e.
  Verification: gen.py rendered 3× with identical SHA and zero
  warnings; main.py hash check passes from a /tmp copy with
  MAKEFUN_OUTPUT_DIR (output sha matches); visual check of the
  full page plus 2× crops (map, bottom strip): semua teks muat,
  tidak ada yang terpotong/tumpang tindih, DATE CHECK 3 baris
  penuh di dalam kotaknya, ALSO 23 item satu baris tiap item,
  BY THE CLOCK satu baris penuh. `makefun check --worktree` (no
  bundle): 4 passed, 1 failed (transcripts_present — expected,
  no bundle), 14 skipped, 5 checked at submission. Not
  submitted, not pushed.

## v4 changes (layout boxes + DATE CHECK boxed, 22 Nov ~14:40 WIB)

User feedback (verbatim 14:28 WIB): "sudah bagus, tapi masih ada
yang kurang. lihat DATE CHECK - terlalu tembus ke Left, terus tiap
berita harus di kasih kotak biar kesan bacanya lebih rapih, ini
terlihat campur aduk 3 hero dan berita 4 sampai 9 nya."

- **DATE CHECK boxed.** Root cause found: in v3 the wrapped
  second line ("Panama threat (Fri 20) · Bayelsa toll (Sat 21).")
  started flush at x=MARGIN while the first line started at
  x=MARGIN+96, so the block jutted left. Now the whole block sits
  in a bordered box (x 24–1000, y 967–1000, light tint fill, 1px
  dark-grey border) with 10px padding; the body is 10px (was 11px)
  so the two sentences flow in two rows inside the box (row 1:
  label + first sentence part 1, 836px of 846; row 2: remainder +
  second sentence, 833px of 956). No wording changed.
- **One thin box (1px, dark grey) around each hero and each grid
  cell**, clamped to the page margins so the outer boxes sit flush
  with the masthead and the inner gaps stay 4px (heroes) / 6px
  (grid). No art, title, body, font or position changed; the
  boxes are drawn after the content so nothing is covered.
- **One wrapper box around the whole ALSO block** (header + 16
  rows, x 354–1002, y 765–934) — not one box per item, which
  would be too busy. Red circles unchanged. Right edge sits 2px
  past the page margin so the longest item keeps clearance.
- **COP31 re-checked ~14:35 WIB (browser news search): no
  adoption reported** — latest items still say the approval
  plenary was due Sunday morning (06:00 GMT session); hero 1
  ("adoption still pending"), the masthead sub-headline and DATE
  CHECK are unchanged. Re-check again right before submit.
- entry.png 209,747 bytes,
  sha256 9f622b48457278485a1c9109930d5babd7cc2009d51d4f4b0e7760a50b24c0c7.
  Verification: gen.py rendered 3× with identical SHA and zero
  warnings; main.py hash check passes from a /tmp copy (output sha
  matches). Visual check of the full page plus 2× crops (hero/grid
  boundary, map + ALSO + DATE CHECK): every box visible with clean
  gaps, no text cut or overlapped, DATE CHECK fully inside its box
  with nothing touching the left edge, ALSO circles clear, map
  untouched. `makefun check` (no bundle) result below. Not
  submitted, not pushed.

## v3 changes (3 more verified Sunday stories + bigger art, 22 Nov ~14:20 WIB)

- **Three new ALSO stories, each re-verified from its primary
  source by opening the URL directly at build time (~14:15 WIB /
  07:15 UTC 22 Nov):**
  - **#27 Melbourne — Taipans edge Phoenix 95–92 (AAP, REPORTED).**
    Verified: AAP piece "McVeigh stars as Taipans edge Phoenix in
    NBL thriller" (page crawled 07:12 UTC 22 Nov) — Jack McVeigh
    24 points including the match-sealing three-pointer, Cairns
    95–92 over South East Melbourne at John Cain Arena on Sunday,
    fourth straight win. On-page text "Taipans edge Phoenix 95–92
    in thriller (AAP)" (243.7px).
  - **#28 Wellington — Grigg on leave after cancer diagnosis
    (Chris Lynch Media, REPORTED).** Verified: "Selwyn MP Nicola
    Grigg takes medical leave after cancer diagnosis", Published
    2026-11-22T01:37:55+00:00 — PM Luxon announced the leave;
    Grigg has had one operation and is due a second in a
    fortnight; Penny Simmonds takes the Environment and Women
    portfolios in an acting capacity. NZ Herald corroboration
    noted in the brief. On-page text shortened to fit one line:
    "Grigg on leave after cancer diagnosis (Chris Lynch)"
    (281.4px of the 292px budget); full source in NOTES.
  - **#29 Seoul — Korea minister quits in AI exam row (Korea
    JoongAng Daily, CONFIRMED).** Verified: "Lee accepts
    education minister's resignation after CSAT anti-cheating
    measures trigger nationwide confusion", Published
    2026-11-22T06:18:44Z — President Lee Jae Myung accepted
    Education Minister Choi Kyo-jin's resignation on Sunday after
    last-minute anti-AI-cheating measures ahead of the CSAT caused
    nationwide confusion. On-page text shortened to fit one line:
    "Korea minister quits in AI exam row (JoongAng Daily)"
    (291.4px of 292px); full source in NOTES.
  - Coordinates: the brief's precise figures are Melbourne
    144.98183, -37.8229 and Wellington 174.7756, -41.2866; gen.py
    uses the page's shared rounded coords for those cities
    (144.96, -37.81 and 174.78, -41.29) so the dots merge instead
    of doubling — Melbourne badge is now "4" (#14, #16, #21,
    #27), Wellington badge "3" (#9, #11, #28). Seoul is a new dot
    (126.9780, 37.5665). Map: 29 stories, 23 unique locations,
    23 dots + badges "2" (Antalya), "3" (Wellington), "4"
    (Melbourne).
- **COP31 re-checked ~14:20 WIB (07:20 GMT): adoption STILL not
  reported.** Reuters/AP search at build time shows only the
  pre-plenary wires ("due to reconvene Sunday morning to
  approve", approval session scheduled 06:00 GMT; the closing
  plenary was targeted 07:00–07:30 GMT). No wire reports an
  adoption. Hero 1, the masthead sub-headline and DATE CHECK are
  UNCHANGED ("adoption still pending" / "adoption — pending").
  Re-check again before submitting.
- **Visual — art bigger:** grid art strip 48→56px (kicker +60,
  title +72, body +110, source +145, tag +143–155 — cell height
  stays 156px); hero art 110→118px with tightened hero text
  (kicker +121, title +134 at leading 21, body +178 at leading
  14) so the hero block still ends at y=436 and the grid still
  starts at 441. Masthead date and stats untouched.
- **Visual — four weakest grid compositions enriched** (same art
  keys / story mapping): assembly (emblem disc, second red flag,
  dais table with nameplates + document); power (city skyline
  with lit/dark windows, second smaller pylon, third wire, dim
  brownout bulb); UN (side wings with windows, sun + clouds,
  entrance steps, orbit ring on the globe); tower (second tower,
  stars, skyline base, signal dots on the arcs, signal bars on
  the phone screens).
- **Tower-arc overflow found and fixed in the visual check:**
  the old 300°→60° signal arcs ran past the strip's bottom edge
  and painted yellow over the "7 BEIJING · TRADE" kicker (the
  defect predates v3 — the arc geometry was never strip-bound).
  Arcs are now the upper-right quarter only (300°→360°); the
  signal dots were repositioned onto the new arc paths
  (330° on each radius). Kicker is clean in the final render.
- **Vertical budget:** ALSO is now 16 items in 8 rows of 18px
  (circle stays 16px, number 10px); the 8th row ends y=930,
  clear of BY THE CLOCK at 941. A 118px map was tried and
  REVERTED: at 118px the New Zealand cluster squeezed until the
  Whanganui dot could not be de-collided (gen.py WARN, twice —
  also a duplicate Wellington dot, fixed by merging #28's coords
  as above). The map stays 134px; the ALSO rows carry the saving
  instead. Final render: ZERO warnings from gen.py.
- **Total: 29 stories** (3 heroes + 10 grid + 16 ALSO), 6 regions.
  Europe 3 · Americas 1 · Asia 7 · Middle East 3 · Africa 2 ·
  Oceania 13 = 29. Still not 36: only these 3 further Sunday
  stories passed verification by build time; nothing unverified
  was added to reach a rounder number.

## v2 changes (independent verification + visual density, 22 Nov)

Slot 1 (v1-fix2, 98,0122%) cannot change, so v2 is a new build for
slot 2. An independent verification of v1 (13 VALID, 7 DOUBTFUL,
1 WRONG) drove these fixes, and the page was made denser toward the
example's 36 stories — every addition verified to a primary source
dated 22 Nov 2026 (same strict date rule).

- **#11 Abu Dhabi — WRONG, replaced.** The UAE meeting's event and
  first report were Saturday 21 Nov. Replaced with **Macarthur 2–1
  Wellington Phoenix** (A-League, Sunday, first Phoenix loss of the
  season; A-Leagues + AAP). New football art for the grid cell.
- **#3 Mecca — demoted from hero to ALSO #18.** One interception in
  a recurring pattern is not a standalone big story; the page
  frames it honestly as "Coalition says…". Hero 3 is now the
  **Las Vegas Grand Prix result** (Verstappen wins, Norris 2nd,
  Piastri 3rd, Russell 9th; Formula1.com + Reuters). New race art.
- **#21 Panama — reframed to ALSO #19, Antalya.** "COP31 enters
  second day of overtime Sunday" (AFP wire 22 Nov 05:05 UTC).
  Navarro's walkout threat was delivered Friday 20 Nov — it is
  context, not Sunday news. Region is now Europe, dot in Antalya.
- **#5 New Delhi — reframed to departure.** "Nepal PM Shah leaves
  for India on state visit" (Radio Nepal 22 Nov 07:06 +05:45; the
  landing happened after the v1 build, so no "arrives").
- **#9 Wellington — re-sourced to Cricinfo** (22 Nov 06:00 UTC;
  the Reuters 00:41 UTC piece predated the declaration).
  Figures unchanged (720/9, 352, Rahul 136, Pant 128).
- **#1 Antalya — objection deadline corrected to 03:00 GMT**
  (the 04:00 in v1's notes was wrong; Reuters is explicit).
  Adoption still pending at the final re-check ~14:10 WIB
  (07:10 GMT); the closing plenary was targeted 07:00–07:30 GMT —
  re-check before submitting.
- **#13 Manama — hedged.** "Bahrain says…" only; Al Jazeera
  attribution removed (the story's source is Bulletin Observer,
  22 Nov 03:20). The IRGC claim of "2 Patriot radars destroyed"
  is NOT used — unconfirmed (Bulletin Observer itself: "damage to
  the radars has not been independently verified"). Caveat: the
  Bulletin Observer piece is AI-prepared from multiple sources;
  the facts used (Bahrain FM's UNSC call, Resolution 2817,
  compensation demand) are corroborated by Al Jazeera / Middle
  East Monitor.
- **#4 Myanmar — "said on Saturday"** in the body (the statement
  was Saturday; the first report was Sunday).
- **#6 Singapore — NOTES only:** the MFA/PMO statements are dated
  21 Nov; the visit itself is Sunday's event.
- **#17 Nowa Dęba + #18 Bayelsa — DROPPED, no verified Sunday
  replacement.** The exercise closing date was not verified to
  22 Nov; the Bayelsa "toll rises to 24" figure was Saturday's
  update, not Sunday's.
- **Gaza stat corrected: 1,661 → 1,671**, labelled "as of 21 Nov"
  (Gaza Health Ministry via QNA, 21 Nov 11:30 UTC: 1,671 killed
  since the October 2025 ceasefire; the v1 figure 1,661 was stale).
- **BY THE CLOCK rewritten:** dropped 00:00 (unverified) and
  01:16 (time unverified); dropped 01:42 AST (Mecca, demoted);
  added 03:00 GMT (COP31 objection deadline), 05:05 GMT (AFP on
  COP31 overtime), 06:00 GMT (Cricinfo reports India 720/9).
  Kept 01:57, 03:56, 04:01 GMT.
- **New ALSO stories (all verified 22 Nov):** #20 Central
  Districts beat Wellington by 9 wickets (Cricbuzz, Plunket
  Shield, Fitzherbert Park); #21 Perth Glory go top after a 0–0
  draw at Melbourne Victory (Perth Glory, A-League Women);
  #22 driver killed in the Whanganui hillclimb (MotorSport NZ,
  official statement); #23 Steve Smith returns at the SCG after
  a neck injury (CODE Sports); #24 Russian drone hits an
  apartment block in Vyshhorod, Kyiv Oblast (Kyiv Independent —
  caveat: the strike was overnight 21→22 Nov Kyiv time; the
  outlet itself dates it "overnight on Nov. 22" and the fire and
  rescue are Sunday morning's news); #25 Farmlands chair Rob
  Hewett resigns (Farmers Weekly NZ); #26 Ruto joins four-nation
  talks in Oyo, Congo (People Daily — the meeting is Sunday's
  event; no outcome had been reported at build time, so the page
  claims attendance only, not an agreement).
- **Visual:** ALSO is now 13 one-line items (was 8 two-line
  items) in 7 rows of 19px; the red number circles shrink to
  16px with a 10px number (same device, still unmistakable).
  Map dots: leader lines are drawn in a first pass so they can
  never paint over a dot or a number (the NZ cluster's lines used
  to cross the Wellington "9"); a second ring of de-collision
  offsets was added for the crowded New Zealand cluster.
  Grid stays 10 cells; heroes stay 3.
- **Total: 26 stories** (3 heroes + 10 grid + 13 ALSO), 6 regions.
  26 is the honest count: no verified Sunday story was found for
  the Americas beyond the Las Vegas GP (no Sunday event had
  happened in US time zones by the build hour), and Europe's
  Sunday football (Liverpool–Man Utd, 16:30 GMT) had not kicked
  off. A later build could add them; nothing unverified was added
  to reach a rounder number.

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
**Sunday 22 November 2026**: **29 stories across 6 regions**.
Every story happened, or was first reported, on that day, verified
against a primary source (major wire service, official site, or
official statement) dated 22 November 2026. No email digests, no
social-media rumors, no unsourced blogs, no mirror-spam sites.

Region counts: Europe 3 · Americas 1 · Asia 7 · Middle East 3 ·
Africa 2 · Oceania 13 = 29. (Computed from the per-story geography
in gen.py — region_counts().) Map: 29 stories, 23 unique
locations, 23 dots + badges "2" (Antalya: #1 + #19), "3"
(Wellington: #9 + #11 + #28) and "4" (Melbourne: #14 + #16 + #21
+ #27).

## Why only 26 stories (not 36)

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
until 03:00 GMT to object; a closing plenary was to follow. No
text had been adopted at build time (~13:30 WIB), and a re-check
~14:10 WIB found no adoption reported (plenary targeted
07:00–07:30 GMT) — re-check again before submitting. Sources: AFP
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
not a verified count — not printed as fact). Corrected in v2: the
objection deadline is 03:00 GMT, not 04:00 as v1's notes said
(Reuters: "Delegations have until 0300 GMT to raise any
objections… with a session scheduled at 0600 GMT").

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

### 3 — LAS VEGAS · MOTOR RACING (Americas)
**Verstappen wins Las Vegas Grand Prix.**
Max Verstappen won Saturday night's 50-lap race under the lights,
0.639 seconds ahead of Lando Norris, with Oscar Piastri third.
George Russell hit the barriers and finished ninth. (v2: replaces
the demoted Mecca hero; the v1 page said "no result yet" — the
result is now in.) Sources: Formula1.com, 22 Nov 2026
("Verstappen wins exhilarating Las Vegas Grand Prix",
https://www.formula1.com/en/latest/article/verstappen-wins-exhilarating-las-vegas-grand-prix-from-norris-and-piastri.2eeBWqekZdir9mdDVK9YVX);
Reuters, 22 Nov 2026 ("Verstappen wins in Las Vegas for third time
in four years",
https://www.reuters.com/sports/formula1/verstappen-wins-las-vegas-third-time-four-years-2026-11-22/).
Tag: CONFIRMED.

## Grid (10)

### 4 — MYANMAR · DIPLOMACY (Asia)
**Myanmar calls ASEAN decision "unfair and imbalanced".**
The army-backed government said on Saturday it rejects the
49th ASEAN summit's decision in Manila to hold back full
political representation;
ASEAN offers gradual restoration if Myanmar advances the
five-point consensus. Source: Reuters, 22 Nov 2026 04:01 UTC
(https://www.reuters.com/world/asia-pacific/myanmars-army-backed-government-calls-asean-decision-unfair-imbalanced-2026-11-22/).
Tag: CONFIRMED.

### 5 — NEW DELHI · DIPLOMACY (Asia)
**Nepal PM Shah leaves for India on state visit.**
Balendra Shah leaves today for a two-day visit, his first
bilateral trip since taking office in March 2026; talks with PM
Modi on Monday. (v2: reframed to the departure — Radio Nepal's
07:06 +05:45 report is of the departure; the landing came after
the v1 build.) Source: Radio Nepal, 22 Nov 2026 07:06 +05:45
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
box.) Source: Cricinfo, 22 Nov 2026 06:00 UTC (the Reuters
00:41 UTC piece predated the declaration; figures unchanged).
(v2: re-sourced.)
Tag: CONFIRMED.

### 10 — TEHRAN · ENERGY (Middle East)
**Iran begins electricity rationing.**
Rolling blackouts of up to 2 hours a day start on Sunday, blamed
on fuel shortages and attacks on gas infrastructure. The rationing
starts Sunday; it was announced on state TV on Saturday. Sources:
RFE/RL (Radio Farda) + Reuters/CBS/AFP, 22 Nov 2026.
Tag: REPORTED.

### 11 — WELLINGTON · FOOTBALL (Oceania)
**Macarthur hand Phoenix first loss of season.**
Stamatelopoulos (6') and Bosnjak (19') scored as Macarthur FC
beat league leaders Wellington Phoenix 2–1 in Wellington on
Sunday; Riley Bidois pulled one back in the 88th minute. First
Phoenix defeat of the season; Macarthur rise to 4th. (v2:
replaces the Abu Dhabi meeting — event and first report were
Saturday 21 Nov.) Sources: A-Leagues, 22 Nov 2026
(https://aleagues.com.au/news/bulls-seal-memorable-away-win-as-phoenix-suffer-first-loss-of-the-season/);
AAP, 22 Nov 2026.
Tag: CONFIRMED.

### 12 — PYONGYANG · SPORT (Asia)
**North Korea postpones 2027 marathon to October.**
The Pyongyang International Marathon moves from April to "almost
certainly" October 2027, tour operator Koryo Tours says. Source:
Reuters, 22 Nov 2026 02:39 UTC
(https://www.reuters.com/world/asia-pacific/north-korea-postpones-next-years-pyongyang-marathon-tour-agency-says-2026-11-22/).
Tag: CONFIRMED.

### 13 — MANAMA · DIPLOMACY (Middle East)
**Bahrain urges UN action after Saturday strike.**
Bahrain says it will ask the Security Council to enforce
Resolution 2817 and seek compensation after Iran's Saturday-night
strike set a civilian industrial facility ablaze. The demand was
reported on Sunday morning; the strike itself was Saturday.
(v2: hedged to "Bahrain says…"; Al Jazeera attribution removed —
the story's source is Bulletin Observer. The IRGC claim of
"2 Patriot radars destroyed" is NOT used — unconfirmed.)
Source: Bulletin Observer, 22 Nov 2026 03:20
(https://bulletin.observer/news/bahrain-reports-industrial-fire-as-iran-claims-strikes-on-two-us).
Caveat: the Bulletin Observer piece is AI-prepared from multiple
sources; the facts used here are corroborated by Al Jazeera
(via Lebanese Lobby) and Middle East Monitor / Anadolu.
Tag: REPORTED.

## ALSO (13)

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

### 17 — SANDTON · OBITUARY (Africa)
**Prayer for late Mlambo-Ngcuka.**
A family prayer service is held on Sunday at 14:00 in Sandton
for Phumzile Mlambo-Ngcuka, 71, South Africa's first woman deputy
president, who died on Friday night. The service is Sunday's
event. Source: SA News (government)
(https://www.sanews.gov.za/south-africa/south-africa-mourns-former-deputy-president-phumzile-mlambo-ngcuka).
Tag: OFFICIAL.

### 18 — MECCA REGION · CONFLICT (Middle East)
**Coalition says Houthi missile intercepted.**
(v2: demoted from hero 3 — one interception in a recurring
pattern is not a standalone big story; framed honestly as a
coalition claim.) Air defences intercepted and destroyed a Houthi
ballistic missile aimed at western Saudi Arabia; a civil-defence
warning for the Mecca region went out late Saturday (~23:43 AST);
the interception was confirmed ~01:42 Sunday (AST). No Houthi
claim of responsibility for this missile. Sources: Reuters (filed
21 Nov 22:50 UTC = 22 Nov 01:50 AST); Anadolu Agency, 22 Nov.
Tag: REPORTED.

### 19 — ANTALYA · CLIMATE (Europe)
**COP31 enters second day of overtime Sunday.**
(v2: replaces the Panama threat — Navarro's walkout threat was
delivered Friday 20 Nov, not Sunday.) The talks run into a second
day of overtime on Sunday, with the new package going to the
plenary for approval; walkout threats remain live. Source: AFP
wire, 22 Nov 2026 05:05 UTC. The dot marks Antalya, where the
talks are held.
Tag: CONFIRMED.

### 20 — PALMERSTON NORTH · CRICKET (Oceania)
**Central Districts win by 9 wickets.**
Central Districts beat Wellington by 9 wickets in the Plunket
Shield at Fitzherbert Park, Palmerston North, on day four:
Wellington 152 & 335, Central Districts 265 & 226/1 (target 223);
Curtis Heaphy 106 not out. Source: Cricbuzz live scorecard,
result 22 Nov 2026 14:09 local
(https://www.cricbuzz.com/live-cricket-scores/171320/cd-vs-wel-2nd-match-day-4-plunket-shield-2026-27).
Tag: CONFIRMED.

### 21 — MELBOURNE · FOOTBALL (Oceania)
**Glory go top after 0–0 draw.**
Perth Glory climb to the top of the A-League Women table after a
0–0 draw with Melbourne Victory at Lakeside Stadium on Sunday
afternoon — their fifth clean sheet in six games. Source: Perth
Glory, 22 Nov 2026
(https://perthglory.com.au/news/alw-match-report-glory-go-top-after-away-draw-with-victory/).
Tag: CONFIRMED.

### 22 — WHANGANUI · MOTORSPORT (Oceania)
**Driver killed in Whanganui hillclimb.**
One driver died and the co-driver was seriously hurt after their
car left the road at the Brunswick Road Hillclimb in Whanganui
just before midday on Sunday 22 Nov. MotorSport New Zealand says
it will cooperate with the investigation and run a full internal
review. Source: MotorSport New Zealand (official statement),
22 Nov 2026
(https://motorsport.org.nz/brunswick-road-hillclimb-statement/).
Tag: OFFICIAL.

### 23 — SYDNEY · CRICKET (Oceania)
**Smith returns at SCG after injury.**
Steve Smith returns for NSW against Queensland at the SCG on
Sunday, his first appearance since the second Test in South
Africa — he missed the decider with a neck injury. Source: CODE
Sports, 22 Nov 2026 02:51 UTC
(https://www.codesports.com.au/cricket/fans-flock-to-the-scg-as-steve-smith-makes-sheffield-shield-return/news-story/b29ec0d1fda03872c96abf88a0f95660).
Tag: CONFIRMED.

### 24 — VYSHHOROD · WAR (Europe)
**Drone hits Kyiv apartment block.**
A Russian drone strike overnight destroyed a five-storey
apartment block in Vyshhorod, Kyiv Oblast; fire gutted units on
all five floors, two people reported hurt including a child, and
rescuers were still checking for people trapped. Source: Kyiv
Independent via BytesEurope, published 22 Nov 2026 05:14 UTC
(https://www.byteseu.com/2537806/). Caveat: the strike was
overnight 21→22 Nov Kyiv time; the outlet itself dates it
"overnight on Nov. 22" and the fire and rescue are Sunday
morning's news. The page claims the strike as reported, not as a
daytime event.
Tag: REPORTED (official source: Kyiv Oblast military
administration head Tymur Tkachenko).

### 25 — CHRISTCHURCH · BUSINESS (Oceania)
**Farmlands chair Hewett resigns.**
Farmlands chair Rob Hewett resigns from the board, announced in
a statement on Sunday, after shareholders rejected a $1 million
investment in AgriZeroNZ; independent director Mark O'Donnell
becomes interim chair ahead of the AGM in Gore on Tuesday 24 Nov.
Source: Farmers Weekly NZ, 22 Nov 2026 15:24:59 +13:00
(https://www.farmersweekly.co.nz/news/farmlands-chair-rob-hewett-resigns-ahead-of-contentious-agm/).
Tag: CONFIRMED.

### 26 — OYO · DIPLOMACY (Africa)
**Ruto joins four-nation talks in Oyo.**
Kenya's President William Ruto arrives in Oyo, Republic of Congo,
for a four-nation meeting on Sunday with Presidents Denis
Sassou-N'Guesso (Congo), Félix Tshisekedi (DR Congo) and Faure
Gnassingbé (Togo), amid Kenya–DR Congo diplomatic tensions.
Source: People Daily, Sunday 22 Nov 2026 07:40
(https://peopledaily.digital/news/ruto-silently-jets-off-to-congo-for-a-high-level-four-nation-meeting).
Caveat: the meeting is Sunday's event; no outcome had been
reported at build time — the page claims attendance only, not an
agreement.
Tag: REPORTED.

### 27 — MELBOURNE · NBL (Oceania)
**Taipans edge Phoenix 95–92 in thriller.**
Jack McVeigh scored 24 points, including the match-sealing
three-pointer with 1:33 left, as Cairns Taipans beat South East
Melbourne Phoenix 95–92 at John Cain Arena on Sunday — their
fourth straight win. Source: AAP, 22 Nov 2026
(https://aapnews.aap.com.au/news/mcveigh-stars-as-taipans-edge-phoenix-in-nbl-thriller);
cross-checked against nbl.com.au per the brief. Precise coords
144.98183, -37.8229; gen.py uses the page's shared Melbourne
coords (144.96, -37.81) so the dot merges (badge "4").
Tag: REPORTED.

### 28 — WELLINGTON · NZ POLITIK (Oceania)
**Grigg takes leave after cancer diagnosis.**
PM Christopher Luxon announced that minister Nicola Grigg is
taking medical leave after a cancer diagnosis; she has had one
operation and is due a second in a fortnight before further
treatment, with a positive prognosis. Penny Simmonds takes her
Environment and Women portfolios in an acting capacity. Source:
Chris Lynch Media, Published 2026-11-22T01:37:55+00:00
(https://www.chrislynchmedia.com/news-items/selwyn-mp-nicola-grigg-takes-medical-leave-after-cancer-diagnosis/);
corroborated by NZ Herald 22 Nov per the brief. Precise coords
174.7756, -41.2866; gen.py uses the page's shared Wellington
coords (174.78, -41.29) so the dot merges (badge "3").
Tag: REPORTED.

### 29 — SEOUL · KOREA (Asia)
**Korea minister quits over AI exam cheating.**
President Lee Jae Myung accepted Education Minister Choi
Kyo-jin's resignation on Sunday after last-minute anti-cheating
measures against AI-assisted cheating ahead of the CSAT college
entrance exam triggered nationwide confusion. Source: Korea
JoongAng Daily, Published 2026-11-22T06:18:44Z
(https://www.koreajoongangdaily.com/korea/lee-accepts-education-ministers-resignation-after-csat-anticheating-measures-trigger-nationwide-confusion/12984387).
Tag: CONFIRMED.

## Stat boxes (6, all from the verified stories above)

- **35%** — electricity share of final energy by 2035, in the COP31 draft (AFP/CNA, 22 Nov).
- **352** — India's lead in Wellington, in runs (Reuters, 22 Nov).
- **25** — Bellamy's final Storm season, his 25th (AAP, 22 Nov).
- **36** — workers still missing after the Cikande factory fire, as of 03:56 UTC (Reuters, 22 Nov).
- **720/9** — India's record Test total in New Zealand (Reuters, 22 Nov).
- **1,671** — killed in Gaza since the ceasefire, as of 21 Nov
  (Gaza Health Ministry via QNA, 21 Nov 11:30 UTC; v2 corrects the
  stale v1 figure 1,661).

## BY THE CLOCK (verified times)

- GMT Sun 01:57 — China opposes the FCC ban (Reuters).
- GMT Sun 03:00 — COP31 objection deadline (Reuters).
- GMT Sun 03:56 — Reuters reports the Cikande fire search.
- GMT Sun 04:01 — Myanmar slams the ASEAN decision (Reuters).
- GMT Sun 05:05 — AFP on COP31 entering a second day of overtime.
- GMT Sun 06:00 — Cricinfo reports India 720/9 in Wellington.
(v2: dropped 00:00 COP31 draft — time unverified; 01:16 AFP —
time unverified; 01:42 AST Mecca intercept — story demoted.)

## DATE CHECK

Left out as other days' news: the APEC trilateral in Shenzhen
(Thu 19 Nov) · the Kyiv barrage (Fri 20 Nov) · Wall St's
correction (Fri 20 Nov) · the Denmark "assassination" plot
(Fri 20 Nov) · the Peru quake (Fri 20 Nov local) · the Abu Dhabi
meeting (Sat 21 Nov) · the Panama threat (Fri 20 Nov) · the
Bayelsa toll (Sat 21 Nov).
Not yet happened, so not shown: COP31 adoption — pending (the
approval session was under way at build time; re-check before
submitting). Every story here happened, or was first reported, on
Sunday 22 November 2026.

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

Dropped in the v2 verification (same date rule): the Abu Dhabi
meeting (event and first report Saturday 21 Nov) · the Panama
walkout threat (Navarro's threat was delivered Friday 20 Nov;
the 22 Nov AFP wire only repeats it as context) · the Nowa Dęba
exercise (closing date not verified to 22 Nov) · the Bayelsa
toll "rises to 24" (that figure was Saturday's update, not
Sunday's) · the Gaza flood story (the article was 8 Nov,
re-crawled 22 Nov) · the EU–Indonesia trade deal (Saturday) ·
the ICJ Myanmar case (19 Nov) · the Sparta II ship (Saturday) ·
the joint Gaza statement by 4 foreign ministers (15/16 Nov;
an aggregator wrongly stamped it 22 Nov) · Kryvyi Rih (dates
conflict across sources — Friday night vs Saturday vs
"overnight 21–22" — excluded as ambiguous).

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

## v3 build (22 Nov ~14:25 WIB) — 29 stories, slot 2

All v3 changes above. entry.png 210,534 bytes,
sha256 162561e1ccdf83d498ea9867f7f6099f68f91066b3d1565d3db52f326cc914a1.
Verification: gen.py rendered 3× with identical SHA and zero
warnings; every text element measured against its box (heroes ≤4
body lines, grid ≤3/3, ALSO exactly 1 line each, all three new
items inside the 292px column budget); 29 stories = masthead =
region bar = 23 map dots + 3 badges (Antalya "2", Wellington "3",
Melbourne "4"); main.py hash check passes from a /tmp copy
(output sha matches). Visual check of the full page plus 2× crops
of the heroes, the grid, the map, the NZ cluster and the ALSO
list: red ALSO circles clear, no overlap or truncation, tower
arcs no longer cross the kicker, DATE CHECK breaks cleanly on
the "·" separator. `makefun check --worktree` (no bundle):
4 passed, 1 failed (transcripts_present — expected, no bundle),
14 skipped, 5 checked at submission. Not submitted, not pushed.

## v2 build (22 Nov ~14:15 WIB) — 26 stories, slot 2

All v2 changes above. entry.png 202,582 bytes,
sha256 d1742c39757ec914650eb7d86e598fc32ca7d3d752cd11e821e1dd0c9db9fc77.
Verification: gen.py rendered 3× with identical SHA and no
warnings; every text element measured against its box (heroes ≤4
body lines, grid ≤3/3, ALSO exactly 1 line each); 26 stories =
masthead = region bar = 22 map dots + 3 badges; main.py hash
check passes from a /tmp copy. Visual check of the full page
plus 2× crops of the ALSO list, the map, the NZ cluster, the
heroes and the grid: red ALSO circles clear, no overlap or
truncation, DATE CHECK breaks cleanly on the "·" separator.

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
