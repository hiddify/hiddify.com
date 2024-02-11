<div dir="rtl" markdown="1">

[**![flag_of_Iran](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://docs.hiddify.com/fa/Hiddify-Manager.wiki/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D9%BE%D8%B4%D8%AA%DB%8C%D8%A8%D8%A7%D9%86%E2%80%8C%DA%AF%DB%8C%D8%B1%DB%8C-%D9%88-%D8%A8%D8%A7%D8%B2%DB%8C%D8%A7%D8%A8%DB%8C-%D9%BE%D9%86%D9%84-%D8%AF%D8%B1-%D9%87%DB%8C%D8%AF%DB%8C%D9%81%D8%A7%DB%8C)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>

</div>

# How to backup and restore panel on Hiddify

Many times you need to backup the panel and restore it on another server. For example, your server is filtered or there is a problem that you cannot continue on that server. In this case, continue the following steps until the end to learn how to do this.
Backup current panel via web

In the admin panel, enter settings and then backup and click on receive backup file.

![backup](https://github.com/hiddify/hiddify-config/assets/125398461/5547180d-e2e6-44b5-a3ec-a651a58a02d3)

Here you can specify the storage location of your backup file so that the json file related to the settings is saved.

## Sending the backup file to Telegram

Every 6 hours, the panel automatically backs up for you, and if you have activated the [Telegram bot](https://github.com/hiddify/hiddify-config/wiki/How-to-set-up-and-use-Telegram-bot-on-Hddify-panel), it will be sent to the bot.

## Backup during important operations

When updating or reinstalling the panel, it is backed up and you can access and use it.

> Note: If for any reason the Telegram bot was not available to you and you were not able to backup via the web, you can access the previous backups of the system from the following path.

`/opt/hiddify-config/hiddify-panel/backup`

and then transfer the file to your PC. [More info here](https://github.com/hiddify/hiddify-config/wiki/How-to-transfer-files-between-a-server-and-a-computer)

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
