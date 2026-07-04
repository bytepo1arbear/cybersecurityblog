---
layout: default
title: "Threat Intel"
permalink: /threat-intel/
sources:
  - name: "Abuse.ch MalwareBazaar"
    category: "Malware Intelligence"
    details: "Community-driven malware sample repository and IOC feed for emerging malware families."
  - name: "CISA Known Exploited Vulnerabilities"
    category: "Vulnerability Intelligence"
    details: "Official list of vulnerabilities observed in active exploitation campaigns."
  - name: "AlienVault OTX"
    category: "Indicator Sharing"
    details: "Collaborative threat feed sharing malicious IPs, domains, URLs, and file hashes." 
---

<section class="page-hero">
  <div class="container">
    <h1>Threat Intelligence</h1>
    <p class="page-subtitle">Consolidated threat feed summary and source overview for defensive analysis.</p>
  </div>
</section>

<div class="container threat-board">
  <article class="threat-panel">
    <h2>Threat Feed Summary</h2>
    <div class="ioc-matrix">
      <table>
        <thead>
          <tr>
            <th>Source</th>
            <th>Type</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {% for source in page.sources %}
          <tr>
            <td>{{ source.name }}</td>
            <td>{{ source.category }}</td>
            <td>{{ source.details }}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
    <p class="threat-note">This page pulls together the selected intelligence sources into a concise operational summary for incident response and threat hunting.</p>
  </article>

  <article class="threat-panel">
    <h2>Threat Intelligence Sources</h2>
    <ul class="source-list">
      {% for source in page.sources %}
      <li><strong>{{ source.name }}</strong> — {{ source.category }}</li>
      {% endfor %}
    </ul>
  </article>

  <article class="threat-panel">
    <h2>Latest Feed Items</h2>
    <!-- NOTE: Threat feed data is refreshed daily by a scheduled GitHub Action that writes to `_data/threats.yml`. -->
    {% if site.data.threats and site.data.threats.items and site.data.threats.items.size > 0 %}
    <div class="ioc-matrix">
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Source</th>
            <th>Title</th>
            <th>Summary</th>
          </tr>
        </thead>
        <tbody>
          {% for item in site.data.threats.items limit:30 %}
          <tr>
            <td>{{ item.published | default: site.data.threats.last_updated }}</td>
            <td>{{ item.source }}</td>
            <td><a href="{{ item.link }}" target="_blank" rel="noopener">{{ item.title }}</a></td>
            <td>{{ item.summary | strip_html | truncate: 180 }}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
    <p class="threat-note">Showing the most recent items aggregated from configured sources. Last updated: {{ site.data.threats.last_updated }}</p>
    {% else %}
    <p class="threat-note">Threat feed data is not yet available. The site will show live updates after the scheduled fetch runs. You can also trigger the update manually via GitHub Actions.</p>
    {% endif %}
  </article>
</div>
