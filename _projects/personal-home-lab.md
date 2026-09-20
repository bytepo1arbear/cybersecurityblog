---
layout: projects
title: "Personal Home Lab"
date: 2025-09-10
status: "Active"
featured: false
tags: [homelab, docker, networking, self-hosting, proxmox]
excerpt: "A self-hosted services stack running in Proxmox with containerized apps for media, networking, storage, and remote access."
---

## Overview

This environment is built for self-hosting and learning how to run applications securely and reliably at home. It focuses on containerization, network isolation, services management, and remote access workflows.

## Technology Stack

The lab runs on Proxmox and includes several self-hosted services and supporting tools.

### Core Services
- Docker and Portainer for container orchestration
- WireGuard for secure remote connectivity
- Jellyfin for media streaming
- TrueNAS for storage services and NAS functionality
- Immich for photo backup and organization
- Gluetun for VPN tunneling and traffic routing
- Reverse proxy / networking layers for internal service access

## Design Goals

- Self-host important services in a controlled environment
- Maintain privacy and ownership over personal data
- Learn networking, Docker, storage, and VPN design
- Build a home lab that is practical, resilient, and easy to maintain

## Operational Notes

Each service is organized around a modular setup to reduce downtime risk and make troubleshooting easier. The environment is designed to be both useful for daily tasks and educational as a platform for hands-on system administration and automation work.

## Example Service Layout

```text
Internet
  |
  v
Router / Firewall
  |
  +---- Proxmox Host
         |
         +---- Docker / Portainer
         |      - Jellyfin
         |      - Immich
         |      - Gluetun
         |
         +---- Storage / NAS
         |      - TrueNAS
         |
         +---- VPN / Remote Access
                - WireGuard
```

## What This Project Demonstrates

This project covers:
- home lab design
- containerized service management
- secure networking and remote access
- storage and media workflows
- practical self-hosting operations
