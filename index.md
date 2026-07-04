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
    <article class="widget-card primary mission-card">
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
          {% for item in site.data.threats.items limit:4 %}
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
    <h2><i class="fas fa-chart-line"></i> Quick-Stats</h2>
    <div class="stats-board">
      <div class="stats-card">
        <strong>{{ site.writeups | size }}</strong>
        <span>Writeups</span>
        <div class="stat-graph">
          <div class="stat-bar" style="--fill: 70%"></div>
          <div class="stat-bar" style="--fill: 55%"></div>
          <div class="stat-bar" style="--fill: 80%"></div>
          <div class="stat-bar" style="--fill: 65%"></div>
          <div class="stat-bar" style="--fill: 90%"></div>
        </div>
        <div class="stat-meta">
          <span><i class="fas fa-arrow-up trend-up"></i> +12% month</span>
          <span><i class="fas fa-check-circle"></i> Active</span>
        </div>
      </div>
      <div class="stats-card">
        <strong>2</strong>
        <span>Certifications</span>
        <div class="stat-graph">
          <div class="stat-bar" style="--fill: 35%"></div>
          <div class="stat-bar" style="--fill: 45%"></div>
          <div class="stat-bar" style="--fill: 55%"></div>
          <div class="stat-bar" style="--fill: 60%"></div>
          <div class="stat-bar" style="--fill: 70%"></div>
        </div>
        <div class="stat-meta">
          <span><i class="fas fa-star"></i> Learning</span>
          <span><i class="fas fa-arrow-up trend-up"></i> +1 this quarter</span>
        </div>
      </div>
      <div class="stats-card">
        <strong>{% if site.data.threats and site.data.threats.items %}{{ site.data.threats.items | size }}{% else %}0{% endif %}</strong>
        <span>Threat Items</span>
        <div class="stat-graph">
          <div class="stat-bar" style="--fill: 85%"></div>
          <div class="stat-bar" style="--fill: 90%"></div>
          <div class="stat-bar" style="--fill: 78%"></div>
          <div class="stat-bar" style="--fill: 93%"></div>
          <div class="stat-bar" style="--fill: 88%"></div>
        </div>
        <div class="stat-meta">
          <span><i class="fas fa-bolt"></i> Real-time</span>
          <span><i class="fas fa-arrow-down trend-down"></i> -5% false positives</span>
        </div>
      </div>
      <div class="stats-card">
        <strong>{{ site.posts | size }}</strong>
        <span>Blog Posts</span>
        <div class="stat-graph">
          <div class="stat-bar" style="--fill: 60%"></div>
          <div class="stat-bar" style="--fill: 70%"></div>
          <div class="stat-bar" style="--fill: 55%"></div>
          <div class="stat-bar" style="--fill: 75%"></div>
          <div class="stat-bar" style="--fill: 80%"></div>
        </div>
        <div class="stat-meta">
          <span><i class="fas fa-pencil-alt"></i> Published</span>
          <span><i class="fas fa-arrow-up trend-up"></i> +20% views</span>
        </div>
      </div>
      <div class="stats-card">
        <strong>{{ site.projects | size }}</strong>
        <span>Projects</span>
        <div class="stat-graph">
          <div class="stat-bar" style="--fill: 50%"></div>
          <div class="stat-bar" style="--fill: 65%"></div>
          <div class="stat-bar" style="--fill: 70%"></div>
          <div class="stat-bar" style="--fill: 80%"></div>
          <div class="stat-bar" style="--fill: 85%"></div>
        </div>
        <div class="stat-meta">
          <span><i class="fas fa-network-wired"></i> Infrastructure</span>
          <span><i class="fas fa-arrow-up trend-up"></i> +3 active</span>
        </div>
      </div>
    </div>
  </article>
</div>
