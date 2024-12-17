---
title: آموزش استفاده از اینترنت آزاد در کلاینت‌های پشت روتر OpenWrt با HiddifyCli
---

<markdown ="1">


### آموزش استفاده از اینترنت آزاد در کلاینت‌های پشت روتر OpenWrt با HiddifyCli

در [مقاله دیگری](/fa/app/How-to-use-HiddifyCli-on-OpenWrt/) نحوه دانلود و نصب HiddifyCli روی روتر OpenWrt توضیح داده شد، در این مقاله به آموزش استفاده از اینترنت آزاد آن روتر برای کلاینت‌های پشت آن می‌پردازیم.

برای استفاده از اینترنت آزاد در کلاینت‌های پشت روتر به دو روش می‌توان اقدام نمود:

#### روش ۱. استفاده از پروکسی برای کلاینت‌های پشت روتر در OpenWrt

اگر می‌خواهید کلاینت‌های متصل به روتر (مانند لپ‌تاپ، گوشی و سایر دستگاه‌ها) از پروکسی **127.0.0.1:12334** استفاده کنند، می‌توانید تنظیمات زیر را اعمال کنید تا این پروکسی به عنوان سرویس مرکزی برای کل شبکه قابل دسترسی باشد.

---

##### ۱. **فعال کردن Port Forwarding در روتر**
پروکسی **127.0.0.1:12334** که روی روتر تنظیم شده، به صورت پیش‌فرض فقط در خود روتر قابل استفاده است. برای دسترسی کلاینت‌ها، این پورت باید روی آدرس LAN روتر نیز باز شود.

۱. **اضافه کردن قانون NAT:**
برای این کار، باید ترافیک ورودی روی این پورت را به پروکسی هدایت کنید:
<div dir="ltr">
```bash
iptables -t nat -A PREROUTING -i br-lan -p tcp --dport 12334 -j DNAT --to-destination 127.0.0.1:12334
iptables -A FORWARD -i br-lan -p tcp --dport 12334 -j ACCEPT
```
</div>
**توضیح:**
- `br-lan`: اینترفیس LAN روتر است.
- `12334`: پورت پروکسی HiddifyCli.

۲. **ذخیره قوانین Iptables:**
برای ذخیره قوانین و اعمال آنها پس از هر راه‌اندازی مجدد، دستور زیر را اجرا کنید:
```bash
service firewall restart
```

---

##### ۲. **اعلام تنظیمات به کلاینت‌ها**
دستگاه‌های متصل به روتر باید تنظیمات مربوط به **پروکسی دستی** را انجام دهند. در کلاینت‌ها، مراحل زیر را دنبال کنید:

###### **برای ویندوز:**
۱. وارد بخش **Settings** شوید.
۲. به **Network & Internet** > **Proxy** بروید.
۳. در قسمت **Manual proxy setup**:
- **Address** را روی آی‌پی LAN روتر (معمولاً `192.168.1.1`) تنظیم کنید.
- **Port** را `12334` قرار دهید.
۴. تنظیمات را ذخیره کنید.

###### **برای اندروید:**
۱. به تنظیمات شبکه Wi-Fi متصل شوید.
۲. روی شبکه Wi-Fi فعلی کلیک کرده و **Modify Network** یا **Advanced Settings** را باز کنید.
۳. **Proxy** را روی **Manual** تنظیم کنید:
<div dir="ltr">
- **Proxy hostname**: آی‌پی LAN روتر (مثلاً `192.168.1.1`).
- **Proxy port**: `12334`.
</div>
۴. تنظیمات را ذخیره کنید.

###### **برای iOS:**
۱. به تنظیمات Wi-Fi بروید.
۲. روی شبکه متصل شده کلیک کنید و **Configure Proxy** را روی **Manual** قرار دهید.
۳. آی‌پی روتر را در **Server** و پورت را `12334` وارد کنید.
۴. تنظیمات را ذخیره کنید.

###### **برای مک‌اواس (macOS):**
۱. به **System Preferences** > **Network** بروید.
۲. روی اتصال فعلی خود کلیک کرده و **Advanced** را انتخاب کنید.
۳. در تب **Proxies**، گزینه **SOCKS Proxy** را فعال کنید و:
<div dir="ltr">
- **SOCKS Proxy Server**: آی‌پی روتر (مثلاً `192.168.1.1`).
- **Port**: `12334`.
</div>
۴. تنظیمات را ذخیره کنید.

---

##### ۳. **تست اتصال کلاینت‌ها**
برای اطمینان از عملکرد پروکسی:
- مرورگر کلاینت را باز کرده و سعی کنید به سایتی که بدون پروکسی فیلتر است متصل شوید.
- اگر اتصال برقرار شد، تنظیمات به درستی اعمال شده است.

---

##### ۴. **نکات تکمیلی**
- اگر کلاینت‌ها نیاز به استفاده خودکار از پروکسی دارند، می‌توانید از یک فایل **PAC (Proxy Auto-Configuration)** استفاده کنید و آن را در تنظیمات کلاینت‌ها معرفی کنید.
- آدرس PAC:
  <div dir="ltr">
