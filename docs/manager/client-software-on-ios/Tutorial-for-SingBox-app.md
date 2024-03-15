---
title: Tutorial for SingBox app
---

<div dir="ltr" markdown="1">


# Tutorial for SingBox app
In this tutorial, we are going to teach how to add Hiddify panel SSH configuration to SingBox app. To do this, follow this tutorial to the end.

## Download the app
Follow the links below to download the program.

- [Android](https://install.appcenter.ms/users/nekohasekai/apps/sfa/distribution_groups/publictest)
- [iOS](https://apps.apple.com/us/app/sing-box/id6451272673)
- [Windows](https://github.com/yebekhe/SingBox-UI)

## Add SSH proxy to the app

- First, read [this article](/manager/wiki/SSH-proxy-setting-on-Hiddify-panel) to learn how to activate this proxy.
- Then go to the Profiles menu in the app.
<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/816fbc46-21c2-4109-b2c9-3d9529a5a0ce" />

</div>

- Select the `New Profile` option.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/b9651f36-24db-437e-9a7d-80c2d4a7622a" />

</div>


- Set `Type` to `Remote`.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/e68609dd-d294-44cf-8404-7f6e7091d61e" />


</div>

- Now put a desired name in the `Name` field and put the config link you copied from your panel in the `URL` field and click `Create`.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/603f8676-b0cf-4e0d-b31a-b272bd6adc03" />

</div>



- Then the profile will be added to the list of program profiles.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/8a27f295-0f46-4655-9c28-bd6acd82c6e0" />

</div>


## Connect to SSH proxy

To connect, go to the `Dashboard` menu and select the desired profile and activate it using the `Enabled` button.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/8d911472-b2b4-4fb9-a36b-5e22cca273db" />

</div>

The work is done.