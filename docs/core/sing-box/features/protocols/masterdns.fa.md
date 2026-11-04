# MasterDNS

[همهٔ قابلیت‌های هیدیفای](../../index.md)

MasterDNS اتصال‌های TCP شما را درون پرسش‌ها و پاسخ‌های DNS، از راه resolverهای عمومی، به سرور
[MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) خودتان می‌برد. این یک outbound است:
`"type": "masterdns"` در فهرست `outbounds`. کلاینت همان کلاینت Go پروژهٔ MasterDnsVPN است که
به شکل کتابخانه در هسته جاسازی شده است.

## چرا از آن استفاده کنیم

- در شبکه‌هایی کار می‌کند که تقریباً همه‌چیز در آن‌ها مسدود است ولی DNS به resolverهای عمومی
  یا محلی هنوز عبور می‌کند، از جمله در حالت اینترنت ملی که فقط resolverهای داخلی پاسخ می‌دهند
  و پرسش‌های شما را به خارج می‌فرستند.
- در مقایسه با [DNSTT](dnstt.md)، پروتکل آن سربار بسیار کمتری دارد، پس هر پرسش دادهٔ بیشتری
  می‌برد؛ هر بسته را هم‌زمان از چند resolver می‌فرستد (duplication)، اتصالی را که resolverش
  بسته‌ها را می‌اندازد به resolver دیگری می‌برد، MTU هر resolver را اندازه می‌گیرد و
  resolverهای ناموفق را در پس‌زمینه دوباره آزمایش می‌کند. پروژه چند برابر DNSTT سرعت گزارش
  می‌کند.
- سرور خودش اتصال به مقصد را باز می‌کند، پس پشت آن به خروجی SOCKS یا SSH نیازی نیست
  (`mode: socks5`).

با این همه یک تونل DNS است: در کنار یک پراکسی مستقیم کند است و به تعداد پرسش‌هایی که resolverها
می‌پذیرند محدود می‌شود. وقتی چیز دیگری عبور نمی‌کند از آن استفاده کنید.

## چطور از فیلترینگ عبور می‌کند

فیلتر پرسش‌های DNS به یک resolver را می‌بیند، برای نام‌هایی زیر دامنهٔ تونل شما، و resolver
آن‌ها را به سرور شما می‌فرستد که مرجع آن دامنه است. داده‌های درون نام‌ها و پاسخ‌ها با کلیدی
رمز می‌شوند که فقط دستگاه شما و سرور شما می‌دانند (`encryption`، `key`): XOR (سبک، بدون بایت
اضافه)، ChaCha20 یا AES-GCM. به resolverهایی که پاسخ‌های باینری را خراب می‌کنند می‌توان پاسخ
base64 داد (`base_encode`).

وقتی resolverهای در دسترس نام‌های بلند را رد کنند، یا همهٔ resolverهای بیرونی مسدود باشند و
داخلی‌ها پرسش را به بیرون نفرستند، کمکی نمی‌کند.

## چطور کار می‌کند

- **شروع.** کلاینت به هر جفت دامنهٔ تونل و resolver در `resolvers` کاوش‌های MTU می‌فرستد،
  `mtu_test_parallelism` تا هم‌زمان، با `mtu_test_retries` تلاش و هر کدام تا
  `mtu_test_timeout`. یک resolver وقتی قبول می‌شود که پاسخ‌های سرور از راه آن برگردند؛ کوچک‌ترین
  اندازه‌های آپلود و دانلودی که قبول شدند MTU تونل می‌شوند. با `auto_remove_low_mtu_resolvers`،
  چند resolver که MTU مشترک را پایین می‌کشند به جای آن کنار گذاشته می‌شوند. سپس کلاینت یک
  نشست با سرور باز می‌کند. خروجی با باز شدن نشست آماده است؛ اتصالی که پیش از آن ساخته شود تا
  `ready_timeout` منتظر می‌ماند.
