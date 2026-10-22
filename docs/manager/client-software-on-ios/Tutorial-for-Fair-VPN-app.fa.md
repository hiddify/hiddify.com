---
title: آموزش کار با نرم‌افزار Fair VPN

---

<div dir="rtl" markdown="1">

# آموزش کار با نرم‌افزار Fair VPN

در این صفحه یاد می‌گیرید چطور لینک اشتراک هیدیفای خود را به برنامه رایگان **Fair VPN** در آیفون و آیپد اضافه کنید، کانفیگ‌ها را تست کنید و VPN خود را با دستگاه‌های دیگر به اشتراک بگذارید.

!!! tip "پیشنهاد ما: Hiddify App"
    ساده‌ترین برنامه برای سرور هیدیفای، برنامه رایگان **Hiddify App** است. آن را از [App Store](https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532) نصب کنید. راهنما: [نصب Hiddify App](/fa/app/How-to-install-Hiddify-app/).

## پیش از شروع

- برنامه **Fair VPN** را از [App Store](https://apps.apple.com/us/app/fair-vpn/id1533873488) نصب کنید. این برنامه رایگان است.
- **لینک صفحه کاربری** خود را آماده داشته باشید. این همان لینکی است که مدیر سرور برایتان فرستاده و صفحه شخصی هیدیفای شما را باز می‌کند.

**لینک اشتراک** (سابسکریپشن) یک لینک است که همه تنظیمات اتصال شما را در خود دارد. **کانفیگ** یعنی تنظیمات یک اتصال به سرور.

## دریافت لینک اشتراک

Fair VPN در فهرست برنامه‌های صفحه کاربری هیدیفای نیست؛ بنابراین لینک را دستی اضافه می‌کنید.

1. لینک صفحه کاربری خود را باز کنید.
2. منو را باز کنید و «همه تنظیمات» (**All Configs**) را بزنید.
3. در بخش «لینک‌های اشتراک»، ردیف **Subscription link b64** را پیدا کنید و «دریافت لینک» را بزنید. پنجره کوچکی با یک QR code و دکمه «کپی لینک» باز می‌شود.

<div align=center markdown=1>
<img width=30% alt="لینک اشتراک در نسخه قدیمی صفحه کاربری" src="https://github.com/hiddify/hiddify-config/assets/125398461/1e4b67ca-ad95-43e1-b9d1-76af7e007822" />
</div>

!!! note "نکته"
    تصویرهای صفحه کاربری مربوط به نسخه قدیمی‌تر پنل هستند. ظاهر صفحه فعلی فرق دارد، اما لینک همان است.

حالا می‌توانید لینک را کپی کنید یا QR code آن را اسکن کنید.

## روش ۱: کپی کردن لینک

1. «کپی لینک» را بزنید.

    <div align=center markdown=1>
    <img width=30% alt="دکمه کپی" src="https://github.com/hiddify/hiddify-config/assets/125398461/564d5f43-f2dd-4e0c-a79a-a2042a2db738" />
    </div>

2. برنامه Fair VPN را باز کنید. در تب `VPN` روی `Import VPN Configs` بزنید.

    <div align=center markdown=1>
    <img width=30% alt="Import VPN Configs" src="https://github.com/hiddify/hiddify-config/assets/125398461/3631c51e-15d7-44a6-bda0-c8df0b61c9d0" />
    </div>

3. لینک را بچسبانید و `OK` را بزنید.

    <div align=center markdown=1>
    <img width=30% alt="چسباندن لینک و زدن OK" src="https://github.com/hiddify/hiddify-config/assets/125398461/16c4e038-ab2f-4f01-86d6-8ed147180c93" />
    </div>

بعد از چند ثانیه کانفیگ‌ها به برنامه اضافه می‌شوند.

## روش ۲: اسکن QR code

اگر صفحه کاربری روی صفحه دیگری (مثلاً کامپیوتر) باز است، از این روش استفاده کنید.

1. در Fair VPN، تب `VPN` را باز کنید و از منوی پایین `Add VPN by QR Code` را بزنید.

    <div align=center markdown=1>
    <img width=30% alt="Add VPN by QR Code" src="https://github.com/hiddify/hiddify-config/assets/125398461/1107964d-22ff-4fd8-854c-32c09be13b1e" />
    </div>

2. دوربین گوشی را روی QR code صفحه کاربری بگیرید. کانفیگ‌ها مثل روش ۱ اضافه می‌شوند.

    <div align=center markdown=1>
    <img width=30% alt="اسکن QR code" src="https://github.com/hiddify/hiddify-config/assets/125398461/a6629f69-cdcc-404f-a8e0-f099a58a290c" />
    </div>

## تست کانفیگ‌ها

1. روی `Test VPN Latency` بزنید.
2. روی `Test Web Latency` بزنید.

برنامه از طریق هر کانفیگ یک تست واقعی انجام می‌دهد و نتیجه را کنار آن نشان می‌دهد. **Latency** (تأخیر) مدت زمان رسیدن پاسخ است؛ هرچه کمتر باشد بهتر است.

<div align=center markdown=1>
<img width=30% alt="نتیجه تست کنار هر کانفیگ" src="https://github.com/hiddify/hiddify-config/assets/125398461/322b3680-e908-4a9d-8423-47ef3c50c1ff" />
</div>

## مرتب‌سازی کانفیگ‌ها بر اساس نتیجه تست

1. روی `Test VPN Latency` بزنید.
2. `Sort by Latency` را بزنید.

کانفیگ‌ها بر اساس نتیجه تست مرتب می‌شوند و بهترین‌ها بالا قرار می‌گیرند.

<div align=center markdown=1>
<img width=30% alt="Sort by Latency" src="https://github.com/hiddify/hiddify-config/assets/125398461/04ef4c98-8dde-4da0-b0dd-2250ec32b8c7" />
</div>

## به‌روزرسانی لینک اشتراک

Fair VPN نمی‌تواند لینک اشتراک را خودش به‌روز کند. برای گرفتن آخرین کانفیگ‌ها:

1. `Delete All VPN` را بزنید تا همه کانفیگ‌ها حذف شوند.
2. لینک اشتراک را طبق مراحل بالا دوباره اضافه کنید.

!!! note "اگر مدیر سرور از Auto CDN استفاده می‌کند"
    برای گرفتن IP تمیز جدید، همه کانفیگ‌ها را با `Delete All VPN` حذف کنید. سپس VPN را خاموش کنید، صفحه کاربری را دوباره بارگذاری کنید و لینک اشتراک را دوباره اضافه کنید.

<div align=center markdown=1>
<img width=30% alt="Delete All VPN" src="https://github.com/hiddify/hiddify-config/assets/125398461/6aef8018-ee10-414f-b889-f1dde61bdbe9" />
</div>

## اشتراک‌گذاری VPN با دستگاه‌های دیگر

می‌توانید VPN گوشی خود را با دستگاه دیگری که به همان Wi-Fi وصل است به اشتراک بگذارید؛ مثلاً دستگاهی که نمی‌توان روی آن برنامه VPN نصب کرد.

1. در Fair VPN، گزینه `Local Sharing` را روشن کنید. برنامه یک آدرس IP و یک پورت نشان می‌دهد.

    <div align=center markdown=1>
    <img width=30% alt="پیام Local Sharing با IP و پورت" src="https://github.com/hiddify/hiddify-config/assets/125398461/781db733-df3f-4190-baaa-5dd4dc529727" />
    </div>

2. در دستگاه دوم، **تنظیمات پروکسی** شبکه را باز کنید.
3. آدرس IP و پورتی را که Fair VPN نشان داده وارد و ذخیره کنید.

اکنون دستگاه دوم از اتصال VPN گوشی شما استفاده می‌کند.

</div>
