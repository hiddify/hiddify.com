<div dir="rtl" markdown=1>
[**![flag_of_Iran](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://github.com/hiddify/hiddify-config/wiki/%D9%86%D8%B5%D8%A8-%D8%B3%D8%B1%DB%8C%D8%B9-%D8%AF%D8%B1-%D8%A7%D9%88%D8%A8%D9%88%D9%86%D8%AA%D9%88)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div>
<br>

# Quick installation on Ubuntu

## Before installation

- If you have important information or an important service, note that installing this configuration may interfere with your other services. Therefore, please do not install any special service on your server.

- This code is only applicable on Ubuntu and has been tested only on version 22.04.


- If not, you need a series of prerequisites which you can read them [here](https://github.com/hiddify/Hiddify-Server/wiki/Installation-prerequisites). 



## Installation video



<div align=center markdown=1>
<a href="https://www.youtube.com/watch?v=XSwCE35lqmU"><img width="32%" src="https://user-images.githubusercontent.com/125398461/235692699-f6cc0a42-3742-44d5-be20-783ac0e50fdc.png" /></a>

</div>

## Installation steps on Ubuntu
1. Connect to your server through ssh and copy and run the following command in the terminal

```
curl https://install.hiddify.com/release |bash
```
If the previous command won't work, use the following one:
```
sudo apt update&&sudo apt install -y curl&& curl -sSL https://raw.githubusercontent.com/hiddify/hiddify-manager/main/common/download.sh | sudo bash -s release
```

Congratulations, the installation is complete. 


2. After installation
At the end, a link will be generated which is the link to setup your proxy. Now we need to set the domain. Click on [this link](https://github.com/hiddify/hiddify-config/wiki/Guide-for-setting-up-the-domain-and-finalizing-the-installation) to complete the installation.


> For making the best use of this panel please view this [article](https://github.com/hiddify/hiddify-config/wiki/How-to-configure-Hiddify-Panel-properly).
