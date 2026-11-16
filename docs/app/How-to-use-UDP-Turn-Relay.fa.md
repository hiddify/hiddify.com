---
title: آموزش استفاده از UDP Turn Relay در اپ هیدیفای
---

# آموزش استفاده از UDP Turn Relay

!!! warning "در اپ هیدیفای نسخهٔ ۴ به بعد پشتیبانی نمی‌شود"
    پارامتر `relay=` که در این صفحه توضیح داده شده، فقط در اپ قدیمی هیدیفای ۲.x (Hiddify Next) کار می‌کند. از نسخهٔ ۴.۰ (اسفند ۱۴۰۴)، که هستهٔ اپ به sing-box 1.13 رفت، این پارامتر نادیده گرفته می‌شود و در اپ هیدیفای ۵.۹ هم همین‌طور است: لینکی که `relay=` دارد مستقیم به سرور وصل می‌شود، بدون سرور میانی. این صفحه فقط برای مراجعه نگه داشته شده است.

## این قابلیت چه بود

UDP Turn Relay از سرور TURN یک پیام‌رسان به عنوان سرور میانی (ریلی) استفاده می‌کرد. سرورهای TURN تماس‌های صوتی و تصویری پیام‌رسان‌ها را جابه‌جا می‌کنند. وقتی یک پیام‌رسان داخل شبکهٔ فیلترشده کار می‌کند (یک پیام‌رسان داخلی، یا یک پیام‌رسان خارجی که فیلتر نشده)، سرور TURN آن می‌تواند ترافیک شما را به سرور خودتان برساند. شکل اتصال این‌طور بود:

<div align=center>

<img width=100% alt="شماتیک UDP Turn Relay" src="https://github.com/hiddify/hiddify-next/assets/125398461/f3df43df-daea-437b-9a68-66537574c8e0">

</div>

این روش فقط با کانفیگ‌هایی کار می‌کرد که روی UDP هستند، مثل Hysteria2 و TUIC v5، و با ریالتی یا کانفیگ‌های TCP دیگر کار نمی‌کرد.

## شکل لینک

سرور میانی به شکل پارامتر `relay` که URL-encode شده، به انتهای لینک Hysteria2 یا TUIC اضافه می‌شد:

```
relay=urlencoded(turn://user:pass@host:port?realm=realm)
```

- `user` و `pass`: نام کاربری و رمز سرور TURN پیام‌رسان.
- `host` و `port`: آدرس سرور TURN.
- `realm`: محدودهٔ احراز هویت (realm) سرور TURN.

برای نمونه، `turn://user:pass@turn.example.com:443?realm=example.com` بعد از URL-encode این می‌شود:

```
relay=turn%3A%2F%2Fuser%3Apass%40turn.example.com%3A443%3Frealm%3Dexample.com
```

و با یک `&` قبل از `#` لینک قرار می‌گیرد:

```
hysteria2://password@server.example.com:443?obfs=salamander&obfs-password=secret&sni=www.speedtest.net&insecure=1&relay=turn%3A%2F%2Fuser%3Apass%40turn.example.com%3A443%3Frealm%3Dexample.com#test
```

پیام‌رسان‌ها خیلی زود سرورهای TURN خود را به روی این نوع استفاده می‌بندند؛ پیام‌رسانی که در نمونه‌های اولیه استفاده شده بود (بله) بعد از مدت کوتاهی همین کار را کرد.

## به جای آن از چه استفاده کنیم

برای رسیدن به سرورتان از یک مسیر دیگر با اپ فعلی، [زنجیره، امنیت بیشتر و رفع‌کنندهٔ مسدودیت](Chain-Extra-security-and-Proxy-unblocker.md) (وارپ یا سایفون قبل یا بعد از سرور شما) و در سمت سرور، [سرور میانی](/fa/manager/domain-worker-cdn-and-tunneling/How-to-setup-relay-server-using-Hiddify-Relay-Builder/) را ببینید.

## مقاله‌های مرتبط

- [کار با اپ هیدیفای](How-to-use-Hiddify-app.md): افزودن پروفایل، اتصال و تنظیمات پایه
- [نصب اپ هیدیفای](How-to-install-Hiddify-app.md)
