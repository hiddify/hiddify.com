---
title: آموزش کار با نرم‌افزار Streisand
---

<div dir="rtl" markdown="1">

# آموزش کار با نرم‌افزار Streisand

در این صفحه یاد می‌گیرید چطور لینک اشتراک هیدیفای‌منیجر خود را به برنامه رایگان **Streisand** (استرایسند) در آیفون و آیپد اضافه کنید، کانفیگ‌ها را تست کنید و از تنظیمات مهم آن، یعنی DNS و فرگمنت TLS، استفاده کنید. استرایسند روی iOS 14 و بالاتر کار می‌کند.

<div class="hi-get"><img class="ico" src="/assets/logos/apps/streisand.webp" alt="Streisand"><div class="meta"><b>Streisand</b><small><span>v1.7.1</span><span>iOS 15+</span><span>رایگان</span><span>آبان ۱۴۰۵</span></small></div><div class="stores"><a class="hi-store" href="https://apps.apple.com/us/app/streisand/id6450534064"><img src="/assets/logos/apple-white.svg" alt=""><span><small>Download on the</small><b>App Store</b></span></a></div></div>
<a class="hi-alt" href="/fa/app/How-to-install-Hiddify-app/"><span class="mk"><img src="/assets/logos/hiddify-mark-white.svg" alt=""></span><span><b>پیشنهاد ما: اپ هیدیفای</b><small>رایگان، ساده‌تر و با پشتیبانی از همهٔ پروتکل‌های هیدیفای‌منیجر</small></span><span class="go">نصب اپ ←</span></a>

## پیش از شروع

