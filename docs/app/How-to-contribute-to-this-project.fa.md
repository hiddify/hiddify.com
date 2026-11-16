---
title: چگونه در پروژهٔ اپ هیدیفای مشارکت کنیم
---

# چگونه در پروژهٔ اپ هیدیفای مشارکت کنیم

اپ هیدیفای متن‌باز است: [github.com/hiddify/hiddify-app](https://github.com/hiddify/hiddify-app). می‌توانید با گزارش مشکل، ترجمه یا تغییر کد کمک کنید. این صفحه هر کدام را توضیح می‌دهد.

!!! info "نوشته‌شده برای اپ هیدیفای ۵.۹"
    دستورهای این صفحه با مخزن در نسخهٔ ۵.۹ (Flutter نسخهٔ ۳.۳۸.۵ یا جدیدتر) می‌خوانند.

## گزارش مشکل یا پیشنهاد قابلیت

1. اول در [issueها](https://github.com/hiddify/hiddify-app/issues?q=is%3Aissue)، باز و بسته، جستجو کنید. اگر کسی قبلاً گزارشش داده، اطلاعات خودتان را همان‌جا اضافه کنید.
2. در غیر این صورت یک [issue جدید](https://github.com/hiddify/hiddify-app/issues/new/choose) باز کنید و **Bug report** یا **Feature request** را انتخاب کنید. نسخهٔ اپ (**تنظیمات › درباره**)، دستگاه و سیستم‌عامل و مراحلی را که مشکل را ایجاد می‌کند بنویسید.
3. لاگ‌ها را اضافه کنید. روش گرفتن لاگ و فرستادن گزارش خطا از داخل اپ: [لاگ‌ها و گزارش مشکل](Logs-and-reporting-a-problem.md). قبل از فرستادن، لینک‌ها، آی‌پی‌ها و رمزهایتان را پاک کنید.

برای یک تغییر بزرگ، قبل از نوشتن کد یک issue باز کنید و با نگه‌دارندگان پروژه درباره‌اش به توافق برسید.

## ترجمه

متن‌های اپ در [`assets/translations`](https://github.com/hiddify/hiddify-app/tree/main/assets/translations) هستند: برای هر زبان یک فایل، مثل `fa.i18n.json`. فایل `en.i18n.json` مبناست و همهٔ فایل‌های دیگر همان کلیدها را دارند.

- برای اصلاح یک ترجمه، فایل زبان خودتان را در گیت‌هاب ویرایش کنید (آیکون مداد) و تغییر را به شکل pull request بفرستید. گیت‌هاب fork و branch را خودش برایتان می‌سازد.
- کلیدها، جاگذارهای `${…}` و شکستن خط‌ها (`\n`) را دست نزنید؛ فقط متن را ترجمه کنید.
- اگر روی سیستم خودتان کار می‌کنید، بعد از ویرایش `make translate` را اجرا کنید تا فایل‌ها بررسی و کد ترجمه‌ها دوباره ساخته شود.

## تغییر کد

### ۱. گرفتن کد

1. در گیت‌هاب [hiddify/hiddify-app](https://github.com/hiddify/hiddify-app) را باز کنید و روی **Fork** بزنید. این کار یک نسخه از مخزن زیر حساب خودتان می‌سازد.
2. fork خودتان را clone (دانلود) کنید و مخزن اصلی را با نام `upstream` اضافه کنید:

```bash
git clone https://github.com/<your-username>/hiddify-app.git
cd hiddify-app
git remote add upstream https://github.com/hiddify/hiddify-app.git
```

### ۲. نصب ابزارها

- [Flutter](https://docs.flutter.dev/get-started/install) نسخهٔ ۳.۳۸.۵ یا جدیدتر (`flutter --version` نسخه را نشان می‌دهد)، همراه ابزارهای پلتفرم مقصد: Android Studio و Android SDK برای اندروید؛ Xcode برای iOS و مک؛ Visual Studio با «Desktop development with C++» برای ویندوز.
- `make`، `curl` و `tar`. روی Debian یا Ubuntu، دستور `make linux-install-deps` چیزهایی را که ساخت لینوکس لازم دارد نصب می‌کند.

### ۳. آماده کردن یک پلتفرم

دستور پلتفرمی را که برایش می‌سازید اجرا کنید:

```bash
make android-prepare     # or: windows-prepare, linux-prepare, macos-prepare, ios-prepare
```

این دستور `flutter pub get` را اجرا می‌کند، کدهای تولیدی (`dart run build_runner build`) و ترجمه‌ها (`dart run slang`) را می‌سازد و کتابخانهٔ هستهٔ هیدیفای را برای آن پلتفرم از [ریلیزهای hiddify-core](https://github.com/hiddify/hiddify-core/releases) دانلود می‌کند. بعد از عوض کردن branch دوباره اجرایش کنید.

در حین کار:

- بعد از تغییر یک model، provider یا هر چیزی که کد تولیدی دارد: `make gen`؛
- بعد از تغییر یک فایل ترجمه: `make translate`.

### ۴. اجرا

```bash
flutter devices
flutter run -d <device-id>
```

`flutter devices` گوشی‌ها، شبیه‌سازها و کامپیوتر شما را فهرست می‌کند. برای ساخت نسخهٔ release جهت تست: `make android-release` (یا `windows-release`، `linux-release`، `macos-release`).

### ۵. ساختن هسته از سورس (اختیاری)

فقط اگر هستهٔ هیدیفای را هم تغییر می‌دهید لازم است. هسته submodule‌ای به نام `hiddify-core` است و به [Go](https://go.dev/dl/) نیاز دارد:

```bash
git config submodule.hiddify-core.url https://github.com/hiddify/hiddify-core.git
git submodule update --init --recursive hiddify-core
make build-android-libs   # or: build-windows-libs, build-linux-libs, build-macos-libs, build-ios-libs
```

دستور اول فقط وقتی لازم است که روی گیت‌هاب کلید SSH ندارید. تغییرهای خود هسته به [hiddify-core](https://github.com/hiddify/hiddify-core) (و [hiddify-sing-box](https://github.com/hiddify/hiddify-sing-box)) می‌روند، با pull request جداگانه. باگ هسته را در اپ دور نزنید: آن را در خود هسته درست یا همان‌جا گزارش کنید.

### ۶. فرستادن تغییر

1. یک branch از آخرین کد بسازید:

    ```bash
    git fetch upstream
    git switch -c fix/short-name upstream/main
    ```

2. در هر branch فقط یک تغییر بدهید. پیام commitها را به سبک [Conventional Commits](https://www.conventionalcommits.org/) بنویسید، مثلاً `fix(home): keep the connect button disabled while stopping`.
3. فایل‌های تولیدی (`*.g.dart`، `*.freezed.dart`، ترجمه‌های تولیدشده در `lib/gen`)، کتابخانه‌های دانلودشدهٔ هسته، اشاره‌گر submodule `hiddify-core` و هیچ لینک، آی‌پی یا کلید واقعی را commit نکنید.
4. روی اندروید و یک سیستم‌عامل دسکتاپ تست کنید.
5. branch را با آخرین کد به‌روز کنید و به fork خودتان push کنید:

    ```bash
    git fetch upstream
    git rebase upstream/main
    git push -u origin fix/short-name
    ```

6. در گیت‌هاب یک **pull request** از branch خودتان به `hiddify/hiddify-app` با پایهٔ `main` باز کنید. بنویسید چه مشکلی بود، چه چیزی را تغییر دادید و چطور تست کردید. برای تغییری که در ظاهر اپ دیده می‌شود، عکس یا ویدیوی کوتاه قبل و بعد بگذارید.

## ارتباط با تیم

- [گروه هیدیفای در تلگرام](https://t.me/hiddify_board) و [کانال](https://t.me/hiddify)
- ایمیل: contribute@hiddify.com

## مقاله‌های مرتبط

- [گزارش‌ها (لاگ) و گزارش مشکل در اپ هیدیفای](/fa/app/Logs-and-reporting-a-problem/)
- [آموزش کار با اپ هیدیفای](/fa/app/How-to-use-Hiddify-app/)
- [آموزش نصب اپ هیدیفای](/fa/app/How-to-install-Hiddify-app/)
