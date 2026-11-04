# خروجی WireGuard (قالب قدیمی)

[همهٔ قابلیت‌های هیدیفای](../../index.md)

sing-box اصلی در نسخهٔ 1.13 خروجی WireGuard را حذف کرد و حالا WireGuard یک endpoint است.
هیدیفای این خروجی را با نام نوع تازه‌ای برمی‌گرداند تا پیکربندی‌هایی که با قالب قدیمی نوشته
شده‌اند کار کنند. این یک outbound است: `"type": "wireguard_legacy"` در فهرست `outbounds`. فیلدها
همان فیلدهای خروجی قدیمی `wireguard` هستند.

## چرا از آن استفاده کنیم

- پیکربندی یا مبدلی دارید که خروجی قدیمی WireGuard را می‌نویسد و نمی‌خواهید آن را به شکل
  endpoint بازنویسی کنید.

برای پیکربندی‌های تازه از [endpoint وایرگارد](wireguard-hiddify.md) استفاده کنید. افزوده‌های
هیدیفای (بسته‌های noise، بازیابی، نام peer) در آن هست و در این خروجی نیست.

## چطور از فیلترینگ عبور می‌کند

عبور نمی‌دهد. این WireGuard ساده است و فیلتر می‌تواند آن را از روی دست‌دادنش بشناسد. برای پنهان
کردن، از [endpoint وایرگارد](wireguard-hiddify.md) با noise یا از [AmneziaWG](amneziawg.md)
استفاده کنید.

## چطور کار می‌کند

- همان موتور WireGuard را اجرا می‌کند که endpoint اجرا می‌کند، با پشتهٔ شبکهٔ فضای کاربر، یا با
  یک رابط شبکهٔ سیستمی وقتی `system_interface` روشن است.
- با `peers`، هر peer نشانی، کلیدها و allowed IPs خودش را دارد. بدون `peers`، فیلدهای
  `server`، `server_port`، `peer_public_key`، `pre_shared_key` و `reserved` در سطح بالا یک peer
  می‌سازند که همهٔ ترافیک (`0.0.0.0/0` و `::/0`) را می‌گیرد.
- مقصدی که دامنه است با قاعده‌های پیش‌فرض DNS resolve می‌شود و بعد اتصال از تونل می‌رود.
  peerی که با دامنه داده شده هم به همین شکل resolve می‌شود.
- TCP، UDP و ping از تونل عبور می‌کنند. `network` ترافیک TCP و UDP را محدود می‌کند؛ ping همیشه پذیرفته می‌شود.
- نوع آن همچنان `wireguard` گزارش می‌شود، پس برنامه آن را WireGuard نشان می‌دهد.

## پیکربندی

```json
{
  "outbounds": [
    {
      "type": "wireguard_legacy",
      "tag": "wg-out",
      "server": "203.0.113.10",
      "server_port": 51820,
      "local_address": ["10.8.0.2/32"],
      "private_key": "<base64 private key>",
      "peer_public_key": "<base64 server public key>"
    }
  ]
}
```

| فیلد | نوع | پیش‌فرض | معنی |
|---|---|---|---|
| `local_address` | list of prefixes | الزامی | نشانی‌های این سمت تونل. |
| `private_key` | string | الزامی | کلید خصوصی، base64. |
| `server` | string | ندارد | نشانی سرور، وقتی `peers` خالی است. |
| `server_port` | int | ندارد | پورت سرور، وقتی `peers` خالی است. |
| `peer_public_key` | string | ندارد | کلید عمومی سرور، base64، وقتی `peers` خالی است. |
| `pre_shared_key` | string | ندارد | کلید پیش‌مشترک، base64، وقتی `peers` خالی است. |
| `reserved` | list of 3 bytes | ندارد | بایت‌های reserved برای peer، وقتی `peers` خالی است. Cloudflare WARP از آن‌ها استفاده می‌کند. |
| `peers` | list of objects | ندارد | چند peer. هر کدام `server`، `server_port`، `public_key`، `pre_shared_key`، `allowed_ips` (الزامی) و `reserved` دارد. |
| `mtu` | int | `1408` | MTU تونل. |
| `workers` | int | تعداد CPUها | تعداد workerهای WireGuard. |
| `system_interface` | bool | `false` | به جای پشتهٔ فضای کاربر از رابط شبکهٔ سیستمی استفاده کن. |
| `interface_name` | string | ندارد | نام رابط سیستمی. |
| `network` | `"tcp"` or `"udp"` | هر دو | شبکه‌هایی که خروجی می‌پذیرد، مثل خروجی قدیمی sing-box اصلی. ping همیشه پذیرفته می‌شود. |
| `gso` | bool | `false` | برای پیکربندی‌های قدیمی پذیرفته می‌شود، اما به کار نمی‌رود. با `detour` قابل استفاده نیست. |

فیلدهای اتصال (`detour`، `bind_interface` و بقیه) مثل خروجی‌های دیگر کار می‌کنند. گزینه‌ای برای
keepalive وجود ندارد، مثل خروجی قدیمی sing-box اصلی.

## همچنین ببینید

- [WireGuard: افزوده‌های هیدیفای](wireguard-hiddify.md)
- [AmneziaWG](amneziawg.md)
- [WARP](warp.md)
