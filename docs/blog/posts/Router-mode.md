---
draft: false
date: 2026-11-07
slug: router-mode
authors:
  - hiddify
categories:
  - Project
tags:
  - Hiddify
  - Release
description: "Router mode puts every device on your network behind Hiddify, with no setup on phones, TVs or consoles."
cover: /assets/blog/covers/Router-mode-en.webp
---

# Router mode: the whole home behind Hiddify

<!-- made by .cache/blog/history_gen.py -->

!!! abstract "In 30 seconds"
    On 7 November 2026 the Hiddify core got **router mode**. Run it on an **OpenWrt** router or any **Linux**
    gateway, and every device on the network (phones, TVs, consoles, smart devices) goes through Hiddify, **with
    nothing to set up on them**.

<!-- more -->

## What was new

- **TCP, UDP and ICMP** through the proxy.
- **No setup on devices**; SSH and the router's web page keep working.
- **OpenWrt package** `hiddify-core`, with router mode as the default for new installs, and opkg and apk feeds.
- **Any Linux gateway:** `hiddify-core run -c <profile> --router`.
- **In the app**: router mode on Linux shares the VPN with your whole network (5.9 test versions).

## Today

Today these tools live inside the Hiddify app and Hiddify Manager. Start with the app, or run your own server.

<div class="hi-cta-wrap"><a class="hi-cta" href="/app/How-to-install-Hiddify-app/">Download the Hiddify app</a></div>

??? note "For experts"
    - Packages for every release since 3 November 2026.
    - Sources: [router mode docs](https://github.com/hiddify/hiddify-core/blob/main/docs/router-mode.md)

## Related articles

- [DNS tunnels in Hiddify: when almost everything is blocked](DNS-tunnels-in-Hiddify.md)
- [Router mode on Linux](/app/Router-mode-on-Linux/)
- [Hiddify turns four](4th-anniversary.md)
