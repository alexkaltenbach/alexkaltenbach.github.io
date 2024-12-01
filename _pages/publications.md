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

<big><b>Publication list (in PDF format):</b> <a href="/files/PubList.pdf">Link to PDF</a></big>

<big><b>Preprints</b></big>

{% for post in site.publications reversed %} 
  {% if post.status == 'unpublished' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}


<big><b>Peer-reviewed Publications</b></big>

{% for post in site.publications reversed %}
  {% if post.status == 'published' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}


<big><b>Monographs</b></big>

<big>Book Contributions</big>

{% for post in site.publications reversed %}
  {% if post.status == 'monograph_book_contribution' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}


<big>Book Publications</big>

{% for post in site.publications reversed %}
  {% if post.status == 'monograph_book' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}


<big>PhD Thesis</big>

{% for post in site.publications reversed %}
  {% if post.status == 'monograph_thesis' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
