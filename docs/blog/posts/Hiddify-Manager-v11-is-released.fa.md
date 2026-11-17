---
draft: false
date: 2025-07-11
authors:
  - hiddify
categories:
  - Manager
tags:
  - هیدیفای
  - نسخهٔ تازه
description: هیدیفای‌منیجر ۱۱ با XHTTP و دامنه‌های جدا برای آپلود و دانلود، QUIC، سیستم پروکسی بازسازی‌شده، و تا نصف مصرف رم.
cover: /assets/blog/covers/Hiddify-Manager-v11-is-released-fa.webp
date_fa: ۲۰ تیر ۱۴۰۴
---

# هیدیفای‌منیجر ۱۱ منتشر شد

!!! abstract "در ۳۰ ثانیه"
    هیدیفای‌منیجر **۱۱.۰.۰** در ۱۹ تیر ۱۴۰۴ منتشر شد. **XHTTP** آورده که آپلود و دانلود را می‌تواند از
    **دامنه‌های جدا** بفرستد، **QUIC** دارد، **سیستم پروکسی بازسازی‌شده‌ای** که هر تنظیمش قابل تغییر است، و
    **تا نصف رم** نسخهٔ قبل مصرف می‌کند.

<!-- more -->

## چه چیزی برای شما عوض می‌شود

- **پروتکل XHTTP**، همچنین همراه با ریالتی (ریالتی XHTTP).
- **دامنه‌های جدا برای آپلود و دانلود.** آپلود و دانلود می‌توانند دامنه یا ALPN جدا داشته باشند و ترافیک
  سخت‌تر شناسایی می‌شود.
- **QUIC**، کنار H1، H2، WS و HTTPUpgrade، و با CDN هم کار می‌کند.
- **سیستم پروکسی بازسازی‌شده**: هر پارامتر هر پروکسی را به دلخواه تغییر دهید.
- **کار دسته‌جمعی روی کاربران**: حذف، فعال‌سازی، غیرفعال‌سازی، یا بازنشانی روز و حجم چند کاربر با هم.
- **رمز برای پنل ادمین**، یک قفل اضافه روی دسترسی ادمین.
- **تا ۵۰٪ رم کمتر** و مصرف CPU پایین‌تر.
- **نصب سریع‌تر و ساده‌تر.**
- **IP به جای دامنه** در پروکسی‌ها، و User-Agent دلخواه.
- **انتخاب بهتر IP برای دامنه‌های AutoCDN**، با User-Agentهای تازه و تصادفی.
- **عبور سایت‌های دلخواه از وارپ** حالا برای Hysteria، Shadowsocks و TUIC هم.
- **نسخهٔ داکر** (اولین نسخهٔ آزمایشی).
- کلی بهبود در ظاهر و کار با پنل.

## باید به‌روزرسانی کنم؟

نسخه‌های تازه‌تر (۱۲، ۱۳ و ۱۴) منتشر شده‌اند و به‌روزرسانی شما را مستقیم به آخرین نسخه می‌برد. اول یک
[پشتیبان](/fa/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/) بگیرید،
بعد [راهنمای به‌روزرسانی هیدیفای‌منیجر](/fa/manager/configuration-and-advanced-settings/How-to-update-Hiddify-panel/) را دنبال کنید.

<div class="hi-cta-wrap"><a class="hi-cta" href="/fa/manager/installation-and-setup/guide/">نصب یا به‌روزرسانی هیدیفای‌منیجر</a></div>

??? note "برای کاربران حرفه‌ای: تغییرات بیشتر نسخهٔ ۱۱"
    - هستهٔ Xray نسخهٔ ۲۵.۶؛ پایتون ۳.۱۳.
    - نسخهٔ تازهٔ HAProxy (فقط روی اوبونتو ۲۴.۰۴)، برای مسیریابی دقیق‌تر و سریع‌تر.
    - به‌روزرسانی لینک اشتراک sing-box.
    - تغییرات از ۱۰.۸۶.۴: [Hiddify-Manager](https://github.com/hiddify/Hiddify-Manager/compare/v10.86.4...v11.0.0)
      و [نسخهٔ ۱۱.۰.۰](https://github.com/hiddify/Hiddify-Manager/releases/tag/v11.0.0).

## مقاله‌های مرتبط

- [هیدیفای‌منیجر ۱۰.۸۰: نصب با داکر](Hiddify-Manager-v10-80-is-released.md)
- [هیدیفای‌منیجر ۱۲ منتشر شد](Hiddify-Manager-v12-is-released.md)
- [به‌روزرسانی هیدیفای‌منیجر](/fa/manager/configuration-and-advanced-settings/How-to-update-Hiddify-panel/)
- [نصب هیدیفای با داکر](/fa/manager/installation-and-setup/Install-Hiddify-using-Docker/)
