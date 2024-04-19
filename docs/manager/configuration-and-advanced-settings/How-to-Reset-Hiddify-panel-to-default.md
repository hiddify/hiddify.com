---
title: How to Reset HiddifyManager to default
weight: -80
---

<div dir="ltr" markdown="1">

# How to Reset HiddifyManager to default
In this article, we are going to teach how to raw the HiddifyManager (complete reset of the panel and database) similar to the initial installation. If you intend to return the Hiddify panel to its initial settings, this tutorial is prepared for you. Follow these steps to the end.

* To begin, first [SSH into your server](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/).
* Then, by using the combination keys `Ctrl+c` or selecting the `Cancel` button, close the Hidیify menu to access the terminal (command line environment) of your server.

* If after performing these steps, the Hiddify menu is still displayed to you, type the word `clear` and press enter.

> It should be mentioned here that if you need to backup your panel, make a backup of the settings-backup before proceeding.
* Then enter this command in the terminal of your server to completely delete the current database:

```
rm -rf /opt/hiddify-config/hiddifypanel/hiddifypanel.db
```
* Then open the menu again using the following command:

```
bash /opt/hiddify-config/menu.sh
```

* And select `Reinstall` option from the Hiddify menu and wait for the panel to be reinstalled.
* After finishing, you can access the new panel and configure it using the displayed admin links.

In this method, after the re-installation is finished, the panel will be completely retested and similar to the initial installation.



