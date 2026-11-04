---
title: راهنمای خط فرمان
description: همه دستورها و گزینه‌های HiddifyCli، خط فرمان hiddify-core
weight: -10
---

# راهنمای خط فرمان HiddifyCli

`HiddifyCli` (که اسکریپت نصب لینوکس آن را با نام `hiddify-core` نصب می‌کند) خط فرمان
[هسته هیدیفای](index.md) است. این صفحه همه دستورها و گزینه‌ها را فهرست می‌کند. `HiddifyCli help` و
`HiddifyCli <command> --help` همین فهرست را از خود برنامه چاپ می‌کنند.

```text
HiddifyCli [global flags] <command> [flags]
```

## گزینه‌های عمومی

این گزینه‌ها با همه دستورها کار می‌کنند.

| گزینه | پیش‌فرض | معنی |
|---|---|---|
| `-D`، `--directory <dir>` | پوشه فعلی | پوشه کاری. اگر نباشد ساخته می‌شود و مسیرهای نسبی (کانفیگ‌ها، `data/`، `tmp/`) از آن خوانده می‌شوند. |
| `--disable-color` | خاموش | چاپ لاگ‌ها بدون رنگ. |
| `-h`، `--help` | | راهنمای هر دستور. |

## دستورها در یک نگاه

