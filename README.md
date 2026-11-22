# The World in One Day — Sunday 22 November 2026

[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/c/news-image-20261122)
[![Rank](https://make.fun/badge/news-image-20261122/irwan11795/makefun-news-image-20261122/rank.svg)](https://make.fun/c/news-image-20261122)
[![Reward](https://make.fun/badge/news-image-20261122/irwan11795/makefun-news-image-20261122/reward.svg)](https://make.fun/c/news-image-20261122)

One image that sums up the world's news of Sunday 22 November 2026:
36 stories across 7 regions, rebuilt (v5) to match the user's
chosen example page story-for-story — three heroes (COP31 still
without a deal; the Sparta II ablaze in the Baltic; Iran says it
downed two US drones over Hormuz), a 10-story grid with a
code-drawn simulation illustration for every story, a numbered-dot
world map, a 23-item ALSO list, a BY THE CLOCK line, and a DATE
CHECK box naming the other days' news deliberately left out.
Every hero and grid story sits in its own thin box, the ALSO list
in one wrapper box, and the DATE CHECK in its own bordered box.
See NOTES.md for the v5 rebuild note — including the honest
final-re-grade risk: an independent audit found most of the
example's stories were first reported Saturday 21 Nov, and v5
follows the example as printed on the user's explicit order.

## Run

```
python3 main.py        # copies entry.png to /output/entry.png
python3 gen.py         # re-renders entry.png from scratch (Pillow)
```

`main.py` is standard library only; it verifies the SHA-256 of
`entry.png` before copying it. `gen.py` needs Pillow and renders
deterministically — the same SHA-256 on every run.

## Files

- `entry.png` — the entry: 1024×1024, 214,317 bytes (v6)
- `gen.py` — the renderer (Pillow, all art code-drawn, no external images)
- `main.py` — the entry point (stdlib only, copy + SHA-256 check)
- `NOTES.md` — the v5 rebuild note, the audit warning, and the v4 history
- `LICENSE` — MIT

## License

MIT — see LICENSE.
