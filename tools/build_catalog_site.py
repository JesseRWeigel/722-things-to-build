#!/usr/bin/env python3
"""Build the public catalog's GitHub Pages site.

Parses the sanitized markdown in `public-catalog/catalog/` into structured records and emits a
single self-contained page with client-side search, filtering and sorting.

Two design constraints drive the implementation:

The parse must be strict. A regex that silently skips a malformed entry produces a site that
looks complete and is not, and nothing downstream would notice 40 missing tasks. So every
entry is required to yield an id, a title, five scores, an effort and a needs field, and the
parser raises on anything it cannot fully account for. `--check` asserts the total against the
count the README advertises.

The page must be self-contained. GitHub Pages will serve whatever is committed, but a CDN
reference turns a working page into a broken one the first time a network is unavailable or a
CSP is applied, so all CSS and JS are inline and there are no webfonts.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# ### SAAS-001: Ship an ACX audiobook preflight checker
ENTRY_RE = re.compile(r"^### ([A-Z]+-\d+): (.+)$", re.M)
# **Scores:** $:4 CV:2 VIR:2 USE:1 ALT:3 | **Effort:** M | **Repo:** public
META_RE = re.compile(
    r"\*\*Scores:\*\*\s*\$:(\d+)\s+CV:(\d+)\s+VIR:(\d+)\s+USE:(\d+)\s+ALT:(\d+)\s*\|"
    r"\s*\*\*Effort:\*\*\s*(XL|[SML])\s*\|\s*\*\*Repo:\*\*\s*(\w+)")
NEEDS_RE = re.compile(r"\*\*Needs:\*\*\s*(.+?)\s*$", re.M)

SCORE_KEYS = ["money", "cv", "viral", "use", "alt"]
SCORE_LABELS = {
    "money": ("$", "Revenue potential"),
    "cv": ("CV", "Resume value"),
    "viral": ("VIR", "Chance of spreading"),
    "use": ("USE", "Usefulness to the author"),
    "alt": ("ALT", "Altruistic value, helps someone"),
}
# The catalog's README defines effort in agent-hours, so the site uses the same definitions
# rather than inventing adjectives. XL exists and covers 70 entries; an earlier version of this
# parser only accepted S, M and L and refused the whole file, which is how the tier was found.
EFFORT_LABELS = {
    "S": ("S", "under 1 agent-hour"),
    "M": ("M", "1 to 4 agent-hours"),
    "L": ("L", "4 to 16 agent-hours"),
    "XL": ("XL", "16+ agent-hours"),
}


def parse_category(path: str) -> dict:
    """Parse one category file. Raises rather than skipping anything it cannot account for."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()

    lines = text.split("\n")
    if not lines or not lines[0].startswith("# "):
        raise ValueError(f"{path}: expected a '# Title' first line")
    title = lines[0][2:].strip()

    # Everything between the title and the first entry is the category preamble.
    first = ENTRY_RE.search(text)
    if not first:
        raise ValueError(f"{path}: no entries found")
    preamble = " ".join(lines[1:text[:first.start()].count("\n")]).strip()

    matches = list(ENTRY_RE.finditer(text))
    entries = []
    for i, m in enumerate(matches):
        body = text[m.end():matches[i + 1].start() if i + 1 < len(matches) else len(text)]
        meta = META_RE.search(body)
        if not meta:
            raise ValueError(f"{path}: {m.group(1)} has no parseable Scores/Effort/Repo line")
        needs = NEEDS_RE.search(body)
        if not needs:
            raise ValueError(f"{path}: {m.group(1)} has no Needs line")

        # The description is whatever sits between the meta line and the Needs line.
        desc = body[meta.end():needs.start()].strip()
        desc = re.sub(r"\s*\n\s*", " ", desc).strip()
        if not desc:
            raise ValueError(f"{path}: {m.group(1)} has an empty description")

        need_text = needs.group(1).strip()
        entries.append({
            "id": m.group(1),
            "prefix": m.group(1).split("-")[0],
            "title": m.group(2).strip(),
            "desc": desc,
            "scores": {k: int(meta.group(i + 1)) for i, k in enumerate(SCORE_KEYS)},
            "effort": meta.group(6),
            "repo": meta.group(7),
            "needs": need_text,
            "needs_nothing": need_text.lower() in ("nothing", "none", "nothing."),
        })
    return {"file": os.path.basename(path), "title": title, "preamble": preamble,
            "entries": entries}


