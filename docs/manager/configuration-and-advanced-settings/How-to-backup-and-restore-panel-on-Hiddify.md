---
title: How to backup and restore HiddifyManager
weight: -100
---

<div dir="ltr" markdown="1">

# How to backup and restore panel on Hiddify

Many times you need to backup the panel and restore it on another server. For example, your server is filtered or there is a problem that you cannot continue on that server. In this case, continue the following steps until the end to learn how to do this.
Backup current panel via web

In the admin panel, enter settings and then backup and click on receive backup file.

![backup](https://github.com/hiddify/hiddify-config/assets/125398461/5547180d-e2e6-44b5-a3ec-a651a58a02d3)


Here you can specify the storage location of your backup file so that the json file related to the settings is saved.


## Sending the backup file to Telegram

Every 6 hours, the panel automatically backs up for you, and if you have activated the [Telegram bot](/manager/configuration-and-advanced-settings/How-to-set-up-and-use-Telegram-bot-on-Hiddify-panel), it will be sent to the bot.

## Backup during important operations

When updating or reinstalling the panel, it is backed up and you can access and use it.

> Note: If for any reason the Telegram bot was not available to you and you were not able to backup via the web, you can access the previous backups of the system from the following path.

`/opt/hiddify-config/hiddify-panel/backup`

and then transfer the file to your PC. [More info here](/manager/basic-concepts-and-troubleshooting/How-to-transfer-files-between-a-server-and-a-computer)

## Restoring backup file
Now install the panel on the new server and do nothing on the `Quick-setup` page.

![Screenshot_20230528_084919](https://github.com/hiddify/hiddify-config/assets/125398461/c419c97a-7dad-4f90-9b07-c33453887050)


Enter the Backup menu in Settings.

![restore](https://github.com/hiddify/hiddify-config/assets/125398461/bb83fc32-bbae-4b89-9bbe-b6498488125c)

Here, select the backup file that you saved in the previous step. Enable recovery options as per your need. For example, if you want to restore the entire panel, select all 3 options and wait for the operation to finish.


## Changing subdomain settings
Change your subdomain settings to the new server's IP. That is, go wherever you have defined your domains and enter the new IPs. For example, enter the DNS settings in Cloudflare and go to the previously registered records and just change the IP.

<div align=center markdown=1>
<img src="https://github.com/hiddify/hiddify-config/assets/125398461/c572da3a-aafb-4457-b06e-c8870a20e171" />
</div>



The work is done. The panel with the admin link will come up on the new server.
