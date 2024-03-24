---
title: آموزش استفاده از سایت PHP برای لینک ساب
---

# ایجاد یک سایت PHP برای انتقال اطلاعات مربوط به لینک‌های سابسکریپشن

## هدف از ایجاد سایت PHP برای لینک‌های سابسکریپشن
هیدیفای‌منیجر بر این اساس پایه‌گذاری شده است که احتمال فیلتر شدن سرور را تا جای ممکن کاهش یابد. یکی از راه‌های کاربردی در این زمینه، جدا کردن کانفیگ‌ها از لینک‌های سابسکریپشن یا اشتراک است. در این صورت همیشه کلاینت شما آخرین اطلاعات کانفیگ‌ها را از طریق لینک سابسکریپشن دریافت می‌کند. حالا فرض کنید به هر دلیل لینک سابسکریپشن در دسترس نبود، در این صورت می‌توان یک سایت PHP بالا آورد و از آن برای انتقال اطلاعات لینک‌های سابسکریپشن (و نه کانفیگ) استفاده کرد. شماتیک انجام این کار به شکل زیر است.

<div align=center markdown=1>

![php site for sub-link](https://github.com/hiddify/hiddify.com/assets/125398461/1430314a-570b-4b27-b4ac-4196649f3edd)
</div>

## مراحل انجام کار
برای ایجاد یک سایت PHP و استفاده از آن برای لینک سابسکریپشن ابتدا باید در [گوگل سرچ](https://www.google.com/search?q=free+php+hosting) کنید و سایت‌های رایگان ارائه دهنده سرویس PHP رایگان را پیدا کنید. 

- یکی از سایت‌ها را انتخاب کنید. 
- در آن اکانت خود را ایجاد کنید. 
- سپس یک سرویس میزبانی PHP را در آن ایجاد کنید. این کار در سایت‌های مختلف مراحل مشابهی دارد و تقریبا ساده است. برای ایجاد این سرویس می‌بایست یک آدرس منحصر به فرد روی یکی از دامنه‌های آن ارائه‌دهنده بسازید. 
- بعد از آن سرویس شما ایجاد می‌گردد. 
- بعد از ایجاد سرویس، روی فایل‌های آن ویرایش بزنید و دو فایل زیر را در مسیر اصلی سرویس خود قرار دهید. 

> - نکته: اگر هر کدام از فایل‌های `htaccess.` و `index.php` را مشاهده نمی‌کنید، باید این فایل‌ها را به صورت دستی ایجاد کنید.

> - دقت شود که فایل `htaccess.` یک نقطه قبل از اسم آن دارد و اگر آن را ایجاد می‌نمایید، این نکته را در نظر بگیرید.

**کد برای فایل `htaccess.`**
```
RewriteEngine On
RewriteRule ^(.*)$ index.php?url=$1 [L]
```

**کد برای فایل `PHP`**

```php
<?php

if (!isset($_SERVER['HTTPS']) || $_SERVER['HTTPS'] !== 'on') {
    http_response_code(403);
    exit('Access Forbidden - HTTPS is required.');
}

$server_domain = "https://hiddify-sub-only-domain.com";

$domain = $_SERVER['HTTP_HOST'];
$ip = $_SERVER['HTTP_CF_CONNECTING_IP'] ?? $_SERVER['HTTP_X_FORWARDED_FOR'] ?? $_SERVER['REMOTE_ADDR'];
$url = $server_domain . $_SERVER['REQUEST_URI'];
$userAgent = $_SERVER['HTTP_USER_AGENT'];

$ch = curl_init();
curl_setopt_array($ch, [
    CURLOPT_URL => $url,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_SSL_VERIFYPEER => false,
    CURLOPT_SSL_VERIFYHOST => 2,
    CURLOPT_HEADERFUNCTION => function($curl, $header) {
        header($header);
        return strlen($header);
    },
]);

$headers = [
    "CF-Connecting-IP: $ip",
    "Host: $domain",
    "User-Agent: $userAgent",
];
foreach ($_SERVER as $key => $value) {
    if (strpos($key, 'HTTP_') === 0) {
        $header = str_replace('_', '-', substr($key, 5));
        $headers[] = "$header: $value";
    }
}
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

$response = curl_exec($ch);
if (curl_errno($ch)) {
    http_response_code(500);
    exit('Internal Server Error');
}

curl_close($ch);
echo $response;

?>

```

دقت شود:
>  در کد PHP بالا دامنه سابسکریپشن خود را جایگزین نمایید.

> در تنظیمات سایت PHP، ورژن PHP بر روی 8 به بالا باشد.

> گزینه CURL در تنظیمات PHP هاست شما روشن باشد.


- سپس تنظیمات را ذخیره کنید. 
-  در این مرحله اگر تنظیمات ssl برای دامنه خود در این ارائه‌دهنده PHP را چک کنید؛ احتمالا متوجه خواهید شد که مقداری زمان می‌گیرد تا سرتیفیکت به آن تخصیص داده شود. 
- حالا برای استفاده؛ لینک مربوط به دامین ساخته شده خود در این ارائه دهنده را کپی کنید و سپس از لینک ادمین خود در پنل بخش بعد از آدرس را کپی کنید و به انتهای لینک PHP خود بچسبانید. پنل با آدرس PHP باز می‌گردد. 
مثلا فرض کنید دامینه PHP شما این است:

https://hello2freeworld.phpsite.com

و لینک ادمین پنل شما اینطوری باشد:

https://t1.hiddify.com/koZlk3E8P59Ghf8R/ab56bgt8-737c-4fd6-9oe0-6d4fa4bb84c0/admin/

آدرس PHP شما برای رسیدن به پنل به این صورت خواهد بود:

https://hello2freeworld.phpsite.com/koZlk3E8P59Ghf8R/ab56bgt8-737c-4fd6-9oe0-6d4fa4bb84c0/admin/

> نکته خیلی مهم: اگر دامنه PHP شما در سایت ارائه‌دهنده هنوز سرتیفیکت نگرفته باشد؛ این آدرس با https باز نمی‌شود و برای تست می‌توانید با http آن را باز کنید اما برای استفاده حتما از https استفاده نمایید. بنابراین باید منتظر بمانید تا سرتیفیکت تخصیص داده شود.

- بعد از انجام تست بالا، دامنه را در هیدیفای‌منیجر خود در قسمت دامنه‌ها ثبت نمایید تا سرور برای آن SSL بگیرد و ارتباط آن کاملا امن گردد.

- بعد از انجام این کار، این لینک را به عنوان لینک سابسکریپشن می‌توانید به اپ‌های کلاینت خود اضافه نمایید. 
- کار تمام است. اکنون شما آدرسی دارید که به سرور شما متصل گردیده و عملا غیر قابل فیلتر است.





