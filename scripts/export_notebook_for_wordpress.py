#!/usr/bin/env python3
"""Export a Jupyter notebook as HTML ready for a WordPress Custom HTML block.

The notebook is not executed. Existing cell outputs, including embedded images,
are used as stored in the .ipynb file.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import nbformat
    from nbconvert import HTMLExporter
except ImportError as error:
    raise SystemExit(
        "Missing dependency. Install nbconvert and nbformat, for example with "
        "`python -m pip install nbconvert nbformat`."
    ) from error


MAIN_PATTERN = re.compile(r"<main(?:\s[^>]*)?>(.*?)</main>", re.IGNORECASE | re.DOTALL)
STYLE_PATTERN = re.compile(r"<style(?:\s[^>]*)?>.*?</style>", re.IGNORECASE | re.DOTALL)
SCRIPT_PATTERN = re.compile(r"<script(?:\s[^>]*)?>.*?</script>", re.IGNORECASE | re.DOTALL)
OUTPUT_DIRECTORY = Path(__file__).resolve().parent / "html_output"


def default_output_path(notebook_path: Path) -> Path:
    """Return scripts/html_output/<notebook-name>.wordpress.html."""
    return OUTPUT_DIRECTORY / f"{notebook_path.stem}.wordpress.html"


def export_fragment(notebook_path: Path) -> str:
    """Render a notebook and return only its WordPress-safe notebook fragment."""
    with notebook_path.open(encoding="utf-8") as notebook_file:
        notebook = nbformat.read(notebook_file, as_version=4)

    exporter = HTMLExporter(template_name="lab")
    rendered_html, _resources = exporter.from_notebook_node(notebook)

    main = MAIN_PATTERN.search(rendered_html)
    if main is None:
        raise RuntimeError(
            "nbconvert output did not contain a <main> element; "
            "the installed template may be incompatible with this exporter."
        )

    cells = main.group(1).strip()

    # Pandas may place repeated scoped styles in individual DataFrame outputs.
    # WordPress uses the shared notebook CSS instead. Scripts are also removed
    # because WordPress normally rejects them and this export is static.
    cells = STYLE_PATTERN.sub("", cells)
    cells = SCRIPT_PATTERN.sub("", cells)

    return f'<div class="jp-Notebook">\n{cells}\n</div>\n'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Convert a saved Jupyter notebook to an HTML fragment that can be "
            "pasted into a WordPress Custom HTML block."
        )
    )
    parser.add_argument("notebook", type=Path, help="path to the .ipynb file")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help=(
            "output path (default: "
            "scripts/html_output/<notebook-name>.wordpress.html)"
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    notebook_path = args.notebook.expanduser().resolve()

    if not notebook_path.is_file():
        print(f"Notebook does not exist: {notebook_path}", file=sys.stderr)
        return 2
    if notebook_path.suffix.lower() != ".ipynb":
        print(f"Expected an .ipynb file: {notebook_path}", file=sys.stderr)
        return 2

    output_path = (
        args.output.expanduser().resolve()
        if args.output
        else default_output_path(notebook_path)
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        fragment = export_fragment(notebook_path)
    except Exception as error:
        print(f"Export failed: {error}", file=sys.stderr)
        return 1

    output_path.write_text(fragment, encoding="utf-8")
    print(f"Created WordPress HTML fragment: {output_path}")
    print("Paste its complete contents into a WordPress Custom HTML block.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
