---
title: آموزش استفاده از API در هیدیفای‌منیجر
---


# آموزش استفاده از API در هیدیفای‌منیجر

در اینجا راهنمای استفاده از API در هیدیفای ارائه می‌‌گردد که در دو بخش کار با یوزرهای معمولی و کار با یوزرهای ادمین می‌آید.

* برای دریافت لیست همه یوزرها
 ``` 
GET https://site.com/proxy_path/admin_key/api/v1/user/
``` 

* برای گرفتن یک یوزر خاص
``` 
 GET https://site.com/proxy_path/admin_key/api/v1/user/?uuid=6ebd2ea8-4d41-48b7-8fc2-7d6570
``` 

* برای ایجاد یا آپدیت یوزر

``` 
POST https://site.com/proxy_path/admin_key/api/v1/user/
        {
            "uuid": "6ebd2ea8-4d41-48b7-8fc2-7d6570da30a9",
            "name": "Test",
            "added_by_uuid": "abb4bdb8-732c-4fa6-92e0-6b3fd4bb8450",
            "current_usage_GB": 0,
            "usage_limit_GB": 1,
            "package_days": 900,
            "start_date": null,
            "comment": null,
            "last_online": "1-01-01 00:00:00",
            "last_reset_time": "2023-05-21",
            "mode": "no_reset",
            "telegram_id": null
        }
``` 
> نکته: فیلد ed25519_private_key و ed25519_public_key اختیاری است و در صورتی که نباشد توسط سیستم تولید می‌شود.

* برای گرفتن همه یوزرهای ادمین
``` 
GET https://site.com/proxy_path/admin_key/api/v1/admin/
``` 
* برای گرفتن  یک یوزر ادمین
``` 
GET https://site.com/proxy_path/admin_key/api/v1/admin/?uuid=abb4bdb8-732c-4fa6-92e0-6b3fd4bb8450
``` 
* برای ایجاد یا آپدیت یوزر ادمین
``` 
POST https://site.com/proxy_path/admin_key/api/v1/admin/
        {
            "uuid": "0749f63d-16c1-4bdf-8d4f-180bcd4cdef6",
            "can_add_admin": false,
            "mode": "agent",
            "name": "Hiddify-Admin",
            "parent_admin_uuid": "abb4bdb8-732c-4fa6-92e0-6b3fd4bb8450",
            "comment": null,
            "telegram_id": null
        }
``` 
* فرمت url مربوط به یوزر
``` 
https://site.com/proxy_path/uuid/
``` 
* برای گرفتن لینک کوتاه صفحه‌ی کاربر
```
GET https://site.com/proxy_path/user_uuid/short/
```
* برای گرفتن اطلاعات کاربر
```
GET https://site.com/proxy_path/user_uuid/info/
```
* برای گرفتن لیست پروکسی های تلگرام کاربر
```
GET https://site.com/proxy_path/user_uuid/mtproxies/
```
* برای گرفتن لینک تمام کانفیگ های کاربر
```
GET https://site.com/proxy_path/user_uuid/all-configs/
```
