---
title: قابلیت‌های sing-box هیدیفای
weight: -50
---

# sing-box هیدیفای

قابلیت‌ها و رفع اشکال‌هایی در فورک هیدیفای که sing-box اصلی ندارد. هر صفحهٔ قابلیت یک نسخهٔ
انگلیسی و یک نسخهٔ فارسی دارد.

## قابلیت‌ها

- [تکه‌تکه کردن TLS](features/tls-fragment.md): ClientHello را با مکث به تکه‌های کوچک تقسیم می‌کند تا DPI نتواند نام سرور را بخواند.
- [ترفندهای TLS](features/tls-tricks.md): نام سرور با حروف بزرگ و کوچک درهم و یک افزونهٔ padding در ClientHello.
- [REALITY در هیدیفای](features/reality-hiddify.md): key share پساکوانتومی، گزینهٔ `key_share` و تکه‌تکه کردن روی REALITY.
- [پروتکل PROXY](features/proxy-protocol.md): ورودی‌ها هدر PROXY protocol را می‌خوانند و خروجی direct آن را می‌فرستد.

## پروتکل‌ها

- [WARP](features/protocols/warp.md): WARP کلادفلر روی WireGuard، AmneziaWG یا MASQUE، با ثبت حساب رایگان، بسته‌های نویز و اسکنری که برای هر شبکه جدا به نشانی دیگری می‌رود.
- [اسکنر و noise در WARP](features/protocols/warp-scanner.md): اسکنر endpoint، حالت‌ها و پیش‌تنظیم‌های noise (DNS، QUIC، SIP، تصادفی)، جست‌وجوی noise و حالت auto چطور راهی برای عبور پیدا می‌کنند.
- [WARP روی MASQUE](features/protocols/warp-masque.md): outbound مستقل `masque` برای WARP روی HTTP/3، HTTP/2 یا هر دو، با دستگاهی که جای دیگری ثبت شده؛ برای ثبت دستگاه، endpoint ‏`warp` با `mode` برابر `masque` را به کار ببرید؛ برای سرور MASQUE شخصی، از `masque-client` در sing-box اصلی استفاده کنید.
- [AmneziaWG](features/protocols/amneziawg.md): WireGuard با بسته‌های بی‌معنی، handshakeهای padding‌دار و نوع پیام‌های دلخواه که شناسایی WireGuard را خنثی می‌کنند.
- [WireGuard: افزوده‌های هیدیفای](features/protocols/wireguard-hiddify.md): بسته‌های نویز پیش از handshake، نام کاربر برای هر peer، بازیابی سوکت و تکه‌تکه کردن UDP که به‌طور پیش‌فرض روشن است.
- [خروجی WireGuard (قالب قدیمی)](features/protocols/wireguard-legacy.md): خروجی قدیمی WireGuard که sing-box اصلی حذفش کرد، نگه داشته شده تا کانفیگ‌های قدیمی هنوز بارگذاری شوند.
- [رمزگذاری VLESS](features/protocols/vless-encryption.md): رمزگذاری پساکوانتومی VLESS از Xray، با Vision روی آن حتی بدون TLS.
- [Sudoku](features/protocols/sudoku.md): یک پراکسی رمزشدهٔ TCP که بایت‌هایش را به شکل سرنخ‌های سودوکو می‌فرستد تا ترافیک شبیه متن باشد یا تصادفی بودن کمی داشته باشد، با تونل‌های HTTP اختیاری (build tag `with_sudoku`).
- [Mieru](features/protocols/mieru.md): یک پراکسی کاملاً رمزشده و padding‌دار روی بازه‌های پورت TCP یا UDP، بدون هیچ الگوی ثابت.
- [TrustTunnel](features/protocols/trusttunnel.md): ترافیک پراکسی به شکل جریان‌های HTTP CONNECT روی HTTP/2 یا HTTP/3.
- [SSH](features/protocols/ssh.md): یک ورودی سرور SSH برای port forwarding، به‌علاوهٔ UDP روی TCP و اتصال پس‌زمینه برای خروجی SSH.
- [سایفون](features/protocols/psiphon.md): بدون سرور شخصی از راه شبکهٔ سایفون وصل شوید و کشور خروجی را انتخاب کنید.
- [DNSTT](features/protocols/dnstt.md): ترافیک را درون پرس‌وجوهای DNS از راه resolverهای عمومی می‌برد و خودش آن‌ها را پیدا می‌کند.
- [MasterDNS](features/protocols/masterdns.md): تونل MasterDnsVPN از راه resolverهای عمومی، با سربار کم، تکرار بسته‌ها روی چند resolver و آزمایش MTU؛ سرور خودش به مقصد وصل می‌شود.
- [Soar](features/protocols/soar.md): تونل DNS پروژهٔ Lantern، هر resolver یک مسیر جدا با بازیابی سریع از دست رفتن بسته‌ها و کشف resolver، به‌طور پیش‌فرض از راه مجموعهٔ هوشمند؛ لینک‌های `soar://`.
- [GooseRelay](features/protocols/gooserelay.md): ترافیک را از راه Google Apps Script به سرور خودتان می‌فرستد، پس شبکه فقط HTTPS به گوگل می‌بیند.
- [تونل تماس](features/protocols/call.md): ترافیک پراکسی را درون یک تماس تصویری در VK، Telemost، Dion، WB Stream یا Bitrix24 می‌برد تا شبیه تماس با یک سرویس داخلی مجاز باشد؛ به‌طور کامل تست نشده است (build tag `with_call`).
- [Tunnel](features/protocols/tunnel.md): یک تونل معکوس که از راه یک سرور عمومی به دستگاه‌های پشت NAT می‌رسد.
- [Bond](features/protocols/bond.md): هر اتصال را هم‌زمان روی چند خروجی تقسیم می‌کند و در سرور به هم وصل می‌کند تا سرعت اتصال‌های محدودشده جمع شود (build tag `with_bond`).

