---
layout: archive
title: "Publications"
description: "Publications, preprints, monographs and theses by Alex Kaltenbach, with DOI, arXiv and research code links."
permalink: /publications/
author_profile: true
---

[Publication list (PDF)]({{ '/files/PubList.pdf' | relative_url }}) · [Google Scholar]({{ site.author.googlescholar }}) · [ORCID]({{ site.author.orcid }})

<nav class="section-nav" aria-label="Publication sections">
  <a href="#preprints">Preprints</a>
  <a href="#accepted--forthcoming">Accepted</a>
  <a href="#peer-reviewed-publications">Journal articles</a>
  <a href="#books">Books</a>
  <a href="#theses">Theses</a>
</nav>

{% assign pubs = site.publications | sort: 'sort_key' | reverse %}

## Preprints

<ul class="pub-list">
{% for pub in pubs %}{% if pub.status == 'unpublished' %}{% include publication-item.html pub=pub %}{% endif %}{% endfor %}
</ul>

## Accepted / forthcoming

<ul class="pub-list">
{% for pub in pubs %}{% if pub.status == 'accepted' %}{% include publication-item.html pub=pub %}{% endif %}{% endfor %}
</ul>

## Peer-reviewed publications

{% assign published = pubs | where: 'status', 'published' | group_by: 'publication_year' %}
{% for year in published %}
### {{ year.name }}

<ul class="pub-list">
{% for pub in year.items %}{% include publication-item.html pub=pub %}{% endfor %}
</ul>
{% endfor %}

## Books

<ul class="pub-list">
{% for pub in pubs %}{% if pub.status == 'monograph_book' %}{% include publication-item.html pub=pub %}{% endif %}{% endfor %}
</ul>

### Book chapters and proceedings

<ul class="pub-list">
{% for pub in pubs %}{% if pub.status == 'monograph_book_contribution' %}{% include publication-item.html pub=pub %}{% endif %}{% endfor %}
</ul>

## Theses

<ul class="pub-list">
{% for pub in pubs %}{% if pub.status == 'monograph_thesis' %}{% include publication-item.html pub=pub %}{% endif %}{% endfor %}
  <li class="pub-item">
    <div class="pub-citation">Kaltenbach, A. <i>Verallgemeinerte nichtlineare Evolutionsgleichungen.</i> Master's thesis, University of Freiburg (2019).</div>
    <a class="pub-link" href="{{ '/files/Kaltenbach_Masterarbeit_2019.pdf' | relative_url }}">PDF · corrected version</a>
  </li>
  <li class="pub-item">
    <div class="pub-citation">Kaltenbach, A. <i>Nichtlineare Evolutionsgleichungen.</i> Bachelor's thesis, University of Freiburg (2017).</div>
    <a class="pub-link" href="{{ '/files/Kaltenbach_Bachelorarbeit_2017.pdf' | relative_url }}">PDF · corrected version</a>
  </li>
</ul>
