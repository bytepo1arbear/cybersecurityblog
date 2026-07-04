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
  {% comment %} Only show two main projects: Personal Home Lab and Cyber Security Lab {% endcomment %}
  {% assign home = site.projects | where: "title", "Homelab Setup" | first %}
  {% assign cyber = site.projects | where: "title", "Penetration Testing Lab" | first %}
  {% if home %}
  <article class="project-preview">
    <div class="card-header"><span class="post-date">{{ home.date | date: "%B %Y" }}</span></div>
    <h3><a href="{{ home.url | relative_url }}">Personal Home Lab</a></h3>
    <p>{{ home.excerpt | strip_html | truncatewords: 40 }}</p>
    <a href="{{ home.url | relative_url }}" class="btn-read-more">View Project →</a>
  </article>
  {% endif %}
  {% if cyber %}
  <article class="project-preview">
    <div class="card-header"><span class="post-date">{{ cyber.date | date: "%B %Y" }}</span></div>
    <h3><a href="{{ cyber.url | relative_url }}">Cyber Security Lab</a></h3>
    <p>{{ cyber.excerpt | strip_html | truncatewords: 40 }}</p>
    <a href="{{ cyber.url | relative_url }}" class="btn-read-more">View Project →</a>
  </article>
  {% endif %}
</div>
