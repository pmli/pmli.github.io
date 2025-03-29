---
title: >-
  $\mathcal{L}_2$-optimal Reduced-order Modeling Using Parameter-separable Forms

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Serkan Gugercin

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2023-04-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-03-27T15:13:48.499259Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*SIAM J. Sci. Comput.*'
publication_short: ''

doi: 10.1137/22M1500678

abstract: >-
  We provide a unifying framework for $\mathcal{L}_2$-optimal reduced-order
  modeling for linear time-invariant dynamical systems and stationary parametric
  problems. Using parameter-separable forms of the reduced-model quantities, we
  derive the gradients of the $\mathcal{L}_2$ cost function with respect to the
  reduced matrices, which then allows a non-intrusive, data-driven,
  gradient-based descent algorithm to construct the optimal approximant using
  only output samples. By choosing an appropriate measure, the framework covers
  both continuous (Lebesgue) and discrete cost functions. We show the efficacy
  of the proposed algorithm via various numerical examples. Furthermore, we
  analyze under what conditions the data-driven approximant can be obtained via
  projection.

# Summary. An optional shortened abstract.
summary: ''

tags:
- model order reduction
- parametric systems
- stationary problems
- linear time-invariant systems
- l2 norm

# Display this page in a list of Featured pages?
featured: true

# Links
url_pdf: 'https://arxiv.org/pdf/2206.02929'
url_code: 'https://zenodo.org/records/6618116'
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
