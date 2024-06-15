---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<!---
{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}
--->

Preprints
====== 

---
title: "The Deep Ritz Method for Parametric p-Dirichlet Problems"
collection: preprints
permalink: /preprints/2022-07-05-paper
excerpt: #'This paper is about the number 1. The number 2 is left for future work.'
date: 2022-07-05
venue: 'ArXiv'
paperurl: 'https://arxiv.org/abs/2207.01894'
---

[Download paper here](https://arxiv.org/pdf/2207.01894) 


{% for post in site.preprints reversed %}
  {% include archive-single.html %}
{% endfor %}


Peer-reviewed Publications
======

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
