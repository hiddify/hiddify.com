---
title: لینک‌ها و فرمت سابسکریپشن اپ هیدیفای
---

# لینک‌ها و فرمت سابسکریپشن اپ هیدیفای

این صفحه برای کسانی است که برای اپ هیدیفای لینک سابسکریپشن، پنل یا بات می‌سازند: لینک‌هایی که اپ را باز می‌کنند، این‌که یک سابسکریپشن چه چیزهایی می‌تواند داشته باشد، و هدرها و پارامترهای لینک که اپ می‌خواند.

!!! info "نوشته‌شده برای اپ هیدیفای ۵.۹"
    همهٔ مطالب این صفحه با کد اپ هیدیفای نسخهٔ ۵.۹.۲ و هستهٔ هیدیفای همراه آن بررسی شده‌اند.

## لینک‌هایی که اپ را باز می‌کنند { #download-configuration }

اگر اپ هیدیفای نصب باشد، لینکی به این شکل اپ را باز می‌کند و از کاربر می‌پرسد که پروفایل را اضافه کند یا نه:

```
hiddify://import/<link>#<name>
```

- `<link>` یک لینک سابسکریپشن است (با هر فرمتی که اپ می‌خواند، [پایین‌تر](#subscription-content) را ببینید) یا یک لینک پروکسی تکی مثل `vless://…`.
- `#<name>` (اختیاری) نام پروفایل است. اپ قبل از افزودن پروفایل از یک لینک بیرونی، از کاربر تأیید می‌گیرد.

نمونه:

```
hiddify://import/https://example.com/sub/abc123#My VPN
hiddify://import/trojan://password@example.com:443?security=tls&type=ws&path=%2Fws#Server 1
```

### شکل‌های دیگری که اپ می‌فهمد { #deprecated }

این شکل‌ها وقتی خوانده می‌شوند که کاربر آن‌ها را در خود اپ اضافه کند (از کلیپ‌بورد یا با **افزودن پروفایل › دستی**). برای لینکی که اپ را باز کند، از همان `hiddify://import/…` بالا استفاده کنید.

```
hiddify://install-sub?url=<URL-encoded link>#<name>
hiddify://install-config?url=<URL-encoded link>#<name>
hiddify://install-proxy?url=<URL-encoded link>#<name>
v2ray://install-config?url=<URL-encoded link>&name=<name>
clash://install-config?url=<URL-encoded link>&name=<name>
sing-box://import-remote-profile?url=<URL-encoded link>#<name>
```

اسکیم‌های `hiddify`، `v2ray`، `v2rayn`، `v2rayng`، `clash`، `clashmeta` و `sing-box` همه با پارامتر `url=` کار می‌کنند. اگر پارامتر `name=` داده شود، به جای بخش `#name` استفاده می‌شود. یک لینک ساده‌ی `https://…` هم می‌تواند `?name=…` داشته باشد.

### اشتراک‌گذاری قانون‌های مسیریابی { #routing-rules }

در **تنظیمات › مسیریابی**، منوی ⋮ گزینه‌ی **کپی قوانین در کلیپ‌بورد** را دارد که لینکی به این شکل کپی می‌کند:

```
hiddify:///settings/routing-options?routeRule=<base64 of the rules as JSON>
```

باز کردن این لینک روی دستگاه دیگر، صفحه‌ی **مسیریابی** را باز می‌کند و بعد از یک هشدار، قانون‌ها را اضافه می‌کند.

## یک سابسکریپشن چه چیزهایی می‌تواند داشته باشد { #subscription-content }

محتوای یک لینک سابسکریپشن (یا فایلی که کاربر وارد می‌کند) می‌تواند این‌ها باشد:

- **لینک‌های اشتراک‌گذاری**، هر کدام در یک خط، ساده یا همه با هم به شکل base64. هسته این‌ها را می‌خواند: `vless`، `vmess`، `trojan`، `ss`، `ssconf`، `tuic`، `hysteria`، `hysteria2` (`hy2`)، `ssh`، `naive` (`naive+https`، `naive+quic`)، `anytls`، `snell`، `mieru` (`mierus`)، `socks`، `http`/`https` (و `phttp`/`phttps`)، `wg`/`wireguard`/`awg`، `warp`، `psiphon`، `tor`، `ovpn`، `dnstt`، `dnst`، `masterdns`، `soar`، `slipnet`، `masque`، `aether` و `direct`. پیشوند `x` (`xvless://`، `xvmess://`، `xtrojan://`) لینک را با هسته‌ی Xray اجرا می‌کند و پیشوند `s` (`svless://` و …) با sing-box.
- **کانفیگ JSON سینگ‌باکس**، **کانفیگ YAML کلش / mihomo**، **کانفیگ JSON ایکس‌ری**، فایل **`.conf` وایرگارد** یا فایل **`.ovpn` اوپن‌وی‌پی‌ان**.
- **لینک‌های سابسکریپشن دیگر:** خطی که یک آدرس `http(s)://` با مسیر باشد دانلود می‌شود و محتوایش جای آن خط را می‌گیرد. خطی که دانلود نشود حذف می‌شود.

نمونه‌ی لینک‌های اشتراک‌گذاری:

```
#profile-title: My VPN
vless://11111111-2222-3333-4444-555555555555@example.com:443?security=tls&sni=example.com&type=ws&path=%2Fws#WebSocket TLS
hysteria2://password@example.com:443?sni=example.com&obfs=salamander&obfs-password=secret#Hysteria2
tuic://11111111-2222-3333-4444-555555555555:password@example.com:443?alpn=h3&congestion_control=bbr&sni=example.com#TUIC
```

## نام پروفایل { #profile-title }

اپ اولین مورد غیرخالی از این فهرست را استفاده می‌کند:

1. نامی که کاربر هنگام ویرایش پروفایل نوشته است.
2. هدر `profile-title`.
3. نام فایل در هدر `content-disposition`.
4. بخش `#name` لینک سابسکریپشن.
5. آخرین بخش لینک، بدون `.json`، `.yaml`، `.yml` یا `.txt`.
6. «Remote Profile».

## هدرهای سابسکریپشن { #response-headers }

سرور می‌تواند این هدرهای HTTP را همراه سابسکریپشن بفرستد. اگر نمی‌توانید هدر بگذارید (مثلاً فایلی روی گیت‌هاب)، آن‌ها را به شکل کامنت در **۱۰ خط اول** محتوا بنویسید، با `#` یا `//` در ابتدای خط:

```
#profile-title: base64:SSDinaTvuI8gSGlkZGlmeQ==
#profile-update-interval: 12
#subscription-userinfo: upload=455727941; download=6174315083; total=1073741824000; expire=1767225600
#support-url: https://t.me/hiddify
#profile-web-page-url: https://hiddify.com
```

اگر یک هدر هم به شکل هدر واقعی HTTP و هم داخل محتوا باشد، هدر HTTP اولویت دارد. اپ فقط این هدرها را می‌خواند:

| هدر | مقدار | کاری که اپ می‌کند |
|---|---|---|
| `profile-title` | متن، یا `base64:` و بعد متن UTF-8 به شکل base64 | نام پروفایل. برای ایموجی یا نام فارسی از base64 استفاده کنید: `base64:SSDinaTvuI8gSGlkZGlmeQ==` نام «I ❤️ Hiddify» را نشان می‌دهد. |
| `content-disposition` | `attachment; filename="name.txt"` یا `filename*=UTF-8''<percent-encoded>` | نام پروفایل، وقتی `profile-title` نباشد. |
| `profile-update-interval` | ساعت، یک عدد صحیح بزرگ‌تر از صفر | هر چند ساعت یک بار اپ پروفایل را به‌روز کند، مگر این‌که کاربر خودش آن را عوض کرده باشد. |
| `subscription-userinfo` | `upload=…; download=…; total=…; expire=…` | حجم مصرف‌شده و کل (به بایت) و روزهای باقی‌مانده را نشان می‌دهد (`expire` زمان یونیکس به ثانیه است). `total=0` یا نبود `total` یعنی نامحدود؛ `expire=0` یا نبود `expire` یعنی بدون تاریخ انقضا. |
| `profile-web-page-url` | یک آدرس | دکمه‌ای نشان می‌دهد که صفحه‌ی وب شما (مثلاً صفحه‌ی کاربر) را باز می‌کند. |
| `support-url` | یک آدرس | دکمه‌ی پشتیبانی نشان می‌دهد. |
| `ipinfo-url` | یک آدرس | آدرسی که اپ برای نشان دادن آی‌پی خروجی و کشور آن استفاده می‌کند. |
| `extra-security` | `psiphon` یا `warp` | [امنیت بیشتر](Chain-Extra-security-and-Proxy-unblocker.md) را برای این پروفایل با سایفون یا وارپ روشن می‌کند. انتخاب خود کاربر در اپ اولویت دارد. |
| `fragment` | `size,sleep,method` یا `tlshello,size,sleep` | فرگمنت TLS را برای این پروفایل روشن می‌کند و مثل پارامتر لینک [پایین](#fragment-parameters) خوانده می‌شود. تنظیم خود کاربر اولویت دارد. |
| `keep-top` | یک عدد، یا `-1` | چند تا از سریع‌ترین پروکسی‌ها روشن بمانند (پیش‌فرض ۵). `-1` یعنی همه. انتخاب خود کاربر اولویت دارد. |

!!! note "دیگر خوانده نمی‌شوند"
    هدرهای `moved-permanently-to` و `DNS` را نسخه‌های قدیمی می‌خواندند. اپ هیدیفای ۵.۹ آن‌ها را نادیده می‌گیرد.

## پارامترهای لینک { #link-parameters }

هیدیفای علاوه بر پارامترهای معمول هر پروتکل، این‌ها را هم در لینک می‌خواند. بزرگی و کوچکی حروف، `_` و `-` در نام پارامتر مهم نیست: `mux_type`، `mux-type` و `muxtype` یکی هستند.

### فرگمنت TLS { #fragment-parameters }

```
&fragment=<size>,<sleep>,<method>
&fragment=tlshello,<size>,<sleep>
```

`size` اندازه‌ی هر تکه به بایت و `sleep` مکث بین تکه‌ها به میلی‌ثانیه است، هر کدام یک عدد یا بازه‌ای مثل `10-100`. هر سه بخش لازم است. نمونه: `&fragment=10-100,100-200,tlshello`. می‌توانید `fgsize=` و `fgsleep=` را هم جداگانه بدهید. [کاربرد و نحوه‌ی عملکرد ترفند TLS](/fa/manager/basic-concepts-and-troubleshooting/How-the-TLS-Trick-works-and-its-usage/) را ببینید.

### ترفندهای دیگر TLS { #tls-tricks-parameters }

- `mc=1`: SNI با حروف بزرگ و کوچک درهم (مثلاً `ExAmPle.com`).
- `padsize=<range>`: یک بخش پدینگ به این اندازه (بایت) قبل از SNI اضافه می‌کند، مثلاً `padsize=100-200`. به اثر انگشت مرورگر (`fp=chrome` یا مشابه) نیاز دارد.

### MUX { #mux-parameter }

| پارامتر | معنی |
|---|---|
| `muxtype` | `smux`، `yamux` یا `h2mux`. MUX فقط وقتی روشن است که این پارامتر داده شود. |
| `muxmaxc` | بیشترین تعداد اتصال |
| `muxsmax` | بیشترین تعداد استریم در هر اتصال |
| `mux` | کمترین تعداد استریم در هر اتصال |
| `muxpad` | `true` برای افزودن پدینگ (سرور هم باید آن را داشته باشد) |
| `muxup`، `muxdown` | سرعت آپلود و دانلود به Mbps برای TCP Brutal؛ هر دو لازم‌اند |

نمونه: `&muxtype=h2mux&muxmaxc=4&muxpad=false&muxup=10&muxdown=50`

!!! warning "نام‌های قدیمی پارامترها"
    نسخه‌های قبلی این صفحه `mux=smux`، `mux_max`، `mux_min`، `mux_up` و `mux_down` را نوشته بودند. اپ این نام‌ها را نمی‌خواند: از جدول بالا استفاده کنید.

## مقاله‌های مرتبط

- [ورود، خروج و بازنشانی تنظیمات و ویرایش پروفایل در اپ هیدیفای](/fa/app/Import-export-settings-and-edit-profile/)
- [آموزش کار با اپ هیدیفای](/fa/app/How-to-use-Hiddify-app/)
- [پروفایل‌های رایگان اپ هیدیفای](/fa/app/Free-profiles-in-Hiddify-app/)
