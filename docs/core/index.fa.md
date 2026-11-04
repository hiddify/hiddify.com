---
title: راهنمای هسته
description: هسته هیدیفای، هسته پروکسی اپ هیدیفای، به‌صورت ابزار خط فرمان برای سرور، روتر و دسکتاپ
weight: -18
comments: false
---

# هسته هیدیفای (Hiddify Core)

هسته هیدیفای (`hiddify-core`، فایل اجرایی `HiddifyCli`) همان هسته پروکسی است که درون اپ هیدیفای در
اندروید، iOS، ویندوز، مک و لینوکس کار می‌کند. می‌توانید آن را به‌تنهایی و از خط فرمان هم اجرا کنید: روی
سرور، روی روتر (OpenWrt) یا روی دسکتاپی که صفحه‌نمایش ندارد.

این هسته بر پایه **hiddify-sing-box**، فورک هیدیفای از [sing-box](https://sing-box.sagernet.org/)، ساخته
شده است. هر کانفیگ sing-box در آن کار می‌کند و پروتکل‌ها، ترنسپورت‌ها و ترفندهای ضدسانسور بسیاری
دارد که sing-box اصلی ندارد. hiddify-core روی این هسته یک سازنده کانفیگ هم دارد: یک لینک اشتراک‌گذاری،
یک لینک سابسکریپشن یا کانفیگی تقریبا در هر قالبی به آن بدهید تا یک کانفیگ کامل کلاینت برایتان بسازد، با
پروکسی محلی یا TUN، DNS، مسیریابی و گروه‌های پروکسی.

!!! info "هسته هیدیفای در یک نگاه"
    - **دانلود:** [نسخه‌های hiddify-core در گیت‌هاب](https://github.com/hiddify/hiddify-core/releases)، برای لینوکس، ویندوز و مک، برای پردازنده‌های مختلف، و بسته‌های OpenWrt.
    - **کد منبع:** [hiddify-core](https://github.com/hiddify/hiddify-core) و [hiddify-sing-box](https://github.com/hiddify/hiddify-sing-box).
    - **راهنمای خط فرمان:** [همه دستورها و گزینه‌ها](cli.md).
    - **قابلیت‌های هسته:** [قابلیت‌های sing-box هیدیفای](sing-box/index.md)، با یک صفحه برای هر پروتکل، ترنسپورت و قابلیت DNS.

## نصب

در لینوکس (اوبونتو، دبیان، CentOS، OpenWrt و دیگر توزیع‌ها) این دستور سیستم و پردازنده شما را تشخیص
می‌دهد، `/usr/bin/hiddify-core` را نصب می‌کند و یک سرویس (systemd، یا procd در OpenWrt) می‌سازد:

```bash
bash <(curl https://i.hiddify.com/core)
```

سرویس این دستور را اجرا می‌کند: `hiddify-core -D /var/lib/hiddify-core run -c /etc/hiddify-core/config.json`.
فایل `/etc/hiddify-core/config.json` را ویرایش کنید و سپس سرویس را با `systemctl restart hiddify-core`
(در OpenWrt با `/etc/init.d/hiddify-core restart`) دوباره راه بیندازید.

راه‌های دیگر:

- **دانلود دستی:** فایل فشرده سیستم خود را از [صفحه نسخه‌ها](https://github.com/hiddify/hiddify-core/releases)
  بگیرید و باز کنید. در لینوکس پوشه `lib` را کنار `HiddifyCli` نگه دارید. در ویندوز `HiddifyCli.exe` را از
  ترمینال اجرا کنید.
- **داکر:** `docker pull ghcr.io/hiddify/hiddify-core:latest`، یا `docker-compose up -d` در پوشه `docker`
  مخزن.

در نمونه‌های این سایت نام فایل اجرایی `HiddifyCli` است؛ پس از نصب با اسکریپت لینوکس نام آن
`hiddify-core` است. هر دو یک برنامه‌اند.

## اجرای کانفیگ: `run` یا `srun` {#run-or-srun}

hiddify-core دو راه برای اجرای کانفیگ دارد. آن را که با چیزی که در دست دارید جور است انتخاب کنید.

| چه دارید | دستور | چه می‌شود |
|---|---|---|
| لینک‌های اشتراک‌گذاری (`vless://`، `hy2://`، `wg://`…)، لینک سابسکریپشن، کانفیگ Clash یا Xray، یا فقط outboundهای یک کانفیگ sing-box | `run` | hiddify-core پروکسی‌ها را می‌خواند، بقیه کانفیگ (پروکسی محلی یا TUN، DNS، مسیریابی، گروه‌ها) را از تنظیمات هیدیفای می‌سازد و اجرا می‌کند |
| یک کانفیگ کامل sing-box که باید دقیقا همان‌طور که نوشته شده اجرا شود (با inboundها، DNS، route و همه چیز) | `srun` | hiddify-core کانفیگ را همان‌طور که هست اجرا می‌کند، مثل `sing-box run`، با همه قابلیت‌های هیدیفای |

### `run`: از پروکسی تا کلاینت آماده

```bash
# فایلی از لینک‌ها، هر خط یک لینک، یا یک سابسکریپشن base64
HiddifyCli run -c links.txt

# لینک سابسکریپشن؛ اگر سرور profile-update-interval بفرستد دوباره به‌روز می‌شود
HiddifyCli run -c https://example.com/sub/abc

# فقط outboundهای کانفیگ sing-box استفاده می‌شوند
HiddifyCli run -c outbounds.json
```

`run` به‌طور پیش‌فرض یک پروکسی mixed (HTTP و SOCKS5) روی `127.0.0.1:12334` باز می‌کند، پروکسی‌ها را در
یک گروه انتخاب با تست خودکار می‌گذارد و DNS را به `1.1.1.1` می‌فرستد. مرورگر یا سیستم را به این پروکسی
وصل کنید، یا بگذارید hiddify-core این کار را بکند:

```bash
# VPN برای کل سیستم (دسترسی root یا administrator لازم است)
sudo HiddifyCli run -c links.txt --tun

# تنظیم پروکسی سیستم در دسکتاپ
HiddifyCli run -c links.txt --system-proxy

# تنظیمات اپ هیدیفای شما (تنظیمات ← ⋮ ← خروجی ← "خروجی تمام تنظیمات به فایل")
HiddifyCli run -c links.txt -d hiddify-settings.json
```

`run` همه این‌ها را به‌عنوان ورودی می‌پذیرد:

- لینک‌های اشتراک‌گذاری همه پروتکل‌هایی که اپ پشتیبانی می‌کند، هر خط یک لینک، ساده یا base64؛
- لینک‌های سابسکریپشن، حتی داخل یک فایل کنار لینک‌های دیگر؛
- کانفیگ JSON sing-box: یک کانفیگ کامل (فقط `outbounds` و `endpoints` آن برداشته می‌شود)، فهرستی از
  outboundها، یا یک outbound تنها؛
- کانفیگ YAML کلش یا mihomo (بخش `proxies` آن)؛
- کانفیگ JSON ایکس‌ری (Xray)؛
- فایل `.conf` وایرگارد.

با `--full-config`، دستور `run` inboundها، DNS و قوانین route ورودی sing-box را هم نگه می‌دارد و بخش‌های
خودش را کنار آن‌ها می‌سازد. اگر کانفیگ باید بدون هیچ تغییری اجرا شود، از `srun` استفاده کنید.

### `srun`: یک کانفیگ کامل sing-box همان‌طور که هست

```bash
HiddifyCli srun -c config.json
```

`srun` همان دستور `run` در sing-box است. یک کانفیگ کامل، با inbound، DNS، route و experimental خودتان،
می‌گیرد و چیزی به آن اضافه نمی‌کند. همه گزینه‌های sing-box کار می‌کنند، همراه با افزوده‌های هیدیفای:
XHTTP، finalmask، WARP، AmneziaWG، تونل‌های DNS، بالانسر و بقیه (ببینید
[قابلیت‌های sing-box هیدیفای](sing-box/index.md)).

```bash
# چند فایل به ترتیب نامشان با هم ادغام می‌شوند
HiddifyCli srun -c base.json -c outbounds.json

# همه فایل‌های .json یک پوشه
HiddifyCli srun -C /etc/hiddify-core/conf.d

# خواندن کانفیگ از ورودی استاندارد
cat config.json | HiddifyCli srun -c stdin
```

با فرستادن `SIGHUP` کانفیگ بدون توقف دوباره بارگذاری می‌شود (کانفیگ جدید اول بررسی می‌شود)؛ `SIGINT`
یا `SIGTERM` آن را متوقف می‌کند. برای اجرای **سرور** با hiddify-core هم از `srun` استفاده کنید، چون کانفیگ
سرور بیشتر inbound است.

!!! tip "پروکسی‌ها را به کانفیگ کامل تبدیل کنید و بعد ویرایشش کنید"
    `HiddifyCli parse links.txt -o outbounds.json` لینک‌ها را به outboundهای sing-box تبدیل می‌کند و
    `HiddifyCli build -c outbounds.json -o config.json` کانفیگ کامل کلاینت را که `run` استفاده می‌کرد
    می‌سازد. `config.json` را ویرایش کنید و با `srun` اجرا کنید. ببینید [راهنمای خط فرمان](cli.md).

## تفاوت با sing-box، Xray و mihomo {#differences}

| | hiddify-core | sing-box | Xray-core | mihomo |
|---|---|---|---|---|
| پایه | فورکی از sing-box 1.15 با افزوده‌های هیدیفای | — | هسته خودش، از خانواده V2Ray | فورکی از Clash |
| قالب کانفیگ | JSON sing-box | JSON sing-box | JSON ایکس‌ری | YAML کلش |
| ورودی‌هایی که می‌خواند | لینک‌های اشتراک‌گذاری، سابسکریپشن، JSON sing-box، JSON ایکس‌ری، YAML کلش و mihomo، `.conf` وایرگارد | JSON sing-box | JSON ایکس‌ری | YAML کلش، و سابسکریپشن لینک در proxy providerها |
| ساخت کانفیگ کلاینت از پروکسی‌های خام | بله، با `run` (TUN یا پروکسی، DNS، قوانین، گروه‌ها) | خیر، کل کانفیگ را خودتان می‌نویسید | خیر، کل کانفیگ را خودتان می‌نویسید | خیر، کل کانفیگ را خودتان می‌نویسید |
| API کنترل | gRPC (که اپ هیدیفای استفاده می‌کند) و Clash API | Clash API | gRPC | REST (Clash API) |

### در مقایسه با sing-box

hiddify-core هر کانفیگ sing-box را اجرا می‌کند و این‌ها را اضافه دارد:

- **ترنسپورت‌های ایکس‌ری در sing-box:** [XHTTP](sing-box/features/transports/xhttp.md)،
  [mKCP](sing-box/features/transports/kcp.md)، [XDRIVE](sing-box/features/transports/xdrive.md)،
  [finalmask](sing-box/features/transports/finalmask.md)، [ترنسپورت raw](sing-box/features/transports/raw.md)،
  [رمزنگاری VLESS](sing-box/features/protocols/vless-encryption.md) و
  [مسیرهای چندبخشی gRPC](sing-box/features/transports/grpc-custom-path.md)، تا کانفیگ‌های ساخته‌شده برای
  ایکس‌ری همان‌طور که هستند بارگذاری شوند.
- **پروتکل‌های بیشتر:** [WARP](sing-box/features/protocols/warp.md) با ثبت‌نام حساب رایگان،
  [اسکنر اندپوینت و نویز](sing-box/features/protocols/warp-scanner.md) و
  [MASQUE](sing-box/features/protocols/warp-masque.md)؛
  [AmneziaWG](sing-box/features/protocols/amneziawg.md)؛ [سایفون](sing-box/features/protocols/psiphon.md)؛
  [Mieru](sing-box/features/protocols/mieru.md)؛ [Sudoku](sing-box/features/protocols/sudoku.md)؛
  [TrustTunnel](sing-box/features/protocols/trusttunnel.md)؛
  [GooseRelay](sing-box/features/protocols/gooserelay.md)؛ [Bond](sing-box/features/protocols/bond.md)؛
  [تونل معکوس](sing-box/features/protocols/tunnel.md)؛ [inbound SSH](sing-box/features/protocols/ssh.md)؛ و
  [outbound قدیمی وایرگارد](sing-box/features/protocols/wireguard-legacy.md) که از نسخه اصلی حذف شده است.
- **تونل‌های DNS** که خودشان ریزالورهای عمومی سالم را پیدا می‌کنند:
  [DNSTT](sing-box/features/protocols/dnstt.md)، [MasterDNS](sing-box/features/protocols/masterdns.md) و
  [Soar](sing-box/features/protocols/soar.md)، با یک
  [استخر هوشمند ریزالور](sing-box/features/dns/smart-dns-pool.md) مشترک.
- **ترفندهای ضدسانسور:** [تکه‌تکه کردن TLS](sing-box/features/tls-fragment.md)،
  [ترفندهای TLS](sing-box/features/tls-tricks.md) (SNI با حروف درهم و padding) و
  [افزوده‌های REALITY](sing-box/features/reality-hiddify.md).
- **گروه‌ها و پایش:** [بالانسر](sing-box/features/groups/balancer.md) با چند روش،
  گروه [fallback](sing-box/features/groups/fallback.md)،
  [افزوده‌های URL test](sing-box/features/groups/urltest.md)،
  [پایش پس‌زمینه](sing-box/features/groups/monitoring.md) تأخیر و IP خروجی، و
  [تأخیر یکسان](sing-box/features/groups/unified-delay.md) که میان پروتکل‌ها قابل مقایسه است.
- **DNS:** [گروه DNS](sing-box/features/dns/dns-group.md)،
  [bypass_if_failed](sing-box/features/dns/dns-bypass-if-failed.md)،
  [DNSCrypt](sing-box/features/dns/sdns.md)، [نام‌های sslip.io](sing-box/features/dns/sslip-hosts.md) و
  [IPv6 بر اساس outbound](sing-box/features/dns/ipv6-by-outbound.md).
- **[رفع باگ‌ها](sing-box/bugfix/v5.md)** روی sing-box 1.15، هر کدام با کامیت خودش.

### در مقایسه با Xray

ترنسپورت‌های XHTTP، mKCP، finalmask، XDRIVE، raw و رمزنگاری VLESS ایکس‌ری در hiddify-core درون خود
sing-box نوشته شده‌اند. پس یک outbound VLESS به سبک ایکس‌ری می‌تواند در یک کانفیگ کنار Hysteria2، TUIC،
وایرگارد، WARP و تونل‌های DNS کار کند، زیر TUN، مسیریابی، rule setها و گروه‌های پروکسی sing-box.
hiddify-core کانفیگ‌های JSON ایکس‌ری و لینک‌های اشتراک‌گذاری ایکس‌ری (از جمله فیلد `extra` در XHTTP) را
می‌خواند، و `HiddifyCli parse --xray` لینک‌ها را به JSON ایکس‌ری تبدیل می‌کند.

### در مقایسه با mihomo

hiddify-core بخش `proxies` کانفیگ YAML کلش یا mihomo را می‌خواند و به sing-box تبدیل می‌کند، پس یک
سابسکریپشن کلش بدون تغییر با `run` کار می‌کند. گروه‌های آن آنچه کاربران mihomo انتظار دارند (انتخاب، URL test،
fallback، تقسیم بار) را پوشش می‌دهند و پایش و failover بالا را هم دارند. کانفیگ‌ها با JSON sing-box نوشته
می‌شوند، نه YAML.

## بیشتر بخوانید

- [راهنمای خط فرمان](cli.md): همه دستورها و گزینه‌های `HiddifyCli`.
- [قابلیت‌های sing-box هیدیفای](sing-box/index.md): یک صفحه برای هر قابلیت، به انگلیسی و فارسی.
- [نکته‌ها برای اپ](sing-box/app_considerations.md): آنچه توسعه‌دهندگان اپ و هسته باید درباره هسته v5 بدانند.
- [استفاده از HiddifyCli در OpenWrt](../app/How-to-use-HiddifyCli-on-OpenWrt.md).
