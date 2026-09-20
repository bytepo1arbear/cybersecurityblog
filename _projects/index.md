---
layout: default
title: "Projects"
permalink: /projects/
exclude_from_collection: true
---

<section class="mb-8 text-center">
  <h1 class="text-3xl font-bold text-white sm:text-4xl">Projects</h1>
  <p class="mx-auto mt-3 max-w-3xl text-slate-300">Two core home lab environments supporting offensive testing, detection engineering, and practical self-hosted infrastructure.</p>
</section>

<div class="mx-auto max-w-6xl">
  <div class="grid gap-6 lg:grid-cols-2">
    {% assign project_list = site.projects | where_exp: "project", "project.path != '_projects/index.md'" | sort: 'featured' | reverse | sort: 'date' | reverse %}
    {% for project in project_list %}
    <article class="rounded-2xl border border-slate-800 bg-slate-900/80 p-6 shadow-glow {% if project.featured %}ring-1 ring-sky-500/40{% endif %}">
      <div class="mb-4 flex items-center justify-between gap-3">
        <span class="rounded-full border border-slate-700 px-2.5 py-1 text-[10px] font-semibold uppercase tracking-[0.18em] text-slate-300">{{ project.date | date: '%b %Y' }}</span>
        {% if project.featured %}
        <span class="rounded-full border border-emerald-500/30 bg-emerald-500/10 px-2.5 py-1 text-[10px] font-semibold uppercase tracking-[0.2em] text-emerald-300">Featured</span>
        {% endif %}
      </div>
      <h3 class="text-2xl font-semibold text-white">{{ project.title }}</h3>
      <p class="mt-3 text-base leading-7 text-slate-300">{{ project.excerpt | strip_html }}</p>
      <div class="mt-5 flex flex-wrap gap-2">
        {% for tag in project.tags limit:5 %}
        <span class="rounded-full border border-slate-700 bg-slate-950 px-2 py-1 text-[10px] uppercase tracking-[0.12em] text-sky-200">{{ tag }}</span>
        {% endfor %}
      </div>
      <div class="mt-6">
        <a href="{{ project.url | relative_url }}" class="inline-flex items-center gap-2 rounded-full border border-sky-500/30 bg-sky-500/10 px-4 py-2 text-sm font-medium text-sky-200 transition hover:border-sky-400 hover:text-sky-100">View project <i class="fa-solid fa-arrow-right"></i></a>
      </div>
    </article>
    {% endfor %}
  </div>
</div>
