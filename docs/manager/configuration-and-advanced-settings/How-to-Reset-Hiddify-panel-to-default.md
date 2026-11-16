---
title: How to Reset HiddifyManager to default
weight: -80
---

<div dir="ltr" markdown="1">

# How to Reset HiddifyManager to default

This guide brings HiddifyManager back to the state of a fresh install: the panel, its database, users, domains and settings are all removed, and you start again from the quick setup. It is written for Hiddify Manager v14.5.

!!! tip "Do you really need a full reset?"
    - **You forgot the admin password:** no reset needed. Run `hiddify reset-password` on the server (see [below](#reset-only-the-admin-password)).
    - **Something misbehaves:** first try **Actions** › **Restart** or **Reinstall** in the panel. Neither of them deletes your users or settings.
    - **You want to move to a new server:** make a backup on the old one and restore it on the new one ([Backup and restore](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/)).

## Before you start: make a backup

A full reset cannot be undone. In the panel, open **Backup** and click **Download Backup**, then keep the file somewhere safe. With it you can bring everything back later. More: [How to backup and restore HiddifyManager](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/).

## Full reset

1. [Connect to your server with SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/).
2. Open the HiddifyManager menu with this command (it may already be open when you log in):

    ```
    hiddify
    ```

3. Choose **advanced** (*Uninstall, Remote Assistant, Downgrade,...*), then **purge** (*Uninstall completely and remove database*). It stops and removes every Hiddify service, the panel and its database.

    !!! warning
        **purge** also removes the MariaDB database server and everything in `/opt/hiddify-manager`. Do not use it on a server where other programs keep their data in MariaDB.

4. Install HiddifyManager again with the install command:

    ```
    bash <(curl https://i.hiddify.com/release)
    ```

5. When the install finishes, open one of the new admin links it shows. The panel starts with the **Quick setup** wizard, exactly like after the first install. See [Main installation guide](/manager/installation-and-setup/guide/).

To restore your old data instead of starting empty, open **Backup** in the new panel and drop your backup file on **Restore**.

## Reset only the admin password { #reset-only-the-admin-password }

If you only lost the admin password, run this on the server:

```
hiddify reset-password
```

The owner's password is cleared. Sign in on one of the admin links with an **empty** password (the command `hiddify admin` shows the links), then set a new password on the **Admins** page or in **My account**.

## Related articles

- [Update](/manager/configuration-and-advanced-settings/How-to-update-Hiddify-panel/)
- [Backup and restore](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/)
- [SSH proxy](/manager/configuration-and-advanced-settings/SSH-proxy-setting-on-Hiddify-panel/)
- [Every part and setting of the panel](/manager/configuration-and-advanced-settings/How-to-configure-Hiddify-panel-properly/)

</div>
