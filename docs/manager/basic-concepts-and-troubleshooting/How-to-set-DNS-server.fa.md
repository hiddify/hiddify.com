---
title: آموزش تنظیم DNS سرور در هیدیفای‌منیجر
---

<div dir="rtl" markdown=1>

# آموزش تنظیم DNS سرور

همانطور که احتمالا می‌دانید، DNS سرویسی است که وظیفه آن تبدیل نام‌ها به آیپی‌هاست. یعنی زمانی که شما مثلا `google.com` را می‌خواهید باز کنید، این نامه ابتدا به سرور DNSی که در کامپیوتر شما تنظیم شده است ارسال می‌شود. سپس آن سرور آیپی مربوط به این نام را به سیستم شما برمی‌گرداند. و درنهایت درخواست بازشدن سایت با استفاده از آیپی ارسال می‌گردد.

<div align=center markdown=1>
  
<img width=50% src="https://github.com/hiddify/hiddify-config/assets/125398461/8b1ce774-3268-4c42-ae0a-02553feb3b26" />
</div>



بنابراین تنظیم سرور DNS در سرور و کلاینت و هرجایی که قصد استفاده از سرویس‌های اینترنتی را دارد، بسیار مهم است.

## سرورهای DNS معروف در جهان
این سرورهای که به صورت جهانی سرویس می‌دهند متعلق به شرکت‌های بزرگ از جمله گوگل و کلادفلر هستند. پیشنهاد می‌شود برای دسترسی راحت به VPN خود حتما از این سرورها استفاده نمایید.

`1.1.1.1` مربوط به کلادفلر

`8.8.8.8` مربوط به گوگل

## تنظیم DNS از طریق پنل
برای این کار به بخش تنظیمات پنل بروید و در قسمت تنظیمات عمومی سرور مورد نظر خود را قرار در قسمت `سرور DNS` قرار دهید. کار تمام است.

<div align=center markdown=1>
  
<img src="https://github.com/hiddify/hiddify-config/assets/125398461/49b3b5a5-8b7a-42d4-8bac-6593c7c50ada" />
</div>


پنل به صورت خودکار سرور مربوط به کلادفلر را برای شما تنظیم کرده است و البته پیشنهاداتی نیز در پایین آن قرار داده است که می‌توانید آن‌ها را در صورت نیاز اعمال کنید.

## تنظیم DNS از طریق SSH
اگر به هر دلیل مایل به استفاده از SSH برای انجام این تنظیمات بودید، [به سرور خود SSH بزنید](/fa/manager/installation-and-setup/How-to-connect-to-server-via-SSH/) و سپس با `ctrl+c` از منوی هیدیفای خارج شوید.

* در محیط ترمینال این کامند را تایپ کنید تا تنظیمات قبلی DNS سرور حذف شود.

<div dir="ltr" markdown=1>
  
```
sudo rm /etc/resolv.conf
```
</div>

* سپس برای ایجاد و تغییر تنظیمات DNS سرور، این کامند را تایپ کنید تا ویرایشگر متنی nano باز شود.

<div dir="ltr" markdown=1>
  
```
sudo nano /etc/resolv.conf
```
</div>

* سپس nameservers که در اینجا به سرور DNS اشاره می‌کند را ادیت نمایید و به شکل زیر تغییر دهید.

<div dir="ltr" markdown=1>
  
```
nameserver 8.8.8.8
nameserver 1.1.1.1
```
</div>

* برای ذخیره `ctrl+s` و برای خروج `ctrl+x` را بزنید.
* حالا باید کاری کنید که این فایل توسط سیستم قابل تغییر نباشد. برای این کار از دستور زیر استفاده کتید.


<div dir="ltr" markdown=1>
  
```
chattr +i /etc/resolv.conf
```
</div>

* کار تمام است. 



## تست نشتی DNS در سرور
ساده‌ترین ابزار برای تست نشتی در سرور استفاده از `nslookup` است.
- ابتدا اگر `nslookup` نصب نیود، با این دستور آن را نصب کنید.

<div dir="ltr" markdown=1>
  
```
sudo apt install dnsutils
```
</div>

- برای انجام تست باید  یک دامنه مثلا google.com را با استفاده از این ابزار تست کنید.

<div dir="ltr" markdown=1>
  
```
nslookup google.com
```
</div>

* اگر خروجی کامند به شکل زیر بود، یعنی کار به درستی انجام شده است و نشتی DNS روی سرور اتفاق نمی‌افتد.

<div align=center markdown=1>
  
![Screenshot_20230624_064021](https://github.com/hiddify/hiddify-config/assets/125398461/3ef15d0b-54b0-43ce-8be5-a5229054d1fb)
</div>

همانطور که می‌بینید در بخش `Server` اولین سرور یعنی `8.8.8.8` که در فایل مربوط به تنظیمات قرار داده شده، نمایش داده می‌شود.
در اینجا نباید غیر از سرورهای تعیین شده چیز دیگری مشاهده کنید. در غیر اینصورت، باید یک بار دیگر مراحل بالا را به درستی انجام دهید. [اطلاعات بیشتر درباره نشتی DNS](/fa/manager/basic-concepts-and-troubleshooting/How-to-check-and-prevent-DNS-leaks/)
</div>
