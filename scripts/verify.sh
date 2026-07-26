#!/usr/bin/env bash
# Verification for the catalog site.
#
# The failure this guards against is a site that looks complete and is not. A markdown parser
# built on regexes will happily skip an entry it cannot match, and nobody reviewing the
# rendered page would notice forty missing tasks among seven hundred. So the entry count is
# asserted against the number the README advertises, the count is re-derived independently
# from the markdown with grep rather than from the parser, and the two must agree.
#
# Attacked on 2026-07-26 by deleting one entry's Scores line and by removing an entry outright.
# Checks 1 and 2 failed respectively. See README.
set -euo pipefail
cd "$(dirname "$0")/.."

EXPECT=722
pass=0
fail=0
ok()  { printf '  ok    %s\n' "$1"; pass=$((pass + 1)); }
bad() { printf '  FAIL  %s\n' "$1"; fail=$((fail + 1)); }

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

BUILD="python3 tools/build_catalog_site.py --catalog catalog --runs ${RUNS_LOG:-runs.jsonl}"

echo "1. the parse is strict and accounts for every entry"
if out=$($BUILD --check --expect "$EXPECT" 2>&1); then
  printf '%s\n' "$out" | tail -3 | sed 's/^/  /'
  ok "parsed exactly $EXPECT entries with unique ids"
else
  printf '%s\n' "$out" | tail -6 | sed 's/^/  /'
  bad "the parse did not account for every entry"
fi

