#!/usr/bin/env python3
"""Convert a YouTube auto-caption SRT file into readable plain text.

Merges caption fragments into lines and inserts a [HH:MM:SS] stream-time
marker at a fixed interval, so summaries can cite video timestamps.

Usage:
    uv run python scripts/srt_to_text.py "tmp/<file>.srt" > out.txt
    uv run python scripts/srt_to_text.py "tmp/<file>.srt" --start 00:20:00 --end 00:45:00
"""
import argparse
import re
import sys

CUE_RE = re.compile(
    r"(\d+)\s*\n(\d{2}:\d{2}:\d{2}),\d{3}\s*-->\s*(\d{2}:\d{2}:\d{2}),\d{3}\s*\n(.*?)(?=\n\n|\Z)",
    re.S,
)


def hms_to_sec(hms: str) -> int:
    h, m, s = (int(x) for x in hms.split(":"))
    return h * 3600 + m * 60 + s


def sec_to_hms(sec: int) -> str:
    return f"{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("srt_file")
    ap.add_argument("--start", default=None, help="only output cues at/after HH:MM:SS")
    ap.add_argument("--end", default=None, help="only output cues before HH:MM:SS")
    ap.add_argument(
        "--marker-interval",
        type=int,
        default=60,
        help="seconds between [HH:MM:SS] markers (default: 60)",
    )
    args = ap.parse_args()

    text = open(args.srt_file, encoding="utf-8").read()
    start = hms_to_sec(args.start) if args.start else 0
    end = hms_to_sec(args.end) if args.end else 10**9

    out: list[str] = []
    buf: list[str] = []
    next_marker = None
    for _, t0, _t1, body in CUE_RE.findall(text):
        sec = hms_to_sec(t0)
        if sec < start or sec >= end:
            continue
        if next_marker is None or sec >= next_marker:
            if buf:
                out.append(" ".join(buf))
                buf = []
            out.append(f"\n[{sec_to_hms(sec)}]")
            next_marker = sec - sec % args.marker_interval + args.marker_interval
        line = " ".join(body.split())
        if line:
            buf.append(line)
    if buf:
        out.append(" ".join(buf))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
