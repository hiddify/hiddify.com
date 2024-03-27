---
title: آموزش ایمپورت کردن پنل X-UI به هیدیفای‌منیجر
---

# آموزش ایمپورت کردن پنل X-UI به هیدیفای‌منیجر

در هیدیفای‌منیجر نسخه ۱۰ این قابلیت اضافه شده است که بتوان پنل X-UI را ایمپورت نمود. برای این کار کافیست مراحل زیر را تا انتها دنبال کنید.
- ابتدا فایل دیتابیس مربوط به آن پنل را به سرور خود منتقل نمایید. ما قبلا در [این مقاله](/fa/manager/basic-concepts-and-troubleshooting/How-to-transfer-files-between-a-server-and-a-computer/) آموزش داده‌ایم که چطور می‌توان به/از سرور انتقال فایل انجام داد.
- سپس از دستور زیر برای ایمپورت نمودن فایل دیتابیس پنل X-UI استفاده نمایید.
<div dir="ltr">

```bash
cd /opt/hiddify-manager/hiddify-panel/&&hiddifypanel xui-importer -x /path/to/db/file.db
```
</div>

  به جای`</path/to/db/file.db>` می‌بایست مسیر مربوط به فایل دیتابیس را قرار دهید. 
  
  فرض کنید فایل دیتابیس در پوشه `root/` باشد در این صورت دستور بالا را به شکل زیر استفاده نمایید.
<div dir="ltr">

```bash
cd /opt/hiddify-manager/hiddify-panel/&&hiddifypanel xui-importer -x </root/file.db>
```
</div>

- کار تمام است. پنل X-UI با موفقیت به هیدیفای‌منیجر منتقل شد.
