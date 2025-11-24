---
layout: default
title: "Writeups"
permalink: /writeups/
exclude_from_collection: true
---

# Writeups

All lab experiments and notes:

{% for writeup in site.writeups %}
  {% unless writeup.exclude_from_collection %}
  <article class="writeup-preview">
    <div class="card-header">
      <span class="post-date">{{ writeup.date | date: "%B %d, %Y" }}</span>
      {% if writeup.difficulty %}
      <span class="difficulty difficulty-{{ writeup.difficulty | downcase }}">{{ writeup.difficulty }}</span>
      {% endif %}
    </div>
    <h3><a href="{{ writeup.url | relative_url }}">{{ writeup.title }}</a></h3>
    <p>{{ writeup.excerpt | strip_html | truncatewords: 60 }}</p>
    {% if writeup.tags %}
    <div class="post-tags">
      {% for tag in writeup.tags %}
      <span class="tag">{{ tag }}</span>
      {% endfor %}
    </div>
    {% endif %}
    <a href="{{ writeup.url | relative_url }}" class="btn-read-more">Read Writeup →</a>
  </article>
  {% endunless %}
{% endfor %}
