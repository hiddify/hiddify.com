# آموزش ایجاد IPv6 لوکال
در بعضی از سرورهای ایران ممکنه IPv6 ارائه نشه و شما میتونید با این روش یک IPv6 لوکال ایجاد کنید.


# سرور ایران

برای ایجاد IPv6 لوکال نیاز اول سرویس iproute2 در ایران با دستور پایین نصب کنید:
```shell
sudo apt-get install iproute2
```
بعد از نصب سرویس بالا با ادیتور `nano` فایل `tunnel.yaml` ایجاد کنید:
```shell
sudo nano /etc/netplan/tunnel.yaml
```

کد پایین رو در فایل کپی کنید:

```yaml
network:
  version: 2
  tunnels:
    tunnel98:
      mode: sit
      local: IPv4-IRAN
      remote: IPv4-Main
      addresses:
        - 2001:db9:900::1/64
 ```

بجای `IPv4-IRAN` ای پی سرور ایران را قرار دهید و بجای `IPv4-Main` ای پی سرور خارج خود را قرار دهید.
بعد از اعمال تغییرات با زدن دکمه `ctrl+s` فایل را ذخیره کنید و با زدن دکمه `ctrl+x` از ادیتور خارج شوید.
در انتها با دستور زیر تغییرات ایجاد شده در `netplan` را اعمال کنید:
```
sudo netplan apply
```

# سرور خارج

برای ایجاد IPv6 لوکال نیاز که سرویس iproute2 در سرور خارج هم نصب کنید:
```shell
sudo apt-get install iproute2
```

بعد از نصب سرویس بالا با ادیتور `nano` فایل `tunnel.yaml` ایجاد کنید:
```shell
sudo nano /etc/netplan/tunnel.yaml
```

کد پایین رو در فایل کپی کنید:
```yaml
network:
  version: 2
  tunnels:
    tunnel98:
      mode: sit
      local: IPv4-Main
      remote: IPv4-IRAN
      addresses:
        - 2001:db9:900::2/64
```

دوباره بجای IPv4-IRAN ای پی سرور ایران را قرار دهید و بجای IPv4-Main ای پی سرور خارج خود را قرار دهید.
بعد از اعمال تغییرات با زدن دکمه ctrl+s فایل را ذخیره کنید و با زدن دکمه ctrl+x از ادیتور خارج شوید.
در انتها با دستور زیر تغییرات ایجاد شده در netplan را اعمال کنید:

```
sudo netplan apply
```

خب تمومه 
در این روش IPv6 لوکال ایران شما : 

```
2001:db9:900::1
```
و IPv6 لوکال سرور اصلی و خارج شما : 

```
2001:db9:900::2
```


# تست ارتباط

برای تست ارتباط کافیه از سرور اصلی و خارج خودتون IPv6 لوکال ایران پینگ کنید:

```
ping 2001:db9:900::1
```

# طریقه استفاده

شما میتونید در سرور ایران خودتون از تانل `Dokodemo-Door` یا `GOST` استفاده کنید
و بجای IP یا دامنه از IPv6 لوکالی که برای سرور اصلی و خارج خودتون ایجاد کردید رو قرار بدید

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
         "address": "2001:db9:900::2",
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


در مثال بالا اگر دقت کنید در فیلد `address` مقدار IPv6 لوکال ایجاد شده برای سرور اصلی یا خارج را وارد شده و در قسمت `port` مقدار 443 وارد شده که می توانید `port` را به پورت تانل شده تغییر بدید.
