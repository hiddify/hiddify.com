[**🇺🇸 English**](https://docs.hiddify.com/Hiddify-Manager.wiki/Quick-installation-on-Vultr-Servers)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/%D9%87%D9%85%D9%87-%D8%A2%D9%85%D9%88%D8%B2%D8%B4%E2%80%8C%D9%87%D8%A7-%D9%88-%D9%88%DB%8C%D8%AF%D8%A6%D9%88%D9%87%D8%A7"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/3704cd84-eee6-4c45-abe7-3c02936bbebb" /></a>

<div dir="rtl" markdown="1">

## ویدئوی آموزش کامل نصب

در ویدئوی زیر تمامی مراحل شامل نصب پروکسی و تنظیم دامنه و زیردامنه با جزییات کامل شرح داده شده است.
حتما با فیلترشکن به سایت ولتر مراجعه کنید در غیر این صورت اکانت شما بسته می‌شود.

[![vultr](https://img.youtube.com/vi/hRRg10BURJI/maxresdefault.jpg)](https://www.youtube.com/watch?v=hRRg10BURJI)

## مراحل نصب پروکسی

۱. در مرحله انتخاب سیستم عامل، حتما گزینه Ubuntu 22.04 را انتخاب کنید.

۲. کد زیر را کپی کنید.

<div dir="ltr" markdown="1">

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
  - bash -c "$(curl -Lfo- https://raw.githubusercontent.com/hiddify/hiddify-config/main/common/download_install.sh)"

final_message: "The system is finally up, after $UPTIME seconds"
output: { all: "| tee -a /root/cloud-init-output.log" }

# you can see the generated link from the website by using http://yourip/ or https://yourip.sslip.io in one hour, after that, it will be disapear.
```

</div>

۳. در قسمت سرور تیک گزینه Enable Cloud-Init User-Data را بزنید و کد کپی شده را در آن قرار دهید. پس از حداکثر ۱۰ تا ۱۵ دقیقه پروکسی شما فعال خواهد بود.

![Group 1](https://user-images.githubusercontent.com/79760104/221190008-239cd200-4184-4c05-82ea-ff00a47e920e.jpg)

۴. حالا باید دامنه را تنظیم کنید. بر روی [این لینک](https://github.com/hiddify/hiddify-config/wiki/%D8%B1%D8%A7%D9%87%D9%86%D9%85%D8%A7%DB%8C-%D8%AA%D9%86%D8%B8%DB%8C%D9%85-%D8%AF%D8%A7%D9%85%D9%86%D9%87-%D9%88-%D9%86%D9%87%D8%A7%DB%8C%DB%8C-%DA%A9%D8%B1%D8%AF%D9%86-%D9%86%D8%B5%D8%A8) کلیک کنید تا نصب را نهایی کنید.

</div>
