# ترنسپورت XHTTP

[همهٔ قابلیت‌های هیدیفای](../../index.md)

XHTTP ترنسپورت HTTP ایکس‌ری (Xray) است. اتصال پروکسی را به شکل درخواست‌ها و پاسخ‌های معمولی HTTP
می‌فرستد: یک پاسخ طولانی برای دانلود، و آپلود یا در چند درخواست کوچک یا در یک درخواست پیوسته. در این
فورک یک ترنسپورت V2Ray است؛ پس آن را در بلوک `transport` یک ورودی یا خروجی VLESS، VMess یا Trojan با
`"type": "xhttp"` تنظیم می‌کنید.

## چرا از آن استفاده کنیم

- از CDNها و پراکسی‌های معکوس (nginx، Caddy) که HTTP ساده را رد می‌کنند ولی WebSocket یا gRPC را
  خراب می‌کنند، عبور می‌کند.
- به سرورهای Xray که XHTTP دارند وصل می‌شود؛ پس یک سرور برای کلاینت‌های Xray و هیدیفای کافی است.
- می‌تواند آپلود و دانلود را به نشانی‌ها یا CDNهای جدا بفرستد (`download`).

## چطور از فیلترینگ عبور می‌کند

از دید فیلتر، XHTTP شبیه مرورگری است که با HTTPS با یک وب‌سایت حرف می‌زند: درخواست‌های معمولی GET و
POST با User-Agent کروم، پدینگ تصادفی با طول تصادفی در هر درخواست و پاسخ، و بدون ارتقای طولانی به
پروتکلی دیگر. پشت CDN، فیلتر فقط اتصال به CDN را می‌بیند. پدینگ و گزینه‌های obfs
(`x_padding_obfs_mode`) جای پدینگ و دادهٔ نشست را عوض می‌کنند تا درخواست‌ها شکل ثابتی نداشته باشند.

اگر فیلتر IP یا دامنهٔ سرور را مسدود کند، XHTTP سرور را پنهان نمی‌کند، مگر آن‌که CDN جلوی آن
بگذارید. بدون TLS (یا REALITY) درخواست‌ها خواناست.

## چطور کار می‌کند

- کلاینت برای هر اتصال پروکسی یک درخواست دانلود (GET) باز می‌کند و دادهٔ سرور را از پاسخ آن می‌خواند.
- آپلود به حالت (mode) بستگی دارد:
  - `packet-up`: کلاینت داده را در چندین درخواست POST، هر کدام با یک شمارهٔ ترتیب، می‌فرستد. تقریباً
    از همهٔ CDNها و پراکسی‌ها می‌گذرد.
  - `stream-up`: کلاینت داده را در یک درخواست POST طولانی و پیوسته می‌فرستد. سریع‌تر است، ولی مسیر باید
    بدنهٔ درخواست پیوسته را رد کند.
  - `stream-one`: آپلود و دانلود در یک درخواست پیوسته‌اند. مسیری می‌خواهد که هر دو جهت را پیوسته رد کند،
    مثل اتصال مستقیم TLS یا REALITY.
  - `auto`: در سرور هر سه حالت را می‌پذیرد. در کلاینت مثل کلاینت Xray انتخاب می‌کند: روی REALITY
    ‏`stream-one`، روی REALITY با `download` جداگانه `stream-up`، و در غیر این صورت `packet-up`.
    حالت خالی همان `auto` است.
- درخواست‌های آپلود و دانلود یک اتصال یک شناسهٔ نشست تصادفی مشترک دارند. پیش‌فرض این شناسه در مسیر
  است؛ `session_placement` و `seq_placement` شناسهٔ نشست و شمارهٔ ترتیب را به پارامتر کوئری، هدر یا
  کوکی منتقل می‌کنند.
- نسخهٔ HTTP از ALPN در TLS می‌آید: بدون TLS یا با `http/1.1` نسخهٔ HTTP/1.1، با `h2` نسخهٔ HTTP/2 و با
  `h3` نسخهٔ HTTP/3 روی QUIC (UDP). سروری که تنها ALPN آن `h3` است روی UDP گوش می‌دهد.
- XMUX اتصال‌های HTTP را برای چند اتصال پروکسی دوباره به کار می‌برد؛ گزینه‌های `xmux` میزان این
  استفادهٔ دوباره را محدود می‌کنند.

