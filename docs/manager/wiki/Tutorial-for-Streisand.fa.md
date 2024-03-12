

<div dir="rtl" markdown="1">


# آموزش کار با نرم‌افزار Streisand
این نرم افزار یکی از اپ‌های رایگان برای iOS است که iOSهای نسخه 14 به بعد قابل نصب است.

## دانلود اپلیکیشن
برای نصب اپلیکیشن می توان از [اینجا](https://apps.apple.com/us/app/streisand/id6450534064) آن را دانلود و نصب نمود.

## افزودن لینک سابسکریپشن
برای این کار ۲ راه وجود دارد.

### کپی کردن لینک سابسکریپشن

* برای این کار به پنل کاربری خود بروید و در قسمت `تمام کانفیگ‌ها`، بخش مربوط به `auto` را باز نمایید.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/5fb09864-81c6-4665-b75c-01988fb7fa81" />

</div>


* حالا می‌توانید QR code را `کپی` کنید.


<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/b8a76e41-4db4-45ac-be27-856f6ec9182e" />

</div>

* وارد نرم‌افزار شوید و دکمه `+` را بزنید.


<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/78fe4b65-d7f7-4d16-b185-82f8dd67a135" />

</div>

* سپس سابسکریپشن به نرم‌افزار اضافه می‌گردد و کانفیگ‌ها لود می‌شوند.

### اسکن کردن لینک سابسکریپشن

* می‌توان به جای کپی لینک سابسکریپشن، QR code را اسکن نمود.


<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/fe4de484-3136-4531-8292-c961e26d838e" />

</div>


* در نرم‌افزار دکمه `+` را بزنید و گزینه `Scan QRCode` را بزنید و QR code را اسکن نمایید.


<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/58c97e17-3cfa-4c40-9b2d-01de70b1e40d" />

</div>

* سپس سابسکریپشن به نرم‌افزار اضافه می‌گردد و کانفیگ‌ها لود می‌شوند.

## تنظیمات Subscription
برای این کار روی سابسکریپشن اضافه شده به نرم‌افزار تپ کنید و نگه دارید. گزینه‌های زیر ظاهر می‌شوند.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/52954cdf-5c76-4fbe-8adb-8371d7fa6747" />

</div>



### Latency
میزان تاخیر مربوط به کانفیگ‌ها را محاسبه می‌کند.

### TCP Ping
از کانفیگ‌ها تست پینگ TCP می‌گیرد.

### ICMP Ping
از کانفیگ‌ها تست پیننگ معمولی می‌گیرد.


> نکته: تفاوت تست پینگ معمولی و پینگ TCP در نوع پروتکل استفاده شده می‌باشد.

### Update
برای آپدیت کردن سابسکریپشن از این گزینه استفاده نمایید.

### Edit
جهت ویرایش لینک سابسکریپشن از این گزینه استفاده نمایید.

### Delete
برای حذف سابسکریپشن از این گزینه استفاده نمایید.



## DNS Settings
در صفحه اصلی نرم‌افزار تنظیمات مربوط به DNS قرار دارد که با ورود به آن می‌توانید آن را تنظیم نمایید و سرور و نوع پروتکل استفاده شده را تغییر دهید.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/152bbbd5-a8a5-4a31-836a-7c2ea7ab3940" />

</div>


### DoH
پروتکلی است که DNS را بر بستر HTTPS ارائه می‌دهد. یعنی درخواست‌های DNS در قالب وب ارسال می‌گردد.

### DoT
در این پروتکل درخواست‌های DNS بر اساس پروتکل TCP ارسال می‌گردد.

### DoU
در این پروتکل درخواست‌های DNS بر اساس پروتکل UDP ارسال می‌گردد.


## Settings
در این صفحه تنظیمات کلی نرم‌افزار قرار دارد که در ادامه توضیح داده خواهند شد.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/989d8fce-4858-4bd1-b5fb-44c4bdac3895" />

</div>

### Import Configuration
برای افزودن فایل کانفیگ‌ها از دستگاه به صورت دستی از این گزینه استفاده نمایید.

### Export Configuration
برای انتقال کانفیگ ایمپورت شده از دستگاه به دستگاهی دیگر از این گزینه می‌توان استفاده نمود.

### Subscription
با فعال کردن گزینه `Update On Open` ، هنگام باز شدن نرم‌افزار به صورت خودکار سابسکریپشن آپدیت می‌گردد.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/068a0d24-c0f5-4cfd-9fa0-e37eb50acf20" />

</div>


### Reset
در این بخش می‌توانید تنظیمات مربوط به اپلیکیشن را ریست نمایید.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/8b336b0b-0c57-49e7-89e4-f86317955061" />

</div>

## فعال‌سازی فرگمنت
برای فعال‌سازی فرگمنت روی کانکشن‌های TLS می‌بایست در این نرم‌افزار روی کانکشن بزنید و گزینه Fragment را فعال کنید.
پارامترهای زیر برای تعیین در فیلدهای مربوطه پیشنهاد می‌شود.

<div align=center markdown=1>
<img src="https://github.com/hiddify/Hiddify-Manager/assets/125398461/055f8437-0bfa-45ce-96e4-f7cbd0026c4c" width="30%" />

</div>


<div dir=ltr markdown=1>
`packets: tlshello`

`length : 100-200`

`interval : 10-20`

</div>

بسته به اپراتور ممکن است نیاز باشد پارمترها را تغییر دهید یا نوع پکت‌ها را از tlshello به حالت `tcp segment 1-3` تغییر دهید. البته این حالت ممکن است زودتر شناسایی شود.
`packets: 1-3`