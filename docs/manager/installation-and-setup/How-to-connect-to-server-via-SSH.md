---
title: How to connect to server via SSH
weight: -80
---

<div dir="ltr" markdown="1">

# How to connect to your server via SSH

**SSH** is a secure way to open a command line on a remote server from your own computer. You need it to install Hiddify Manager, and to fix the panel when you cannot reach it from the web (for example, if you lost your admin link).

## What you need

- Your server's **IP address** (four numbers separated by dots, for example `1.1.1.1`).
- The **username** and **password** (or SSH key) from your server provider. The username is usually `root`.
- An SSH program on your computer. Windows 10 and 11, macOS and Linux already include one.

<details markdown="1"><summary>Windows only: install SSH if it is missing</summary>

Windows 10 and 11 usually include SSH already. If the `ssh` command is not found:

1. Right-click **PowerShell** and choose **Run as Administrator**.

    ![Opening PowerShell as administrator](https://user-images.githubusercontent.com/114227601/222904592-cd26b3bf-a014-4253-9488-ee9717f006fe.png)

2. Run this command:

    ```powershell
    Add-WindowsCapability -Online -Name OpenSSH.Client
    ```

3. You should see a result like this:

    ![Result of installing OpenSSH](https://user-images.githubusercontent.com/114227601/222904870-e709f69e-1a8d-4a6d-ad6a-3d7bdcd917c3.png)

SSH is now installed.

</details>

## Connect to the server

1. Open a terminal on your computer:
    - Windows: **PowerShell**
    - macOS: **Terminal**
    - Linux: **Terminal**
2. Type this command, replacing `<IP_Address>` with your server's IP address, and press Enter:

    ```bash
    ssh root@<IP_Address>
    ```

    For example, if your server's IP is `1.1.1.1`:

    ```bash
    ssh root@1.1.1.1
    ```

3. The first time you connect, SSH asks if you trust the server (`Are you sure you want to continue connecting`). Type `yes` and press Enter.
4. Enter your password and press Enter. The password does not appear on the screen while you type; this is normal.

When you are connected, the prompt changes to something like `root@your-server:~#`. You can now run commands on the server.

If you see `Connection timed out` or `Connection refused`, check the IP address and port, and make sure the server is running.

## If you changed the SSH port

SSH uses port 22 by default. If you changed it, add `-p` and your port number:

```bash
ssh root@<IP_Address> -p <port_number>
```

For example, if your IP is `1.1.1.1` and your port is `2222`:

```bash
ssh root@1.1.1.1 -p 2222
```

## Useful commands after you connect

If Hiddify Manager is already installed, these commands help you manage it:

- `hiddify`: opens the management menu.
- `hiddify admin`: shows the admin panel links.
- `hiddify status`: shows the status of the services.
- `hiddify restart`: restarts the services.

For example, to see the admin links:

```bash
hiddify admin
```

To install Hiddify Manager, follow the [main installation guide](/manager/installation-and-setup/guide/).

</div>
