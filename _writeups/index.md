---
layout: default
title: "Writeups"
permalink: /writeups/
---

# Writeups

All lab experiments and notes:

{% for writeup in site.writeups %}
  <article class="writeup">
    <h2><a href="{{ writeup.url | relative_url }}">{{ writeup.title }}</a></h2>
    <div class="writeup-content">
      {{ writeup.content }}
    </div>
  </article>
{% endfor %}
