[**🇺🇸 English**](https://github.com/hiddify/hiddify-config/wiki/TLS-setting-for-increased-security)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/%D9%87%D9%85%D9%87-%D8%A2%D9%85%D9%88%D8%B2%D8%B4%E2%80%8C%D9%87%D8%A7-%D9%88-%D9%88%DB%8C%D8%AF%D8%A6%D9%88%D9%87%D8%A7"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/3704cd84-eee6-4c45-abe7-3c02936bbebb" /></a>

<div dir=rtl markdown=1>


# تنظیم TLS برای افزایش امنیت
با توجه به شدت فیلترینگ و قابلیت تشخیص الگوهای بسته‌های اینترنتی روی پروتکل‌های مبتنی بر TLS نیاز است که تدابیری اندیشیده شود که از این کار لویری کند. در ادامه چند راه‌کار برای این موضوع بررسی می‌شوند.

## تنظیم نسخه TLS در CDN
برای استفاده از کانکشن‌های مبتنی بر CDN نیاز است در تنظیمات دامنه خود نسخه TLS را روی بالاترین حالت قرار دهید.

وارد اکانت  `Cloudflare` خودتون شوید و در بخش `Domain` گزینه `SSL/TLS` را بزنید. سپس در `Edge Certificates` حداقل نسخه TLS را با استفاده از فیلد `Minimum TLS Version` روی `TLS 1.3` قرار دهید.

<div align=center markdown=1>
![tls1.3 در کلافلر](https://github.com/hiddify/hiddify-config/assets/125398461/69edd121-028f-43f5-87ca-35cb5be00c0f)

</div>

> دقت شود اگر این بخش روی گزینه `TLS 1.3` نباشد، روی بعضی اپراتورها ممکن است دچار اختلال شوید.

> در صورتی که با تغییر نسخه TLS همچنان دچار اختلال بودید، یک ساب‌دامین جدید امتخان کنید، چون ممکن است ساب‌دامین قبلی توسط سیستم فیلترینگ شناسایی شده باشد.


## قعال‌سازی TLS 1.3 در کلاینت
روی ویندوز ۱۱ و سیستم عامل مک و اکثر نسخه‌های جدید لینوکس ، TLS 1.3 به صورت پیش‌فرض فعال است. در اینجا نحوه فعال‌سازی این نسخه از TLS برای ویندزو ۱۰ توضیح داده می‌شود.

### فعال‌سازی TLS 1.3 روی ویندوز ۱۰
* ابتدا یک فایل `notepad` باز کنید و دستورات رجیستری زیر را در آن کپی کنید.

<div dir=ltr markdown=1>
```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols]

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0]

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0\Client]
"DisableBy Default"=dword:00000000
"Enabled"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0\Server]
"DisabledByDefault"=dword:00000000
"Enabled"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2]

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client]
"DisableBy Default"=dword:00000000
"Enabled"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server]
"DisableBy Default"=dword:00000000
"Enabled"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.3]

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.3\Client]
"DisabledByDefault"=dword:00000000
"Enabled"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.3\Server]
"DisableBy Default"=dword:00000000
"Enabled"=dword:00000001

```
</div>

* حالا فایل را با پسوند `.reg` ذخیره نمایید تا حالت اجرایی پیدا کند.
> دقت شود که فایل پسوند `.txt` نداشته باشد.

* حالا با دوبار کلیک روی فایل، ان را اجرا نمایید.
* کار تمام است. `TLS 1.3` روی ویندوز ۱۰ فعال شد. تنها نیاز است یک بار سیستم را ریستارت کنید.

* برای چک کردن صحت انجام کار می‌توانید وارد رجیستری‌های ویندوز شوید. برای این کار در `Run` عبارت `regedit` را تایپ کنید و اینتر بزنید.
* حالا در مسیر مشخص شده در تصویر زیر بروید. نسخه‌های TLS فعال شده به این شکل قابل مشاهده هستند.

<div align=center markdown=1>
![ تصویر رجیستری ویندوز](https://github.com/hiddify/hiddify-config/assets/125398461/53b259f3-267a-4e7f-90b2-8f5ce3a216ca)
</div>