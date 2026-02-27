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

<ul class="pub-list">
{% assign pubs = site.publications | sort: "date" | reverse %}
{% for pub in pubs %}
  {% if pub.status == 'unpublished' %}
    <li class="pub-item">
      <span class="pub-title">
        <a href="{{ pub.url | relative_url }}">{{ pub.title }}</a>
      </span>
      <div class="pub-meta">
        {% if pub.authors %}{{ pub.authors }}. {% endif %}
        {% if pub.venue %}<em>{{ pub.venue }}</em>{% endif %}
        {% if pub.date %} · {{ pub.date | date: "%B %Y" }}{% endif %}
        {% if pub.paperurl %}
          · <a class="pub-link" href="{{ pub.paperurl }}">arXiv</a>
        {% endif %}
      </div>
    </li>
  {% endif %}
{% endfor %}
</ul>

## Peer-reviewed publications

<ul class="pub-list">
{% for pub in pubs %}
  {% if pub.status == 'published' %}
    <li class="pub-item">
      <div class="pub-citation">
        {{ pub.citation }}
      </div>
      <div class="pub-links">
        <a class="pub-link" href="{{ pub.paperurl }}">DOI</a>{% endif %}
      </div>
    </li>
  {% endif %}
{% endfor %}
</ul>

## Monographs

### Book contributions

<ul class="pub-list">
{% for pub in pubs %}
  {% if pub.status == 'monograph_book_contribution' %}
    <li class="pub-item">
      {% if pub.citation %}
        <div class="pub-citation">{{ pub.citation }}</div>
      {% else %}
        <div class="pub-citation">
          {% if pub.authors %}{{ pub.authors }}. {% endif %}
          <span class="pub-title"><a href="{{ pub.url | relative_url }}">{{ pub.title }}</a></span>
          {% if pub.venue %}. <em>{{ pub.venue }}</em>{% endif %}
          {% if pub.date %} ({{ pub.date | date: "%Y" }}){% endif %}
        </div>
      {% endif %}
      <div class="pub-links">
        <a class="pub-link" href="{{ pub.paperurl }}">DOI</a>{% endif %}
      </div>
    </li>
  {% endif %}
{% endfor %}
</ul>

### Book publications

<ul class="pub-list">
{% for pub in pubs %}
  {% if pub.status == 'monograph_book' %}
    <li class="pub-item">
      {% if pub.citation %}
        <div class="pub-citation">{{ pub.citation }}</div>
      {% else %}
        <div class="pub-citation">
          {% if pub.authors %}{{ pub.authors }}. {% endif %}
          <span class="pub-title"><a href="{{ pub.url | relative_url }}">{{ pub.title }}</a></span>
          {% if pub.venue %}. <em>{{ pub.venue }}</em>{% endif %}
          {% if pub.date %} ({{ pub.date | date: "%Y" }}){% endif %}
        </div>
      {% endif %}
      <div class="pub-links">
        <a class="pub-link" href="{{ pub.paperurl }}">DOI</a>{% endif %}
      </div>
    </li>
  {% endif %}
{% endfor %}
</ul>

### PhD thesis

<ul class="pub-list">
{% for pub in pubs %}
  {% if pub.status == 'monograph_thesis' %}
    <li class="pub-item">
      {% if pub.citation %}
        <div class="pub-citation">{{ pub.citation }}</div>
      {% else %}
        <div class="pub-citation">
          {% if pub.authors %}{{ pub.authors }}. {% endif %}
          <span class="pub-title"><a href="{{ pub.url | relative_url }}">{{ pub.title }}</a></span>
          {% if pub.venue %}. <em>{{ pub.venue }}</em>{% endif %}
          {% if pub.date %} ({{ pub.date | date: "%Y" }}){% endif %}
        </div>
      {% endif %}
      <div class="pub-links">
        <a class="pub-link" href="{{ pub.paperurl }}">DOI</a>{% endif %}
      </div>
    </li>
  {% endif %}
{% endfor %}
</ul>