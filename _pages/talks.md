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
      {% if t.venue or t.location or t.date %}<br>{% endif %}
      {% if t.venue %}<span style="opacity:0.9">{{ t.venue }}</span>{% endif %}
      {% if t.location %}<span style="opacity:0.9"> · {{ t.location }}</span>{% endif %}
      {% if t.date %}<span style="opacity:0.8"> · {{ t.date | date: "%b %Y" }}</span>{% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>

## Past talks

{% assign past_talks = site.talks | where: "status", "past" | sort: "date" | reverse %}

{% assign current_year = "" %}

{% for t in past_talks %}
  {% assign talk_year = t.date | date: "%Y" %}

  {% if talk_year != current_year %}
    {% unless forloop.first %}</ul>{% endunless %}
    <h3>{{ talk_year }}</h3>
    <ul class="compact-list">
    {% assign current_year = talk_year %}
  {% endif %}

  <li>
    <strong><a href="{{ t.url | relative_url }}">{{ t.title }}</a></strong> 
    {% if t.venue or t.location or t.date %}<br>{% endif %}
    {% if t.venue %}<span style="opacity:0.9">{{ t.venue }}</span>{% endif %}
    {% if t.location %}<span style="opacity:0.9"> · {{ t.location }}</span>{% endif %}
    {% if t.date %}<span style="opacity:0.8"> · {{ t.date | date: "%B %Y" }}</span>{% endif %}
  </li>

  {% if forloop.last %}</ul>{% endif %}
{% endfor %}