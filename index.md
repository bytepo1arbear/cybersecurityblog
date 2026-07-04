---
layout: default
title: Home
permalink: /
---

<section class="page-hero">
  <div class="container">
    <h1>SOC Analyst Dashboard</h1>
    <p class="page-subtitle">Operationalizing a Blue Team posture with tactical alerting, SIEM coverage, and offensive-aware risk intelligence.</p>
  </div>
</section>

<div class="container dashboard-grid">
  <div class="widget-stack">
    <article class="widget-card primary">
      <h2>Mission Statement & Career Objective</h2>
      <p>Enable enterprise detection and response through continuous monitoring, log-driven investigations, and rapid incident validation. Build Blue Team skills while leveraging offensive security context for more effective defenses.</p>
      <ul style="list-style:none; padding-left:0; margin-top:1rem; display:grid; gap:0.8rem; color: var(--text-secondary);">
        <li>Targeting SOC L1 / Blue Team readiness and security operations execution.</li>
        <li>Prioritizing attack surface reduction, alert accuracy, and adversary-informed defense.</li>
        <li>Supporting career growth with hands-on analysis, threat hunting, and response workflows.</li>
      </ul>
    </article>

    <article class="widget-card secondary">
      <h2>Latest Defensive Alerts</h2>
      <div class="alert-list">
        {% if site.data.threats and site.data.threats.items and site.data.threats.items.size > 0 %}
          {% for item in site.data.threats.items limit:3 %}
          <div class="alert-item">
            <h3>{{ item.title }}</h3>
            <p>{{ item.summary | strip_html | truncate: 18 }}</p>
            <div style="margin-top:0.75rem;text-align:right;"><a class="btn-small" href="{{ item.link }}" target="_blank" rel="noopener">Source</a></div>
          </div>
          {% endfor %}
        {% else %}
          <p class="threat-note">No recent feed items yet. The feed updates daily.</p>
        {% endif %}
      </div>
    </article>
  </div>

  <article class="widget-card tertiary">
    <h2>Quick-Stats</h2>
    <div class="stats-board">
      <div class="stats-card">
        <strong>{{ site.posts | size }}</strong>
        <span>Rooms Cleared</span>
      </div>
      <div class="stats-card">
        <strong>12</strong>
        <span>Labs Deployed</span>
      </div>
      <div class="stats-card">
        <strong>34</strong>
        <span>SIEM Rules Configured</span>
      </div>
    </div>
  </article>
</div>
