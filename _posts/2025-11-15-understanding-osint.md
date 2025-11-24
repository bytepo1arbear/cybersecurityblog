---
layout: post
title: "Understanding OSINT: Gathering Intelligence from Public Sources"
date: 2025-11-15 20:00:00 +0000
categories: [osint, intelligence]
tags: [open source intelligence, recon, investigation, cybersecurity]
---

# Understanding OSINT: Gathering Intelligence from Public Sources

Open Source Intelligence (OSINT) refers to the collection and analysis of publicly available information. It plays an important role in cybersecurity, threat intelligence, and digital investigations. With OSINT techniques, analysts can uncover valuable data about individuals, systems, or organizations without accessing private or restricted resources.

## What is OSINT?

OSINT involves gathering data from sources such as:

- Social media platforms  
- Public records and government databases  
- Domain and IP lookup services  
- News articles and online publications  
- Forums and paste sites  
- Code repositories  

Because this information is openly accessible, OSINT does not involve hacking. Instead, it relies on strategic searching, correlation, and analysis.

## Popular OSINT Tools

1. **Maltego:** Graph-based link analysis tool for connecting people, domains, and infrastructure.
2. **theHarvester:** Gathers emails, subdomains, and hosts using public search engines.
3. **Shodan:** A search engine for discovering internet-connected devices.
4. **SpiderFoot:** Automated reconnaissance tool that aggregates results from dozens of data sources.

## Example: Gathering Domain Information

Using `whois`:

```bash
whois example.com
