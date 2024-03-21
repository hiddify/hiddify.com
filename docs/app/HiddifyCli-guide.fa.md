---
title: آموزش استفاده از HiddifyCli یا هیدیفای‌کامندلاین
---

# آموزش استفاده از HiddifyCli یا هیدیفای‌کامندلاین
این اپ برای مواردی که دسکتاپ وجود ندارد مثل سرورها توسعه داده شده است و از همه پردازنده‌ها پشتیبانی می‌کند.

برای استفاده از آن باید از کامند زیر استفاده شود.
<div dir="ltr" markdown="1">
  
```
Hiddifycli run -c <config file or sublink> -h <HiddifyManager config file or sublink>
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
Hiddifycli run -h <HiddifyManager config file>
```
</div>
که دراینجا فایل کانفیگ خود در هیدیفای‌منیجر را به جای `<HiddifyManager config file>` وارد نمایید.

- می‌توانید به جای کانفیگ، سابسکریپشن خود در هیدیفای‌منیجر را استفاده نمایید.
<div dir="ltr" markdown="1">
  
```
Hiddifycli run -h <HiddifyManager sublink>
```
</div>
که ساب لینک خود در هیدیفای‌منیجر را به جای `<HiddifyManager sublink>` قرار دهید.
