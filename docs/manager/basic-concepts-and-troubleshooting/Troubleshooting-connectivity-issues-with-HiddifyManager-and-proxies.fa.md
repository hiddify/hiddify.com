---
title: عیب‌یابی مشکلات اتصال با هیدیفای‌منیجر و پراکسی‌ها
---

# عیب‌یابی مشکلات اتصال با هیدیفای‌منیجر و پراکسی‌ها
چرا با وجود نصب هیدیفای‌منیجر کانکشن‌های من وصل نمی‌شوند؟

یا داستان چیه که با رایتل وصل میشه ولی مثلا با ایرانسل وصل نمیشه؟

برای پاسخ به این سوالان این مقاله را تا انتها دنبال کنید.


همانطور که در مقدمات پیکربندی هیدیفای‌منیجر گفته شده، این موضوع چند دلیل بیشتر ندارد:

> ۱. آیپی یا دامنه بلاک شده است.
> 
> ۲. آیپی نیمه‌بلاک و در لیست زرد قرار گرفته شده است. مثلا در بعضی ISPها وصل و در بعضی وصل نیست.
> 
> ۳. اگر از دامین CDN استفاده شده است، آیپی کلادفلر تمیزی انتخاب نشده است. 
> 

بنابراین این پنل قرار نیست معجزه بکند. نصب آن مقدماتی نیاز دارد. حتما قبل از پیکربندی پنل، مطمئن شوید آیپی و یا دامنه شما سالم است.[نحوه تست](/fa/manager/basic-concepts-and-troubleshooting/How-to-make-sure-the-server%27s-IP-or-domain-is-clean/) 


اگر از دامنه CDN استفاده می‌شود نیاز است [آیپی تمیز کلادفلر](/fa/manager/domain-worker-cdn-and-tunneling/Guide-for-finding-a-clean-Cloudflare-IP/)  پیدا کنید و در فیلد اجباری دامنه در منوی دامنه‌ها قرار دهید. 


اگر شما توانسته اید از یک ابزار دیگه، روی همون سرور و همون دامنه، متصل بشید، بلافاصله اون لینک تروجان یا وی لس یا وی مس را برای ما بفرستید تا توی پنل اضافه کنیم




# راه کارهایی برای حل مشکل
- [آیپی سالم پیدا کنید](/fa/manager/basic-concepts-and-troubleshooting/How-to-make-sure-the-server%27s-IP-or-domain-is-clean/)
- [دامنه ی جدیدی استفاده کنید](/fa/manager/domain-worker-cdn-and-tunneling/Domain-types-and-how-to-register-them/)
- [می‌توانید از CDN استفاده کنید](/fa/manager/domain-worker-cdn-and-tunneling/What-is-CDN-and-how-does-it-help-us%3F/)
- [میتوانید از Relay استفاده کنید](/fa/manager/domain-worker-cdn-and-tunneling/How-to-add-relay-domain-to-Hiddify-manager/)
- [از دامنه ی Fake استفاده کنید](/fa/manager/domain-worker-cdn-and-tunneling/How-to-create-and-use-fake-domain/)



