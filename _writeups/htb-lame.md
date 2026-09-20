---
layout: writeup
title: "HackTheBox: Lame"
date: 2025-02-18
platform: "HackTheBox"
difficulty: "Easy"
tags: [HackTheBox, linux, samba, enumeration]
excerpt: "A beginner-focused HackTheBox walkthrough covering SMB enumeration, service discovery, and privilege escalation through a simple but classic misconfiguration."
---

## Summary

This machine demonstrated how a poorly configured SMB service can expose an easy foothold. It reinforced the value of careful enumeration and validating which services are actually reachable and exploitable.

## Enumeration

- Review open ports and listening services
- Identify SMB-related exposure
- Confirm service version and patch level
- Map the attack path to an exploit candidate

## Exploitation Path

The room highlighted classic SMB mapping and version-based exploitation. Once the vulnerable service was identified, the next steps focused on validating the issue and turning it into a working foothold.

## Lessons Learned

- Low-hanging exposures are still valuable targets
- Service versioning matters during triage
- Enumeration is often the difference between a failed attempt and a successful chain
- A clean workflow keeps the attack path understandable and repeatable

## Defensive Takeaways

- Close unnecessary SMB exposure
- Review service baselines and patch gaps
- Log and alert on abnormal SMB access patterns
- Keep asset inventories current so unknown network services are not left unmanaged
