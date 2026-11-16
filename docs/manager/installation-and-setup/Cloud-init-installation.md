---
title: Easy installation through the data center (Cloud-init)
weight: -45
---

<div dir="ltr" markdown="1">

# Easy installation through the data center (Cloud-init)

Use this page if your server provider lets you paste a setup script when you create a server. Hiddify Manager then installs itself automatically while the server starts; you only connect once at the end, to see your admin link.

**Cloud-init** is a standard tool that runs a setup script the first time a new server starts. Most providers (Hetzner, Vultr, OVH, DigitalOcean and others) support it. The field is often called **User data**, **Cloud-init** or **Custom data**.

## Before you start

- Choose **Ubuntu 26.04** or **24.04** as the server's operating system. If neither is offered, Ubuntu 22.04 also works. Other versions are not supported.
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
3. [Connect to the server with SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/), or open the web console in your server provider's dashboard, and run `hiddify admin`. It shows your admin links: this is the server's normal, permanent admin link (there is no one-hour temporary link any more). Open one of them in your browser and keep it somewhere safe.

If `hiddify admin` says the command is not found, the installation is not finished yet: wait a few more minutes and try again.

Then:

<div class="hi-grid" style="grid-template-columns:1fr">
<a class="hi-card big" href="/manager/installation-and-setup/Guide-for-setting-up-the-domain-and-finalizing-the-installation/"><span class="hi-ic green"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M16.36 14c.08-.66.14-1.32.14-2 0-.68-.06-1.34-.14-2h3.38c.16.64.26 1.31.26 2s-.1 1.36-.26 2m-5.15 5.56c.6-1.11 1.06-2.31 1.38-3.56h2.95a8.03 8.03 0 0 1-4.33 3.56M14.34 14H9.66c-.1-.66-.16-1.32-.16-2 0-.68.06-1.35.16-2h4.68c.09.65.16 1.32.16 2 0 .68-.07 1.34-.16 2M12 19.96c-.83-1.2-1.5-2.53-1.91-3.96h3.82c-.41 1.43-1.08 2.76-1.91 3.96M8 8H5.08A7.923 7.923 0 0 1 9.4 4.44C8.8 5.55 8.35 6.75 8 8m-2.92 8H8c.35 1.25.8 2.45 1.4 3.56A8.008 8.008 0 0 1 5.08 16m-.82-2C4.1 13.36 4 12.69 4 12s.1-1.36.26-2h3.38c-.08.66-.14 1.32-.14 2 0 .68.06 1.34.14 2M12 4.03c.83 1.2 1.5 2.54 1.91 3.97h-3.82c.41-1.43 1.08-2.77 1.91-3.97M18.92 8h-2.95a15.65 15.65 0 0 0-1.38-3.56c1.84.63 3.37 1.9 4.33 3.56M12 2C6.47 2 2 6.5 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2Z"/></svg></span><span class="tx"><b>Set up the domain and finish</b><small>Next step: point your domain to the server.</small></span></a>
</div>

## Related articles

<div class="hi-related" markdown="1">

- [Install a specific version](/manager/installation-and-setup/How-to-install-different-versions-of-Hiddify-Manager/)
- [![](/assets/logos/docker.svg) Install with Docker](/manager/installation-and-setup/Install-Hiddify-using-Docker/)
- [Installation prerequisites](/manager/installation-and-setup/Installation-prerequisites/)
- [Connect to your server with SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/)

</div>

</div>
