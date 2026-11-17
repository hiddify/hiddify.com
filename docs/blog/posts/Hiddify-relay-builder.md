---
draft: false
date: 2024-07-05
slug: hiddify-relay-builder
authors:
  - hiddify
categories:
  - Project
tags:
  - Hiddify
  - Release
description: "One script that builds a relay (tunnel) server with the methods that work: iptables, GOST, Dokodemo-door, HAProxy, socat and WST."
cover: /assets/blog/covers/Hiddify-relay-builder-en.webp
---

# Hiddify relay builder: a tunnel server in a few minutes

<!-- made by .cache/blog/history_gen.py -->

!!! abstract "In 30 seconds"
    A relay server inside the country passes your traffic to the main server abroad. The **Hiddify relay builder**
    (first release 5 July 2024) builds one with a single script and the methods that work: **iptables, GOST,
    Dokodemo-door, HAProxy, socat and WST**.

<!-- more -->

## What was new

- **Six methods** in one menu: iptables, GOST, Dokodemo-door, HAProxy, socat, WST.
- **Works on many Linux systems** (apt, dnf, yum) since 0.0.2 (October 2024).
- **Safe:** asks before uninstalling or reinstalling, and checks the ports you type.
- Pairs with relay domains in Hiddify Manager.

<div align=center>

<img src="/assets/blog/2nd-anniversary/16171834.webp" alt="Hiddify relay builder" width="50%" />
</div>

## Today

Today these tools live inside the Hiddify app and Hiddify Manager. Start with the app, or run your own server.

<div class="hi-cta-wrap"><a class="hi-cta" href="/app/How-to-install-Hiddify-app/">Download the Hiddify app</a></div>

??? note "For experts"
    - We introduced it in May 2024; the first tagged release is 0.0.1 (5 July 2024). The repository dates from May 2023.
    - Sources: [hiddify-relay](https://github.com/hiddify/hiddify-relay)

## Related articles

- [HiddifyCli and Docker: Hiddify without a screen](HiddifyCli-and-Docker.md)
- [Hiddify extensions: anyone can add a feature](Hiddify-Extensions.md)
- [Relay domains in Hiddify Manager](/manager/domain-worker-cdn-and-tunneling/How-to-add-relay-domain-to-Hiddify-manager/)
- [Hiddify turns four](4th-anniversary.md)