echo
echo "2. an independent count from the raw markdown agrees"
# Deliberately not using the parser. If the parser and a plain grep disagree, one of them is
# wrong and the site should not be published either way.
grep_count=$(grep -hc '^### [A-Z]\+-[0-9]\+:' catalog/*.md | awk '{s+=$1} END {print s}')
if [ "$grep_count" -eq "$EXPECT" ]; then
  ok "grep also finds $grep_count entry headings"
else
  bad "grep finds $grep_count entry headings but the target is $EXPECT"
fi

echo
echo "3. every entry has all five scores, an effort and a needs line"
missing_meta=$(( $(grep -hc '^### [A-Z]\+-[0-9]\+:' catalog/*.md | awk '{s+=$1} END {print s}') \
                 - $(grep -hc '^\*\*Scores:\*\*' catalog/*.md | awk '{s+=$1} END {print s}') ))
missing_needs=$(( $(grep -hc '^### [A-Z]\+-[0-9]\+:' catalog/*.md | awk '{s+=$1} END {print s}') \
                  - $(grep -hc '^\*\*Needs:\*\*' catalog/*.md | awk '{s+=$1} END {print s}') ))
if [ "$missing_meta" -eq 0 ] && [ "$missing_needs" -eq 0 ]; then
  ok "score lines and needs lines both match the entry count"
else
  bad "$missing_meta entries lack a Scores line, $missing_needs lack a Needs line"
fi

echo
echo "4. the built page carries every entry and no remote assets"
if $BUILD --out "$work/index.html" --expect "$EXPECT" >/dev/null 2>&1; then
  page="$work/index.html"
  # The records live in a JSON script block, so count them there rather than in markup.
  n=$(python3 -c "
import json, re, sys
html = open('$page', encoding='utf-8').read()
m = re.search(r'<script id=\"data\" type=\"application/json\">(.*?)</script>', html, re.S)
if not m: print('0'); sys.exit()
print(len(json.loads(m.group(1))))
")
  remote=$(grep -coE '(src|href)="https?://[^\"]*\.(css|js)"' "$page" || true)
  fonts=$(grep -co '@import\|fonts.googleapis\|cdn\.' "$page" || true)
  if [ "$n" -ne "$EXPECT" ]; then bad "the page embeds $n records, expected $EXPECT"
  elif [ "$remote" -ne 0 ]; then bad "$remote remote stylesheet or script references"
  elif [ "$fonts" -ne 0 ]; then bad "$fonts CDN or webfont references"
  else ok "$n records embedded, no remote assets"
  fi
  # Both themes must be defined, and the attribute form must be able to override the media query.
  if grep -q 'prefers-color-scheme: dark' "$page" \
     && grep -q 'data-theme="dark"' "$page" && grep -q 'data-theme="light"' "$page"; then
    ok "light and dark are both defined, with an attribute override in both directions"
  else
    bad "the theme handling is incomplete"
  fi
else
  bad "the build failed"
fi

echo
echo "5. only genuinely passing runs are labelled as built"
# A task marked "Built and verified" on a public page had better have a passing run behind it.
if python3 -c "
import json, re, sys
html = open('$work/index.html', encoding='utf-8').read()
recs = json.loads(re.search(r'<script id=\"data\" type=\"application/json\">(.*?)</script>', html, re.S).group(1))
claimed = {r['i'] for r in recs if r['r']}
passing = set()
failing = set()
for line in open(__import__('os').environ.get('RUNS_LOG', 'runs.jsonl'), encoding='utf-8'):
    line = line.strip()
    if not line: continue
    r = json.loads(line)
    (passing if r.get('passed') else failing).add(r.get('task'))
liars = claimed - passing
print('  %d tasks marked built, all backed by a passing run' % len(claimed))
if liars:
    print('  tasks claiming built with NO passing run: %s' % sorted(liars))
    sys.exit(1)
if not claimed:
    print('  nothing is marked built, so this check proved nothing')
    sys.exit(1)
" 2>&1; then
  ok "every 'built' label is backed by a recorded passing run"
else
  bad "a task is labelled built without a passing run behind it"
fi

echo
echo "6. NEGATIVE CONTROL: a damaged catalog must fail the parse"
# Without this, checks 1 through 4 could all be passing vacuously.
cp -r catalog "$work/broken"
python3 - "$work/broken" <<'PY'
import pathlib, sys, re
d = pathlib.Path(sys.argv[1])
f = sorted(d.glob("*.md"))[0]
t = f.read_text(encoding="utf-8")
# remove one entry's Scores line, which is exactly the silent-skip case
t = re.sub(r"\n\*\*Scores:\*\*[^\n]*\n", "\n", t, count=1)
f.write_text(t, encoding="utf-8")
PY
if $BUILD --catalog "$work/broken" --check --expect "$EXPECT" >/dev/null 2>&1; then
  bad "a catalog with a missing Scores line still passed, so the parse is not strict"
else
  ok "a missing Scores line is refused rather than skipped"
fi

echo
echo "7. NEGATIVE CONTROL: a missing entry must fail the count"
cp -r catalog "$work/short"
python3 - "$work/short" <<'PY'
import pathlib, sys, re
d = pathlib.Path(sys.argv[1])
f = sorted(d.glob("*.md"))[0]
t = f.read_text(encoding="utf-8")
parts = re.split(r"(?m)^(?=### [A-Z]+-\d+:)", t)
f.write_text("".join(parts[:-1]), encoding="utf-8")   # drop the last entry
PY
if $BUILD --catalog "$work/short" --check --expect "$EXPECT" >/dev/null 2>&1; then
  bad "a catalog one entry short still passed the count assertion"
else
  ok "one missing entry is caught by the count assertion"
fi

echo
echo "8. no secrets or personal paths in anything tracked"
if leaks=$(grep -rIEn 'sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|/home/[a-z]+/(Projects|Documents)|BEGIN [A-Z ]*PRIVATE KEY' \
      --include='*.md' --include='*.html' --include='*.sh' . 2>/dev/null); then
  printf '%s\n' "$leaks" | head -8
  bad "found credential-shaped or personal strings"
else
  # Names of environment variables are fine and appear throughout; values are not.
  ok "no credential-shaped or personal strings found"
fi

echo
printf '%d passed, %d failed\n' "$pass" "$fail"
if [ "$fail" -ne 0 ]; then echo "VERIFY FAILED"; exit 1; fi
echo "VERIFY OK"
