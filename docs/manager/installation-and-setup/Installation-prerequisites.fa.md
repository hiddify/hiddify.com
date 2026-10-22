---
title: پیش‌نیازهای نصب
weight: -82
---



<div dir="rtl" markdown=1>
    
# پیش‌نیازهای نصب

در این صفحه می‌بینید قبل از [نصب هیدیفای‌منیجر](/fa/manager/installation-and-setup/guide/) به چه چیزهایی نیاز دارید: یک سرور، سیستم‌عامل مناسب و راهی برای اتصال به سرور.

## ۱. سرور مجازی (VPS)

**VPS** یا سرور مجازی، کامپیوتری در یک دیتاسنتر است که اجاره می‌کنید و از طریق اینترنت کنترلش می‌کنید. چند راه برای تهیه‌ی آن دارید:

- **با کارت اعتباری خارجی یا [سایت‌های پرداخت واسط](https://www.google.com/search?q=%D9%BE%D8%B1%D8%AF%D8%A7%D8%AE%D8%AA+%D9%81%D8%A7%DA%A9%D8%AA%D9%88%D8%B1+%D8%AE%D8%A7%D8%B1%D8%AC%DB%8C)**، مستقیم از دیتاسنترهای معروف دنیا. در این حالت معمولاً هزینه‌ی کمتری می‌پردازید. می‌توانید [سرورهای ارزان](https://www.google.com/search?q=buy+cheap+and+good+quality+vps+server) را جست‌وجو کنید یا [فهرست ارائه‌دهنده‌های ما](https://github.com/hiddify/awesome-freedom/blob/main/vps-providers.md) را ببینید.
- **با رمزارز.** سایت‌های زیادی رمزارز قبول می‌کنند؛ آن‌ها را [در گوگل جست‌وجو کنید](https://www.google.com/search?q=purchase+vps+via+crypto) یا [فهرست ما](https://github.com/hiddify/awesome-freedom/blob/main/vps-providers.md) را ببینید که دیتاسنترهای پذیرنده‌ی رمزارز در آن مشخص شده‌اند.
- **از [سایت‌های ایرانی](https://www.google.com/search?q=%D8%AE%D8%B1%DB%8C%D8%AF+%D8%B3%D8%B1%D9%88%D8%B1+%D9%85%D8%AC%D8%A7%D8%B2%DB%8C)**. ویدئوی زیر روش خرید سرور از ایران را نشان می‌دهد.

</div>
    
<div align=center markdown=1>
    
<a href="https://youtu.be/tcd1wBUR3cY"><img width="50%" src="https://user-images.githubusercontent.com/125398461/229348575-c564efe9-02dc-4b97-bf66-410060934a94.png" alt="ویدئوی آموزش خرید سرور از ایران" /></a>

</div>

<div dir="rtl" markdown=1>

## ۲. منابع سرور

حداقل پیشنهادی:

- ۱ گیگابایت رم
- ۱ هسته‌ی CPU
- ۱۰ گیگابایت فضای دیسک

اگر رم سرور کم باشد، نصب‌کننده در طول نصب یک فضای swap موقت (بخشی از دیسک که مثل رم اضافه استفاده می‌شود) می‌سازد.

## ۳. سیستم‌عامل

سیستم‌عامل سرور باید **Ubuntu 22.04، 24.04 یا 26.04** باشد (پردازنده‌ی amd64/x86_64 یا arm64). اوبونتو یکی از نسخه‌های معروف لینوکس است و لوگوی آن این شکلی است: ![لوگوی اوبونتو](https://img.shields.io/badge/Ubuntu--E95420?style=flat-square&logo=ubuntu)

Ubuntu 20.04 و نسخه‌های قدیمی‌تر و توزیع‌های دیگر لینوکس پشتیبانی نمی‌شوند. یک سرور تازه انتخاب کنید که چیز دیگری روی آن نصب نشده باشد.

## ۴. پورت‌ها

هیدیفای به پورت‌های **80** و **443** نیاز دارد و هیچ برنامه‌ی دیگری روی سرور نباید از آن‌ها استفاده کند. اگر ارائه‌دهنده‌ی سرور فایروال جداگانه دارد، دست‌کم پورت‌های 22 (SSH)، 80 و 443 را باز کنید.

## ۵. دسترسی SSH

برای اجرای دستور نصب باید از طریق SSH به سرور وصل شوید. آموزش آن در [اتصال به سرور از طریق SSH](/fa/manager/installation-and-setup/How-to-connect-to-server-via-SSH/) است.

برای امن‌تر کردن دسترسی SSH این دو مطلب را بخوانید:

- [غیرفعال کردن ورود با رمز عبور در SSH](/fa/manager/basic-concepts-and-troubleshooting/Disable-SSH-Password-Authentication/)
- [تغییر پورت SSH روی سرور](/fa/manager/basic-concepts-and-troubleshooting/How-to-change-SSH-port-on-your-server/)

وقتی آماده شدید، به [راهنمای نصب اصلی](/fa/manager/installation-and-setup/guide/) بروید.

</div>