- **resolverها.** هر پرسش به resolverی می‌رود که `balancing` انتخاب می‌کند و
  `packet_duplication` بار از resolverهای متفاوت فرستاده می‌شود، تا یک resolver پرافت آن را گم
  نکند. اتصالی که روی resolverش مدام دوباره می‌فرستد به resolver دیگری می‌رود. resolverی که
  فقط timeout می‌دهد کنار گذاشته می‌شود (`auto_disable_timeout_resolvers`) و بعداً دوباره
  آزمایش می‌شود (`recheck_inactive_resolvers`).
- **مجموعهٔ هوشمند.** با `smart_pool`، کلاینت یک resolver می‌بیند: [مجموعهٔ هوشمند
  resolver](../dns/smart-dns-pool.md) خود خروجی، همان کد [DNSTT](dnstt.md). به هر
  resolver در `resolvers` اول یک پرسش ساده فرستاده می‌شود (`pretest_domain`،
  `pretest_record_type`)، اول آن‌هایی که قبلاً کار کرده‌اند، و آن‌هایی که پاسخ دهند به
  مجموعه می‌پیوندند تا ۱۰ تا کار کنند؛ وقتی برخی از کار بیفتند، بعدی‌ها بررسی می‌شوند. مجموعه پرسش‌های تونل را میان آن‌ها پخش می‌کند، برای resolverی که محدودیت
  نرخ می‌گذارد کند می‌شود و resolverی را که دیگر پاسخ نمی‌دهد کنار می‌گذارد. resolverها آن‌گاه
  می‌توانند DoT (`dot://host:853`)، DoH (`https://host/dns-query`) یا `auto`، فهرست داخلی
  resolverهای عمومی، هم باشند. امتیاز هر resolver در فایل کش ذخیره می‌شود. توازن، تکرار و MTU
  به‌ازای هر resolver در خود کلاینت MasterDnsVPN آن‌گاه روی کل مجموعه اعمال می‌شود، پس مجموعه‌ای
  از resolverهای با محدودیت‌های متفاوت MTU کوچک‌ترین را می‌گیرد؛ بدون `smart_pool` کلاینت
  همهٔ این‌ها را خودش انجام می‌دهد، فقط روی resolverهای سادهٔ UDP.
- **درون تونل.** هر اتصال یک stream است با تحویل مطمئن خودش (ARQ: تأیید، ارسال دوباره، پنجره‌ای
  به اندازهٔ `arq_window` بسته). پیام‌های کنترلی با هم بسته‌بندی می‌شوند و داده‌ها می‌توانند
  فشرده شوند (`upload_compression`، `download_compression`).
- **مقصد.** در حالت `socks5` (پیش‌فرض سرور) سرور به نشانی هر اتصال وصل می‌شود، پس خروجی به
  تنهایی هر اتصال TCP را می‌برد. در حالت `tcp` سرور هر اتصال را به همان یک مقصدی می‌فرستد که
  برایش تنظیم شده و مقصد اتصال نادیده گرفته می‌شود؛ خروجی متناسب (مثلاً `socks` یا `ssh`) را
  با `detour` جلوی آن بگذارید. سرور MasterDnsVPN اتصال به نشانی‌های خصوصی و loopback را رد
  می‌کند.

فقط TCP. ترافیک UDP مسیریابی‌شده از این خروجی استفاده نمی‌کند؛ `udp_over_tcp` برای سرورهایی که
آن را پشتیبانی می‌کنند UDP را روی یک stream می‌برد.

## پیکربندی

```json
{
  "type": "masterdns",
  "tag": "masterdns-out",
  "domains": ["v.example.com"],
  "resolvers": ["8.8.8.8", "1.1.1.1", "9.9.9.9:53"],
  "encryption": "xor",
  "key": "<the server's encrypt_key.txt>"
}
```

