---
title: نصب سریع و آسان در Microsoft Azure
weight: -50
---


<div dir="rtl" markdown="1">
در این مقاله به شما آموزش میدهیم چگونه یک فیلترشکن اختصاصی ایجاد کنید.


## ایده کلی
شرکت هایی مثل مایکروسافت و دیجیتال اوشن برای دانشجوها حدود 100 دلار کردیت یکساله رایگان (قابل تمدید) ارائه میکنند

ما از این کردیت رایگان استفاده میکنیم تا دو پروکسی برای خانواده خود ایجاد کنیم

- یک پروکسی برای تلگرام
- یک پروکسی برای عبور از فیلتر سایر اپلیکیشن ها و برنامه ها

## مراحل
### مرحله 1: ایجاد یک اکانت دانشجویی در مایکروسافت Azure


ابتدا وارد سایت [Microsoft Azure](https://azure.microsoft.com/en-us/free/students/) شوید
و مراحل زیر را مطابق گیف زیر انجام دهید:

![](http://hiddify.github.io/assets/create_student_account.gif)

برای مشاهده میزان اعتبار باقیمانده در حساب کاربری خود از لینک زیر اقدام کنید
[مشاهده اعتبار دانشجویی در azure](https://www.microsoftazuresponsorships.com/Balance)

### مرحله 2: ساخت یک ماشین مجازی در Azure برای تلگرام

  
بر روی این آیکون
<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fhiddify%2Fconfig%2Fmain%2Ftelegram%2Ftelegram-vm-azure-template.json" target="_blank"><img src="https://aka.ms/deploytoazurebutton"/></a>
کنید
و مطابق گیف زیر مراحل را ادامه دهید.


![](https://github.com/hiddify/hiddify.github.io/raw/main/assets/azure-auto-deploy.gif)
<div class="alert alert-success" markdown=1>و لینک پروکسی تلگرام را از قسمت `output` کپی کنید. فراموش نکنید که این لینک پاک می شود پس آن را در جای امنی ذخیره کنید
</div>






  
### مرحله 3: ساخت یک ماشین مجازی در Azure برای پروکسی سایت ها و اپلیکیشن ها

  
بر روی این آیکون
<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fhiddify%2Fconfig%2Fmain%2Fshadowsocks%2Fss-azure-template.json" target="_blank"><img src="https://aka.ms/deploytoazurebutton"/></a>
کنید
و مطابق گیف قبل مراحل را ادامه دهید.

<div class="alert alert-success" markdown=1>و لینک پروکسی را از قسمت `output` کپی کنید. فراموش نکنید که این لینک پاک می شود پس آن را در جای امنی ذخیره کنید
</div>
سپس لینک را باز کرده تا آموزش استفاده از پروکسی نمایش داده شود. 


</div>