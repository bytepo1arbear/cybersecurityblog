---
layout: default
title: "Threat Intel"
permalink: /threat-intel/
---

<section class="mb-8 rounded-2xl border border-slate-800 bg-slate-900/80 p-6 shadow-glow sm:p-8">
  <div class="flex flex-col gap-3 lg:flex-row lg:items-end lg:justify-between">
    <div>
      <div class="mb-3 inline-flex items-center gap-2 rounded-full border border-sky-500/30 bg-sky-500/10 px-3 py-1 text-[10px] font-semibold uppercase tracking-[0.22em] text-sky-300">
        <span class="h-2 w-2 rounded-full bg-emerald-400 status-dot"></span>
        Threat Feed
      </div>
      <h1 class="text-4xl font-bold tracking-tight text-white">Threat Intelligence</h1>
    </div>
    <p class="max-w-2xl text-sm leading-6 text-slate-300">
      Recent incident reporting, advisories, and research curated from multiple public sources for alert awareness and defensive analysis.
    </p>
  </div>
</section>

{% if site.data.threats and site.data.threats.items and site.data.threats.items.size > 0 %}
  <section class="mb-8 grid gap-5 md:grid-cols-3">
    <div class="rounded-2xl border border-slate-800 bg-slate-900/80 p-5 panel-glow">
      <p class="text-[10px] uppercase tracking-[0.22em] text-slate-400">Sources</p>
      <p class="mt-3 text-3xl font-bold text-white">{{ site.data.threat_sources | size }}</p>
      <p class="mt-2 text-sm text-slate-400">Curated and refreshed by automation</p>
    </div>
    <div class="rounded-2xl border border-slate-800 bg-slate-900/80 p-5 panel-glow">
      <p class="text-[10px] uppercase tracking-[0.22em] text-slate-400">Items</p>
      <p class="mt-3 text-3xl font-bold text-white">{{ site.data.threats.items | size }}</p>
      <p class="mt-2 text-sm text-slate-400">Recent articles, advisories, and reports</p>
    </div>
    <div class="rounded-2xl border border-slate-800 bg-slate-900/80 p-5 panel-glow">
      <p class="text-[10px] uppercase tracking-[0.22em] text-slate-400">Last Updated</p>
      <p class="mt-3 text-lg font-semibold text-sky-300">{{ site.data.threats.last_updated | date: '%b %d, %Y' }}</p>
      <p class="mt-2 text-sm text-slate-400">Automated sync from the GitHub Action feed</p>
    </div>
  </section>

  <section class="mb-8 rounded-2xl border border-slate-800 bg-slate-900/80 p-6 panel-glow">
    <div class="mb-5 flex items-center justify-between">
      <h2 class="text-xl font-semibold text-white">Feed Sources</h2>
      <span class="rounded-full border border-slate-700 px-2.5 py-1 text-[10px] uppercase tracking-[0.2em] text-slate-400">Public intel</span>
    </div>

    <div class="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
      {% for source in site.data.threat_sources %}
        <div class="rounded-xl border border-slate-800 bg-slate-950/70 p-4">
          <div class="flex items-center justify-between gap-3">
            <span class="threat-source-pill rounded-full border border-sky-500/30 bg-sky-500/10 px-2 py-1 text-sky-300">{{ source.category }}</span>
            <span class="text-[10px] uppercase tracking-[0.16em] text-slate-500">{{ source.name }}</span>
          </div>
          <p class="mt-3 text-sm leading-6 text-slate-400">{{ source.notes }}</p>
        </div>
      {% endfor %}
    </div>
  </section>

  <section class="rounded-2xl border border-slate-800 bg-slate-900/80 p-6 panel-glow">
    <div class="mb-6 flex items-center justify-between">
      <h2 class="text-xl font-semibold text-white">Latest Incidents & Research</h2>
      <span class="rounded-full border border-emerald-500/30 bg-emerald-500/10 px-2.5 py-1 text-[10px] uppercase tracking-[0.2em] text-emerald-300">Live</span>
    </div>

    <div class="space-y-4">
      {% for item in site.data.threats.items limit:12 %}
        <article class="threat-item-card rounded-xl p-4">
          <div class="mb-3 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
            <div class="flex flex-wrap items-center gap-2">
              <span class="rounded-full border border-emerald-500/30 bg-emerald-500/10 px-2 py-1 text-[9px] uppercase tracking-[0.18em] text-emerald-300">{{ item.source }}</span>
              <span class="text-[11px] uppercase tracking-[0.18em] text-slate-500">{{ item.published | date: '%b %d, %Y' }}</span>
            </div>
            <a href="{{ item.link }}" target="_blank" rel="noopener" class="text-sm font-medium text-sky-300 hover:text-sky-200">Open source →</a>
          </div>

          <h3 class="text-lg font-semibold text-white">{{ item.title }}</h3>
          <p class="mt-3 text-sm leading-6 text-slate-300">{{ item.summary | strip_html | truncate: 220 }}</p>
        </article>
      {% endfor %}
    </div>
  </section>
{% else %}
  <div class="rounded-2xl border border-slate-800 bg-slate-900/80 p-8 text-center panel-glow">
    <h2 class="text-xl font-semibold text-white">Threat feed data is not available yet</h2>
    <p class="mt-3 text-slate-300">
      The GitHub Action has not populated _data/threats.yml yet. Trigger the workflow or run the fetch script locally to populate the feed.
    </p>
  </div>
{% endif %}
