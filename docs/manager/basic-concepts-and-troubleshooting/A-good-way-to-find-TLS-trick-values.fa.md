---
title: یک روش مناسب برای پیدا کردن مقادیر ترفند TLS و نحوه تنظیم آن از سمت هیدیفای‌منیجر و اپ هیدیفای
---


### یک روش مناسب برای پیدا کردن مقادیر ترفند TLS و نحوه تنظیم آن از سمت هیدیفای‌منیجر و اپ هیدیفای

---
در ماه‌های اخیر استفاده از TLS Trick یا فرگمنت به کابوسی برای سیستم‌های فیلترینگ و فایروال‌ها در کشورها تبدیل شده است. متاسفانه، طیف وسیعی از این روش‌ها محدود شده‌اند و در حال حاضر تنها روی برخی ISPها (اپراتورها) کارساز هستند. با این حال، می‌توان با استفاده از یک اسکنر، مقادیر سازگار با هر اپراتور را از طریق سرور مجازی (VPS) پیدا کرد.

---

### روش پیدا کردن مقادیر فرگمنت

برای پیدا کردن مقادیر مناسب فرگمنت، مراحل زیر را دنبال کنید:

1. **وارد سرور مجازی یا Tremux** خود شوید و دستور زیر را اجرا کنید:
   ```bash
   bash <(curl -fsSL https://raw.githubusercontent.com/Ptechgithub/FragmentScanner/main/install.sh)
   ```

2. پس از نصب اسکریپت، سه گزینه به شما نمایش داده می‌شود:
   1. `config to fragment`
   2. `fragment scanner`
   3. `exit`

3. ابتدا گزینه **1** را انتخاب کنید که از شما درخواست می‌کند کانفیگ مورد نظر خود برای تست را ارسال کنید.

**نکته مهم:** اسکریپت تنها از پروکسی‌هایی مانند `tls`, `grpc`, `vless/vmess/torjan` پشتیبانی می‌کند.

4. پس از ارسال کانفیگ، اسکریپت فرمت فرگمنت کانفیگ را به شما نمایش داده و آن را داخل فایل `config.json` ذخیره می‌کند که برای اسکن در مرحله بعدی از آن استفاده کند.

5. سپس گزینه **2** را انتخاب کرده و به چهار سوال پاسخ دهید تا اسکن آغاز شود:

   - **سوال اول:** تعداد دفعات امتحان مقادیر تصادفی فرگمنت (پیش‌فرض: ۱۰)
   - **سوال دوم:** زمان تداوم تست هر مقدار بر حسب ثانیه [Time out] (پیشنهاد: ۴)
   - **سوال سوم:** اگر می‌خواهید پورت کانفیگ را تغییر دهید، پورت جدید را وارد کنید و برای استفاده از پورت کانفیگ وارد شده در مرحله ۱، Enter بزنید.
   - **سوال چهارم:** تعداد دفعات تست هر مقدار.

6. پس از پاسخ به این سوالات، اسکن آغاز شده و نتایج به شما نمایش داده می‌شود. مقادیر برتر در بالای لیست قرار دارند. مقادیر ارائه شده شامل نوع پکت، مقدار Interval و Length می‌باشد.

---

### تنظیم مقادیر ترفند TLS در هیدیفای‌منیجر

اگر مقادیر برتر دارای پکت tlshello هستند، می‌توانید آنها را از سمت هیدیفای‌منیجر تنظیم کنید. در غیر این صورت، باید از طریق کلاینت این تنظیمات را انجام دهید.

**نکات پیشنهادی:**

- گزینه TLS Mixed Sni فعال باشد.
- گزینه TLS padding غیرفعال باشد.

برای تنظیم این موارد، به بخش تنظیمات پنل > ترفند TLS مراجعه کنید.

---

### تنظیم مقادیر در اپلیکیشن هیدیفای

کافی است وارد برنامه شوید و در بخش تنظیمات، وارد گزینه All config option شوید. سپس به دنبال گزینه `Tls Fregment` بگردید و آن را فعال کنید و مقادیر را تنظیم نمایید.
