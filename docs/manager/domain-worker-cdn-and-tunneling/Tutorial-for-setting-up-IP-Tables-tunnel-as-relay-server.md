---
title: Tutorial for setting up IP-Table tunnel as relay server
---

# Tutorial for setting up IP-Table tunnel as relay server

This page shows you how to turn a server into a relay for your Hiddify Manager server using IP-Tables, the firewall built into Linux. It is the simplest method: one script, no extra software to keep running.

A **relay server** is a second server, usually inside your own country, that your users connect to. It forwards their traffic to your main Hiddify server abroad. This helps when the main server's IP is blocked or slow from your country. [Read more about relay servers](/manager/domain-worker-cdn-and-tunneling/How-to-add-relay-domain-to-Hiddify-manager/#what-is-a-relay-server-and-why-use-one).

<div align=center markdown="1">

![Diagram: users connect to the relay server, which forwards traffic to the main server](https://github.com/hiddify/hiddify.com/assets/125398461/1ac4e9e4-4529-4c79-8ff5-eb40e2efad54)
</div>

There is also a [video tutorial in Persian](https://www.youtube.com/watch?v=kz_Ih__jS9c) for this method.

## Prerequisites

- A main server with Hiddify Manager installed. See the [installation guide](/manager/installation-and-setup/guide/).
- A relay server running Ubuntu or Debian, with a clean IP and enough bandwidth and CPU for your users. RAM matters little: a small, cheap server (for example 256 MB of RAM) is enough, and you can run several of them.
- SSH access to the relay server as `root`. New to SSH? See [how to connect to a server via SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/).
- The IP address of your main server.

## Set up the relay server

1. Connect to your **relay server** over SSH.
2. Run this command:

    ```bash
    bash <(curl https://gist.githubusercontent.com/hiddify-com/63836c9a158eca29bad6c941610028cf/raw/0e4e2138148ab9d3d678723fd904b1cad461ce62/relay.sh)
    ```

3. When asked `Enter your main server IP like(1.1.1.1):`, type your main server's IP and press `Enter`.
4. The script installs `iptables` and `iptables-persistent`. If a blue screen asks whether to save the current IPv4 (and IPv6) rules, choose **Yes**.

    The script forwards TCP ports `80` and `443`, and all UDP traffic, to your main server, and saves the rules so they come back after a reboot.

5. The script turns on IP forwarding (needed for the tunnel) only until the next reboot. Make it permanent:

    ```bash
    echo "net.ipv4.ip_forward=1" | sudo tee /etc/sysctl.d/99-relay.conf
    sudo sysctl --system
    ```

### Check that it worked

Run this on the relay server:

```bash
sudo iptables -t nat -L -n
```

You should see `DNAT` lines that point to your main server's IP. If you do not, run the script again and check the IP you typed.

## Add the relay server to Hiddify Manager

1. Point a subdomain (for example `relay.example.com`) at the **relay server's IP** with an `A` record. On Cloudflare, keep the proxy off (grey cloud).
2. In the panel, open **Domains**, click **Add domain**, enter the subdomain and choose the mode **Relay**.
3. Edit your subscription domain, select the relay domain under **Show configs of**, then apply the changes.

For the full steps, see [How to add a relay server (domain) to HiddifyManager](/manager/domain-worker-cdn-and-tunneling/How-to-add-relay-domain-to-Hiddify-manager/).

??? note "Screenshots from an older panel version"
    <img src="https://github.com/hiddify/hiddify.com/assets/125398461/4c0ade4e-394c-4d52-8067-f15d1778c9ed" alt="Adding a relay domain in an older panel version">

    <img src="https://github.com/hiddify/hiddify.com/assets/125398461/e9fa3756-bb3a-4ee9-8adb-77a9f58f6354" alt="Selecting the relay domain in the subscription domain settings, older panel version">

## Remove the relay rules

The forwarding rules live in the `nat` table. To delete them and save the empty rule set, run this on the relay server:

```bash
sudo iptables -t nat -F
sudo iptables-save | sudo tee /etc/iptables/rules.v4
```

!!! warning
    This deletes **every** rule in the `nat` table, including any you added yourself.

To also turn IP forwarding off, delete the file you created:

```bash
sudo rm /etc/sysctl.d/99-relay.conf
```
