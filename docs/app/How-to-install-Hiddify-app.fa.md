---
title: آموزش نصب اپ هیدیفای
---

<div markdown="1" dir="rtl">

# آموزش نصب اپ هیدیفای

در این صفحه یاد می‌گیرید برنامهٔ هیدیفای را روی گوشی یا کامپیوتر خود دانلود و نصب کنید. اپ هیدیفای یک برنامهٔ رایگان، بدون تبلیغ و متن‌باز است که شما را به یک سرور پروکسی یا VPN وصل می‌کند تا به اینترنت آزاد دسترسی داشته باشید. اگر کسی (یا سرور هیدیفای خودتان) به شما یک کانفیگ یا لینک سابسکریپشن داده است، به این برنامه نیاز دارید.

اپ هیدیفای بر پایهٔ **sing-box** (موتوری که اتصال‌ها را برقرار می‌کند) ساخته شده است. از پروتکل‌های زیادی پشتیبانی می‌کند، از جمله VLESS، VMess، Trojan، Reality، TUIC، Hysteria، WireGuard، AmneziaWG، Naive و SSH، و لینک‌های سابسکریپشن sing-box، V2ray، Clash و Clash Meta را می‌پذیرد. [فهرست کامل امکانات](https://github.com/hiddify/hiddify-app/blob/main/README_fa.md) را در GitHub ببینید.

آخرین نسخهٔ پایدار **v4.1.1** است.

## پیش از شروع

بررسی کنید که دستگاه شما پشتیبانی می‌شود:

| دستگاه | چه چیزی لازم دارید |
|---|---|
| اندروید | Android 7.0 یا جدیدتر |
| آیفون / آیپد | iOS 15 یا جدیدتر |
| ویندوز | Windows 10 (نسخهٔ 1809) یا Windows 11، نسخهٔ ۶۴ بیتی |
| مک | macOS 10.15 (Catalina) یا جدیدتر، اینتل یا Apple Silicon |
| لینوکس | لینوکس ۶۴ بیتی (x64)؛ توزیع‌های مبتنی بر Debian/Ubuntu بهترین پشتیبانی را دارند |

!!! note "ویندوز ۷، ویندوز ۸ و لینوکس‌های RPM"
    اپ هیدیفای از ویندوز ۷ و ۸ پشتیبانی نمی‌کند. بستهٔ `.rpm` هم دیگر منتشر نمی‌شود (از نسخهٔ ۴ حذف شد): در Fedora، openSUSE و سیستم‌های مشابه از فایل AppImage استفاده کنید.

## کدام فایل را دانلود کنم؟

ردیف مربوط به دستگاه خود را انتخاب کنید. نسخه‌های فروشگاهی خودکار به‌روز می‌شوند، اما فایل‌های GitHub نه.

| دستگاه | پیشنهاد ما | گزینه‌های دیگر |
|---|---|---|
| اندروید | [Google Play](https://play.google.com/store/apps/details?id=app.hiddify.com) | فایل APK: [universal](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Android-universal.apk) (روی همهٔ گوشی‌ها کار می‌کند)، [arm64](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Android-arm64.apk)، [arm7](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Android-arm7.apk)، [x86_64](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Android-x86_64.apk) |
| آیفون / آیپد | [App Store](https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532) | — |
| ویندوز | [فایل نصب (.exe)](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Windows-Setup-x64.exe) | [Microsoft Store](https://apps.microsoft.com/detail/9pdfnl3qv2s5)، [بستهٔ MSIX](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Windows-x64.msix)، [نسخهٔ پرتابل ZIP](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Windows-Portable-x64.zip)، winget |
| مک | [فایل DMG](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-MacOS.dmg) | [نصب‌کنندهٔ PKG](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-MacOS-Installer.pkg)، [App Store](https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532) (مک‌های Apple Silicon) |
| لینوکس | [AppImage](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Linux-x64-AppImage.AppImage) | [بستهٔ .deb](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Debian-x64.deb) (Debian، Ubuntu، Mint)، [AppImage داخل فایل .tar.gz](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Linux-x64-AppImage.tar.gz) |

همهٔ فایل‌ها در [صفحهٔ انتشارها در GitHub](https://github.com/hiddify/hiddify-app/releases/latest) هم هستند.

<div markdown="1" align=center>
 <a href="https://play.google.com/store/apps/details?id=app.hiddify.com"><img width=20% alt="دریافت از Google Play" src="https://raw.githubusercontent.com/hiddify/hiddify-app/main/docs/google-play-badge.png"></a>
<br>
<br>
<a href="https://www.youtube.com/watch?v=vUaA1AEUy1s"><img width="32%" alt="ویدیو: نصب هیدیفای روی ویندوز" src="https://github.com/hiddify/hiddify-next/assets/125398461/0f1e88a7-ecf0-4ba7-8c12-f24f70c68c3d" /></a>
</div>

## نصب برنامه

بخش مربوط به دستگاه خود را باز کنید.

<details markdown="1"> <summary><b>نصب روی اندروید</b> (کلیک کنید)</summary>

**از Google Play (پیشنهادی)**

1. [صفحهٔ هیدیفای در Google Play](https://play.google.com/store/apps/details?id=app.hiddify.com) را باز کنید.
2. روی `Install` بزنید.
3. پس از پایان نصب، روی `Open` بزنید.

**با فایل APK (اگر به Google Play دسترسی ندارید)**

1. [فایل APK نسخهٔ universal](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Android-universal.apk) را دانلود کنید. این فایل روی همهٔ گوشی‌های اندرویدی کار می‌کند.
2. فایل دانلودشده را از بخش اعلان‌ها یا پوشهٔ `Downloads` باز کنید.
3. اگر اندروید گفت اجازهٔ نصب از این منبع را ندارد، روی `Settings` (تنظیمات) بزنید، گزینهٔ `Allow from this source` را روشن کنید و برگردید.
4. روی `Install` و سپس `Open` بزنید.

</details>
<br>

<details markdown="1"> <summary><b>نصب روی آیفون یا آیپد</b> (کلیک کنید)</summary>

1. [صفحهٔ Hiddify Proxy & VPN در App Store](https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532) را باز کنید.
2. روی `Get` بزنید و با Face ID، Touch ID یا رمز عبور تأیید کنید.
3. برنامه را باز کنید. اولین بار که وصل می‌شوید، iOS اجازهٔ افزودن تنظیمات VPN را می‌خواهد: روی `Allow` بزنید.

!!! note "نکته"
    این برنامه در App Store همهٔ کشورها در دسترس نیست. اگر آن را پیدا نمی‌کنید، احتمالاً کشور Apple ID شما کشوری است که برنامه در آن ارائه نمی‌شود.

</details>
<br>

<details markdown="1"> <summary><b>نصب روی ویندوز</b> (کلیک کنید)</summary>

می‌توانید برنامه را از [Microsoft Store](https://apps.microsoft.com/detail/9pdfnl3qv2s5) هم نصب کنید، یا **Command Prompt** را باز کنید و این دستور را اجرا کنید:

<div markdown="1" dir="ltr">

```bash
winget install Hiddify.Next
```

</div>

(`Hiddify.Next` نام قدیمی برنامه است، اما همین نسخهٔ فعلی برنامهٔ هیدیفای را نصب می‌کند.)

برای نصب با فایل نصب:

1. [فایل نصب](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Windows-Setup-x64.exe) (`Hiddify-Windows-Setup-x64.exe`) را دانلود کنید.
2. روی فایل دانلودشده دو بار کلیک کنید. وقتی ویندوز پرسید «آیا اجازه می‌دهید این برنامه تغییراتی در دستگاه شما ایجاد کند؟»، روی `Yes` بزنید.

    <div align=center>
    <img width=30% alt="پیغام User Account Control ویندوز" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/e4174de0-10b5-4b46-9baf-2e302162da5a">
    </div>

3. اگر پنجرهٔ آبی «Windows protected your PC» ظاهر شد، روی `More info` بزنید.

    <div align=center>
    <img width=40% alt="هشدار Windows protected your PC" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/8a3bc452-004d-4be7-a9bb-21aad90db7fc">
    </div>

4. روی `Run anyway` بزنید.

    <div align=center>
    <img width=40% alt="دکمهٔ Run anyway" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/36293a7c-f56a-4811-8302-474874654b70">
    </div>

5. نصب‌کننده محل نصب برنامه را نشان می‌دهد. پوشهٔ پیش‌فرض را نگه دارید (یا تغییرش دهید) و روی `Next` بزنید.

    <div align=center>
    <img width=60% alt="انتخاب محل نصب" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/7196a86f-3f74-4177-b611-19b484e0da9a">
    </div>

6. گزینه‌های اضافه، مثل ساخت میان‌بر (Shortcut) روی دسکتاپ یا اجرای خودکار برنامه، را انتخاب کنید و روی `Next` بزنید.

    <div align=center>
    <img width=60% alt="گزینه‌های اضافهٔ نصب" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/bcac0d1e-f8d8-46d9-bedc-4fe04571a504">
    </div>

7. روی `Install` بزنید.

    <div align=center>
    <img width=60% alt="آمادهٔ نصب" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/980314df-c907-407c-aa4d-a94d4d492b66">
    </div>

8. صبر کنید تا نصب تمام شود.

    <div align=center>
    <img width=60% alt="در حال نصب" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/1aee90d0-dde1-4bf8-b673-058fc0e9204a">
    </div>

9. وقتی پنجرهٔ زیر را دیدید، روی `Finish` بزنید. برنامه اجرا می‌شود. اگر اجرا نشد، روی میان‌بر هیدیفای در دسکتاپ دو بار کلیک کنید.

    <div align=center>
    <img width=60% alt="پایان نصب" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/4a8849c5-24f0-4376-be4d-355eb754f395">
    </div>

!!! tip "اگر برنامه اجرا نشد"
    اگر ویندوز خطایی دربارهٔ نبودن فایلی مثل `MSVCP140.dll` نشان داد، [Microsoft Visual C++ Redistributable (x64)](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist) را نصب کنید و دوباره امتحان کنید.

</details>
<br>

<details markdown="1"> <summary><b>نصب روی مک</b> (کلیک کنید)</summary>

اگر مک شما Apple Silicon (M1 یا جدیدتر) دارد، می‌توانید برنامه را از [App Store](https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532) هم نصب کنید.

برای نصب با فایل DMG:

1. [فایل DMG](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-MacOS.dmg) (`Hiddify-MacOS.dmg`) را دانلود کنید. این فایل روی مک‌های اینتل و Apple Silicon کار می‌کند.
2. پوشهٔ `Downloads` را باز کنید و روی فایل دو بار کلیک کنید.

    <div align=center>
    <img width=60% alt="فایل DMG دانلودشده" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/e6cbdb24-ef18-49a0-9c40-0f4ea4859def">
    </div>

3. آیکون هیدیفای را بگیرید و روی پوشهٔ `Applications` رها کنید. با این کار برنامه روی مک شما کپی می‌شود.

    <div align=center>
    <img width=60% alt="کشیدن برنامه به Applications" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/07fa37b8-fc37-4613-b148-2eb932a3d53a">
    </div>

4. پوشهٔ `Applications` را باز کنید و روی هیدیفای دو بار کلیک کنید.

    <div align=center>
    <img width=60% alt="هیدیفای در پوشهٔ Applications" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/8a32bcd9-367d-4cf1-8951-c764b5f86795">
    </div>

5. بار اول ممکن است macOS بگوید برنامه را باز نمی‌کند، چون از App Store دانلود نشده است. روی `OK` (یا `Done`) بزنید.

    <div align=center>
    <img width=30% alt="هشدار macOS برای باز نکردن برنامه" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/a65690ed-e169-4c9d-a908-93a4260fddf1">
    </div>

6. به **System Settings > Privacy & Security** بروید (در نسخه‌های قدیمی‌تر macOS: **System Preferences > Security & Privacy > General**)، پایین بروید و کنار پیغام هیدیفای روی `Open Anyway` بزنید.

    <div align=center>
    <img width=60% alt="دکمهٔ Open Anyway در تنظیمات امنیتی" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/97fa1692-5eb2-436c-9070-804a71c3bc81">
    </div>

7. روی `Open` بزنید.

    <div align=center>
    <img width=60% alt="تأیید Open" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/cbdec7f8-e12e-4613-b51d-9870df2acd49">
    </div>

از این به بعد می‌توانید هیدیفای را مثل هر برنامهٔ دیگری از `Applications` باز کنید.

</details>
<br>

<details markdown="1"> <summary><b>نصب روی لینوکس</b> (کلیک کنید)</summary>

**روش ۱: AppImage (روی بیشتر توزیع‌های ۶۴ بیتی کار می‌کند)**

1. [فایل AppImage](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Linux-x64-AppImage.AppImage) (`Hiddify-Linux-x64-AppImage.AppImage`) را دانلود کنید. لازم نیست آن را از حالت فشرده خارج کنید.
2. ترمینال را باز کنید و فایل را اجرایی کنید. در این مثال فرض شده فایل در پوشهٔ `Downloads` است:

    <div markdown="1" dir="ltr">

    ```bash
    chmod +x ~/Downloads/Hiddify-Linux-x64-AppImage.AppImage
    ```

    </div>

3. برنامه را اجرا کنید:

    <div markdown="1" dir="ltr">

    ```bash
    ~/Downloads/Hiddify-Linux-x64-AppImage.AppImage
    ```

    </div>

    می‌توانید روی فایل در File Manager هم دو بار کلیک کنید.

اگر اتفاقی نیفتاد یا خطایی دربارهٔ **FUSE** (کتابخانه‌ای از سیستم که فایل‌های AppImage به آن نیاز دارند) دیدید، آن را در ترمینال نصب کنید و دوباره امتحان کنید.

در Ubuntu 22.04:

<div markdown="1" dir="ltr">

```bash
sudo apt install libfuse2
```

</div>

در Ubuntu 24.04 و جدیدتر:

<div markdown="1" dir="ltr">

```bash
sudo apt install libfuse2t64
```

</div>

**روش ۲: بستهٔ .deb (برای Debian، Ubuntu و Linux Mint)**

1. [بستهٔ .deb](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Debian-x64.deb) (`Hiddify-Debian-x64.deb`) را دانلود کنید.
2. در ترمینال این دستور را اجرا کنید:

    <div markdown="1" dir="ltr">

    ```bash
    sudo apt install ~/Downloads/Hiddify-Debian-x64.deb
    ```

    </div>

3. هیدیفای را از منوی برنامه‌ها باز کنید.

</details>
<br>

## اولین اجرا

اولین بار که برنامه را باز می‌کنید، چند سؤال می‌پرسد:

1. روی `Language` (زبان) بزنید و زبان خود را انتخاب کنید.
2. روی `Region` (منطقه) بزنید و کشوری را که در آن هستید (مثلاً ایران) انتخاب کنید. برنامه با این تنظیم سایت‌های داخلی را مستقیم و بدون پروکسی باز می‌کند.
3. گزینهٔ `Enable analytics` (فعال‌سازی آمار) را روشن یا خاموش کنید. اگر روشن باشد، برنامه گزارش‌های خطا و آمار ناشناس استفاده را می‌فرستد تا سازندگان آن را بهتر کنند.
4. روی `Start` (شروع) بزنید.

<div markdown="1" align=center>
<img width=60% alt="اولین اجرا: زبان، منطقه و آمار" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/0d50c68f-d6e5-45f3-b86a-0f0217b29867">
</div>

حالا باید صفحهٔ اصلی برنامه را ببینید. دفعه‌های بعد برنامه مستقیم همین صفحه را باز می‌کند.

<div markdown="1" align=center>
<img width=60% alt="صفحهٔ اصلی اپ هیدیفای" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/9ff5d21c-7fbf-4183-96bb-acd12cebf2a8">
</div>

!!! note "نکته"
    تصاویر این صفحه از نسخه‌ای قدیمی‌تر از برنامه هستند. مراحل همین است، اما ظاهر بعضی صفحه‌ها در نسخهٔ ۴ فرق دارد.

## قدم بعدی

برای افزودن کانفیگ یا لینک سابسکریپشن و وصل شدن، [آموزش کار با اپ هیدیفای](How-to-use-Hiddify-app.md) را بخوانید.

</div>
