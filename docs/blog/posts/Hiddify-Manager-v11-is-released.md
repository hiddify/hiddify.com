---
draft: false
date: 2025-07-11
slug: hiddifymanager-version-11-released
authors:
  - hiddify
categories:
  - Manager
tags:
  - Hiddify
  - Release
description: Hiddify Manager 11 adds XHTTP with separate upload and download domains, QUIC, a reworked proxy system, and uses up to half the RAM.
cover: /assets/blog/covers/Hiddify-Manager-v11-is-released-en.webp
---

# Hiddify Manager 11 is out

!!! abstract "In 30 seconds"
    Hiddify Manager **11.0.0** came out on 10 July 2025. It adds **XHTTP**, which can send upload and
    download through **different domains**, **QUIC**, a **rebuilt proxy system** where every setting can be
    changed, and it uses **up to half the RAM** it used before.

<!-- more -->

## What changes for you

- **XHTTP protocol**, also with Reality (Reality XHTTP).
- **Separate domains for upload and download.** Upload and download can use different domains or ALPNs,
  which makes the traffic harder to detect.
- **QUIC**, next to H1, H2, WS and HTTPUpgrade, and it works with a CDN.
- **A rebuilt proxy system**: change every parameter of each proxy as you like.
- **Bulk actions on users**: delete, turn on, turn off, or reset the days and traffic of many users at once.
- **A password for the admin panel**, an extra lock on admin access.
- **Up to 50% less RAM** and lower CPU use.
- **Faster, simpler installation.**
- **IP instead of a domain** in proxies, and a custom User-Agent.
- **Better IP choice for AutoCDN domains**, with random recent User-Agents.
- **Send chosen sites through WARP** now also for Hysteria, Shadowsocks and TUIC.
- **A Docker version** (first test version).
- Many panel improvements in look and use.

## Should I update?

Newer versions are out now (12, 13 and 14), and an update takes you straight to the latest one. Take a
[backup](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/) first,
then follow [How to update HiddifyManager](/manager/configuration-and-advanced-settings/How-to-update-Hiddify-panel/).

<div class="hi-cta-wrap"><a class="hi-cta" href="/manager/installation-and-setup/guide/">Install or update Hiddify Manager</a></div>

??? note "For experts: more changes in 11"
    - Xray core 25.6; Python 3.13.
    - New HAProxy version (on Ubuntu 24.04 only), for more exact and faster routing.
    - sing-box subscription updated.
    - Changes since 10.86.4: [Hiddify-Manager](https://github.com/hiddify/Hiddify-Manager/compare/v10.86.4...v11.0.0)
      and the [11.0.0 release](https://github.com/hiddify/Hiddify-Manager/releases/tag/v11.0.0).

## Related articles

- [Hiddify Manager 10.80: install with Docker](Hiddify-Manager-v10-80-is-released.md)
- [Hiddify Manager 12 is out](Hiddify-Manager-v12-is-released.md)
- [How to update HiddifyManager](/manager/configuration-and-advanced-settings/How-to-update-Hiddify-panel/)
- [Install Hiddify using Docker](/manager/installation-and-setup/Install-Hiddify-using-Docker/)