- برنامه **Streisand** را از [App Store](https://apps.apple.com/us/app/streisand/id6450534064) نصب کنید. رایگان است.
- **لینک صفحه کاربری** خود را آماده داشته باشید. این همان لینکی است که مدیر سرور برایتان فرستاده و صفحه شخصی هیدیفای‌منیجر شما را باز می‌کند.

**لینک اشتراک** (سابسکریپشن) یک لینک است که همه تنظیمات اتصال (کانفیگ‌ها) را در خود دارد. **کانفیگ** یعنی تنظیمات یک اتصال به سرور. استرایسند می‌تواند بعداً لینک اشتراک را به‌روز کند و کانفیگ‌های جدید را از سرور بگیرد.

!!! note
    تصویرهای صفحهٔ کاربری تازه‌اند (هیدیفای‌منیجر ۱۴.۵). تصویرهای خود برنامه از نسخه‌های قدیمی‌ترند؛ صفحه‌های فعلی کمی فرق دارند، ولی مراحل همین است. صفحه‌های فعلی کمی فرق دارند، ولی مراحل همین است.

## افزودن لینک اشتراک: روش سریع

1. در آیفون، لینک صفحه کاربری خود را در Safari باز کنید.
2. روی دکمه گرد بزرگ وسط صفحه بزنید. پنجره «VPN خود را پیکربندی کنید» باز می‌شود.
3. در بخش «یکی از برنامه‌های زیر را انتخاب کنید»، روی **Streisand** بزنید. اگر آن را نمی‌بینید، «بیشتر...» را بزنید. از همین‌جا می‌توانید برنامه را دانلود هم بکنید.

    <img width=300 alt="Streisand در صفحهٔ کاربری" src="/assets/manager/Tutorial-for-Streisand/fa-user-app.webp" style="display:block;margin:0 auto">

4. «وارد کردن در برنامه» را بزنید. استرایسند باز می‌شود و لینک اشتراک را اضافه می‌کند.

اگر این روش کار نکرد، طبق مراحل زیر لینک را دستی اضافه کنید.

## افزودن لینک اشتراک به‌صورت دستی

ابتدا لینک را بگیرید:

1. در صفحه کاربری، منو را باز کنید و «همه تنظیمات» (**All Configs**) را بزنید.
2. در بخش «لینک‌های اشتراک»، ردیف **Subscription link** را پیدا کنید و «دریافت لینک» را بزنید. پنجره‌ای با QR code و دکمه «کپی لینک» باز می‌شود.

<div align=center markdown=1>
<img width=300 alt="«همهٔ تنظیمات» در صفحهٔ کاربری" src="/assets/manager/Tutorial-for-Streisand/fa-user-configs.webp" style="display:block;margin:0 auto">
</div>

سپس آن را به یکی از دو روش زیر به استرایسند اضافه کنید.

### کپی کردن لینک

1. «کپی لینک» را بزنید.

    <img style="display:block;margin:0 auto" width=30% alt="کپی لینک" src="/assets/manager/Tutorial-for-Streisand/gh-b8a76e41-4db4-45ac-be27-856f6ec9182e.webp" />

2. استرایسند را باز کنید و دکمه `+` را بزنید. استرایسند لینک را از کلیپ‌بورد می‌خواند، لینک اشتراک را اضافه می‌کند و کانفیگ‌ها را بارگذاری می‌کند.

    <img style="display:block;margin:0 auto" width=30% alt="دکمه + در استرایسند" src="/assets/manager/Tutorial-for-Streisand/gh-78fe4b65-d7f7-4d16-b185-82f8dd67a135.webp" />

### اسکن QR code

این روش برای وقتی است که صفحه کاربری روی صفحه دیگری، مثلاً کامپیوتر، باز است.

1. QR code لینک اشتراک را روی صفحه دیگر نمایش دهید.

    <img style="display:block;margin:0 auto" width=30% alt="QR code لینک اشتراک" src="/assets/manager/Tutorial-for-Streisand/gh-fe4de484-3136-4531-8292-c961e26d838e.webp" />

2. در استرایسند `+` و سپس **Scan QRCode** را بزنید و دوربین را روی QR code بگیرید. لینک اشتراک اضافه و کانفیگ‌ها بارگذاری می‌شوند.

    <img style="display:block;margin:0 auto" width=30% alt="گزینه Scan QRCode در استرایسند" src="/assets/manager/Tutorial-for-Streisand/gh-58c97e17-3cfa-4c40-9b2d-01de70b1e40d.webp" />

## تست، به‌روزرسانی و مدیریت لینک اشتراک

انگشت خود را روی لینک اشتراک در استرایسند نگه دارید. منویی با این گزینه‌ها باز می‌شود:

<div align=center markdown=1>
<img width=30% alt="منوی لینک اشتراک در استرایسند" src="/assets/manager/Tutorial-for-Streisand/gh-52954cdf-5c76-4fbe-8adb-8371d7fa6747.webp" />
</div>

- **Latency**: هر کانفیگ را با یک اتصال واقعی تست می‌کند. این مفیدترین تست است. هرچه عدد کمتر، بهتر.
- **TCP Ping**: فقط بررسی می‌کند که پورت سرور جواب می‌دهد. سریع است، ولی ممکن است کانفیگی این تست را رد کند و باز هم کار نکند.
- **ICMP Ping**: پینگ معمولی به سرور. خیلی از سرورها به آن جواب نمی‌دهند، پس رد شدن آن به این معنی نیست که کانفیگ خراب است.
- **Update**: آخرین کانفیگ‌ها را از سرور می‌گیرد. هر وقت مدیر چیزی را تغییر داد یا کانفیگ‌ها از کار افتادند، این را بزنید.
- **Edit**: نام یا لینک اشتراک را تغییر می‌دهد.
- **Delete**: لینک اشتراک و کانفیگ‌هایش را حذف می‌کند.

برای اتصال، روی کانفیگی که نتیجه تست خوبی داشته بزنید و سپس کلید صفحه اصلی را روشن کنید. بار اول، iOS برای افزودن پیکربندی VPN اجازه می‌خواهد؛ **Allow** را بزنید.

## تنظیمات DNS

در صفحه اصلی، تنظیمات DNS را باز کنید. اینجا انتخاب می‌کنید استرایسند برای پیدا کردن آدرس سایت‌ها از کدام سرور DNS و به چه روشی استفاده کند:

<div align=center markdown=1>
<img width=30% alt="تنظیمات DNS در استرایسند" src="/assets/manager/Tutorial-for-Streisand/gh-152bbbd5-a8a5-4a31-836a-7c2ea7ab3940.webp" />
</div>

- **DoH** (DNS روی HTTPS): درخواست‌های DNS رمزنگاری می‌شوند و شبیه ترافیک معمولی وب هستند. معمولاً بهترین انتخاب است.
- **DoT** (DNS روی TLS): درخواست‌های DNS با TLS رمزنگاری می‌شوند، روی یک پورت جداگانه (۸۵۳). مسدود کردن آن از DoH ساده‌تر است.
- **DoU** (DNS روی UDP): همان DNS معمولی و بدون رمزنگاری. اپراتور اینترنت می‌تواند آن را ببیند و تغییر دهد؛ فقط وقتی از آن استفاده کنید که بقیه کار نکنند.

## تنظیمات برنامه

صفحه **Settings** تنظیمات کلی برنامه را دارد:

<div align=center markdown=1>
<img width=30% alt="صفحه Settings در استرایسند" src="/assets/manager/Tutorial-for-Streisand/gh-989d8fce-4858-4bd1-b5fb-44c4bdac3895.webp" />
</div>

- **Import Configuration**: یک فایل تنظیمات استرایسند را از دستگاه بارگذاری می‌کند.
- **Export Configuration**: تنظیمات استرایسند را در یک فایل ذخیره می‌کند، مثلاً برای انتقال به دستگاه دیگر.
- **Subscription**: گزینه **Update On Open** را روشن کنید تا هر بار که برنامه را باز می‌کنید، لینک‌های اشتراک به‌روز شوند.

    <img style="display:block;margin:0 auto" width=30% alt="گزینه Update On Open" src="/assets/manager/Tutorial-for-Streisand/gh-068a0d24-c0f5-4cfd-9fa0-e37eb50acf20.webp" />

- **Reset**: تنظیمات برنامه را به حالت پیش‌فرض برمی‌گرداند.

    <img style="display:block;margin:0 auto" width=30% alt="گزینه Reset" src="/assets/manager/Tutorial-for-Streisand/gh-8b336b0b-0c57-49e7-89e4-f86317955061.webp" />

## فعال‌سازی فرگمنت TLS

**فرگمنت** اولین بسته اتصال TLS را به تکه‌های کوچک تقسیم می‌کند تا فیلتر نتواند نام سایت را در آن به‌راحتی بخواند. وقتی کانفیگ‌های TLS وصل نمی‌شوند، ممکن است کمک کند. برای اطلاعات بیشتر، [ترفند TLS چطور کار می‌کند](/fa/manager/basic-concepts-and-troubleshooting/How-the-TLS-Trick-works-and-its-usage/) را ببینید.

1. روی کانفیگ بزنید تا تنظیماتش باز شود.
2. گزینه **Fragment** را روشن کنید.
3. این مقادیر را به‌عنوان نقطه شروع وارد کنید:

    ```
    packets: tlshello
    length: 100-200
    interval: 10-20
    ```

<div align=center markdown=1>
<img src="/assets/manager/Tutorial-for-Streisand/gh-055f8437-0bfa-45ce-96e4-f7cbd0026c4c.webp" width="30%" alt="تنظیمات فرگمنت" />
</div>

بهترین مقادیر به اپراتور اینترنت شما بستگی دارد. اگر کمکی نکرد، طول‌ها و فاصله‌های دیگر را امتحان کنید، یا **packets** را به‌جای `tlshello` روی `1-3` (سه بخش اول TCP) بگذارید. حالت `1-3` ممکن است زودتر توسط فیلتر شناسایی شود.

## مقاله‌های مرتبط

<div class="hi-related" markdown="1">

- [sing-box](/fa/manager/client-software-on-ios/Tutorial-for-SingBox-app/)
- [V2Box](/fa/manager/client-software-on-ios/Tutorial-for-V2Box-app/)
- [FoXray](/fa/manager/client-software-on-ios/Tutorial-for-FoXray-app/)
- [Shadowrocket](/fa/manager/client-software-on-ios/Tutorial-for-ShadowRocket-app/)

</div>

</div>
