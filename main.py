"""Copy entry.png next to this script into the output directory."""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    # copyfile preserves the image bytes exactly, with no re-encoding.
    shutil.copyfile(source, output_dir / "entry.png")


if __name__ == "__main__":
    main()
