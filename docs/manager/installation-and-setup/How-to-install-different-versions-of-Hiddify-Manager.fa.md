---
title: Quick installation on Vultr Servers
---

<div dir="rtl" markdown="1">


# نصب نسخه‌های مختلف هیدیفای‌منیجر
همانطور که می‌دانید، هیدیفای‌منیجر در سه نسخه ارائه می‌گردد که به شرح زیر است:
* **نسخه در حال توسعه یا دولوپ:** 

این نسخه نسخه‌ای از نرم‌افزار است که در حال توسعه برای ایجاد آخرین قابلیت‌هاست. ممکن است این نسخه دارای باگ باشد بنابراین بهتر است روی سرورهای تستی نصب گردد.
* **نسخه بتا:** 

این نسخه یک ورژن بعد از نسخه در حال توسعه است و در حقیقت نسخه قبل از انتشار نهایی است که در آن بخشی از باگ‌ها رفع شده است و دارای قابلیت‌های جدید می‌باشد.
* **نسخه پایدار یا ریلیز:** 

این نسخه در حقیقت ورژن نهایی از نرم‌افزار است که پس از تست‌های نهایی منتشر شده است و پایدارترین نسخه ممکن است.
برای درک بهتر این شکل را ملاحظه فرمایید.

<div align=center>

