---
layout: writeup
title: "HackTheBox: Network Monitoring Analysis"
date: 2025-11-18
difficulty: Hard
tags: [HackTheBox, Network, Detection, Forensics]
platform: "HackTheBox"
excerpt: "A HackTheBox walkthough emphasizing network monitoring, packet inspection, and attacker visibility within a segmented lab environment."
---

# HackTheBox: Network Monitoring Analysis

## Overview

This writeup focuses on using network monitoring and packet capture techniques to detect lateral movement and suspicious C2-like behavior in an HTB machine.

## Analysis

- Captured traffic with `tcpdump` and Wireshark
- Identified unusual DNS and HTTP beaconing patterns
- Correlated host events with network indicators for detection tuning

## Conclusion

The exercise reinforces why network telemetry remains a critical part of a layered SOC defense strategy.
