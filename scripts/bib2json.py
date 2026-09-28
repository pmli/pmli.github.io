"""Convert bib/*.bib into data/publications/*.json for the Hugo site.

Each BibTeX file becomes one JSON file: a list of year groups (newest first),
each holding formatted entries for layouts/_shortcodes/publications.html.

Website-only BibTeX fields:
    abstract       shown in a collapsible block
    fulltext       link labeled "full text"
    customlinkXYZ  link labeled "XYZ"
They are dropped from the BibTeX shown on the page.
"""

import html
import json
import re
import sys
from itertools import groupby
from pathlib import Path

from pybtex.database import BibliographyData, Entry
from pybtex.database.input.bibtex import Parser
from pybtex.markup import LaTeXParser
from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.style.template import tag

ROOT = Path(__file__).resolve().parent.parent
BIB_DIR = ROOT / "bib"
OUT_DIR = ROOT / "data" / "publications"
HIGHLIGHT_AUTHORS = ["Petar Mlinarić"]
CUSTOM_LINK_PREFIX = "customlink"

MATH_RE = re.compile(r"\\\((.+?)\\\)", re.DOTALL)


class Style(UnsrtStyle):
    """Unsrt style with bold titles."""

    def format_title(self, e, which_field, as_sentence=True):
        return tag("strong")[super().format_title(e, which_field, as_sentence)]


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

    abstract = ""
    if "abstract" in fields:
        abstract = str(LaTeXParser(fields["abstract"]).parse())
        abstract = text_to_html(" ".join(abstract.split()))

    public_fields = {
        name: value
        for name, value in fields.items()
        if name.lower() not in ("abstract", "fulltext")
        and not name.lower().startswith(CUSTOM_LINK_PREFIX)
    }
    public_entry = Entry(entry.type, public_fields, entry.persons)
    bibtex = BibliographyData({key: public_entry}).to_string("bibtex").strip()

    return {
        "key": key,
        "reference": ref,
        "links": links,
        "abstract": abstract,
        "bibtex": bibtex,
    }


def convert_file(style, path):
    entries = Parser().parse_file(str(path)).entries
    # Newest first; entries from the same year keep their order in the file.
    items = sorted(
        entries.items(), key=lambda item: item[1].fields["year"], reverse=True
    )
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
        out = OUT_DIR / f"{path.stem}.json"
        out.write_text(
            json.dumps(groups, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
        )
        count = sum(len(g["entries"]) for g in groups)
        print(f"{path.relative_to(ROOT)} -> {out.relative_to(ROOT)} ({count} entries)")


if __name__ == "__main__":
    main()
