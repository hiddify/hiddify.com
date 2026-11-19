---
draft: false
date: 2023-04-19
slug: hiddify-panel-4
authors:
  - hiddify
categories:
  - Manager
tags:
  - Hiddify
  - Release
description: "Hiddify Manager 4 added the Reality protocol, admins and agents with their own users and limits, and backups and messages through Telegram."
cover: /assets/blog/covers/Hiddify-Panel-v4-en.webp
---

# Hiddify Manager 4: Reality and admins with levels

<!-- made by .cache/blog/history_gen.py -->

!!! abstract "In 30 seconds"
    **Hiddify Manager 4** came out on 19 April 2023. Its big news was **Reality**, a protocol that looks like a
    visit to a real, well-known site. It also brought **admins with levels**: admins and agents with their own
    users, usage and limits.

<!-- more -->

## What was new

- **Reality**, with a check that the Reality settings are right and a warning when they are not.
- **Admins with levels:** each admin has their own users and usage; "agents" can sell to their own users.
- **Permissions and limits** for sub-admins (4.1–4.2), IP limits and a minimum of valid users (4.5).
- **Telegram:** backups sent to Telegram, and messages to users from the panel.
- **A better domain manager** and a parent panel.
- **Confirm before dangerous actions.**
- **New colours** in an Apple style (4.3), and a better result page (4.5).

<div align=center>

<img src="/assets/blog/2nd-anniversary/7876f1e2.webp" alt="Reality in Hiddify Manager 4" width="50%" />
</div>

## Today

Hiddify Manager is at version 14 now. Install the latest version, or update yours from the panel (take a [backup](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/) first).

<div class="hi-cta-wrap"><a class="hi-cta" href="/manager/installation-and-setup/guide/">Install Hiddify Manager</a></div>

??? note "For experts"
    - Until March 2024 the panel had its own version numbers, and the server package (then called Hiddify Config) had others: Hiddify Manager 4 shipped with package 9.0. Since 10.10 both share one number.
    - Reality on the server: Xray 1.8.1 behind HAProxy.
    - Sources: [panel HISTORY 4.0.0](https://github.com/hiddify/hiddifypanel/blob/main/HISTORY.md), [package 9.0.0](https://github.com/hiddify/Hiddify-Manager/releases/tag/v9.0.0), [Reality commit](https://github.com/hiddify/Hiddify-Manager/commit/f6cec680)

## Related articles

- [Hiddify Manager 3: a new look and dark mode](Hiddify-Panel-v3.md)
- [Hiddify Manager 5: domain types and usage in the link](Hiddify-Panel-v5.md)
- [How to use Reality on Hiddify](/manager/configuration-and-advanced-settings/How-to-use-Reality-on-Hiddify/)
- [Hiddify Manager 14 is out](Hiddify-Manager-v14-is-released.md)
