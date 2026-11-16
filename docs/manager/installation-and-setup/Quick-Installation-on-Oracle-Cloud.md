---
title: Quick and easy installation on Oracle Cloud
weight: -60
---

<div dir="ltr" markdown="1">

# Quick installation on Oracle Cloud

Oracle Cloud supports **cloud-init**: you paste a setup script when you create the instance, and Hiddify Manager installs itself, without SSH. Oracle's **Always Free** tier includes Arm (Ampere A1) instances, which Hiddify Manager supports. This page is for Hiddify Manager v14.5; the general guide for any provider is [Easy installation through the data center (Cloud-init)](/manager/installation-and-setup/Cloud-init-installation/).

!!! info "The old Deploy to Oracle Cloud button is gone"
    Earlier versions of this page had a **Deploy to Oracle Cloud** button. The files it used are no longer in the repository; use the steps below instead.

## Before you start

- Choose a **Canonical Ubuntu 26.04** or **24.04** image. If neither is offered, 22.04 also works. Other versions are not supported.
- Choose an **amd64** or **Arm (Ampere)** shape.

## Installation steps

### Create the instance

1. In the [Oracle Cloud console](https://cloud.oracle.com/), open **Compute** › **Instances** and click **Create instance**.
2. Under **Image and shape**, choose **Canonical Ubuntu** and the shape. Keep **Assign a public IPv4 address** on, and add your SSH key.
3. Open **Show advanced options** › **Management**, choose **Paste cloud-init script**, then copy the code below and paste it there.

{% include 'cloud-init.yml' %}

### Open the ports

Oracle blocks incoming traffic by default. In **Networking** › **Virtual cloud networks** › your network › **Security Lists** › **Default Security List**, add **Ingress Rules** from `0.0.0.0/0` for **TCP 80** and **TCP 443** (and the UDP ports of protocols such as Hysteria2 or TUIC, if you use them).

Oracle's Ubuntu images also have their own firewall rules on the server. If the page still does not open after 15 minutes, connect with SSH and run:

```bash
sudo iptables -I INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -I INPUT -p tcp --dport 443 -j ACCEPT
```

### Finish

1. Click **Create**.
2. Wait 10 to 15 minutes for the installation to finish. Then [connect to the server with SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/) (the **Public IP address** is on the instance's page), or open the web console in your server provider's dashboard, and run `hiddify admin`. It shows your admin links; this is the server's normal, permanent admin link. Open one of them in your browser and keep it somewhere safe.
3. Now set up your domain and finish the installation:

<div class="hi-grid c2">
<a class="hi-card " href="/manager/installation-and-setup/Guide-for-setting-up-the-domain-and-finalizing-the-installation/"><span class="hi-ic green"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M16.36 14c.08-.66.14-1.32.14-2 0-.68-.06-1.34-.14-2h3.38c.16.64.26 1.31.26 2s-.1 1.36-.26 2m-5.15 5.56c.6-1.11 1.06-2.31 1.38-3.56h2.95a8.03 8.03 0 0 1-4.33 3.56M14.34 14H9.66c-.1-.66-.16-1.32-.16-2 0-.68.06-1.35.16-2h4.68c.09.65.16 1.32.16 2 0 .68-.07 1.34-.16 2M12 19.96c-.83-1.2-1.5-2.53-1.91-3.96h3.82c-.41 1.43-1.08 2.76-1.91 3.96M8 8H5.08A7.923 7.923 0 0 1 9.4 4.44C8.8 5.55 8.35 6.75 8 8m-2.92 8H8c.35 1.25.8 2.45 1.4 3.56A8.008 8.008 0 0 1 5.08 16m-.82-2C4.1 13.36 4 12.69 4 12s.1-1.36.26-2h3.38c-.08.66-.14 1.32-.14 2 0 .68.06 1.34.14 2M12 4.03c.83 1.2 1.5 2.54 1.91 3.97h-3.82c.41-1.43 1.08-2.77 1.91-3.97M18.92 8h-2.95a15.65 15.65 0 0 0-1.38-3.56c1.84.63 3.37 1.9 4.33 3.56M12 2C6.47 2 2 6.5 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2Z"/></svg></span><span class="tx"><b>Set up the domain and finish</b><small>Next step: point your domain to the server.</small></span></a>
<a class="hi-card " href="/manager/configuration-and-advanced-settings/How-to-configure-Hiddify-panel-properly/"><span class="hi-ic "><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 8a4 4 0 0 1 4 4 4 4 0 0 1-4 4 4 4 0 0 1-4-4 4 4 0 0 1 4-4m0 2a2 2 0 0 0-2 2 2 2 0 0 0 2 2 2 2 0 0 0 2-2 2 2 0 0 0-2-2m-2 12c-.25 0-.46-.18-.5-.42l-.37-2.65c-.63-.25-1.17-.59-1.69-.99l-2.49 1.01c-.22.08-.49 0-.61-.22l-2-3.46a.493.493 0 0 1 .12-.64l2.11-1.66L4.5 12l.07-1-2.11-1.63a.493.493 0 0 1-.12-.64l2-3.46c.12-.22.39-.31.61-.22l2.49 1c.52-.39 1.06-.73 1.69-.98l.37-2.65c.04-.24.25-.42.5-.42h4c.25 0 .46.18.5.42l.37 2.65c.63.25 1.17.59 1.69.98l2.49-1c.22-.09.49 0 .61.22l2 3.46c.13.22.07.49-.12.64L19.43 11l.07 1-.07 1 2.11 1.63c.19.15.25.42.12.64l-2 3.46c-.12.22-.39.31-.61.22l-2.49-1c-.52.39-1.06.73-1.69.98l-.37 2.65c-.04.24-.25.42-.5.42h-4m1.25-18-.37 2.61c-1.2.25-2.26.89-3.03 1.78L5.44 7.35l-.75 1.3L6.8 10.2a5.55 5.55 0 0 0 0 3.6l-2.12 1.56.75 1.3 2.43-1.04c.77.88 1.82 1.52 3.01 1.76l.37 2.62h1.52l.37-2.61c1.19-.25 2.24-.89 3.01-1.77l2.43 1.04.75-1.3-2.12-1.55c.4-1.17.4-2.44 0-3.61l2.11-1.55-.75-1.3-2.41 1.04a5.42 5.42 0 0 0-3.03-1.77L12.75 4h-1.5Z"/></svg></span><span class="tx"><b>Configure the panel properly</b><small>Every part of the panel, to get the most out of it.</small></span></a>
</div>

!!! note
    The Oracle console changes from time to time; if a field has another name, look for *cloud-init*, *user data* or *initialization script*.

## Related articles

<div class="hi-related" markdown="1">

- [![](/assets/logos/hetzner.svg) Hetzner](/manager/installation-and-setup/Quick-installation-on-Hetzner-Servers/)
- [![](/assets/logos/vultr.svg) Vultr](/manager/installation-and-setup/Quick-installation-on-Vultr-Servers/)
- [![](/assets/logos/ovh.svg) OVH](/manager/installation-and-setup/Quick-Installation-on-OVH-Servers/)
- [![](/assets/logos/microsoftazure.svg) Microsoft Azure](/manager/installation-and-setup/Quick-Installation-on-Microsoft-Azure/)

</div>

</div>
