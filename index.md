<link rel="stylesheet" href="/assets/css/style.css">

---
layout: home
title: "Welcome to My Cybersecurity Blog"
---

<section class="hero">
  <div class="container">
    <h1>BytePolarBear's Cybersecurity Blog</h1>
    <p>Exploring the world of ethical hacking, reverse engineering, and digital forensics. Sharing insights, tutorials, and practical experiences.</p>
    <img src="/assets/images/cybersecurity-image.jpg" alt="Cybersecurity Landscape" class="hero-image">
  </div>
</section>

<section class="about">
  <div class="container">
    <h2>About Me</h2>
    <div class="profile-wrapper">
      <img src="/assets/images/my-photo.jpg" alt="My Photo" class="profile-image">
      <p>Hi, I'm [Your Name]!  I’m a passionate cybersecurity enthusiast with a focus on reverse engineering and vulnerability research. This blog is my way of documenting my learning journey and sharing what I discover along the way.</p>
    </div>
  </div>
</section>

<section class="featured-posts">
  <div class="container">
    <h2>Featured Posts</h2>
    <ul>
      {% for post in site.posts limit:3 %}
        <li>
          <article class="post-preview">
            <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
            <p>{{ post.content | truncate: 150 }}</p>  <!-- Truncate content for preview -->
            <a href="{{ post.url }}" class="read-more">Read More →</a>
          </article>
        </li>
      {% endfor %}
    </ul>
  </div>
</section>

<section class="contact">
  <div class="container">
    <h2>Connect With Me</h2>
    <p>Feel free to reach out with questions, feedback, or collaboration opportunities!</p>
    <ul>
      <li><a href="#">LinkedIn</a></li>
      <li><a href="#">GitHub</a></li>
      <li><a href="#">Twitter</a></li>
    </ul>
  </div>
</section>
