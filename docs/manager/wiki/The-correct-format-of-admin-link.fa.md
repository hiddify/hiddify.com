[**🇺🇸 English**](/manager/wiki/The-correct-format-of-admin-link)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/manager/wiki/%D9%87%D9%85%D9%87-%D8%A2%D9%85%D9%88%D8%B2%D8%B4%E2%80%8C%D9%87%D8%A7-%D9%88-%D9%88%DB%8C%D8%AF%D8%A6%D9%88%D9%87%D8%A7"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/3704cd84-eee6-4c45-abe7-3c02936bbebb" /></a>
<div dir="rtl" markdown=1>

# فرمت صحیح لینک ادمین
یا توجه به اینکه لینک مربوط به ادمین و همینطور سایر لینک های برنامه از قسمت های مختلفی تشکیل شده است و در تنظیمات می توان آن ها را تغییر دارد؛ لازم است اینجا توضیحاتی در خصوص فرمت صحیح لینک ادمین داده شود.

در حالت کلی لینک ادمین چنین فرمتی دارد:
</div>

https://sub.domain.com/DrtGho0n4b8H9D/8bncvfb5-8193-vv76-ab97-4c35965l250m/admin/
![](https://user-images.githubusercontent.com/125398461/230101702-4c15ce6d-ced7-4e07-83ea-b505fc725b60.png)





<div dir="rtl" markdown=1>
هر کدام از قسمت ها با "/" از همدیگر جدا می شوند که در ادامه تشریح می گردند.

> ابتدای لینک که پروتکل سایت را مشخص می کند. اگر از https  استفاده شده باشد؛ به این معنی است که ارتباط کلاینت و سرور توسط یه سرتیفیکیت TLS رمزگذاری می شود و ارتباط امن است. اگر از http استفاده شده باشد؛ به این معنی است که ارتباط کلاینت و سرور بدون رمزگذاری برقرار شده است که پیشنهاد نمی گردد. بنابراین توصیه اکید می گردد حتما از لینک های https جهت ارتباط با سرور استفاده نمایید.

> پس از آن آدرس ساب دامین به همراه دامین وجود دارد که این ساب دامین می تواند دایرکت یا CDN و یا Relay باشد. [توضیحات بیشتر در خصوص انواع دامنه](/manager/wiki/%D8%A7%D9%86%D9%88%D8%A7%D8%B9-%D8%AF%D8%A7%D9%85%D9%86%D9%87-%D9%88-%D9%86%D8%AD%D9%88%D9%87-%D8%AB%D8%A8%D8%AA-%E2%80%8C%D8%A2%D9%86%E2%80%8C%D9%87%D8%A7)

> بعد از آن مسیر مخفی پروکسی قرار دارد که این مسیر در منوی تنظیمات؛ قسمت تنظیمات پیشرفته قرار دارد و قابل تغییر است.

> قسمت بعدی رمز ادمین است که این رمز را می توان در منوی تنظیمات؛ تنظیمات ادمین ویرایش کرد.

> قسمت انتهایی لینک ادمین آدرس صفحه است که باadmin به انتها میرسد.

حال صفحات زیر مجموعه این صفحه هر کدام در ادامه می توانند اضافه شوند. به عنوان مثال صفحه یوزرها می تواند به این فرمت باشد

</div>

https://sub.domain.com/DrtGho0n4b8H9D/8bncvfb5-8193-vv76-ab97-4c35965l250m/admin/user/

<div dir="rtl" markdown=1>
* چنانچه بعد از پایان نصب اولیه از طریق ترمینال؛ لینک های ادمین داده شده به فرمت گفته شده بالا نبودند؛ مشخص می شود که نصب به درستی انجام نشده است.
* همچنین اگر تغییری در رمز ادمین صورت گیرد این لینک تغییر می کند

* همچنین اگر مسیر مخفی پروکسی تغییر کند این آدرس تغییر می کند

</div>