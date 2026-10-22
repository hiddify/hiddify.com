---
title: تنظیم TLS برای افزایش امنیت
---

<div dir=rtl markdown=1>

# تنظیم TLS برای افزایش امنیت

این صفحه به شما نشان می‌دهد چطور اتصال‌های TLS که از CDN عبور می‌کنند را سخت‌تر قابل‌تشخیص کنید. اگر با هیدیفای از دامنه CDN کلودفلر استفاده می‌کنید و اتصال‌هایتان روی بعضی اپراتورها ناپایدار است، این صفحه به کار شما می‌آید.

**TLS** همان رمزنگاری است که از اتصال‌های `https` محافظت می‌کند. سیستم‌های فیلترینگ می‌توانند الگوهای ترافیک TLS را بررسی کنند و نسخه‌های قدیمی‌تر TLS الگوهای بیشتری را نشان می‌دهند. **TLS 1.3**، جدیدترین نسخه، بخش بیشتری از شروع اتصال را رمزنگاری می‌کند و تشخیص آن سخت‌تر است.

## تنظیم حداقل نسخه TLS در Cloudflare

**نشانه:** کانفیگ‌های CDN (کلودفلر) روی بعضی اپراتورها وصل می‌شوند ولی روی بعضی دیگر ناپایدارند یا وصل نمی‌شوند.

**علت محتمل:** Cloudflare هنوز نسخه‌های قدیمی‌تر TLS را برای دامنه شما می‌پذیرد.

**راه‌حل:** تنظیم کنید که Cloudflare فقط TLS 1.3 را بپذیرد.

1. وارد حساب Cloudflare خود شوید و دامنه‌تان را انتخاب کنید.
2. از منو، **SSL/TLS** و سپس **Edge Certificates** را باز کنید.
3. گزینه **Minimum TLS Version** را پیدا کنید و آن را روی **TLS 1.3** بگذارید.

<div align=center markdown=1>
![تنظیم Minimum TLS Version روی TLS 1.3 در کلودفلر](https://github.com/hiddify/hiddify-config/assets/125398461/69edd121-028f-43f5-87ca-35cb5be00c0f)
</div>

**بررسی:** با دستگاهی که روی اپراتور مشکل‌دار است دوباره وصل شوید.

**اگر هنوز کار نمی‌کند:** یک ساب‌دامین جدید امتحان کنید. ممکن است سیستم فیلترینگ ساب‌دامین قبلی را شناسایی کرده باشد.

## TLS 1.3 روی دستگاه شما

**اپ Hiddify** و دیگر اپ‌های مبتنی بر Xray یا sing-box، TLS داخلی خودشان را دارند. این اپ‌ها از تنظیمات TLS سیستم‌عامل استفاده نمی‌کنند، پس معمولاً لازم نیست چیزی را روی گوشی یا کامپیوتر خود تغییر دهید.

ویندوز ۱۱، macOS و بیشتر نسخه‌های جدید لینوکس هم TLS 1.3 را برای برنامه‌های خودشان از قبل فعال کرده‌اند.

??? note "اختیاری: فعال کردن TLS 1.2 و 1.3 در تنظیمات ویندوز ۱۰"
    این کار فقط روی برنامه‌هایی اثر دارد که از TLS داخلی ویندوز استفاده می‌کنند. مایکروسافت TLS 1.3 را در ویندوز ۱۰ به‌طور رسمی پشتیبانی نمی‌کند، پس ممکن است این کار اثری نداشته باشد. فقط اگر با رجیستری ویندوز آشنا هستید آن را تغییر دهید.

    1. برنامه **Notepad** را باز کنید و متن زیر را در آن بچسبانید:

        ```ini
        Windows Registry Editor Version 5.00

        [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client]
        "DisabledByDefault"=dword:00000000
        "Enabled"=dword:00000001

        [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server]
        "DisabledByDefault"=dword:00000000
        "Enabled"=dword:00000001

        [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.3\Client]
        "DisabledByDefault"=dword:00000000
        "Enabled"=dword:00000001

        [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.3\Server]
        "DisabledByDefault"=dword:00000000
        "Enabled"=dword:00000001
        ```

    2. فایل را با پسوند `.reg` ذخیره کنید، مثلاً `tls.reg`. در فهرست **Save as type** گزینه **All files** را انتخاب کنید تا پسوند فایل `.txt` نشود.
    3. روی فایل دوبار کلیک کنید و پیغام‌ها را تأیید کنید.
    4. کامپیوتر را ری‌استارت کنید.
    5. برای بررسی: کلیدهای `Win+R` را بزنید، `regedit` را بنویسید و Enter بزنید. به مسیری که در تصویر زیر می‌بینید بروید. نسخه‌های TLS فعال‌شده آنجا دیده می‌شوند.

    ![کلیدهای SCHANNEL Protocols در رجیستری ویندوز](https://github.com/hiddify/hiddify-config/assets/125398461/53b259f3-267a-4e7f-90b2-8f5ce3a216ca)

!!! warning "هشدار"
    نسخه‌های قبلی این صفحه **SSL 3.0** را هم فعال می‌کردند. SSL 3.0 قدیمی و ناامن است. اگر از آن فایل استفاده کرده‌اید، کلید `SSL 3.0` را در همان مسیر رجیستری پاک کنید.

</div>
