#!/usr/bin/env python3
"""Entry point for news-image-20261122 (v1-fix2, slot 1).

Copies the pre-rendered entry.png (drawn by gen.py from the 21
stories verified in NOTES.md) to the grader's output directory and
verifies its SHA-256 first, so a corrupted or swapped image can
never be submitted silently. Standard library only — no Pillow,
no network, no drawing at run time.
"""
import hashlib
import os
import shutil
import sys
import tempfile

EXPECTED_SHA256 = "d0d47f648a3d1f024c4cce8a76b0a1dd3a353558493167618e2e4f08b0fc36b0"
EXPECTED_SIZE = 204437

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def output_dir():
    for cand in (os.environ.get("MAKEFUN_OUTPUT_DIR"), "/output",
                 "output", tempfile.gettempdir()):
        if cand:
            try:
                os.makedirs(cand, exist_ok=True)
                probe = os.path.join(cand, ".write-test")
                with open(probe, "w") as fh:
                    fh.write("ok")
                os.remove(probe)
                return cand
            except OSError:
                continue
    return tempfile.gettempdir()


def main():
    with open(SRC, "rb") as fh:
        data = fh.read()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"entry.png sha mismatch: {digest} != {EXPECTED_SHA256}",
              file=sys.stderr)
        return 1
    if len(data) != EXPECTED_SIZE:
        print(f"entry.png size mismatch: {len(data)} != {EXPECTED_SIZE}",
              file=sys.stderr)
        return 1
    out = output_dir()
    dest = os.path.join(out, "entry.png")
    shutil.copyfile(SRC, dest)
    print(f"wrote {dest} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