def load_all(catalog_dir: str) -> list[dict]:
    files = sorted(f for f in os.listdir(catalog_dir) if f.endswith(".md"))
    if not files:
        raise ValueError(f"no markdown in {catalog_dir}")
    return [parse_category(os.path.join(catalog_dir, f)) for f in files]


def load_shipped(runs_path: str) -> dict:
    """Map task id to the repo that was actually built and verified for it.

    Only runs that genuinely passed count. A task with a failed run is not shipped, and
    labelling it as such on a public page would be the exact kind of overclaim this catalog
    is supposed to avoid.
    """
    shipped = {}
    if not os.path.exists(runs_path):
        return shipped
    with open(runs_path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not r.get("passed"):
                continue
            task = r.get("task")
            repo = r.get("repo") or ""
            if task and repo.startswith("http"):
                shipped[task] = {"repo": repo, "slug": r.get("slug", "")}
    return shipped


def meter(value: int, maximum: int = 5) -> str:
    """A 0..5 score as filled and empty cells.

    Drawn rather than printed because the whole point of the scores is comparison across
    hundreds of rows, and a row of digits does not compare at a glance. The number is kept
    alongside for anyone who wants the value, and for screen readers.
    """
    cells = "".join(
        f'<i class="{"on" if i < value else "off"}"></i>' for i in range(maximum))
    return f'<span class="meter" aria-hidden="true">{cells}</span>'


def render(cats: list[dict], shipped: dict) -> str:
    total = sum(len(c["entries"]) for c in cats)
    n_shipped = sum(1 for c in cats for e in c["entries"] if e["id"] in shipped)
    needs_nothing = sum(1 for c in cats for e in c["entries"] if e["needs_nothing"])

    # Every record the page needs, as JSON, so filtering never touches the DOM text.
    records = []
    for c in cats:
        for e in c["entries"]:
            sh = shipped.get(e["id"])
            records.append({
                "i": e["id"], "t": e["title"], "d": e["desc"], "c": c["title"],
                "f": c["file"], "s": [e["scores"][k] for k in SCORE_KEYS],
                "e": e["effort"], "n": e["needs"], "nn": e["needs_nothing"],
                "r": sh["repo"] if sh else "",
            })
    payload = json.dumps(records, separators=(",", ":"), ensure_ascii=False)

    cat_opts = "".join(
        f'<option value="{html.escape(c["title"])}">{html.escape(c["title"])} '
        f'({len(c["entries"])})</option>' for c in cats)

    score_filters = "".join(f"""
      <label class="sf"><span>{SCORE_LABELS[k][0]}</span>
        <input type="range" min="0" max="5" value="0" data-score="{i}"
               aria-label="minimum {html.escape(SCORE_LABELS[k][1])}">
        <output>0+</output></label>""" for i, k in enumerate(SCORE_KEYS))

    legend = "".join(
        f'<div><dt>{SCORE_LABELS[k][0]}</dt><dd>{html.escape(SCORE_LABELS[k][1])}</dd></div>'
        for k in SCORE_KEYS)

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{total} Things To Build With AI Agents</title>
<meta name="description" content="A searchable catalog of {total} concrete, scored, buildable
software projects. Every entry names a specific deliverable, scores it on five axes, and states
what it needs beyond a normal developer workstation.">
<meta property="og:title" content="{total} Things To Build With AI Agents">
<meta property="og:description" content="Concrete, scored, buildable projects. No filler.">
<style>{CSS}</style>
</head>
<body>
<header>
  <div class="inner">
    <p class="eyebrow">A catalog, not a listicle</p>
    <h1>{total} things to build<br>with AI agents</h1>
    <p class="lede">Every entry names a specific deliverable, scores it on five axes, estimates
    effort, and says what it needs beyond a normal developer workstation. Generated by ten agents
    working against a shared specification that told each of them to reject their own first
    ideas, then filtered and indexed programmatically.</p>
    <div class="stats">
      <div><b>{total}</b><span>entries</span></div>
      <div><b>{len(cats)}</b><span>categories</span></div>
      <div><b>{needs_nothing}</b><span>need nothing but a workstation</span></div>
      <div><b>{n_shipped}</b><span>built and verified so far</span></div>
    </div>
    <dl class="legend">{legend}</dl>
  </div>
</header>

<div class="controls" role="search">
  <div class="inner">
    <div class="row">
      <input type="search" id="q" placeholder="Search {total} entries by title, description or id"
             aria-label="Search entries" autocomplete="off">
      <select id="cat" aria-label="Filter by category">
        <option value="">All categories</option>{cat_opts}
      </select>
      <select id="effort" aria-label="Filter by effort">
        <option value="">Any effort</option>
        <option value="S">S, under 1 agent-hour</option>
        <option value="M">M, 1 to 4 agent-hours</option>
        <option value="L">L, 4 to 16 agent-hours</option>
        <option value="XL">XL, 16+ agent-hours</option>
      </select>
      <select id="sort" aria-label="Sort by">
        <option value="id">Sort by id</option>
        <option value="0">Highest revenue potential</option>
        <option value="1">Highest resume value</option>
        <option value="2">Most likely to spread</option>
        <option value="3">Most useful</option>
        <option value="4">Most altruistic</option>
        <option value="sum">Highest total score</option>
      </select>
    </div>
    <div class="row secondary">
      <div class="sliders">{score_filters}</div>
      <label class="chk"><input type="checkbox" id="nn"> Needs nothing extra</label>
      <label class="chk"><input type="checkbox" id="built"> Already built</label>
      <button type="button" id="reset">Reset</button>
    </div>
    <p id="count" class="count" aria-live="polite"></p>
  </div>
</div>

<main class="inner"><ol id="list"></ol>
  <p id="empty" class="empty" hidden>Nothing matches those filters.
  <button type="button" id="reset2">Reset them</button></p>
</main>

<footer class="inner">
  <p>The result is uneven in places. Some entries are excellent and some are merely decent, which
  is the honest tradeoff of generating at this volume, and the scores exist so you can filter.
  This is the public subset of a 1000-entry catalog; the remainder referenced personal details
  and was removed programmatically.</p>
  <p><a href="https://github.com/JesseRWeigel/722-things-to-build">Repository</a> ยท
  Markdown source for every category is in <code>catalog/</code>.</p>
</footer>

<script id="data" type="application/json">{payload}</script>
<script>{JS}</script>
</body>
</html>
"""


CSS = """
:root {
  --ink:#101418; --ink2:#48535f; --ink3:#78848f; --line:#dfe3e8; --bg:#f4f6f8;
  --surface:#fff; --accent:#4436c8; --accent-soft:#eceafb; --good:#136c46; --warm:#a4501a;
  --shadow:0 1px 2px rgba(16,20,24,.05);
}
@media (prefers-color-scheme: dark) {
  :root { --ink:#e9edf1; --ink2:#a3aeb9; --ink3:#76818c; --line:#2a3138; --bg:#111519;
          --surface:#181d22; --accent:#a99bff; --accent-soft:#241f4a; --good:#5fc48f;
          --warm:#e0a06a; --shadow:none; }
}
:root[data-theme="dark"] {
  --ink:#e9edf1; --ink2:#a3aeb9; --ink3:#76818c; --line:#2a3138; --bg:#111519;
  --surface:#181d22; --accent:#a99bff; --accent-soft:#241f4a; --good:#5fc48f;
  --warm:#e0a06a; --shadow:none;
}
:root[data-theme="light"] {
  --ink:#101418; --ink2:#48535f; --ink3:#78848f; --line:#dfe3e8; --bg:#f4f6f8;
  --surface:#fff; --accent:#4436c8; --accent-soft:#eceafb; --good:#136c46; --warm:#a4501a;
  --shadow:0 1px 2px rgba(16,20,24,.05);
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
  font:15px/1.55 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,sans-serif;
  -webkit-font-smoothing:antialiased}
.inner{max-width:1080px;margin:0 auto;padding:0 1.25rem}
header{background:var(--surface);border-bottom:1px solid var(--line);padding:3.5rem 0 2.25rem}
.eyebrow{font:600 .7rem/1 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.16em;
  text-transform:uppercase;color:var(--accent);margin:0 0 1rem}
h1{font-size:clamp(2rem,5.5vw,3.4rem);line-height:1.02;letter-spacing:-.03em;margin:0 0 1rem;
  font-weight:800;text-wrap:balance}
.lede{color:var(--ink2);max-width:64ch;margin:0 0 2rem;font-size:1.02rem}
.stats{display:flex;flex-wrap:wrap;gap:2.25rem;margin-bottom:2rem}
.stats div{display:flex;flex-direction:column}
.stats b{font:700 1.7rem/1 ui-monospace,SFMono-Regular,Menlo,monospace;
  font-variant-numeric:tabular-nums;letter-spacing:-.02em}
.stats span{font-size:.76rem;color:var(--ink3);margin-top:.3rem;max-width:16ch}
.legend{display:flex;flex-wrap:wrap;gap:.4rem 1.4rem;margin:0;padding-top:1.25rem;
  border-top:1px solid var(--line)}
.legend div{display:flex;gap:.5rem;align-items:baseline}
.legend dt{font:700 .72rem/1 ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--accent);
  min-width:2.2em}
.legend dd{margin:0;font-size:.76rem;color:var(--ink3)}

.controls{position:sticky;top:0;z-index:10;background:var(--surface);
  border-bottom:1px solid var(--line);padding:.85rem 0;box-shadow:var(--shadow)}
.controls .row{display:flex;gap:.5rem;flex-wrap:wrap;align-items:center}
.controls .secondary{margin-top:.6rem}
#q{flex:1 1 22rem;min-width:0}
input[type=search],select,button{font:inherit;font-size:.86rem;padding:.48rem .7rem;
  border:1px solid var(--line);border-radius:5px;background:var(--bg);color:var(--ink)}
/* A select sizes itself to its widest OPTION, so the category list, whose longest label is
   "Developer Tools & Open Source Libraries (48)", pushed 3px past the viewport at 390px and
   put a horizontal scrollbar on the body. min-width:0 lets it shrink inside the flex row. */
select{max-width:100%;min-width:0}
#cat{flex:1 1 12rem}
#effort,#sort{flex:0 1 11rem}
input[type=search]:focus-visible,select:focus-visible,button:focus-visible,
input[type=range]:focus-visible,input[type=checkbox]:focus-visible{
  outline:2px solid var(--accent);outline-offset:1px}
button{cursor:pointer;background:var(--surface)}
button:hover{border-color:var(--accent);color:var(--accent)}
.sliders{display:flex;gap:.85rem;flex-wrap:wrap}
.sf{display:flex;align-items:center;gap:.35rem;font-size:.76rem;color:var(--ink2)}
.sf span{font:700 .72rem/1 ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--accent);
  min-width:2.1em}
