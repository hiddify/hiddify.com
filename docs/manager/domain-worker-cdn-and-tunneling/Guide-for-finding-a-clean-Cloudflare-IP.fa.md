---
title: آیپی تمیز کلادفلر چیست و چگونه می‌توان آن را پیدا کرد
---

<div dir="rtl" markdown=1>
# چگونگی یافتن آیپی تمیز کلادفلر

بزرگترین ارائه دهنده خدمات CDN در جهان کلادفلر است و احتمالا می دانید؛ به دلیل فیلترینگ شدید اینترنت در ایران اختلال زیادی روی سرویس های آن وجود دارد زیرا امکان فیلتر نمودن کامل آن برای فیلترچی مقدور نیست اما می تواند روی آن اختلال ایجاد کند. 

در اینجا اگر شما نیز از سرویس های CDN کلادفلر استفاده می کنید؛ متاثر از این اختلالات خواهید شد. برای کاهش تاثیر این اختلالات می بایست آیپی های تمیز (آیپی هایی که اختلالی روی آن نیست) را پیدا کرد.

در اینجا چند راه کار برای این موضوع معرفی و بررسی می گردد.

نکته:
> قبل از شروع تاکید می شود تمامی این تست ها روی سیستم کلاینت و بدون اتصال به VPN باید انجام شوند.

