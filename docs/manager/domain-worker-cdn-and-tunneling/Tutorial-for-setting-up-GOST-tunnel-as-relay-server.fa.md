---
title: آموزش راه‌اندازی تانل GOST به عنوان سرور میانی
---

# آموزش راه‌اندازی تانل GOST به عنوان سرور میانی
<div align=center dir="rtl" markdown="1">

چیست؟  iptables بهترین راه‌کار جایگزین برای IP Forwarding با**




ابتدا می‌توانید این ویدئو را هم تماشا کنید .

<a href="https://youtu.be/T3yfTqqQqJQ" > <img width="32%" src="https://user-images.githubusercontent.com/125398461/235361265-c8f5c2ab-1ccd-46d2-b2b2-112d4fe106dd.png" /></a>

</div>


<div dir="rtl" markdown="1">

برای این کار شما به یک سرور میانی نیاز دارید تا از طریق آن به سرور اصلی متصل شوید. معمولا این سرور میانی در کشور محل اقامت در نظر گرفته می‌شود.

<div align=center dir="rtl" markdown="1">
 
<img src="https://user-images.githubusercontent.com/125398461/235339506-bdd76cec-0378-4942-8352-ebebeb006231.png">
</div>










یکی از بهترین روشها برای جایگزین کردن IP-Forwarding با استفاده از IP-Tables استفاده از تانل GOST است. 

این تانل از چند لحاظ خیلی بهتر از IP Forwarding هست. ( یا همان تانل زدن معمولی که همه استفاده میکنند)
تو این روش بر خلاف آیپی فورواردینگ شما میتونید به جای IP از نام دامین یا ساب دامین استفاده کنید که این خودش باعث کمتر شناسایی شدن IP سرور شما میشه.
یه خوبی دیگه که این روش داره اینه که از یه تانل رمز نگاری شده دیتا عبور میکنه.
این تانل Open Source هست. 
با پروتکل های V2Ray - VMess - Vless - Trojan به خوبی سازگاری داره.
در این تانل هم WebSocket جواب میده هم gRPC
این تانل چون خودش یک سرویس داره با ریبوت شدن سرور اجرا میشه و نیازی به زدن دستور مجدد نداره.
اگر بخواید میتونید هم پورت TCP رو فوروارد کنید و هم UDP. کافیه داخل دستور به جای TCP بزنید UDP.
میتونید هر چند تا پورت که خواستید رو فوروارد کنید

برای نصب در حالت Relay طبق این آموزش جلو برید.

- وارد سرور میانی خود شوید یعنی به سرور خود SSH بزنید.
- ابتدا سورس برنامه مورد نظر را با کد زیر دانلود و از حالت فشرده خارج کنید. 

```
sudo apt install wget nano -y && wget https://github.com/ginuerzh/gost/releases/download/v2.11.5/gost-linux-amd64-2.11.5.gz && gunzip gost-linux-amd64-2.11.5.gz

```

- سپس فایلهای آن را به پوشه اجرایی منتقل کنید و به آن دسترسی اجرا دهید. 

```
sudo mv gost-linux-amd64-2.11.5 /usr/local/bin/gost && sudo chmod +x /usr/local/bin/gost
```

- حالا باید سرویس آن را نیز ایجاد کنید.
- ابتدا با استفاده از ویرایشگر nano فایل سرویس را ایجاد کنید.

```
sudo nano /usr/lib/systemd/system/gost.service
```

سپس کد زیر را در فایل باز شد به صورت کامل کپی کنید. 

```
[Unit]
Description=GO Simple Tunnel
After=network.target
Wants=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/gost -L=tcp://:443/domain.com:443 -L=tcp://:80/domain.com:80

[Install]
WantedBy=multi-user.target
```

بعد از کپی باید نام دامین خودتان را به جای domain.com قرار دهید. توجه کنید که نام دامنه ای که وارد میکنید باید آدرس IP اصلی سرور شما باشد.  ( هر ۲ تا domain.com را پاک کنید و نام دامنه خودتون را وارد کنید)

خوب کار تقریبا تمام شد.
حالا با کد زیر ابتدا سرویس gost را استارت کنید. و با سپس سرویس را فعال می‌کنید که با هر بار ریستارت سرویس اجرا شود:

```
sudo systemctl start gost && systemctl enable gost
```

کار تمام شد و میتوانید از تانل استفاده کنید.

## تعریف سرور میانی در هیدیفای‌منیجر
حالا برای آیپی سرور میانی خود **یک ساب‌دامین با پروکسی خاموش** ثبت نمایید و آن را در هیدیفای‌منیجر روی حالت Relay ثبت نمایید.

 
![](https://user-images.githubusercontent.com/125398461/235341283-97c026b7-1d70-4362-8950-1e5c1b79d508.png)

## افزودن کانفیگ‌های Relay جهت استفاده به لینک سابسکریپشن
همانند همیشه در هیدیفای‌منیجر بهتر است کانفیگ‌ها را از لینک سابسکریپشن جدا کنید. بنابراین برای دامنه Relay ثبت شده نیز می‌توانید در تنظیمات دامنه مربوط به سابسکریپشن، تیک مربوط به دامین Relay را بزنید تا کانفیگ‌های آن به دامنه سابسکریپشن اضافه گردند.

فرض شود که دامنه مربوط به سابسکریپشن t1.hiddify.com باشد، مطابق با تصویر زیر جلو بروید تا کار انجام شود.

![Screenshot_20230430_1104341](https://user-images.githubusercontent.com/125398461/235342038-cfda2574-2444-4414-843d-2ed507537d1d.png)


حالا اگه صفحه کاربر را با دامین سابسکریپشن (در اینجا t1.hiddify.com) باز نمایید خواهید دید که کانکشن‌های مربوط به Relay نیز اضافه شده‌اند. می‌توانید این کانکشن‌ها را به صورت تک تک و یا با استفاده از لینک‌های سابسکریشن معمولی یا سابسکریپشن b64 به کلاینت خود اضافه نمایید و استفاده نمایید.



## حذف کانفیگ گوست از سرور میانی

برای این کار ابتدا این کامند را اجرا کنید.

```
systemctl daemon-reload
```
و سپس سرویس گوست را متوقف و غیرفعال کنید.
```
sudo systemctl stop gost && systemctl disable gost
```
در نهایت برای حذف کامل برنامه و سرویس این کامندها را بزنید.

```
sudo rm -f  /usr/lib/systemd/system/gost.service /usr/local/bin/gost
```
[سورس پروژه GOST](https://github.com/ginuerzh/gost)