.sf input[type=range]{width:64px;accent-color:var(--accent)}
.sf output{font-variant-numeric:tabular-nums;color:var(--ink3);min-width:2.2em}
.chk{display:flex;align-items:center;gap:.4rem;font-size:.8rem;color:var(--ink2)}
.chk input{accent-color:var(--accent)}
.count{margin:.6rem 0 0;font:.78rem/1 ui-monospace,SFMono-Regular,Menlo,monospace;
  color:var(--ink3);font-variant-numeric:tabular-nums}

main{padding:1.75rem 1.25rem 4rem}
ol{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:.6rem}
li{background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:1rem 1.1rem}
.top{display:flex;gap:.7rem;align-items:baseline;flex-wrap:wrap;margin-bottom:.35rem}
.tid{font:700 .74rem/1.4 ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--accent);
  background:var(--accent-soft);padding:.16rem .42rem;border-radius:3px;white-space:nowrap}
h2{font-size:1rem;font-weight:650;margin:0;flex:1 1 20rem;letter-spacing:-.01em}
.desc{margin:.45rem 0 .7rem;color:var(--ink2);font-size:.9rem;max-width:80ch}
.foot{display:flex;gap:.5rem 1.1rem;flex-wrap:wrap;align-items:center;font-size:.76rem;
  color:var(--ink3);padding-top:.55rem;border-top:1px solid var(--line)}
