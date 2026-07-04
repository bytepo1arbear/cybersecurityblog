---
layout: default
title: "Threat Intel"
permalink: /threat-intel/
---

<section class="page-hero">
  <div class="container">
    <h1>Threat Intelligence</h1>
    <p class="page-subtitle">A dedicated dashboard for tracking phishing campaigns and IOC data relevant to blue team operations.</p>
  </div>
</section>

<div class="container threat-board">
  <article class="threat-panel">
    <h2>Live Phishing Campaign Tracker</h2>
    <div class="phishing-tracker">
      <div class="phishing-row">
        <div><strong>Campaign:</strong> Cloud Credential Harvest</div>
        <div><span class="severity-pill severity-medium">Medium</span></div>
      </div>
      <div class="phishing-row">
        <div><strong>Target:</strong> Enterprise SaaS Users</div>
        <div><strong>Stage:</strong> Credential Capture</div>
      </div>
      <div class="phishing-row">
        <div><strong>Indicators:</strong> suspicious login forms, forged headers, redirect domains.</div>
        <div><a href="https://otx.alienvault.com/" target="_blank" rel="noopener">View Feed</a></div>
      </div>
      <p class="threat-note">This tracker is a placeholder UI for SOC analysts to monitor phishing campaign behavior and validate email filtering controls.</p>
    </div>
  </article>

  <article class="threat-panel">
    <h2>IOC Matrix Table</h2>
    <div class="ioc-matrix">
      <table>
        <thead>
          <tr>
            <th>Indicator</th>
            <th>Type</th>
            <th>Severity</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>192.168.100.77</td>
            <td>IP</td>
            <td><span class="severity-pill severity-high">High</span></td>
            <td>Detected C2 host associated with credential stuffing operations.</td>
          </tr>
          <tr>
            <td>malicious.example.com</td>
            <td>Domain</td>
            <td><span class="severity-pill severity-medium">Medium</span></td>
            <td>Phishing landing page used in recent BEC campaigns.</td>
          </tr>
          <tr>
            <td>e3b0c44298fc1c14</td>
            <td>Hash</td>
            <td><span class="severity-pill severity-high">High</span></td>
            <td>Malware sample observed during endpoint compromise testing.</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p class="threat-note">Use the IOC matrix to prioritize detection coverage and correlate artifacts across sensors.</p>
  </article>
</div>
