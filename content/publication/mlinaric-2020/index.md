---
title: Structure-preserving model order reduction for network systems

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- admin

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2020-01-23'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-03-29T18:14:15.308560Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- thesis

# Publication name and optional abbreviated publication name.
publication: 'Otto von Guericke University of Magdeburg'
publication_short: ''

doi: 10.25673/33570

abstract: >-
  This thesis considers structure-preserving system-theoretic model order
  reduction for certain structured input-output systems, particularly network
  systems. In the first part, our focus lies on the clustering-based approach to
  reduce network systems. Therein, we begin by considering clustering-based
  model order reduction for linear multi-agent systems. This approach finds a
  reduced model whose dynamics evolve over a smaller network. To measure the
  reduction error, we use the $\mathcal{H}_2$-norm and consider the
  $\mathcal{H}_2$-optimal clustering problem. Since clustering is generally a
  difficult combinatorial problem, we propose a framework based on relaxing the
  discrete problem to find an $\mathcal{H}_2$-suboptimal clustering. Following
  on this, we directly extend the framework to a class of nonlinear multi-agent
  systems. Next, we derive upper bounds for $\mathcal{H}_2$ and
  $\mathcal{H}_\infty$ clustering-based reduction errors for linear multi-agent
  systems based on almost equitable partitions. These results generalize work
  for multi-agent systems with single-integrator agents. Using a similar
  approach for power systems, which are a special class of nonlinear multi-agent
  systems, we find conditions for exact clustering-based reduction.
  Additionally, we study subsystem reduction for network systems. We propose a
  balancing-based approach that guarantees stability preservation under a
  small-gain condition. Furthermore, we consider the $\mathcal{H}_2$-optimal
  subsystem reduction problem. We derive Gramian-based first-order necessary
  $\mathcal{H}_2$-optimality conditions and use a gradient-based optimization
  method to fulfill them. Finally, we apply the structure-preserving
  $\mathcal{H}_2$-optimal model reduction approach for network systems to other
  structured systems. In particular, we consider $\mathcal{H}_2$-optimal model
  order reduction of second-order systems, port-Hamiltonian systems, time-delay
  systems and $\mathcal{H}_2 \otimes \mathcal{L}_2$-optimal model order
  reduction of parametric systems. Here, we also derive Gramian-based
  $\mathcal{H}_2$-optimality conditions and use an optimization approach to
  construct a reduced model. For some structured systems, we also derive
  interpolatory $\mathcal{H}_2$-optimality conditions under additional
  assumptions on the reduced model.

# Summary. An optional shortened abstract.
summary: ''

tags:
- model order reduction
- network systems
- linear time-invariant systems
- structured systems
- h2 norm

# Display this page in a list of Featured pages?
featured: false

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
---
