---
title: آموزش راه‌اندازی پروکسی تلگرام در هیدیفای‌منیجر
weight: -120
---

<div dir="rtl" markdown=1>
# آموزش راه‌اندازی پروکسی تلگرام در هیدیفای‌منیجر
یکی از قابلیت‌های خوب پنل هیدیفای‌منیجر، ارائه پروکسی تلگرام است. دو نوع پروکسی تلگرام وجود دارد که در ادامه توضیح داده می‌شوند.

* **MTProxy FakeTLS**: پروکسی MTProto تلگرام در قالب TLS (لینک‌های `tg://proxy`). به دامنه مستقیم یا رله نیاز دارد.
* **پروکسی وب تلگرام**: پروکسی تلگرام روی HTTPS، روی همه دامنه‌های دارای گواهی معتبر، از جمله CDN (لینک‌های `tg://webproxy`).

## فعال‌سازی پروکسی تلگرام
* برای این کار در منوی کناری پنل روی **پروتکل‌ها** کلیک کنید و گزینه **فعال کردن MTProxy FakeTLS** و/یا **فعال کردن پروکسی وب تلگرام** را روشن کنید و سپس ذخیره کنید.

<div align=center markdown=1>
![کلیدهای پروکسی تلگرام در صفحه پروتکل‌ها](/assets/manager/How-to-set-up-Telegram-proxy-on-Hiddify/fa-protocols.webp)

</div>

* همین کلیدها در کارت **کانفیگ‌های تلگرام** در صفحه **تنظیمات** هم وجود دارند.

<div align=center markdown=1>
![کارت کانفیگ‌های تلگرام در تنظیمات](/assets/manager/How-to-set-up-Telegram-proxy-on-Hiddify/fa-telegram-configs.webp)

</div>

* در صورت نمایش پیغام مربوط به `اعمال تغییرات`، حتما دکمه را فشار دهید تا تغییرات در سرور اعمال گردند. این کار را از منوی **اقدامات** هم می‌توانید انجام دهید: در کارت **اعمال تغییرات** روی **الان اعمال کن** بزنید.

* حالا کاربران پروکسی‌ها را در صفحهٔ کاربری خود پیدا می‌کنند: در منوی بالای صفحه، **پروکسی تلگرام** را باز می‌کنند. این صفحه برای هر آدرس سرور یک پروکسی و اگر **پروکسی وب تلگرام** روشن باشد، برای هر دامنه یک پروکسی **Web** نشان می‌دهد. با زدن روی هر ردیف، کد QR آن، لینک با دکمهٔ کپی و دکمهٔ **بازکردن تلگرام** نمایش داده می‌شود که پروکسی را با یک ضربه به تلگرام اضافه می‌کند.

![صفحهٔ پروکسی تلگرام در صفحهٔ کاربری](/assets/manager/How-to-set-up-Telegram-proxy-on-Hiddify/fa-user-telegram-proxy.webp)

## فعال‌سازی تبلیغات
برای این کار ربات [MTProxybot](https://t.me/MTProxybot) را جستجو نمایید.

<div align=center markdown=1>
![proxybot](/assets/manager/How-to-set-up-Telegram-proxy-on-Hiddify/gh-3fed75f8-0580-469a-a306-e01d385ee6ec.webp)

</div>

* حالا پروکسی‌ای که ساخته شده را وارد بات کنید. ممکن است مقداری زمان بگیرد تا به صورت کامل فعال شود.

* سپس در تنظیمات پنل در فیلد `تگ تبلیغاتی تلگرام` آدرس مورد نظر خود برای تبلیغ را وارد نمایید. مثلا می‌توانید آدرس اکانت پشتیبانی خود را بدهید.

* کار تمام است.

## مقاله‌های مرتبط

- [بات تلگرام پنل](/fa/manager/configuration-and-advanced-settings/How-to-set-up-and-use-Telegram-bot-on-Hiddify-panel/)
- [فعال‌سازی وارپ](/fa/manager/configuration-and-advanced-settings/How-to-activate-WARP-on-the-Hiddify-panel/)
- [استفاده از IPv6](/fa/manager/configuration-and-advanced-settings/IPv6-usage-guide/)
- [آشنایی کامل با پنل و تنظیمات آن](/fa/manager/configuration-and-advanced-settings/How-to-configure-Hiddify-panel-properly/)

</div>
