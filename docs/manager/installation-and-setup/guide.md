---
title: Main installation guide
weight: -90
---


<div dir="ltr" markdown="1">

# Quick installation on Ubuntu

This page shows you how to install Hiddify Manager on your own server with one command. Hiddify Manager is the server-side panel: you install it once on a server, and then you create users and share their connection links from the panel.

## Before you start

You need:

- A server (VPS) with a fresh install of **Ubuntu 22.04, 24.04 or 26.04**, on an **amd64 (x86_64)** or **arm64** processor. Older versions such as Ubuntu 20.04 are not supported: the installer stops with the message `This script only works on Ubuntu 22 and above`. Other Linux distributions (Debian, CentOS, ...) are not supported either. See [Installation prerequisites](/manager/installation-and-setup/Installation-prerequisites/) for how to get a server.
- A way to connect to the server over **SSH** (a secure way to type commands on a remote server). See [How to connect to the server via SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/).

!!! warning "Use a dedicated server"
    Install Hiddify only on a server that does nothing else. Hiddify changes the server's settings and uses ports 80 and 443, so it can break other services (websites, other panels, other VPNs) on the same server. Hiddify is also not designed for servers shared with other users or applications.

## Installation video

<div align=center markdown=1>
<a href="https://www.youtube.com/watch?v=XSwCE35lqmU"><img width="32%" src="https://user-images.githubusercontent.com/125398461/235692699-f6cc0a42-3742-44d5-be20-783ac0e50fdc.png" alt="Video: How to install Hiddify panel on Ubuntu using SSH" /></a>

</div>

The video shows an older version, so some screens look different now. The command is the same.

## Installation steps

1. Connect to your server over SSH as the `root` user. If you logged in as another user, first run this command to become root:

    ```bash
    sudo -i
    ```

2. On your server, copy and run this command:

    ```bash
    bash <(curl https://i.hiddify.com/release)
    ```

3. Wait until the installation finishes. It can take several minutes. The installer shows its progress on the screen.
4. When it is done, the installer shows your **admin links**. Copy them and keep them in a safe place. Anyone with an admin link can manage your panel.

If the installation fails, the installer shows `Installation Failed!` with an error code. Run the command again; if it fails again, ask for help in the [Hiddify Telegram group](https://t.me/hiddify_board) or on [GitHub](https://github.com/hiddify/Hiddify-Manager/issues), and attach the log files from the `/opt/hiddify-manager/data/log/` folder on your server.

!!! tip "Show the admin links again later"
    If you lose your admin links, connect to your server over SSH and run:

    ```bash
    hiddify admin
    ```

    Running `hiddify` with no extra word opens the management menu (update, restart, status, uninstall and more).

!!! note "Other ways to install"
    - Install on a cloud provider without SSH: [Cloud-init installation](/manager/installation-and-setup/Cloud-init-installation/).
    - Install a beta, development or specific version: [Installing different versions](/manager/installation-and-setup/How-to-install-different-versions-of-Hiddify-Manager/).
    - Install with Docker (experimental): [Install Hiddify using Docker](/manager/installation-and-setup/Install-Hiddify-using-Docker/).

## After installation

Next, you open the panel and set your domain. Follow [Setting up the domain and finalizing the installation](/manager/installation-and-setup/Guide-for-setting-up-the-domain-and-finalizing-the-installation/).

To get the most out of the panel, read [How to configure the Hiddify panel properly](/manager/configuration-and-advanced-settings/How-to-configure-Hiddify-panel-properly/).

</div>
