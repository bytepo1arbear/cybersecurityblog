---
layout: default
title: "Threat Feeds"
permalink: /threats/
---

<section class="page-hero">
  <div class="container">
    <h1>Threat Feeds</h1>
    <p class="page-subtitle">A defensive cyber security page curated from open-source threat intelligence and reputable community feeds.</p>
  </div>
</section>

<section class="threat-feed-section">
  <div class="container">
    <div class="dashboard-grid">
      <div class="dashboard-panel">
        <h2><i class="fas fa-shield-alt"></i> Defense Focus</h2>
        <p>Monitor active cyber threats, vulnerability disclosures, and detection guidance from trusted open-source feeds. These sources help align defensive posture with current attacker tactics.</p>
      </div>
      <div class="dashboard-panel">
        <h2><i class="fas fa-bolt"></i> Offensive Awareness</h2>
        <p>Understand attacker behavior by following proven threat reports and malware activity. Offensive insight improves detection engineering and incident response readiness.</p>
      </div>
      <div class="dashboard-panel">
        <h2><i class="fas fa-network-wired"></i> Threat Intelligence</h2>
        <p>Feeds include CVE alerts, malware families, phishing campaigns, and suspicious infrastructure. Use this page as a starting point for situational awareness and research.</p>
      </div>
    </div>

    <div class="threat-feed-list">
      <article class="feed-card">
        <h3>Abuse.ch - MalwareBazaar</h3>
        <p>MalwareBazaar collects and shares malware samples and IOCs from the community, focusing on current malware families and campaigns.</p>
        <ul>
          <li>Focus: Malware sample distribution</li>
          <li>Use for: Detection engineering, threat hunting</li>
          <li>Feed: <a href="https://bazaar.abuse.ch/export/" target="_blank" rel="noopener">bazaar.abuse.ch/export/</a></li>
        </ul>
      </article>

      <article class="feed-card">
        <h3>US-CERT / CISA Known Exploited Vulnerabilities</h3>
        <p>Official list of vulnerabilities actively exploited in the wild. These prioritized CVEs are essential for patch management and critical risk reduction.</p>
        <ul>
          <li>Focus: Exploited CVEs</li>
          <li>Use for: defensive patch prioritization</li>
          <li>Feed: <a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog" target="_blank" rel="noopener">cisa.gov/known-exploited-vulnerabilities-catalog</a></li>
        </ul>
      </article>

      <article class="feed-card">
        <h3>MISP Project</h3>
        <p>Open-source threat intelligence platform for sharing IOCs, adversary techniques, and campaign metadata across trusted communities.</p>
        <ul>
          <li>Focus: Community-shared threat intelligence</li>
          <li>Use for: IOC ingestion and threat modeling</li>
          <li>Feed: <a href="https://www.misp-project.org/" target="_blank" rel="noopener">misp-project.org</a></li>
        </ul>
      </article>

      <article class="feed-card">
        <h3>AlienVault OTX</h3>
        <p>Open Threat Exchange provides collaborative threat data including malicious IPs, domains, URLs, and file hashes from a global user base.</p>
        <ul>
          <li>Focus: Community-sourced indicators</li>
          <li>Use for: threat hunting and detection rule development</li>
          <li>Feed: <a href="https://otx.alienvault.com/" target="_blank" rel="noopener">otx.alienvault.com</a></li>
        </ul>
      </article>

      <article class="feed-card">
        <h3>VirusTotal Intelligence</h3>
        <p>Aggregated malware and phishing telemetry from crowdsourced uploads and security vendors. Use it to correlate suspicious samples and domains.</p>
        <ul>
          <li>Focus: Malware/phishing telemetry</li>
          <li>Use for: IOC validation and adversary tracking</li>
          <li>Feed: <a href="https://www.virustotal.com/" target="_blank" rel="noopener">virustotal.com</a></li>
        </ul>
      </article>

      <article class="feed-card">
        <h3>Tenable / Qualys Vulnerability Alerts</h3>
        <p>Vendor-sourced vulnerability intelligence and exploit coverage. Good for comparing vulnerability findings against known active exploitation data.</p>
        <ul>
          <li>Focus: Vulnerability research and alerts</li>
          <li>Use for: vulnerability management and risk assessment</li>
          <li>Feed: <a href="https://www.tenable.com/blog" target="_blank" rel="noopener">tenable.com/blog</a></li>
        </ul>
      </article>
    </div>

    <div class="feed-sources">
      <h3>Open-Source Threat Intelligence Sources</h3>
      <ul>
        <li><strong>Abuse.ch</strong> — open malware sample feeds and botnet tracking.</li>
        <li><strong>CISA</strong> — official exploited vulnerability catalog and alerts.</li>
        <li><strong>MISP</strong> — community threat sharing for IOCs and campaigns.</li>
        <li><strong>OTX</strong> — global collaborative indicator exchange.</li>
        <li><strong>VirusTotal</strong> — file, URL, and domain threat analysis.</li>
        <li><strong>Tenable/Qualys</strong> — vulnerability intelligence and research.</li>
      </ul>
    </div>
  </div>
</section>
