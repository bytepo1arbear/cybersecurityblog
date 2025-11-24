---
layout: default
title: Home
permalink: /
---

<section class="hero">
  <div class="container">
    <h1>My Cybersecurity Learning Journey</h1>
    <p>Sharing my experiences, lessons learned, and resources along the way.</p>
  </div>
</section>

<section class="latest-posts">
  <div class="container">
    <h2>Latest Blog Posts</h2>
    <div class="post-grid">
      {% for post in site.posts limit:10 %}
      <article class="post-preview">
        <h3>{{ post.title }}</h3>
        <p>{{ post.excerpt | strip_html | truncate: 120 }}</p>
      </article>
      {% endfor %}
    </div>
    <a href="{{ '/blog/' | relative_url }}" class="btn">View All Blog Posts</a>
  </div>
</section>

<section class="projects">
  <div class="container">
    <h2>Projects</h2>
    <div class="project-grid">
      {% for project in site.projects limit:2 %}
      <article class="project-preview">
        <h3>{{ project.title }}</h3>
        <p>{{ project.excerpt | strip_html | truncate: 120 }}</p>
      </article>
      {% endfor %}
    </div>
    <a href="{{ '/projects/' | relative_url }}" class="btn">View All Projects</a>
  </div>
</section>

<section class="writeups">
  <div class="container">
    <h2>Latest Writeups</h2>
    <div class="writeup-grid">
      {% for writeup in site.writeups limit:2 %}
      <article class="writeup-preview">
        <h3>{{ writeup.title }}</h3>
        <p>{{ writeup.excerpt | strip_html | truncate: 120 }}</p>
      </article>
      {% endfor %}
    </div>
    <a href="{{ '/writeups/' | relative_url }}" class="btn">View All Writeups</a>
  </div>
</section>
