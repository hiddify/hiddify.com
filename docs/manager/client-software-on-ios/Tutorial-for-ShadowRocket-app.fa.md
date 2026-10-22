---
title: آموزش کار با نرم‌افزار ShadowRocket شدوراکت

---


<div dir="rtl" markdown="1">

# آموزش کار با نرم‌افزار ShadowRocket شدوراکت

در این صفحه یاد می‌گیرید چطور لینک اشتراک هیدیفای خود را به برنامه **Shadowrocket** (شدوراکت) در آیفون و آیپد اضافه کنید و از تنظیمات مهم آن استفاده کنید. شدوراکت یک برنامه پولی است که با کانفیگ‌های مبتنی بر Xray کار می‌کند.

!!! tip "پیشنهاد ما: Hiddify App"
    ساده‌ترین برنامه برای سرور هیدیفای، برنامه رایگان **Hiddify App** است. آن را از [App Store](https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532) نصب کنید. راهنما: [نصب Hiddify App](/fa/app/How-to-install-Hiddify-app/).

## پیش از شروع

- برنامه **Shadowrocket** را از [App Store](https://apps.apple.com/us/app/shadowrocket/id932747118) بخرید و نصب کنید.
- **لینک صفحه کاربری** خود را آماده داشته باشید. این همان لینکی است که مدیر سرور برایتان فرستاده و صفحه شخصی هیدیفای شما را باز می‌کند.

**لینک اشتراک** (سابسکریپشن) یک لینک است که همه تنظیمات اتصال (کانفیگ‌ها) را در خود دارد. شدوراکت می‌تواند بعداً آن را به‌روز کند و تنظیمات جدید را از سرور بگیرد.

## افزودن لینک اشتراک: روش سریع

1. در آیفون، لینک صفحه کاربری خود را در Safari باز کنید.
2. روی دکمه گرد بزرگ وسط صفحه بزنید. پنجره «VPN خود را پیکربندی کنید» باز می‌شود.
3. در بخش «یکی از برنامه‌های زیر را انتخاب کنید»، روی **Shadowrocket** بزنید. اگر آن را نمی‌بینید، «بیشتر...» را بزنید. از همین‌جا می‌توانید برنامه را دانلود هم بکنید.
4. «وارد کردن در برنامه» را بزنید. شدوراکت باز می‌شود و لینک اشتراک را اضافه می‌کند.

اگر این روش کار نکرد، طبق مراحل زیر لینک را دستی اضافه کنید.

!!! note "کانفیگ‌های Lite و Normal دیگر وجود ندارند"
    در نسخه‌های قدیمی صفحه کاربری، در تب **آی‌اواس** دو نوع کانفیگ بود: **Lite** (فقط سایت‌های فیلترشده از VPN عبور می‌کنند) و **Normal** (همه ترافیک از VPN عبور می‌کند). صفحه کاربری فعلی تب iOS و انتخاب Lite/Normal ندارد. اگر می‌خواهید سایت‌های ایرانی بدون VPN باز شوند، از مدیر سرور بپرسید؛ این مورد روی سرور تنظیم می‌شود. اگر مدیر، [وارپ](/fa/manager/configuration-and-advanced-settings/How-to-activate-WARP-on-the-Hiddify-panel/) را فعال کرده باشد، سایت‌های ایرانی می‌توانند از طریق وارپ باز شوند.

<div align=center markdown=1>
<img width=30% alt="بخش شدوراکت در نسخه قدیمی صفحه کاربری" src="https://github.com/hiddify/hiddify-config/assets/125398461/c4eb7d80-2685-4288-8d9b-c643d3886cad" />
</div>

<div align=center markdown=1>
<img width=30% alt="لینک دانلود برنامه در نسخه قدیمی صفحه کاربری" src="https://github.com/hiddify/hiddify-config/assets/125398461/ac45f39c-b582-4357-9162-e46287c4fd58" />
</div>

<div align=center markdown=1>
<img width=30% alt="کانفیگ‌های Lite و Normal در نسخه قدیمی صفحه کاربری" src="https://github.com/hiddify/hiddify-config/assets/125398461/eb7a87ce-3e0f-4825-8401-ffe0747328e8" />
</div>

## افزودن لینک اشتراک به‌صورت دستی

ابتدا لینک را بگیرید:

1. در صفحه کاربری، منو را باز کنید و «همه تنظیمات» (**All Configs**) را بزنید.
2. در بخش «لینک‌های اشتراک»، ردیف **Subscription link** را پیدا کنید و «دریافت لینک» را بزنید. پنجره‌ای با QR code و دکمه «کپی لینک» باز می‌شود.

سپس آن را به یکی از دو روش زیر به شدوراکت اضافه کنید.

### کپی کردن لینک در شدوراکت

1. «کپی لینک» را بزنید.
2. شدوراکت را باز کنید و دکمه `+` را در گوشه بالا سمت راست بزنید.

    <div align=center markdown=1>
    <img width=30% alt="دکمه + در شدوراکت" src="https://github.com/hiddify/hiddify-config/assets/125398461/d116347f-31bc-4ca9-a1fc-bdb9364e5e74" />
    </div>

3. `Type` را روی `Subscribe` بگذارید.
4. لینک را در فیلد `URL` بچسبانید.
5. `Save` را بزنید.

    <div align=center markdown=1>
    <img width=30% alt="Type روی Subscribe و فیلد URL" src="https://github.com/hiddify/hiddify-config/assets/125398461/c087970e-aebc-479d-8b8a-bc54a78cc7f8" />
    </div>

همه کانفیگ‌ها در برنامه بارگذاری می‌شوند.

### اسکن QR code در شدوراکت

1. در صفحه اصلی شدوراکت، دکمه اسکنر را بزنید.

    <div align=center markdown=1>
    <img width=30% alt="دکمه اسکنر" src="https://github.com/hiddify/hiddify-config/assets/125398461/cee3abfe-db05-4e2c-925d-fa57010d3465" />
    </div>

2. QR code صفحه کاربری را اسکن کنید. کانفیگ‌ها به برنامه اضافه می‌شوند.

## تست کانفیگ‌ها

در صفحه اصلی برنامه، `Connectivity Test` را بزنید. برنامه همه کانفیگ‌ها را تست می‌کند.

<div align=center markdown=1>
<img width=30% alt="Connectivity Test" src="https://github.com/hiddify/hiddify-config/assets/125398461/49a37a3c-b1f7-48ba-91e2-0a4ac7dc3e5f" />
</div>

برای نتیجه واقعی‌تر:

1. از منوی پایین `Settings` را بزنید.
2. `Test Method` را روی `Connect` بگذارید.
3. دوباره تست بگیرید.

<div align=center markdown=1><img width=30% alt="Test Method روی Connect" src="https://github.com/hiddify/hiddify-config/assets/125398461/8760fd19-9056-4c0c-a4a0-aeebd728656f" />
</div>


## به‌روزرسانی لینک اشتراک و کانفیگ‌ها

روی نماد به‌روزرسانی بالای کانفیگ‌های هر لینک اشتراک بزنید. کانفیگ‌ها با آخرین اطلاعات سرور به‌روز می‌شوند.

<div align=center markdown=1>
<img width=30% alt="نماد به‌روزرسانی بالای کانفیگ‌ها" src="https://github.com/hiddify/hiddify-config/assets/125398461/0878e805-a24e-4f19-831a-f526b475db4a" />
</div>


## تنظیمات لینک اشتراک

به `Settings` بروید و پایین صفحه `Subscribe` را بزنید. در اینجا این موارد را می‌توانید تنظیم کنید:

### به‌روزرسانی هنگام باز شدن برنامه

گزینه `Update on Open` را روشن کنید.

<div align=center markdown=1>
<img width=30% alt="Update on Open" src="https://github.com/hiddify/hiddify-config/assets/125398461/aeb08d16-20d3-424e-8c6d-7d13f06aeb8d" />
</div>

### به‌روزرسانی خودکار در پس‌زمینه

گزینه `Auto Background Update` را روشن کنید. برنامه در فاصله‌های زمانی مشخص لینک‌های اشتراک را به‌روز می‌کند.

<div align=center markdown=1>
<img width=30% alt="Auto Background Update" src="https://github.com/hiddify/hiddify-config/assets/125398461/97540ef0-399f-4260-85a1-af0c0594533b" />
</div>

### مرتب‌سازی بر اساس پینگ

گزینه `Sort by ping` را روشن کنید تا کانفیگ‌ها بر اساس نتیجه تست مرتب شوند و بهترین‌ها بالا بیایند.

<div align=center markdown=1>
<img width=30% alt="Sort by ping" src="https://github.com/hiddify/hiddify-config/assets/125398461/afeb9a4d-a12f-49f1-aca7-f5eae5c6bed2" />
</div>


## جلوگیری از نشت IP

**نشت IP** یعنی سایت‌ها با وجود روشن بودن VPN، IP واقعی شما را ببینند.

1. به `Settings` و سپس بخش `UDP` بروید.
2. گزینه `Disable STUN` را روشن کنید.

<div align=center markdown=1>
<img width=30% alt="Disable STUN" src="https://github.com/hiddify/hiddify-config/assets/125398461/3bd81556-4119-4659-8db7-0826bbdbd6ee" />
</div>


## رفع مشکل پخش نشدن صدا در بعضی برنامه‌ها

اگر در بعضی برنامه‌ها (مثلاً Clubhouse) صدا پخش نمی‌شود:

1. به `Settings` و سپس بخش `TCP` بروید.
2. مقدار `Fingerprint` را تغییر دهید.

<div align=center markdown=1>
<img width=30% alt="تنظیم Fingerprint" src="https://github.com/hiddify/hiddify-config/assets/125398461/fe7a7a27-016c-45b9-92b5-2e9427ba165a" />
</div>


## میان‌برها (Shortcuts)

به `Settings` و سپس بخش `Shortcuts` بروید. در اینجا می‌توانید برای یک کار، مثلاً روشن کردن VPN، یک فرمان صوتی تعیین کنید.

## روشن نگه داشتن VPN (On Demand)

به `Settings` و سپس بخش `On Demand` بروید.

<div align=center markdown=1>
<img width=30% alt="تنظیمات On Demand" src="https://github.com/hiddify/hiddify-config/assets/125398461/af641742-dc91-468e-9135-78de911e6703" />
</div>

### Always On
با روشن کردن این گزینه، VPN شما همیشه روشن می‌ماند.

### On Demand
با روشن کردن این گزینه، اگر اتصال شما قطع شود، شدوراکت کل اینترنت را قطع می‌کند تا IP واقعی شما لو نرود.

### Disconnect on Sleep
با روشن کردن این گزینه، وقتی گوشی به حالت خواب (Sleep) می‌رود، VPN قطع می‌شود.

## اشتراک‌گذاری VPN با دستگاه‌های دیگر

می‌توانید VPN خود را با دستگاه دیگری در همان شبکه به اشتراک بگذارید؛ مثلاً دستگاهی که نمی‌توان روی آن برنامه VPN نصب کرد.

1. به `Settings` و سپس بخش `Proxy` بروید.
2. `Proxy Share` را بزنید.
3. گزینه `Enable Share` را روشن کنید. برنامه یک آدرس IP و یک پورت نشان می‌دهد.

    <div align=center markdown=1>
    <img width=30% alt="Proxy Share با IP و پورت" src="https://github.com/hiddify/hiddify-config/assets/125398461/d764b726-6ddd-4a5a-aa76-f9ad8165e4f1" />
    </div>

4. در دستگاه دیگر، تنظیمات پروکسی شبکه را باز کنید و همان IP و پورت را وارد کنید.

اکنون دستگاه دوم بدون نصب هیچ برنامه‌ای از VPN شما استفاده می‌کند.

## ساخت لودبالانس

**لودبالانس** (Load Balance) ترافیک شما را بین چند کانفیگ پخش می‌کند تا اگر یک کانفیگ کند یا مسدود شد، اتصال شما قطع نشود.

1. در صفحه اصلی، انگشت خود را روی صفحه نگه دارید و به پایین بکشید. یک منوی مخفی باز می‌شود.

    <div align=center markdown=1>
    <img width=30% alt="منوی مخفی" src="https://github.com/hiddify/hiddify-config/assets/125398461/59872f56-e9ff-4c50-85a0-65ccd488e704" />
    </div>

2. دکمه `+` را بزنید.

    <div align=center markdown=1>
    <img width=30% alt="دکمه + برای لودبالانس جدید" src="https://github.com/hiddify/hiddify-config/assets/125398461/b67bc883-e643-465c-85dc-e6eeb719723c" />
    </div>

3. یک نام دلخواه بنویسید.
4. `Type` را روی `load-balance` بگذارید.
5. در بخش `Policy`، کانفیگ‌هایی را که پینگ بهتری دارند یا همه کانفیگ‌ها را انتخاب کنید.
6. `Interval` (فاصله بین تست‌ها) و `Timeout` (مدتی که یک کانفیگ می‌تواند قطع باشد و هنوز سالم حساب شود) را روی مقدار پیش‌فرض بگذارید، مگر اینکه دقیقاً بدانید چه می‌خواهید.
7. `Save` را بزنید.

    <div align=center markdown=1>
    <img width=30% alt="تنظیمات لودبالانس" src="https://github.com/hiddify/hiddify-config/assets/125398461/be6e132b-d9d4-45ff-ab8a-94b72d764139" />
    </div>

8. روی لودبالانس ساخته‌شده بزنید و سپس `Test` را بزنید. این کار آن را تست می‌کند و از طریق آن وصل می‌شود.

    <div align=center markdown=1>
    <img width=30% alt="تست لودبالانس" src="https://github.com/hiddify/hiddify-config/assets/125398461/819da751-8a46-4ab3-88e2-00a5e0b3f724" />
    </div>

با روشن یا خاموش کردن شدوراکت، لودبالانس هم روشن یا خاموش می‌شود.

## رفع مشکل باز نشدن بعضی سایت‌ها و برنامه‌ها

اگر بعضی سایت‌ها یا برنامه‌ها باز نمی‌شوند یا گیف‌های تلگرام بارگذاری نمی‌شوند:

1. به منوی `Settings` بروید.
2. بخش `TCP` را باز کنید.
3. `TLS` را روی `Network` بگذارید.
4. `Fingerprint` را روی `Safari15_5` بگذارید.
5. `Max Read Length` را روی `16384` بگذارید.
6. به `Home` برگردید.
7. `Global Routing` را روی `Proxy` بگذارید.

</div>
