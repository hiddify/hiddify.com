---
title: قابلیت‌ها
weight: 10
---

# قابلیت‌های هسته

قابلیت‌ها و رفع اشکال‌هایی در فورک هیدیفای که sing-box اصلی ندارد. هر صفحهٔ قابلیت یک نسخهٔ
انگلیسی و یک نسخهٔ فارسی دارد.

## قابلیت‌ها

- [تکه‌تکه کردن TLS](tls-fragment.md): ClientHello را با مکث به تکه‌های کوچک تقسیم می‌کند تا DPI نتواند نام سرور را بخواند.
- [ترفندهای TLS](tls-tricks.md): نام سرور با حروف بزرگ و کوچک درهم و یک افزونهٔ padding در ClientHello.
- [REALITY در هیدیفای](reality-hiddify.md): key share پساکوانتومی، گزینهٔ `key_share` و تکه‌تکه کردن روی REALITY.
- [پروتکل PROXY](proxy-protocol.md): ورودی‌ها هدر PROXY protocol را می‌خوانند و خروجی direct آن را می‌فرستد.

## پروتکل‌ها

- [WARP](protocols/warp.md): WARP کلادفلر روی WireGuard، AmneziaWG یا MASQUE، با ثبت حساب رایگان، بسته‌های نویز و اسکنری که برای هر شبکه جدا به نشانی دیگری می‌رود.
- [اسکنر و noise در WARP](protocols/warp-scanner.md): اسکنر endpoint، حالت‌ها و پیش‌تنظیم‌های noise (DNS، QUIC، SIP، تصادفی)، جست‌وجوی noise و حالت auto چطور راهی برای عبور پیدا می‌کنند.
- [WARP روی MASQUE](protocols/warp-masque.md): outbound مستقل `masque` برای WARP روی HTTP/3، HTTP/2 یا هر دو، با دستگاهی که جای دیگری ثبت شده؛ برای ثبت دستگاه، endpoint ‏`warp` با `mode` برابر `masque` را به کار ببرید؛ برای سرور MASQUE شخصی، از `masque-client` در sing-box اصلی استفاده کنید.
- [AmneziaWG](protocols/amneziawg.md): WireGuard با بسته‌های بی‌معنی، handshakeهای padding‌دار و نوع پیام‌های دلخواه که شناسایی WireGuard را خنثی می‌کنند.
- [WireGuard: افزوده‌های هیدیفای](protocols/wireguard-hiddify.md): بسته‌های نویز پیش از handshake، نام کاربر برای هر peer، بازیابی سوکت و تکه‌تکه کردن UDP که به‌طور پیش‌فرض روشن است.
- [خروجی WireGuard (قالب قدیمی)](protocols/wireguard-legacy.md): خروجی قدیمی WireGuard که sing-box اصلی حذفش کرد، نگه داشته شده تا کانفیگ‌های قدیمی هنوز بارگذاری شوند.
- [رمزگذاری VLESS](protocols/vless-encryption.md): رمزگذاری پساکوانتومی VLESS از Xray، با Vision روی آن حتی بدون TLS.
- [Sudoku](protocols/sudoku.md): یک پراکسی رمزشدهٔ TCP که بایت‌هایش را به شکل سرنخ‌های سودوکو می‌فرستد تا ترافیک شبیه متن باشد یا تصادفی بودن کمی داشته باشد، با تونل‌های HTTP اختیاری (build tag `with_sudoku`).
- [Mieru](protocols/mieru.md): یک پراکسی کاملاً رمزشده و padding‌دار روی بازه‌های پورت TCP یا UDP، بدون هیچ الگوی ثابت.
- [TrustTunnel](protocols/trusttunnel.md): ترافیک پراکسی به شکل جریان‌های HTTP CONNECT روی HTTP/2 یا HTTP/3.
- [SSH](protocols/ssh.md): یک ورودی سرور SSH برای port forwarding، به‌علاوهٔ UDP روی TCP و اتصال پس‌زمینه برای خروجی SSH.
- [سایفون](protocols/psiphon.md): بدون سرور شخصی از راه شبکهٔ سایفون وصل شوید و کشور خروجی را انتخاب کنید.
- [DNSTT](protocols/dnstt.md): ترافیک را درون پرس‌وجوهای DNS از راه resolverهای عمومی می‌برد و خودش آن‌ها را پیدا می‌کند.
- [MasterDNS](protocols/masterdns.md): تونل MasterDnsVPN از راه resolverهای عمومی، با سربار کم، تکرار بسته‌ها روی چند resolver و آزمایش MTU؛ سرور خودش به مقصد وصل می‌شود.
- [Soar](protocols/soar.md): تونل DNS پروژهٔ Lantern، هر resolver یک مسیر جدا با بازیابی سریع از دست رفتن بسته‌ها و کشف resolver، به‌طور پیش‌فرض از راه مجموعهٔ هوشمند؛ لینک‌های `soar://`.
- [GooseRelay](protocols/gooserelay.md): ترافیک را از راه Google Apps Script به سرور خودتان می‌فرستد، پس شبکه فقط HTTPS به گوگل می‌بیند.
- [تونل تماس](protocols/call.md): ترافیک پراکسی را درون یک تماس تصویری در VK، Telemost، Dion، WB Stream یا Bitrix24 می‌برد تا شبیه تماس با یک سرویس داخلی مجاز باشد؛ به‌طور کامل تست نشده است (build tag `with_call`).
- [Tunnel](protocols/tunnel.md): یک تونل معکوس که از راه یک سرور عمومی به دستگاه‌های پشت NAT می‌رسد.
- [Bond](protocols/bond.md): هر اتصال را هم‌زمان روی چند خروجی تقسیم می‌کند و در سرور به هم وصل می‌کند تا سرعت اتصال‌های محدودشده جمع شود (build tag `with_bond`).

