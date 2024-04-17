---
title: نحوه افزودن سرور (دامنه) میانی به هیدیفای منیجر
---

# نحوه افزودن سرور (دامنه) میانی به هیدیفای منیجر
فرض کنیم که شما سرور میانی خود را با استفاده از یکی از روش‌های زیر و یا هر روش دیگری راه‌اندازی نموده‌اید.

1. [راه‌اندازی سرور میانی با استفاده از سازنده سرور میانی هیدیفای (همه روش‌ها در یک اپ)](/fa/manager/domain-worker-cdn-and-tunneling/How-to-setup-relay-server-using-Hiddify-Relay-Builder/)
2. [راه‌اندازی سرور میانی به روش IP-Tables](/fa/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-IP-Tables-tunnel-as-relay-server/)
3. [راه‌اندازی سرور میانی به روش GOST](/fa/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-GOST-tunnel-as-relay-server/)
4. [راه‌اندازی سرور میانی به روش WST](/fa/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-WST-tunnel-as-relay-server/)
5. [راه‌اندازی سرور میانی به روش Dokodemo-Door](/fa/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-Dokodemo-Door-tunnel-as-relay-server/)
6. [راه‌اندازی سرور میانی به روش HA-Proxy](/fa/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-HA-Proxy-tunnel-as-relay-server/)

برای افزودن آن سرور به هیدیفای‌منیجر و استفاده از کانفیگ های آن کافیست مراحل زیر را دنبال نمایید.

## تعریف سرور میانی در هیدیفای‌منیجر
حالا برای آیپی سرور میانی (ایران) خود یک ساب‌دامین با پروکسی خاموش ثبت نمایید و آن را در هیدیفای‌منیجر روی حالت `سرور میانی` ثبت نمایید.
- ساب‌دامین ثبت شده را در فیلد `دامنه` قرار دهید و یک `نام نمایشی` نیز برای نمایش در کانفیگ‌ها می‌توانید تعیین نمایید.

<img src="https://github.com/hiddify/hiddify.com/assets/125398461/3f41d92a-04b9-44fb-b645-ac660601472a">

## افزودن کانفیگ‌های `سرور میانی` جهت استفاده به لینک سابسکریپشن

همانند همیشه در هیدیفای‌منیجر بهتر است کانفیگ‌ها را از لینک سابسکریپشن جدا کنید. بنابراین برای دامنه `سرور میانی` ثبت شده نیز می‌توانید در تنظیمات دامنه مربوط به سابسکریپشن، تیک مربوط به دامنه `سرور میانی` را بزنید تا کانفیگ‌های آن به دامنه سابسکریپشن اضافه گردند.

فرض شود که دامنه مربوط به سابسکریپشن `sublink.hiddify.com` باشد، مطابق با تصویر زیر جلو بروید تا کار انجام شود.

<img src="https://github.com/hiddify/hiddify.com/assets/125398461/3661045d-ced7-4694-916f-6ef160c63230">

حالا اگه صفحه کاربر را با دامین سابسکریپشن (در اینجا `sublink.hiddify.com`) باز نمایید خواهید دید که کانکشن‌های مربوط به `سرور میانی` نیز اضافه شده‌اند. می‌توانید این کانکشن‌ها را به صورت تک تک و یا با استفاده از لینک‌های سابسکریشن به کلاینت خود اضافه نمایید و استفاده نمایید.



