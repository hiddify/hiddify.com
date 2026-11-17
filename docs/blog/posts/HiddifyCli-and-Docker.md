---
draft: false
date: 2024-03-09
slug: hiddifycli-docker
authors:
  - hiddify
categories:
  - Project
tags:
  - Hiddify
  - Release
description: "The Hiddify app without a graphical interface, with a small web page: for servers, routers and Docker."
cover: /assets/blog/covers/HiddifyCli-and-Docker-en.webp
---

# HiddifyCli and Docker: Hiddify without a screen

<!-- made by .cache/blog/history_gen.py -->

!!! abstract "In 30 seconds"
    On 9 March 2024 we released **HiddifyCli**: the Hiddify app with every feature, but **without a graphical
    interface**, and a small web page to control it. You can run it on **servers, routers (OpenWrt)** and in
    **Docker**.

<!-- more -->

## What was new

- **HiddifyCli** with a basic web page (core 0.17).
- **Docker image** (March 2024), for more platforms from September 2024.
- **OpenWrt** web page and init script (core 2.3, September 2024).
- **One-line install:** `bash <(curl https://i.hiddify.com/core)`.
- **Router mode** later (November 2026): put a whole home network behind Hiddify.

## Today

Today these tools live inside the Hiddify app and Hiddify Manager. Start with the app, or run your own server.

<div class="hi-cta-wrap"><a class="hi-cta" href="/app/How-to-install-Hiddify-app/">Download the Hiddify app</a></div>

??? note "For experts"
    - HiddifyCli is part of the hiddify-core repository, not a separate project.
    - Sources: [core 0.17.0](https://github.com/hiddify/hiddify-core/releases/tag/v0.17.0), [core 2.3.0](https://github.com/hiddify/hiddify-core/releases/tag/v2.3.0)

## Related articles

- [Hiddify Reality Scanner: find the best SNI for Reality](Hiddify-Reality-Scanner.md)
- [Hiddify relay builder: a tunnel server in a few minutes](Hiddify-relay-builder.md)
- [HiddifyCli guide](/app/HiddifyCli-guide/)
- [HiddifyCli on OpenWrt](/app/How-to-use-HiddifyCli-on-OpenWrt/)
- [Hiddify turns four](4th-anniversary.md)
