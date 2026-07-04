---
layout: writeup
title: "TryHackMe: Linux Privilege Escalation Lab"
date: 2025-11-24
difficulty: Medium
tags: [TryHackMe, Linux, Privilege Escalation, Sudo]
platform: "TryHackMe"
excerpt: "A hands-on TryHackMe lab focused on Linux privilege escalation paths, sudo misconfigurations, and post-exploit evidence capture."
---

# TryHackMe: Linux Privilege Escalation Lab

## Overview

This TryHackMe writeup covers a lab where the objective is to escalate from a low-privileged shell to root by identifying misconfigured sudo rules and weak service permissions.

## Key Findings

- Enumerated user sudo privileges using `sudo -l`
- Found a custom binary with elevated permissions
- Exploited writable configuration files to trigger root execution

## Outcome

The lab demonstrates how small misconfigurations can lead to full system compromise and why detection rules should monitor unusual `sudo` command execution.
