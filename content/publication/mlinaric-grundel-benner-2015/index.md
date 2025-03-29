---
title: >-
  Efficient model order reduction for multi-agent systems using QR
  decomposition-based clustering

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Sara Grundel
- Peter Benner

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2015-12-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-03-27T09:36:46.541812Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*54th IEEE Conference on Decision and Control (CDC)*'
publication_short: ''

doi: 10.1109/CDC.2015.7402967

abstract: >-
  In this paper we present an efficient model order reduction method for
  multi-agent systems with Laplacian-based dynamics. The method combines an
  established model order reduction method and a clustering algorithm to produce
  a graph partition used for reduction, thus preserving structure and consensus.
  By the Iterative Rational Krylov Algorithm, a good reduced order model can be
  found which is not necessarily structure preserving. However, based on this we
  can efficiently find a partition using the QR decomposition with column
  pivoting as a clustering algorithm, so that the structure can be restored. We
  illustrate the effectiveness on an example from the open literature.

# Summary. An optional shortened abstract.
summary:

tags:
- model order reduction
- multi-agent systems
- linear time-invariant systems
- clustering

# Display this page in a list of Featured pages?
featured: true

# Links
url_pdf: ''
url_code: ''
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

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides:
---
