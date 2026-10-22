---
title: آموزش راه‌اندازی تانل GOST به عنوان سرور میانی
---

# آموزش راه‌اندازی تانل GOST به عنوان سرور میانی

این صفحه نشان می‌دهد چطور با **GOST** (GO Simple Tunnel) یک سرور را به سرور میانی برای هیدیفای‌منیجر تبدیل کنید. GOST یک برنامه کوچک و متن‌باز است که پورت‌ها را از یک سرور به سرور دیگر می‌فرستد.

**سرور میانی** (Relay) یک سرور دوم، معمولا داخل کشور خودتان است که کاربران به آن وصل می‌شوند و ترافیکشان را به سرور اصلی هیدیفای در خارج می‌رساند. وقتی IP سرور اصلی از کشور شما مسدود یا کند است، این کار کمک می‌کند. [درباره سرور میانی بیشتر بخوانید](/fa/manager/domain-worker-cdn-and-tunneling/How-to-add-relay-domain-to-Hiddify-manager/).

<div align=center dir="rtl" markdown="1">

ویدئوی آموزشی این روش را هم می‌توانید ببینید:

<a href="https://youtu.be/T3yfTqqQqJQ"><img width="32%" src="https://user-images.githubusercontent.com/125398461/235361265-c8f5c2ab-1ccd-46d2-b2b2-112d4fe106dd.png" alt="ویدئوی آموزش تانل GOST" /></a>

</div>

<div dir="rtl" markdown="1">

<div align=center dir="rtl" markdown="1">

<img src="https://user-images.githubusercontent.com/125398461/235339506-bdd76cec-0378-4942-8352-ebebeb006231.png" alt="نمودار: کاربران به سرور میانی وصل می‌شوند و سرور میانی ترافیک را به سرور اصلی می‌فرستد">
</div>

## چرا GOST به جای فوروارد ساده با IP-Tables؟

- می‌توانید تانل را به **دامنه** سرور اصلی وصل کنید، نه به IP آن؛ پس IP سرور اصلی در تنظیمات سرور میانی دیده نمی‌شود.
- به شکل سرویس سیستم اجرا می‌شود و بعد از ری‌استارت سرور خودبه‌خود دوباره روشن می‌شود.
- با همه پروتکل‌های هیدیفای (VLESS، VMess، Trojan، WebSocket، gRPC و غیره) کار می‌کند، چون ترافیک خام TCP را جابه‌جا می‌کند. ترافیک پروکسی شما با خود پروتکل پروکسی رمزنگاری شده باقی می‌ماند.
- هر تعداد پورت TCP یا UDP که بخواهید می‌توانید فوروارد کنید.

!!! tip "راه ساده‌تر"
    [سرور میانی‌ساز هیدیفای](/fa/manager/domain-worker-cdn-and-tunneling/How-to-setup-relay-server-using-Hiddify-Relay-Builder/) می‌تواند GOST را از طریق منو برای شما نصب کند.

## پیش‌نیازها

- یک سرور اصلی که هیدیفای‌منیجر روی آن نصب است. [راهنمای نصب](/fa/manager/installation-and-setup/guide/) را ببینید.
- یک سرور میانی با Ubuntu یا Debian و دسترسی SSH با کاربر `root`. با SSH آشنا نیستید؟ [نحوه اتصال به سرور با SSH](/fa/manager/installation-and-setup/How-to-connect-to-server-via-SSH/) را ببینید.
- دامنه‌ای که **مستقیم** به IP سرور اصلی اشاره کند (پروکسی خاموش، نه از طریق CDN)، یا فقط IP سرور اصلی.

## نصب GOST روی سرور میانی

1. با SSH به **سرور میانی** وصل شوید.
2. GOST را دانلود کنید و از حالت فشرده خارج کنید:

    ```bash
    sudo apt install wget nano -y
    wget https://github.com/ginuerzh/gost/releases/download/v2.11.5/gost-linux-amd64-2.11.5.gz
    gunzip gost-linux-amd64-2.11.5.gz
    ```

    این نسخه برای سرورهای معمولی x86-64 (amd64) است. روی سرور ARM به جای آن از `gost-linux-armv8-2.11.5.gz` استفاده کنید و نام فایل را در قدم بعد هم مطابق آن عوض کنید.

