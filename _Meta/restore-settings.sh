#!/bin/bash
# Re-applies the Brain vault settings.
# Run this only if Obsidian reverted them (no custom theme, wrong folders).
# Quit Obsidian completely first, then run it, then reopen Obsidian.
set -e
V="$HOME/Desktop/Claude/Claude/.obsidian"
if pgrep -x Obsidian >/dev/null; then
  echo "Obsidian is still running. Quit it with Cmd+Q first, then run this again."
  exit 1
fi
cp "$V/.brain-backup/"*.json "$V/"
echo "Settings restored. Open Obsidian."
