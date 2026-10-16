# pmli.github.io

Source of <https://pmli.github.io>, built with [Hugo](https://gohugo.io/)
(no theme; templates are in `layouts/`).

## Layout

- `content/`: pages in Markdown (math with `\( ... \)` and `\[ ... \]`)
- `bib/`: publications as BibTeX, one file per section of the publications page
- `scripts/bib2json.py`: converts `bib/*.bib` into `data/publications/*.json`
- `static/`: files copied as is (`static/pdf/mlinaric_cv.pdf` is served at
  `/pdf/mlinaric_cv.pdf`)

Besides the standard BibTeX fields, entries can have `abstract`, `fulltext`
(shown as "full text" link) and `customlinkXYZ` (shown as "XYZ" link).

## Local preview

CI uses the Python version in `.python-version` and the Hugo version in
`.github/workflows/main.yml` (`HUGO_VERSION`).

```sh
uv venv  # creates .venv with the Python from .python-version
source .venv/bin/activate
uv pip install -r requirements.txt
python scripts/bib2json.py
hugo server
```

Rerun `scripts/bib2json.py` after editing a `.bib` file.

## Deployment

Pushing to `main` builds the site and deploys it to GitHub Pages
(`.github/workflows/main.yml`).
Other workflows run the pre-commit hooks with prek (`lint.yml`)
and check for dead links monthly (`links.yml`).
