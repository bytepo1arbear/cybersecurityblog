---
layout: default
title: Home
permalink: /
---

<section class="mb-8 rounded-2xl border border-slate-800 bg-slate-950/90 p-5 shadow-glow sm:p-7 lg:p-8">
  <div class="mx-auto max-w-6xl">
    <div class="flex min-h-[280px] flex-col justify-between gap-6">
      <div class="mx-auto max-w-3xl text-center">
        <div class="mb-4 inline-flex items-center gap-2 rounded-full border border-sky-500/30 bg-sky-500/10 px-3 py-1 text-[10px] font-semibold uppercase tracking-[0.22em] text-sky-300">
          <span class="h-2 w-2 rounded-full bg-emerald-400 status-dot"></span>
          Active Monitoring
        </div>
        <h1 class="text-4xl font-black tracking-tight text-white sm:text-5xl lg:text-6xl">Jack Diamond</h1>
        <p class="mt-3 text-lg font-medium text-sky-300">SOC L1 Analyst / Junior Detection Analyst</p>
      </div>

      <div class="mx-auto w-full max-w-4xl rounded-2xl border border-sky-500/20 bg-gradient-to-r from-slate-900/80 via-slate-900/75 to-slate-900/80 p-5 text-center shadow-inner shadow-sky-950/30">
        <p class="text-base leading-7 text-slate-200">
          I support a modern SOC by triaging alerts, validating telemetry, investigating suspicious behavior, and helping turn noisy signals into actionable security outcomes.
          My focus is on SIEM workflows, log analysis, detection engineering, and hands-on lab validation for real-world cyber defense practices.
        </p>
      </div>

      <div class="flex flex-wrap items-center justify-end gap-3 text-sm text-slate-300">
        <a href="https://github.com/bytepo1arbear" target="_blank" rel="noopener" class="rounded-full border border-slate-700 bg-slate-900/80 px-3 py-2 transition hover:border-sky-400 hover:text-sky-300">GitHub</a>
        <a href="https://www.linkedin.com" target="_blank" rel="noopener" class="rounded-full border border-slate-700 bg-slate-900/80 px-3 py-2 transition hover:border-sky-400 hover:text-sky-300">LinkedIn</a>
        <a href="https://www.credly.com/users/jackthepolarbear" target="_blank" rel="noopener" class="rounded-full border border-slate-700 bg-slate-900/80 px-3 py-2 transition hover:border-sky-400 hover:text-sky-300">Credly</a>
        <a href="{{ '/about/' | relative_url }}" class="rounded-full border border-slate-700 bg-slate-900/80 px-3 py-2 transition hover:border-sky-400 hover:text-sky-300">About Me</a>
      </div>
    </div>
  </div>
</section>

