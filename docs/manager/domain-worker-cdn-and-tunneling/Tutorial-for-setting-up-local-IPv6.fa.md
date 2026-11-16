---
title: آموزش ایجاد IPv6 لوکال برای سرور میانی
---

<div markdown="1">

# آموزش ایجاد IPv6 لوکال برای سرور میانی

در بعضی از سرورهای میانی ممکن است IPv6 ارائه نشده باشد و شما می‌تونید با این روش یک IPv6 لوکال ایجاد کنید که از آن در تونل‌های خود استفاده نمایید.



!!! note "نکته"
    آدرس‌های زیر (`fd00:900::1` و `fd00:900::2`) آدرس‌های IPv6 خصوصی (محلی) هستند؛ می‌توانید آدرس‌های دیگری از بازهٔ `fd00::/8` هم بگذارید. نسخه‌های قبلی این آموزش از `2001:db9:900::` استفاده می‌کردند که یک بازهٔ عمومی است: اگر با آن تنظیم کرده‌اید، آن را به یک آدرس خصوصی تغییر دهید.

## سرور میانی

برای ایجاد IPv6 لوکال نیاز است ابتدا سرویس `iproute2` در سرور میانی با دستور زیر نصب کنید.

```shell
sudo apt-get install iproute2
```

بعد از نصب سرویس بالا با ادیتور `nano` فایل `tunnel.yaml` را در پوشه `netplan` ایجاد کنید.

```shell
sudo nano /etc/netplan/tunnel.yaml
```

سپس کد زیر ر در فایل کپی کنید.


```yaml
network:
  version: 2
  tunnels:
    tunnel98:
      mode: sit
      local: IPv4-RELAY
      remote: IPv4-MAIN
      addresses:
        - fd00:900::1/64
```


- به جای `IPv4-RELAY` آی‌پی سرور میانی خود را قرار دهید و به جای `IPv4-MAIN` آی‌پی سرور اصلی خود را قرار دهید.
- بعد از اعمال تغییرات با زدن دکمه `Ctrl+s` فایل را ذخیره کنید و با زدن دکمه `Ctrl+x` از ادیتور خارج شوید.
- در انتها با دستور زیر تغییرات ایجاد شده در `netplan` را اعمال کنید.


```
sudo netplan apply
```

## سرور اصلی
برای ایجاد IPv6 لوکال در سرور اصلی نیز نیاز است که سرویس `iproute2` نصب کنید.

```shell
sudo apt-get install iproute2
```

بعد از نصب سرویس بالا با ادیتور `nano` فایل `tunnel.yaml` را در پوشه `netplan` ایجاد کنید.

```shell
sudo nano /etc/netplan/tunnel.yaml
```

سپس کد زیر را در فایل کپی کنید.

```yaml
network:
  version: 2
  tunnels:
    tunnel98:
      mode: sit
      local: IPv4-MAIN
      remote: IPv4-RELAY
      addresses:
        - fd00:900::2/64
```

- مجددا به جای IPv4-RELAY آی‌پی سرور میانی را قرار دهید و به جای IPv4-MAIN آی‌پی سرور اصلی خود را قرار دهید.
- بعد از اعمال تغییرات با زدن دکمه `Ctrl+s‍` فایل را ذخیره کنید و با زدن دکمه `Ctrl+x` از ادیتور خارج شوید.
- در انتها با دستور زیر تغییرات ایجاد شده در netplan را اعمال کنید.

```
sudo netplan apply
```

- کار تمام است.
  
در این روش IPv6های لوکال به شرح زیر هستند.

سرور میانی شما: 

```
fd00:900::1
```
سرور اصلی شما : 

```
fd00:900::2
```


## تست ارتباط

برای تست ارتباط کافیست از سرور اصلی خودتان IPv6 لوکال سرور میانی را پینگ نمایید:

```
ping fd00:900::1
```

!!! tip "فایروال"
    این تونل از پروتکل IP شمارهٔ ۴۱ (SIT) استفاده می‌کند. اگر فایروال هیدیفای‌منیجر (**تنظیمات** › **تنظیمات عمومی** › **فایروال**) یا فایروال دیگری روشن باشد، تونل را مسدود می‌کند. روی هر دو سرور، سرور دیگر را مجاز کنید؛ مثلا روی سرور اصلی: `iptables -I INPUT -p 41 -s IPv4-RELAY -j ACCEPT` (و روی سرور میانی با `-s IPv4-MAIN`). اگر بعد از اعمال تغییرات در پنل تونل قطع شد، این دستور را دوباره اجرا کنید. [تنظیم فایروال](/fa/manager/basic-concepts-and-troubleshooting/How-to-setup-Firewall-on-Hiddify-panel/)
    
## طریقه استفاده

شما میتونید در سرور میانی خود از تونل [`Dokodemo-Door`](/fa/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-Dokodemo-Door-tunnel-as-relay-server/) یا [`GOST`](/fa/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-GOST-tunnel-as-relay-server/) استفاده کنید
و بجای IP یا دامنه از IPv6 لوکالی که برای سرور اصلی و خارج ایجاد کرده‌اید، استفاده نمایید.

مثال `Dokodemo-Door` :

```json

{
   "inbounds": [
     {
       "listen": "127.0.0.1",
       "port": 62789,
       "protocol": "dokodemo-Door",
       "settings": {
         "address": "127.0.0.1"
       },
       "tag": "api"
     },
     {
       "listen": null,
       "port": 443,
       "protocol": "dokodemo-Door",
       "settings": {
         "address": "fd00:900::2",
         "followRedirect": false,
         "network": "tcp,udp",
         "port": 443
       },
       "tag": "inbound-IPv6-local"
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




اگر دقت کنید در مثال بالا در فیلد `address` مقدار IPv6 لوکال ایجاد شده برای سرور اصلی قرار داده شده و در قسمت `port` مقدار 443 وارد شده که می‌توانید `port` را به پورت تونل شده تغییر داد.

برای آموزش نحوه افزودن سرور (دامنه) میانی به هیدیفای‌منیجر [این مقاله](/fa/manager/domain-worker-cdn-and-tunneling/How-to-add-relay-domain-to-Hiddify-manager/) را مطالعه نمایید.

## مقاله‌های مرتبط

- [IPv6 اصلی سرور برای تونل پایدارتر](/fa/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-IPv6-to-improve-Relay-stability/)
- [تونل 4to6](/fa/manager/domain-worker-cdn-and-tunneling/Setup-ip4toip6-tunnel/)
- [انواع دامنه و ثبت آن‌ها](/fa/manager/domain-worker-cdn-and-tunneling/Domain-types-and-how-to-register-them/)
- [دامنهٔ فیک](/fa/manager/domain-worker-cdn-and-tunneling/How-to-create-and-use-fake-domain/)

</div>