فهرست مطالب:
- [اسکنر مرتضی باشسیز](#%D8%A7%D8%B3%DA%A9%D9%86%D8%B1-%D8%A2%DB%8C%D9%BE%DB%8C-%DA%A9%D9%84%D8%A7%D8%AF%D9%81%D9%84%D8%B1-%D9%85%D8%B1%D8%AA%D8%B6%DB%8C-%D8%A8%D8%A7%D8%B4%D8%B3%DB%8C%D8%B2)
- [اسکنر وحید فرید](#%D8%A7%D8%B3%DA%A9%D9%86%D8%B1-%D8%A2%DB%8C%D9%BE%DB%8C-%DA%A9%D9%84%D8%A7%D8%AF%D9%81%D9%84%D8%B1-%D9%88%D8%AD%DB%8C%D8%AF-%D9%81%D8%B1%DB%8C%D8%AF)
- [اسکنر صفا صفریان](#%D8%A7%D8%B3%DA%A9%D9%86%D8%B1-%D8%A2%DB%8C%D9%BE%DB%8C-%DA%A9%D9%84%D8%A7%D8%AF%D9%81%D9%84%D8%B1-%D8%B5%D9%81%D8%A7-%D8%B5%D9%81%D8%B1%DB%8C)
- [بعد از یافتن آیپی تمیز کلادفلر چه کار کنیم](#%D8%A8%D8%B9%D8%AF-%D8%A7%D8%B2-%DB%8C%D8%A7%D9%81%D8%AA%D9%86-%D8%A2%DB%8C%D9%BE%DB%8C-%D8%AA%D9%85%DB%8C%D8%B2-%DA%86%D9%87-%DA%A9%D8%A7%D8%B1-%DA%A9%D9%86%DB%8C%D9%85)

<br>

***

<br>

## اسکنر آیپی کلادفلر مرتضی باشسیز
آقای باشسیز یک مهندس ایرانی است که برنامه ای تحت عنوان CFScanner توسعه داده است که با استفاده از آن می توان لیست آیپی های کلادفلر را بر روی شبکه های مختلف تست نمود و به آیپی های تمیز کلادفلر رسید.

این برنامه در نسخه‌های متعدد از جمله لینوکس و ویندوز منتشر شده است.
نسخه‌های در دسترس تا تاریخ ویرایش این مطلب:
- بَش
- داکر
- ویندوز
- پایتون
- گولنگ
- اندروید

برای این کار در ابتدا از [اینجا](https://github.com/MortezaBashsiz/CFScanner) نسخه مدنظر خود را دانلود کنید و سپس نحوه اجرای آن را بر اساس سیستم عامل مورد نظر دنبال کنید.

</div>


<details dir=rtl><summary><h3>اجرا در نسخه لینوکس</h3>(کلیک کنید)</summary>

<div dir="rtl" align=center markdown=1>



<!--
https://www.youtube.com/watch?v=BKLRAHolhvM
-->


 فایل های برنامه را دانلود کنید و ابتدا توضیحات آقای باشسیز درباره نحوه اجرا را در ویدئوی زیر ببینید.

<a href="https://www.youtube.com/watch?v=cgV6uPBty90"><img width="50%" src="https://user-images.githubusercontent.com/125398461/234840939-ec06a505-0d37-45f3-b3b2-00f0a384cca0.png" /></a>

</div>

<div dir="rtl" markdown=1>
این برنامه پیش نیازهایی دارد که باید از قبل نصب باشند.
[jq](https://stedolan.github.io/jq/)&nbsp;&nbsp;&nbsp;[git](https://git-scm.com/)&nbsp;&nbsp;&nbsp;[tput](https://command-not-found.com/tput)&nbsp;&nbsp;&nbsp;[bc](https://www.gnu.org/software/bc/)&nbsp;&nbsp;&nbsp;[curl](https://curl.se/download.html)&nbsp;&nbsp;&nbsp;
[parallel](https://www.gnu.org/software/parallel/)


سپس ابتدا آن را با کد زیر روی سیستم خود clone کنید.

</div>

```
git clone https://github.com/MortezaBashsiz/CFScanner.git 
```


<div dir="rtl" markdown=1>
به پوشه دانلود برنامه بروید و به آن دسترسی اجرا دهید.
</div>

```
cd CFScanner/bash
chmod +x ../bin/*
```

<div dir="rtl" markdown=1>
فایل config.real را دانلود کنید.

</div>

```
curl -s https://raw.githubusercontent.com/MortezaBashsiz/CFScanner/main/bash/ClientConfig.json -o config.real
```

<div dir="rtl" markdown=1>
توصیه می شود فایل config.real را بر اساس کانفیگ خود تغییر دهید.
</div>

![Screenshot_20230305_094935](https://user-images.githubusercontent.com/125398461/222945619-756a8a4c-9cd7-4977-8679-c5a3a5b9b96c.png)

<div dir="rtl" markdown=1>
اگر می خواهید فایل کانفیگ خود را داشته باشید آن را به اسم دیگری ذخیره کنید که هنگام آپدیت اسکریپت تغییر نکند.

#### اجرای اسکریپت 

به محل فایل اسکریپت دانلود شده بروید و سپس اسکریپت را به شکل زیر اجرا کنید

</div>

```
bash cfScanner.sh SUBNET DOWN threads tryCount config.real speed custom.subnets
```


![](https://user-images.githubusercontent.com/125398461/222946688-bcec3d65-7bf1-495a-b1bf-fe517f69f882.png)
<div dir="rtl" markdown=1>مثلا
</div>

```
bash cfScanner.sh SUBNET DOWN 8 1 config.real 100 custom.subnets
```
<div dir="rtl" markdown=1>
در نهایت نتیجه تست در پوشه result قرار می گیرد که میتوانید آن را ملاحظه کنید و از آن استفاده نمایید. اطلاعات بیشتر در [ویکی](https://github.com/MortezaBashsiz/CFScanner/tree/main/bash) برنامه

</div>

</details>


<details dir=rtl><summary><h3>اجرا در نسخه ویندوز</h3>(کلیک کنید)</summary>



<details><summary><h4>پیش‌نیازها<h4></summary>

<div dir=rtl markdown=1>
ابتدا باید پیش‌نیازهایی وجود داشته باشند که به ترتیب توضیح داده خواهند شد:

- دانلود اپ اسکنر ویندوز از [گیتهاب پروژه](https://github.com/MortezaBashsiz/CFScanner/tree/main/windows)

- اپ .NET Desktop Runtime 6 را نصب کنید از سایت اصلی برنامه که در زیر آورده شده
‍‍‍‍
</div>

<div dir=ltr markdown=1>
```
https://dotnet.microsoft.com/en-us/download/dotnet/6.0
```

</div>

<div dir"rtl" markdown=1>
- چک نمودن TLS Handshake

برای این کار ابتدا باید وارد پوشه برنامه بشید و Command Prompt از داخل آن پوشه را باز نمایید. یعنی در پوشه `شیفت+راست‌کلیک` را بزنید و گزینه `Open in Windows Terminal` را بزنید. 

در محیط ترمینال کامند زیر را اجرا کنید.

</div>

<div dir=ltr markdown=1>
‍‍`.\v2ray.exe tls ping sub.yourdomain.com`


</div>

<div dir="rtl" markdown=1>
به جای `sub.yourdomain.com` ساب‌دامین خودتون را بذارید. اگر پیغام `handshake succeeded` ظاهر شد؛ یعنی اسکنر آماده استفاده است در غیر اینصورت باید در تنظیمات سرتیفیکت در سایت کلادفلر به صورت موقت تغییراتی اعمال کنید.

ورژن TLS را روی TLS 1.0 بذارید و گزینه TLS 1.3 را غیر فعال کنید.

![](https://user-images.githubusercontent.com/125398461/234774581-c1a07bdb-352f-43cc-97f7-2ce6c87a761d.png)

* نکته: یادتون نره بعد انجام تست این گزینه‌ها را به حالت اول برگردونید.


- ساختارهای الگوی کانفیگ را برای تست آماده کنید.

اگر می‌خواهید کانفیگ‌های خودتون را تست کنید باید در فایل Json مربوط به کانکشن درون پوشه برنامه اعمال کنید. نیاز است در `inbound` این تغییر اعمال گردد.

</div>


<div dir="ltr" markdown=1>
```

{
  "inbounds": [{
    "port": "PORTPORT", 
    "listen": "127.0.0.1",
    "tag": "socks-inbound",
    "protocol": "socks",
    "settings": {
...
```

</div>

<div dir=rtl markdown=1>
و همینطور در `outbound` نیز این تغییر اعمال گردد.

</div>

<div dir=ltr markdown=1>
```
{
"outbounds": [
   {
   "protocol": "vmess",
   "settings": {
     "vnext": [{
       "address": "IP.IP.IP.IP",
...
```
</div>


حالا برای راحتی کار، چند نمونه الگوی کانفیگ که iSegaro زحمت کشیده حاضر کرده؛ قرار داده می‌شه می‌توانید مطابق با نیازتون یکی را انتخاب کنید.

* دقت کنید در این ساختار ها فقط در قسمت `outbounds` باید مشخصات کانفیگ شامل ۵ قسمت `Port , UUID, PATH , HOST , SNI` را تغییر بدهید که با عبارت `xxxxx` مشخص شده , پس هرجا که عبارت `xxxxx` وجود داره رو فقط بسته به کانفیگ خودتون تغییر بدید و در باقی کدها تغییری انجام ندهید.

- نمونه الگوی Vmess+WS+TLS : 

<div dir=ltr markdown=1>
```
{
  "inbounds": [{
    "port": "PORTPORT", 
    "listen": "127.0.0.1",
    "tag": "socks-inbound",
    "protocol": "socks",
    "settings": {
      "auth": "noauth",
      "udp": false,
      "ip": "127.0.0.1"
    },
    "sniffing": {
      "enabled": true,
      "destOverride": ["http", "tls"]
    }
  }],
  "outbounds": [
    {
    "protocol": "vmess",
    "settings": {
      "vnext": [{
        "address": "IP.IP.IP.IP", 
        "port": xxxxx,
        "users": [{"id": "xxxxx" }]
      }]
    },
		"streamSettings": {
        "network": "ws",
        "security": "tls",
        "wsSettings": {
            "headers": {
                "Host": "xxxxx"
            },
            "path": "xxxxx"
        },
        "tlsSettings": {
            "serverName": "xxxxx",
            "allowInsecure": false,
			"fingerprint": "chrome",
			"alpn": [
			"http/1.1"
			]
        }
    }
	}],
  "other": {}
}
```
</div>

- نمونه الگوی Vless+GRPC+TLS :

<div dir=ltr markdown=1>
```
{
  "inbounds": [{
    "port": "PORTPORT", 
    "listen": "127.0.0.1",
    "tag": "socks-inbound",
    "protocol": "socks",
    "settings": {
      "auth": "noauth",
      "udp": false,
      "ip": "127.0.0.1"
    },
    "sniffing": {
      "enabled": true,
      "destOverride": ["http", "tls"]
    }
  }],
  "outbounds": [
    {
    "protocol": "vless",
    "settings": {
      "vnext": [{
        "address": "IP.IP.IP.IP", 
        "port": xxxxx,
        "users": [{"id": "xxxxx",
		"encryption": "none"
			}]
      }]
    },
		"streamSettings": {
        "network": "grpc",
        "security": "tls",
        "tlsSettings": {
          "allowInsecure": false,
          "serverName": "xxxxx",
          "alpn": [
            "http/1.1"
          ],
          "fingerprint": "chrome"
        },
        "grpcSettings": {
          "serviceName": "",
          "multiMode": false
        }
      }
	}],
  "other": {}
}
```

</div>

- نمونه الگوی Trojan+WS+TLS :

<div dir=ltr markdown=1>
```
{
  "inbounds": [{
    "port": "PORTPORT", 
    "listen": "127.0.0.1",
    "tag": "socks-inbound",
    "protocol": "socks",
    "settings": {
      "auth": "noauth",
      "udp": false,
      "ip": "127.0.0.1"
    },
    "sniffing": {
      "enabled": true,
      "destOverride": ["http", "tls"]
    }
  }],
  "outbounds": [
    {
      "tag": "proxy",
      "protocol": "trojan",
      "settings": {
        "servers": [
          {
            "address": "IP.IP.IP.IP",
            "method": "chacha20",
            "ota": false,
            "password": "xxxxx",
            "port": xxxxx,
            "level": 1,
            "flow": ""
          }
        ]
      },
      "streamSettings": {
        "network": "ws",
        "security": "tls",
        "tlsSettings": {
          "allowInsecure": false,
          "serverName": "xxxxx",
          "alpn": [
            "http/1.1"
          ],
          "fingerprint": "chrome"
        },
        "wsSettings": {
          "path": "xxxxx",
          "headers": {
            "Host": "xxxxx"
          }
        }
      },
      "mux": {
        "enabled": false,
        "concurrency": -1
      }
    }
  ],
  "other": {}
}
```

</div>

- نمونه الگوی Vless+WS+TLS :

<div dir=ltr markdown=1>
```
{
"inbounds": [{
    "port": "PORTPORT", 
    "listen": "127.0.0.1",
    "tag": "socks-inbound",
    "protocol": "socks",
    "settings": {
      "auth": "noauth",
      "udp": false,
      "ip": "127.0.0.1"
    },
    "sniffing": {
      "enabled": true,
      "destOverride": ["http", "tls"]
    }
  }],
  "outbounds": [
    {
      "tag": "proxy",
      "protocol": "vless",
      "settings": {
        "vnext": [{
        "address": "IP.IP.IP.IP", 
        "port": xxxxx,
        "users": [{"id": "xxxxx",
		"encryption": "none"
			}]
      }]
      },
      "streamSettings": {
        "network": "ws",
        "security": "tls",
        "tlsSettings": {
          "allowInsecure": false,
          "serverName": "xxxxx",
          "alpn": [
            "http/1.1"
          ],
          "fingerprint": "chrome"
        },
        "wsSettings": {
          "path": "xxxxx",
          "headers": {
            "Host": "xxxxx"
          }
        }
      }
    }
  ],
	"other": {}
}
```

</div>

در نهایت شما کانفیگ خودتون را طبق نمونه‌ها برای مرحله بعد حاضر کنید یا از کانفیگ دیفالت استفاده کنید.

</details>

حالا فرض  کنیم پیش‌نیازها را انجام دادید؛ کافیه فایل کانفیگ نمونه برنامه یا فایل کانفیگ ساخته شده توسط خودتون را که به فرمت Json است؛ از منوی `Tools > Add custom v2ray config` در برنامه قرار بدید تا اسکن بر اساس اون انجام بشه در غیر اینصورت برنامه با کانفیگ دیفالت اسکن می‌کند.

![](https://user-images.githubusercontent.com/125398461/234803794-7c7f5bb9-0967-4f1b-b519-9db266b7a0e7.png)

۱. از مسبر `Tools > Add custom v2ray config` می‌توانید فایل مورد نظر خود را مطابق با الگوی توضیح داده شده به نرم‌افزار بدید تا اسکن بر اساس اون انجام بشه.

۲. می‌توانید نوع تست دانلود یا آپلود یا هردو را تعیین کنید.

۳. در این قسمت می توانید تعداد همزمانی آیپی‌ها برای تست توسط اسکنر را مشخص کنید. پیشنهاد می‌گردد به صورت مرحله‌ای این عدد را بالا ببرید و بر اساس قدرت پردازش CPU سیستم خود آن را کم یا زیاد کنید. مثدار دیفالت آن ۴ می‌باشد.

۴. سریع‌ترین آیپی بعد از اتمام اسکن نمایش داده می‌شه

۵. رنج آیپی‌های تست شده نمایش داده می‌شه

۶. از این قسمت می‌تونید رنج آیپی‌های مورد نظر خود را به نرم‌افزار بدید که اسکن بر اساس آن انجام بشه.

* **پیشنهاد:** می‌تونید نرم‌افزار را تنظیم کنید که یک‌بار کل رنج آیپی دیفالت را اسکن کنه. برای دفعالت بعد می‌تونید این خروجی را فقط اسکن کنید (با دقت بالاتر) احتمالا نتیجه بهتری خواهید گرفت. همچنین اگر تست آپلود بگیرید احتمالا نتیجه بهتری خواهید گرفت. همه اینها به تلاش و خلاقیت خودتون بستگی داره.

</details>


***

<br>

<div dir="rtl" markdown=1>

## اسکنر آیپی کلادفلر وحید فرید
این برنامه در نسخه‌های مختلف بر اساس پلتفرم‌های متفاوت تهیه شده است که می‌توانید متناسب با نیازتان از آن‌ها استفاده نمایید.

نسخه‌های در دسترس تا تاریخ ویرایش این مطلب:
- مک
- ویندوز
- اندروید
- وب

<details dir=rtl><summary><h3>پیش‌نیازها</h3></summary>

* ابتدا پایتون را بر اساس سیستم عامل خود [دانلود](https://www.python.org/downloads/) کنید.
* فایل فشرده مربوط به کد را از [اینجا](https://github.com/vfarid/cf-ip-scanner-py) دانلود کنید و سپس آن را اکسترکت کنید.
* حالا نیاز هست requests را نیز نصب کنید.

<div dir="ltr" markdown=1>
```
pip install requests
```
</div>

</details>

<details dir=rtl><summary><h3>اجرای برنامه</h3></summary>

- جهت اجرا در پوشه اکسترکت شده برنامه ترمینال را باز نمایید. یعنی مثلا در ویندوز وارد پوشه برنامه شوید و ‍‍`شیفت+راست‌کلیک` کنید و سپس Open in Command Prompt را بزنید تا از آن پوشه وارد ترمینال شوید.

- حالا کامند زیر را بزنید تا برنامه اجر شود.

<div dir="ltr" markdown=1>
```
python start.py
```
</div>

- در ابتدا تعداد آیپی مورد نیاز را وارد می‌کنید.
- در مرحله بعد حداکثر تاخیر مورد نظر خود را بر حسب میلی ثانیه وارد کنید. مثلا ۵۰۰ یعنی ۵۰۰ میلی ثانیه
- رنج مورد نظر خود برای اسکن را می‌توانید انتخاب کنید. برای انتخاب چند رنج از کاما استفاده نمایید و برای نادیده گرفتن یک رنج از `-` استفاده کنید.
- می‌توانید چند رنج را از جستجو مستثنا کنید. برای انتخاب چند رنج از کاما استفاده نمایید و برای نادیده گرفتن یک رنج از `-` استفاده کنید.
- در مرحله بعد می توانید حجم بسته‌های ارسالی جهت اسکن را بر حسب کیلوبایت مشخص نمایید. هر چه این حجم بالاتر باشد، دقت اسکن بالاتر می‌رود اما از آن طرف، حجم ترافیک نیز افزایش می‌یابد.
- بر اساس نیازتان سرعت دانلود را تعیین کنید تا آیپی‌هایی که سرعت دانلودشان بالاتر از این مقدار است را پیدا کند. سرعت را بر اساس مگابیت بر ثانیه وارد کنید.
- در مرحله بعد سرعت آپلود را بر اساس نیازتان تعیین کنید تا آیپی‌هایی که سرعت آپلودشان بالاتر از این مقدار است را پیدا کند. این مقدار را بر اساس مگابیت بر ثانیه وارد کنید.
- در مرحله بعد در صورت نیاز می‌توانید نتایج اسکن شده را مستقیما وارد کلادفلر کنید یا اینکه آن را نادیده بگیرید تا اسکن شروع شود.
- در صورتی که در جواب مرحله قبل `y` زده‌اید، باید اینجا ایمیل متصل به اکانت خود در کلادفلر را بدهید.
- سپس در مرحله بعد `Zone ID` را کپی کنید. برای پیدا کردن `Zone ID` وارد تنظیمات دامنه در اکانت خود شوید سپس مانند تصویر زیر `Zone ID` را پیدا کنید و کپی کنید.
 
![](https://user-images.githubusercontent.com/125398461/235452066-9be0f0d9-e314-47cc-9565-4e05158b9d00.png)

- در این مرحله باید توکن گلوبال خود را به نرم‌افزار بدهید. برای این کار در همان صفحه اصلی داشبورد روی `Get your API token` کلیک کنید.

![](https://user-images.githubusercontent.com/125398461/235454090-7a23c21a-fd1a-4fe8-9eb9-d9343402929b.png)

* سپس در صفحه توکن‌ها در `Global API Key` گزینه `View` را انتخاب کنید.

![](https://user-images.githubusercontent.com/125398461/235454894-4e8bad4d-6561-4dec-9d5a-859ef0f64932.png)

* در اینجا از شما رمز اکانت‌تان را می‌خواهد و سپس توکن شما را نمایش می‌دهد.

![](https://user-images.githubusercontent.com/125398461/235455122-9d39781e-bb9b-4abb-8c77-a4b68a07f048.png)

* این توکن را در نرم‌افزار کپی کنید.

- سپس ساب‌دامین مورد نظر برای ثبت این آیپی‌ها روی دامنه خود را بدهید. مثلا `cf.yourdomain.com`
- پس از آن اسکنر شروع به اسکن می‌کند و در پایان آیپی‌ها بر اساس مشخصات داده شده به شما نمایش داده خواهد شد. همچنین اگر بخش مربوط به ثبت آیپی در کلادفلر را انجام داده باشید، این آیپی‌ها در کلادفلر هم روی ساب‌دامین مورد نظر ثبت می‌گردند. یعنی شما در کلادفلر ساب‌دامنه‌هایی خواهید داشت که با نام `cf.yourdomain.com` و با آیپی‌های یافته شده توسط اسکنر با پروکسی خاموش به صورت خودکار ثبت شده‌اند.

</details>

<details dir=rtl><summary><h3>ویدئوهای آقای فرید در این زمینه</h3></summary>
<a href="https://youtu.be/YCSwZG3cjAU"><img width="30%" src="https://user-images.githubusercontent.com/125398461/235457940-07eb8105-e8b2-46e6-a617-ebbf7e659af6.png" /></a> <a href="https://youtu.be/OO80Nx1bhOo"><img width="30%" src="https://user-images.githubusercontent.com/125398461/235457896-89222a93-00ab-44ef-a90a-526496c519d6.png" /></a> <a href="https://youtu.be/piKS04W6AHE"><img width="30%" src="https://user-images.githubusercontent.com/125398461/235457925-7354392b-d4d1-4150-bbc4-27f43e2f326c.png" /></a>


</details>

***
<br>

## اسکنر آیپی کلادفلر صفا صفری
این اسکنر در چند نسخه توسعه داده شده است که می‌توانید متناسب با نیازتون از آن استفاده کنید.

نسخه‌های در دسترس تا تاریخ ویرایش این مطلب:
- ویندوز
- مک
- اندروید
</div>

<details dir="rtl"><summary><h3>نصب اسکریپت</h3></summary>

<details dir="rtl"><summary><h4>ویندوز</h4></summary>

* ابتدا از [این لینک](https://www.python.org/downloads/windows/) پایتون را دانلود کنید.
* در هنگام نصب پایتون تیک مربوط به نصب pip و اضافه کردن پایتون به PATH را فراموش نکنید. 
*  [فایل اصلی اسکنر](https://github.com/SafaSafari/ss-cloud-scanner/archive/refs/heads/main.zip) فشرده را دانلود کنید و آن را از حالت فشرده خارج کنید.
* در مسیر اکسترکت شده یک ترمینال `Command Prompt` باز کنید. یعنی وارد مسیر اکسترکت شده شوید. `شیفت+راست‌کلیک` را بزنید تا ترمینال باز شود.
* برای  نصب پیش‌نیازها از کامند زیر استفاده کنید.

</div>

<div dir="ltr" markdown=1>
```
pip install -r ./requirements.txt
```

</div>

<div dir="rtl" markdown=1>
* بعد از نصب پیش‌نیازها کار تمام است و نوبت به اجرای برنامه می‌رسد.

</div>

</details>

<details dir="rtl"><summary><h4>اندروید</h4></summary>

* برای نصب روی سیستم عامل اندروید، نیاز به برنامه‌ای تحت عنوان ترموکس (Termux) می‌باشد که [از اینجا](https://github.com/termux/termux-app/releases/) می‌توانید دانلود کنید.
* در اینجا با چندین فایل apk مواجه می‌شوید که باید یکی را بر اساس نوع دستگاه خود انتخاب کنید. اگر نوع دستگاه اندرویدی خود را نمیدانید، نسخه armeabi-v7a را دانلود و نصب کنید.
* در ادامه با باز کردن برنامه ترموکس، خط فرمان به شما نشان داده میشود به ترتیب دستورات زیر را وارد کنید.
* در هنگان نصب تمام پرسش‌ها را با `y` جواب دهید.

</div>

<div dir="ltr" markdown=1>
```
pkg update -y; pkg install -y python python-pip openssl python-cryptography
```
</div>

<div dir="rtl" markdown=1>
* سپس کامند زیر را اجرا کنید.

</div>

<div dir="ltr" markdown=1>
```
curl -sLo main.zip https://github.com/SafaSafari/ss-cloud-scanner/archive/refs/heads/main.zip && unzip -qq main.zip && rm main.zip
```
</div>

<div dir="rtl" markdown=1>
* بعد از آن وارد پوشه برنامه شوید و پیش‌نیازها را نصب کنید.

</div>

<div dir="ltr" markdown=1>
```
cd ss-cloud-scanner-main
pip install -r ./requirements.txt
```

</div>

* بعد از نصب پیش‌نیازها کار تمام است و نوبت به اجرای برنامه می‌رسد.

</details>

</details>

<details dir="rtl"><summary><h3>اجرای اسکریپت</h3></summary>

* با دستور زیر، عملکرد برنامه آغاز می‌شود.

<div dir="ltr" markdown=1>
```
python main.py
```
</div>

* به محض اجرا، برنامه از شما تعداد آیپی مورد نیاز را درخواست می‌کند.
* در مرحله بعد نوع اسکن را می‌توان مشخص نمود.
* سپس از شما میپرسد که عملیات اسکن با `https` انجام بشود یا `http`.
* و سپس شروع به اسکن می‌کند و پس از مدتی آیپی‌های سالم (در صورت وجود) در صفحه ظاهر می‌شوند
* اگر نوع ۲ انتخاب بشود در ادامه از شما `uuid` و `دامنه` ، `پورت` ، `path` پروکسی مورد استفاده‌ را درخواست می‌کند و به محض وارد کردن آن‌ها در جاهای مورد نظر، عملیات اسکن شروع می‌شود. بدین ترتیب حالت ۲ با تنظیمات کانفیگ شما اسکن می‌کند.

#### حالت اسپید

این نوع از اسکن، با توجه به وایت لیست بودن SNI در ایران ([منبع](https://twitter.com/safasafari3/status/1643154352326975488)) از یک ورکر جایگزین استفاده می‌کند که بازدهی این مدل اسکن را به شدت بالا می‌برد

#### حالت Vmess
این مدل اسکن با ساخت پکت Vmess و ارسال آن به سمت سرور با Websocket عملا یک ارتباط پروکسی را شبیه سازی میکند اسکنر های جایگزین، این کار با استفاده از هسته های V2ray یا Xray انجام میدهند، اما این اسکنر این اقدام را بصورت خالص با پایتون پیاده سازی نموده است.


[منبع اصلی](https://github.com/SafaSafari/ss-cloud-scanner)

</details>




***
<br>

<div dir="rtl" markdown=1>
## بعد از یافتن آیپی تمیز چه کار کنیم؟

پس از یافتن آیپی تمیز؛ می توانید آن را با یک رکورد dns بدون پروکسی ثبت نمایید. یعنی در سایت کلادفلر یک ساب دامین بسازید. پروکسی را خاموش کنید و آیپی را وارد کنید.

![Screenshot_20230302_171704](https://user-images.githubusercontent.com/125398461/222942018-f53bf1bd-77c4-45b5-9604-0224061869d0.png)
در صورت نیاز به توضیحات بیشتر درباره دامنه [اینجا](/manager/wiki/%D8%A7%D9%86%D9%88%D8%A7%D8%B9-%D8%AF%D8%A7%D9%85%D9%86%D9%87-%D9%88-%D9%86%D8%AD%D9%88%D9%87-%D8%AB%D8%A8%D8%AA-%E2%80%8C%D8%A2%D9%86%E2%80%8C%D9%87%D8%A7) کلیک کنید.

سپس در پنل هیدیفای می توانید آن را در تنظیمات دامنه CDN در فیلد **اجبار به استفاده از هاست در کانفیگ CDN**  قرار دهید. [توضیحات بیشتر](/manager/wiki/%D9%86%D8%AD%D9%88%D9%87-%D9%BE%DB%8C%DA%A9%D8%B1%D8%A8%D9%86%D8%AF%DB%8C-%D9%BE%D9%86%D9%84-%D9%87%DB%8C%D8%AF%DB%8C%D9%81%D8%A7%DB%8C#%D8%AF%D8%A7%D9%85%D9%86%D9%87-cdn)

![Screenshot_20230301_095103](https://user-images.githubusercontent.com/125398461/222942200-ce36835f-41d9-4bc9-abf5-a4c35c34d33f.png)

</div>

