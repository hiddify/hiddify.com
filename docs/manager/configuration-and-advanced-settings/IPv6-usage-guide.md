---
title: IPv6 Usage Guide
---

<div dir="ltr" markdown="1">

# IPv6 Usage Guide

This page shows you how to give your users configs that connect to your server over IPv6. It is for panel admins whose server has an IPv6 address and whose users' internet supports IPv6.

## What is IPv6?
**IPv6** (Internet Protocol version 6) is the newer kind of internet address. It replaces the older IPv4 addresses (like `1.2.3.4`). An IPv6 address is longer and looks like `2001:db8::1`.

There are far more IPv6 addresses than IPv4 addresses, so blocking them one by one is harder and costlier for filtering systems. For this reason, IPv6 connections are often blocked less than IPv4 ones.

## Prerequisites
1. **Your server has IPv6.** Your provider (data center) must enable IPv6 on your server. Ask them if you are not sure. To see your server's IPv6 address, run this command on your server over SSH:

    ```bash
    ip -6 addr show scope global
    ```

    The address is on the line that starts with `inet6`. If nothing is shown, your server has no public IPv6 address.

2. **IPv6 is not turned off in the panel.** In the panel sidebar, under **Settings**, click **Settings**. In **General Settings**, make sure **Only IPv4** is off. (If it is on, IPv6 is disabled on the server.)
3. **Your users' internet supports IPv6.** Only some internet operators support IPv6. In Iran, for example, it was available on Irancell and Rightel, and on Hamrah-e Aval and Mokhaberat only in some regions. Check with your users.

!!! tip
    The **Max Proxy IPs Per Version** setting (in **General Settings**) controls how many IPv4 and how many IPv6 addresses the panel uses to build proxies for each domain.

## Use IPv6 in the panel

### Method 1: Direct domain (recommended)
1. In your DNS provider (for example Cloudflare), create a record of type **AAAA** for a subdomain (for example `v6.example.com`). Put your server's IPv6 address as its value. In Cloudflare, turn the proxy (orange cloud) **off**, so it says **DNS only**.
2. In the panel sidebar, under **Settings**, click **Domains**.
3. Click **Add domain**.
4. Type the subdomain you created and continue.
5. For the mode, choose **Direct**. For TLS, choose **Valid TLS**.
6. Finish the wizard. The panel gets a certificate for the domain.
7. Apply the changes when the panel asks you to.

Leave **Custom proxies** on **Automatic** so the panel uses every proxy that fits this domain.

### Method 2: Reality
1. In the panel sidebar, under **Settings**, click **Domains**, then **Add domain**.
2. As the domain, type a Reality-friendly site, for example `www.speedtest.net`.
3. For the mode, choose **Direct**. For TLS, choose **Reality**.
4. In **Server names**, enter the same site (for example `www.speedtest.net`).
5. Open **Advanced**. In **Force configs to use these IPs / domains**, enter your server's IPv6 address.
6. Save, then apply the changes.

For more about Reality, see [How to use Reality on Hiddify](/manager/configuration-and-advanced-settings/How-to-use-Reality-on-Hiddify/).

!!! note "Legacy Direct XTLS mode was removed"
    Older versions had a separate "Legacy Direct XTLS" domain mode. Since Hiddify Manager v13 it no longer exists: such domains were turned into **Direct** domains. Use Method 1 instead.

## Turn on IPv6 on your users' devices

### On Android
1. Open the phone's **Settings** and search for **APN**.
2. Open the APN in use and set **APN protocol** (or "Internet Protocol") to **IPv4/IPv6**.

### On Windows
1. Open **Control Panel**.
2. Go to **Network and Internet**, then **Network and Sharing Center**.
3. In the side menu, click **Change adapter settings**.
4. Right-click your connected network and choose **Properties**.
5. Tick **Internet Protocol Version 6 (TCP/IPv6)** and click **OK**.

### On iOS
1. Open [this website](https://mobileconfig.azurewebsites.net).
2. Enter `google.com` in the first two fields and tick **IPv4/IPv6**.
3. Download the profile. Install it from **Settings** → **Profile Downloaded**.
4. In **Settings**, search for **APN**, and reset the network settings from the bottom of that page.

When these steps are done, your users can connect to your server over IPv6. If you do not want IPv6 at all, see [How to disable IPv6 on Hiddify](/manager/basic-concepts-and-troubleshooting/How-to-disable-IP-version-6-on-Hiddify/).

</div>
