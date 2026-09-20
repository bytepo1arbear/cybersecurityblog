---
layout: writeup
title: "HackTheBox: Legacy"
date: 2025-04-02
platform: "HackTheBox"
difficulty: "Easy"
tags: [HackTheBox, windows, smb, exploitation]
excerpt: "An older Windows-based HTB challenge covering SMB exploitation basics, version-to-vulnerability mapping, and a straightforward path to system access."
---

## Summary

This machine introduced the classic pattern of identifying an old Windows service and mapping it to a known vulnerable implementation. It was a strong reminder that legacy services can still matter in real environments and should be prioritized during review.

## Process

- Enumerate listening services and versions
- Match observed behavior to known SMB-related vulnerabilities
- Validate whether an exploit chain is feasible in the lab
- Confirm the final foothold and review the overall attack path

## Key Lessons

- Legacy services remain a real risk in lab and enterprise environments
- Service versioning is often the key to determining exposure
- Exploit chains are easier to reason about when the service behavior is well understood
- Defensive teams should aggressively identify and retire unsupported tooling

## Practical Relevance

This walkthrough reinforced how quickly an old but reachable system can become a high-priority issue. It also connected well with detection engineering work, where strong baselining and alerting help catch vulnerable services before they become a real foothold.

## Defensive Takeaways

- Patch or isolate legacy services quickly
- Use network and endpoint telemetry to identify unsupported configurations
- Review SMB access patterns for suspicious activity
- Ensure internal and external exposure is minimized consistently
