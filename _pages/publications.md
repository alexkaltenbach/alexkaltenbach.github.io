---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}


Preprints
====== 

{% for post in site.publications reversed %} 
  {% if post.status == 'unpublished' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}


Peer-reviewed Publications
======

{% for post in site.publications reversed %}
  {% if post.status == 'published' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
