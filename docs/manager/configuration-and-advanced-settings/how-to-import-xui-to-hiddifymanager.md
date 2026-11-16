---
title: How to import X-UI to HiddifyManager
---

<div dir="ltr" markdown="1">

# How to import X-UI to HiddifyManager

!!! info "Written for Hiddify Manager v14.5"
    The importer has no page in the admin panel: you run it with one command on the server, over SSH.

If you are moving from an X-UI panel (or a panel based on it, such as 3X-UI), Hiddify Manager can import its users, so they keep their accounts and their usage.

## What is imported

- **Users:** every client of the X-UI inbounds becomes a Hiddify Manager user with the same name, the same UUID (when it is a valid UUID, so the users' existing links keep their ID), the traffic limit, the traffic already used, the days left (no expiry in X-UI becomes 10 years), the Telegram ID and whether the user is enabled. The note "Imported from X-UI" is added to each one, and they belong to the admin who runs the import (the owner).
- **Reality domains:** the destination site of every X-UI Reality inbound is added as a **Direct** domain with **Reality** TLS.

Inbounds, ports and other settings are not imported, because the two panels work differently. After the import, your users need their **new** Hiddify Manager links (their user page or subscription link).

## Steps

1. **Get the X-UI database.** On the X-UI server it is usually `/etc/x-ui/x-ui.db`. Copy it to your Hiddify Manager server, for example into `/tmp/`. See [How to transfer files between a server and a computer](/manager/basic-concepts-and-troubleshooting/How-to-transfer-files-between-a-server-and-a-computer/).
2. **Back up your panel first:** **Backup** › **Download Backup**. See [How to back up and restore](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/).
3. **Connect to the Hiddify Manager server over SSH** as `root` and run (change the path to your file):

    ```bash
    chmod 644 /tmp/x-ui.db
    cd /opt/hiddify-manager && source scripts/common/utils.sh && hiddify-panel-cli xui-importer -x /tmp/x-ui.db
    ```

    The panel runs the command as its own user (`hiddify-panel`), so the file must be readable by it; that is why the file is in `/tmp/` with `chmod 644`. The command prints `success`, or `failed to import xui data` with the reason.

4. Open **Users** in the panel: the imported users are there. If Reality domains were added, open **Actions** and click **Apply now** (or **Reinstall** if the panel asks for it).
5. Send each user their new link.

!!! note
    If you run the import twice, users whose X-UI ID is a valid UUID are updated, not added again. Users with any other ID get a new random UUID each time, so they would be added twice: run the import once.

## Related articles

- [Every part and setting of the panel](/manager/configuration-and-advanced-settings/How-to-configure-Hiddify-panel-properly/)
- [All panel settings, one by one](/manager/configuration-and-advanced-settings/Settings-reference/)
- [The Hiddify Manager menu over SSH](/manager/configuration-and-advanced-settings/How-to-connect-and-troubleshoot-via-SSH/)
- [The admin link and its format](/manager/domain-worker-cdn-and-tunneling/The-correct-format-of-admin-link/)

</div>
