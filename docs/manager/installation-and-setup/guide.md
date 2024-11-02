---
title: Main installation guide
weight: -90
---


<div dir="ltr" markdown="1">

# Quick installation on Ubuntu

## Before installation

- If you have important information or an important service, note that installing this configuration may interfere with your other services. Therefore, please do not install any special service on your server.
- It is strongly recommended that **Hiddify only be deployed on a single-use host**. Hiddify's deployment model assumes that the host is dedicated solely to running Hiddify and is not shared with other applications or users. Hiddify is not secure in a multi-user environment and that the server should be treated as a dedicated proxy host. We are working in making it proper for multi-user environment and also provide a docker image.

- This code is only applicable on Ubuntu and has been tested only on version 22.04.


- If not, you need a series of prerequisites which you can read them [here](/manager/installation-and-setup/Installation-prerequisites/). 



## Installation video



<div align=center markdown=1>
<a href="https://www.youtube.com/watch?v=XSwCE35lqmU"><img width="32%" src="https://user-images.githubusercontent.com/125398461/235692699-f6cc0a42-3742-44d5-be20-783ac0e50fdc.png" /></a>

</div>

## Installation steps on Ubuntu
1. Connect to your server through ssh and copy and run the following command in the terminal

```
bash <(curl https://i.hiddify.com/release)
```

Congratulations, the installation is complete. 


2. After installation
At the end, a link will be generated which is the link to setup your proxy. Now we need to set the domain. Click on [this link](/manager/installation-and-setup/Guide-for-setting-up-the-domain-and-finalizing-the-installation/) to complete the installation.


> For making the best use of this panel please view this [article](/manager/configuration-and-advanced-settings/How-to-configure-Hiddify-panel-properly/).