![install versions](https://github.com/hiddify/Hiddify-Manager/assets/125398461/b5c8a60a-88ce-48e5-a0bb-aaec33f2f5d8)

</div>

## نصب نسخه پایدار (ریلیز)
* قبل از نصب اگر از قبل نسخه دیگری از پنل را نصب کرده‌اید، یک بکاپ از پنل بگیرید. [بیشتر بخوانید ...](https://github.com/hiddify/Hiddify-Manager/wiki/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D9%BE%D8%B4%D8%AA%DB%8C%D8%A8%D8%A7%D9%86%E2%80%8C%DA%AF%DB%8C%D8%B1%DB%8C-%D9%88-%D8%A8%D8%A7%D8%B2%DB%8C%D8%A7%D8%A8%DB%8C-%D9%BE%D9%86%D9%84-%D8%AF%D8%B1-%D9%87%DB%8C%D8%AF%DB%8C%D9%81%D8%A7%DB%8C#%D9%BE%D8%B4%D8%AA%DB%8C%D8%A8%D8%A7%D9%86%DA%AF%DB%8C%D8%B1%DB%8C-%D8%A7%D8%B2-%D9%BE%D9%86%D9%84-%D9%81%D8%B9%D9%84%DB%8C-%D8%A7%D8%B2-%D8%B7%D8%B1%DB%8C%D9%82-%D9%88%D8%A8)
* حالا کافیه دستور تک خطی زیر را در ترمینال اجرا نمایید.


<div dir=ltr>

```
bash <(curl i.hiddify.com/release)
```

</div>

* پس از نصب، کافیه بکاپ خود را برگردانید. [بیشتر بخوانید ...](https://github.com/hiddify/Hiddify-Manager/wiki/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D9%BE%D8%B4%D8%AA%DB%8C%D8%A8%D8%A7%D9%86%E2%80%8C%DA%AF%DB%8C%D8%B1%DB%8C-%D9%88-%D8%A8%D8%A7%D8%B2%DB%8C%D8%A7%D8%A8%DB%8C-%D9%BE%D9%86%D9%84-%D8%AF%D8%B1-%D9%87%DB%8C%D8%AF%DB%8C%D9%81%D8%A7%DB%8C#%D8%A8%D8%A7%D8%B2%DB%8C%D8%A7%D8%A8%DB%8C-%D9%81%D8%A7%DB%8C%D9%84-%D9%BE%D8%B4%D8%AA%DB%8C%D8%A8%D8%A7%D9%86)




## نصب نسخه بتا
* قبل از نصب اگر از قبل نسخه دیگری از پنل را نصب کرده‌اید، یک بکاپ از پنل بگیرید. [بیشتر بخوانید ...](https://github.com/hiddify/Hiddify-Manager/wiki/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D9%BE%D8%B4%D8%AA%DB%8C%D8%A8%D8%A7%D9%86%E2%80%8C%DA%AF%DB%8C%D8%B1%DB%8C-%D9%88-%D8%A8%D8%A7%D8%B2%DB%8C%D8%A7%D8%A8%DB%8C-%D9%BE%D9%86%D9%84-%D8%AF%D8%B1-%D9%87%DB%8C%D8%AF%DB%8C%D9%81%D8%A7%DB%8C#%D9%BE%D8%B4%D8%AA%DB%8C%D8%A8%D8%A7%D9%86%DA%AF%DB%8C%D8%B1%DB%8C-%D8%A7%D8%B2-%D9%BE%D9%86%D9%84-%D9%81%D8%B9%D9%84%DB%8C-%D8%A7%D8%B2-%D8%B7%D8%B1%DB%8C%D9%82-%D9%88%D8%A8)
* حالا کافیه دستور تک خطی زیر را در ترمینال اجرا نمایید.

<div dir=ltr>

```
bash <(curl i.hiddify.com/beta)
```

</div>

* پس از نصب، کافیه بکاپ خود را برگردانید. [بیشتر بخوانید ...](https://github.com/hiddify/Hiddify-Manager/wiki/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D9%BE%D8%B4%D8%AA%DB%8C%D8%A8%D8%A7%D9%86%E2%80%8C%DA%AF%DB%8C%D8%B1%DB%8C-%D9%88-%D8%A8%D8%A7%D8%B2%DB%8C%D8%A7%D8%A8%DB%8C-%D9%BE%D9%86%D9%84-%D8%AF%D8%B1-%D9%87%DB%8C%D8%AF%DB%8C%D9%81%D8%A7%DB%8C#%D8%A8%D8%A7%D8%B2%DB%8C%D8%A7%D8%A8%DB%8C-%D9%81%D8%A7%DB%8C%D9%84-%D9%BE%D8%B4%D8%AA%DB%8C%D8%A8%D8%A7%D9%86)



## نصب نسخه در حال توسعه (دولوپ)
* قبل از نصب اگر از قبل نسخه دیگری از پنل را نصب کرده‌اید، یک بکاپ از پنل بگیرید. [بیشتر بخوانید ...](https://github.com/hiddify/Hiddify-Manager/wiki/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D9%BE%D8%B4%D8%AA%DB%8C%D8%A8%D8%A7%D9%86%E2%80%8C%DA%AF%DB%8C%D8%B1%DB%8C-%D9%88-%D8%A8%D8%A7%D8%B2%DB%8C%D8%A7%D8%A8%DB%8C-%D9%BE%D9%86%D9%84-%D8%AF%D8%B1-%D9%87%DB%8C%D8%AF%DB%8C%D9%81%D8%A7%DB%8C#%D9%BE%D8%B4%D8%AA%DB%8C%D8%A8%D8%A7%D9%86%DA%AF%DB%8C%D8%B1%DB%8C-%D8%A7%D8%B2-%D9%BE%D9%86%D9%84-%D9%81%D8%B9%D9%84%DB%8C-%D8%A7%D8%B2-%D8%B7%D8%B1%DB%8C%D9%82-%D9%88%D8%A8)
* حالا کافیه دستور تک خطی زیر را در ترمینال اجرا نمایید.

<div dir=ltr>

```
bash <(curl i.hiddify.com/dev)
```

</div>


* پس از نصب، کافیه بکاپ خود را برگردانید. [بیشتر بخوانید ...](https://github.com/hiddify/Hiddify-Manager/wiki/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D9%BE%D8%B4%D8%AA%DB%8C%D8%A8%D8%A7%D9%86%E2%80%8C%DA%AF%DB%8C%D8%B1%DB%8C-%D9%88-%D8%A8%D8%A7%D8%B2%DB%8C%D8%A7%D8%A8%DB%8C-%D9%BE%D9%86%D9%84-%D8%AF%D8%B1-%D9%87%DB%8C%D8%AF%DB%8C%D9%81%D8%A7%DB%8C#%D8%A8%D8%A7%D8%B2%DB%8C%D8%A7%D8%A8%DB%8C-%D9%81%D8%A7%DB%8C%D9%84-%D9%BE%D8%B4%D8%AA%DB%8C%D8%A8%D8%A7%D9%86)

## نصب نسخه دلخواه
این قابلیت وجود دارد که یک نسخه دلخواه را نصب کنید. کافیست طبق دستور زیر عمل کنید.


<div dir=ltr>

```
bash <(curl i.hiddify.com/vVERSION)
```
</div>

که در اینجا به جای VERSION باید نسخه مورد نظر خود را وارد کنید. فرض کنید نسخه `8` را می‌خواهید نصب کنید. کافیست دستور زیر را اجرا نمایید تا آخرین نسخه `8` برای شما نصب شود.

<div dir=ltr>

```
bash <(curl i.hiddify.com/v8)
```
</div>

از نسخه 10 می‌توانید دقیقا یک آپدیت خاص را نصب نمایید. به عنوان مثال برای نصب نسخه `10.7.0` کافیست از دستور زیر استفاده نمایید.

<div dir=ltr>

```
bash <(curl i.hiddify.com/v10.7.0)
```
</div>
