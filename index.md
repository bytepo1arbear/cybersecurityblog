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
    <h2>Latest Blog Post</h2>
    {% for post in site.posts limit:1 %}
    <article class="featured-post">
      <div class="featured-post-header">
        <span class="post-date">{{ post.date | date: "%B %d, %Y" }}</span>
        {% if post.category %}
        <span class="post-category">{{ post.category }}</span>
        {% endif %}
      </div>
      <h3>{{ post.title }}</h3>
      <div class="post-excerpt">
        {{ post.content | strip_html | truncatewords: 60 }}
      </div>
      {% if post.tags %}
      <div class="post-tags">
        {% for tag in post.tags %}
        <span class="tag">{{ tag }}</span>
        {% endfor %}
      </div>
      {% endif %}
      <a href="{{ post.url | relative_url }}" class="btn-read-more">Read Full Post →</a>
    </article>
    {% else %}
    <div class="empty-state">
      <p>No blog posts yet. Check back soon!</p>
    </div>
    {% endfor %}
    <div class="section-footer">
      <a href="{{ '/blog/' | relative_url }}" class="btn">View All Blog Posts</a>
    </div>
  </div>
</section>

<section class="projects">
  <div class="container">
    <h2>Latest Projects</h2>
    <div class="project-grid">
      {% assign visible_projects = site.projects | where_exp: "item", "item.exclude_from_collection != true" %}
      {% for project in site.projects limit:3 %}
      <article class="project-preview">
        <div class="card-header">
          <span class="post-date">{{ project.date | date: "%B %Y" }}</span>
        </div>
        <h3>{{ project.title }}</h3>
        <p>{{ project.excerpt | strip_html | truncatewords: 50 }}</p>
        <a href="{{ project.url | relative_url }}" class="btn-read-more">View Project →</a>
      </article>
      {% else %}
      <div class="empty-state">
        <p>No projects yet. Coming soon!</p>
      </div>
      {% endfor %}
    </div>
    <div class="section-footer">
      <a href="{{ '/projects/' | relative_url }}" class="btn">View All Projects</a>
    </div>
  </div>
</section>

<section class="writeups">
  <div class="container">
    <h2>Latest Writeup</h2>
    <div class="writeup-grid">
      {% assign visible_projects = site.projects | where_exp: "item", "item.exclude_from_collection != true" %}
      {% for writeup in site.writeups limit:3 %}
      <article class="writeup-preview featured">
        <div class="card-header">
          <span class="post-date">{{ writeup.date | date: "%B %d, %Y" }}</span>
          {% if writeup.difficulty %}
          <span class="difficulty difficulty-{{ writeup.difficulty | downcase }}">{{ writeup.difficulty }}</span>
          {% endif %}
        </div>
        <h3>{{ writeup.title }}</h3>
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
      {% else %}
      <div class="empty-state">
        <p>No writeups yet. Stay tuned!</p>
      </div>
      {% endfor %}
    </div>
    <div class="section-footer">
      <a href="{{ '/writeups/' | relative_url }}" class="btn">View All Writeups</a>
    </div>
  </div>
</section>