## پیکربندی

یک کلاینت VLESS و سرور متناظر آن:

```json
{
  "outbounds": [
    {
      "type": "vless",
      "tag": "proxy",
      "server": "example.com",
      "server_port": 443,
      "uuid": "bf000d23-0752-40b4-affe-68f7707a9661",
      "tls": {
        "enabled": true,
        "server_name": "example.com",
        "alpn": ["h2"],
        "utls": { "enabled": true, "fingerprint": "chrome" }
      },
      "transport": {
        "type": "xhttp",
        "mode": "packet-up",
        "path": "/assets",
        "x_padding_bytes": "100-1000"
      }
    }
  ]
}
```

```json
{
  "inbounds": [
    {
      "type": "vless",
      "listen": "::",
      "listen_port": 443,
      "users": [{ "uuid": "bf000d23-0752-40b4-affe-68f7707a9661" }],
      "tls": {
        "enabled": true,
        "server_name": "example.com",
        "alpn": ["h2", "http/1.1"],
        "certificate_path": "/etc/ssl/example.com.crt",
        "key_path": "/etc/ssl/example.com.key"
      },
      "transport": { "type": "xhttp", "mode": "auto", "path": "/assets" }
    }
  ]
}
```

فیلدهای بازه (range) یک رشتهٔ `"from-to"`، یک عدد یا `{"from": 1, "to": 2}` می‌گیرند.

| فیلد | نوع | پیش‌فرض | معنا |
|---|---|---|---|
| `mode` | string | `auto` | `auto`، `packet-up`، `stream-up` یا `stream-one`. در سرور، حالتی غیر از `auto` درخواست‌های حالت‌های دیگر را رد می‌کند. |
| `host` | string | نام سرور TLS، سپس نشانی سرور | Host درخواست‌های HTTP. سرور درخواست‌های هاست دیگر را رد می‌کند. |
| `path` | string | `/` | مسیر درخواست. می‌تواند کوئری داشته باشد (`/path?ed=2048`) که با هر درخواست فرستاده می‌شود. |
| `headers` | object | — | هدرهای اضافهٔ درخواست. نباید `Host` داشته باشد. اگر `User-Agent` نباشد، User-Agent کروم گذاشته می‌شود. |
| `x_padding_bytes` | range | `100-1000` | طول پدینگ تصادفی هر درخواست و پاسخ. نمی‌تواند ۰ باشد. |
| `x_padding_obfs_mode` | bool | `false` | از چهار گزینهٔ زیر برای پدینگ استفاده می‌کند. خاموش باشد، پدینگ مثل Xray قدیمی در کوئری `Referer` (کلاینت) و هدر `X-Padding` (سرور) می‌رود. |
| `x_padding_placement` | string | `queryInHeader` | جای پدینگ: `queryInHeader`، `header`، `query` یا `cookie`. |
| `x_padding_key` | string | `x_padding` | نام کوئری یا کوکی پدینگ. |
| `x_padding_header` | string | `X-Padding` | هدری که پدینگ را می‌برد (برای `header` و `queryInHeader`). |
| `x_padding_method` | string | `repeat-x` | `repeat-x` (رشته‌ای از `X`) یا `tokenish` (متن تصادفی base62 شبیه توکن). |
| `session_placement` | string | `path` | جای شناسهٔ نشست: `path`، `query`، `header` یا `cookie`. |
| `session_key` | string | `x_session` (کوئری، کوکی)، `X-Session` (هدر) | نام کوئری، هدر یا کوکی شناسهٔ نشست. |
| `seq_placement` | string | `path` | جای شمارهٔ ترتیب packet-up: `path`، `query`، `header` یا `cookie`. وقتی `session_placement` برابر `path` است باید `path` باشد. |
| `seq_key` | string | `x_seq` (کوئری، کوکی)، `X-Seq` (هدر) | نام کوئری، هدر یا کوکی شمارهٔ ترتیب. |
| `uplink_http_method` | string | `POST` | متد HTTP درخواست‌های آپلود. `GET` فقط در `packet-up` مجاز است. |
| `uplink_data_placement` | string | `body` | جای دادهٔ آپلود: `body`، یا `header` / `cookie` (فقط در `packet-up`). |
| `uplink_data_key` | string | `x_data` (کوکی)، `X-Data` (هدر) | نام هدر یا کوکی که دادهٔ آپلود را می‌برد. |
| `uplink_chunk_size` | integer | ۴۰۹۶ (هدر)، ۳۰۷۲ (کوکی) | اندازهٔ هر تکهٔ دادهٔ آپلود در هدر یا کوکی. دست‌کم ۶۴. |
| `no_grpc_header` | bool | `false` | `Content-Type: application/grpc` را در درخواست‌های آپلود نمی‌فرستد. |
| `no_sse_header` | bool | `false` | سرور: `Content-Type: text/event-stream` را در پاسخ‌های دانلود نمی‌فرستد. |
| `sc_max_each_post_bytes` | range | `1000000` | بزرگ‌ترین درخواست آپلود packet-up، به بایت. |
| `sc_min_posts_interval_ms` | range | `30` | کلاینت: کمترین فاصلهٔ دو آپلود packet-up، به میلی‌ثانیه. |
| `sc_max_buffered_posts` | integer | `30` | سرور: تعداد آپلودهای packet-up که هنگام انتظار برای یک آپلود جامانده نگه داشته می‌شوند. |
| `sc_stream_up_server_secs` | range | `20-80` | سرور: هر چند ثانیه روی پاسخ stream-up پدینگ می‌فرستد تا پراکسی‌ها آن را باز نگه دارند. |
| `xmux` | object | پایین را ببینید | استفادهٔ دوباره از اتصال‌های HTTP. |
| `download` | object | — | کلاینت: درخواست دانلود را به جای دیگری می‌فرستد. پایین را ببینید. |

