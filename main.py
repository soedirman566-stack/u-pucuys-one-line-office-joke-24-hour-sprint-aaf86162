"""Entry program for the make.fun bounty "One-Line Office Joke: 24-Hour Sprint".

Writes this repository's one-line office joke to ``entry.txt`` inside the
output directory (optional argv[1] override, default ``/output``). The joke
itself is the whole entry; this program only has to put it in the file.
"""

import os
import sys

JOKE = (
    "HR told us to bring our whole selves to work, so I brought the version "
    "of me that naps after lunch \u2014 now there\u2019s a disciplinary meeting, "
    "and both of me have to attend."
)


def main() -> None:
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(JOKE + "\n")


if __name__ == "__main__":
    main()
