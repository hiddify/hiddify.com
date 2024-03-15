---
title: آموزش کار با نرم‌افزار Fair VPN

---

<div dir=rtl markdown=1>

# آموزش کار با نرم‌افزار Fair VPN


## افزودن لینک سابسکریپشن به نرم‌افزار

برای این کار به صفحه کاربری خود در پنل هیدیفای بروید. سپس در بخش مربوط به اپ `Fair VPN` لینک سابسکریپشن می‌بینید. 

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/1e4b67ca-ad95-43e1-b9d1-76af7e007822" />
</div>



روی دکمه `QR code` مربوط به` لینک برای Subscription b64` بزنید تا پنجره کوچک نشان داده شود. 





حالا دو امکان وجود دارد. 

## کپی کردن لینک

* می‌توانید گزینه `کپی` را انتخاب کنید

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/564d5f43-f2dd-4e0c-a79a-a2042a2db738" />
</div>

 * سپس وارد نرم‌افزار `Fair VPN` شوید و در تب `VPN` روی گزینه `Import VPN Configs` تپ کنید.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/3631c51e-15d7-44a6-bda0-c8df0b61c9d0" />
</div>

* لینک مربوط به سابسکریپشن را که کپی کرده بودید را در اینجا قرار دهید `OK` کنید. 

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/16c4e038-ab2f-4f01-86d6-8ed147180c93" />
</div>


بعد از چند ثانیه کانفیگ‌ها به نرم‌افزار اضافه می‌شوند. 


## اسکن کردن QR Code
 حالت بعدی وارد کردن لینک، استفاده از QR code می‌باشد. 
* برای این کار باید از منوی پایین نرم‌افزار در تب `VPN` گزینه `Add VPN by QR Code` را بزنید 

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/1107964d-22ff-4fd8-854c-32c09be13b1e" />
</div>

* سپس با استفاده از دوربین گوشی QR code مربوط را در صفحه کاربری پنل اسکن کنید. با این کار شما به حالت قبل کانفیگ‌ها به نرم‌افزار اضافه می‌شوند. 


<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/a6629f69-cdcc-404f-a8e0-f099a58a290c" />
</div>


## تست کانفیگ‌ها

برای تست کانفیگ‌ها از گزینه `Test VPN Latency` تپ کنید سپس گزینه `Test Web Latency` را بزنید. با این کار تست واقعی از کانکشن‌ها گرفته می‌شود و در کنار هر کانکشن نتیجه آن نمایش داده می‌شود. 

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/322b3680-e908-4a9d-8423-47ef3c50c1ff" />
</div>



## مرتب‌سازی کانفیگ‌ها بر اساس نتیجه تست

برای این کار از گزینه `Test VPN Latency` گزینه `Sort by Latency` را انتخاب کنید. با این کار کانکشن‌ها بر اساس نتیجه تست مرتب می‌شوند. 

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/04ef4c98-8dde-4da0-b0dd-2250ec32b8c7" />
</div>


## آپدیت کردن لینک سابسکریپشن
این برنامه این قابلیت را ندارد بنابراین در صورت نیاز به آپدیت لینک سابسکریپشن و کانفیگ‌ها باید از گزینه `Delete All VPN` استفاده کنید و مجدد لینک سابسکریپشن را اضافه نمایید. 

> نکته: اگر از قابلیت AutoCDN استفاده می‌کنید، برای آپدیت کانکشن‌ها و دریافت آیپی تمیز جدید باید همه کانکشن‌ها را با استفاده از `Delete All VPN` حذف کنید و سپس با VPN خاموش صفحه کاربری را رفرش کنید و مجددا لینک سابسکریپشن را به نرم‌افزار اضافه نمایید.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/6aef8018-ee10-414f-b889-f1dde61bdbe9" />
</div>

## قابلیت اشتراک‌گذاری اتصال VPN با دستگاه‌های موجود دیگر

فرض کنید نیاز دارید روی گوشی VPN را روشن کنید و دستگاه دیگری که نیاز به اتصال به اینترنت آزاد دارد ولی قابلیت نصب VPN را ندارد؛ متصل کنید. برای این کار کافیه در Fair VPN از دکمه `Local Sharing` استفاده کنید و آن را روشن کنید. بعد از آن یک پیغام به شمل زیر داده می‌شود. 

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/781db733-df3f-4190-baaa-5dd4dc529727" />
</div>


در دستگاه دوم کافیه در قسمت تنظیمات پروکسی دستگاه، روی آیپی و پورت داده شده تنظیمات را انجام بدهید تا انصال به VPN برقرار گردد. 


