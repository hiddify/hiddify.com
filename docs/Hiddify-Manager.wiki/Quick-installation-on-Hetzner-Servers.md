<div dir="rtl">

[**![flag_of_Iran](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://github.com/hiddify/hiddify-config/wiki/Hetzner-%D9%86%D8%B5%D8%A8-%D8%AE%DB%8C%D9%84%DB%8C-%D8%B3%D8%B1%DB%8C%D8%B9-%D8%AF%D8%B1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>
</div>

# Quick installation on Hetzner Servers

<!--
In the video below, all the steps are described in full detail. This video is in Farsi and if you watch the steps you can handle that. Although We are considering making some English videos for non-Persian people, till then you can visit this or follow the instructions in this article.

[![Hetzner](https://img.youtube.com/vi/vQ-NAfRXTZo/maxresdefault.jpg)](https://www.youtube.com/watch?v=vQ-NAfRXTZo)
-->

## Installation Steps
- First of all, login to your Hetzner account and click on `ADD SERVER` button.

<div align=center>

![206861285-58832cec-a2a3-441e-91d4-8300d16584d6](https://user-images.githubusercontent.com/125398461/228821324-f873517a-a977-4370-8d35-fb56116f579f.png)
</div>

- Now copy the following code

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

- Put the above code in the place shown in the picture and click on `CREATE & BUY NOW` button. 
<div align=center>

![206861304-656682b4-17a3-44c1-89f9-7b0d89566728](https://user-images.githubusercontent.com/125398461/228821370-f99f7091-e65c-45b5-a2da-df33c9103d06.png)
</div>
- After a maximum of 10 to 15 minutes, your server will be ready and the proxy will be active. Copy your IP according to the picture and open it in the browser.

<div align=center>

![206861323-1de41700-6ce4-403a-a644-0836e2a22876](https://user-images.githubusercontent.com/125398461/228821397-4c762ea9-9215-4f6b-960f-b14d862c1e0c.png)
</div>

Do not forget to wait at least 10 minutes

- Now we need to set the domain. Click on [this link](https://github.com/hiddify/hiddify-config/wiki/Guide-for-setting-up-the-domain-and-finalizing-the-installation) to complete the installation.

For making the best use of this panel please view this [article](https://github.com/hiddify/hiddify-config/wiki/How-to-configure-Hiddify-Panel-properly).