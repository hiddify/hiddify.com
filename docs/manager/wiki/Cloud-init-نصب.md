[**🇺🇸 English**](https://github.com/hiddify/hiddify-config/wiki/Cloud-init-installation)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/%D9%87%D9%85%D9%87-%D8%A2%D9%85%D9%88%D8%B2%D8%B4%E2%80%8C%D9%87%D8%A7-%D9%88-%D9%88%DB%8C%D8%AF%D8%A6%D9%88%D9%87%D8%A7"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/3704cd84-eee6-4c45-abe7-3c02936bbebb" /></a>

<div dir="rtl" markdown=1>

این بخش مناسب برای هاستینگ‌هایی هست که کلود کانفیگ را ساپورت می‌کنه
این کد را کپی کنید و در قسمت مربوطه قرار دهید

</div>

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
  - bash -c "export CREATE_EASYSETUP_LINK='true';curl i.hiddify.com/release|bash"

final_message: "The system is finally up, after $UPTIME seconds"
output: { all: "| tee -a /root/cloud-init-output.log" }

# you can see the generated link from the website by using https://yourip.sslip.io/hiddify in one hour, after that, it will be disappear.  
```

<div dir="rtl" markdown=1>
بعد از نصب این اسکریپت، از [اینجا](https://github.com/hiddify/hiddify-config/wiki/%D8%B1%D8%A7%D9%87%D9%86%D9%85%D8%A7%DB%8C-%D8%AA%D9%86%D8%B8%DB%8C%D9%85-%D8%AF%D8%A7%D9%85%D9%86%D9%87-%D9%88-%D9%86%D9%87%D8%A7%DB%8C%DB%8C-%DA%A9%D8%B1%D8%AF%D9%86-%D9%86%D8%B5%D8%A8) ادامه نصب را دنبال کنید تا نصب نهایی شود.

<div markdown=1>