<section class="mb-8 grid gap-5 lg:grid-cols-[1.55fr_0.95fr] lg:items-start">
  <div class="rounded-2xl border border-slate-800 bg-slate-900/80 p-5 panel-glow">
    <div class="mb-4 flex items-center justify-between">
      <h2 class="text-xl font-semibold text-white">Case Files</h2>
      <span class="rounded-full border border-slate-700 px-2.5 py-1 text-[10px] font-semibold uppercase tracking-[0.2em] text-slate-400">Top Findings</span>
    </div>

    {% assign case_files = site.writeups | where_exp: "item", "item.path != '_writeups/index.md' and item.platform != 'Home Lab'" | sort: 'date' | reverse %}
    <div class="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
      {% for item in case_files limit:6 %}
        {% assign severity = item.difficulty | default: 'Medium' %}

        {% assign badge_class = 'bg-sky-500/10 text-sky-300 border-sky-500/30' %}
        {% case severity %}
          {% when 'Critical' %}{% assign badge_class = 'bg-rose-500/10 text-rose-300 border-rose-500/30' %}
          {% when 'High' %}{% assign badge_class = 'bg-amber-500/10 text-amber-300 border-amber-500/30' %}
          {% when 'Operational' %}{% assign badge_class = 'bg-emerald-500/10 text-emerald-300 border-emerald-500/30' %}
          {% when 'Beginner' %}{% assign badge_class = 'bg-emerald-500/10 text-emerald-300 border-emerald-500/30' %}
          {% when 'Intermediate' %}{% assign badge_class = 'bg-sky-500/10 text-sky-300 border-sky-500/30' %}
        {% endcase %}

        <article class="rounded-xl border border-slate-800 bg-slate-950/70 p-4 transition hover:-translate-y-1 hover:border-sky-500/40">
          <div class="mb-4 flex items-center justify-between gap-3">
            <span class="inline-flex rounded-full border px-2 py-1 text-[10px] font-semibold uppercase tracking-[0.18em] {{ badge_class }}">{{ severity }}</span>
            <span class="text-[10px] uppercase tracking-[0.2em] text-slate-500">{{ item.date | date: '%b %d, %Y' }}</span>
          </div>

          <h3 class="text-lg font-semibold text-white">{{ item.title }}</h3>
          <p class="mt-3 text-sm leading-6 text-slate-400">{{ item.excerpt | default: item.description | strip_html | truncate: 120 }}</p>

          <div class="mt-4 flex flex-wrap gap-2">
            {% for tag in item.tags limit:3 %}
              {% assign tool = tag | downcase %}
              {% case tool %}
                {% when 'wireshark' %}{% assign label = 'Wireshark' %}
                {% when 'splunk' %}{% assign label = 'Splunk' %}
                {% when 'sysmon' %}{% assign label = 'Sysmon' %}
                {% when 'linux' %}{% assign label = 'Linux' %}
                {% when 'network' %}{% assign label = 'Network' %}
                {% when 'detection' %}{% assign label = 'Detection' %}
                {% when 'windows' %}{% assign label = 'Windows' %}
                {% when 'homelab' %}{% assign label = 'Homelab' %}
                {% when 'pentesting' %}{% assign label = 'Pentest' %}
                {% else %}{% assign label = tag | capitalize %}
              {% endcase %}
              <span class="rounded-md border border-slate-700 bg-slate-900 px-2 py-1 font-mono text-[10px] uppercase tracking-[0.12em] text-sky-200">[{{ label }}]</span>
            {% endfor %}
          </div>

          <a href="{{ item.url | relative_url }}" class="mt-5 inline-flex items-center gap-2 text-sm font-medium text-sky-300 transition hover:text-sky-200">Open case file <i class="fa-solid fa-arrow-right"></i></a>
        </article>
      {% endfor %}
    </div>
  </div>

  <div class="space-y-5">
    <div class="rounded-2xl border border-slate-800 bg-slate-900/80 p-4 panel-glow">
      <h2 class="text-xl font-semibold text-white">Operational Snapshot</h2>
      <div class="mt-4 space-y-3">
        <div class="rounded-xl border border-slate-800 bg-slate-950/70 p-3.5">
          <div class="flex items-center justify-between text-sm text-slate-400">
            <span>Threat triage</span>
            <span class="text-emerald-300">92%</span>
          </div>
          <div class="mt-2.5 h-2.5 rounded-full bg-slate-800">
            <div class="h-2.5 w-[92%] rounded-full bg-emerald-400"></div>
          </div>
        </div>

        <div class="rounded-xl border border-slate-800 bg-slate-950/70 p-3.5">
          <div class="flex items-center justify-between text-sm text-slate-400">
            <span>Log coverage</span>
            <span class="text-sky-300">84%</span>
          </div>
          <div class="mt-2.5 h-2.5 rounded-full bg-slate-800">
            <div class="h-2.5 w-[84%] rounded-full bg-sky-400"></div>
          </div>
        </div>

        <div class="rounded-xl border border-slate-800 bg-slate-950/70 p-3.5">
          <div class="flex items-center justify-between text-sm text-slate-400">
            <span>Detection tuning</span>
            <span class="text-violet-300">76%</span>
          </div>
          <div class="mt-2.5 h-2.5 rounded-full bg-slate-800">
            <div class="h-2.5 w-[76%] rounded-full bg-violet-400"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="rounded-2xl border border-slate-800 bg-slate-900/80 p-4 panel-glow">
      <h2 class="text-xl font-semibold text-white">Certifications</h2>
      <div class="mt-4 space-y-3">
        <div class="rounded-xl border border-slate-800 bg-slate-950/70 p-4">
          <div class="flex items-center justify-between gap-3">
            <span class="font-medium text-white">CompTIA Security+</span>
            <span class="text-emerald-300">Completed</span>
          </div>
        </div>
        <div class="rounded-xl border border-slate-800 bg-slate-950/70 p-4">
          <div class="flex items-center justify-between gap-3">
            <span class="font-medium text-white">CompTIA Network+</span>
            <span class="text-sky-300">Completed</span>
          </div>
        </div>
        <div class="rounded-xl border border-slate-800 bg-slate-950/70 p-4">
          <div class="flex items-center justify-between gap-3">
            <span class="font-medium text-white">THM SEC1 Certification</span>
            <span class="text-violet-300">Completed</span>
          </div>
        </div>
        <div class="rounded-xl border border-slate-800 bg-slate-950/70 p-4">
          <div class="flex items-center justify-between gap-3">
            <span class="font-medium text-white">SAL1 Certification (SOC L1)</span>
            <span class="text-amber-300">In Progress</span>
          </div>
        </div>
      </div>
    </div>

    <div class="rounded-2xl border border-slate-800 bg-slate-900/80 p-5 pb-10 panel-glow">
      <h2 class="text-xl font-semibold text-white">Core Areas</h2>
      <ul class="mt-4 space-y-2 text-sm text-slate-300">
        <li>• SIEM and log validation</li>
        <li>• Network traffic analysis</li>
        <li>• Detection engineering</li>
        <li>• Offensive and defensive testing</li>
      </ul>
    </div>
  </div>
