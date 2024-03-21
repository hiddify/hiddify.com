---
title: آموزش استفاده از HiddifyCli یا هیدیفای‌کامندلاین
---

# آموزش استفاده از HiddifyCli یا هیدیفای‌کامندلاین
این اپ برای مواردی که دسکتاپ وجود ندارد مثل سرورها توسعه داده شده است و از همه پردازنده‌ها پشتیبانی می‌کند.

برای استفاده از آن باید از کامند زیر استفاده شود.
<div dir="ltr" markdown="1">
  
```
Hiddifycli run -c <config file or sublink> -h <HiddifyApp config file or URL>
```
</div>

- برای اتصال به یک کانفیگ خاص کافیه کامند بالا را به شکل زیر اجرا کنید.
<div dir="ltr" markdown="1">

```
Hiddifycli run -c <config file>
```
</div>

در اینجا کانفیگ مورد نظر خود را به جای `<config file>` قرار دهید.

- همچنین می‌توانید یک سابسکریپشن را در اپ اجرا نمایید.
<div dir="ltr" markdown="1">
  
```
Hiddifycli run -c <sublink>
```
</div>

که در اینجا لینک سابسکریپشن خود را به جای `<sublink>` قرار دهید.

- همچنین اگر بخواهید از کانفیگ‌های هیدیفای‌منیجر خود استفاده کنید می‌بایست از کامند زیر استفاده نمایید.
<div dir="ltr" markdown="1">
  
```
Hiddifycli run -c <config file or sublink> -h <HiddifyApp config file>
```
</div>

که دراینجا فایل کانفیگ یا ساب‌لینک خود  را به جای `<config file or sublink>` قرار دهید و فایل تنظیمات مربوط به هیدیفای‌اپ را به جای `<HiddifyApp config file>` وارد نمایید. مقلا فرضا فایل تنظیمات فرگمنت را در اینجا وارد نمایید.

- می‌توانید به جای کانفیگ، لینک مربوط به تنظیمات در هیدیفای‌اپ را استفاده نمایید.
<div dir="ltr" markdown="1">
  
```
Hiddifycli run -c <config file or sublink> -h <HiddifyApp config URL>
```
</div>

که دراینجا فایل کانفیگ یا ساب‌لینک خود  را به جای `<config file or sublink>` قرار دهید و لینک مربوط به تنظیمات مورد نظر در هیدیفای‌اپ را به جای `<HiddifyApp config URL>` قرار دهید.
