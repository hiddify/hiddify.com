---
title: آموزش استفاده از HiddifyCli یا هیدیفای‌کامندلاین
---

<div markdown="1">

# آموزش استفاده از HiddifyCli یا هیدیفای‌کامندلاین
این اپ برای مواردی که دسکتاپ وجود ندارد مثل سرورها توسعه داده شده است و از همه پردازنده‌ها پشتیبانی می‌کند.

## اجرای کانفیگ یا لینک سابسکریپشن در HiddifyCli

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

## اجرای کانفیگ یا لینک سابسکریپشن در HiddifyCli با تنظیمات HiddifyApp
برای این کار ابتدا می‌بایست تنظیمات مربوط به هیدیفای‌اپ خود را استخراج نمایید.
<details><summary><h3>استخراج تنظیمات HiddifyApp</h3></summary>

  - برای این کار هیدیفای‌اپ را باز نمایید و وارد `Config Options` یا `تنظیمات پیکربندی` شوید و منوی سه نقطه را بزنید.

<div align=center>

![config-options](https://github.com/hiddify/hiddify.com/assets/125398461/f1822c80-1e2a-4752-aabe-8306b1124874)

</div>

- حالا گزینه `صادر کردن تنظیمات به کلیپ‌بورد` را بزنید تا تنظیمات وارد کلیپ‌بورد شوند.
<div align=center>
  
![export configs](https://github.com/hiddify/hiddify.com/assets/125398461/b4ff8a34-4a8a-4d93-9c53-d2d928c095e6)
</div>


- حالا می‌توانید این تنظیمات را در یک فایل با پسوند `json` ذخیره نمایید.
  
- همچنین می‌توانید این تنظیمات در گیتهاب قرار دهید و از لینک آن به عنوان `URL` استفاده نمایید.



</details>

### اجرای کانفیگ یا لینک سابسکریپشن در HiddifyCli با تنظیمات استخراج شده از HiddifyApp
- همچنین اگر بخواهید از تنظیمات هیدیفای‌اپ خود استفاده کنید می‌بایست از کامند زیر استفاده نمایید.
<div dir="ltr" markdown="1">
  
```
Hiddifycli run -c <config file or sublink> -h <HiddifyApp config file>
```
</div>

که دراینجا فایل کانفیگ یا ساب‌لینک خود  را به جای `<config file or sublink>` قرار دهید و فایل تنظیمات مربوط به هیدیفای‌اپ را که  در مرحله قبل استخراج کرده بودید را به جای `<HiddifyApp config file>` وارد نمایید. 

- می‌توانید به جای فایل کانفیگ، لینک مربوط به تنظیمات در هیدیفای‌اپ را که فرضا در گیتهاب قرار داده‌اید، استفاده نمایید.
<div dir="ltr" markdown="1">
  
```
Hiddifycli run -c <config file or sublink> -h <HiddifyApp config URL>
```
</div>

که دراینجا فایل کانفیگ یا ساب‌لینک خود  را به جای `<config file or sublink>` قرار دهید و لینک مربوط به تنظیمات مورد نظر در هیدیفای‌اپ را به جای `<HiddifyApp config URL>` قرار دهید.