| فیلد | نوع | پیش‌فرض | معنی |
|---|---|---|---|
| `domains` | list of strings | الزامی | دامنه‌های تونل که سرور مرجع آن‌هاست، همان `DOMAIN` سرور. همه باید متعلق به یک سرور باشند. |
| `resolvers` | list of strings | الزامی | resolverهای سادهٔ DNS: `"8.8.8.8"`، `"1.1.1.1:5353"`، `"10.0.0.0/30"`، `"10.0.0.0/30:5353"` یا `"[2001:db8::1]:53"`. یک بازه همهٔ نشانی‌های درونش را اضافه می‌کند. با `smart_pool` (بدون بازه): `"dot://host:853"`، `"https://host/dns-query"` و `"auto"` هم. |
| `encryption` | string | `"xor"` | `DATA_ENCRYPTION_METHOD` سرور: `none`، `xor`، `chacha20`، `aes-128-gcm`، `aes-192-gcm` یا `aes-256-gcm`، یا شمارهٔ آن از ۰ تا ۵. |
| `key` | string | الزامی مگر با `none` | کلید سرور، محتوای `encrypt_key.txt` آن. |
| `mode` | string | `"socks5"` | `PROTOCOL_TYPE` سرور: `socks5` یا `tcp`، چنان‌که بالا گفته شد. |
| `smart_pool` | bool یا object | `false` | مجموعهٔ resolver خود خروجی را اجرا کن، چنان‌که بالا گفته شد: `true`، یا یک شیء با `load_balance`، `deadline`، `per_attempt`، `probe_interval` و `down_after` ([مجموعهٔ هوشمند resolver](../dns/smart-dns-pool.md) را ببینید). برای resolverهای DoT، DoH و `auto` لازم است. |
| `pretest_domain` | string | `"www.google.com"` | با `smart_pool`: نامی که برای بررسی پاسخ دادن resolver پرسیده می‌شود. |
| `pretest_record_type` | string | `"a"` | با `smart_pool`: نوع رکورد آن پرسش: `a`، `aaaa`، `cname`، `mx`، `ns`، `ptr`، `soa`، `srv` یا `txt`. |
| `balancing` | string | `"round-robin"` | انتخاب resolver هر پرسش: `random`، `round-robin`، `least-loss`، `lowest-latency`، `hybrid`، `loss-then-latency`، `least-loss-top-random` یا `least-loss-top-round-robin`، یا شمارهٔ ۱ تا ۸ از `RESOLVER_BALANCING_STRATEGY`. `least-loss` برای لینک‌های پرافت با resolverهای زیاد مناسب است. |
| `packet_duplication` | int | `2` | هر بسته چند بار، از resolverهای متفاوت، فرستاده شود (۱ تا ۱۰). بیشتر یعنی مطمئن‌تر و پرمصرف‌تر. |
| `setup_packet_duplication` | int | `2` | همان برای بسته‌هایی که اتصال را باز می‌کنند (تا ۱۲). |
| `upload_compression` | string | `"off"` | `off`، `zstd`، `lz4` یا `zlib`. |
| `download_compression` | string | `"off"` | `off`، `zstd`، `lz4` یا `zlib`. |
| `base_encode` | bool | `false` | درخواست پاسخ base64، برای resolverهایی که رکوردهای باینری را خراب می‌کنند. |
| `min_upload_mtu` | int | `38` | کوچک‌ترین MTU آپلود پذیرفتنی، به بایت. |
| `max_upload_mtu` | int | `150` | بزرگ‌ترین MTU آپلود آزمایش‌شده. |
| `min_download_mtu` | int | `100` | کوچک‌ترین MTU دانلود پذیرفتنی. |
| `max_download_mtu` | int | `500` | بزرگ‌ترین MTU دانلود آزمایش‌شده. resolverهایی که پاسخ‌های بزرگ را عبور می‌دهند بیشتر را ممکن می‌کنند. |
| `mtu_test_timeout` | duration | `2s` | بیشترین زمان یک کاوش MTU. |
| `mtu_test_retries` | int | `2` | هر کاوش چند بار فرستاده شود. |
| `mtu_test_parallelism` | int | `16` | چند resolver هم‌زمان آزمایش شوند. |
| `auto_remove_low_mtu_resolvers` | bool | `true` | چند resolver را که MTU مشترک را پایین می‌کشند کنار بگذار. |
| `recheck_inactive_resolvers` | bool | `true` | resolverهای ناموفق را در پس‌زمینه دوباره آزمایش کن. |
| `auto_disable_timeout_resolvers` | bool | `true` | resolverی را که فقط timeout می‌دهد کنار بگذار. |
| `workers` | int | `4` | کارگرهای خواندن و نوشتن UDP. |
| `process_workers` | int | از روی دستگاه | پردازنده‌های بسته. |
| `arq_window` | int | `600` | پنجرهٔ تحویل مطمئن، به بسته. |
| `ready_timeout` | duration | `30s` | یک اتصال چقدر منتظر آماده شدن تونل بماند تا ناموفق شود. |
| `connect_timeout` | duration | `30s` | یک اتصال چقدر منتظر رسیدن سرور به مقصد بماند. |
| `log_level` | string | `"info"` | سطح پیام‌های خود کلاینت MasterDnsVPN: `debug`، `info`، `warn` یا `error`. در لاگ sing-box دیده می‌شوند. |
| `udp_over_tcp` | object | | تنظیم UDP over TCP از sing-box، برای سروری که آن را پایان می‌دهد. |

