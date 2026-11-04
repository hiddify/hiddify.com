# ترنسپورت XDRIVE

[همهٔ قابلیت‌های هیدیفای](../../index.md)

XDRIVE ترنسپورت ذخیره‌سازی Xray-core است. کلاینت و سرور هرگز به هم وصل نمی‌شوند: کلاینت دادهٔ اتصال را
به شکل فایل در یک سرویس ذخیره‌سازی می‌نویسد، سرور آن‌ها را همان‌جا می‌خواند و پاسخ‌هایش را برمی‌گرداند.
این سرویس می‌تواند Google Drive، هر سرویس S3، سرویسی که با «template» از درخواست‌های HTTP توصیف شده،
یا یک پوشهٔ محلی باشد. در این فورک یک ترنسپورت V2Ray است که در بلوک `transport` ورودی یا خروجی VLESS با
`"type": "xdrive"` تنظیم می‌شود.

## چرا از آن استفاده کنیم

- وقتی همهٔ راه‌ها به سرور بسته است کار می‌کند: کلاینت فقط با سرویس ذخیره‌سازی، مثلاً APIهای Google،
  حرف می‌زند که فیلتر به‌ندرت مسدودش می‌کند.
- به سرورهای Xray که از XDRIVE استفاده می‌کنند وصل می‌شود.
- سرور نه پورت باز می‌خواهد نه نشانی عمومی؛ فقط باید به سرویس ذخیره‌سازی برسد.

## چطور از فیلترینگ عبور می‌کند

از دید فیلتر، کلاینت برنامه‌ای است که فایل‌ها را با Google Drive یا S3 همگام می‌کند: درخواست‌های HTTPS
به دامنهٔ خود سرویس، با اثر انگشت TLS و هدرهای HTTP مرورگر Chrome. نشانی سرور هرگز در شبکهٔ کلاینت
دیده نمی‌شود. `fronting_address` می‌تواند این درخواست‌ها را به نشانی دیگری از همان سرویس بفرستد، مثلاً
یک IP جلویی Google، در حالی که نام سرور در TLS همان نام سرویس می‌ماند.

کند و پرهزینه است: هر نوشتن یک بارگذاری فایل است و طرف دیگر برای آن polling می‌کند؛ پس رفت‌وبرگشت
صدها میلی‌ثانیه یا بیشتر است و سهمیهٔ API سرویس مقدار عبوری را محدود می‌کند. آن را آخرین راه بدانید، نه
برای ترافیک روزانه.

## چطور کار می‌کند

- کلاینت با نوشتن یک فایل اعلام با شناسهٔ تصادفی نشست در `remote_folder` نشست را باز می‌کند. سرور
  پوشه را فهرست می‌کند، نشست را برمی‌دارد و در آن پاسخ می‌دهد.
- هر جهت دنباله‌ای از تکه‌هاست، فایل‌هایی تا اندازهٔ `segment_bytes`. داده‌ای که در `flush_interval_ms`
  نوشته شود در یک تکه می‌رود. خواننده هر `poll_interval_ms` سر می‌زند و وقتی چیزی نمی‌آید فاصله را تا
  `max_poll_interval_ms` بیشتر می‌کند.
- روی Google Drive، نشست به جای فایل تازه برای هر تکه از حلقه‌ای از فایل‌های slot استفاده می‌کند که
  بازنویسی می‌شوند.
- نشست‌های قدیمی پس از `session_ttl_seconds` پاک می‌شوند.
- درخواست‌ها به سرویس با کلاینت خود Xray فرستاده می‌شوند، روی h2، یا روی h3 وقتی `alpn` در TLS فقط
  `["h3"]` باشد، با XMUX برای استفادهٔ دوباره از اتصال‌ها. هر سوکتی که باز می‌کند از dialer خروجی
  می‌گذرد؛ پس `detour`، گزینه‌های اینترفیس و `finalmask` خروجی اعمال می‌شوند.
- هر اتصال پروکسی یک نشست است. کلاینت XDRIVE در Xray همیشه Mux.Cool را رویش اجرا می‌کند تا یک نشست
  چند اتصال را ببرد. سرور VLESS این فورک آن را می‌پذیرد، ولی کلاینتش Mux.Cool ندارد و برای هر اتصال
  یک نشست باز می‌کند.

## پیکربندی

یک کلاینت VLESS روی Google Drive، و سمت سرور در همان پوشه:

