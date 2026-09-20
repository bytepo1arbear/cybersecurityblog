---
layout: writeup
title: "TryHackMe: Network Services"
date: 2025-02-08
platform: "TryHackMe"
difficulty: "Intermediate"
tags: [TryHackMe, networking, services, enumeration]
excerpt: "A practical walkthrough of common network services, enumeration patterns, and how service exposure can become a security issue."
---

## Summary

This room focused on the basics of network services and how service discovery and misconfiguration can create exploitable paths. It reinforced the importance of understanding what is running on a host and how it communicates.

## What I Learned

- Services often expose more than expected
- Enumeration helps identify running ports and application types
- Weak or overly permissive configurations can become attack surfaces
- Logging and monitoring are essential when services are exposed externally

## Practical Takeaways

This was a useful exercise for developing a more structured approach to identifying services and understanding how they can be abused or monitored. It also connected closely with real-world SOC tasks like reviewing endpoint and network telemetry.

## Example Observations

- Unknown services should be reviewed and documented
- Baseline behavior helps detect anomalies
- Unnecessary exposure increases risk and investigation complexity
