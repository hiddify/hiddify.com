---
title: آموزش استفاده از CDN GCore
---


<div dir="rtl" markdown=1>
  
# آموزش استفاده از CDN GCore بر روی دامنه ثبت شده در Cloudflare

همانطور که می‌دانید برای استفاده بهینه از هیدیفای‌منیجر نیاز است یک ارائه دهنده CDN استفاده نمایید تا با استفاده از سرویس‌های آن بتوان فیلترینگ را دور زد. در مطالب دیگر ما Cloudflare را معرفی و نحوه کار با آن را آموزش دادیم. این سرویس به دلیل اختلالات گسترده‌ای که در ایران بر روی آن ایجاد می‌شود؛ بعضی اوقات کار را برای کاربران مشکل می‌کند. یک راه جایگزین استفاده از سرویس CDN شرکت GCore می‌باشد. برای آشنایی با نحوه تنظیمات آن این مقاله را تا انتها مطالعه نمایید.

۱. ابتدا به [اینجا](https://gcore.com) بروید و اکانت خود را در سایت GCore بسازید. سپس وارد اکانت ساخته شده بشوید و در داشبورد خود گزینه CDN را بزنید.

![1](https://user-images.githubusercontent.com/125398461/235283540-83a44dbc-6b81-45d2-a04f-be2749cf0429.jpg)

۲. در مرحله بعد پلن رایگان را انتخاب نمایید و `Next` کنید.

![2](https://user-images.githubusercontent.com/125398461/235283581-a392f93e-4d8a-44d9-9521-be83fb09564b.jpg)

۳. پس از تکمیل مشخصات خواسته شده بر روی گزینه `Get started` کلیک کنید.

![3](https://user-images.githubusercontent.com/125398461/235283590-6654cae1-cc3b-42c6-ae8c-d4cc26b71a15.jpg)

۴. در مرحله بعد بر روی `Create CDN resource` بزنید.

![4](https://user-images.githubusercontent.com/125398461/235283617-042ee013-e1a1-4567-aa6c-fcbf1080fa99.jpg)

۵. حال در صفحه باز شده بر روی `Confirm` کلیک کنید.

![5](https://user-images.githubusercontent.com/125398461/235283626-b7923519-ffbc-425b-a65b-3063e19595a1.jpg)

۶. در این مرحله دامنه‌ای را که در کلاد فلر ثبت نموده‌اید را به همراه ساب‌دامنین دلخواه وارد کنید.

![6](https://user-images.githubusercontent.com/125398461/235283639-ef21b5ba-5efd-48d5-a852-7aa8050b4316.jpg)

۷. سپس آیپی سرور خود را وارد کنید و بر روی گزینه Add بزنید.

![7](https://user-images.githubusercontent.com/125398461/235283674-400d9213-029a-429b-9985-699c0bd40ba3.jpg)

۸. در مرحله بعد مجددا بر روی Confirm کلیک کنید.

![8](https://user-images.githubusercontent.com/125398461/235283679-fbb415e0-5b12-4880-be94-3f2a17ba5895.jpg)

۹.  از آنجایی که شما قصد استفاده از CDN GCore را دارید، نیازی به ثبت nameserverهای GCore بر روی دامنه خود ندارید و فقط بر روی `Confirm` کلیک کنید.

![9](https://user-images.githubusercontent.com/125398461/235283686-69d71bb4-2c27-4375-8a04-3a7f2f1fac21.jpg)

۱۰. در این مرحله مجدد بر روی `Confirm` کلیک کنید.

![10](https://user-images.githubusercontent.com/125398461/235283803-1ca531c7-efb6-4bf2-ba21-5f68de3cc9df.jpg)

۱۱. سپس بر روی گزینه `Open resource settings` بزنید.

![11](https://user-images.githubusercontent.com/125398461/235283807-225d6325-b388-4a21-9b41-5da3f7457ba9.jpg)

۱۲. در صفحه باز شده بر روی گزینه `DNS` کلیک کنید.

![12](https://user-images.githubusercontent.com/125398461/235283814-711cf947-256c-4cda-8cc5-236abe8a6b31.jpg)

۱۳. حالا روی دامنه خود کلیک کنید تا لیست رکوردهای ثبت شده را نمایش دهد.

![13](https://user-images.githubusercontent.com/125398461/235283822-62ce802c-d7c2-44e8-8fd6-a418fe6a04c2.jpg)

۱۴. در مرحله بعد برای ویرایش رکورد CDN دکمه مداد را بزنید.

![14](https://user-images.githubusercontent.com/125398461/235283921-81cfdb21-b00b-4e94-907d-3a6b95f7b650.jpg)

۱۵. در این مرحله بر روی گزینه `CDN Integration` بزنید تا یکپارچه سازی CDNها را انجام دهید. 

![15](https://user-images.githubusercontent.com/125398461/235284019-0301d8e3-d882-4482-9c75-23a30e4fb2f1.jpg)

۱۶. حالا دامنه‌ای که در بخش `CDN Integration` وجود دارد را کپی کنید.

![16](https://user-images.githubusercontent.com/125398461/235284138-6355a421-a7da-46c8-803a-b4b65cdc8fb1.jpg)

۱۷. حالا وارد اکانت کلادفلر خود شوید، وارد تنظیمات دامنه‌ی خود شوید و در بخش DNS یک رکورد `CNAME` با استفاده از دامنه‌ای که خود در بخش قبل کپی کرده بودید، ثبت نمایید. دقت شود که تیک پروکسی برای این رکورد خاموش باشد.

![17](https://user-images.githubusercontent.com/125398461/235284172-560987a3-8528-497a-89c9-58927fddc327.jpg)

۱۸. مجدد وارد داشبورد خود در سایت GCore شده و در بخش CDN پس از اطمینان از Active بودن آن، بر روی دامنه‌ی بر روی دامنه‌ی خود کلیک کنید.

> نکته: ممکن است `Active` شدن کمی زمان بگیرد.

![18](https://user-images.githubusercontent.com/125398461/235284405-71b9fe26-e25c-4750-b349-1fac9cd34efb.jpg)

۱۹. سپس در بخش `Origin`، تنظیمات `Origin pull protocol` را بر روی `HTTPS` تنظیم نمایید.

![19](https://user-images.githubusercontent.com/125398461/235284438-6d4e0c6e-79dc-4175-8718-8a85b68b46d1.jpg)

۲۰. حالا برای گرفتن سرتیفیکت در سربرگ `SSL`، بر روی گزینه `Get SSL certificate` بزنید.

![20](https://user-images.githubusercontent.com/125398461/235284577-e0ee7fbb-31d9-476b-9901-f2fb78c5c22d.jpg)

۲۱. دریافت سرتیفیکت ممکن است حدودا ۱۵ دقیقه زمان ببرد. پس از گرفتن سرتیفیکت، شما پیغامی مبنی بر استفاده و تمدید خودکار آن مشاهده خواهید کرد.

![21](https://user-images.githubusercontent.com/125398461/235284579-898335c0-28d3-477f-b900-3f8a381bcdda.jpg)

۲۲. حالا می‌توانیم از این ساب‌دامین به عنوان دامنه CDN در هیدیفای‌منیجر استفاده کنید.

![22](https://user-images.githubusercontent.com/125398461/235284966-63477444-51d0-45dd-be27-2307f43df54f.jpg)

* نکته پایانی و مهم: یادتون نره که CDN GCore در پلن رایگان محدودیت ۱۰۰۰ گیگابایتی دارد.
