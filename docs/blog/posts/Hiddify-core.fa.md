---
draft: false
date: 2023-09-11
slug: hiddify-core
authors:
  - hiddify
categories:
  - Project
tags:
  - هیدیفای
  - نسخهٔ تازه
description: "موتور زیر اپ هیدیفای، ساخته‌شده روی sing-box خود ما: همان قابلیت‌ها روی اندروید، iOS، ویندوز، مک و لینوکس."
cover: /assets/blog/covers/Hiddify-core-fa.webp
date_fa: ۲۰ شهریور ۱۴۰۲
---

# هستهٔ هیدیفای: یک موتور برای همهٔ سیستم‌ها

<!-- made by .cache/blog/history_gen.py -->

!!! abstract "در ۳۰ ثانیه"
    همراه اولین اپ Hiddify Next، در ۲۰ شهریور ۱۴۰۲، **هستهٔ هیدیفای** ۰.۱ را منتشر کردیم: یک موتور که روی
    **اندروید، iOS، ویندوز، مک و لینوکس** یکسان کار می‌کند. روی **hiddify-sing-box** ساخته شده؛ نسخهٔ ما از
    sing-box با قابلیت‌هایی که نسخهٔ اصلی ندارد، مثل ترفندهای TLS، وارپ و سایفون.

<!-- more -->

## چه چیزهایی تازه بود

- **یک موتور، پنج سیستم:** اپ همه‌جا یک شکل و یک رفتار دارد.
- **hiddify-sing-box** (از اردیبهشت ۱۴۰۲): فرگمنت و ترفندهای TLS، وارپ (WireGuard، AmneziaWG، MASQUE)، سایفون، XHTTP و تونل‌های DNS.
- **ray2sing:** لینک‌های VLESS، VMess، تروجان، Hysteria2، SSH، وایرگارد و وارپ را می‌خواند و به کانفیگ sing-box تبدیل می‌کند.
- **Xray داخل هسته** (هستهٔ ۱.۹، تیر ۱۴۰۳) برای کانفیگ‌هایی که sing-box اجرا نمی‌کند.
- **بیش از ۱۰۰ نسخه**؛ حدود ۸۸۰ هزار دانلود هسته و ۱٬۰۶۰٬۰۰۰ دانلود sing-box از گیت‌هاب.
- **هستهٔ ۵** (مهر ۱۴۰۵): بارگذاری دوباره بدون قطع اتصال، زنجیره برای امنیت بیشتر و رفع فیلتر پروکسی.

<div align=center>

<img src="/assets/blog/2nd-anniversary/34829e2e.svg" alt="Hiddify" width="40%" />
</div>

## امروز

امروز این ابزارها داخل اپ هیدیفای و هیدیفای‌منیجر هستند. با اپ شروع کنید، یا سرور خودتان را راه بیندازید.

<div class="hi-cta-wrap"><a class="hi-cta" href="/fa/app/How-to-install-Hiddify-app/">دانلود اپ هیدیفای</a></div>

??? note "برای کاربران حرفه‌ای"
    - مخزن هسته در ۲۵ مرداد ۱۴۰۲ و ray2sing در ۱۸ شهریور ۱۴۰۲ ساخته شدند.
    - منبع‌ها: [hiddify-core 0.1.0](https://github.com/hiddify/hiddify-core/releases/tag/v0.1.0)، [hiddify-sing-box](https://github.com/hiddify/hiddify-sing-box)، [ray2sing](https://github.com/hiddify/ray2sing)

## مقاله‌های مرتبط

- [HiddifyNG و HiddifyN: اپ‌های ما برای اندروید و ویندوز](HiddifyNG-and-HiddifyN.md)
- [اسکنر ریالتی هیدیفای: بهترین SNI برای ریالتی](Hiddify-Reality-Scanner.md)
- [راهنمای هستهٔ هیدیفای](/fa/core/)
- [هیدیفای چهار ساله شد](4th-anniversary.md)
