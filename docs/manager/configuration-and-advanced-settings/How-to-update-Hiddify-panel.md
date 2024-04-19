---
title: How to update HiddifyManager
weight: -90
---

<div dir="ltr" markdown="1">



# How to update HiddifyManager
There are 2 ways to update the panel.

## Update through admin panel
In the panel, go to the Actions menu and click `Update`.

<div align=center markdown=1>
  
![update approach ](https://github.com/hiddify/hiddify-config/assets/125398461/9f482e1c-30ae-4fd3-8d3c-44d72b08155f)

</div>

This may take between 5 and 10 minutes, after which the operation will finish and the panel will be updated with the latest update.



## Change the update mode

If you need to change the update mode, you can choose one of the `Release`, `Beta` and `Develop` versions and then `update`.


<div align=center markdown=1>
  
![Update](https://github.com/hiddify/hiddify.com/assets/125398461/9b24004d-cb44-4137-a573-76eb59d8930a)

</div>

For example, in the above picture, set the update mode to the `Beta` mode and click `Submit`.

Then select the `Update` option from the `Actions` menu. After about 5 minutes, the panel will be updated to the version you want.

## Automatic update settings in the panel

The panel updates itself daily with the latest version of released version on project's GitHub. Its settings are in the general settings section.


<div align=center markdown=1>
  
![auto update](https://github.com/hiddify/hiddify-config/assets/125398461/9ba845b1-2538-44db-90e2-57c7b31e5c8c)

</div>

For this, the automatic update option should be enabled in the general settings, the panel will be updated daily.

## Update via SSH

Connect via [SSH to the server](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/) and select Update in the Hiddify menu. There are 3 modes.

<div align=center markdown=1>

![](https://user-images.githubusercontent.com/125398461/230083991-e90d579a-5301-49f3-ae5c-645ae5cb6d18.png)

</div>

* The `default` option updates the panel based on default.
* The update `release` option is based on the stable version.
* The `develop` option is to update the version under development.
