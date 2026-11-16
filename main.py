"""ai-excited-01 entry: copy the lion image to the output directory.

The program is deliberately trivial: the image is the entry. It copies
entry.png (the lion breaking out of its golden frame) next to this script
into the output directory, byte for byte, every run. No network, no
randomness, no timestamps in the output: two runs write identical bytes.
"""

import os
import shutil
import sys


SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, OUTPUT_NAME)
    shutil.copyfile(source, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
