---
draft: false
date: 2024-07-29
slug: hiddify-manager-10-70
authors:
  - hiddify
categories:
  - Manager
tags:
  - هیدیفای
  - نسخهٔ تازه
description: "تابستان ۱۴۰۳: راه‌اندازی سریع (۱۰.۵۰)، و بعد SplitHTTP، فرگمنت Xray، وایرگارد در پنل و ویرایشگر HTML (۱۰.۷۰)."
cover: /assets/blog/covers/Hiddify-Manager-v10-70-is-released-fa.webp
date_fa: ۸ مرداد ۱۴۰۳
---

# هیدیفای‌منیجر ۱۰.۷۰: SplitHTTP و فرگمنت

<!-- made by .cache/blog/history_gen.py -->

!!! abstract "در ۳۰ ثانیه"
    هیدیفای‌منیجر **۱۰.۷۰** در ۸ مرداد ۱۴۰۳ منتشر شد. **SplitHTTP**، راهی تازه برای رد شدن از فیلتر از روی CDN،
    **فرگمنت Xray**، خروجی وایرگارد در پنل و ویرایشگری برای متنی که کاربران می‌بینند را آورد. دو هفته پیش‌تر،
    **۱۰.۵۰** مرحله‌های **راه‌اندازی سریع** سرور تازه را آورده بود.

<!-- more -->

## چه چیزهایی تازه بود

- **SplitHTTP** (Xray)، همچنین روی HTTP/3 (QUIC)، که پشت CDN خوب کار می‌کند.
- **فرگمنت Xray**، و تست URL دلخواه.
- خروجی **وایرگارد** در پنل.
- **ویرایشگر HTML** برای متن دلخواه در صفحهٔ کاربر.
- **راه‌اندازی سریع** (۱۰.۵۰): چند قدم برای سرور تازه، با چند سرویس که به‌طور پیش‌فرض خاموش‌اند.
- **مدیریت بهتر IPv4 و IPv6** (۱۰.۵۰)، و ریالتی و VLESS جدا روشن می‌شوند (۱۰.۳۰).
- **سرور سبک‌تر** (۱۰.۲۰): کانفیگ‌های Xray یا sing-box که لازم نیستند خاموش می‌شوند تا حافظه آزاد بماند.

## امروز

هیدیفای‌منیجر حالا در نسخهٔ ۱۴ است. آخرین نسخه را نصب کنید، یا نسخهٔ خودتان را از پنل به‌روزرسانی کنید (اول یک [پشتیبان](/fa/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/) بگیرید).

<div class="hi-cta-wrap"><a class="hi-cta" href="/fa/manager/installation-and-setup/guide/">نصب هیدیفای‌منیجر</a></div>

??? note "برای کاربران حرفه‌ای"
    - نسخهٔ ۱۰.۲۰ (۲۴ فروردین ۱۴۰۳) بررسی‌کنندهٔ سایت‌های وارپ و «روزهای مانده تا بازنشانی» را هم آورد؛ پنل به Python venv رفت.
    - در اردیبهشت ۱۴۰۳ میانی‌ساز هیدیفای را هم برای سرورهای تونل منتشر کردیم (GOST، HAProxy، Socat، iptables و بقیه).
    - منبع‌ها: [SplitHTTP](https://github.com/hiddify/Hiddify-Manager/commit/529f6bc0)، [Xray fragment](https://github.com/hiddify/Hiddify-Manager/commit/f45f5d10)، [quick setup (10.50)](https://github.com/hiddify/Hiddify-Manager/commit/9372c3cb)

## مقاله‌های مرتبط

- [هیدیفای‌منیجر ۱۰.۱۰: شدوساکس ۲۰۲۲، HTTPUpgrade و وایرگارد](Hiddify-Manager-v10-10-is-released.md)
- [هیدیفای‌منیجر ۱۰.۸۰: نصب با داکر](Hiddify-Manager-v10-80-is-released.md)
- [هیدیفای‌منیجر ۱۴ منتشر شد](Hiddify-Manager-v14-is-released.md)