## ترنسپورت‌ها

- [XHTTP](transports/xhttp.md): ترنسپورت XHTTP از Xray با حالت‌ها، padding، جایگاه‌ها، XMUX و دانلود جداگانه.
- [mKCP](transports/kcp.md): mKCP نسخهٔ Xray 26 روی UDP برای شبکه‌های پرافت یا شبکه‌هایی که TCP را کند می‌کنند، پنهان‌شده با ماسک‌های UDP در finalmask (build tag `with_kcp`).
- [XDRIVE](transports/xdrive.md): ترنسپورت ذخیره‌سازی Xray؛ اتصال VLESS در فایل‌هایی روی Google Drive، S3 یا سرویس ذخیره‌سازی دیگر حمل می‌شود و کلاینت هرگز به سرور وصل نمی‌شود (build tag `with_xdrive`).
- [ترنسپورت raw](transports/raw.md): ترنسپورت `raw`، تا کانفیگ‌هایی که از Xray تبدیل شده‌اند بارگذاری شوند.
- [مسیرهای دلخواه gRPC](transports/grpc-custom-path.md): مسیرهای چندبخشی gRPC به سبک Xray در `service_name`.
- [finalmask](transports/finalmask.md): ماسک‌های finalmask از Xray (fragment، noise، header-custom، xdns روی UDP، TCP یا DoH، udphop، merge، oob و موارد دیگر) روی هر اتصالی که یک خروجی برقرار می‌کند.
- [سرور simple-obfs در Shadowsocks](transports/shadowsocks-obfs.md): یک سرور simple-obfs روی ورودی‌های Shadowsocks، با یک مقصد فریب وقتی obfs یا ورود شکست بخورد.
- [rmux](transports/rmux.md): یک پروتکل چندگانه‌سازی دیگر برای بردن چند اتصال در یک اتصال، در کنار smux، yamux و h2mux.

## DNS

- [گروه DNS](dns/dns-group.md): از چند سرور DNS هم‌زمان یا به نوبت بپرسید، یا روی سروری که کار می‌کند بمانید، و پاسخ‌های مسموم را کنار بگذارید.
- [IPv6 بر اساس خروجی](dns/ipv6-by-outbound.md): IPv6 فقط از خروجی‌هایی که معلوم است آن را رد می‌کنند، بررسی‌شده در تست URL و آموخته از اتصال‌ها؛ اتصالی که خروجی نتواند رد کند درون همان اتصال با IPv4 برده می‌شود تا هیچ برنامه‌ای مرگش را نبیند.
- [قاعده‌های DNS: bypass_if_failed](dns/dns-bypass-if-failed.md): وقتی سرور یک قاعدهٔ DNS شکست می‌خورد، پرس‌وجو به قاعدهٔ منطبق بعدی می‌رود.
- [مجموعهٔ هوشمند resolver](dns/smart-dns-pool.md): مجموعهٔ resolverی که هر خروجی تونل DNS با `smart_pool` برای خودش راه می‌اندازد، مشترک میان DNSTT، MasterDNS و Soar، با resolverهای `auto`، امتیازهای ذخیره‌شده و DoT/DoH.
- [DNSCrypt (استمپ‌های SDNS)](dns/sdns.md): سرور `sdns` که پرس‌وجوهای رمزشده را به یک resolver از نوع DNSCrypt می‌فرستد که با استمپش مشخص شده است.
- [نام‌های sslip.io](dns/sslip-hosts.md): سرور `hosts` به نام‌های `sslip.io` با نشانی‌ای که در خود نام نوشته شده پاسخ می‌دهد.

## گروه‌ها و پایش