## ترنسپورت‌ها

- [XHTTP](features/transports/xhttp.md): ترنسپورت XHTTP از Xray با حالت‌ها، padding، جایگاه‌ها، XMUX و دانلود جداگانه.
- [mKCP](features/transports/kcp.md): mKCP نسخهٔ Xray 26 روی UDP برای شبکه‌های پرافت یا شبکه‌هایی که TCP را کند می‌کنند، پنهان‌شده با ماسک‌های UDP در finalmask (build tag `with_kcp`).
- [XDRIVE](features/transports/xdrive.md): ترنسپورت ذخیره‌سازی Xray؛ اتصال VLESS در فایل‌هایی روی Google Drive، S3 یا سرویس ذخیره‌سازی دیگر حمل می‌شود و کلاینت هرگز به سرور وصل نمی‌شود (build tag `with_xdrive`).
- [ترنسپورت raw](features/transports/raw.md): ترنسپورت `raw`، تا کانفیگ‌هایی که از Xray تبدیل شده‌اند بارگذاری شوند.
- [مسیرهای دلخواه gRPC](features/transports/grpc-custom-path.md): مسیرهای چندبخشی gRPC به سبک Xray در `service_name`.
- [finalmask](features/transports/finalmask.md): ماسک‌های finalmask از Xray (fragment، noise، header-custom، xdns روی UDP، TCP یا DoH، udphop، merge، oob و موارد دیگر) روی هر اتصالی که یک خروجی برقرار می‌کند.
- [سرور simple-obfs در Shadowsocks](features/transports/shadowsocks-obfs.md): یک سرور simple-obfs روی ورودی‌های Shadowsocks، با یک مقصد فریب وقتی obfs یا ورود شکست بخورد.
- [rmux](features/transports/rmux.md): یک پروتکل چندگانه‌سازی دیگر برای بردن چند اتصال در یک اتصال، در کنار smux، yamux و h2mux.

## DNS

- [گروه DNS](features/dns/dns-group.md): از چند سرور DNS هم‌زمان یا به نوبت بپرسید، یا روی سروری که کار می‌کند بمانید، و پاسخ‌های مسموم را کنار بگذارید.
- [IPv6 بر اساس خروجی](features/dns/ipv6-by-outbound.md): IPv6 فقط از خروجی‌هایی که معلوم است آن را رد می‌کنند، بررسی‌شده در تست URL و آموخته از اتصال‌ها؛ اتصالی که خروجی نتواند رد کند درون همان اتصال با IPv4 برده می‌شود تا هیچ برنامه‌ای مرگش را نبیند.
- [قاعده‌های DNS: bypass_if_failed](features/dns/dns-bypass-if-failed.md): وقتی سرور یک قاعدهٔ DNS شکست می‌خورد، پرس‌وجو به قاعدهٔ منطبق بعدی می‌رود.
- [مجموعهٔ هوشمند resolver](features/dns/smart-dns-pool.md): مجموعهٔ resolverی که هر خروجی تونل DNS با `smart_pool` برای خودش راه می‌اندازد، مشترک میان DNSTT، MasterDNS و Soar، با resolverهای `auto`، امتیازهای ذخیره‌شده و DoT/DoH.
- [DNSCrypt (استمپ‌های SDNS)](features/dns/sdns.md): سرور `sdns` که پرس‌وجوهای رمزشده را به یک resolver از نوع DNSCrypt می‌فرستد که با استمپش مشخص شده است.
- [نام‌های sslip.io](features/dns/sslip-hosts.md): سرور `hosts` به نام‌های `sslip.io` با نشانی‌ای که در خود نام نوشته شده پاسخ می‌دهد.

## گروه‌ها و پایش

- [متعادل‌کننده](features/groups/balancer.md): اتصال‌ها را با round robin، کمترین تأخیر، consistent hashing، ‏sticky session یا یک مخزن چسبنده (pool) میان اعضا پخش می‌کند.
- [جایگزین](features/groups/fallback.md): اعضا را به ترتیب امتحان می‌کند و عضوی را که شکست خورده تا مدتی کنار می‌گذارد.
- [تست URL: افزوده‌های هیدیفای](features/groups/urltest.md): نشانی‌های تست بیشتر، حالت `failover` و رفتن به عضو دیگر با اولین اتصال ناموفق.
- [پایش](features/groups/monitoring.md): تست پس‌زمینهٔ همهٔ خروجی‌ها برای تأخیر و IP خروجی، که نتیجه‌اش به گروه‌ها داده می‌شود.
- [تأخیر یکسان](features/groups/unified-delay.md): تست‌های URL زمان یک رفت‌وبرگشت HTTP را روی اتصال باز می‌سنجند، تا تأخیرها میان پروتکل‌ها قابل مقایسه باشند.

## برای توسعه‌دهندگان اپ

- [ملاحظات اپ](app_considerations.md) (انگلیسی): آنچه hiddify-app و hiddify-core به‌خاطر کارهای v5 باید تغییر دهند یا بدانند.

## رفع اشکال‌ها

- [رفع اشکال‌های v5](bugfix/v5.md): اشکال‌هایی که روی sing-box نسخهٔ v1.15 رفع شده‌اند، جدیدترین در بالا، هر کدام با کامیتش.
