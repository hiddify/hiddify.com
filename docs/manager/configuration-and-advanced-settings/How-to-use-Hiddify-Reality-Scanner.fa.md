---
title: آموزش استفاده از اسکنر ریالتی هیدیفای
---

<div dir="rtl" markdown="1">

# اسکنر ریالیتی هیدیفای
اسکنر ریالیتی هیدیفای کمک می‌کند سایت‌های مناسبی برای دامنه Reality پیدا کنید. این ابزار فهرستی از نام سایت‌ها (**SNI**، یعنی نام سایتی که اپ هنگام باز کردن اتصال رمزنگاری‌شده می‌فرستد) را از داخل شبکه خود شما تست می‌کند و نشان می‌دهد کدام‌ها بهتر کار می‌کنند. این صفحه برای ادمین‌های هیدیفای‌منیجر است که با اجرای دستور روی سرور و کامپیوتر آشنا هستند. برای اطلاعات بیشتر درباره پروژه، [راهنمای مشارکت](https://github.com/hiddify/Hiddify-Reality-Scanner/blob/main/CONTRIBUTING.md) را ببینید.

!!! warning "این ابزار دیگر به‌طور فعال نگهداری نمی‌شود"
    آخرین نسخه اسکنر در PyPI نسخه 1.8.0 است که در نوامبر ۲۰۲۳ منتشر شده است. این ابزار برای نسخه‌های قدیمی هیدیفای‌منیجر نوشته شده و برای نسخه ۱۳ و ۱۴ به‌روز نشده است، پس ممکن است آن‌طور که اینجا آمده کار نکند. در هیدیفای‌منیجر نسخه ۱۴، مراحل **افزودن دامنه** هم خودش بررسی می‌کند که سایت برای Reality مناسب است یا نه (TLS 1.3 و HTTP/2). [آموزش استفاده از Reality در هیدیفای‌منیجر](/fa/manager/configuration-and-advanced-settings/How-to-use-Reality-on-Hiddify/) را ببینید.

## این ابزار چطور کار می‌کند
اسکنر دو بخش دارد:

- **سمت سرور**: یک سرور Reality موقت برای تست که روی سرور شما اجرا می‌شود.
- **سمت کلاینت**: یک برنامه پایتون که روی کامپیوتر شما و داخل شبکه‌ای که می‌خواهید تست کنید (مثلا اینترنت خانگی شما در ایران) اجرا می‌شود.

## پیش‌نیازها
- سروری که بتوانید با SSH به آن وصل شوید ([آموزش اتصال به سرور با SSH](/fa/manager/installation-and-setup/How-to-connect-to-server-via-SSH/) را ببینید).
- کامپیوتری که [پایتون](https://www.python.org/downloads/) روی آن نصب باشد.

!!! warning "در زمان تست، اتصال‌های Xray کاربران قطع می‌شود"
    اگر هیدیفای‌منیجر روی همین سرور نصب است، مراحل زیر سرویس `hiddify-xray` را متوقف می‌کنند. تا وقتی این سرویس متوقف است، کانفیگ‌های Xray کاربران شما کار نمی‌کنند. تست را در زمان کم‌ترافیک انجام دهید و در پایان، سرویس را دوباره روشن کنید (آخرین مرحله همین صفحه).

## نصب سمت سرور
این دستورها را روی سرور خود و از طریق SSH اجرا کنید.

1. Xray قدیمی را که با نصب‌کننده رسمی XTLS نصب شده حذف کنید، Xray هیدیفای را متوقف کنید و هسته Xray سفارشی هیدیفای را نصب کنید:

    ```bash
    # remove old xray
    bash -c "$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)" @ remove

    # only if you have Hiddify Manager on this server
    systemctl stop hiddify-xray

    # install hiddify custom xray
    bash -c "$(curl -L https://github.com/hiddify/Xray-core-custom/raw/main/install-release.sh)" @ install
    ```

2. فایل کانفیگ سرور اسکنر را دانلود کنید و لینک‌های تست را چاپ کنید (یکی برای IPv6 و یکی برای IPv4):

    ```bash
    curl -o server_config.json https://raw.githubusercontent.com/hiddify/Hiddify_Reality_Scanner/main/server_config.json

    echo "---------------IPV6---------"
    echo "vless://hiddify@$(curl -6 ip.sb):11443/?fp=chrome&security=reality&pbk=Z84J2IelR9ch3k8VtlVhhs5ycBUlXA7wHBWcBrjqnAw&sid=6ba85179e30d4fc2&sni=www.google.com&type=tcp&flow=xtls-rprx-vision&encryption=none#Hiddify"

    echo "---------------IPV4---------"
    echo "vless://hiddify@$(curl -4 ip.sb):11443/?fp=chrome&security=reality&pbk=Z84J2IelR9ch3k8VtlVhhs5ycBUlXA7wHBWcBrjqnAw&sid=6ba85179e30d4fc2&sni=www.google.com&type=tcp&flow=xtls-rprx-vision&encryption=none#Hiddify"
    ```

    لینک `vless://` چاپ‌شده را کپی کنید. این کانفیگ تست شماست و شبیه لینک زیر است، با این تفاوت که به جای `SERVER_IP` آی‌پی سرور شما در آن است:

    ```text
    vless://hiddify@SERVER_IP:11443/?fp=chrome&security=reality&pbk=Z84J2IelR9ch3k8VtlVhhs5ycBUlXA7wHBWcBrjqnAw&sid=6ba85179e30d4fc2&sni=www.yahoo.com&type=tcp&flow=xtls-rprx-vision&encryption=none#Hiddify
    ```

3. سرور تست موقت را اجرا کنید. تا پایان اسکن این پنجره را باز نگه دارید:

    ```bash
    xray run -c server_config.json
    ```

    سرور تست روی پورت `11443` کار می‌کند. اگر اسکنر نتوانست وصل شود، مطمئن شوید این پورت در فایروال سرور باز است.

## نصب سمت کلاینت
روی کامپیوتر خود یک ترمینال باز کنید (در ویندوز: Command Prompt یا PowerShell) و اسکنر را نصب کنید:

```bash
pip install -U hiddify_reality_scanner
```

## استفاده پایه
روی کامپیوتر خود یکی از دستورهای زیر را اجرا کنید. به جای `vless_link` لینک تستی را که از سرور کپی کردید بگذارید و علامت‌های نقل‌قول را نگه دارید:

```bash
python -m hiddify_reality_scanner "vless_link"
```

یا

```bash
hiddify_reality_scanner "vless_link"
```

برای قطع کردن اسکن، کلیدهای `Ctrl+C` را بزنید.

## استفاده پیشرفته
برای اینکه مشخص کنید کدام SNIها تست شوند و چند نتیجه نگه داشته شود، این دستور را اجرا کنید:

```bash
hiddify_reality_scanner --jobs 10 --limit 100 --sni yahoo.com,google.com "vless_link"
```

اگر فهرست SNIها را در یک فایل دارید، مسیر فایل را بعد از `--sni` بنویسید:

```bash
hiddify_reality_scanner --jobs 10 --limit 100 --sni path_to_the_list "vless_link"
```

معنی این گزینه‌ها:

- `--jobs 10`: تعداد SNIهایی که هم‌زمان تست می‌شوند. پیش‌فرض: 10.
- `--sni`: SNIهایی که باید تست شوند، جداشده با کاما، یا مسیر فایلی که فهرست آن‌ها را دارد.
- `--limit 100`: تعداد SNIهای سالمی که در نتیجه نگه داشته می‌شوند. پیش‌فرض: 10.

## نتایج
اسکنر نتایج را روی کامپیوتر شما در فایل‌های `results.txt` و `results.json` ذخیره می‌کند. از بهترین SNIها به عنوان دامنه Reality و نام‌های سرور در سرور خود استفاده کنید. [آموزش استفاده از Reality در هیدیفای‌منیجر](/fa/manager/configuration-and-advanced-settings/How-to-use-Reality-on-Hiddify/) را ببینید.

## پایان کار: روشن کردن دوباره Xray هیدیفای
اگر هیدیفای‌منیجر روی سرور نصب است، سرور تست را متوقف کنید (در پنجره آن `Ctrl+C` بزنید). سپس این دستور را روی سرور و از طریق SSH اجرا کنید:

```bash
systemctl start hiddify-xray
```

بررسی کنید که کاربران دوباره می‌توانند وصل شوند.

</div>
