---
title: آموزش کار با نرم‌افزار Stash
---

<div dir="rtl" markdown="1">

# آموزش کار با نرم‌افزار Stash

در این صفحه یاد می‌گیرید چطور پروفایل هیدیفای خود را به برنامه **Stash** در آیفون و آیپد اضافه کنید و از حالت‌های اصلی آن استفاده کنید. Stash یک برنامه پولی بر پایه کلش (Clash) است.

!!! tip "پیشنهاد ما: Hiddify App"
    ساده‌ترین برنامه برای سرور هیدیفای، برنامه رایگان **Hiddify App** است. آن را از [App Store](https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532) نصب کنید. راهنما: [نصب Hiddify App](/fa/app/How-to-install-Hiddify-app/).

## پیش از شروع

- برنامه **Stash** را از [App Store](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349) بخرید و نصب کنید. طبق App Store به iOS 16 یا بالاتر نیاز دارد.
- **لینک صفحه کاربری** خود را آماده داشته باشید. این همان لینکی است که مدیر سرور برایتان فرستاده و صفحه شخصی هیدیفای شما را باز می‌کند.

در Stash، **پروفایل** یک فایل (با فرمت YAML) است که همه کانکشن‌ها (کانفیگ‌ها) و قوانین عبور ترافیک از VPN را در خود دارد.

## افزودن پروفایل: روش سریع

1. در آیفون، لینک صفحه کاربری خود را در Safari باز کنید.
2. روی دکمه گرد بزرگ وسط صفحه بزنید. پنجره «VPN خود را پیکربندی کنید» باز می‌شود.
3. در بخش «یکی از برنامه‌های زیر را انتخاب کنید»، روی **Stash** بزنید. اگر آن را نمی‌بینید، «بیشتر...» را بزنید. از همین‌جا می‌توانید برنامه را دانلود هم بکنید.
4. «وارد کردن در برنامه» را بزنید. Stash باز می‌شود و پروفایل را اضافه می‌کند.

اگر این روش کار نکرد، طبق مراحل زیر پروفایل را دستی اضافه کنید.

!!! note "پروفایل‌های Lite و Normal دیگر وجود ندارند"
    در نسخه‌های قدیمی صفحه کاربری، تب **آی‌اواس** دو پروفایل برای Stash داشت: پروفایل سبز **Lite** (فقط سایت‌های فیلترشده از VPN عبور می‌کنند) و پروفایل نارنجی **Normal** (همه ترافیک از VPN عبور می‌کند). پنل فعلی به جای آن‌ها یک لینک اشتراک **Clash Meta** ارائه می‌دهد. اگر می‌خواهید سایت‌های ایرانی بدون VPN باز شوند، از مدیر سرور بپرسید؛ این مورد روی سرور تنظیم می‌شود.

<div align=center markdown=1>
<img width=30% alt="بخش Stash در نسخه قدیمی صفحه کاربری" src="https://github.com/hiddify/hiddify-config/assets/125398461/77e91556-27a9-47a8-8c90-8099285a571f" />
</div>

<div align=center markdown=1>
<img width=30% alt="پروفایل‌های Lite و Normal در نسخه قدیمی صفحه کاربری" src="https://github.com/hiddify/hiddify-config/assets/125398461/9ae75a32-1700-466c-872b-393edb870462" />
</div>

## افزودن پروفایل به‌صورت دستی

ابتدا لینک را بگیرید:

1. در صفحه کاربری، منو را باز کنید و «همه تنظیمات» (**All Configs**) را بزنید.
2. در بخش «لینک‌های اشتراک»، ردیف **Clash Meta** را پیدا کنید و «دریافت لینک» را بزنید. پنجره‌ای با QR code و دکمه «کپی لینک» باز می‌شود.

### کپی کردن لینک در Stash

1. «کپی لینک» را بزنید.
2. برنامه Stash را باز کنید. در صفحه `Settings` روی `Config File` بزنید.
3. `Download from URL` را بزنید.

    <div align=center markdown=1>
    <img width=30% alt="Download from URL" src="https://github.com/hiddify/hiddify-config/assets/125398461/ffbbd7a4-96aa-4331-9987-09f13f46edc8" />
    </div>

4. لینک را بچسبانید و `Download` را بزنید. پروفایل به برنامه اضافه می‌شود.

    <div align=center markdown=1>
    <img width=30% alt="چسباندن لینک و زدن Download" src="https://github.com/hiddify/hiddify-config/assets/125398461/84e1e1da-2d09-4b59-ac88-91412746e4ee" />
    </div>

### افزودن پروفایل با QR code

1. QR code صفحه کاربری را روی صفحه نگه دارید (مثلاً روی کامپیوتر).
2. برنامه Stash را باز کنید. در صفحه `Settings` روی `Config File` بزنید.
3. `Download from QRcode` را بزنید.

    <div align=center markdown=1>
    <img width=30% alt="Download from QRcode" src="https://github.com/hiddify/hiddify-config/assets/125398461/02ca1ecf-3552-4c8e-9a2f-625be8c8b7ac" />
    </div>

4. QR code را اسکن کنید. پروفایل به برنامه اضافه می‌شود.

## منوی Policy

این منو پالیسی‌ها، یعنی کانفیگ‌های پروفایل‌هایی را که وارد کرده‌اید، نشان می‌دهد.

