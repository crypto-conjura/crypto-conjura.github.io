#!/bin/sh
# Compile one document that uses the shared AICR house classes.
#
# The classes live once in latex/cls/ rather than as a copy beside every
# document, so pdflatex has to be told where to find them. Pointing TEXINPUTS
# at that one directory is the whole job of this script, and the reason
# `cd <dir> && pdflatex main.tex` on its own no longer works.
#
#   scripts/build_paper.sh c/0001/latex             # builds main.tex
#   scripts/build_paper.sh c/0004/latex proof.tex   # builds a named file
#
# Runs pdflatex twice: these documents carry their own aicrbibliography
# environment rather than a .bib, so two passes settle refs and labels and no
# bibtex run is needed.
set -e
dir=${1:?usage: scripts/build_paper.sh <dir-with-main.tex> [texfile]}
tex=${2:-main.tex}
root=$(cd "$(dirname "$0")/.." && pwd)
cd "$dir"
for _ in 1 2; do
  TEXINPUTS="$root/latex/cls:" pdflatex -interaction=nonstopmode -halt-on-error "$tex" >/dev/null
done
echo "built $dir/$(basename "$tex" .tex).pdf"
