#!/usr/bin/env bash
#
# Builds the site for Cloudflare Workers Builds.
#
# This exists because Cloudflare's build image has no Quarto, and `_site/` is
# gitignored -- so a clone of this repository contains .qmd sources and no HTML
# at all. Without this, `wrangler deploy` finds nothing to upload and fails with
# "Could not detect a directory containing static files".
#
# It is wired in as `build.command` in wrangler.jsonc rather than as a build
# command in the Cloudflare dashboard, so that the build lives in the repository
# and a deploy is reproducible from a checkout alone.
#
# The steps below mirror .github/workflows/publish.yml, which builds the same
# site for GitHub Pages. THE TWO MUST STAY IN STEP: when a gate is added there,
# add it here. Two of these steps are not checks but generators --
# build_index.py writes conjura.json and _generated/, both gitignored and both
# listed as Quarto `resources:` -- so skipping them does not error, it silently
# ships a site whose facet listings are empty.

set -euo pipefail

QUARTO_VERSION="1.10.18" # Pinned to match publish.yml's quarto-actions/setup.

# Python dependencies are deliberately NOT installed here. Cloudflare detects
# requirements.txt and runs `pip install -r requirements.txt` before the deploy
# command, exactly as publish.yml does before its gates, so installing again
# would be redundant there -- and doing it unconditionally breaks the local
# path, since `pip install` into a Homebrew-managed python fails outright with
# externally-managed-environment. Running this by hand wants a venv with
# requirements.txt in it; the gates below will say so plainly if there isn't one.

# Skip the ~80MB download when a developer running `wrangler deploy` locally
# already has Quarto. Version drift against the pin is the developer's problem;
# in the build image there is never a hit.
if ! command -v quarto >/dev/null 2>&1; then
  echo "--> Installing Quarto ${QUARTO_VERSION}"
  quarto_dir="${HOME}/.local/quarto-${QUARTO_VERSION}"
  mkdir -p "${quarto_dir}"
  curl -fsSL \
    "https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-amd64.tar.gz" \
    | tar -xz -C "${quarto_dir}" --strip-components=1
  export PATH="${quarto_dir}/bin:${PATH}"
fi
quarto --version

echo "--> Validating statement schema and badges"
python3 scripts/status_badge.py --check c papers

echo "--> Building facet index (conjura.json, _generated/)"
python3 scripts/build_index.py

echo "--> Checking relation graph consistency"
python3 scripts/check_relations.py

echo "--> Checking UC interface boxes against their LaTeX"
python3 scripts/gen_interface.py --check

echo "--> Checking artifacts match their LaTeX source"
python3 scripts/artifact_manifest.py --check

echo "--> Checking each UC entry says whether it has a definition"
python3 scripts/uc_status.py --check

# Report-only by design: an unpromoted draft is editorial backlog, not a broken
# build, and this runs before the render. It exits 1 only on a `draft:` link
# that contradicts the tree.
echo "--> Reporting conjecture drafts with no site page"
python3 scripts/draft_status.py --check

echo "--> Rendering site"
quarto render

# wrangler is about to upload whatever is in _site/. An empty or missing
# directory is the failure this whole script exists to prevent, and it is worth
# failing here -- with the render's output still on screen -- rather than in
# wrangler's assets sniffing, which reports it as if no build had run at all.
if [ ! -f _site/index.html ]; then
  echo "!! quarto render produced no _site/index.html; refusing to deploy" >&2
  exit 1
fi
echo "--> Built $(find _site -type f | wc -l | tr -d ' ') files into _site/"
