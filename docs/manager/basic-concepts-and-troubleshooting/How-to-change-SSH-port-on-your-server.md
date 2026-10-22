---
title: How to change SSH port on your server
---

<div dir="ltr" markdown="1">

# How to change SSH port on your server

This page shows you how to move SSH from the default port 22 to another port on an Ubuntu server. Bots scan port 22 all day, so a different port means far fewer automated login attempts. It does not replace [turning off password login](/manager/basic-concepts-and-troubleshooting/Disable-SSH-Password-Authentication/), which is the more important step.

A **port** is a numbered door on your server. Each service listens on its own port: SSH uses 22 by default, and Hiddify uses 80 and 443.

## Before you start

- You can connect to your server over SSH. See [How to connect to the server via SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/).
- Choose a new port number between 1024 and 65535 that nothing else uses. This page uses `2222` as the example; replace it with your own number everywhere.
- Do not choose 80, 443, 53 or any port that Hiddify uses for proxies.

!!! warning "Keep your current SSH window open"
    Do every step in one SSH window and keep it open until you have logged in on the new port from a second window. If something goes wrong, the open window is your way back in.

## Steps

Run all commands **on your server, over SSH**.

1. Open the new port in the server firewall, so you are not locked out when SSH moves:

    ```bash
    sudo iptables -I INPUT -p tcp --dport 2222 -j ACCEPT
    sudo ip6tables -I INPUT -p tcp --dport 2222 -j ACCEPT
    sudo sh -c 'iptables-save > /etc/iptables/rules.v4'
    sudo sh -c 'ip6tables-save > /etc/iptables/rules.v6'
    ```

    The last two lines save the rules so they survive a reboot. If `ip6tables` prints an error, your server has IPv6 turned off and you can ignore it.

    If your provider also has a firewall in its web dashboard (often called "Security group" or "Firewall"), allow TCP port 2222 there too.

2. Set the new port in a small SSH settings file:

    ```bash
    echo "Port 2222" | sudo tee /etc/ssh/sshd_config.d/01-port.conf
    ```

3. Check the SSH settings for mistakes:

    ```bash
    sudo sshd -t
    ```

    **It worked if** the command prints nothing.

4. Restart SSH. Which command you need depends on your Ubuntu version. First run:

    ```bash
    systemctl is-enabled ssh.socket
    ```

    === "It prints `enabled` (usually Ubuntu 24.04 and newer)"

        ```bash
        sudo systemctl daemon-reload
        sudo systemctl restart ssh.socket
        ```

    === "It prints `disabled` or an error (usually Ubuntu 22.04)"

        ```bash
        sudo systemctl restart ssh
        ```

5. Check that SSH listens on the new port:

    ```bash
    sudo ss -tlnp | grep 2222
    ```

    **It worked if** you see a line with `:2222`.

6. Test the new port. On your **own computer**, open a **new** terminal window and run:

    ```bash
    ssh -p 2222 root@your_server_ip
    ```

    **It worked if** you can log in. From now on, always add `-p 2222` when you connect, and change the port in any SSH app you use.

## If you cannot connect on the new port

- **"Connection timed out"**: a firewall blocks the port. Check that you did step 1, including your provider's dashboard firewall.
- **"Connection refused"**: SSH is not listening on the new port. Go back to the SSH window you kept open and repeat steps 3 to 5.
- **To undo the change**, delete the file in the open window, run the same restart command you used in step 4, and connect on port 22 again:

    ```bash
    sudo rm /etc/ssh/sshd_config.d/01-port.conf
    ```

!!! note "Hiddify firewall"
    When the **Firewall** setting is on in the Hiddify panel, Hiddify keeps port 22 open and opens the ports Hiddify needs. The rule you added in step 1 keeps your new SSH port open as well. See [How to set up the firewall on the Hiddify panel](/manager/basic-concepts-and-troubleshooting/How-to-setup-Firewall-on-Hiddify-panel/).

</div>
