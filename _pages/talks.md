---
layout: archive
title: "Talks"
permalink: /talks/
author_profile: true
---

{% include base_path %}

{% if site.talkmap_link == true %}
<p style="text-decoration:underline;"><a href="/talkmap.html">See a map of all the places I've given a talk!</a></p>
{% endif %}

## Upcoming talks

<ul class="compact-list">
{% assign talks_sorted = site.talks | sort: "date" %}
{% for t in talks_sorted %}
  {% if t.status == 'upcoming' %}
    <li>
      <strong><a href="{{ t.url | relative_url }}">{{ t.title }}</a></strong>
      {% if t.type %} — {{ t.type }}{% endif %}
      {% if t.venue or t.location or t.date %}<br>{% endif %}
      {% if t.venue %}<span style="opacity:0.9">{{ t.venue }}</span>{% endif %}
      {% if t.location %}<span style="opacity:0.9"> · {{ t.location }}</span>{% endif %}
      {% if t.date %}<span style="opacity:0.8"> · {{ t.date | date: "%Y-%m-%d" }}</span>{% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>

## Past talks

<ul class="compact-list">
{% assign talks_sorted_desc = site.talks | sort: "date" | reverse %}
{% for t in talks_sorted_desc %}
  {% if t.status == 'past' %}
    <li>
      <strong><a href="{{ t.url | relative_url }}">{{ t.title }}</a></strong>
      {% if t.type %} — {{ t.type }}{% endif %}
      {% if t.venue or t.location or t.date %}<br>{% endif %}
      {% if t.venue %}<span style="opacity:0.9">{{ t.venue }}</span>{% endif %}
      {% if t.location %}<span style="opacity:0.9"> · {{ t.location }}</span>{% endif %}
      {% if t.date %}<span style="opacity:0.8"> · {{ t.date | date: "%Y-%m-%d" }}</span>{% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>