---
title: Quick installation on Vultr Servers
---

<div dir="rtl" markdown=1>
# آموزش اتصال به سرور از طریق SSH

<details markdown="1"> <summary><h2> پیش نیاز: نصب SSH در ویندوز</h2> (کلیک کنید)</summary>

* اگر کلاینت شما ویندوز است؛ می توانید از پاورشل استفاده نمایید. ابتدا اگر تا کنون ماژول OpenSSH را نصب ننموده اید؛ پاورشل را با **دسترسی ادمین** باز کنید یعنی روی PowerShell راست کلیک کنید و Run as Administrator را بزنید. 

![image](https://user-images.githubusercontent.com/114227601/222904592-cd26b3bf-a014-4253-9488-ee9717f006fe.png)

سپس این دستور را اجرا کنید:


<div dir="ltr" markdown=1>
```
Add-WindowsCapability -Online -Name OpenSSH.Client
```
</div>
پس از آن چنین چیزی را باید مشاهده کنید:

![image](https://user-images.githubusercontent.com/114227601/222904870-e709f69e-1a8d-4a6d-ad6a-3d7bdcd917c3.png)

تبریک نصب ssh به پایان رسید
</details>


# نحوه اتصال و رفع عیب از طریق SSH


در صورتی که به هر دلیلی دسترسی نیاز به اتصال به سرور داشته باشید؛ در این حالت تنها راه اتصال به سرور و اعمال کانفیگ و تغییرات از طریق ترمینال است.


در این حالت نیاز است ابتدا به سرور SSH بزنید.
برای این کار:
با توجه به سیستم عامل خود یکی از برنامه های زیر را باز کنید.
- ویندوز: `PowerShell`
- مک: `Terminal`
- لینوکس : `Terminal` 

سپس از طریق اجرای دستور زیر به سرور متصل شوید:

<div dir="ltr" markdown=1>
```
ssh user@<IP_Address>
```
</div>

معمولا یوزر شما در سروری که خریداری کردید `root` هست فرض کنید IP سرور شما `1.1.1.1` هست پس دستور به شکل زیر میشه 
<div dir="ltr" markdown=1>
```
ssh root@1.1.1.1
```
</div>

<div dir="rtl" markdown=1>
اگر پورت دیفالت SSH را تغییر داده اید در این صورت باید کامند فوق را به این شکل تغییر دهید.

</div>

<div dir="ltr" markdown=1>
```
ssh root@<IP_Address> -p <port_number>
```

</div>

<div dir="rtl" markdown=1>
یعنی مثلا اگر آیپی شما `1.1.1.1`  و پورت `2222` باشد باید به این شکل کامند را اجرا کرد.

</div>

<div dir="ltr" markdown=1>
```
ssh root@1.1.1.1 -p 2222
```

</div>