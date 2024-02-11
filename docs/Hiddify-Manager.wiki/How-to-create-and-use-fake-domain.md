<div dir="rtl" markdown="1">

[**![Lang_farsi](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://github.com/hiddify/Hiddify-Manager/wiki/%D9%86%D8%AD%D9%88%D9%87-%D8%A7%DB%8C%D8%AC%D8%A7%D8%AF-%D9%88-%D8%A7%D8%B3%D8%AA%D9%81%D8%A7%D8%AF%D9%87-%D8%A7%D8%B2-%D8%AF%D8%A7%D9%85%D9%86%D9%87-%D9%81%DB%8C%DA%A9)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>
</div>


# How to create and use fake domain

## Creating fake domain
As the name suggests, we want to use a fake domain that is not related to us, so we don't need to register it in advance. But we can only use it in the panel.

* To create a misleading or fake domain in the settings section, refer to the domains menu.

<div align=center markdown=1>
![fake-domain1-en](https://github.com/hiddify/Hiddify-Manager/assets/125398461/3f8ee165-5ea9-41d5-b64d-60cefb95828d)

</div>

* Click `Create`.

* Select `Fake Site` from the `Mode` field.

<div align=center markdown=1>
![fake-domain2-en](https://github.com/hiddify/Hiddify-Manager/assets/125398461/147cb16c-29ca-40ba-bfdb-1ac6243a34a2)
</div>

* Put the fake domain you want in the `Domain` field. If you need to use the server domain instead of the IP, complete the `Force Config to Use Following IPs` field to the domain of your direct server.

<div align=center markdown=1>
![fake-domain3-en](https://github.com/hiddify/Hiddify-Manager/assets/125398461/db2b1523-c954-4203-aebe-76a895c370f2)
</div>

[here](https://gist.github.com/ofou/654efe67e173a6bff5c64ba26c09d058) you can see a list of sites and ports to use as fake domains.

* Finally, click on `Save` to register your fake domain.

## Connecting the fake domain to the subscription domain
* To use the registered fake domain configurations, you need to edit your subscription domain and add the fake domain from `Show Configs of Domains`.

<div align=center markdown=1>
![](https://user-images.githubusercontent.com/125398461/247821040-b0749490-6e4e-43aa-b9b4-ab721cceb6b8.png)

</div>

* The work is done, the fake configs have been added to the subscription link. Just update the subscription link on your client application.


## Proxy section settings
* To make sure that the created fake proxies are active, enter the proxies menu in the settings section.
* Check that `http` is enabled from the `Global Configs` section.
*  If you want to use VMess, check that `VMess` is active in the `Global Configs` section.

<div align=center markdown=1>
![Global settings of Proxies](https://github.com/hiddify/Hiddify-Manager/assets/125398461/357a290d-799d-4f71-b956-b734915d137b)

</div>

* In `Direct` section, check that the following proxies are enabled.

<div align=center markdown=1>
![](https://user-images.githubusercontent.com/125398461/282223262-7707d08d-f4ba-4875-b06a-32302817d31f.png)

</div>