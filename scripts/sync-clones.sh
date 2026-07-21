#!/usr/bin/env bash
# Shallow-clone or refresh Project Pythia cookbook repos as siblings of this one.
#
# Deep content review needs the notebooks locally; the audit itself never touches
# a clone. Clones land in the parent directory (../<name>), deliberately outside
# this repo.
#
#   ./scripts/sync-clones.sh radar-cookbook esgf-cookbook   # named repos
#   ./scripts/sync-clones.sh --gallery                      # every gallery cookbook
#
# Re-running is a fast-forward, never a clobber: a clone with local changes is
# reported and skipped.

set -euo pipefail

ORG=projectpythia
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PARENT="$(dirname "$ROOT")"
GALLERY_URL="https://raw.githubusercontent.com/$ORG/cookbook-gallery/main/cookbook_gallery.txt"

usage() {
    echo "usage: $(basename "$0") [--gallery | <repo-name>...]" >&2
    exit 1
}

[ $# -eq 0 ] && usage

if [ "$1" = "--gallery" ]; then
    mapfile -t repos < <(curl -fsSL "$GALLERY_URL" | grep -v '^[[:space:]]*$')
    echo "Syncing ${#repos[@]} gallery cookbooks into $PARENT"
else
    repos=("$@")
fi

for name in "${repos[@]}"; do
    target="$PARENT/$name"

    if [ ! -d "$target" ]; then
        echo "==> cloning $name"
        gh repo clone "$ORG/$name" "$target" -- --depth 1
        continue
    fi

    if [ -n "$(git -C "$target" status --porcelain)" ]; then
        echo "==> $name: local changes, skipping" >&2
        continue
    fi

    echo "==> updating $name"
    # Shallow clones need an explicit depth bump to fast-forward.
    git -C "$target" pull --ff-only --depth 1 || {
        echo "    could not fast-forward $name" >&2
    }
done
