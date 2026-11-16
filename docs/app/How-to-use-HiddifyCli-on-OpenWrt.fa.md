---
title: هستهٔ هیدیفای روی OpenWrt
---

# هستهٔ هیدیفای روی OpenWrt

این صفحه نشان می‌دهد چطور **هستهٔ هیدیفای** را روی روتر OpenWrt نصب کنید، لینک اتصالتان را به آن بدهید و ترافیک کل شبکهٔ خانه را از آن عبور دهید. هستهٔ هیدیفای (`hiddify-core` که به آن HiddifyCli هم می‌گویند) همان موتور اپ هیدیفای است، بدون خود اپ: [هستهٔ هیدیفای](../core/index.md) را ببینید.

!!! note "نوشته‌شده برای هستهٔ هیدیفای نسخهٔ 5.9"
    این صفحه برای هستهٔ هیدیفای نسخهٔ **5.9** (5.9.3) و OpenWrt **نسخهٔ 23.05 یا جدیدتر** است (OpenWrt 24.10 و 25.12 از مدیر بستهٔ `apk` استفاده می‌کنند و نسخه‌های قدیمی‌تر از `opkg`). راهنماهای قدیمی می‌گفتند فایل `hiddify-cli-linux-…tar.gz` را دانلود کنید و سرویس را دستی بنویسید؛ این کار دیگر لازم نیست و آن فایل‌ها هم دیگر وجود ندارند.

## پیش از شروع

