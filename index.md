---
layout: default
title: My blog
---

## {{ page.title }}

* my latest blog

{% for post in site.posts %}

*   {{ post.data | date_to_string }}  [{{ post.title }}]({{ site.baseurl }}{{ post.url }})

{% endfor %}
