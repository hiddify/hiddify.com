---
draft: false
date: 2024-07-29
slug: hiddify-manager-10-70
authors:
  - hiddify
categories:
  - Manager
tags:
  - Hiddify
  - Release
description: "Summer 2024: quick setup (10.50), then SplitHTTP, Xray fragment, WireGuard in the panel and an HTML editor (10.70)."
cover: /assets/blog/covers/Hiddify-Manager-v10-70-is-released-en.webp
---

# Hiddify Manager 10.70: SplitHTTP and fragment

<!-- made by .cache/blog/history_gen.py -->

!!! abstract "In 30 seconds"
    Hiddify Manager **10.70** came out on 29 July 2024. It added **SplitHTTP**, a new way to pass the filter over
    a CDN, **Xray fragment**, WireGuard output in the panel, and an editor for the text users see. Two weeks
    earlier, **10.50** had added **quick setup** steps for a new server.

<!-- more -->

## What was new

- **SplitHTTP** (Xray), also over HTTP/3 (QUIC), which works well behind a CDN.
- **Xray fragment**, and a custom URL test.
- **WireGuard** output in the panel.
- **HTML editor** for the custom text on the user page.
- **Quick setup** (10.50): a few steps for a new server, with some services off by default.
- **Better IPv4 and IPv6 handling** (10.50), and Reality and VLESS can be turned on separately (10.30).
- **Lighter server** (10.20): Xray or sing-box configs that are not needed are turned off to save memory.

## Today

Hiddify Manager is at version 14 now. Install the latest version, or update yours from the panel (take a [backup](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/) first).

<div class="hi-cta-wrap"><a class="hi-cta" href="/manager/installation-and-setup/guide/">Install Hiddify Manager</a></div>

??? note "For experts"
    - 10.20 (12 April 2024) also added a WARP site validator and "remaining days to reset"; the panel moved to a Python venv.
    - In May 2024 we also released the Hiddify relay builder for tunnel servers (GOST, HAProxy, Socat, iptables and more).
    - Sources: [SplitHTTP](https://github.com/hiddify/Hiddify-Manager/commit/529f6bc0), [Xray fragment](https://github.com/hiddify/Hiddify-Manager/commit/f45f5d10), [quick setup (10.50)](https://github.com/hiddify/Hiddify-Manager/commit/9372c3cb)

## Related articles

- [Hiddify Manager 10.10: Shadowsocks 2022, HTTPUpgrade and WireGuard](Hiddify-Manager-v10-10-is-released.md)
- [Hiddify Manager 10.80: install with Docker](Hiddify-Manager-v10-80-is-released.md)
- [Hiddify Manager 14 is out](Hiddify-Manager-v14-is-released.md)