- [متعادل‌کننده](groups/balancer.md): اتصال‌ها را با round robin، کمترین تأخیر، consistent hashing، ‏sticky session یا یک مخزن چسبنده (pool) میان اعضا پخش می‌کند.
- [جایگزین](groups/fallback.md): اعضا را به ترتیب امتحان می‌کند و عضوی را که شکست خورده تا مدتی کنار می‌گذارد.
- [تست URL: افزوده‌های هیدیفای](groups/urltest.md): نشانی‌های تست بیشتر، حالت `failover` و رفتن به عضو دیگر با اولین اتصال ناموفق.
- [پایش](groups/monitoring.md): تست پس‌زمینهٔ همهٔ خروجی‌ها برای تأخیر و IP خروجی، که نتیجه‌اش به گروه‌ها داده می‌شود.
- [خروجی‌های تنبل و keep top](groups/keep-top.md): خروجی‌هایی که با اولین استفاده ساخته و در بی‌کاری بسته می‌شوند، و فقط سریع‌ترین چندتای آن‌ها در استفاده، که چندتا چندتا پیدا می‌شوند، تا پروفایلی با صدها پروکسی در حافظهٔ گوشی جا شود.
- [تأخیر یکسان](groups/unified-delay.md): تست‌های URL زمان یک رفت‌وبرگشت HTTP را روی اتصال باز می‌سنجند، تا تأخیرها میان پروتکل‌ها قابل مقایسه باشند.

## برای توسعه‌دهندگان اپ

- [ملاحظات اپ](../app_considerations.md) (انگلیسی): آنچه hiddify-app و hiddify-core به‌خاطر کارهای v5 باید تغییر دهند یا بدانند.

## قدردانی

قابلیت‌های هیدیفای بر پایهٔ این پروژه‌ها ساخته شده‌اند. صفحهٔ هر قابلیت، در بخش «منبع‌ها و قدردانی»، می‌گوید چه چیزی از آن‌ها گرفته است. از نویسندگان آن‌ها سپاسگزاریم.

- [SagerNet/sing-box](https://github.com/SagerNet/sing-box): پروژهٔ اصلی که این فورک بر پایهٔ آن ساخته شده است.
- [shtorm-7/sing-box-extended](https://github.com/shtorm-7/sing-box-extended): تونل تماس، bond، fallback، Sudoku و rmux.
- [Leadaxe/sing-box-lx](https://github.com/Leadaxe/sing-box-lx): افزوده‌های URL test، `key_share` در REALITY، جابه‌جایی MASQUE و حالت‌های DNS group.
- [reF1nd/sing-box](https://github.com/reF1nd/sing-box): DNS group، بازیابی WireGuard و رفع اشکال‌های دیگر.
- [kyochikuto/sing-box-plus](https://github.com/kyochikuto/sing-box-plus): probe مربوط به WireGuard در اسکنر WARP.
- [XTLS/Xray-core](https://github.com/XTLS/Xray-core): XHTTP، mKCP، XDRIVE، finalmask و رمزنگاری VLESS.
- [patterniha/Xray-core](https://github.com/patterniha/Xray-core): ماسک‌های `merge` و `oob`.
- [PoriyaVali/mirage](https://github.com/PoriyaVali/mirage): ماسک `mirage`.
- [amnezia-vpn/amneziawg-go](https://github.com/amnezia-vpn/amneziawg-go): AmneziaWG.
- [enfein/mieru](https://github.com/enfein/mieru): Mieru.
- [SUDOKU-ASCII/sudoku](https://github.com/SUDOKU-ASCII/sudoku): پروتکل Sudoku.
- [TrustTunnel/TrustTunnel](https://github.com/TrustTunnel/TrustTunnel): پروتکل TrustTunnel.
- [xchacha20-poly1305/sing-trusttunnel](https://github.com/xchacha20-poly1305/sing-trusttunnel): کتابخانهٔ TrustTunnel.
- [Psiphon-Labs/psiphon-tunnel-core](https://github.com/Psiphon-Labs/psiphon-tunnel-core): Psiphon.
- [dnstt](https://www.bamsoftware.com/software/dnstt/): DNSTT اصلی.
- [net2share/vaydns](https://github.com/net2share/vaydns): کلاینت DNSTT.
- [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN): MasterDNS.
- [getlantern/soar](https://github.com/getlantern/soar): Soar.
- [Kianmhz/GooseRelayVPN](https://github.com/Kianmhz/GooseRelayVPN): GooseRelay.
- [kulikov0/headless-client](https://github.com/kulikov0/headless-client): اثرانگشت کروم برای تونل تماس.
- [Diniboy1123/connect-ip-go](https://github.com/Diniboy1123/connect-ip-go): CONNECT-IP برای WARP روی MASQUE.
- [Leadaxe/utls-lx](https://github.com/Leadaxe/utls-lx): اثرانگشت TLS مرورگرهای فعلی.
- [ameshkov/dnscrypt](https://github.com/ameshkov/dnscrypt): DNSCrypt.
- [pires/go-proxyproto](https://github.com/pires/go-proxyproto): PROXY protocol.
- [shadowsocks/simple-obfs](https://github.com/shadowsocks/simple-obfs): simple-obfs.

## رفع اشکال‌ها

- [رفع اشکال‌های v5](../bugfix/v5.md): اشکال‌هایی که روی sing-box نسخهٔ v1.15 رفع شده‌اند، جدیدترین در بالا، هر کدام با کامیتش.
