---
title: Quick and easy installation on Microsoft Azure
weight: -50
---

<div dir="ltr" markdown="1">

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
<div class="alert alert-success" markdown=1>
And copy the link for Telegram proxy from the `output` section. Don't forget that this link will be deleted, so save it in a safe place.

### Step 3: Create a virtual machine in Azure to proxy sites and applications
Click on this icon <a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fhiddify%2Fconfig%2Fmain%2Fshadowsocks%2Fss-azure-template.json" target="_blank"><img src="https://aka.ms/deploytoazurebutton"/></a> and continue the steps according to the previous gif.
 And copy the proxy link from `output` section. Don't forget that this link will be deleted, so save it in a safe place
Then open the link to display the tutorial on how to use the proxy.

You can finalize the installation using [this link](/manager/wiki/Guide-for-setting-up-the-domain-and-finalizing-the-installation)

For making the best use of this panel please view this [article](/manager/wiki/How-to-configure-Hiddify-Panel-properly).