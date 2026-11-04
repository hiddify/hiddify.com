# سرور simple-obfs و fallback در Shadowsocks

[همهٔ قابلیت‌های هیدیفای](../../index.md)

ورودی Shadowsocks می‌تواند سمت سرور simple-obfs (`obfs-server`) را اجرا کند؛ پس کلاینت‌هایی که افزونهٔ
`obfs-local` را در حالت `http` یا `tls` به کار می‌برند مستقیم به sing-box وصل می‌شوند. همچنین می‌تواند هر
اتصالی را که کلاینت معتبر نیست به یک سرور پوششی بفرستد تا کاوشگر به جای اتصال بسته، یک وب‌سایت واقعی
ببیند. این‌ها فیلدهای `obfs_mode` و `obfs_fallback` در ورودی `"type": "shadowsocks"` هستند و با ورودی
تک‌کاربره، چندکاربره (`users`) و relay (`destinations`) کار می‌کنند.

## چرا از آن استفاده کنیم

- برای پاسخ به کلاینت‌های Shadowsocks که از `obfs-local` استفاده می‌کنند (اپ‌های Shadowsocks و خروجی
  Shadowsocks خود sing-box با `"plugin": "obfs-local"`) بدون اجرای جداگانهٔ `obfs-server`.
- تا سرور برای هر کسی که بدون رمز درست به آن وصل شود، شبیه یک وب‌سرور معمولی باشد.

## چطور از فیلترینگ عبور می‌کند

- simple-obfs آغاز هر اتصال را در یک درخواست ارتقای WebSocket در HTTP (`http`) یا یک ClientHello در TLS
  (`tls`) می‌پیچد؛ پس ترافیک Shadowsocks ساده، که تصادفی به نظر می‌رسد، مثل ترافیک وب شروع می‌شود.
- فیلترها اغلب سرورهای مشکوک را کاوش می‌کنند: وصل می‌شوند و دادهٔ خودشان را می‌فرستند، یا درخواست ضبط‌شدهٔ
  یک کلاینت را دوباره می‌فرستند، و پاسخ را می‌پایند. با `obfs_fallback` چنین کاوشی به سرور پوششی، مثلاً
  یک وب‌سایت واقعی روی همان پورت، وصل می‌شود و پاسخ عادی آن را می‌گیرد.

simple-obfs قدیمی است و شکل‌های HTTP و TLS آن برای فیلتری که دقیق بررسی کند به‌سادگی شناختنی است؛ شکل TLS
آن TLS واقعی نیست. آن را برای کلاینت‌هایی به کار ببرید که گزینهٔ دیگری ندارند.

## چطور کار می‌کند

- با تنظیم `obfs_mode`، ورودی اولین درخواست کلاینت را می‌خواند. برای `http` باید یک GET با
  `Upgrade: websocket` باشد؛ برای `tls` یک ClientHello با ساختار دقیق simple-obfs. سرور با HTTP 101 یا
  یک ServerHello در TLS پاسخ می‌دهد و دادهٔ Shadowsocks درون آن را جلو می‌فرستد.
- با تنظیم `obfs_fallback`، ورودی تا وقتی Shadowsocks کلاینت را احراز هویت نکرده، رونوشتی از آنچه کلاینت
  فرستاده (تا ۱۶ کیلوبایت) نگه می‌دارد. اگر پیش از آن چیزی شکست بخورد، اتصال و بایت‌های رونوشت به نشانی
  fallback می‌روند. این شامل این موارد است:
  - اتصال‌هایی که simple-obfs نیستند، مثل مرورگر یا اسکنر (مثل `obfs-server --failover`)؛
  - اتصال‌هایی که از obfs می‌گذرند ولی در Shadowsocks شکست می‌خورند: کاربر ناشناخته، رمز نادرست یا
    درخواست تکراری. پس کاوشگری که درخواست obfs یک کلاینت واقعی را کپی کند هم سرور پوششی را می‌بیند.
- پس از احراز هویت دیگر چیزی ضبط نمی‌شود و خطای بعدی اتصال را می‌بندد.
- اتصال fallback مثل هر اتصال دیگری از این ورودی مسیریابی می‌شود و مقصدش نشانی fallback است؛ پس
  قواعد مسیریابی شما تعیین می‌کنند کدام خروجی به آن برسد (معمولاً `direct`).
- obfs فقط روی TCP اعمال می‌شود. UDP در Shadowsocks تغییری نمی‌کند.

## پیکربندی

```json
{
  "inbounds": [
    {
      "type": "shadowsocks",
      "listen": "::",
      "listen_port": 443,
      "method": "2022-blake3-aes-128-gcm",
      "password": "8JCsPssfgS8tiRwiMlhARg==",
      "users": [{ "name": "alice", "password": "PCD2Z4o12bKUoFa3cC97Hw==" }],
      "obfs_mode": "tls",
      "obfs_fallback": { "server": "www.example.com", "server_port": 443 }
    }
  ]
}
```

یک کلاینت متناظر:

```json
{
  "outbounds": [
    {
      "type": "shadowsocks",
      "server": "203.0.113.1",
      "server_port": 443,
      "method": "2022-blake3-aes-128-gcm",
      "password": "8JCsPssfgS8tiRwiMlhARg==:PCD2Z4o12bKUoFa3cC97Hw==",
      "plugin": "obfs-local",
      "plugin_opts": "obfs=tls;obfs-host=www.example.com"
    }
  ]
}
```

| فیلد | نوع | پیش‌فرض | معنا |
|---|---|---|---|
| `obfs_mode` | string | `""` | `http` یا `tls`: سرور simple-obfs را اجرا می‌کند. خالی: بدون obfs. |
| `obfs_fallback` | object | — | سرور پوششی برای اتصال‌هایی که در obfs یا احراز هویت Shadowsocks شکست می‌خورند: `server` و `server_port`. به `obfs_mode` نیاز دارد. |
| `obfs_host` | string | `""` | هاست‌هایی که کلاینت می‌تواند بفرستد، جدا شده با کاما. اگر تنظیم شود، کلاینتی که `Host` در HTTP یا نام سرور در TLS آن در فهرست نباشد simple-obfs حساب نمی‌شود: به `obfs_fallback` فرستاده یا بسته می‌شود. خالی یعنی هر هاستی. به `obfs_mode` نیاز دارد. |

خطاها: `obfs_mode` غیر از `http` یا `tls`، `obfs_fallback` بدون `obfs_mode`، یا fallback بدون نشانی و
پورت معتبر خطای پیکربندی است. بدون `obfs_fallback`، اتصال ناموفق بسته می‌شود.

## همچنین ببینید

- [finalmask](finalmask.md)