```
http://192.168.1.1/proxy.pac
```
</div>
فایل PAC می‌تواند مسیرها و استثنائات دلخواهی را برای استفاده از پروکسی تعریف کند.

### روش ۲. راه‌اندازی روتینگ در OpenWrt برای عبور تمام ترافیک از **Socks5 Proxy**

برای هدایت تمام ترافیک اینترنت از طریق **Socks5 Proxy**، باید از ابزارهایی مانند `redsocks` یا `iptables` استفاده کنید. مراحل زیر را دنبال کنید:

---

#### ۱. **نصب ابزارهای مورد نیاز**
ابتدا ابزارهای لازم را نصب کنید. در OpenWrt، `redsocks` برای روتینگ ترافیک از طریق **Socks5 Proxy** استفاده می‌شود.

۱. به‌روزرسانی لیست بسته‌ها:
<div dir="ltr">
```bash
opkg update
```
</div>
۲. نصب `redsocks` و سایر ابزارها:
<div dir="ltr">
```bash
opkg install redsocks iptables-mod-nat-extra iptables-mod-tproxy
```
</div>

---

#### ۲. **پیکربندی Redsocks**
فایل پیکربندی `redsocks` را در مسیر `/etc/redsocks.conf` ایجاد کنید:
<div dir="ltr">

```bash
nano /etc/redsocks.conf
```
</div>
و محتوای زیر را در آن قرار دهید:
<div dir="ltr">

```plaintext
base {
log_debug = off;
log_info = on;
log = "syslog:daemon";
daemon = on;
user = "nobody";
group = "nogroup";
redirector = iptables;
}

redsocks {
local_ip = 127.0.0.1;
local_port = 12345; # پورت محلی برای ترافیک پروکسی
ip = 127.0.0.1;     # آدرس سرور Socks5
port = 12334;        # پورت سرور Socks5
type = socks5;
}
```
</div>
**توضیح:**

<div dir="ltr">

- `local_ip` و `local_port`: آدرس و پورتی که Redsocks به آن گوش می‌دهد.
- `ip` و `port`: آدرس و پورت **Socks5 Proxy**.
</div>
---

#### ۳. **تنظیمات iptables برای روتینگ**
برای هدایت ترافیک به Redsocks، قوانین `iptables` را اضافه کنید:

۱. یک اسکریپت با نام `redsocks-routing` در `/etc/init.d/` ایجاد کنید:
<div dir="ltr">
  
```bash
touch /etc/init.d/redsocks-routing
chmod +x /etc/init.d/redsocks-routing
```
</div>
۲. اسکریپت را با محتوای زیر پر کنید:
<div dir="ltr">

```bash
#!/bin/sh /etc/rc.common
START=99
STOP=10

start() {
iptables -t nat -N REDSOCKS
iptables -t nat -A REDSOCKS -d 0.0.0.0/8 -j RETURN
iptables -t nat -A REDSOCKS -d 127.0.0.0/8 -j RETURN
iptables -t nat -A REDSOCKS -d 192.168.0.0/16 -j RETURN
iptables -t nat -A REDSOCKS -d 10.0.0.0/8 -j RETURN
iptables -t nat -A REDSOCKS -d 172.16.0.0/12 -j RETURN
iptables -t nat -A REDSOCKS -p tcp -j REDIRECT --to-ports 12345

iptables -t nat -A OUTPUT -p tcp -j REDSOCKS
iptables -t nat -A PREROUTING -p tcp -j REDSOCKS
}

stop() {
iptables -t nat -F REDSOCKS
iptables -t nat -X REDSOCKS
}
```
</div>
۳. اسکریپت را فعال و اجرا کنید:
<div dir="ltr">

```bash
service redsocks-routing enable
service redsocks-routing start
```
</div>
---

#### ۴. **فعال‌سازی Redsocks**
برای فعال‌سازی و اجرای خودکار Redsocks:
<div dir="ltr">

```bash
service redsocks enable
service redsocks start
```
</div>
---

#### ۵. **بازنشانی روتر**
برای اعمال تغییرات، روتر را ری‌استارت کنید:
<div dir="ltr">

```bash
reboot
```
</div>
---

#### ۶. **بررسی عملکرد**
برای بررسی وضعیت و لاگ‌ها:
- وضعیت `redsocks`:
  <div dir="ltr">
```bash
ps | grep redsocks
```
</div>
- لاگ‌های سیستم:
<div dir="ltr">

```bash
logread | grep redsocks
```
</div>
---

#### نتیجه:
پس از اجرای این تنظیمات:
- تمام ترافیک TCP از طریق **Socks5 Proxy** عبور می‌کند.
- ترافیک شبکه‌های داخلی (`192.168.0.0/16`, `10.0.0.0/8`) و آدرس‌های محلی از پروکسی عبور نمی‌کنند.

**نکته:** اگر به ترافیک UDP نیز نیاز دارید، باید از ابزارهای دیگری مانند `dns2socks` یا تنظیمات اضافی `redsocks` استفاده کنید.