| دستور | کار |
|---|---|
| [`run`](#run) | اجرای لینک‌ها، سابسکریپشن یا پروکسی‌های یک کانفیگ، با کانفیگ کلاینتی که دورشان ساخته می‌شود |
| [`srun`](#srun) | اجرای یک کانفیگ کامل sing-box همان‌طور که هست |
| [`parse`](#parse) | تبدیل لینک‌ها یا هر قالب کانفیگ به outboundهای sing-box (یا JSON ایکس‌ری) |
| [`build`](#build) | ساخت کانفیگ کامل کلاینتی که `run` استفاده می‌کند، بدون اجرای آن |
| [`instance`](#instance) | راه‌اندازی یک نمونه کوچک آزمایشی با پورت SOCKS و پینگ از طریق آن |
| [`health`](#health) | آزمایش DNS، HTTP یا QUIC از طریق یک پروکسی |
| [`speedtest`](#speedtest) | اندازه‌گیری دانلود، آپلود، پینگ و جیتر از طریق یک پروکسی |
| [`warp`](#warp) | ثبت‌نام یک حساب رایگان WARP و چاپ outbound وایرگارد آن |
| [`vlessenc`](#vlessenc) | ساخت جفت کلید رمزنگاری VLESS |
| [`version`](#version) | چاپ نسخه‌ها و جزئیات ساخت |
| [`admin_bgservice`](#admin_bgservice) | مدیریت سرویس پس‌زمینه‌ای که اپ دسکتاپ برای حالت VPN استفاده می‌کند |
| [`grpcweb`](#grpcweb) | یک صفحه وب کوچک برای راه‌اندازی و کنترل هسته از مرورگر |
| [`extension`](#extension) | سرور آزمایشی برای افزونه‌های هیدیفای |
| [`ezytel`](#ezytel) | نمایشگر کانال‌های عمومی تلگرام |
| [`gen-cert`](#gen-cert) | ساخت گواهی TLS برای سرور gRPC هسته |
| [دستورهای توسعه‌دهنده](#developer-commands) | `gen`، `profile`، `command` |
| `completion` | چاپ اسکریپت تکمیل خودکار شل (bash، zsh، fish، powershell) |

## run

```text
HiddifyCli run -c <file or URL> [flags]
```

پروکسی‌ها را از ورودی می‌خواند، یک کانفیگ کامل کلاینت از تنظیمات هیدیفای می‌سازد و آن را تا وقتی
Ctrl+C را بزنید اجرا می‌کند. برای اینکه کی از `run` و کی از `srun` استفاده کنید، ببینید
[اجرای کانفیگ](index.md#run-or-srun).

ورودی می‌تواند این‌ها باشد:

- فایلی از لینک‌های اشتراک‌گذاری (هر خط یک لینک، ساده یا base64) که می‌تواند لینک سابسکریپشن هم داشته باشد؛
- یک لینک سابسکریپشن `http://` یا `https://`. اگر سرور هدر `profile-update-interval` بفرستد (یا متن آن
  خط `#profile-update-interval:` داشته باشد)، سابسکریپشن هر چند ساعت یک بار دوباره گرفته می‌شود و اگر
  تغییر کرده باشد هسته دوباره راه می‌افتد؛
- یک کانفیگ JSON sing-box، فهرستی از outboundها یا یک outbound. فقط `outbounds` و `endpoints` برداشته
  می‌شوند، مگر با `--full-config`؛
- یک کانفیگ YAML کلش یا mihomo، یک کانفیگ JSON ایکس‌ری، یا یک فایل `.conf` وایرگارد.

در زمان اجرا، سرور gRPC هسته روی `127.0.0.1:17078` و Clash API روی `127.0.0.1:16756` گوش می‌دهند
(اگر `allow-connection-from-lan` در فایل تنظیمات روشن باشد، روی `0.0.0.0:16756`).

### گزینه‌های `run`، `build` و `instance` {#run-flags}

| گزینه | پیش‌فرض | معنی |
|---|---|---|
| `-c`، `--config <path or URL>` | الزامی | پروکسی‌ها: یک فایل، یا یک لینک سابسکریپشن (فقط در `run`). |
| `-d`، `--hiddify <file>` | | فایل JSON تنظیمات هیدیفای ([پایین‌تر](#settings-file) را ببینید). اگر داده شود، همه تنظیمات از فایل خوانده می‌شود و گزینه‌های زیر نادیده گرفته می‌شوند. |
| `--full-config` | خاموش | inboundها، DNS و قوانین route ورودی sing-box را هم نگه می‌دارد، کنار آنچه hiddify-core می‌سازد. |
| `--tun` | خاموش | گرفتن همه ترافیک سیستم با TUN (VPN برای کل سیستم). دسترسی root یا administrator لازم است. |
| `--tun-service` | خاموش | استفاده از سرویس پس‌زمینه هیدیفای برای TUN، مثل اپ دسکتاپ. |
| `--system-proxy` | خاموش | تنظیم پروکسی سیستم دسکتاپ روی پروکسی محلی. |
| `--in-proxy-port <port>` | `12334` | پورت پروکسی محلی mixed (HTTP و SOCKS5). |
| `--dns-remote <server>` | `1.1.1.1` | سرور DNS که از طریق پروکسی استفاده می‌شود: `1.1.1.1`، `tcp://…`، `tls://…`، `https://…/dns-query`. |
| `--dns-direct <server>` | `1.1.1.1` | سرور DNS برای اتصال‌های مستقیم. |
| `--fragment` | خاموش | روشن کردن [تکه‌تکه کردن TLS](sing-box/features/tls-fragment.md). |
| `--fragment-size <range>` | `2-4` | اندازه هر تکه به بایت. |
| `--fragment-sleep <range>` | `2-4` | مکث میان تکه‌ها به میلی‌ثانیه. |
| `--padding` | خاموش | افزودن padding به TLS ([ترفندهای TLS](sing-box/features/tls-tricks.md)). |
| `--padding-size <range>` | `1300-1400` | اندازه padding. |
| `--mixed-sni-case` | خاموش | فرستادن نام سرور با حروف بزرگ و کوچک درهم. |
| `--log`، `--log-level <level>` | `warn` | `trace`، `debug`، `info`، `warn`، `error`، `fatal` یا `panic`. |
| `--web-port <port>` | `6756` | پورت Clash API در خروجی `build`. `run` همیشه از `16756` استفاده می‌کند. |
| `--web-secret <secret>` | | رمز Clash API در خروجی `build`. |

نمونه‌ها:

```bash
HiddifyCli run -c links.txt
HiddifyCli run -c https://example.com/sub/abc --in-proxy-port 1080 --log info
sudo HiddifyCli run -c links.txt --tun --dns-remote https://1.1.1.1/dns-query
HiddifyCli run -c links.txt --fragment --fragment-size 10-100 --fragment-sleep 50-200
HiddifyCli run -c sing-box.json --full-config
HiddifyCli -D /var/lib/hiddify-core run -c /etc/hiddify-core/config.json -d settings.json
```

### فایل تنظیمات هیدیفای {#settings-file}

`-d` تنظیمات اپ هیدیفای را به‌صورت JSON می‌گیرد. در اپ، تنظیمات را باز کنید، روی منوی ⋮ بزنید و
خروجی ← «خروجی تمام تنظیمات به فایل» را انتخاب کنید («خروجی تنظیمات ناشناس به فایل» مقدارهای خصوصی را
کنار می‌گذارد). تنظیماتی که در فایل نیستند از پیش‌فرض‌ها پر نمی‌شوند، پس از یک فایل خروجی گرفته‌شده
شروع کنید. کلیدهای اصلی:

| کلید | معنی |
|---|---|
| `log-level` | سطح لاگ. |
| `enable-full-config` | مانند `--full-config`. |
| `mixed-port`، `tproxy-port`، `redirect-port`، `direct-port` | پورت‌های محلی؛ `enable-mixed-port` و مانند آن هر کدام را روشن یا خاموش می‌کنند. |
| `enable-tun`، `enable-tun-service`، `set-system-proxy` | VPN و پروکسی سیستم، مانند گزینه‌ها. |
| `tun-implementation`، `mtu`، `strict-route`، `auto-redirect` | پشته و گزینه‌های TUN. |
| `allow-connection-from-lan`، `lan-sharing-port`، `lan-sharing-password` | اشتراک اتصال با شبکه محلی. |
| `remote-dns-address`، `direct-dns-address`، `remote-dns-domain-strategy`، `direct-dns-domain-strategy`، `enable-fake-dns`، `independent-dns-cache` | DNS. |
| `ipv6-mode`، `bypass-lan`، `block-quic`، `resolve-destination`، `region`، `block-ads`، `route-rule` | مسیریابی. |
| `connection-test-url`، `connection-test-urls`، `url-test-interval`، `ipinfo-url` | تست پروکسی‌ها. |
| `balancer-strategy`، `default-proxy`، `keep-top`، `keep-tags` | کدام پروکسی استفاده شود و چندتا اجرا شوند. |
| `tls-tricks` | `enable-fragment`، `fragment-size`، `fragment-sleep`، `mixed-sni-case`، `enable-padding`، `padding-size`. |
| `mux` | `enable`، `padding`، `max-streams`، `protocol`. |
| `warp`، `warp2` | تنظیمات WARP. |
| `extra-security`، `unblocker`، `chain-status` | زنجیر کردن پروکسی از طریق WARP، سایفون یا پروفایلی دیگر. |
| `enable-clash-api`، `clash-api-port`، `web-secret` | Clash API. |

## srun

```text
HiddifyCli srun -c <file> [-c <file>…] [-C <folder>…]
```

یک کانفیگ کامل sing-box را بدون تغییر اجرا می‌کند، مثل `sing-box run`. همه افزوده‌های هیدیفای به
sing-box در دسترس‌اند ([قابلیت‌ها](sing-box/index.md)).

| گزینه | معنی |
|---|---|
| `-c`، `--config <path>` | یک فایل کانفیگ. برای ادغام چند فایل آن را تکرار کنید؛ به ترتیب مسیرشان ادغام می‌شوند. `stdin` کانفیگ را از ورودی استاندارد می‌خواند. |
| `-C`، `--config-directory <dir>` | خواندن همه فایل‌های `.json` یک پوشه. قابل تکرار است. |

سیگنال‌ها: `SIGHUP` کانفیگ را بررسی و بدون توقف دوباره بارگذاری می‌کند (کانفیگ خراب گزارش می‌شود و
کانفیگ در حال اجرا می‌ماند)؛ `SIGINT` و `SIGTERM` آن را متوقف می‌کنند.

```bash
HiddifyCli srun -c config.json
HiddifyCli srun -c base.json -c outbounds.json
HiddifyCli srun -C /etc/hiddify-core/conf.d
HiddifyCli -D /var/lib/hiddify-core srun -c /etc/hiddify-core/server.json
```

## parse

```text
HiddifyCli parse <file> [-o <file>] [--xray]
```

فایلی در هر قالبی که `run` می‌فهمد را می‌خواند، پروکسی‌ها را به‌صورت JSON sing-box (`outbounds` و
`endpoints`) چاپ می‌کند و نتیجه را بررسی می‌کند. لینک‌های سابسکریپشن داخل فایل گرفته می‌شوند. برای دیدن
اینکه یک لینک چطور خوانده می‌شود، یا به‌عنوان قدم اول یک کانفیگ دست‌ساز، از آن استفاده کنید.

| گزینه | معنی |
|---|---|
| `-o`، `--output <file>` | نوشتن نتیجه در فایل (نسبت به `-D`) به‌جای صفحه. |
| `--xray` | تبدیل لینک‌ها به JSON ایکس‌ری، با libxray. |

```bash
HiddifyCli parse links.txt
HiddifyCli parse clash.yaml -o outbounds.json
HiddifyCli parse links.txt --xray -o xray.json
```

## build

```text
HiddifyCli build -c <sing-box json> [-d <settings>] [flags] [-o <file>]
```

کانفیگ کامل کلاینت، همان که `run` اجرا می‌کند، را از outboundهای sing-box و تنظیمات هیدیفای می‌سازد و
چاپ می‌کند. ورودی باید JSON sing-box باشد؛ قالب‌های دیگر را اول با `parse` تبدیل کنید.
[گزینه‌های `run`](#run-flags) را می‌پذیرد و همچنین:

| گزینه | معنی |
|---|---|
| `-o`، `--output <file>` | نوشتن نتیجه در فایل (نسبت به `-D`) به‌جای صفحه. |

```bash
HiddifyCli parse links.txt -o outbounds.json
HiddifyCli build -c outbounds.json --tun -o config.json
HiddifyCli srun -c config.json
```

## instance

```text
HiddifyCli instance -c <file> [flags]
```

یک نمونه کوچک از پروکسی‌های داده‌شده با یک پورت SOCKS5 راه می‌اندازد، چند بار از طریق آن به کلادفلر
پینگ می‌زند، آدرس SOCKS را چاپ می‌کند و منتظر Ctrl+C می‌ماند. برای آزمایش سریع یک کانفیگ مفید است.
[گزینه‌های `run`](#run-flags) را می‌پذیرد.

## health

```text
HiddifyCli health [target] [flags]
```

اتصال به یک مقصد (پیش‌فرض `google.com`) را مستقیم یا از طریق یک پروکسی SOCKS بررسی می‌کند. اگر هیچ‌کدام
از `--dns`، `--http` و `--quic` داده نشود، HTTP آزمایش می‌شود.

| گزینه | پیش‌فرض | معنی |
|---|---|---|
| `--proxy <url>` | مستقیم | پروکسی برای آزمایش: `socks://[user:pass@]host:port`. |
| `--dns` | خاموش | گرفتن IP مقصد از DNS. |
| `--http` | خاموش | گرفتن مقصد با HTTP روی TCP. |
| `--quic` | خاموش | باز کردن یک اتصال QUIC روی UDP. |
| `--dns-server <addr>` | `1.1.1.1:53` | سرور DNS: `host:port`، `udp://host:port` یا `tcp://host:port`. |
| `--timeout <duration>` | `15s` | محدودیت زمان هر بررسی. |
| `-v`، `--verbose` | | لاگ‌های اشکال‌زدایی؛ `-vv` برای جزئیات بیشتر. |

```bash
HiddifyCli health --proxy socks://127.0.0.1:12334 --dns --http --quic cloudflare.com
```

## speedtest

```text
HiddifyCli speedtest [flags]
```

یک تست speedtest.net را مستقیم یا از طریق یک پروکسی SOCKS اجرا می‌کند.

| گزینه | پیش‌فرض | معنی |
|---|---|---|
| `--proxy <url>` | مستقیم | `socks://[user:pass@]host:port` یا فقط `host:port`. |
| `--distance <km>` | `2000` | فاصله سرور تستی که انتخاب می‌شود. |
| `--no-download` | خاموش | رد کردن تست دانلود. |
| `--no-upload` | خاموش | رد کردن تست آپلود. |
| `--no-ping` | خاموش | رد کردن تست پینگ (و جیتر). |
| `--no-jitter` | خاموش | چاپ نکردن جیتر. |
| `-v`، `--verbose` | | لاگ‌های اشکال‌زدایی؛ `-vv` برای جزئیات بیشتر. |

```bash
HiddifyCli speedtest --proxy 127.0.0.1:12334
```

## warp

```text
HiddifyCli warp
```

یک حساب رایگان جدید WARP کلادفلر ثبت می‌کند و یک outbound وایرگارد sing-box برای آن چاپ می‌کند. روش
هیدیفای برای استفاده از WARP در کانفیگ، [اندپوینت `warp`](sing-box/features/protocols/warp.md) است که
خودش ثبت‌نام می‌کند.

## vlessenc

```text
HiddifyCli vlessenc [--json]
```

یک جفت کلید تازه برای [رمزنگاری VLESS](sing-box/features/protocols/vless-encryption.md)
(`mlkem768x25519plus`) می‌سازد: مقدار `decryption` برای سرور و مقدار `encryption` برای کلاینت. `--json`
آن‌ها را به‌صورت JSON چاپ می‌کند.

## version

```text
HiddifyCli version [-n]
```

نسخه hiddify-core و hiddify-sing-box، نسخه Go، سیستم، تگ‌های ساخت، کامیت و روشن بودن CGO را چاپ
می‌کند. `-n`، `--name` فقط نام نسخه sing-box را چاپ می‌کند.

## admin_bgservice

```text
HiddifyCli admin_bgservice <action> [argument]
```

نام دیگر آن `tunnel` است. اپ دسکتاپ (ویندوز، مک، لینوکس) حالت VPN را از طریق یک سرویس پس‌زمینه با
دسترسی مدیر اجرا می‌کند و این دستور آن را مدیریت می‌کند. برای اجرای کانفیگ توسط خودتان لازمش ندارید.

| کار | معنی |
|---|---|
| `install [owner]` | نصب سرویس. در لینوکس می‌توان کاربر صاحب آن را داد. |
| `uninstall` | حذف سرویس. |
| `start`، `stop` | راه‌اندازی یا توقف سرویس. |
| `run` | اجرای سرویس در پیش‌زمینه. |
| `activate`، `deactivate` | روشن کردن VPN سرویس (با IPv6 و پورت mixed ‏12334) یا خاموش کردن اجباری آن. |
| `connect <request.json>` | درخواست اتصال از سرویس با یک فایل درخواست. |
| `disconnect` | درخواست قطع اتصال از سرویس. |
| `exit` | درخواست خروج از سرویس. |
| `build-id` | چاپ شناسه ساخت، که اپ با سرویس در حال اجرا مقایسه می‌کند. |

## grpcweb

```text
HiddifyCli grpcweb [flags]
```

یک هسته راه می‌اندازد و یک صفحه HTML کوچک و API gRPC هسته را روی یک پورت ارائه می‌کند، تا از مرورگر
هسته را روشن و خاموش کنید و پروکسی انتخاب کنید. `http://127.0.0.1:18088` را باز کنید.

| گزینه | پیش‌فرض | معنی |
|---|---|---|
| `--listen <addr>` | `0.0.0.0:18088` | آدرس صفحه و API gRPC. |
| `--workdir <dir>` | یک پوشه موقت | پوشه کاری هسته. |
| `--config <path>` | | مسیر کانفیگی که در صفحه نشان داده می‌شود. |
| `--mixed-port <port>` | `12334` | پورت پروکسی محلی هسته‌ای که راه می‌اندازد. |
| `--connect` | خاموش | هسته‌ای راه نمی‌اندازد؛ هسته روی `--grpc` را کنترل می‌کند. |
| `--grpc <addr>` | | آدرس gRPC هسته‌ای که کنترل می‌شود، همراه `--connect`. |

## extension

```text
HiddifyCli extension
```

یک سرور آزمایشی برای [افزونه‌های هیدیفای](https://github.com/hiddify/hiddify-app-example-extension) راه
می‌اندازد تا رابط افزونه را در مرورگر روی `https://127.0.0.1:12346` امتحان کنید.

## ezytel

```text
HiddifyCli ezytel <command> [flags]
```

کانال‌های عمومی تلگرام را از طریق پیش‌نمایش وب آن‌ها می‌خواند، مانند نمایشگر کانال اپ.

| دستور | گزینه‌ها | معنی |
|---|---|---|
| `info` | `--channel <id>`، `--last-read <post id>`، `--disable-inline-images`، `--json` | جزئیات کانال، با تعداد نخوانده‌ها پس از `--last-read`. |
| `messages` | `--channel <id>`، `--before <post id>`، `--disable-inline-images`، `--html-only`، `--json` | پیام‌های کانال به‌صورت HTML، صفحه به صفحه. |
| `proxy-image` | `--hex <url>`، `-o <file>`، `--json` | دانلود تصویر یک پست. |
| `parse-channels` | `--raw <text>`، `-f <file>`، `--json` | خواندن فهرستی از کانال‌ها، هر خط یکی. |
| `serve` | `--listen <addr>` (پیش‌فرض `127.0.0.1:17079`) | اجرای سرور gRPC نمایشگر. |

همه آن‌ها `--cache-dir <dir>` را می‌پذیرند (پیش‌فرض: پوشه‌ای در پوشه موقت سیستم).

```bash
HiddifyCli ezytel messages --channel hiddify --html-only
```

## gen-cert

```text
HiddifyCli gen-cert
```

یک گواهی سرور و یک گواهی کلاینت برای سرور gRPC هسته در `data/cert/` می‌سازد (`server-cert.pem`،
`server-key.pem`، `client-cert.pem`، `client-key.pem`).

## دستورهای توسعه‌دهنده {#developer-commands}

این دستورها برای توسعه hiddify-core هستند و ممکن است تغییر کنند:

- `gen <file>`: ساخت کانفیگ به روش اپ و نوشتن آن در لاگ با سطح debug.
- `profile <url>`: افزودن یک پروفایل از URL، مانند اپ، و چاپ نتیجه.
- `command`: اتصال به API gRPC هسته در حال اجرا (`127.0.0.1:17078`) و چاپ وضعیت، outboundها و لاگ‌های آن.
