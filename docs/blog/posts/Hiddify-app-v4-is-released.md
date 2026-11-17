---
draft: false
date: 2026-02-19
slug: hiddify-app-4
authors:
  - hiddify
categories:
  - App
tags:
  - Hiddify
  - Release
description: Hiddify app 4 brings free profiles, Extra security, automatic app lists for per-app proxy, and new protocols.
cover: /assets/blog/covers/Hiddify-app-v4-is-released-en.webp
---

# Hiddify app 4 is out

!!! abstract "In 30 seconds"
    Hiddify app **4.0.4** came out on 19 February 2026, and **4.1** followed in March. It has
    **free profiles** you can add with one tap, an **Extra security** mode, ready-made **app lists** for
    the per-app proxy on Android, and new ways to connect such as **Naive, AmneziaWG and DNSTT**.

<!-- more -->

## What changes for you

- **Free profiles.** Add free WARP and Psiphon profiles from the app, without a subscription link.
- **Extra security.** Put WARP behind your own proxy, so websites see a Cloudflare IP and your proxy
  provider can't see where you go.
- **Per-app proxy that picks the apps for you** (Android). The app downloads a list of apps for your
  region and keeps it up to date; you can still change it by hand.
- **New protocols**: Naive, AmneziaWG, raw WireGuard configs with "noise", and (4.1) DNSTT for heavy
  filtering.
- **Quick settings** on the home page, and settings sorted into clearer groups.
- **More about your connection**: your IP's country with its flag, and upload/download speed and the
  active profile in the Android notification.
- **Balancer strategies** (4.1): choose how the app spreads traffic over the proxies of a profile.
- **Fragment** (4.1): split the TLS handshake into packets to get past some filters.
- **Desktop**: start on login on macOS, the window opens where you left it, and a raw AppImage on Linux.
- You can now **delete the active profile**.

## Should I update?

Version 5 is out now, and it is better in every way. Update to the latest version from your store or
from [How to install the Hiddify app](/app/How-to-install-Hiddify-app/).

<div class="hi-cta-wrap"><a class="hi-cta" href="/app/How-to-install-Hiddify-app/">Download the Hiddify app</a></div>

??? note "For experts: more changes in 4"
    - More inbounds on desktop: TPROXY, REDIRECT and DIRECT.
    - Route rules with regex checks; endpoint in the JSON editor.
    - `enable-warp` in profile headers; WARP license errors shown on connection failure.
    - Region detection from time zone and locale (4.1).
    - Changes: [2.5.7 → 4.0.4](https://github.com/hiddify/hiddify-app/compare/v2.5.7...v4.0.4),
      [4.0.4 → 4.1.2](https://github.com/hiddify/hiddify-app/compare/v4.0.4...v4.1.2).

## Related articles

- [Hiddify app 2: config editor and two cores](Hiddify-app-v2-is-released.md)
- [How to install the Hiddify app](/app/How-to-install-Hiddify-app/)
- [Free profiles in the Hiddify app](/app/Free-profiles-in-Hiddify-app/)
- [Routing in the Hiddify app](/app/Routing-in-Hiddify-app/)
