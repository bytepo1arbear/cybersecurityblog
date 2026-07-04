---
layout: default
title: "Homelab Architecture"
permalink: /projects/homelab-architecture/
---

<section class="page-hero">
  <div class="container">
    <h1>Proxmox & Docker Architecture</h1>
    <p class="page-subtitle">Enterprise-style homelab architecture with virtual machines, container services, and segmented security domains.</p>
  </div>
</section>

## Network & Services Topology

Below is the current design for my homelab, with a focus on Proxmox VE, Docker orchestration, and segmented security zones.

```
[Internet] --> [Edge Firewall] --> [VLAN 10 | Core Services] --> [Proxmox VE Cluster]
                                          |--> [Docker Host]
                                          |      |--> [Jellyfin Container]
                                          |      |--> [SIEM / Log Aggregation]
                                          |      |--> [Red Team Lab Containers]
                                          |      |--> [Vulnerability Scanner]
                                          |--> [VLAN 20 | Security Labs]
                                          |      |--> [Kali Linux VM]
                                          |      |--> [Blue Team VM]
                                          |      |--> [Forensic Analysis VM]
```

## Architecture Overview

- **Proxmox VE**: Virtualization platform for running isolated lab VMs and service nodes.
- **Docker Containers**: Rapid service deployment for monitoring, security tooling, and media services.
- **Jellyfin**: Media server running inside a segmented container to keep non-security workloads isolated.
- **Network Segmentation**: Separate zones for production-style services, attack infrastructure, and management.

## Cyber Security Lab & Tool Testing Showcase

This project documents my security lab built for defensive testing, infrastructure hardening, and offensive validation.

### Log Aggregation & Monitoring (SIEM)

- Centralized log collection from host systems, containers, and network sensors.
- SIEM pipeline supports alerting, rule tuning, and incident validation.
- Designed for real-world defensive scenarios and tabletop exercise support.

### Attack Infrastructure

- Dedicated offensive lab VMs and containerized tooling for exploit development.
- Isolated network segment prevents accidental cross-contamination into defensive zones.
- Includes simulated C2 infrastructure, phishing landing zones, and adversary emulation assets.

### Defense Validation

- IDS/IPS and host monitoring running against simulated attack traffic.
- Validation workflows include detection testing, alert triage, and control verification.
- Traffic analysis and response exercises support SOC readiness.

### Hands-on Tools

- **Kali Linux**: offensive toolset for exploitation, reconnaissance, and lateral movement.
- **Wireshark**: packet capture and network anomaly analysis.
- **Suricata / Zeek**: network detection and threat telemetry.
- **OpenSearch / Elasticsearch**: centralized logs, dashboards, and search.
- **Metasploit**: attack infrastructure for penetration tests and exploit validation.
