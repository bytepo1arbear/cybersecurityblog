---
layout: default
title: "Projects"
permalink: /projects/
exclude_from_collection: true
---

<section class="page-hero">
  <div class="container">
    <h1>Projects</h1>
    <p class="page-subtitle">Hands-on builds, lab infrastructure, and defensive/offensive security tooling.</p>
  </div>
</section>

<div class="project-grid">
{% assign visible_projects = site.projects | where_exp: "item", "item.exclude_from_collection != true" %}
{% for project in visible_projects %}
  <article class="project-preview">
    <div class="card-header">
      <span class="post-date">{{ project.date | date: "%B %Y" }}</span>
    </div>
    <h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
    <p>{{ project.excerpt | strip_html | truncatewords: 40 }}</p>
    <a href="{{ project.url | relative_url }}" class="btn-read-more">View Project →</a>
  </article>
{% endfor %}
</div>
