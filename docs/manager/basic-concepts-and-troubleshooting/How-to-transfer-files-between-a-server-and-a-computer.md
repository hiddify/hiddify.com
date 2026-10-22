---
title: How to transfer files between a server and a computer
---

<div dir="ltr" markdown="1">

# How to transfer files between a server and a computer

This page shows you how to copy files from your server to your computer and back, for example to keep a copy of a Hiddify backup or to upload a file to the server.

!!! tip "Only need a panel backup?"
    You do not need any commands for that. In the Hiddify admin panel, open the **Backup & restore** page and click **Download backup**. See [How to back up and restore the panel](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/).

## Before you start

- You know your server's IP address and SSH username (usually `root`), and you can [connect to it over SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/).
- Open a terminal on your computer:
    - Windows: **PowerShell**
    - macOS: **Terminal**
    - Linux: **Terminal**

This page uses **scp**, a command that copies files over SSH. It is already included in Windows 10 and 11, macOS and Linux.

!!! note "If Windows says `scp` is not recognized"
    Open PowerShell **as administrator** (right-click PowerShell, then **Run as administrator**) and run this command to install the OpenSSH client:

    ```powershell
    Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
    ```

    Then close PowerShell and open it again.

<div align=center markdown=1>

<img src="https://user-images.githubusercontent.com/114227601/222904870-e709f69e-1a8d-4a6d-ad6a-3d7bdcd917c3.png" alt="Opening PowerShell from the Windows Start menu" />
</div>

## Find the file on the server

Hiddify Manager saves an automatic backup of the panel every 6 hours in `/opt/hiddify-manager/data/backup/`. To see the list, connect to the server over SSH and run:

```bash
ls /opt/hiddify-manager/data/backup/
```

You will see files named by date and time, like `2026_10_20__06_00_03.json`:

<div align=center markdown=1>

<img src="https://github.com/hiddify/Hiddify-Manager/assets/125398461/924b149e-6ec8-4b48-8fbb-ad99a234ee5e" alt="Example list of backup files on the server" />
</div>

Pick the file you want to copy and note its name.

## Copy a file from the server to your computer

Run this **on your own computer**, not on the server. The general form is:

```bash
scp <user>@<server-ip>:<path/on/server> "<folder on your computer>"
```

Example: your username is `root`, the server IP is `1.1.1.1`, and you want to copy a backup into the folder `C:\Backup`:

```powershell
scp root@1.1.1.1:/opt/hiddify-manager/data/backup/2026_10_20__06_00_03.json "C:\Backup"
```

Type your server password (or key passphrase) when asked. **It worked if** the file now appears in `C:\Backup`.

## Copy a file from your computer to the server

Run this **on your own computer**. Example: the file `C:\File\text.txt` should go to the `/root/` folder on the server:

```powershell
scp "C:\File\text.txt" root@1.1.1.1:/root/
```

To check, connect to the server over SSH and run:

```bash
ls /root/
```

**It worked if** `text.txt` is in the list.

## If it does not work

- **`No such file or directory`**: the path is wrong. Check it with `ls` on the server, and remember that Linux paths are case-sensitive (`hiddify-manager`, not `Hiddify-Manager`).
- **`Permission denied`**: the username, password or key is wrong, or the user cannot read or write that folder. Use `root` or a folder your user owns.
- **`Connection timed out`**: the server IP or SSH port is wrong. If you changed the SSH port, add `-P` with the port number (capital P for scp), for example `scp -P 2222 ...`.

## Use the web panel instead

In Hiddify Manager v14, the admin panel has an **SSH terminal** page with a built-in file browser. You can upload files to the server and download files from it there, without a separate program. Avoid entering your server password on third-party websites.

</div>
