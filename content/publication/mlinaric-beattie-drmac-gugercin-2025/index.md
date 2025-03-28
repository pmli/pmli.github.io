---
title: IRKA is a Riemannian Gradient Descent Method

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Christopher A. Beattie
- Zlatko Drmač
- Serkan Gugercin

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-03-27T15:13:48.495576Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*IEEE Trans. Autom. Control*'
publication_short: ''

doi: 10.1109/TAC.2024.3489416

abstract: |
  The iterative rational Krylov algorithm (IRKA) is a commonly used fixed-point
  iteration developed to minimize the $\mathcal{H}_2$ model order reduction
  error. In this work, IRKA is recast as a Riemannian gradient descent method
  with a fixed step size over the manifold of rational functions having fixed
  degree. This interpretation motivates the development of a Riemannian
  gradient descent method utilizing as a natural extension variable step size
  and line search. Comparisons made between IRKA and this extension on a few
  examples demonstrate significant benefits.

# Summary. An optional shortened abstract.
summary: ''

tags:
- model order reduction
- Riemannian optimization
- linear time-invariant systems

# Display this page in a list of Featured pages?
featured: true

# Links
url_pdf: 'https://arxiv.org/pdf/2311.02031'
url_code: 'https://github.com/pmli/rgd-irka-experiments'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

# Publication image
# Add an image named `featured.jpg/png` to your page's folder then add a caption below.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
---
