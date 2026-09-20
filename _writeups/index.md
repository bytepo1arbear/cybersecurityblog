---
layout: default
title: "Writeups"
permalink: /writeups/
exclude_from_collection: true
---

<section class="mb-8 text-center">
  <h1 class="text-3xl font-bold text-white sm:text-4xl">Writeups</h1>
  <p class="mx-auto mt-3 max-w-3xl text-slate-300">Six example room writeups covering TryHackMe and HackTheBox practice, ready to be refined into personal walkthroughs later.</p>
</section>

{% assign all_writeups = site.writeups | where_exp: "w", "w.path != '_writeups/index.md' and w.platform != 'Home Lab'" | sort: 'date' | reverse %}
{% assign thm_writeups = all_writeups | where: 'platform', 'TryHackMe' | limit: 3 %}
{% assign htb_writeups = all_writeups | where: 'platform', 'HackTheBox' | limit: 3 %}

<div class="mx-auto max-w-6xl">
  <div class="grid gap-5 lg:grid-cols-2">
    <article class="rounded-2xl border border-slate-800 bg-slate-900/80 p-6 panel-glow">
      <h3 class="text-xl font-semibold text-white">TryHackMe</h3>
      <p class="mt-3 text-slate-300">Foundation skills covering security basics, Linux fundamentals, and networking services use cases.</p>
      <ul class="mt-5 space-y-3 text-sm text-slate-200">
        {% for item in thm_writeups %}
        <li class="rounded-xl border border-slate-800 bg-slate-950/60 p-3">
          <a href="{{ item.url | relative_url }}" class="font-medium text-sky-300 hover:text-sky-200">{{ item.title }}</a>
          <p class="mt-2 text-xs leading-5 text-slate-400">{{ item.excerpt | strip_html | truncate: 120 }}</p>
        </li>
        {% endfor %}
      </ul>
    </article>

    <article class="rounded-2xl border border-slate-800 bg-slate-900/80 p-6 panel-glow">
      <h3 class="text-xl font-semibold text-white">HackTheBox</h3>
      <p class="mt-3 text-slate-300">Example machine walkthroughs focused on enumeration, exploitation flow, and operational triage.</p>
      <ul class="mt-5 space-y-3 text-sm text-slate-200">
        {% for item in htb_writeups %}
        <li class="rounded-xl border border-slate-800 bg-slate-950/60 p-3">
          <a href="{{ item.url | relative_url }}" class="font-medium text-sky-300 hover:text-sky-200">{{ item.title }}</a>
          <p class="mt-2 text-xs leading-5 text-slate-400">{{ item.excerpt | strip_html | truncate: 120 }}</p>
        </li>
        {% endfor %}
      </ul>
    </article>
  </div>
</div>
