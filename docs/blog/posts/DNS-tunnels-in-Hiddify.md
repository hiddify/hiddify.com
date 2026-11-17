---
draft: false
date: 2026-03-05
slug: dns-tunnels
authors:
  - hiddify
categories:
  - Project
tags:
  - Hiddify
  - Release
description: "DNSTT, VayDNS, MasterDNS and Soar carry traffic inside DNS questions: slow, but they can work when almost nothing else does."
cover: /assets/blog/covers/DNS-tunnels-in-Hiddify-en.webp
---

# DNS tunnels in Hiddify: when almost everything is blocked

<!-- made by .cache/blog/history_gen.py -->

!!! abstract "In 30 seconds"
    From 5 March 2026 the Hiddify app and Hiddify Manager learned **DNS tunnels**. They hide traffic inside DNS
    questions, which are rarely fully blocked. They are slow, but in the worst shutdowns they can still connect:
    **DNSTT**, **VayDNS**, **MasterDNS** and **Soar**.

<!-- more -->

## What was new

- **DNSTT** in the core (March 2026), then many resolvers at once.
- **VayDNS** with automatic choice of resolvers.
- **MasterDNS and Soar** (November 2026); MasterDNS with few resolvers is about 8 times faster with our multi-resolver pool.
- **Links** such as `dnst://`, `masterdns://` and `soar://` open in the app.
- **In the panel** since Hiddify Manager 13.

## Today

Today these tools live inside the Hiddify app and Hiddify Manager. Start with the app, or run your own server.

<div class="hi-cta-wrap"><a class="hi-cta" href="/app/How-to-install-Hiddify-app/">Download the Hiddify app</a></div>

??? note "For experts"
    - These tunnels are projects of other teams (net2share, masterking32, Lantern and others); we integrated them. Thank you to their makers.
    - Sources: [core 4.1.0](https://github.com/hiddify/hiddify-core/releases/tag/v4.1.0), [protocols docs](https://github.com/hiddify/hiddify-sing-box/tree/main/docs/hiddify/features/protocols)

## Related articles

- [Hiddify extensions: anyone can add a feature](Hiddify-Extensions.md)
- [Router mode: the whole home behind Hiddify](Router-mode.md)
- [Hiddify Manager 13 is out](Hiddify-Manager-v13-is-released.md)
- [Hiddify turns four](4th-anniversary.md)