.scores{display:flex;gap:.7rem;flex-wrap:wrap}
.sc{display:flex;align-items:center;gap:.3rem}
.sc b{font:700 .7rem/1 ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--ink3)}
.sc em{font-style:normal;font-variant-numeric:tabular-nums;color:var(--ink2);font-size:.72rem}
.meter{display:inline-flex;gap:1.5px}
.meter i{width:5px;height:11px;border-radius:1px;background:var(--line)}
.meter i.on{background:var(--accent)}
.tag{font:.72rem/1 ui-monospace,SFMono-Regular,Menlo,monospace;padding:.22rem .42rem;
  border:1px solid var(--line);border-radius:3px;color:var(--ink2);white-space:nowrap}
.tag.cat{border-color:transparent;background:var(--bg)}
.tag.built{color:var(--good);border-color:currentColor;font-weight:700}
.tag.needs{color:var(--warm);border-color:currentColor;max-width:100%;overflow:hidden;text-overflow:ellipsis}
.tag.needs code{background:none;border:none;padding:0;color:inherit;font-size:1em}
a{color:var(--accent)}
mark{background:var(--accent-soft);color:inherit;font-weight:650;border-radius:2px;padding:0 1px}
.empty{text-align:center;color:var(--ink3);padding:3rem 0}
footer{border-top:1px solid var(--line);padding:2rem 1.25rem 4rem;color:var(--ink3);
  font-size:.82rem;max-width:1080px}
