#!/usr/bin/env bash
# Generate teacher "slideshow" versions of each momentum notebook.
#
# Thin wrapper around make-teacher-versions.py, which generates the teacher .py
# files and a slides layout that groups each interactive control with its graph
# onto the same slide (so sliders/graphs stay usable while presenting).
#
# The generated *-teacher.py files and layouts/*.slides.json are GENERATED from
# the student sources, do not hand-edit them. Edit source/momentum-part<N>.py,
# then re-run this script (and ./build.sh) to regenerate.
set -euo pipefail
cd "$(dirname "$0")"
exec python3 make-teacher-versions.py
