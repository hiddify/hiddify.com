---
title: Tutorial for setting up GOST tunnel as relay server
---

# Tutorial for setting up GOST tunnel as relay server

This page shows you how to turn a server into a relay for your Hiddify Manager server using **GOST** (GO Simple Tunnel), a small open-source program that forwards ports from one server to another.

A **relay server** is a second server, usually inside your own country, that your users connect to. It forwards their traffic to your main Hiddify server abroad. This helps when the main server's IP is blocked or slow from your country. [Read more about relay servers](/manager/domain-worker-cdn-and-tunneling/How-to-add-relay-domain-to-Hiddify-manager/#what-is-a-relay-server-and-why-use-one).

<div align="center" dir="ltr" markdown="1">

![Diagram: users connect to the relay server, which forwards traffic to the main server](https://github.com/hiddify/hiddify.com/assets/125398461/1ac4e9e4-4529-4c79-8ff5-eb40e2efad54)
</div>

There is also a [video tutorial in Persian](https://youtu.be/T3yfTqqQqJQ) for this method.

## Why GOST instead of plain IP-Tables forwarding?

- You can point the tunnel at your main server's **domain** instead of its IP, so the IP does not appear in the relay's settings.
- It runs as a system service, so it starts again by itself after a reboot.
- It works with any protocol Hiddify offers (VLESS, VMess, Trojan, WebSocket, gRPC and others), because it forwards raw TCP traffic. Your proxy traffic stays encrypted by the proxy protocol itself.
- You can forward as many ports as you like, TCP or UDP.

!!! tip "Easier option"
    [Hiddify Relay Builder](/manager/domain-worker-cdn-and-tunneling/How-to-setup-relay-server-using-Hiddify-Relay-Builder/) can install GOST for you from a menu.

## Prerequisites

- A main server with Hiddify Manager installed. See the [installation guide](/manager/installation-and-setup/guide/).
- A relay server running Ubuntu or Debian, with SSH access as `root`. New to SSH? See [how to connect to a server via SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/).
- A domain that points **directly** to your main server's IP (proxy off, not through a CDN), or just the main server's IP.

## Install GOST on the relay server

1. Connect to your **relay server** over SSH.
2. Download GOST and unpack it:

    ```bash
    sudo apt install wget nano -y
    wget https://github.com/ginuerzh/gost/releases/download/v2.11.5/gost-linux-amd64-2.11.5.gz
    gunzip gost-linux-amd64-2.11.5.gz
    ```

    This is the build for normal x86-64 (amd64) servers. On an ARM server, use `gost-linux-armv8-2.11.5.gz` instead, and change the file name in the next step to match.

3. Move the program to the system folder and make it executable:

    ```bash
    sudo mv gost-linux-amd64-2.11.5 /usr/local/bin/gost
    sudo chmod +x /usr/local/bin/gost
    ```

4. Create a service file, so GOST runs in the background and after reboots. Open the editor:

    ```bash
    sudo nano /usr/lib/systemd/system/gost.service
    ```

5. Paste this text into the editor:

    ```ini
    [Unit]
    Description=GO Simple Tunnel
    After=network.target
    Wants=network.target

    [Service]
    Type=simple
    ExecStart=/usr/local/bin/gost -L=tcp://:443/domain.com:443 -L=tcp://:80/domain.com:80

    [Install]
    WantedBy=multi-user.target
    ```

6. Replace **both** `domain.com` with your main server's direct domain (or its IP).
7. Save with `Ctrl+S` and exit with `Ctrl+X`. (In older nano versions, press `Ctrl+X`, then `Y`, then `Enter`.)
8. Start the service and make it start on every boot:

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable --now gost
    ```

### Check that it worked

```bash
sudo systemctl status gost
```

You should see `active (running)`. Press `q` to leave this screen. If it says `failed`, check the `ExecStart` line for typos, fix it, and run the two commands from step 8 again.

To forward more ports, add another `-L=tcp://:PORT/domain.com:PORT` to the `ExecStart` line. For UDP, write `udp://` instead of `tcp://`.

!!! note "About GOST versions"
    This page uses GOST v2.11.5 from the original [ginuerzh/gost](https://github.com/ginuerzh/gost) project. Its last release is v2.12.0 (October 2024). The actively developed version is GOST v3 at [go-gost/gost](https://github.com/go-gost/gost); Hiddify Relay Builder installs v3 and uses the same `-L=tcp://...` style of command.

## Add the relay server to Hiddify Manager

1. Point a subdomain (for example `relay.example.com`) at the **relay server's IP** with an `A` record. On Cloudflare, keep the proxy off (grey cloud).
2. In the panel, open **Domains**, click **Add domain**, enter the subdomain and choose the mode **Relay**.
3. Edit your subscription domain, select the relay domain under **Show configs of**, then apply the changes.

For the full steps, see [How to add a relay server (domain) to HiddifyManager](/manager/domain-worker-cdn-and-tunneling/How-to-add-relay-domain-to-Hiddify-manager/).

??? note "Screenshots from an older panel version"
    <img src="https://github.com/hiddify/hiddify.com/assets/125398461/4c0ade4e-394c-4d52-8067-f15d1778c9ed" alt="Adding a relay domain in an older panel version">

    <img src="https://github.com/hiddify/hiddify.com/assets/125398461/e9fa3756-bb3a-4ee9-8adb-77a9f58f6354" alt="Selecting the relay domain in the subscription domain settings, older panel version">


## Remove GOST from the relay server

Run these commands on the relay server:

```bash
sudo systemctl disable --now gost
sudo rm -f /usr/lib/systemd/system/gost.service /usr/local/bin/gost
sudo systemctl daemon-reload
```
