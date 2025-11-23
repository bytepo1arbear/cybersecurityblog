---
layout: default
title: "Projects"
permalink: /projects/
---

# Projects

Welcome to my homelab and cybersecurity projects.

{% for project in site.projects %}
  <article class="project">
    <h2><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h2>
    <div class="project-content">
      {{ project.content }}
    </div>
  </article>
{% endfor %}
