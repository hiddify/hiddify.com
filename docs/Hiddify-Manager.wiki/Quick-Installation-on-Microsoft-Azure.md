<div dir="rtl">

[**![flag_of_Iran](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://github.com/hiddify/hiddify-config/wiki/Azure-%D9%86%D8%B5%D8%A8-%D8%AE%DB%8C%D9%84%DB%8C-%D8%AE%DB%8C%D9%84%DB%8C-%D8%B3%D8%B1%DB%8C%D8%B9-%D8%AF%D8%B1-%D9%85%D8%A7%DB%8C%DA%A9%D8%B1%D9%88%D8%B3%D8%A7%D9%81%D8%AA-%D8%A2%DA%98%D9%88%D8%B1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>
</div>

# Quick Installation on Microsoft Azure
 In this article, we will teach you how to create a dedicated VPN server on Azure via Hiddify panel.


## General idea
Companies such as Microsoft and Digital Ocean offer free one-year credit (renewable) of about $100 for students. We use this free credit to create a VPN server for our family and friends.
- A Telegram proxy
- A VPN server

## Installation Steps

### Step 1: Create a student account on Microsoft Azure
First, log in to the [Microsoft Azure](https://azure.microsoft.com/en-us/free/students/) website and follow the steps according to the gif below:

![](http://hiddify.github.io/assets/create_student_account.gif)

To view the amount of credit remaining in your user account, use [this link](https://www.microsoftazuresponsorships.com/Balance).

### Step 2: Creating a virtual machine in Azure for Telegram
Click on this icon <a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fhiddify%2Fconfig%2Fmain%2Ftelegram%2Ftelegram-vm-azure-template.json" target="_blank"><img src="https://aka.ms/deploytoazurebutton"/></a> and continue the steps according to the gif below.

![](https://github.com/hiddify/hiddify.github.io/raw/main/assets/azure-auto-deploy.gif)
<div class="alert alert-success">

And copy the link for Telegram proxy from the `output` section. Don't forget that this link will be deleted, so save it in a safe place.

### Step 3: Create a virtual machine in Azure to proxy sites and applications
Click on this icon <a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fhiddify%2Fconfig%2Fmain%2Fshadowsocks%2Fss-azure-template.json" target="_blank"><img src="https://aka.ms/deploytoazurebutton"/></a> and continue the steps according to the previous gif.
 And copy the proxy link from `output` section. Don't forget that this link will be deleted, so save it in a safe place
Then open the link to display the tutorial on how to use the proxy.

You can finalize the installation using [this link](https://github.com/hiddify/hiddify-config/wiki/Guide-for-setting-up-the-domain-and-finalizing-the-installation)

For making the best use of this panel please view this [article](https://github.com/hiddify/hiddify-config/wiki/How-to-configure-Hiddify-Panel-properly).