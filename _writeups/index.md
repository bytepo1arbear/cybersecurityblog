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
  <article class="platform-card thm">
    <h3>TryHackMe (THM)</h3>
    <p>Targeted lessons and blue team challenges with a focus on defensive control implementation and adversary learning.</p>
    <div class="platform-meta">
      <span><strong>Difficulty:</strong> Medium / Hard</span>
      <span><strong>OS:</strong> Linux / Windows</span>
      <span><strong>Concepts:</strong> Privilege Escalation, Log Analysis, Alert Triage</span>
    </div>
  </article>
  <article class="platform-card htb">
    <h3>HackTheBox (HTB)</h3>
    <p>Professional machine writeups documenting attacker techniques, post-exploitation, and detection validation.</p>
    <div class="platform-meta">
      <span><strong>Difficulty:</strong> Pro / Insane</span>
      <span><strong>OS:</strong> Linux / Windows</span>
      <span><strong>Concepts:</strong> Network Exploitation, Persistence, Evasion</span>
    </div>
  </article>
</div>

<section class="timeline-section container">
  <div class="timeline">
    {% assign writeup_posts = site.writeups | sort: 'date' | reverse %}
    {% for writeup in writeup_posts %}
    <div class="timeline-node">
      <div class="timeline-marker"></div>
      <div class="timeline-card">
        <span class="timeline-meta">{{ writeup.date | date: "%b %d, %Y" }}</span>
        <h3><a href="{{ writeup.url | relative_url }}">{{ writeup.title }}</a></h3>
        <p>{{ writeup.excerpt | strip_html | truncatewords: 24 }}</p>
      </div>
    </div>
    {% endfor %}
  </div>
</section>