سوکت‌هایی که پرسش‌های DNS را می‌فرستند از تنظیمات سوکت خروجی مثل `bind_interface` و
`routing_mark` و از حفاظت سوکت پلتفرم استفاده می‌کنند، پس روی VPN پرسش‌ها به درون تونل
برنمی‌گردند. `detour` پشتیبانی نمی‌شود: پرسش‌ها مستقیم بیرون می‌روند و لاگ هشدار می‌دهد.

هر تنظیم دیگر کلاینت MasterDnsVPN پیش‌فرض پیکربندی نمونهٔ آن را نگه می‌دارد. یابندهٔ resolver
خود کلاینت (`client_resolvers.txt` با بازه‌ها) جایش را به `resolvers` می‌دهد. ray2sing در هستهٔ
هیدیفای دو لینک را به این خروجی می‌خواند: `masterdns://` که همین فیلدها را می‌برد، و نشانی
`dnst://` از مشخصات dnst URL (`dnst://v.example.com/masterdns/socks?mkey=…&encryption=5`) که در آن
backend `socks` همین خروجی به‌تنهایی است و هر backend دیگر `mode: tcp` را با آن خروجی در جلو
می‌گذارد. لینک پروفایل `masterdns://` برنامهٔ WhiteDNS (JSON با base64url، schema
`whitedns.profile`) را هم می‌خواند. لینک `smart_pool` را روشن می‌کند مگر `smart_pool=0` بگوید یا
بازهٔ نشانی داشته باشد، و لینک بی resolver (لینک `dnst://` هیچ resolverی نام نمی‌برد) `auto` را از
راه مجموعه به کار می‌برد، و بی مجموعه فهرستی از resolverهای عمومی شناخته‌شده را.

## نکته‌ها

- با resolverهای زیاد شروع طولانی‌تر می‌شود، چون اول MTU همهٔ آن‌ها آزمایش می‌شود. فهرستی از
  resolverهای قبول‌شده نگه دارید و بهترین‌ها را اول بگذارید.
- کلید و روش رمزگذاری باید دقیقاً با سرور یکی باشند، وگرنه سرور همهٔ بسته‌ها را می‌اندازد و
  کلاینت هرگز آماده نمی‌شود.
- لینک‌هایی که دامنهٔ تونل را دارند فقط با افراد مورد اعتماد به اشتراک بگذارید: دامنهٔ
  منتشرشده ظرف چند ساعت مسدود می‌شود.

## همچنین ببینید

- [DNSTT](dnstt.md)
- [مجموعهٔ هوشمند resolver](../dns/smart-dns-pool.md)
- [پایش](../groups/monitoring.md)
- [جایگزین](../groups/fallback.md)
