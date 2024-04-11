---
title: آموزش راه‌اندازی تانل Dokodemo-door به عنوان سرور میانی
---

# آموزش راه‌اندازی تانل Dokodemo-door به عنوان سرور میانی

برای این کار شما به یک سرور میانی نیاز دارید تا از طریق آن به سرور اصلی متصل شوید. معمولا این سرور میانی در کشور محل اقامت شما در نظر گرفته می‌شود.
<div align=center dir="rtl" markdown="1">
 
<img src="https://user-images.githubusercontent.com/125398461/235339506-bdd76cec-0378-4942-8352-ebebeb006231.png">
</div>


- به  سرور میانی [SSH بزنید](https://github.com/hiddify/Hiddify-Manager/wiki/SSH-%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%A7%D8%AA%D8%B5%D8%A7%D9%84-%D8%A8%D9%87-%D8%B3%D8%B1%D9%88%D8%B1-%D8%A7%D8%B2-%D8%B7%D8%B1%DB%8C%D9%82) و دستور نصب هسته Xray اجرا کنید

```
sudo bash -c "$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)" @ install
```

- پس از نصب باید فایل `config.json` را با دستور زیر ایجاد نمایید.

```
nano /usr/local/etc/xray/config.json
```

- حالا کد زیر که مربوط به ترافیک `inbound` و `outbound` تانل dokodemo-door است را ملاحظه فرمایید.

```
{
  "inbounds": [
    {
      "listen": "127.0.0.1",
      "port": 62789,
      "protocol": "dokodemo-door",
      "settings": {
        "address": "127.0.0.1"
      },
      "tag": "api"
    },
    {
      "listen": null,
      "port": Main_Server_Port,
      "protocol": "dokodemo-door",
      "settings": {
        "address": "MAIN_SERVER_IP",
        "followRedirect": false,
        "network": "tcp,udp",
        "port": MAIN_SERVER_PORT
      },
      "tag": "inbound-MAIN_SERVER_PORT"
    }
  ],
  "outbounds": [
    {
      "protocol": "freedom"
    },
    {
      "protocol": "blackhole",
      "tag": "blocked"
    }
  ]
}
```
   در قسمت پورت `MAIN_SERVER_PORT` پورت سرور اصلی خود (هیدیفای) را قرار دهید که برای اتصال تانل در آن سرور در نظر گرفتید.
   به طور مثال پورت ۴۴۳ توسط هیدیفای به صورت دیفالت برای کانشکن‌ها استفاده می‌شود.
   در قسمت `MAIN_SERVER_IP`  بایستی آیپی سرور  اصلی خود را قرار دهید.

- به عنوان مثال اگر آیپی سرور شما `10.10.10.10` باشد و پورت آن `443` باشد بنابراین کد `inbound` به شکل زیر خواهد بود:

```
{
  "inbounds": [
    {
      "listen": "127.0.0.1",
      "port": 62789,
      "protocol": "dokodemo-door",
      "settings": {
        "address": "127.0.0.1"
      },
      "tag": "api"
    },
    {
      "listen": null,
      "port": 443,
      "protocol": "dokodemo-door",
      "settings": {
        "address": "10.10.10.10",
        "followRedirect": false,
        "network": "tcp,udp",
        "port": 443
      },
      "tag": "inbound-443"
    }
  ],
  "outbounds": [
    {
      "protocol": "freedom"
    },
    {
      "protocol": "blackhole",
      "tag": "blocked"
    }
  ]
}
```


پس از انجام عملیات کانفیگ دکمه `Ctrl + s` زده تا تغییرات ذخبره شود و `Ctrl + x` بزنید تا از فایل `config.json` خارج شوید.

##### تعریف چند inbound مختلف در سرور میانی برای اتصال به چند سرور اصلی

برای این کار کافیه در کد مربوط به `config.json` بعد از اتمام هر `inbound` یک `inbound` جدید تعریف نمایید. به عنوان مثال فرض شود دو سرور اصلی داریم که آیپی سرور اول `10.10.10.10` و پورت آن `443` آیپی سرور دوم `20.20.20.20` و پورت آن `8443` است. برای ایجاد دو تانل مستقل به این سرورها باید به شکل زیر دو `inbound`  ایجاد شود.

```
{
  "inbounds": [
    {
      "listen": "127.0.0.1",
      "port": 62789,
      "protocol": "dokodemo-door",
      "settings": {
        "address": "127.0.0.1"
      },
      "tag": "api"
    },
    {
      "listen": null,
      "port": 443,
      "protocol": "dokodemo-door",
      "settings": {
        "address": "10.10.10.10",
        "followRedirect": false,
        "network": "tcp,udp",
        "port": 443
      },
      "tag": "inbound-443"
    }
   {
      "listen": null,
      "port": 8443,
      "protocol": "dokodemo-door",
      "settings": {
        "address": "20.20.20.20",
        "followRedirect": false,
        "network": "tcp,udp",
        "port": 8443
      },
      "tag": "inbound-8443"
    }
  ],
  "outbounds": [
    {
      "protocol": "freedom"
    },
    {
      "protocol": "blackhole",
      "tag": "blocked"
    }
  ]
}
```

- پس از ذخیره فایل دستور ریستارت هسته Xray را بزنید.

```
sudo systemctl restart xray
```

## تعریف سرور میانی در هیدیفای
حالا برای آیپی سرور میانی (ایران) خود یک ساب‌دامین با پروکسی خاموش ثبت نمایید و آن را در هیدیفای روی حالت Relay ثبت نمایید.

<img src="https://user-images.githubusercontent.com/125398461/235341283-97c026b7-1d70-4362-8950-1e5c1b79d508.png">

## افزودن کانفیگ‌های Relay جهت استفاده به لینک سابسکریپشن

همانند همیشه در هیدیفای بهتر است کانفیگ‌ها را از لینک سابسکریپشن جدا کنید. بنابراین برای دامنه Relay ثبت شده نیز می‌توانید در تنظیمات دامنه مربوط به سابسکریپشن، تیک مربوط به دامین Relay را بزنید تا کانفیگ‌های آن به دامنه سابسکریپشن اضافه گردند.

فرض شود که دامنه مربوط به سابسکریپشن t1.hiddify.com باشد، مطابق با تصویر زیر جلو بروید تا کار انجام شود.
<img src="https://user-images.githubusercontent.com/125398461/235342038-cfda2574-2444-4414-843d-2ed507537d1d.png">

حالا اگه صفحه کاربر را با دامین سابسکریپشن (در اینجا t1.hiddify.com) باز نمایید خواهید دید که کانکشن‌های مربوط به Relay نیز اضافه شده‌اند. می‌توانید این کانکشن‌ها را به صورت تک تک و یا با استفاده از لینک‌های سابسکریشن معمولی یا سابسکریپشن b64 به کلاینت خود اضافه نمایید و استفاده نمایید.

## حذف کانفیگ dokodemo از سرور میانی

- برای این کار ابتدا این کامند را اجرا کنید.

```
sudo rm /usr/local/etc/xray/config.json
```

- سپس هسته Xray را متوقف و حذف کنید.

```
sudo systemctl stop xray && systemctl disable xray
````

- در نهایت برای حذف کامل برنامه و سرویس این کامندها را بزنید.

```
bash -c "$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)" @ remove
```

