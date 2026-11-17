---
draft: false
date: 2024-12-15
slug: hiddify-manager-10-80
authors:
  - hiddify
categories:
  - Manager
tags:
  - Hiddify
  - Release
description: "Version 10.80 made Docker a real way to install, added WireGuard and Shadowsocks to v2rayNG links, and a faster install."
cover: /assets/blog/covers/Hiddify-Manager-v10-80-is-released-en.webp
---

# Hiddify Manager 10.80: install with Docker

<!-- made by .cache/blog/history_gen.py -->

!!! abstract "In 30 seconds"
    Hiddify Manager **10.80** came out on 15 December 2024. You can now install it with **Docker**, links for
    **v2rayNG** include WireGuard and Shadowsocks, and the install and certificates are faster. It was the last
    big 10.x update before version 11 in July 2025.

<!-- more -->

## What was new

- **Docker installation**, as a real way to install next to the one-command install.
- **WireGuard and Shadowsocks in v2rayNG links.**
- **A button to reset the owner's password.**
- **SSH host keys stay the same** across your servers.
- **Faster install and certificate issue**, with tasks running in the background.
- **API for the maximum number of IPs** per user.

## Today

Hiddify Manager is at version 14 now. Install the latest version, or update yours from the panel (take a [backup](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/) first).

<div class="hi-cta-wrap"><a class="hi-cta" href="/manager/installation-and-setup/guide/">Install Hiddify Manager</a></div>

??? note "For experts"
    - Early 2025 development builds (10.80.12.dev*) moved Docker to Ubuntu 24, installed the panel from source and used Python 3.13; XHTTP stream-up over H2 replaced gRPC for h2-vless-grpc.
    - The last 10.x was 10.86.4 (July 2025), with Xray 25.6.8.
    - Sources: [Docker](https://github.com/hiddify/Hiddify-Manager/commit/6b204d70), [panel HISTORY v10.80.0](https://github.com/hiddify/hiddifypanel/blob/main/HISTORY.md)

## Related articles

- [Hiddify Manager 10.70: SplitHTTP and fragment](Hiddify-Manager-v10-70-is-released.md)
- [Hiddify Manager 11 is out](Hiddify-Manager-v11-is-released.md)
- [Install Hiddify using Docker](/manager/installation-and-setup/Install-Hiddify-using-Docker/)
- [Hiddify Manager 14 is out](Hiddify-Manager-v14-is-released.md)
