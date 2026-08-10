#!/usr/bin/env python3
"""Generate teacher "slideshow" versions of each notebook in NOTEBOOKS.

A teacher version is identical to the student notebook, but its marimo App
references a slides layout so the WASM export renders as a reveal.js-style
slideshow for presenting in class.

Crucially, the generated slides layout GROUPS each interactive control with the
output it drives (its live calculation and graph) onto the SAME slide, so the
sliders and graphs stay usable while presenting. It does this with per-cell
slide types:

    - "slide"    : the cell starts a new slide (markdown headings / questions)
    - "fragment" : the cell stays on the current slide, revealed on advance
                   (sliders, graphs, number inputs, feedback, accordions, prose)
    - "skip"     : the cell is hidden (the imports cell)

These teacher .py files and their layout JSONs are GENERATED from the student
sources, do not hand-edit them. Edit the relevant source/<name>.py, then re-run
this script (and ./build.sh) to regenerate.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "source"
LAYOUTS = SOURCE / "layouts"
NOTEBOOKS = ["momentum-part1", "momentum-part2", "momentum-part3", "momentum-part4", "suvat"]

# A cell starts a new slide when its markdown contains a heading (#..######)
# or a question marker (**Q1 ...**, **1. ...**, **Step ...**-free) at line start.
HEADING_RE = re.compile(r"\n\s*#{1,6}\s")
QUESTION_RE = re.compile(r"\*\*(?:Q\d|\d+\.)")


def split_cells(src: str) -> list[str]:
    """Return the source of each @app.cell block, in file order."""
    # Everything from one "@app.cell" up to the next (or the trailing __main__).
    parts = re.split(r"(?=^@app\.cell)", src, flags=re.MULTILINE)
    return [p for p in parts if p.lstrip().startswith("@app.cell")]


def classify(cell_src: str, is_first: bool) -> str:
    if is_first:
        return "skip"  # the imports cell
    if "mo.md(" in cell_src and (HEADING_RE.search(cell_src) or QUESTION_RE.search(cell_src)):
        return "slide"
    return "fragment"


def main() -> None:
    LAYOUTS.mkdir(parents=True, exist_ok=True)
    for name in NOTEBOOKS:
        src_path = SOURCE / f"{name}.py"
        if not src_path.exists():
            print(f"skip: {src_path} not found")
            continue
        src = src_path.read_text(encoding="utf-8")

        layout_name = f"{name}-teacher.slides.json"
        teacher_src = src.replace(
            'app = marimo.App(width="medium")',
            f'app = marimo.App(width="medium", layout_file="layouts/{layout_name}")',
        )
        (SOURCE / f"{name}-teacher.py").write_text(teacher_src, encoding="utf-8")

        cells = split_cells(src)
        types = [classify(c, i == 0) for i, c in enumerate(cells)]
        # Guarantee the deck opens on a real slide, not a fragment.
        for i, t in enumerate(types):
            if t == "slide":
                break
            if t == "fragment":
                types[i] = "slide"
                break

        layout = {
            "type": "slides",
            "data": {"cells": [{"type": t} for t in types], "deck": {}},
        }
        (LAYOUTS / layout_name).write_text(json.dumps(layout, indent=2) + "\n", encoding="utf-8")

        n_slides = types.count("slide")
        n_frag = types.count("fragment")
        print(f"{name}: {len(cells)} cells -> {n_slides} slides, {n_frag} fragments, 1 skipped")


if __name__ == "__main__":
    main()
