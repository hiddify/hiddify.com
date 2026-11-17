---
draft: false
date: 2026-11-07
slug: router-mode
authors:
  - hiddify
categories:
  - Project
tags:
  - هیدیفای
  - نسخهٔ تازه
description: "حالت روتر همهٔ دستگاه‌های شبکهٔ شما را پشت هیدیفای می‌برد، بدون تنظیم روی گوشی، تلویزیون یا کنسول."
cover: /assets/blog/covers/Router-mode-fa.webp
date_fa: ۱۶ آبان ۱۴۰۵
---

# حالت روتر: کل خانه پشت هیدیفای

<!-- made by .cache/blog/history_gen.py -->

!!! abstract "در ۳۰ ثانیه"
    در ۱۶ آبان ۱۴۰۵ هستهٔ هیدیفای **حالت روتر** گرفت. آن را روی یک روتر **OpenWrt** یا هر دروازهٔ **لینوکس** اجرا
    کنید تا همهٔ دستگاه‌های شبکه (گوشی، تلویزیون، کنسول، دستگاه‌های هوشمند) از هیدیفای بگذرند، **بدون هیچ تنظیمی
    روی خودشان**.

<!-- more -->

## چه چیزهایی تازه بود

- **TCP، UDP و ICMP** از پروکسی.
- **بدون تنظیم روی دستگاه‌ها**؛ SSH و صفحهٔ وب روتر کار می‌کنند.
- **بستهٔ OpenWrt** با نام `hiddify-core`، با حالت روتر به‌طور پیش‌فرض برای نصب‌های تازه، و مخزن‌های opkg و apk.
- **هر دروازهٔ لینوکس:** `hiddify-core run -c <profile> --router`.
- **در اپ**: حالت روتر در لینوکس VPN را با کل شبکه شریک می‌شود (نسخه‌های آزمایشی ۵.۹).

## امروز

امروز این ابزارها داخل اپ هیدیفای و هیدیفای‌منیجر هستند. با اپ شروع کنید، یا سرور خودتان را راه بیندازید.

<div class="hi-cta-wrap"><a class="hi-cta" href="/fa/app/How-to-install-Hiddify-app/">دانلود اپ هیدیفای</a></div>

??? note "برای کاربران حرفه‌ای"
    - بسته‌ها برای هر نسخه از ۱۲ آبان ۱۴۰۵.
    - منبع‌ها: [router mode docs](https://github.com/hiddify/hiddify-core/blob/main/docs/router-mode.md)

## مقاله‌های مرتبط

- [تونل‌های DNS در هیدیفای: وقتی تقریباً همه‌چیز بسته است](DNS-tunnels-in-Hiddify.md)
- [حالت روتر در لینوکس](/fa/app/Router-mode-on-Linux/)
- [هیدیفای چهار ساله شد](4th-anniversary.md)