فیلدهای `xmux` (همه بازه‌اند). وقتی `xmux` تنظیم نشده باشد، `max_concurrency` برابر ۱،
`h_max_request_times` برابر 600-900 و `h_max_reusable_secs` برابر 1800-3000 است.

| فیلد | نوع | پیش‌فرض | معنا |
|---|---|---|---|
| `max_concurrency` | range | `0` | تعداد اتصال پروکسی در هر اتصال HTTP. با `max_connections` با هم تنظیم نمی‌شود. |
| `max_connections` | range | `0` | تعداد اتصال‌های HTTP که باز و مشترک می‌شوند. |
| `c_max_reuse_times` | range | `0` | هر اتصال HTTP پیش از کنار گذاشته شدن به چند اتصال پروکسی خدمت می‌کند. |
| `h_max_request_times` | range | `0` | هر اتصال HTTP پیش از کنار گذاشته شدن چند درخواست HTTP می‌فرستد. |
| `h_max_reusable_secs` | range | `0` | پس از این چند ثانیه، اتصال HTTP دیگر دوباره به کار نمی‌رود. |
| `h_keep_alive_period` | integer | HTTP/2: مقدار کروم؛ HTTP/3: مقدار quic-go | دورهٔ keepalive به ثانیه. مقدار منفی آن را خاموش می‌کند. |

مقدار `0` یعنی بدون محدودیت.

`download` همان فیلدهای ترنسپورت (به جز `mode`) را می‌گیرد، به‌علاوهٔ `server`، `server_port`،
`tls` (به همان شکل `tls` خروجی) و `detour` (تگ خروجی‌ای که از طریق آن وصل می‌شود). آپلود به سرور
خروجی و دانلود به این سرور می‌رود؛ هر دو باید به یک سرور XHTTP در پشت خود برسند، مثلاً دو CDN جلوی
یک سرور اصلی.

سازگاری: در هر دو جهت با Xray 26.3.27 و 26.10.21 آزموده شده است. نام گزینه‌ها شکل snake_case نام‌های
Xray است (`xPaddingBytes` می‌شود `x_padding_bytes`). دو طرف باید مسیر، جای پدینگ و جای session/seq
یکسان داشته باشند. گزینهٔ نادرست هنگام بارگذاری کانفیگ خطای پیکربندی می‌دهد.

## همچنین ببینید

- [REALITY در هیدیفای](../reality-hiddify.md)
- [رمزگذاری VLESS](../protocols/vless-encryption.md)
- [finalmask](finalmask.md)
