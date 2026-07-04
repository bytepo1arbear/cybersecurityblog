---
layout: projects
title: "Homelab Setup"
date: 2024-06-01
tags: [homelab, virtualization]
excerpt: "Notes and configuration for my homelab: Proxmox, networking, and storage design."
---

This project documents the homelab I built for practising deployments, virtualization, and network management. I cover Proxmox setup, VM templates, and network segmentation.

Key topics:
- Proxmox installation and configuration
- VM templates and backups
- VLANs and virtual networks
- Secure remote access and backups

This project documents the personal home lab used for hosting self-hosted services, media, and experimentation. Below are primary services and applications I run and why they're useful.

Services & Apps
- Proxmox: Type-1 hypervisor used to run and manage virtual machines and containers. I use it for VM orchestration, snapshots, resource scheduling, and creating isolated lab environments.
- TrueNAS: Network-attached storage for robust file storage, backups, and ZFS-based datasets. Provides shared storage for VMs, media libraries, and encrypted backup targets.
- Docker & Portainer: Container runtime for lightweight application deployment; Portainer provides a web UI to manage containers, stacks, and deployments in a reproducible manner.
- Jellyfin: Self-hosted media server for streaming personal media libraries (movies, TV, music) to devices across the home network.
- Immich: Self-hosted photo management and backup platform for securely storing and syncing personal photos and videos.
- WireGuard: Lightweight VPN for secure remote access to the homelab network and services, with easy mobile and desktop client configuration.
- Home Assistant: Home automation and monitoring, device health tracking, and notifications for lab infrastructure events.
- Vaultwarden: Password management service for securely storing login credentials and secrets used across lab systems.

Configuration details
- Proxmox hosts several VMs and LXC containers, with services grouped by function (media, storage, networking, lab sandboxes, and tool infrastructure).
- TrueNAS serves as the primary datastore for VM backups, media shares, and synced datasets; it integrates with Proxmox storage using NFS and iSCSI.
- Docker/Portainer host multiple service containers, allowing quick updates, rollback, and separation of workloads from the base VM environment.
- WireGuard provides secure access to the lab from outside networks; I use it for encrypted tunnels, remote SSH access, and cross-site service access.
- Home Assistant collects telemetry from the lab and provides dashboard alerting for service health, while Vaultwarden stores API keys and SSH key passphrases securely.

Read on for configuration tips, recommended resource allocations, backup strategies, and security hardening notes.
