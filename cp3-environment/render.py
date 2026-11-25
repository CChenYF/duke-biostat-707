"""Render CP3 using the interpreter from its own locked Pixi environment."""
from pathlib import Path
import os
import subprocess
import sys


def main():
    project_root = Path(__file__).resolve().parent.parent
    environment = os.environ.copy()
    environment["QUARTO_PYTHON"] = sys.executable
    result = subprocess.run(
        ["quarto", "render", "checkpoint3.qmd", "--output-dir", "output", "--no-clean"],
        cwd=project_root,
        env=environment,
        check=False,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
