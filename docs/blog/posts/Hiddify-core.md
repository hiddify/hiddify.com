---
draft: false
date: 2023-09-11
slug: hiddify-core
authors:
  - hiddify
categories:
  - Project
tags:
  - Hiddify
  - Release
description: "The engine under the Hiddify app, built on our own sing-box: the same features on Android, iOS, Windows, macOS and Linux."
cover: /assets/blog/covers/Hiddify-core-en.webp
---

# Hiddify core: one engine for every platform

<!-- made by .cache/blog/history_gen.py -->

!!! abstract "In 30 seconds"
    With the first Hiddify Next app, on 11 September 2023, we released **hiddify-core** 0.1: one engine that runs
    the same way on **Android, iOS, Windows, macOS and Linux**. It is built on **hiddify-sing-box**, our version
    of sing-box with features the original does not have, such as TLS tricks, WARP and Psiphon.

<!-- more -->

## What was new

- **One engine, five systems:** the app looks and works the same everywhere.
- **hiddify-sing-box** (since May 2023): TLS fragment and tricks, WARP (WireGuard, AmneziaWG, MASQUE), Psiphon, XHTTP and DNS tunnels.
- **ray2sing:** reads VLESS, VMess, Trojan, Hysteria2, SSH, WireGuard and WARP links and turns them into sing-box configs.
- **Xray inside** (core 1.9, July 2024) for configs sing-box cannot run.
- **More than 100 releases**; about 880,000 core and 1,060,000 sing-box downloads from GitHub.
- **Core 5** (October 2026): hot reload, chains for Extra security and Proxy unblocker.

<div align=center>

<img src="/assets/blog/2nd-anniversary/34829e2e.svg" alt="Hiddify" width="40%" />
</div>

## Today

Today these tools live inside the Hiddify app and Hiddify Manager. Start with the app, or run your own server.

<div class="hi-cta-wrap"><a class="hi-cta" href="/app/How-to-install-Hiddify-app/">Download the Hiddify app</a></div>

??? note "For experts"
    - The core repository was created on 16 August 2023; ray2sing on 9 September 2023.
    - Sources: [hiddify-core 0.1.0](https://github.com/hiddify/hiddify-core/releases/tag/v0.1.0), [hiddify-sing-box](https://github.com/hiddify/hiddify-sing-box), [ray2sing](https://github.com/hiddify/ray2sing)

## Related articles

- [HiddifyNG and HiddifyN: our apps for Android and Windows](HiddifyNG-and-HiddifyN.md)
- [Hiddify Reality Scanner: find the best SNI for Reality](Hiddify-Reality-Scanner.md)
- [Hiddify core guide](/core/)
- [Hiddify turns four](4th-anniversary.md)
