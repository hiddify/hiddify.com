---
title: ریست کردن تنظیمات هیدیفای‌منیجر به حالت اولیه
weight: -80
---

<div dir=rtl markdown=1>

# ریست کردن تنظیمات هیدیفای‌منیجر به حالت اولیه

این آموزش هیدیفای‌منیجر را به حالت نصب تازه برمی‌گرداند: پنل، دیتابیس، کاربران، دامنه‌ها و تنظیمات همه پاک می‌شوند و دوباره از راه‌اندازی سریع شروع می‌کنید. این آموزش برای هیدیفای‌منیجر نسخهٔ ۱۴.۵ نوشته شده است.

!!! tip "واقعاً به ریست کامل نیاز دارید؟"
    - **رمز ادمین را فراموش کرده‌اید:** ریست لازم نیست. روی سرور دستور `hiddify reset-password` را اجرا کنید ([پایین‌تر](#reset-only-the-admin-password) را ببینید).
    - **چیزی درست کار نمی‌کند:** اول در پنل در صفحهٔ **اقدامات** (**اعمال و وضعیت**) گزینهٔ **راه‌اندازی مجدد** یا **نصب دوباره** را امتحان کنید. هیچ‌کدام کاربران و تنظیمات شما را پاک نمی‌کنند.
    - **می‌خواهید به سرور جدید بروید:** روی سرور قدیمی پشتیبان بگیرید و روی سرور جدید بازیابی کنید ([پشتیبان‌گیری و بازیابی](/fa/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/)).

## قبل از شروع: پشتیبان بگیرید

ریست کامل برگشت‌پذیر نیست. در پنل به **پشتیبان‌گیری** بروید، روی **دانلود پشتیبان** بزنید و فایل را جای امنی نگه دارید. با این فایل بعداً می‌توانید همه‌چیز را برگردانید. بیشتر: [آموزش پشتیبان‌گیری و بازیابی هیدیفای‌منیجر](/fa/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/).

## ریست کامل

۱. [با SSH به سرور وصل شوید](/fa/manager/installation-and-setup/How-to-connect-to-server-via-SSH/).

۲. منوی هیدیفای‌منیجر را با این دستور باز کنید (ممکن است بعد از ورود خودش باز باشد):

<div dir=ltr markdown=1>

```
hiddify
```

</div>

۳. گزینهٔ **advanced** (*Uninstall, Remote Assistant, Downgrade,...*) و بعد **purge** (*Uninstall completely and remove database*) را انتخاب کنید. همهٔ سرویس‌های هیدیفای، پنل و دیتابیس آن متوقف و حذف می‌شوند.

!!! warning "هشدار"
    گزینهٔ **purge** سرور دیتابیس MariaDB و همهٔ محتوای `/opt/hiddify-manager` را هم حذف می‌کند. روی سروری که برنامه‌های دیگری هم داده‌هایشان را در MariaDB نگه می‌دارند از آن استفاده نکنید.

۴. هیدیفای‌منیجر را با دستور نصب دوباره نصب کنید:

<div dir=ltr markdown=1>

```
bash <(curl https://i.hiddify.com/release)
```

</div>

۵. بعد از پایان نصب، یکی از لینک‌های ادمین جدید را که نمایش داده می‌شود باز کنید. پنل مثل بار اول نصب، با **راه‌اندازی سریع** شروع می‌شود. [راهنمای نصب اصلی](/fa/manager/installation-and-setup/guide/) را ببینید.

اگر می‌خواهید به جای شروع از صفر، اطلاعات قبلی را برگردانید، در پنل جدید به **پشتیبان‌گیری** بروید و فایل پشتیبان را روی بخش **بازیابی** بیندازید.

## فقط ریست رمز ادمین { #reset-only-the-admin-password }

اگر فقط رمز ادمین را گم کرده‌اید، این دستور را روی سرور اجرا کنید:

<div dir=ltr markdown=1>

```
hiddify reset-password
```

</div>

رمز ادمین اصلی پاک می‌شود. با یکی از لینک‌های ادمین و رمز **خالی** وارد شوید (دستور `hiddify admin` لینک‌ها را نشان می‌دهد) و بعد در صفحهٔ **ادمین‌ها** یا **حساب من** رمز تازه بگذارید.

## مقاله‌های مرتبط

- [به‌روزرسانی](/fa/manager/configuration-and-advanced-settings/How-to-update-Hiddify-panel/)
- [پشتیبان‌گیری و بازیابی](/fa/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/)
- [پروکسی SSH](/fa/manager/configuration-and-advanced-settings/SSH-proxy-setting-on-Hiddify-panel/)
- [آشنایی کامل با پنل و تنظیمات آن](/fa/manager/configuration-and-advanced-settings/How-to-configure-Hiddify-panel-properly/)

</div>