```json
{
  "outbounds": [
    {
      "type": "vless",
      "server": "127.0.0.1",
      "server_port": 1,
      "uuid": "bf000d23-0752-40b4-affe-68f7707a9661",
      "encryption": "mlkem768x25519plus.native.0rtt.…",
      "tls": { "enabled": true, "utls": { "enabled": true, "fingerprint": "chrome" } },
      "transport": {
        "type": "xdrive",
        "service": "google-drive",
        "remote_folder": "1AbCdEfGhIjKlMnOpQrStUvWxYz",
        "secrets": ["<client id>", "<client secret>", "<refresh token>"]
      }
    }
  ],
  "inbounds": [
    {
      "type": "vless",
      "listen": "127.0.0.1",
      "listen_port": 1,
      "users": [{ "uuid": "bf000d23-0752-40b4-affe-68f7707a9661" }],
      "decryption": "mlkem768x25519plus.native.600s.…",
      "transport": {
        "type": "xdrive",
        "service": "google-drive",
        "remote_folder": "1AbCdEfGhIjKlMnOpQrStUvWxYz",
        "secrets": ["<client id>", "<client secret>", "<refresh token>"]
      }
    }
  ]
}
```

`server` و `server_port` خروجی را VLESS لازم دارد ولی استفاده نمی‌شوند. پورت شنود ورودی به محض شروع
ترنسپورت بسته می‌شود: سرور به جای آن سرویس ذخیره‌سازی را می‌خواند.

| فیلد | نوع | پیش‌فرض | معنا |
|---|---|---|---|
| `service` | string | — | `google-drive`، `s3`، `template` یا `local`. الزامی. |
| `remote_folder` | string | — | پوشه: شناسهٔ پوشهٔ Drive، پیشوند کلید در S3، یا یک پوشهٔ محلی. |
| `secrets` | فهرست رشته | — | `google-drive`: client id، client secret، refresh token. `s3`: access key id، secret access key و در صورت نیاز session token. `template`: مقدارهایی که درخواست‌هایش به آن‌ها اشاره می‌کنند. |
| `s3` | object | — | برای `s3`: `endpoint`، `region`، `bucket`، `path_style` (پیش‌فرض `true`). |
| `template` | object | — | برای `template`: درخواست‌های HTTP برای put، get، list و delete، مثل Xray. |
| `segment_bytes` | number | `524288` | بزرگ‌ترین فایل تکه، حداکثر ۱۶ مگابایت. |
| `flush_interval_ms` | number | `20` | مدتی که نوشتن‌ها در یک تکه جمع می‌شوند. |
| `poll_interval_ms`، `max_poll_interval_ms` | number | `50`، `500` | اولین و طولانی‌ترین مکث میان pollها. |
| `session_ttl_seconds` | number | `300` | زمانی که فایل‌های نشست بی‌کار پاک می‌شوند. |
| `concurrency` | number | `8` | درخواست‌های هم‌زمان هر نشست، حداکثر ۶۴. |
| `eager_window_ms` | number | `2000` | مدتی که خواننده پس از آخرین داده با سرعت بالا poll می‌کند. |
| `hole_timeout_ms` | number | `30000` | مدت انتظار برای تکهٔ گم‌شده پیش از شکست نشست. |
| `xmux` | object | ۴ اتصال روی Google Drive با h2، وگرنه ۱ | استفادهٔ دوباره از اتصال‌ها، همان فیلدهای `xmux` در XHTTP. |
| `fronting_address`، `fronting_port` | string، number | — | این نشانی برای همهٔ میزبان‌های سرویس شماره‌گیری می‌شود؛ نام سرور در TLS همان نام میزبان می‌ماند. |

`tls` خروجی TLS درخواست‌ها به سرویس را تعیین می‌کند: `server_name`، `alpn` و `fingerprint` در uTLS.
نام سروری که با `server` خروجی یکی باشد نادیده گرفته می‌شود، چون XDRIVE هرگز به آن‌جا وصل نمی‌شود.
بدون `tls` یا بدون uTLS، درخواست‌ها با اثر انگشت Chrome و نام خود هر میزبان فرستاده می‌شوند.

## نکته‌ها

- Xray اجازهٔ XDRIVE را فقط برای VLESS با `encryption` (برای جفت کلید `xray vlessenc` را اجرا کنید) و
  بدون `flow` می‌دهد. با سرور Xray همین را به کار ببرید.
- ترنسپورت با تگ `with_xdrive` ساخته می‌شود که Makefile و hiddify-core آن را روشن می‌کنند.
- Xray لینک اشتراک‌گذاری برای XDRIVE ندارد. hiddify-core خروجی JSON از Xray با XDRIVE را به لینک VLESS
  با `type=xdrive` می‌نویسد و `xdriveSettings` در Xray را به‌صورت JSON در `xdrive=` می‌گذارد (همراه
  `address` و `port` جریان برای fronting)، و ray2sing همان لینک را می‌خواند.
- سرویس `local` برای آزمایش و برای کلاینت و سروری روی یک ماشین یا یک دیسک مشترک است.
- در هر دو جهت روی سرویس `local` با Xray-core 26.10.31 آزموده شده است
  (`h_xray_xdrive_interop_test.go`).

## همچنین ببینید

- [finalmask](finalmask.md)
- [ترنسپورت XHTTP](xhttp.md)
