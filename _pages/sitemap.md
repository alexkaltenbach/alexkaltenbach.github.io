---
layout: archive
title: "Sitemap"
description: "Main sections of Alex Kaltenbach's academic website."
permalink: /sitemap/
author_profile: true
---

- [Home]({{ '/' | relative_url }})
{% for item in site.data.navigation.main %}
- [{{ item.title }}]({{ item.url | relative_url }})
{% endfor %}

Individual articles are listed under [Publications]({{ '/publications/' | relative_url }}). An [XML sitemap]({{ '/sitemap.xml' | relative_url }}) is also available.
