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
   wget -O /tmp/HiddifyCli.tar.gz https://github.com/hiddify/hiddify-core/releases/download/{نسخه_مناسب}/HiddifyCli-{معماری}.tar.gz
   ```
</div>
   **توضیح:**
   
   - `{نسخه_مناسب}` را با نسخه مورد نظر جایگزین کنید (مثلاً `v1.0.0`).
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

---

??? success "استفاده از اینترنت آزاد در کلاینت‌های پشت روتر"
            برای استفاده از اینترنت آزاد در کلاینت‌های پشت روتر به دو روش می‌توان اقدام نمود:
            
            ### استفاده از پروکسی برای کلاینت‌های پشت روتر در OpenWrt
            
            اگر می‌خواهید کلاینت‌های متصل به روتر (مانند لپ‌تاپ، گوشی و سایر دستگاه‌ها) از پروکسی **127.0.0.1:12334** استفاده کنند، می‌توانید تنظیمات زیر را اعمال کنید تا این پروکسی به عنوان سرویس مرکزی برای کل شبکه قابل دسترسی باشد.
            
            ---
            
            ??? info "1. **فعال کردن Port Forwarding در روتر**"
                        پروکسی **127.0.0.1:2334** که روی روتر تنظیم شده، به صورت پیش‌فرض فقط در خود روتر قابل استفاده است. برای دسترسی کلاینت‌ها، این پورت باید روی آدرس LAN روتر نیز باز شود.
                        
                        1. **اضافه کردن قانون NAT:**
                           برای این کار، باید ترافیک ورودی روی این پورت را به پروکسی هدایت کنید:
                           <div dir="ltr">
                           ```bash
                           iptables -t nat -A PREROUTING -i br-lan -p tcp --dport 2334 -j DNAT --to-destination 127.0.0.1:12334
                           iptables -A FORWARD -i br-lan -p tcp --dport 12334 -j ACCEPT
                           ```
                           </div>
                           **توضیح:**
                           - `br-lan`: اینترفیس LAN روتر است.
                           - `2334`: پورت پروکسی HiddifyCli.
                        
                        3. **ذخیره قوانین Iptables:**
                           برای ذخیره قوانین و اعمال آنها پس از هر راه‌اندازی مجدد، دستور زیر را اجرا کنید:
                           ```bash
                           service firewall restart
                           ```
                        
                        ---
                        
                        #### 2. **اعلام تنظیمات به کلاینت‌ها**
                        دستگاه‌های متصل به روتر باید تنظیمات مربوط به **پروکسی دستی** را انجام دهند. در کلاینت‌ها، مراحل زیر را دنبال کنید:
                        
                        ##### **برای ویندوز:**
                        1. وارد بخش **Settings** شوید.
                        2. به **Network & Internet** > **Proxy** بروید.
                        3. در قسمت **Manual proxy setup**:
                           - **Address** را روی آی‌پی LAN روتر (معمولاً `192.168.1.1`) تنظیم کنید.
                           - **Port** را `2334` قرار دهید.
                        4. تنظیمات را ذخیره کنید.
                        
                        ##### **برای اندروید:**
                        1. به تنظیمات شبکه Wi-Fi متصل شوید.
                        2. روی شبکه Wi-Fi فعلی کلیک کرده و **Modify Network** یا **Advanced Settings** را باز کنید.
                        3. **Proxy** را روی **Manual** تنظیم کنید:
                           - **Proxy hostname**: آی‌پی LAN روتر (مثلاً `192.168.1.1`).
                           - **Proxy port**: `2334`.
                        4. تنظیمات را ذخیره کنید.
                        
                        ##### **برای iOS:**
                        1. به تنظیمات Wi-Fi بروید.
                        2. روی شبکه متصل شده کلیک کنید و **Configure Proxy** را روی **Manual** قرار دهید.
                        3. آی‌پی روتر را در **Server** و پورت را `2334` وارد کنید.
                        4. تنظیمات را ذخیره کنید.
                        
                        ##### **برای مک‌اواس (macOS):**
                        1. به **System Preferences** > **Network** بروید.
                        2. روی اتصال فعلی خود کلیک کرده و **Advanced** را انتخاب کنید.
                        3. در تب **Proxies**، گزینه **SOCKS Proxy** را فعال کنید و:
                           - **SOCKS Proxy Server**: آی‌پی روتر (مثلاً `192.168.1.1`).
                           - **Port**: `2334`.
                        4. تنظیمات را ذخیره کنید.
                        
                        ---
                        
                        #### 3. **تست اتصال کلاینت‌ها**
                        برای اطمینان از عملکرد پروکسی:
                        - مرورگر کلاینت را باز کرده و سعی کنید به سایتی که بدون پروکسی فیلتر است متصل شوید.
                        - اگر اتصال برقرار شد، تنظیمات به درستی اعمال شده است.
                        
                        ---
                        
                        #### 4. **نکات تکمیلی**
                        - اگر کلاینت‌ها نیاز به استفاده خودکار از پروکسی دارند، می‌توانید از یک فایل **PAC (Proxy Auto-Configuration)** استفاده کنید و آن را در تنظیمات کلاینت‌ها معرفی کنید.
                        - آدرس PAC:
                          ```
                          http://192.168.1.1/proxy.pac
                          ```
                          فایل PAC می‌تواند مسیرها و استثنائات دلخواهی را برای استفاده از پروکسی تعریف کند.
                        
            
            
            
              
            
            
            ??? info "2. راه‌اندازی روتینگ در OpenWrt برای عبور تمام ترافیک از **Socks5 Proxy**"
            
                        برای هدایت تمام ترافیک اینترنت از طریق **Socks5 Proxy**، باید از ابزارهایی مانند `redsocks` یا `iptables` استفاده کنید. مراحل زیر را دنبال کنید:
                        
                        ---
                        
                        ### 1. **نصب ابزارهای مورد نیاز**
                        ابتدا ابزارهای لازم را نصب کنید. در OpenWrt، `redsocks` برای روتینگ ترافیک از طریق **Socks5 Proxy** استفاده می‌شود.
                        
                        1. به‌روزرسانی لیست بسته‌ها:
                           ```bash
                           opkg update
                           ```
                        
                        2. نصب `redsocks` و سایر ابزارها:
                           ```bash
                           opkg install redsocks iptables-mod-nat-extra iptables-mod-tproxy
                           ```
                        
                        ---
                        
                        ### 2. **پیکربندی Redsocks**
                        فایل پیکربندی `redsocks` را در مسیر `/etc/redsocks.conf` ایجاد کنید:
                        ```bash
                        nano /etc/redsocks.conf
                        ```
                        
                        و محتوای زیر را در آن قرار دهید:
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
                            port = 2334;        # پورت سرور Socks5
                            type = socks5;
                        }
                        ```
                        
                        **توضیح:**
                        - `local_ip` و `local_port`: آدرس و پورتی که Redsocks به آن گوش می‌دهد.
                        - `ip` و `port`: آدرس و پورت **Socks5 Proxy**.
                        
                        ---
                        
                        ### 3. **تنظیمات iptables برای روتینگ**
                        برای هدایت ترافیک به Redsocks، قوانین `iptables` را اضافه کنید:
                        
                        1. یک اسکریپت با نام `redsocks-routing` در `/etc/init.d/` ایجاد کنید:
                           ```bash
                           touch /etc/init.d/redsocks-routing
                           chmod +x /etc/init.d/redsocks-routing
                           ```
                        
                        2. اسکریپت را با محتوای زیر پر کنید:
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
                        
                        3. اسکریپت را فعال و اجرا کنید:
                           ```bash
                           service redsocks-routing enable
                           service redsocks-routing start
                           ```
                        
                        ---
                        
                        ### 4. **فعال‌سازی Redsocks**
                        برای فعال‌سازی و اجرای خودکار Redsocks:
                        ```bash
                        service redsocks enable
                        service redsocks start
                        ```
                        
                        ---
                        
                        ### 5. **بازنشانی روتر**
                        برای اعمال تغییرات، روتر را ری‌استارت کنید:
                        ```bash
                        reboot
                        ```
                        
                        ---
                        
                        ### 6. **بررسی عملکرد**
                        برای بررسی وضعیت و لاگ‌ها:
                        - وضعیت `redsocks`:
                           ```bash
                           ps | grep redsocks
                           ```
                        - لاگ‌های سیستم:
                           ```bash
                           logread | grep redsocks
                           ```
                        
                        ---
                        
                        ### نتیجه:
                        پس از اجرای این تنظیمات:
                        - تمام ترافیک TCP از طریق **Socks5 Proxy** عبور می‌کند.
                        - ترافیک شبکه‌های داخلی (`192.168.0.0/16`, `10.0.0.0/8`) و آدرس‌های محلی از پروکسی عبور نمی‌کنند.
                        
                        **نکته:** اگر به ترافیک UDP نیز نیاز دارید، باید از ابزارهای دیگری مانند `dns2socks` یا تنظیمات اضافی `redsocks` استفاده کنید.
                        
            
            
