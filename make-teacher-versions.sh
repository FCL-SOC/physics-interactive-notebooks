#!/usr/bin/env bash
# Generate teacher "slideshow" versions of each momentum notebook.
#
# A teacher version is identical to the student notebook, but its marimo App
# references a slides layout, so the WASM export renders as a reveal.js-style
# slideshow for presenting in class.
#
# These teacher .py files and their layout JSONs are GENERATED from the student
# sources — do not hand-edit them. Edit source/momentum-part<N>.py, then re-run
# this script (and ./build.sh) to regenerate.
set -euo pipefail
cd "$(dirname "$0")"

mkdir -p source/layouts

for n in 1 2 3 4; do
    src="source/momentum-part${n}.py"
    dst="source/momentum-part${n}-teacher.py"
    layout_name="momentum-part${n}-teacher.slides.json"
    [ -f "$src" ] || { echo "skip: $src not found"; continue; }

    # Slides layout: each cell becomes a slide. Empty data = default ordering.
    printf '{\n  "type": "slides",\n  "data": {}\n}\n' > "source/layouts/${layout_name}"

    # Point the App at the slides layout; everything else is copied verbatim.
    sed "s#app = marimo.App(width=\"medium\")#app = marimo.App(width=\"medium\", layout_file=\"layouts/${layout_name}\")#" \
        "$src" > "$dst"

    echo "generated: $dst  (+ layouts/${layout_name})"
done
