---
draft: false
date: 2026-03-05
slug: dns-tunnels
authors:
  - hiddify
categories:
  - Project
tags:
  - هیدیفای
  - نسخهٔ تازه
description: "DNSTT، VayDNS، MasterDNS و Soar ترافیک را داخل پرسش‌های DNS می‌برند: کند، ولی وقتی تقریباً هیچ راه دیگری کار نمی‌کند، شاید کار کنند."
cover: /assets/blog/covers/DNS-tunnels-in-Hiddify-fa.webp
date_fa: ۱۴ اسفند ۱۴۰۴
---

# تونل‌های DNS در هیدیفای: وقتی تقریباً همه‌چیز بسته است

<!-- made by .cache/blog/history_gen.py -->

!!! abstract "در ۳۰ ثانیه"
    از ۱۴ اسفند ۱۴۰۴ اپ هیدیفای و هیدیفای‌منیجر **تونل‌های DNS** را یاد گرفتند. این تونل‌ها ترافیک را داخل
    پرسش‌های DNS پنهان می‌کنند، که کمتر کامل بسته می‌شوند. کندند، ولی در بدترین قطعی‌ها هنوز می‌توانند وصل شوند:
    **DNSTT**، **VayDNS**، **MasterDNS** و **Soar**.

<!-- more -->

## چه چیزهایی تازه بود

- **DNSTT** در هسته (اسفند ۱۴۰۴)، و بعد چند resolver با هم.
- **VayDNS** با انتخاب خودکار resolverها.
- **MasterDNS و Soar** (آبان ۱۴۰۵)؛ MasterDNS با resolverهای کم، با مخزن چند-resolver ما حدود ۸ برابر سریع‌تر است.
- **لینک‌هایی** مثل `dnst://`، `masterdns://` و `soar://` در اپ باز می‌شوند.
- **در پنل** از هیدیفای‌منیجر ۱۳.

## امروز

امروز این ابزارها داخل اپ هیدیفای و هیدیفای‌منیجر هستند. با اپ شروع کنید، یا سرور خودتان را راه بیندازید.

<div class="hi-cta-wrap"><a class="hi-cta" href="/fa/app/How-to-install-Hiddify-app/">دانلود اپ هیدیفای</a></div>

??? note "برای کاربران حرفه‌ای"
    - این تونل‌ها پروژه‌های تیم‌های دیگرند (net2share، masterking32، Lantern و دیگران)؛ ما آن‌ها را یکپارچه کردیم. از سازندگانشان سپاسگزاریم.
    - منبع‌ها: [core 4.1.0](https://github.com/hiddify/hiddify-core/releases/tag/v4.1.0)، [protocols docs](https://github.com/hiddify/hiddify-sing-box/tree/main/docs/hiddify/features/protocols)

## مقاله‌های مرتبط

- [افزونه‌های هیدیفای: هر کسی می‌تواند قابلیتی اضافه کند](Hiddify-Extensions.md)
- [حالت روتر: کل خانه پشت هیدیفای](Router-mode.md)
- [هیدیفای‌منیجر ۱۳ منتشر شد](Hiddify-Manager-v13-is-released.md)
- [هیدیفای چهار ساله شد](4th-anniversary.md)
