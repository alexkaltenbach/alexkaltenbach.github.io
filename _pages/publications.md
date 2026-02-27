---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a></u>.
{% endif %}

{% include base_path %}

**Publication list (PDF):** [Link to PDF](/files/PubList.pdf)

---

## Preprints

<ol reversed>
{% assign pubs = site.publications | sort: "date" | reverse %}
{% for pub in pubs %}
  {% if pub.status == 'unpublished' %}
    <li>
      {% if pub.authors %}{{ pub.authors }}:{% endif %}
      <strong>{{ pub.title }}</strong>,
      <em>{{ pub.venue }}</em>{% if pub.year %} ({{ pub.year }}){% endif %}
      {% if pub.paperurl %} [<a href="{{ pub.paperurl }}">PDF</a>]{% endif %}
      {% if pub.doi %} [<a href="https://doi.org/{{ pub.doi }}">DOI</a>]{% endif %}
    </li>
  {% endif %}
{% endfor %}
</ol>

## Peer-reviewed Publications

<ol reversed>
{% for pub in pubs %}
  {% if pub.status == 'published' %}
    <li>
      {% if pub.authors %}{{ pub.authors }}:{% endif %}
      <strong>{{ pub.title }}</strong>,
      <em>{{ pub.venue }}</em>{% if pub.year %} ({{ pub.year }}){% endif %}
      {% if pub.paperurl %} [<a href="{{ pub.paperurl }}">PDF</a>]{% endif %}
      {% if pub.doi %} [<a href="https://doi.org/{{ pub.doi }}">DOI</a>]{% endif %}
    </li>
  {% endif %}
{% endfor %}
</ol>

## Monographs

### Book Contributions

<ul>
{% for pub in pubs %}
  {% if pub.status == 'monograph_book_contribution' %}
    <li>
      {% if pub.authors %}{{ pub.authors }}:{% endif %}
      <strong>{{ pub.title }}</strong>,
      <em>{{ pub.venue }}</em>{% if pub.year %} ({{ pub.year }}){% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>

### Book Publications

<ul>
{% for pub in pubs %}
  {% if pub.status == 'monograph_book' %}
    <li>
      {% if pub.authors %}{{ pub.authors }}:{% endif %}
      <strong>{{ pub.title }}</strong>,
      <em>{{ pub.venue }}</em>{% if pub.year %} ({{ pub.year }}){% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>

### PhD Thesis

<ul>
{% for pub in pubs %}
  {% if pub.status == 'monograph_thesis' %}
    <li>
      {% if pub.authors %}{{ pub.authors }}:{% endif %}
      <strong>{{ pub.title }}</strong>,
      <em>{{ pub.venue }}</em>{% if pub.year %} ({{ pub.year }}){% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>