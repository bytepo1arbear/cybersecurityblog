---
layout: projects
title: "Cyber Security Home Lab"
date: 2025-09-01
status: "Active"
featured: true
tags: [homelab, proxmox, security, blue-team, detection]
excerpt: "A purpose-built security lab for testing tools, adversary emulation, defensive monitoring, and new detection workflows."
---

## Overview

This lab is designed for continuous learning and practical validation of detection engineering, offensive security, and defensive monitoring workflows. It is used to test new tools, explore threat behavior, and validate how detection logic holds up in realistic conditions.

## Core Architecture

The environment is built on Proxmox and segmented to mimic a realistic security operations setup with multiple virtual machines and supporting services.

### Primary Components
- Proxmox hypervisor for VM orchestration and resource allocation
- Kali Linux for offensive testing and enumeration workflows
- Wazuh for host-based monitoring and SIEM-style log collection
- Caldera for red team automation and adversary simulation
- TheHive for case management and incident triage workflows
- DVWA and BWAPP for web application security testing
- Nessus for vulnerability discovery and scanning
- Splunk-aligned log sources for alert validation and analysis
- Linux and Windows endpoint lab hosts for cross-platform testing

## Lab Goals

- Test security tooling in a controlled environment
- Validate detection logic against realistic adversary behavior
- Build hands-on lab experience with SIEM, EDR, and network telemetry
- Practice different phases of the security lifecycle

## Example Workflow

1. Validate threat behavior in attack VMs
2. Collect telemetry from endpoints and logging services
3. Correlate events in SIEM or alerting workflows
4. Investigate, document, and tune detections

## Configuration Notes

This build includes network segmentation, isolated target machines, monitoring servers, and dedicated management infrastructure. It is used not only for exploitation testing, but also for understanding how telemetry, alerts, and mitigation strategies work together in real environments.

## Lab Diagram

```text
Internet
  |
  v
Firewall / Router
  |
  +---- Management Network
  |      - Proxmox
  |      - Wazuh
  |      - TheHive
  |
  +---- Attack Network
  |      - Kali Linux
  |      - Metasploitable / DVWA / BWAPP
  |
  +---- Detection Network
         - Windows/Linux endpoint lab VMs
```

## What This Project Demonstrates

This project is a practical environment for learning how to:
- deploy security tools in a secure lab
- validate detections and alert logic
- assess attacker tradecraft
- build repeatable workflows that support investigation and response
