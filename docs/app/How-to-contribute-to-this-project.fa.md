---
title: چگونه می‌توان در این پروژه همکاری نمود
---

<div dir="rtl">

# چگونه می‌توان در این پروژه همکاری نمود

برای این کار کافیه شما git را روی سیستم خود نصب نمایید.

## نصب git روی سیستم 
بر اساس سیستم عامل خود یکی از موارد زیر را باز نمایید.

<br>
<details dir=rtl><summary><b>ویندوز</b></summary>



- ابتدا به [اینجا](https://git-scm.com/download/win) بروید و نسخه مخصوص ویندوز را دانلود کنید.
- سپس فایل دانلود شده را از حالت فشرده خارج نمایید و برای نصب آن را ارا نمایید.
<div align=center>

![location-git-windows-download](https://github.com/hiddify/hiddify-config/assets/125398461/cd883726-f340-441c-bbca-df98f0389de2)

</div>

- سپس wizard نصب را تا انتها با next و yes دنبال کنید. پیشنهاد می‌شود تنظیمات دیفالت را تغییر ندهید.

<div align=center>

![read-and-accept-git-license-agreement](https://github.com/hiddify/hiddify-config/assets/125398461/c8220a90-4f88-451f-ac60-ca6280feef20)

</div>
به صورت دیفالت محل نصب git در این مسیر است.
<div dir=ltr>

```
C:/Program Files/Git
```
</div>
یعنی در مراحل بعد، پروژه‌ها در این مسیر قرار می‌گیرند. کار تمام است.
- برای چک کردن ورژن `git` نصب شده، `command prompt` را باز نمایید و دستور زیر را اجرا کنید.

<div dir=ltr>

```
git version
```

</div>

- به صورت دیفالت `git` در پوشه `Home` کاربر نصب می‌گردد.
</details>

<br>
<details dir=rtl><summary><b>مک</b></summary>

- ابتدا از [اینجا](https://sourceforge.net/projects/git-osx-installer/files/git-2.23.0-intel-universal-mavericks.dmg/download?use_mirror=autoselect) فایل نصب را دانلود کنید.
- سپس آن را جارا نمایید. نصب خیلی ساده‌ای دارد.
- بعد از نصب برای چک کردن ورژن `git` نصب شده، `terminal` را باز نمایید و دستور زیر را اجرا کنید.

<div dir=ltr>

```
git version
```

</div>


</details>

<br>
<details dir=rtl><summary><h3>لینوکس</h3></summary>

در اکثر توزیع‌های سیستم عامل لینوکس git به صورت دیفالت نصب است و نیاز نیست کار خاصی بکنید. اما اگر به هر دلیلی نیاز بود آن را نصب نمایید باید سرچ بزنید و کامند مناسب مربوط به آن توزیع را پیدا کنید. در ادامه کامند نصب مربوط به ند توزیع معروف قرار می‌گیرد.
<div dir=ltr>

**Debian/Ubuntu**

```
sudo apt-get install git-all
```

**Fedora**

```
dnf install git-all
```

**Arch**
````
pacman -Syu git-all
````
</div>

در همه توزیع‌ها git در مسیر Home کاربر نصب می‌گردد.
- برای چک کردن نسخه git نصب شده در ترمیال این دستور را اجرا کنید.

<div dir=ltr>

```
git version
```
</div>

</details>




## استفاده از git جهت توسعه پروژه هیدیفای

- ابتدا باید پروژه را fork کنید. برای این کار اگر قصد fork کردن پنل را دارید کامند زیر را اجرا کنید.

<div dir=ltr>

```
git clone https://github.com/hiddify/hiddify-next.git
```

</div>


- اندکی صبر کنید تا فایل‌های پروژه کپی شود.

<div align=center>

![Screenshot_20230807_172554](https://github.com/hiddify/hiddify-config/assets/125398461/b4730f3a-3f86-4792-8ccc-6a5789056c1d)

</div>

- حالا باید یک شاخه یا branch از پروژه درست کنید تا روی آن کار کنید. برای این کار ابتدا برای شاخه یک اسم انتخاب کنید. مثلا فرض کنیم اسم شاخه را `Hiddify-develop` انتخاب می‌کنیم. حالا دستورات زیر را اجرا کنید. 

<div dir="ltr" >

```
git branch Hiddify-develop
git checkout Hiddify-develop
```

</div>

<div dir="rtl" >

-  حالا تغییرات مورد نظر خود را روی فایل‌ها با استفاده از هر ابزاری اعمال کنید. توصیه می‌شود از `VSCode` استفاده نمایید.
-  یادتون نره مسیر تمامی فایل‌ها در پوشه‌های گفته شده در مرحله نصب است.
- 
- حالا وقتی تغییرات مورد نظر خود را اعمال نمودید باید تغییرات را در `git` نیز ثبت کنید. بنابراین در ترمینال کامند‌های زیر را به ترتیب اجرا نمایید.
- ابتدا با کامند زیر انجام تغییرات را به `git` اعلام کنید.


<div dir=ltr>

```
git add
```

</div>

- سپس تغییرات را کامیت نمایید. نیاز است که در اینجا یک توضیح برای تغییرات اعلام نمایید.

<div dir=ltr>

```
git commit -m "a short description of the change"
```

</div>

مثلا اگر تغییرات مدنظر شما مربوط به بخش توسعه بات باشد می‌توان چنین توضیحی نوشت.


<div dir=ltr>

```
git commit -m "a short description of the change"
```

</div> 

هیچ مشکلی ندارد که توضیحات این بخش زیاد باشد و اتفاقا توصیه می‌شود تا جای ممکن توضیحات کامل و جامع باشد.
در این مرحله تغییرات با موفقیت وارد سیستم git شد. حالا باید تغییرات را به سمت GitHub بفرستید. برای این کار دستور زیر را اجرا کنید. 

<div dir=ltr>

```
git push
```
</div>

در اینجا مشخصات اکانت شما در گیتهاب پرسیده می‌شود. نیاز است `username` و `password` خود در گیتهاب را وارد نمایید.


- حالا وارد اکانت خود در گیتهاب شوید و پروژه فورک شده را باز نمایید.
مسیری به شکل زیر دارد:

<div dir=ltr>

`https://github.com/<your_username>/hiddify-next`

</div>

- حالا یک banner مشاهده می‌کنید که به شما اعلام می‌کند که branch شما از پروژه اصلی یک مرحله جلوتر است. برای اینکه تغییرات با پروژه اصلی merge یا ادغام شود `Contribute` را کلیک کنید و `Open a pull request` را بزنید.
- کار تمام است تغییرات به پروژه ارسال شد. حالا پس از تایید مدیر پروژه تغییرات شما به پروژه اضافه می‌گردد.

<br>

**این برنامه با استفاده از [Flutter](https://flutter.dev/) و [Go](https://go.dev/) توسعه یافته است. برای اطلاعات بیشتر در خصوص توسعه می‌توانید [دستورالعمل‌های مشارکت](https://github.com/hiddify/hiddify-next/blob/main/CONTRIBUTING.md) در پروژه ما را مطالعه نمایید.**

