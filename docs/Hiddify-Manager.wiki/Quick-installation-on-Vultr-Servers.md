<div dir="rtl" markdown=1>
[**![flag_of_Iran](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://docs.hiddify.com/fa/Hiddify-Manager.wiki/Vultr-%D9%86%D8%B5%D8%A8-%D8%B3%D8%B1%DB%8C%D8%B9-%D8%AF%D8%B1-%D9%88%D9%84%D8%AA%D8%B1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>
</div>

# Quick installation on Vultr Servers

Complete installation training video

In the video below, all the steps, including proxy installation and domain and subdomain settings, are described in full detail. This video is in Farsi and if you watch the steps you can get by that. We are considering making some English videos for non-Persian people. Till then you can visit this or follow the instructions in this article.

For using Vultr site and services please use VPN Connection if you live in countries with sanctions enforced, otherwise your account will be closed.

[![vultr](https://img.youtube.com/vi/hRRg10BURJI/maxresdefault.jpg)](https://www.youtube.com/watch?v=hRRg10BURJI)

# Proxy installation steps

1. At the operating system selection stage, be sure to select Ubuntu 22.04.

2. Copy the code below.

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

3. In the server section, check the Enable Cloud-Init User-Data option and put the copied code in it. After a maximum of 10 to 15 minutes, your proxy will be active.

![Group 1](https://user-images.githubusercontent.com/79760104/221190008-239cd200-4184-4c05-82ea-ff00a47e920e.jpg)

4. Now you need to set the domain. Click on [this link](https://github.com/hiddify/hiddify-config/wiki/Guide-for-setting-up-the-domain-and-finalizing-the-installation) to complete the installation.