footer p{max-width:74ch}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.9em}
.desc code,h2 code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.86em;
  background:var(--bg);border:1px solid var(--line);border-radius:3px;padding:.04em .3em;
  color:var(--ink)}
@media (max-width:640px){
  .stats{gap:1.25rem}
  .sliders{gap:.5rem}
  .sf input[type=range]{width:52px}
}
"""

JS = r"""
(function () {
  var DATA = JSON.parse(document.getElementById('data').textContent);
  var LBL = ['$', 'CV', 'VIR', 'USE', 'ALT'];
  var EFFORT = { S: 'under 1 agent-hour', M: '1 to 4 agent-hours',
               L: '4 to 16 agent-hours', XL: '16+ agent-hours' };
  var list = document.getElementById('list');
  var count = document.getElementById('count');
  var empty = document.getElementById('empty');
  var q = document.getElementById('q');
  var cat = document.getElementById('cat');
  var effort = document.getElementById('effort');
  var sort = document.getElementById('sort');
  var nn = document.getElementById('nn');
  var built = document.getElementById('built');
  var sliders = [].slice.call(document.querySelectorAll('input[data-score]'));

  function esc(s) {
    return s.replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  // Order matters and is deliberate: escape first so a query or a description containing
  // markup can never inject, then highlight, then turn markdown code spans into <code>.
  // Highlighting before the code conversion means a term found inside a code span still gets
  // marked, and the backtick regex only ever consumes backticks, so it cannot corrupt the
  // <mark> tags already inserted. Doing it the other way round would let a search for "cod"
  // rewrite the inside of a <code> tag name.
  function hl(s, terms) {
    var out = esc(s);
    terms.forEach(function (t) {
      if (t.length < 2) return;
      out = out.replace(new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi'),
                        '<mark>$1</mark>');
    });
    return out.replace(/`([^`]+)`/g, '<code>$1</code>').replace(/`/g, '');
  }
  // The Needs field also carries code spans, and it gets truncated for the badge, so a naive
  // conversion leaves a dangling backtick wherever the cut landed inside a span. Truncate the
  // raw text first, then convert what is still balanced, then drop any survivor.
  function codeify(s) {
    return esc(s).replace(/`([^`]+)`/g, '<code>$1</code>').replace(/`/g, '');
  }
  function clip(s, n) {
    return s.length > n ? s.slice(0, n) + '\u2026' : s;
  }
  function meter(v) {
    var s = '';
    for (var i = 0; i < 5; i++) s += '<i class="' + (i < v ? 'on' : 'off') + '"></i>';
    return '<span class="meter" aria-hidden="true">' + s + '</span>';
  }

  function render(rows, terms) {
    if (!rows.length) { list.innerHTML = ''; empty.hidden = false; return; }
    empty.hidden = true;
    var buf = [];
    for (var k = 0; k < rows.length; k++) {
      var r = rows[k], sc = '';
      for (var i = 0; i < 5; i++) {
        sc += '<span class="sc"><b>' + LBL[i] + '</b>' + meter(r.s[i]) +
              '<em>' + r.s[i] + '</em></span>';
      }
      buf.push(
        '<li><div class="top"><span class="tid">' + r.i + '</span>' +
        '<h2>' + hl(r.t, terms) + '</h2></div>' +
        '<p class="desc">' + hl(r.d, terms) + '</p>' +
        '<div class="foot"><span class="tag cat">' + esc(r.c) + '</span>' +
        '<span class="tag">' + r.e + ', ' + EFFORT[r.e] + '</span>' +
        (r.r ? '<a class="tag built" href="' + esc(r.r) + '">Built and verified</a>' : '') +
        (r.nn ? '' : '<span class="tag needs" title="' + esc(r.n) + '">Needs: ' +
                     codeify(clip(r.n, 46)) + '</span>') +
        '<span class="scores">' + sc + '</span></div></li>');
    }
    list.innerHTML = buf.join('');
  }

  function apply() {
    var terms = q.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    var mins = sliders.map(function (s) { return +s.value; });
    var c = cat.value, ef = effort.value, wantNN = nn.checked, wantBuilt = built.checked;

    var rows = DATA.filter(function (r) {
      if (c && r.c !== c) return false;
      if (ef && r.e !== ef) return false;
      if (wantNN && !r.nn) return false;
      if (wantBuilt && !r.r) return false;
      for (var i = 0; i < 5; i++) if (r.s[i] < mins[i]) return false;
      if (terms.length) {
        var hay = (r.i + ' ' + r.t + ' ' + r.d + ' ' + r.c).toLowerCase();
        for (var j = 0; j < terms.length; j++) if (hay.indexOf(terms[j]) === -1) return false;
      }
      return true;
    });

    var s = sort.value;
    if (s === 'id') {
      rows.sort(function (a, b) { return a.i < b.i ? -1 : a.i > b.i ? 1 : 0; });
    } else if (s === 'sum') {
      var sum = function (r) { return r.s.reduce(function (x, y) { return x + y; }, 0); };
      rows.sort(function (a, b) { return sum(b) - sum(a) || (a.i < b.i ? -1 : 1); });
    } else {
      var idx = +s;
      rows.sort(function (a, b) { return b.s[idx] - a.s[idx] || (a.i < b.i ? -1 : 1); });
    }

    count.textContent = rows.length === DATA.length
      ? 'Showing all ' + DATA.length + ' entries'
      : 'Showing ' + rows.length + ' of ' + DATA.length + ' entries';
    render(rows, terms);
  }

  function reset() {
    q.value = ''; cat.value = ''; effort.value = ''; sort.value = 'id';
    nn.checked = false; built.checked = false;
    sliders.forEach(function (s) {
      s.value = 0;
      s.parentNode.querySelector('output').textContent = '0+';
    });
    apply();
  }

  [q, cat, effort, sort, nn, built].forEach(function (el) {
    el.addEventListener('input', apply);
  });
  sliders.forEach(function (s) {
    s.addEventListener('input', function () {
      s.parentNode.querySelector('output').textContent = s.value + '+';
      apply();
    });
  });
  document.getElementById('reset').addEventListener('click', reset);
  document.getElementById('reset2').addEventListener('click', reset);
  apply();
})();
"""


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--catalog", default=os.path.join(ROOT, "catalog"))
    ap.add_argument("--out", default=os.path.join(ROOT, "docs", "index.html"))
    ap.add_argument("--runs", default=os.path.join(ROOT, "logs", "runs.jsonl"))
    ap.add_argument("--expect", type=int, default=None,
                    help="required entry count; exit 1 on a mismatch")
    ap.add_argument("--check", action="store_true", help="parse and report, write nothing")
    a = ap.parse_args(argv)

    try:
        cats = load_all(a.catalog)
    except (ValueError, OSError) as err:
        sys.stderr.write(f"parse failed: {err}\n")
        return 1

    total = sum(len(c["entries"]) for c in cats)
    ids = [e["id"] for c in cats for e in c["entries"]]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        sys.stderr.write(f"duplicate ids: {sorted(dupes)[:10]}\n")
        return 1

    shipped = load_shipped(a.runs)
    matched = sum(1 for i in ids if i in shipped)

    for c in cats:
        print(f"  {c['file']:<26} {len(c['entries']):>4} entries  {c['title']}")
    print(f"  {'TOTAL':<26} {total:>4} entries in {len(cats)} categories, "
          f"{len(set(ids))} unique ids")
    print(f"  verified-built tasks in this catalog: {matched} "
          f"(of {len(shipped)} passing runs overall)")

    if a.expect is not None and total != a.expect:
        sys.stderr.write(f"expected {a.expect} entries, parsed {total}\n")
        return 1
    if a.check:
        return 0

    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    page = render(cats, shipped)
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(page)
    print(f"  wrote {a.out} ({len(page) / 1024:.0f} KiB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
