---
title: Disable SSH Password Authentication
---

<div dir="ltr" markdown="1">

# Disable SSH Password Authentication

This page shows you how to stop your server from accepting SSH logins with a password, so that only your own key can log in. Do this on every server where you run Hiddify Manager.

## Why you need this

- **Symptom:** the Hiddify admin panel shows the warning *"Your server is vulnerable to abuses because Password Authentication is enabled in your SSH"*, or a **WARNING** box appears when you open the `hiddify` menu on the server.
- **Cause:** your server still accepts SSH logins with a password. Bots on the internet try thousands of passwords per day. If one guess works, they can take over your server and use it for attacks, which can get your server suspended by the provider for abuse.
- **Fix:** log in with an **SSH key** instead, then turn password logins off. An **SSH key** is a pair of files made on your own computer: a *private key* that stays with you, and a *public key* that you copy to the server. The server lets in only the computer that holds the matching private key.

## Before you start

- You can already connect to your server over SSH. If not, see [How to connect to the server via SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/).
- You know your server's IP address and SSH username (usually `root`).
- You have a terminal on your computer: **PowerShell** on Windows, **Terminal** on macOS or Linux.

!!! warning "Do not skip Part 1"
    If you turn off passwords before your key works, you will lock yourself out of the server. Some providers have a web console in their dashboard that can still let you in, but not all do.

## Part 1: Set up key login

Run these steps **on your own computer**, not on the server.

1. Create a key pair (skip this step if you already have one):

    ```bash
    ssh-keygen -t ed25519
    ```

    Press **Enter** to accept the default file location. You can type a passphrase to protect the key, or press **Enter** twice to leave it empty.

2. Copy the public key to the server. Replace `root` with your username and `your_server_ip` with your server's IP address. Type your server password once when asked.

    === "Windows (PowerShell)"

        ```powershell
        type $env:USERPROFILE\.ssh\id_ed25519.pub | ssh root@your_server_ip "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
        ```

    === "macOS and Linux"

        ```bash
        ssh-copy-id root@your_server_ip
        ```

3. Test the key. Open a **new** terminal window and run:

    ```bash
    ssh root@your_server_ip
    ```

    **It worked if** you are logged in without being asked for the server password (you may be asked for the key's passphrase if you set one).

    **If you are still asked for the server password**, the key was not copied correctly. Repeat step 2 and do not continue to Part 2.

## Part 2: Turn off password login

Run these steps **on your server, over SSH**. Keep your current SSH window open until the end, so you still have a way in if something goes wrong.

1. Create a small settings file that turns off password login:

    ```bash
    echo "PasswordAuthentication no" | sudo tee /etc/ssh/sshd_config.d/00-disable-password.conf
    ```

    Ubuntu reads files in `/etc/ssh/sshd_config.d/` before the main `sshd_config` file, and the first value it finds wins. Some providers add a file there (for example `50-cloud-init.conf`) that turns password login back on. The `00-` at the start of the name makes your file win.

2. Check the SSH settings for mistakes:

    ```bash
    sudo sshd -t
    ```

    **It worked if** the command prints nothing. If it prints an error, fix the file it names before you continue.

3. Restart the SSH service so the change takes effect:

    ```bash
    sudo systemctl restart ssh
    ```

4. Confirm that the setting is active:

    ```bash
    sudo sshd -T | grep -i passwordauthentication
    ```

    **It worked if** you see `passwordauthentication no`.

## Part 3: Test it

1. Open a **new** terminal window on your computer and connect again with `ssh root@your_server_ip`. You should get in with your key, without the server password.
2. Optional: try to connect from another computer that does not have your key. The server should refuse with `Permission denied (publickey)`.
3. Refresh the Hiddify admin panel. The password warning should be gone.

**If you can no longer log in:** go back to the SSH window you kept open and delete the file you created, then restart SSH:

```bash
sudo rm /etc/ssh/sshd_config.d/00-disable-password.conf
sudo systemctl restart ssh
```

If you closed every window, use your provider's web console to run the same commands.

## More ways to protect your server

- [Change the SSH port](/manager/basic-concepts-and-troubleshooting/How-to-change-SSH-port-on-your-server/) from the default 22 to reduce automated login attempts.
- [Turn on the Hiddify firewall](/manager/basic-concepts-and-troubleshooting/How-to-setup-Firewall-on-Hiddify-panel/) so only the ports you use are open.
- Keep your server updated.

</div>
