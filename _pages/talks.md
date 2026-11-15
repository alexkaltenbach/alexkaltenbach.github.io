---
layout: archive
title: "Talks"
description: "Upcoming and past talks by Alex Kaltenbach, including lecture series slides."
permalink: /talks/
author_profile: true
---

{% include base_path %}

{% if site.talkmap_link == true %}
<p><a class="talkmap-link" href="/talkmap.html">Map of talks</a></p>
{% endif %}

## Upcoming talks

<ul class="talk-list">
{% assign talks_sorted = site.talks | sort: "date" %}
{% for t in talks_sorted %}
  {% if t.status == 'upcoming' %}
    <li class="talk-item">
      <div class="talk-row">
        <span class="talk-title">{{ t.title }}</span>
      </div>
      <div class="talk-meta">
        {% if t.venue %}<span>{{ t.venue }}</span>{% endif %}
        {% if t.location %}<span> · {{ t.location }}</span>{% endif %}
        {% if t.date %}<span class="talk-date"> · {{ t.date | date: "%B %Y" }}</span>{% endif %}
      </div>
    </li>
  {% endif %}
{% endfor %}
</ul>

## Lecture series materials

**Duality-based numerical methods — Freiburg, 2024.**
[Session 1 (PDF)]({{ '/talks/slides/Freiburg_Session1.pdf' | relative_url }}) · [Session 2 (PDF)]({{ '/talks/slides/Freiburg_Session2.pdf' | relative_url }}) · [Session 3 (PDF)]({{ '/talks/slides/Freiburg_Session3.pdf' | relative_url }}) · [Session 4 (PDF)]({{ '/talks/slides/Freiburg_Session4.pdf' | relative_url }})

## Past talks

{% assign past_talks = site.talks | where: "status", "past" | sort: "date" | reverse %}
{% assign grouped = past_talks | group_by_exp: "t", "t.date | date: '%Y'" %}

{% for year in grouped %}
### {{ year.name }}

<ul class="talk-list">
{% for t in year.items %}
  <li class="talk-item">
    <div class="talk-row">
      <span class="talk-title">{{ t.title }}</span>
    </div>
    <div class="talk-meta">
      {% if t.venue %}<span>{{ t.venue }}</span>{% endif %}
      {% if t.location %}<span> · {{ t.location }}</span>{% endif %}
      {% if t.date %}<span class="talk-date"> · {{ t.date | date: "%B %Y" }}</span>{% endif %}
    </div>
  </li>
{% endfor %}
</ul>
{% endfor %}