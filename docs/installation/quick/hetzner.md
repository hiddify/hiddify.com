---
sidebar_position: 3
id: quick-install-hetzner
title: نصب در Hetzner
tags:
  - نصب سریع
  - hetzner
---

import YouTube from "react-youtube";

# نصب سریع در Hetzner

### ویدئوی‌ آموزشی مراحل نصب

<YouTube videoId="vQ-NAfRXTZo" opts={{ width: "100%" }} />

---

## مراحل نصب

1. روی Add Server کلیک کنید
   ![image](https://user-images.githubusercontent.com/114227601/206861285-58832cec-a2a3-441e-91d4-8300d16584d6.png)

2. حالا کد زیر را کپی کنید

```
#cloud-config
package_upgrade: true
packages:
  - apt-transport-https
  - ca-certificates
  - curl
  - wget
  - gnupg-agent
  - software-properties-common
  - git

runcmd:
  - cd /opt
  - git clone https://github.com/hiddify/hiddify-config/
  - cd hiddify-config
  - bash install.sh

final_message: "The system is finally up, after $UPTIME seconds"
output: { all: "| tee -a /root/cloud-init-output.log" }

# you can see the generated link from the website by using http://yourip/ or https://yourip.sslip.io in one hour, after that, it will be disapear.
```

3. کد بالا را در محل نشان داده در عکس قرار دهید.
   ![image](https://user-images.githubusercontent.com/114227601/206861304-656682b4-17a3-44c1-89f9-7b0d89566728.png)

4. پس از حداکثر 10 تا 15 دقیقه سرور شما آماده و پروکسی فعال خواهد بود مطابق عکس
   آی پی خود را کپی کنید و در مرورگر باز کنید

![image](https://user-images.githubusercontent.com/114227601/206861323-1de41700-6ce4-403a-a644-0836e2a22876.png)

5. یادتون نره حداقل 10 دقیقه صبر کنیدا

6. در آخر باید دامنه را تنظیم کنیم و نصب را **نهایی** کنیم. برای اینکار به صفحه [نهایی کردن نصب](/docs/installation/finalize) بروید.
