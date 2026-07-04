---
layout: default
title: "Writeups"
permalink: /writeups/
exclude_from_collection: true
---

<section class="page-hero">
  <div class="container">
    <h1>Writeups</h1>
    <p class="page-subtitle">Capture the Flag solutions, lab findings, and incident-style analysis.</p>
  </div>
</section>

<div class="container platform-grid">
  {% assign all_writeups = site.writeups | sort: 'date' | reverse %}
  {% assign thm_posts = all_writeups | where_exp: "w", "w.platform == 'TryHackMe' or w.tags contains 'TryHackMe' or w.tags contains 'thm' or w.tags contains 'THM'" %}
  {% assign htb_posts = all_writeups | where_exp: "w", "w.platform == 'HackTheBox' or w.tags contains 'htb' or w.tags contains 'HTB' or w.tags contains 'HackTheBox'" %}
  <article class="platform-card thm">
    <h3>TryHackMe (THM)</h3>
    <p>Targeted lessons and blue team challenges with a focus on defensive control implementation and adversary learning.</p>
    <div class="platform-meta">
      <span><strong>Difficulty:</strong> Medium / Hard</span>
      <span><strong>OS:</strong> Linux / Windows</span>
      <span><strong>Concepts:</strong> Privilege Escalation, Log Analysis, Alert Triage</span>
    </div>
    <div class="platform-count">Completed writeups: <strong>{{ thm_posts | size }}</strong></div>
  </article>
  <article class="platform-card htb">
    <h3>HackTheBox (HTB)</h3>
    <p>Professional machine writeups documenting attacker techniques, post-exploitation, and detection validation.</p>
    <div class="platform-meta">
      <span><strong>Difficulty:</strong> Pro / Insane</span>
      <span><strong>OS:</strong> Linux / Windows</span>
      <span><strong>Concepts:</strong> Network Exploitation, Persistence, Evasion</span>
    </div>
    <div class="platform-count">Completed writeups: <strong>{{ htb_posts | size }}</strong></div>
  </article>
</div>
<section class="timeline-section container">
  {% assign all_writeups = site.writeups | sort: 'date' | reverse %}
  {% assign thm_posts = all_writeups | where_exp: "w", "w.platform == 'TryHackMe' or w.tags contains 'TryHackMe' or w.tags contains 'thm' or w.tags contains 'THM'" %}
  {% assign htb_posts = all_writeups | where_exp: "w", "w.platform == 'HackTheBox' or w.tags contains 'htb' or w.tags contains 'HTB' or w.tags contains 'HackTheBox'" %}

  <div class="writeup-columns">
    <div>
      <h3 style="margin-bottom:1rem;">TryHackMe Writeups</h3>
      {% if thm_posts and thm_posts.size > 0 %}
      {% for w in thm_posts %}
      <div class="writeup-card">
        <div style="display:flex;justify-content:space-between;align-items:center;gap:1rem;">
          <h4 style="margin:0;"><a href="{{ w.url | relative_url }}">{{ w.title }}</a></h4>
          <span class="post-date">{{ w.date | date: "%b %d, %Y" }}</span>
        </div>
        <p style="margin:0;color:var(--text-secondary);">{{ w.excerpt | strip_html | truncatewords: 28 }}</p>
        <div style="margin-top:auto;text-align:right;"><a class="btn-small" href="{{ w.url | relative_url }}">Read</a></div>
      </div>
      {% endfor %}
      {% else %}
        <p class="empty-state">No TryHackMe writeups found yet.</p>
      {% endif %}
    </div>

    <div>
      <h3 style="margin-bottom:1rem;">HackTheBox Writeups</h3>
      {% if htb_posts and htb_posts.size > 0 %}
      {% for w in htb_posts %}
      <div class="writeup-card">
        <div style="display:flex;justify-content:space-between;align-items:center;gap:1rem;">
          <h4 style="margin:0;"><a href="{{ w.url | relative_url }}">{{ w.title }}</a></h4>
          <span class="post-date">{{ w.date | date: "%b %d, %Y" }}</span>
        </div>
        <p style="margin:0;color:var(--text-secondary);">{{ w.excerpt | strip_html | truncatewords: 28 }}</p>
        <div style="margin-top:auto;text-align:right;"><a class="btn-small" href="{{ w.url | relative_url }}">Read</a></div>
      </div>
      {% endfor %}
      {% else %}
        <p class="empty-state">No HackTheBox writeups found yet.</p>
      {% endif %}
    </div>
  </div>
</section>