<div align=center markdown=1>
<img width=30% alt="منوی Policy" src="https://github.com/hiddify/hiddify-config/assets/125398461/7fd169ea-18b4-4f7f-85b4-ee2073b8c25f" />
</div>

هر حالت در منوی Policy همراه با یکی از حالت‌های بخش **Outbound** کار می‌کند که پایین‌تر توضیح داده شده است.

### حالت Proxy
از یک کانفیگ که خودتان انتخاب می‌کنید استفاده می‌شود. این حالت همراه با حالت **Global** در Outbound به کار می‌رود.

### حالت Automatic
برنامه به کانفیگی که بهترین نتیجه تست را دارد وصل می‌شود. این حالت همراه با حالت **Rule** در Outbound به کار می‌رود.

### حالت Sequential
برنامه کانفیگ‌ها را یکی پس از دیگری استفاده می‌کند و هر از گاهی عوض می‌کند. این کار بار را در طول زمان پخش می‌کند. با حالت لودبالانس که هم‌زمان از چند کانفیگ استفاده می‌کند فرق دارد. این حالت همراه با حالت **Rule** در Outbound به کار می‌رود.

### حالت Auto
همان انتخاب خودکار کانفیگ است که حالت **Automatic** از آن استفاده می‌کند.

### حالت Load-Balance
از چند کانکشن به‌طور هم‌زمان استفاده می‌کند و بار را بین آن‌ها پخش می‌کند. وقتی IP سرور تا حدی مسدود شده و کانکشن‌های تکی خوب کار نمی‌کنند، این حالت می‌تواند کمک کند. این حالت هم همراه با حالت **Rule** در Outbound به کار می‌رود.

### تست کانکشن‌ها
روی نماد رعد و برق بزنید تا کانکشن‌ها تست شوند.

<div align=center markdown=1>
<img width=30% alt="نماد رعد و برق برای تست" src="https://github.com/hiddify/hiddify-config/assets/125398461/7bdb1519-7179-4c6e-a6e9-ee00c3bc06db" />
</div>

## به‌روزرسانی پروفایل‌ها

1. به `Settings` و سپس `Config File` بروید.
2. انگشت خود را روی یک پروفایل نگه دارید.
3. در منوی باز شده `Update Now` را بزنید.

<div align=center markdown=1>
<img width=30% alt="Update Now" src="https://github.com/hiddify/hiddify-config/assets/125398461/3ecb0ab1-40b9-40e5-8f93-5a37f9b0a1dd" />
</div>

## به‌روزرسانی خودکار پروفایل‌ها

1. در `Settings` روی `More Settings` بزنید.

    <div align=center markdown=1>
    <img width=30% alt="More Settings" src="https://github.com/hiddify/hiddify-config/assets/125398461/ab8222a0-b24b-487b-bb62-4c5509d27806" />
    </div>

2. در بخش `CONFIG FILE`، فاصله زمانی بین به‌روزرسانی‌ها را در `Update Interval` تعیین کنید.
3. گزینه `Auto Update` را روشن کنید.

Stash همچنین هر بار که برنامه را باز می‌کنید پروفایل‌ها را به‌روز می‌کند.

## انتخاب حالت Outbound

در صفحه `Home` برنامه، بخش `Outbound` سه حالت دارد.

<div align=center markdown=1>
<img width=30% alt="حالت‌های Outbound" src="https://github.com/hiddify/hiddify-config/assets/125398461/51b861c7-2e12-4541-a214-84311270cb8d" />
</div>

### Rule mode
بر اساس قوانین (Rule) داخل پروفایل تصمیم می‌گیرد کدام ترافیک از VPN عبور کند. مثلاً اگر پروفایل برای سایت‌های ایرانی قانون داشته باشد، ترافیک آن‌ها از VPN عبور نمی‌کند.

### Global mode
قوانین نادیده گرفته می‌شوند. در منوی **Policy** و در حالت **Proxy** یک کانفیگ انتخاب می‌کنید و همه ترافیک گوشی از آن عبور می‌کند. این حالت وقتی مفید است که بخواهید از یک کانفیگ خاص استفاده کنید.

### Direct mode
هیچ ترافیکی از VPN عبور نمی‌کند؛ مثل این است که VPN خاموش باشد.

## قابلیت On Demand

به `Settings` و سپس `On Demand` بروید.

<div align=center markdown=1>
<img width=30% alt="تنظیمات On Demand" src="https://github.com/hiddify/hiddify-config/assets/125398461/0854f4f3-3628-41a3-a8b4-3a3a08474370" />
</div>

### Always On
با روشن کردن این گزینه، VPN شما همیشه روشن است.

### On Demand
با روشن کردن این گزینه، VPN فقط وقتی قفل گوشی باز است فعال است و در بقیه زمان‌ها خاموش می‌شود.

## عیب‌یابی کانکشن‌ها

برای دیدن جزئیات بیشتر اتصال‌ها، منوی `Utilities` را باز کنید و `Network Diagnosis` را بزنید. در اینجا لاگ همه کانکشن‌ها نمایش داده می‌شود که برای پیدا کردن مشکل مفید است. زیربخش‌های `Connectivity` و `Proxy` از همه کاربردی‌ترند.

<div align=center markdown=1>
<img width=30% alt="Network Diagnosis" src="https://github.com/hiddify/hiddify-config/assets/125398461/3685baf2-5d0f-4305-a151-12bcc761ab23" />
</div>

</div>
