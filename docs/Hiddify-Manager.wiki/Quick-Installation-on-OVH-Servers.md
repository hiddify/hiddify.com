<div dir="rtl">

[**![flag_of_Iran](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://github.com/hiddify/hiddify-config/wiki/OVH-%D9%86%D8%B5%D8%A8-%D8%AE%DB%8C%D9%84%DB%8C-%D8%B3%D8%B1%DB%8C%D8%B9-%D8%AF%D8%B1-%D8%A7%D9%88-%D9%88%DB%8C-%D8%A7%DA%86)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>
</div>


# Quick Installation on OVH Servers

In the video below, all the steps are described. This video is in Farsi and if you watch the steps you can handle it. We are considering making some English videos for non-Persian people. Till then you can visit this video or follow the instructions in this article.

[![OVH](https://img.youtube.com/vi/06fMizOb-DE/maxresdefault.jpg)](https://www.youtube.com/watch?v=06fMizOb-DE)

# Installation steps
1. copy the following code:
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

Do not forget to wait at least 10 minutes.

2. Now we need to setup the domain and finalize the installation. [(visit this article)](https://github.com/hiddify/hiddify-config/wiki/Guide-for-setting-up-the-domain-and-finalizing-the-installation)

For making the best use of this panel please view this [article](https://github.com/hiddify/hiddify-config/wiki/How-to-configure-Hiddify-Panel-properly).