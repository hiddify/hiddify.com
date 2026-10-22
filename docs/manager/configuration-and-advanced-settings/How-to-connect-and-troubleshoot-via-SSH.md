---
title: How to connect and troubleshoot via SSH (Working with Hiddify Menu)
weight: -145
---

<div dir="ltr" markdown="1">


<details markdown="1"><summary><h1>Prerequisite: Installing SSH on Windows</h1></summary>

Windows 10 and 11 usually already include the SSH client. If the `ssh` command does not work in PowerShell, install it like this:

1. Open the Start menu and search for **PowerShell**.
2. Right-click **PowerShell** and choose **Run as Administrator**.

    ![PowerShell, Run as Administrator](https://user-images.githubusercontent.com/114227601/222904592-cd26b3bf-a014-4253-9488-ee9717f006fe.png)

3. Run this command in PowerShell:

    ```powershell
    Add-WindowsCapability -Online -Name OpenSSH.Client
    ```

4. When it finishes, you should see something like this:

    ![OpenSSH client installed](https://user-images.githubusercontent.com/114227601/222904870-e709f69e-1a8d-4a6d-ad6a-3d7bdcd917c3.png)

The SSH client is now installed.

</details>

# How to connect and troubleshoot via SSH

This page shows you how to manage Hiddify Manager from your server's command line when the web panel does not open, or when you have lost your admin link. It also explains each option of the Hiddify menu.

**SSH** is a secure way to open a text terminal on your server from your own computer or phone. Everything you type runs on the server.

## Prerequisites

- Your server's IP address.
- The server's username (usually `root`) and password or SSH key. Your server provider gives you these.
- An SSH app on your device:
    - Android: `Termius`
    - Windows: `PowerShell` (or `PuTTY`)
    - macOS: `Terminal`
    - Linux: `Terminal`

For a full guide, see [How to connect to the server via SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/).

## Connect to the server

1. Open your SSH app.
2. Run this command on your device. Replace `user` with your username and `<IP_Address>` with your server's IP:

    ```bash
    ssh user@<IP_Address>
    ```

    For example, if your username is `root` and your server's IP is `1.1.1.1`:

    ```bash
    ssh root@1.1.1.1
    ```

3. Type `yes` if you are asked to trust the server, then enter your password. (The password is not shown while you type. This is normal.)

If the connection works, you see the server's command prompt, and the Hiddify menu may open by itself.

!!! warning "Password login warning"
    If password login is enabled on your server, the menu first shows a **WARNING** that your server is open to abuse. Press Enter to continue. To fix it, follow [Disable SSH password authentication](/manager/basic-concepts-and-troubleshooting/Disable-SSH-Password-Authentication/).

## Open the Hiddify menu

Run this command on your server to open the Hiddify menu:

```bash
hiddify
```

The menu looks like this (the screenshots on this page are from an older version, so some items may look a little different):

![Hiddify Manager menu](https://github.com/hiddify/hiddify.com/assets/125398461/5b3b47fb-4437-4388-b22d-0d2df6359620)

Use the arrow keys to move, and press Enter to choose an item. The sections below explain each item.

!!! tip "Commands instead of the menu"
    Most menu items are also available as direct commands, for example `hiddify status`, `hiddify admin`, `hiddify restart`, `hiddify apply` and `hiddify upgrade release`. Run `hiddify --help` to see them all.

## Cancel or Quit
Choose **Quit** (or press **Cancel** / `Esc`) to leave the menu and go back to the normal server terminal.

To open the menu again, run this command on your server:

```bash
hiddify
```

## Status
Shows whether each Hiddify service is running. If everything is fine, the result looks like this:

![Status](https://github.com/hiddify/hiddify.com/assets/125398461/bb5072e7-635b-486e-9dce-024b8479adb8)

Press `q` to return to the main menu.

**When to use it:** to check quickly whether all services are running.

## Admin
Shows your admin panel links. Open one of the links marked **Secure** (on your domain) in your browser. Use the **Not Secure** IP link only if no domain link works.

![Admin](https://github.com/hiddify/hiddify.com/assets/125398461/d15fb764-45b4-40ec-84f2-7dc0ea134f13)

On this screen you can also press `r` to reset the owner admin password. Press any other key to return to the main menu.

The same links are printed by this command:

```bash
hiddify admin
```

**When to use it:** you installed the panel but forgot to copy the admin link.

## Log
Shows the system logs. After you choose it, pick the log file you want to read.

![Log](https://github.com/hiddify/hiddify.com/assets/125398461/4fa52e34-1f2a-4378-ae1a-881dc81e1269)

For example, choose the install log to see what happened during installation. At its end, it shows the system status and the admin links.

![Install log](https://github.com/hiddify/hiddify.com/assets/125398461/6a980bbf-9d7a-4ef6-aa92-7a4bfeeb34e3)

Press `q` to close the log. The log files are stored on the server in `/opt/hiddify-manager/data/log/`.

**When to use it:** one of the services is not working and you need to see why.

## Restart
Restarts all Hiddify services without changing any settings.

![Restart](https://github.com/hiddify/hiddify.com/assets/125398461/d0caf625-9f09-4543-bc22-ae3843bf289a)

Press any key to return to the main menu.

**When to use it:** a service has stopped and you want to restart all services at once.

## Apply configs
The menu no longer has an "Apply Configs" item. To apply the settings you saved in the panel, run this command on your server:

```bash
hiddify apply
```

![Apply Configs](https://github.com/hiddify/hiddify.com/assets/125398461/76446e31-8efd-4d0e-84b9-a1358887a027)

**When to use it:** you saved changes in the panel but lost web access before you could apply them.

## Install
Reinstalls Hiddify Manager on the server. Your panel data (users, settings, domains) is kept.

**When to use it:** an install step failed and the panel does not open.

## Update
Updates Hiddify Manager to the latest version. It offers these options:

![Update](https://github.com/hiddify/hiddify.com/assets/125398461/9b24004d-cb44-4137-a573-76eb59d8930a)

- **default**: updates to the channel chosen in the panel settings.
- **release**: updates to the latest stable version (recommended).
- **beta**: updates to the latest pre-release version. It may have bugs.

You can also update with a command, for example:

```bash
hiddify upgrade release
```

While it runs, the terminal shows something like this:

![Update running](https://user-images.githubusercontent.com/125398461/222898474-0d72f442-f19a-40a9-9f35-fcad96807fc4.png)

**When to use it:** an update from the web panel failed and you lost access.

## Advanced
This submenu has several options.

![Advanced](https://github.com/hiddify/hiddify.com/assets/125398461/61336508-2dbf-43d8-893c-8d9adbdf3a51)

### warp
Shows the status of the WARP service.

### add_remote
Gives the Hiddify support team SSH access to your server, through the [Hiddify bot](https://t.me/hiddifybot). Use it only when the support team asks you to.

### remove_remote
Removes the SSH access you gave to the [Hiddify bot](https://t.me/hiddifybot).

### enable
Shows the Hiddify menu automatically every time you log in to the server over SSH. Use it if you turned this off before.

### disable
Stops the Hiddify menu from opening automatically when you log in. You can still open it with `hiddify`.

### uninstall
Removes Hiddify Manager services from the server. It does not remove everything that was installed. If you want the server exactly as it was before the installation, rebuild it from your provider's control panel.

### purge
Removes Hiddify Manager **and its database** completely. All users and settings are deleted, so [take a backup](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/) first.

> If this does not work for any reason, you can **Rebuild** the server from your provider's control panel. This deletes all data on the server.

</div>
