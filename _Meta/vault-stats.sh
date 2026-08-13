#!/bin/bash
# Appends a dated row to _Meta/Vault Stats.md
# Run monthly, during the monthly review.
set -e
V="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$V/_Meta/Vault Stats.md"

count_md()   { find "$V" -name '.obsidian' -prune -o -type f -name '*.md' -print | wc -l | tr -d ' '; }
count_in()   { find "$V/$1" -type f -name '*.md' 2>/dev/null | wc -l | tr -d ' '; }
count_links(){ grep -roh '\[\[[^]]*\]\]' --include='*.md' "$V" 2>/dev/null | wc -l | tr -d ' '; }

TOTAL=$(count_md)
NOTES=$(count_in "02 Notes")
PROJ=$(count_in "04 Projects")
LINKS=$(count_links)
RATIO=$(awk -v l="$LINKS" -v t="$TOTAL" 'BEGIN{ if (t>0) printf "%.1f", l/t; else print "0" }')
WORDS=$(find "$V" -name '.obsidian' -prune -o -type f -name '*.md' -exec cat {} + | wc -w | tr -d ' ')
DATE=$(date +%Y-%m-%d)

if [ ! -f "$OUT" ]; then
  cat > "$OUT" <<'HEADER'
---
type: meta
tags:
  - meta
---

# Vault Stats

One row per month, appended by `_Meta/vault-stats.sh`.

**Links per note is the number that matters.** Notes climbing while that stays flat means capture without thinking. See [[How this brain grows]].

| Date | Notes | Permanent | Projects | Links | Links per note | Words |
|---|---|---|---|---|---|---|
HEADER
fi

printf '| %s | %s | %s | %s | %s | %s | %s |\n' \
  "$DATE" "$TOTAL" "$NOTES" "$PROJ" "$LINKS" "$RATIO" "$WORDS" >> "$OUT"

echo "Added row: $DATE  notes=$TOTAL  links=$LINKS  ratio=$RATIO"