</section>

<section class="mb-8 rounded-2xl border border-slate-800 bg-slate-900/80 p-5 text-center panel-glow">
  <div class="mb-4 flex flex-col items-center justify-center gap-3 sm:flex-row sm:justify-between sm:text-left">
    <div class="mx-auto sm:mx-0">
      <p class="text-xs uppercase tracking-[0.22em] text-sky-300">Project Spotlight</p>
      <h2 class="mt-2 text-2xl font-semibold text-white">Cyber Security Home Lab</h2>
    </div>
    <a href="{{ '/projects/' | relative_url }}" class="inline-flex items-center justify-center rounded-full border border-sky-500/30 bg-sky-500/10 px-3 py-1.5 text-xs font-semibold uppercase tracking-[0.18em] text-sky-200 transition hover:border-sky-400 hover:text-sky-100">View Projects</a>
  </div>

  <p class="mx-auto max-w-2xl text-slate-300">
    My primary lab environment is built for detection engineering, blue-team validation, and offensive tooling evaluation. It runs on Proxmox and includes Wazuh, Caldera, TheHive, Kali Linux, DVWA, BWAPP, Nessus, and other security-focused workloads.
  </p>

  <div class="mt-5 flex flex-wrap justify-center gap-2">
    <span class="rounded-full border border-slate-700 bg-slate-950 px-2 py-1 text-[10px] uppercase tracking-[0.14em] text-sky-200">Proxmox</span>
    <span class="rounded-full border border-slate-700 bg-slate-950 px-2 py-1 text-[10px] uppercase tracking-[0.14em] text-sky-200">Wazuh</span>
    <span class="rounded-full border border-slate-700 bg-slate-950 px-2 py-1 text-[10px] uppercase tracking-[0.14em] text-sky-200">Caldera</span>
    <span class="rounded-full border border-slate-700 bg-slate-950 px-2 py-1 text-[10px] uppercase tracking-[0.14em] text-sky-200">Kali</span>
    <span class="rounded-full border border-slate-700 bg-slate-950 px-2 py-1 text-[10px] uppercase tracking-[0.14em] text-sky-200">TheHive</span>
  </div>
</section>

<section class="mb-8 grid gap-5 lg:grid-cols-4">
  <div class="rounded-2xl border border-slate-800 bg-slate-900/80 p-4 panel-glow">
    <p class="text-xs uppercase tracking-[0.22em] text-sky-300">SIEM & Logs</p>
    <ul class="mt-4 space-y-3 text-sm text-slate-300">
      <li>Splunk / SIEM triage</li>
      <li>Windows event logs</li>
      <li>Sysmon telemetry</li>
      <li>PowerShell hunting</li>
    </ul>
  </div>

  <div class="rounded-2xl border border-slate-800 bg-slate-900/80 p-5 panel-glow">
    <p class="text-xs uppercase tracking-[0.22em] text-sky-300">Network Analysis</p>
    <ul class="mt-4 space-y-3 text-sm text-slate-300">
      <li>Wireshark packet review</li>
      <li>Protocol analysis</li>
      <li>DNS / HTTP anomalies</li>
      <li>Traffic baselining</li>
    </ul>
  </div>

  <div class="rounded-2xl border border-slate-800 bg-slate-900/80 p-5 panel-glow">
    <p class="text-xs uppercase tracking-[0.22em] text-sky-300">Scripting</p>
    <ul class="mt-4 space-y-3 text-sm text-slate-300">
      <li>Python automation</li>
      <li>Bash / PowerShell</li>
      <li>Log parsing</li>
      <li>Detection validation</li>
    </ul>
  </div>

  <div class="rounded-2xl border border-slate-800 bg-slate-900/80 p-4 panel-glow">
    <p class="text-xs uppercase tracking-[0.22em] text-sky-300">Threat Intel</p>
    <ul class="mt-4 space-y-3 text-sm text-slate-300">
      <li>MITRE ATT&CK mapping</li>
      <li>IOC enrichment</li>
      <li>Adversary tradecraft</li>
      <li>Risk prioritization</li>
    </ul>
  </div>
</section>
