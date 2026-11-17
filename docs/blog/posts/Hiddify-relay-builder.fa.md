---
draft: false
date: 2024-07-05
slug: hiddify-relay-builder
authors:
  - hiddify
categories:
  - Project
tags:
  - هیدیفای
  - نسخهٔ تازه
description: "یک اسکریپت که سرور میانی (تونل) را با روش‌هایی که کار می‌کنند می‌سازد: iptables، GOST، Dokodemo-door، HAProxy، socat و WST."
cover: /assets/blog/covers/Hiddify-relay-builder-fa.webp
date_fa: ۱۵ تیر ۱۴۰۳
---

# میانی‌ساز هیدیفای: سرور تونل در چند دقیقه

<!-- made by .cache/blog/history_gen.py -->

!!! abstract "در ۳۰ ثانیه"
    سرور میانی داخل کشور ترافیک شما را به سرور اصلی خارج می‌رساند. **میانی‌ساز هیدیفای** (اولین نسخه ۱۵ تیر ۱۴۰۳)
    آن را با یک اسکریپت و روش‌هایی که کار می‌کنند می‌سازد: **iptables، GOST، Dokodemo-door، HAProxy، socat و
    WST**.

<!-- more -->

## چه چیزهایی تازه بود

- **شش روش** در یک منو: iptables، GOST، Dokodemo-door، HAProxy، socat، WST.
- **روی سیستم‌های مختلف لینوکس کار می‌کند** (apt، dnf، yum) از نسخهٔ ۰.۰.۲ (مهر ۱۴۰۳).
- **امن:** پیش از حذف یا نصب دوباره می‌پرسد و پورت‌هایی را که وارد می‌کنید بررسی می‌کند.
- با دامنه‌های relay در هیدیفای‌منیجر جفت می‌شود.

<div align=center>

<img src="/assets/blog/2nd-anniversary/16171834.webp" alt="میانی‌ساز هیدیفای" width="50%" />
</div>

## امروز

امروز این ابزارها داخل اپ هیدیفای و هیدیفای‌منیجر هستند. با اپ شروع کنید، یا سرور خودتان را راه بیندازید.

<div class="hi-cta-wrap"><a class="hi-cta" href="/fa/app/How-to-install-Hiddify-app/">دانلود اپ هیدیفای</a></div>

??? note "برای کاربران حرفه‌ای"
    - آن را در اردیبهشت ۱۴۰۳ معرفی کردیم؛ اولین نسخهٔ برچسب‌دار ۰.۰.۱ (۱۵ تیر ۱۴۰۳) است. مخزن از خرداد ۱۴۰۲ هست.
    - منبع‌ها: [hiddify-relay](https://github.com/hiddify/hiddify-relay)

## مقاله‌های مرتبط

- [HiddifyCli و داکر: هیدیفای بدون صفحه](HiddifyCli-and-Docker.md)
- [افزونه‌های هیدیفای: هر کسی می‌تواند قابلیتی اضافه کند](Hiddify-Extensions.md)
- [دامنهٔ relay در هیدیفای‌منیجر](/fa/manager/domain-worker-cdn-and-tunneling/How-to-add-relay-domain-to-Hiddify-manager/)
- [هیدیفای چهار ساله شد](4th-anniversary.md)
