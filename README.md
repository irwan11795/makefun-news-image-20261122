# The World in One Day — Sunday 22 November 2026

[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/c/news-image-20261122)
[![Rank](https://make.fun/badge/news-image-20261122/irwan11795/makefun-news-image-20261122/rank.svg)](https://make.fun/c/news-image-20261122)
[![Reward](https://make.fun/badge/news-image-20261122/irwan11795/makefun-news-image-20261122/reward.svg)](https://make.fun/c/news-image-20261122)

One image that sums up the world's news of Sunday 22 November 2026:
21 stories across 6 regions, every one verified against a primary
source dated that day. Three heroes (COP31's Sunday text, adoption
pending; the Cikande factory fire; the Saudi coalition's missile
intercept),
a 10-story grid with a code-drawn simulation illustration for every
story, a numbered-dot world map, an ALSO list, a BY THE CLOCK line,
and a DATE CHECK box naming the other days' news deliberately left
out. See NOTES.md for the source and date verification of every
story — including the stories that were checked and dropped.

## Run

```
python3 main.py        # copies entry.png to /output/entry.png
python3 gen.py         # re-renders entry.png from scratch (Pillow)
```

`main.py` is standard library only; it verifies the SHA-256 of
`entry.png` before copying it. `gen.py` needs Pillow and renders
deterministically — the same SHA-256 on every run.

## Files

- `entry.png` — the entry: 1024×1024, 204,437 bytes
- `gen.py` — the renderer (Pillow, all art code-drawn, no external images)
- `main.py` — the entry point (stdlib only, copy + SHA-256 check)
- `NOTES.md` — every story, its primary source, and its date check
- `LICENSE` — MIT

## License

MIT — see LICENSE.
