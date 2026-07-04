---
layout: default
title: "Threat Intel"
permalink: /threat-intel/
---

<section class="page-hero">
  <div class="container">
    <h1>Threat Intelligence</h1>
    <p class="page-subtitle">Consolidated threat feed summary and source overview for defensive analysis.</p>
  </div>
</section>

<div class="container threat-board">
  <article class="threat-panel">
    <h2>Latest Feed Items</h2>
    <!-- NOTE: Threat feed data is refreshed daily by a scheduled GitHub Action that writes to `_data/threats.yml`. -->
    {% if site.data.threats and site.data.threats.items and site.data.threats.items.size > 0 %}
    <div class="ioc-matrix">
      <table id="threat-table">
        <thead>
          <tr>
            <th>Date</th>
            <th>Source</th>
            <th>Title</th>
            <th>Summary</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {%- assign groups = site.data.threats.items | group_by: "source" -%}
          {%- assign shown = 0 -%}
          {%- assign printed_titles = "" -%}

          {%- for g in groups -%}
            {%- assign item = g.items[0] -%}
            <tr class="threat-row">
              <td>{{ item.published | default: site.data.threats.last_updated }}</td>
              <td>{{ item.source }}</td>
              <td><a class="btn-small" href="{{ item.link }}" target="_blank" rel="noopener">{{ item.title }}</a></td>
              <td>{{ item.summary | strip_html | truncate: 120 }}</td>
              <td></td>
            </tr>
            {%- assign shown = shown | plus: 1 -%}
            {%- assign printed_titles = printed_titles | append: item.title | append: "||" -%}
          {%- endfor -%}

          {%- if shown < 15 -%}
            {%- for item in site.data.threats.items -%}
              {%- if shown >= 15 -%}
                {%- break -%}
              {%- endif -%}
              {%- unless printed_titles contains item.title -%}
                <tr class="threat-row extra-row" style="display:none;">
                  <td>{{ item.published | default: site.data.threats.last_updated }}</td>
                  <td>{{ item.source }}</td>
                  <td><a class="btn-small" href="{{ item.link }}" target="_blank" rel="noopener">{{ item.title }}</a></td>
                  <td>{{ item.summary | strip_html | truncate: 120 }}</td>
                  <td></td>
                </tr>
                {%- assign shown = shown | plus: 1 -%}
                {%- assign printed_titles = printed_titles | append: item.title | append: "||" -%}
              {%- endunless -%}
            {%- endfor -%}
          {%- endif -%}
        </tbody>
      </table>
    </div>
    <p class="threat-note">Showing up to 15 aggregated items (one per source, then latest). Last updated: {{ site.data.threats.last_updated }}</p>
    <div style="text-align:center;margin-top:1rem;">
      <button id="show-more-btn" class="btn">Show more</button>
    </div>
    <script>
      document.addEventListener('DOMContentLoaded', function(){
        const btn = document.getElementById('show-more-btn');
        if(!btn) return;
        btn.addEventListener('click', function(){
          document.querySelectorAll('.extra-row').forEach(r => r.style.display = 'table-row');
          btn.style.display = 'none';
        });
      });
    </script>
    {% else %}
    <p class="threat-note">Threat feed data is not yet available. The site will show live updates after the scheduled fetch runs. You can also trigger the update manually via GitHub Actions.</p>
    {% endif %}
  </article>
</div>
