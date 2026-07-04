---
layout: projects
title: "Penetration Testing Lab"
date: 2024-11-01
tags: [pentesting, lab, vulnhub]
excerpt: "A curated pentesting lab with vulnerable VMs for practicing enumeration and exploitation."
---

This project documents the build and management of a penetration testing lab: vulnerable VMs, network isolation, and tooling.

Includes configuration for attacking machines, typical workflows, and a short list of intentionally vulnerable boxes.

Cyber Security Lab — Services & Tools

The lab is designed to emulate attacker/defender workflows and includes the following components:

- Proxmox: Hypervisor platform to host attack & defense VMs, network segments, and orchestration for reproducible lab environments.
- Docker: Container runtime for deploying tools and services when lightweight isolation is preferred.
- pfSense: Firewall and virtual router for network segmentation, NAT, and controlled ingress/egress in the lab network.
- Caldera: Adversary emulation and automation framework to simulate attacker behavior and validate detection.
- Wazuh: Host-based detection and SIEM integration for log collection, alerting, and threat detection telemetry.
- DVWA / BWAPP: Intentionally vulnerable web applications used for web-app vulnerability practice and detection tuning.
- Metasploit & Metasploitable: Exploitation framework and intentionally vulnerable VMs for practicing exploitation and post-exploitation techniques.
- Nessus: Vulnerability scanner for mapping vulnerable services and prioritising patching/testing.
- Kali Linux: Attacker toolkit distribution for enumeration, exploitation, and post-exploitation work.
- Windows 10/11: Target OS images for realistic endpoint exploitation and detection validation.

These tools together provide a full stack for both offensive practice and blue team validation. The project documents deployment steps, network layout, and sample attack/playbook scenarios.

Detailed lab notes
- Network segmentation: I separate attack, target, monitoring, and management zones to mirror real-world controls while keeping the lab safe.
- Detection validation: Wazuh and Caldera allow me to test alerts, collector rules, and detection pipelines against simulated adversary behavior.
- Workflow examples: The writeup includes enumeration checklists, exploitation paths, post-exploitation cleanup, and how to document findings.
- Tool chaining: I use Nmap and Nessus for discovery, Burp Suite for web testing, Metasploit for exploitation, and custom scripts for privilege escalation analysis.
- Coverage: The lab includes both Linux and Windows targets so I can practise cross-platform attacks, lateral movement, and endpoint detection.

The lab is organized so I can practice both attack workflows and defensive monitoring, with a focus on repeatable, measurable results.
