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
This project documents the personal home lab used for hosting self-hosted services, media, and experimentation. Below are primary services and applications I run and why they're useful.

Services & Apps
- Proxmox: Type-1 hypervisor used to run and manage virtual machines and containers. I use it for VM orchestration, snapshots, and resource management.
- TrueNAS: Network-attached storage for robust file storage, backups, and ZFS-based datasets. Provides shared storage for VMs and media.
- Docker & Portainer: Container runtime for lightweight application deployment; Portainer provides a simple web UI to manage containers and stacks.
- Jellyfin: Self-hosted media server for streaming personal media libraries (movies, TV, music) to devices.
- Immich: Self-hosted photo management and backup platform for personal photos and videos.
- WireGuard: Lightweight VPN for secure remote access to the homelab network and services.

Brief usage notes
- Proxmox hosts several VMs and LXC containers: services are grouped by function (media, storage, networking, lab sandboxes).
- TrueNAS serves as the primary datastore for VM backups and media shares; integrates with Proxmox storage via NFS/iSCSI.
- Docker/Portainer host many small services (Jellyfin, Immich, web apps) for easy updates and isolation.
- WireGuard allows secure access from outside networks to the homelab; used for tunneling and remote management.

Read on for configuration tips, recommended resource allocations, and backup strategies.
