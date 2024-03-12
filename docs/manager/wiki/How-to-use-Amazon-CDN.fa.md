

<div dir="rtl" markdown="1">

# استفاده از CDN آمازون یا Cloudfront
## ثبت دامنه
* برای این کار ابتدا یک رکورد A به آدرس سرور خود در  DNS پوینت کنید. فرضا `sub1.domain.com` را به آدرس آیپی سرور خود پوینت کرده‌اید.


* به سایت [Amazon AWS](https://aws.amazon.com/) رفته و سرویس Cloudfront را جستجو نمایید.
* با زدن create distribution یک مقصد ایجاد نمایید.
* در صفحه باز شده مطابق با تصویر زیر مقادیر را وارد نمایید.

<div align=center markdown=1>
<img alt="aws settings" src="https://github.com/hiddify/Hiddify-Manager/assets/125398461/9e1623b7-ffdc-4881-be24-b7223c63cb90" width=70% />
</div>

تمام مقادیر در این صفحه به صورت پیش‌فرض است به جز موارد زیر که باید همانند تصاویر تعیین شوند.


<div align=center markdown=1>
<img alt="protocols policy" src="https://github.com/hiddify/Hiddify-Manager/assets/125398461/322d696e-cc53-4272-87ec-b5f77baa1546" width=70% />
</div>


<div align=center markdown=1>
<img alt="cache policy" src="https://github.com/hiddify/Hiddify-Manager/assets/125398461/404b3134-de2d-4dca-a942-a524b43ed883" width=70% />
</div>

<div align=center markdown=1>
<img alt="waf settings" src="https://github.com/hiddify/Hiddify-Manager/assets/125398461/3139e115-5c4f-41df-9d49-766e973a4d14" width=70% />
</div>

* در انتها بر روی `create distribution` بزنید تا عملیات ایجاد انجام شود.
* در مرحله بعد به محل ثبت رکوردهای DNS خود بروید. فرضا اگر در کلادفلر ثبت نموده‌اید، وارد بخش DNS دامنه خود شوید و یک رکورد cname ایجاد نمایید. فرضا `sub2.domain.com` را ایجاد نموده و مقدار آن را معادل دامنه ایجاد شده در مرحله قبل در AWS قرار دهید. این مقدار در بخش `details` و تحت عنوان `Distribution domain name` قابل مشاهده است.

در واقع این ساب‌دامنه برای دامنه CDN مورد نظر ما استفاده خواهد شد.

* به پنل AWS برگشته و در صفحه مربوط به مقصد در تب `General` از قسمت `setting` گزینه `edit` را بزنید و در صفحه باز شده بخش `Alternate domain name (CNAME) - optional` بر روی `Add item` کلیک کنید و دامنه cname مرحله قبل یعنی `sub2.domain.com` را وارد نمایید.

## گرفتن سرتیفیکت
* وارد بخش `Custom SSL certificate - optional` شده و برای دامنه مورد نظر `ssl certificate` دریافت نمایید. برای این کار بر روی `Request certificate` کلیک نمایید.
* در صفحه جدید باز شده مراحل دریافت سرتیفیکتن را ادامه داده و در بخش `domain name` و فیلد مربوط به آدرس، مشخصات ساب‌دامین ثبت شده در مرحله قبل یعنی `sub2.domain.com` را وارد نماییدو سایر مقادیر را به صورت پیش‌فرض قرار داد و روی `Request` بزنید.

* در صفحه لیست سرتیفیکت‌ها می‌بینید که وضعیت دامنه مورد نظر بر روی `pending validation` قرار دارد. بر روی ID کلیک کرده و در صفحه باز شده قسمت `Domains` را مشاهده نمایید.


<div align=center markdown=1>
<img alt="domain settings" src="https://github.com/hiddify/Hiddify-Manager/assets/125398461/e2a5d38a-efde-45c5-b55b-d2f395aa846a" width=70% />
</div>


* در این قسمت برای تکمیل وضعیت سرتیفیکت به دو مقدار این بخش یعنی `Cname name` و `Cname value` نیاز است.
* به محل ثبت رکوردهای DNS خود (فرضا کلادفلر) بروید و یک رکورد `Cname name` ایجاد نمایید و مقادیری که در مرحله قبل در AWS داشتید را وارد نمایید. در کلادفلر به جای `name` مقدار `Cname name` و به جای `Target` مقداری `Cname value` را وارد کنید.
* حالا اگر به AWS و صفحه لیست سرتیفیکت برگشته و صفحه را رفرش کنید، می‌بینید که وضعیت از حالت `pending` به `issues` تغییر یافته است و این بدان معناست که دامنه ما به درستی سرتیفیکت را دریافت نموده است.
* حالا به صفحه تنظیمات `distribution` و مرحله دریافت سرتیفیکت برگشته و اگر دکمه رفرش مربوط به `custom ssl` را بزنید، می‌توان سرتیفیکتی که در مرحله قبل دریافت نموده‌اید را مشاهده کنید. آن را انتخاب نمایید و مقادیر دیگر این صفحه را به حالت پیش‌فرض باقی بگذارید.



> [!نکته]
> نکته: دقت شود که تیک مربوط به `Legacy client support` را نزید چون این گزینه ماهیانه ۶۰۰ دلار هزینه دارد.

* در انتها گزینه save changes را بزنید تا تغییرات ذخیره گردد.
* حالا صبر کنید تا تغییرات انجام شده اعمال گردند و طبق تصویر زیر وضعیت `Last modified` از `Depoloying` به حالت انجام شده به تاریخ و ساعت تغییر می‌کند.

<div align=center markdown=1>
<img alt="done page" src="https://github.com/hiddify/Hiddify-Manager/assets/125398461/893cfd82-7ccc-4fe6-9b25-09da4272e9a3" width=70% />
</div>

* معمولا بین ۲-۵ دقیقه زمان می‌برد که این تغییرات اعمال گردند که با صفحه رفرش قابل پگیری است. همیشه به یاد داشته باشید در هر مرحله‌ای که تغییرات ایجاد می‌کنید باید به این وضعیت تغییر پیدا کند که به این مفهوم است که تغییرات کاملا اعمال شده و قابل بهره‌برداری است.

* تبریک کار تمام است. CDN کلودفرانت آمازون با موفقیت راه‌اندازی شد. حالا کافیه دامنه CDN خود را در هیدیفای منیجر خود ثبت نمایید.