- **فضای خالی روی روتر:** هستهٔ هیدیفای حدود **۱۰۵ مگابایت** فضای خالی لازم دارد. روی روتر بررسی کنید:

    ```bash
    df -h /overlay
    ```

    خیلی از روترهای کوچک فقط ۱۶ تا ۱۲۸ مگابایت حافظه دارند. اگر فضای خالی روتر شما کمتر است، اول یک فلش USB را به‌عنوان فضای اضافه وصل کنید ([extroot](https://openwrt.org/docs/guide-user/additional-software/extroot_configuration))، یا از روتر یا مینی‌پی‌سی با حافظهٔ بیشتر استفاده کنید.

- **دسترسی SSH** به روتر (`ssh root@192.168.1.1` یا آدرس روتر خودتان).
- **یک لینک اتصال:** لینک سابسکریپشن یا لینک کانفیگ، مثلاً از پنل هیدیفای.

## قدم ۱: نصب

نصب‌کننده پردازندهٔ روتر را تشخیص می‌دهد، بستهٔ آمادهٔ آخرین نسخهٔ هستهٔ هیدیفای را دانلود و نصب می‌کند و سرویسش را راه می‌اندازد. نصب‌کننده به `bash` و `curl` نیاز دارد که OpenWrt به‌طور پیش‌فرض ندارد.

1. `bash` و `curl` را نصب کنید.

    در OpenWrt 24.10 و جدیدتر (`apk`):

    ```bash
    apk update && apk add bash curl
    ```

    در OpenWrt 23.05 (`opkg`):

    ```bash
    opkg update && opkg install bash curl
    ```

2. نصب‌کننده را اجرا کنید:

    ```bash
    bash <(curl -fsSL https://raw.githubusercontent.com/hiddify/hiddify-core/main/installer.sh)
    ```

وقتی کارش تمام شد، `Installation successful!` و محل فایل تنظیمات و سرویس را نشان می‌دهد.

??? info "نصب دستی بسته"
    هر [نسخهٔ هستهٔ هیدیفای](https://github.com/hiddify/hiddify-core/releases/latest) برای همهٔ انواع پردازندهٔ OpenWrt بسته دارد: فایل‌های `.apk` برای OpenWrt 24.10 و جدیدتر و فایل‌های `.ipk` برای OpenWrt 23.05.

    1. معماری بستهٔ روترتان را پیدا کنید: `apk --print-arch` (یا در OpenWrt 23.05، خط آخر `opkg print-architecture`). مثلاً `mipsel_24kc`، `aarch64_cortex-a53` یا `x86_64`.
    2. فایل با همان اسم را از صفحهٔ نسخه دانلود کنید، مثلاً `hiddify-core-5.9.3-r0_mipsel_24kc.apk` یا `hiddify-core_5.9.3_mipsel_24kc.ipk`، و در پوشهٔ `/tmp` روتر کپی کنید.
    3. نصبش کنید: `apk add --allow-untrusted /tmp/hiddify-core-*.apk` (یا `opkg install /tmp/hiddify-core_*.ipk`).
    4. راهش بیندازید: `/etc/init.d/hiddify-core enable && /etc/init.d/hiddify-core restart`.

## قدم ۲: دادن لینک اتصال

دستور `run` هستهٔ هیدیفای لینک‌های شما را می‌خواند و بقیهٔ تنظیمات را خودش می‌سازد. لینک سابسکریپشن، لینک کانفیگ تکی (`vless://`، `vmess://` و …) و کانفیگ‌های sing-box، Clash و Xray را می‌خواند: [چه چیزهایی را `run` می‌خواند](../core/index.md#run-or-srun) را ببینید.

1. لینک سابسکریپشن خود (یا لینک‌های کانفیگ، هر کدام در یک خط) را در یک فایل بگذارید:

    ```bash
    echo 'https://example.com/your-subscription-link' > /etc/hiddify-core/links.txt
    ```

2. به سرویس بگویید از این فایل استفاده کند و آن را دوباره راه بیندازید:

    ```bash
    uci set hiddify-core.main.conffile='/etc/hiddify-core/links.txt'
    uci commit hiddify-core
    /etc/init.d/hiddify-core restart
    ```

## قدم ۳: بررسی کار

- لاگ سرویس:

    ```bash
    logread -e hiddify-core
    ```

- روی گوشی یا کامپیوتری که به روتر وصل است، سایتی را باز کنید که آی‌پی شما را نشان می‌دهد. باید آی‌پی سرور پروکسی را نشان دهد، نه آی‌پی خودتان را.

## حالت روتر و حالت پروکسی { #router-mode-and-proxy-mode }

سرویس دو حالت دارد که در `/etc/config/hiddify-core` (`option mode`) تعیین می‌شود:

- `router` (پیش‌فرض): همهٔ دستگاه‌های پشت روتر، برای TCP، UDP و پینگ، از هستهٔ هیدیفای عبور می‌کنند و روی خود دستگاه‌ها لازم نیست چیزی تنظیم کنید. اتصال‌هایی که از بیرون می‌آیند هنوز به روتر و پورت‌فورواردهایش می‌رسند. [اینترنت آزاد برای همهٔ دستگاه‌های پشت روتر](How-to-Enable-Free-Internet-Access-for-Clients-Behind-an-OpenWrt-Router-Using-HiddifyCli.md) را ببینید.
- `proxy`: فقط یک پروکسی محلی HTTP و SOCKS5 روی خود روتر اجرا می‌شود، روی `127.0.0.1:12334`.

برای عوض کردن حالت:

```bash
uci set hiddify-core.main.mode='proxy'
uci commit hiddify-core
/etc/init.d/hiddify-core restart
```

## مدیریت سرویس

| می‌خواهید | دستور |
|---|---|
| متوقف یا روشنش کنید | `/etc/init.d/hiddify-core stop` / `start` |
| بعد از تغییر دوباره راهش بیندازید | `/etc/init.d/hiddify-core restart` |
| موقع روشن شدن روتر اجرا نشود | `/etc/init.d/hiddify-core disable` |
| لاگ را ببینید | `logread -e hiddify-core` |
| به جدیدترین نسخه به‌روزش کنید | نصب‌کنندهٔ قدم ۱ را دوباره اجرا کنید |
| حذفش کنید | `apk del hiddify-core` (یا `opkg remove hiddify-core`) |

وقتی خود OpenWrt را به‌روز می‌کنید (sysupgrade)، تنظیمات این بسته حفظ می‌شود. همهٔ گزینه‌های هستهٔ هیدیفای در [هستهٔ هیدیفای](../core/index.md) و [راهنمای خط فرمان](../core/cli.md) توضیح داده شده‌اند.

## مقاله‌های مرتبط

- [اینترنت آزاد برای همهٔ دستگاه‌های پشت روتر OpenWrt](How-to-Enable-Free-Internet-Access-for-Clients-Behind-an-OpenWrt-Router-Using-HiddifyCli.md)
- [هستهٔ هیدیفای](../core/index.md) و [راهنمای دستورهای آن](../core/cli.md)
- [حالت روتر در لینوکس](Router-mode-on-Linux.md): همین کار روی یک گیت‌وی لینوکسی، با اپ هیدیفای

