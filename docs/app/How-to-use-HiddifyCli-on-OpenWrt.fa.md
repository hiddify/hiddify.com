---
title: آموزش کامل نصب و راه‌اندازی HiddifyCli در سیستم‌عامل OpenWrt 
---


### آموزش کامل نصب و راه‌اندازی HiddifyCli در سیستم‌عامل OpenWrt

برای نصب **HiddifyCli** در سیستم‌عامل OpenWrt، تمام مراحل زیر را به ترتیب انجام دهید. این آموزش شامل دانلود، استخراج، نصب و پیکربندی کامل است.

---
#### 1. **دانلود فایل HiddifyCli**
برای دانلود نسخه مناسب معماری روتر، ابتدا از دستور زیر برای دانلود مستقیم فایل استفاده کنید:
<div dir="ltr">
   ```bash
   wget -O /tmp/HiddifyCli.tar.gz https://github.com/hiddify/hiddify-core/releases/download/latest/HiddifyCli-{معماری}.tar.gz
   ```
</div>
   **توضیح:**
   
   - `{معماری}` را با معماری روتر خود جایگزین کنید (مثلاً `mips`, `arm`, یا `x86_64`).

---

#### 2. **استخراج فایل**
پس از دانلود، فایل را با دستور زیر استخراج کنید:

<div dir="ltr">
```bash
tar -xvzf /tmp/HiddifyCli.tar.gz -C /tmp
```
</div>
**توضیحات دستور:**
- `x-` برای استخراج فایل.
- `v-` برای نمایش جزئیات فرآیند.
- `z-` برای باز کردن فایل‌های فشرده gzip.
- `f-` برای مشخص کردن نام فایل.
- `tmp/` مسیری است که فایل در آن استخراج می‌شود (می‌توانید مسیر دلخواه خود را جایگزین کنید).
  
---

#### 3. **انتقال فایل اجرایی به مسیر مناسب**
فایل اجرایی `HiddifyCli` را به مسیر `/usr/bin/` منتقل کنید:

<div dir="ltr">
```bash
mv /tmp/HiddifyCli /usr/bin/
```
</div>

---

#### 4. **تنظیم مجوز اجرا**
برای فعال کردن قابلیت اجرا برای فایل، دستور زیر را وارد کنید:

<div dir="ltr">
```bash
chmod +x /usr/bin/HiddifyCli
```
</div>

---

#### 5. **ساخت فایل راه‌اندازی (Init Script)**
برای ایجاد سرویس خودکار:
1. یک فایل در مسیر `/etc/init.d/` با نام `HiddifyCli` ایجاد کنید:
   
<div dir="ltr">
   ```bash
   touch /etc/init.d/HiddifyCli
   ```
</div>

3. فایل را با محتوای زیر پر کنید:


<div dir="ltr">
   ```bash
   #!/bin/sh /etc/rc.common
   START=91
   USE_PROCD=1

   start_service() {
       procd_open_instance
       procd_set_param command /usr/bin/HiddifyCli run -c /root/config.conf
       procd_set_param stdout 1
       procd_set_param stderr 1
       procd_set_param respawn
       procd_close_instance
   }
   ```
</div>
4. مجوز فایل را تنظیم کنید:


<div dir="ltr">
   ```bash
   chmod 755 /etc/init.d/HiddifyCli
   ```
 </div>

---

#### 6. **فعال‌سازی و اجرای سرویس**
دستورات زیر را برای فعال‌سازی و راه‌اندازی سرویس اجرا کنید:

<div dir="ltr">
```bash
service HiddifyCli enable
service HiddifyCli start
```
</div>

---

#### 7. **تنظیم کانفیگ**
1. **استخراج کانفیگ از اپ دسکتاپ هیدیفای:**
 
   - تنظیمات دلخواه را در اپلیکیشن انجام دهید.
   - کانفیگ را استخراج کرده و در یک فایل متنی ذخیره کنید.
   - پسوند فایل را به `conf.` تغییر دهید (مثلاً `config.conf`).
   - 
2. **فایل کانفیگ را به مسیر `/root/` در روتر انتقال دهید:**
   
<div dir="ltr">
   ```bash
   mv config.conf /root/
   ```
</div>

---

#### 8. **راه‌اندازی مجدد روتر**
روتر را ری‌استارت کنید تا تغییرات اعمال شوند:

<div dir="ltr">
```bash
reboot
```
</div>

پس از راه‌اندازی مجدد، سرویس HiddifyCli فعال شده و **Socks5 Proxy** در آدرس زیر در دسترس خواهد بود:

<div dir="ltr">
```plaintext
127.0.0.1:12334
```
</div>

---

### نکات تکمیلی:
- برای بررسی معماری روتر، دستور زیر را اجرا کنید:
  
<div dir="ltr">
  ```bash
  uname -m
  ```
</div>

- اگر در هر مرحله مشکلی پیش آمد، می‌توانید با دستور زیر لاگ‌های سرویس را بررسی کنید:
  
<div dir="ltr">
  ```bash
  logread | grep HiddifyCli
  ```
</div>

در [مقاله دیگری](/fa/app/How-to-Enable-Free-Internet-Access-for-Clients-Behind-an-OpenWrt-Router-Using-HiddifyCli/) نحوه استفاده از این اینترنت آزاد برای کلاینت‌های پشت روتر را آموزش خواهیم داد.
