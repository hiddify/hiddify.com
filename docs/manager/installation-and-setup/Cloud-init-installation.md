---
title: Easy installation through the data center (Cloud-init)
weight: -45
---

<div dir="ltr" markdown="1">

# Easy installation through the data center (Cloud-init)

Use this page if your server provider lets you paste a setup script when you create a server. Hiddify Manager then installs itself automatically, and you don't need to connect over SSH.

**Cloud-init** is a standard tool that runs a setup script the first time a new server starts. Most providers (Hetzner, Vultr, OVH, DigitalOcean and others) support it. The field is often called **User data**, **Cloud-init** or **Custom data**.

## Before you start

- Choose **Ubuntu 22.04, 24.04 or 26.04** as the server's operating system. Other versions are not supported.
- Choose an **amd64 (x86_64)** or **arm64** server.

## Steps

### Create the server

1. Start creating a new server in your provider's dashboard.
2. Find the cloud-init / user data field.
3. Copy the code below and paste it into that field.

{% include 'cloud-init.yml' %}

### Finish

1. Create the server.
2. Wait 10 to 15 minutes for the installation to finish.
3. Open `http://YOUR-SERVER-IP/` in your browser (replace `YOUR-SERVER-IP` with your server's IP address). You will see a temporary link to your admin panel. This link works for **one hour only**, so open it soon.

If the page does not open after 15 minutes, wait a few more minutes and try again. If the hour has passed, connect to the server over SSH and get the admin links with the `hiddify admin` command (see the [main installation guide](/manager/installation-and-setup/guide/)).

Then continue with [setting up the domain and finalizing the installation](/manager/installation-and-setup/Guide-for-setting-up-the-domain-and-finalizing-the-installation/).

</div>
