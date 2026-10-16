"""Convert bib/*.bib into data/publications/*.json for the Hugo site.

Each BibTeX file becomes one JSON file with the date of the last commit that
changed it ("lastmod", used in the sitemap) and a list of year groups ("years",
newest first) holding formatted entries for layouts/_shortcodes/publications.html.

Website-only BibTeX fields:
    abstract       shown in a collapsible block
    fulltext       link labeled "full text"
    customlinkXYZ  link labeled "XYZ"
They are dropped from the BibTeX shown on the page.
"""

import html
import json
import re
import subprocess
import sys
from itertools import groupby
from pathlib import Path

from pybtex.database import BibliographyData, Entry
from pybtex.database.input.bibtex import Parser
from pybtex.database.output.bibtex import Writer as BibTeXWriter
from pybtex.markup import LaTeXParser
from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.style.template import tag

ROOT = Path(__file__).resolve().parent.parent
BIB_DIR = ROOT / "bib"
OUT_DIR = ROOT / "data" / "publications"
HIGHLIGHT_AUTHORS = ["Petar Mlinarić"]
CUSTOM_LINK_PREFIX = "customlink"

MATH_RE = re.compile(r"\\\((.+?)\\\)", re.DOTALL)
MONTHS = [
    "jan",
    "feb",
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec",
]


class Style(UnsrtStyle):
    """Unsrt style with bold titles."""

    def format_title(self, e, which_field, as_sentence=True):
        return tag("strong")[super().format_title(e, which_field, as_sentence)]


class Writer(BibTeXWriter):
    """BibTeX writer that outputs fields as written.

    Parsed fields are already LaTeX, so the default encoding would escape them
    again (e.g., `_` becomes `\\_`, breaking DOIs and math).
    """

    def _encode(self, text):
        return text


def date_key(entry):
    """Sort key (year, month); month is 0 if missing or unrecognized."""
    month = entry.fields.get("month", "").strip().lower()
    month_num = MONTHS.index(month[:3]) + 1 if month[:3] in MONTHS else 0
    return int(entry.fields["year"]), month_num


def git_lastmod(path):
    """Date of the last commit that changed `path` (None if unavailable)."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", str(path)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip() or None


def unescape_math(s):
    """Undo HTML escaping inside \\( ... \\) so KaTeX gets plain TeX."""
    return MATH_RE.sub(lambda m: r"\(" + html.unescape(m.group(1)) + r"\)", s)


def text_to_html(s):
    """HTML-escape plain text and typeset dashes, leaving \\( ... \\) untouched."""

    def convert(t):
        return html.escape(t, quote=False).replace("---", "—").replace("--", "–")

    parts, pos = [], 0
    for m in MATH_RE.finditer(s):
        parts += [convert(s[pos : m.start()]), m.group(0)]
        pos = m.end()
    parts.append(convert(s[pos:]))
    return "".join(parts)


def latex_to_html(s):
    """Convert a LaTeX field value to HTML, keeping \\( ... \\) for KaTeX."""
    return text_to_html(" ".join(str(LaTeXParser(s).parse()).split()))


def highlight(ref, author):
    """Make the first occurrence of `author` bold (pybtex may use &nbsp;)."""
    pattern = r"(?:\s|&nbsp;)+".join(map(re.escape, author.split()))
    return re.sub(pattern, lambda m: f"<strong>{m.group(0)}</strong>", ref, count=1)


def convert_entry(style, key, entry):
    ref = next(iter(style.format_entries([entry]))).text.render_as("html")
    ref = unescape_math(ref)
    for author in HIGHLIGHT_AUTHORS:
        ref = highlight(ref, author)

    fields = dict(entry.fields)
    links = []
    if "fulltext" in fields:
        links.append({"label": "full text", "url": fields["fulltext"]})
    for name, value in fields.items():
        if name.lower().startswith(CUSTOM_LINK_PREFIX):
            links.append({"label": name[len(CUSTOM_LINK_PREFIX) :], "url": value})

    abstract = latex_to_html(fields["abstract"]) if "abstract" in fields else ""

    public_fields = {
        name: value
        for name, value in fields.items()
        if name.lower() not in ("abstract", "fulltext")
        and not name.lower().startswith(CUSTOM_LINK_PREFIX)
    }
    public_entry = Entry(entry.type, public_fields, entry.persons)
    bibtex = Writer().to_string(BibliographyData({key: public_entry})).strip()

    return {
        "key": key,
        "title": latex_to_html(fields["title"]),
        "reference": ref,
        "links": links,
        "abstract": abstract,
        "bibtex": bibtex,
    }


def convert_file(style, path):
    entries = Parser().parse_file(str(path)).entries
    # Newest first by year and month (bibtex-tidy sorts the files by key).
    items = sorted(entries.items(), key=lambda item: date_key(item[1]), reverse=True)
    return [
        {
            "year": year,
            "entries": [convert_entry(style, key, entry) for key, entry in group],
        }
        for year, group in groupby(items, key=lambda item: item[1].fields["year"])
    ]


def main():
    bib_files = sorted(BIB_DIR.glob("*.bib"))
    if not bib_files:
        sys.exit(f"No .bib files found in {BIB_DIR}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for old in OUT_DIR.glob("*.json"):
        old.unlink()
    style = Style()
    for path in bib_files:
        groups = convert_file(style, path)
        data = {"lastmod": git_lastmod(path), "years": groups}
        out = OUT_DIR / f"{path.stem}.json"
        out.write_text(
            json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
        )
        count = sum(len(g["entries"]) for g in groups)
        print(f"{path.relative_to(ROOT)} -> {out.relative_to(ROOT)} ({count} entries)")


if __name__ == "__main__":
    main()