3. برنامه را به پوشه سیستم منتقل کنید و اجازه اجرا به آن بدهید:

    ```bash
    sudo mv gost-linux-amd64-2.11.5 /usr/local/bin/gost
    sudo chmod +x /usr/local/bin/gost
    ```

4. یک فایل سرویس بسازید تا GOST در پس‌زمینه و بعد از هر ری‌استارت اجرا شود. ویرایشگر را باز کنید:

    ```bash
    sudo nano /usr/lib/systemd/system/gost.service
    ```

5. این متن را در ویرایشگر قرار دهید:

    ```ini
    [Unit]
    Description=GO Simple Tunnel
    After=network.target
    Wants=network.target

    [Service]
    Type=simple
    ExecStart=/usr/local/bin/gost -L=tcp://:443/domain.com:443 -L=tcp://:80/domain.com:80

    [Install]
    WantedBy=multi-user.target
    ```

6. **هر دو** `domain.com` را با دامنه مستقیم سرور اصلی (یا IP آن) عوض کنید.
7. با `Ctrl+S` ذخیره کنید و با `Ctrl+X` خارج شوید. (در نسخه‌های قدیمی nano، `Ctrl+X` و سپس `Y` و `Enter` را بزنید.)
8. سرویس را روشن کنید و طوری تنظیم کنید که با هر بار روشن شدن سرور اجرا شود:

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable --now gost
    ```

### بررسی درستی کار

<div dir="ltr" markdown="1">

```bash
sudo systemctl status gost
```

</div>

باید عبارت `active (running)` را ببینید. برای خروج از این صفحه `q` را بزنید. اگر `failed` دیدید، خط `ExecStart` را از نظر غلط تایپی بررسی و اصلاح کنید و دو دستور قدم ۸ را دوباره اجرا کنید.

برای فوروارد پورت‌های بیشتر، یک `-L=tcp://:PORT/domain.com:PORT` دیگر به خط `ExecStart` اضافه کنید. برای UDP به جای `tcp://` بنویسید `udp://`.

!!! note "درباره نسخه‌های GOST"
    این صفحه از GOST نسخه 2.11.5 از پروژه اصلی [ginuerzh/gost](https://github.com/ginuerzh/gost) استفاده می‌کند. آخرین نسخه آن 2.12.0 (اکتبر ۲۰۲۴) است. نسخه‌ای که فعالانه توسعه داده می‌شود GOST v3 در [go-gost/gost](https://github.com/go-gost/gost) است؛ سرور میانی‌ساز هیدیفای نسخه ۳ را نصب می‌کند و از همان شکل دستور `-L=tcp://...` استفاده می‌کند.

## تعریف سرور میانی در هیدیفای‌منیجر

1. با یک رکورد `A`، یک ساب‌دامین (مثلا `relay.example.com`) را به **IP سرور میانی** وصل کنید. در Cloudflare پروکسی را خاموش بگذارید (ابر خاکستری).
2. در پنل، بخش **دامنه‌ها** را باز کنید، روی **افزودن دامنه** بزنید، ساب‌دامین را وارد کنید و حالت **رله** را انتخاب کنید.
3. دامنه اشتراک خود را ویرایش کنید، در بخش **نمایش کانفیگ‌های** دامنه سرور میانی را انتخاب کنید و تغییرات را اعمال کنید.

برای مراحل کامل، [نحوه افزودن سرور (دامنه) میانی به هیدیفای‌منیجر](/fa/manager/domain-worker-cdn-and-tunneling/How-to-add-relay-domain-to-Hiddify-manager/) را ببینید.

??? note "تصاویر نسخه قدیمی پنل"
    <img src="https://github.com/hiddify/hiddify.com/assets/125398461/3f41d92a-04b9-44fb-b645-ac660601472a" alt="افزودن دامنه سرور میانی در نسخه قدیمی پنل">

    <img src="https://github.com/hiddify/hiddify.com/assets/125398461/3661045d-ced7-4694-916f-6ef160c63230" alt="انتخاب دامنه سرور میانی در تنظیمات دامنه اشتراک، نسخه قدیمی پنل">

## حذف GOST از سرور میانی

این دستورها را روی سرور میانی اجرا کنید:

<div dir="ltr" markdown="1">

```bash
sudo systemctl disable --now gost
sudo rm -f /usr/lib/systemd/system/gost.service /usr/local/bin/gost
sudo systemctl daemon-reload
```

</div>

</div>
