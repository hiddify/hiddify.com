---
title: How to configure HiddifyManager properly (Getting familiar with its different parts)
weight: -150
---

<div dir="ltr" markdown="1">

# How to configure HiddifyManager properly

This page walks you through the first setup of the HiddifyManager admin panel and explains what each part of the panel does. Read it right after you install the panel, or whenever you want to know what a menu or setting is for.

!!! info "Updated for HiddifyManager v14"
    Since v13 the panel opens **Admin V2** by default, and in v14 the old (classic) admin pages redirect to it. The menu names on this page are the Admin V2 names. Most screenshots below were taken in an older version, so your screen will look different, but the ideas are the same.

The panel makes running proxies easier, but it cannot fix a blocked server or a broken domain. If you finish this page and your users still cannot connect, read [Troubleshooting connectivity issues](/manager/basic-concepts-and-troubleshooting/Troubleshooting-connectivity-issues-with-HiddifyManager-and-proxies/).

There is also a [video walkthrough in Persian](https://www.youtube.com/watch?v=OfvKL9CaOQU). It was recorded for an older version.

## Before you start

You need:

1. **A server with a clean IP.** A clean IP is one that is not blocked in your users' country. Check it with [How to make sure the server's IP or domain is clean](/manager/basic-concepts-and-troubleshooting/How-to-make-sure-the-server%27s-IP-or-domain-is-clean/). If the IP is blocked, get a new IP or a new server.
2. **HiddifyManager installed**, as described in the [installation guide](/manager/installation-and-setup/guide/). At the end of the install you get your **admin links**. The admin link contains your secret path and your admin ID, so it works like a password. See [the correct format of the admin link](/manager/domain-worker-cdn-and-tunneling/The-correct-format-of-admin-link/).
3. **A registered domain that is reachable.** A domain is a name such as `example.com` that points to your server. See [domain types and how to register them](/manager/domain-worker-cdn-and-tunneling/Domain-types-and-how-to-register-them/), then [check that the domain is clean](/manager/basic-concepts-and-troubleshooting/How-to-make-sure-the-server%27s-IP-or-domain-is-clean/).

If a word on this page is new to you, see [Basic concepts](/manager/basic-concepts-and-troubleshooting/Basic-Concepts/).

## Open the admin panel for the first time

- If you used a one-click install link from a provider such as Vultr or OVH, wait about 10 minutes. You then get a one-time link that opens the admin page.

![One-time admin link after a one-click install](https://user-images.githubusercontent.com/125398461/227714581-5034c5ac-9204-498c-8195-2ff2d0f66d84.png)

- If you installed over SSH, the admin links are printed in the terminal at the end of the install. Open one of the **Secure** (https, domain) links in your browser. Use the IP link only if no domain link works.
- If you lost the links, connect to your server over SSH and run:

```bash
hiddify admin
```

The first time you open the admin page, the **Quick setup** wizard starts.

## Quick setup

The wizard has a few short steps. You can change everything later in **Settings**.

1. **Welcome:** choose the admin panel language and the country your users are in. The country selects settings that suit its filtering.
2. **Password:** set a password for the admin area (at least 8 characters).
3. **Domains:** point your domain to the server IPs shown on the page (an `A` record for IPv4, `AAAA` for IPv6). Then type your domain and press Enter. The panel detects the domain type by itself; tap the type to change it. You need at least one direct, CDN or subscription-only domain.
4. **Protocols:** pick the protocols you want to offer. Choose as few as you need.
5. **Nodes** (optional): connect other Hiddify servers to manage them from this panel. You can skip this.
6. **Finish:** review your choices and click **Finish**. The panel applies the configuration and reinstalls the services. This takes a few minutes. The log and your new admin links are shown while it runs.

When it finishes, the panel is ready to use. Copy the new admin links and keep them somewhere safe.

![Quick setup page in an older version](https://user-images.githubusercontent.com/125398461/236670372-500351a3-d829-4665-af29-651451f45c2d.png)

## The admin menu

The Admin V2 sidebar has three groups:

- **Manager:** Dashboard, Users, Admins, Broadcast, Nodes and Utils.
- **Settings:** Proxy Editor, Domains, Settings, Backup, Actions (the **Apply & status** page) and, if you set one up, your Telegram bot.
- **Help:** links to the tutorials, bug reports and donations.

## Dashboard

The Dashboard shows your server's resources (CPU, RAM, disk, traffic) as charts. If you use several servers (nodes), it also shows the health of each node.

![Dashboard](https://user-images.githubusercontent.com/125398461/236671412-9887bac1-1ce6-45d7-ad9d-8d74ad1a32b2.png)

## Users

Here you create an account for each person who will use your proxies.

1. Open **Users** and click the add button.
2. Enter a name, the usage limit (in GB), the number of days (package days) and the reset mode.
3. Save.

<img src="https://user-images.githubusercontent.com/125398461/236673236-3ca6b99a-2586-4755-b21e-4e6f85405135.png" alt="Users list">

<img width="1259" src="https://user-images.githubusercontent.com/125398461/236682495-988f2cc9-52b6-42c0-ac07-d19553425dd4.png" alt="Create user form">

Each user has their own **user page**. Open it from the link next to the user. At the top of the user page the user can download a client app for their device. Further down are the user's configs.

<img width="1280" src="https://user-images.githubusercontent.com/125398461/236682677-4b72bb63-d4c0-41d2-b0e5-05786770aa00.png" alt="User page">

![Configs on the user page](https://user-images.githubusercontent.com/125398461/236682704-86f4b740-172f-442e-a31f-73752c7aea43.png)

You can give users access in three ways:

1. **The user page link (recommended).** The user opens it and finds everything there.
2. **The subscription link.** A subscription link is one address that the app re-reads to get the latest configs. If you change your settings, the user's app updates itself.
3. **A single config link.** It does not update. If you change your settings, you must send the user a new link.

For help connecting client apps, see the [YouTube playlist](https://www.youtube.com/watch?v=Ml7XeYp70mM&list=PL2DSfh6Z6tTIalRDm3hY7G7ku9-yrCfBL) and the client tutorials on the [HiddifyManager tutorials page](/manager/).

## Admins

Here you create accounts for other people who help you manage the panel. Click the add button and fill in the form.

<img width="1201" src="https://user-images.githubusercontent.com/125398461/236682754-91aa4f0e-2b12-483d-a06a-14109adb87bc.png" alt="Admins list">

There are three admin types:

- **Super admin:** full access to the whole panel and all settings.
- **Admin:** can manage users and some settings.
- **Agent:** can only manage users.

For each admin you can:

- limit the number of users and active users;
- allow or forbid adding sub-admins;
- reset their password.

!!! note
    Each admin's link contains their secret ID. If you change it, that admin's panel address changes completely. See [the correct format of the admin link](/manager/domain-worker-cdn-and-tunneling/The-correct-format-of-admin-link/).

## Domains

Open **Settings → Domains** to add or edit your domains. Each domain has a **type**, which says how users reach your server, and a **TLS mode**, which says which certificate or disguise it uses.

Domain types:

- **Direct:** the domain points straight to your server's IP. If the domain is on Cloudflare, keep the cloud off (DNS only).
- **CDN:** the domain goes through a CDN such as Cloudflare (orange cloud on). A **CDN** is a network of servers that sits between your users and your server, so your server's IP stays hidden.
- **Relay:** users connect to another server in between, which forwards the traffic to this one.
- **Subscription only:** used only for subscription links, with no proxies.
- **Cloudflare Worker:** Cloudflare workers are created for this domain automatically.

TLS modes: **Valid TLS** (a real certificate issued automatically), **Fake**, **Reality** and **DNS** (DNS tunnel only).

!!! info "Changed in v13"
    The old separate types **Auto CDN IP**, **Fake** and **Reality** are no longer domain types. On upgrade, Auto CDN IP domains became **CDN** domains, and Fake and Reality domains became **Direct** domains with the **Fake** or **Reality** TLS mode.

### Direct domain

Click the add button and fill in the form.

![Direct domain form](https://user-images.githubusercontent.com/125398461/236682821-4b721589-8adc-43e8-b90e-8c096aa27c6e.png)

- **Display name:** shown in the users' apps instead of the domain. Use it if you don't want the domain to appear in the configs.
- **Force configs to use these IPs / domains:** leave it empty for a direct domain. It is mainly for CDN domains.
- **Show configs of:** choose which domains' configs users see when they open their user page through this domain.

### Subscription-only domain

A subscription-only domain only serves subscription links. Because no proxy traffic goes through it, it is less likely to be blocked, so users can always update their configs.

![Subscription-only domain](https://user-images.githubusercontent.com/125398461/236683456-2e99c6f2-ab23-4c54-a5cf-89e565472e8f.png)

After you link the subscription-only domain to your connection domains in **Show configs of**, open a user page through it. The configs on that page use your connection domains.

Tip: a subscription domain works best behind a CDN, so users can still update when your proxy domains are blocked. You can also use a PHP website for subscription links: see [How to use a PHP site for sub links](/manager/domain-worker-cdn-and-tunneling/How-to-use-a-PHP-site-for-sub-links/).

### CDN domain { #cdn-domain }

Click the add button and fill in the form.

![CDN domain form](https://user-images.githubusercontent.com/125398461/236682963-aa6bf603-7449-43f2-9639-436332043e2a.png)

- **Display name:** shown in the users' apps instead of the domain.
- **Force configs to use these IPs / domains:** put a clean Cloudflare IP here, or better, a normal DNS record (cloud off) that points to a clean IP. Then, when you need a new clean IP, you only update that DNS record and the panel and configs stay the same. To find clean IPs, see [Guide for finding a clean Cloudflare IP](/manager/domain-worker-cdn-and-tunneling/Guide-for-finding-a-clean-Cloudflare-IP/). This field replaces the old Auto CDN IP mode: see [Guide for using mode Auto_CDN_IP](/manager/domain-worker-cdn-and-tunneling/Guide-for-using-mode-Auto_CDN_IP-on-Hiddify/).
- **Domain fronting:** optional. Users' apps show another site's name (SNI) instead of your domain, so a filter only sees that other site. Use sites on the same CDN as your domain. In older versions this was a global setting; now it is set per CDN domain. See [Guide for domain fronting](/manager/domain-worker-cdn-and-tunneling/Guide-for-domain-fronting/).
- **ECH:** uses Encrypted Client Hello for this CDN domain. Turn on **Enable TLS ECH** in **Settings** first.
- **Show configs of:** choose which domains' configs users see on this domain's user page.

If you have many users and want to give each group its own domain, read [How to use multi-CDN domains](/manager/domain-worker-cdn-and-tunneling/How-to-use-multiCDN-domains-in-HiddifyManager/).

### Other domain setups

- **Relay domain:** see [How to add a relay domain](/manager/domain-worker-cdn-and-tunneling/How-to-add-relay-domain-to-Hiddify-manager/).
- **Fake TLS mode:** see [How to create and use a fake domain](/manager/domain-worker-cdn-and-tunneling/How-to-create-and-use-fake-domain/).
- **Reality TLS mode:** see [How to use Reality](/manager/configuration-and-advanced-settings/How-to-use-Reality-on-Hiddify/).
- **Cloudflare Worker:** see [How to set up and use Cloudflare workers](/manager/domain-worker-cdn-and-tunneling/How-to-set-up-and-use-Cloudflare-workers/).

## Proxies and protocols

You turn protocols on or off in **Settings → Settings**, in the **Proxies Settings** group. The **Proxy Editor** lets advanced users edit each built-in proxy template.

<img width="1188" src="https://user-images.githubusercontent.com/125398461/236683886-a08db1ce-5939-4d96-80ef-4dd1c40e129b.png" alt="Proxy settings in an older version">

Note: plain HTTP connections are not encrypted. TLS connections are encrypted.

## Settings

Open **Settings → Settings**. Common settings are shown first. Click **Show advanced settings** to see the rest, or use the search box. Settings marked **Reinstall** only take effect after a reinstall (see [Actions](#apply-status)). The groups are described below.

### Admin Settings

<img width="573" src="https://user-images.githubusercontent.com/125398461/236683990-4bf2b03a-b080-4479-91f2-aff85ef326e0.png" alt="Admin settings">

- **Admin Panel Language:** the language of the admin area. Admin V2 is translated into English and Persian; other languages fall back to English.
- **Parent Panel (Multi Server):** connect this panel to a central (parent) panel. You then define users on the parent panel, and the usage of all servers is added up there.
- **Node name:** a name for this server when it is part of a multi-server setup.

### Customizing User Page

<img width="574" src="https://user-images.githubusercontent.com/125398461/236684199-cbd46efc-c13b-4263-ba35-c94d5915224f.png" alt="Customizing the user page">

- **User Area Language:** the language of the user page.
- **User Page Title:** your brand name, shown at the top of the user page.
- **Support Link:** a link to your support channel.
- **Support Section Text:** a message shown in the support box of the user page.

### General Settings

<img width="568" src="https://user-images.githubusercontent.com/125398461/236684249-02f6d52d-09dd-491a-baf2-b18b78241279.png" alt="General settings">

- **Country:** the country of your users. It selects settings that suit that country's filtering. Changing it needs a reinstall.
- **Auto Update:** lets the panel update itself.
- **Only IPv4:** turns off IPv6 on the server.
- **Speed Test:** lets users test their connection speed to your server.
- **Decoy Site:** a fake website. If someone (for example a filtering system) opens your domain directly, they see this site instead of your panel, which makes your server harder to identify. Do not use bank, payment, Iranian or very famous sites.
- **Firewall:** when on, only the ports Hiddify needs (such as 22, 80 and 443) stay open and all other ports are closed.
- **DNS Server**, **Show Usage in Sublink**, **Torrent Block** and **Keep Backups (days)** are also here. **Keep Backups (days)** deletes automatic backups older than this number of days; `0` keeps all of them.

### Proxies Settings

<img width="575" src="https://user-images.githubusercontent.com/125398461/236684281-c32f4141-ad33-4866-9bf9-99d429758278.png" alt="Proxy settings">

- **Block Domestic Sites:** blocks traffic from your server to Iranian sites and `.ir` domains. This makes it harder for the filtering system to identify your server. We recommend turning it on.
- **Shared Secret:** a password used by connections whose traffic is not counted per user.
- On/off switches for protocols and transports, for example **VLess**, **Trojan**, **VMess**, **Reality**, **Websocket**, **gRPC**, **HTTPUpgrade**, **XHTTP**, **TCP**, **QUIC**, **Naive**, **AnyTLS**, **Snell** and **SOCKS**.

Tip: in the Hiddify app, routing rules can send traffic for Iranian sites directly, without the proxy. This saves your server's traffic.

!!! info "Removed settings"
    The old **V2Ray** switch is gone. The browser fingerprint setting (**uTLS**) is now under **Advanced Settings**.

### Domain fronting

The old global **Domain Fronting** settings group was removed. Domain fronting is now set on each CDN domain (see [CDN domain](#cdn-domain)). More information: [Guide for domain fronting](/manager/domain-worker-cdn-and-tunneling/Guide-for-domain-fronting/).

<img width="581" src="https://user-images.githubusercontent.com/125398461/236684655-3d8c0123-c66a-44ae-8e83-599b8f8720da.png" alt="Old domain fronting settings (removed)">

### Telegram Configs

A Telegram proxy works only inside the Telegram app and helps users bypass Telegram filtering.

<img width="569" src="https://user-images.githubusercontent.com/125398461/236684736-23daa824-cb42-4a6b-94ed-9c1594f46502.png" alt="Telegram proxy settings in an older version">

- **MTProxy FakeTLS Enable:** turns the Telegram proxy on or off.
- **Telegram Web Proxy Enable:** turns on the Telegram web proxy.
- **Telegram AD Tag:** an advertising tag that shows your channel in the user's Telegram chat list.
- **Telegram Fake Domain:** a domain whose name is used to disguise the proxy traffic.
- **Telegram Bot Token:** connects the panel to your Telegram bot. See [How to set up and use the Telegram bot](/manager/configuration-and-advanced-settings/How-to-set-up-and-use-Telegram-bot-on-Hiddify-panel/).

!!! info "Changed in v14"
    The Telegram proxy now always uses **telemt**. The old choice of Telegram proxy library (Python, Erlang and others) was removed.

### HTTP Configuration

<img width="578" src="https://user-images.githubusercontent.com/125398461/236684772-39b2fe70-6ea5-4a6a-84dd-bec43ac3232e.png" alt="HTTP settings in an older version">

- **Allow HTTP Connection:** allows unencrypted HTTP connections. We don't recommend turning it on.

The custom HTTP port list was removed in v14. Proxies are served on ports 80 and 443 whenever possible.

### TLS Settings

<img width="563" src="https://user-images.githubusercontent.com/125398461/236684810-8a3c1cdf-f49e-48e6-a059-834c9c8e8a50.png" alt="TLS settings in an older version">

- **Certificate (ACME) Email:** the email used when the panel requests certificates.
- **Enable TLS ECH:** turns on Encrypted Client Hello support. You then enable it per CDN domain.
- **Allow Invalid SNI**.

The custom TLS port list was removed in v14. Since v14 the panel issues and stores certificates itself.

The **TLS Trick** group (TLS fragment, mixed SNI case, padding) is explained in [How the TLS trick works](/manager/basic-concepts-and-troubleshooting/How-the-TLS-Trick-works-and-its-usage/).

### Shadowsocks

**Shadowsocks FakeTLS** is a simple disguise that wraps data in TLS-looking packets to fool the filter.

<img width="575" src="https://user-images.githubusercontent.com/125398461/236684838-aec3d882-fbeb-46cb-b072-2f1336ab9b63.png" alt="Shadowsocks settings">

- **Shadowsocks 2022:** turns Shadowsocks 2022 on or off.
- **Shadowsocks FakeTLS (Simple OBFS):** we don't recommend it.
- **SS FakeTLS FakeDomain:** the fake domain used to disguise the packets.

### ShadowTLS

ShadowTLS shows the firewall a real TLS handshake with a valid certificate from a site you choose. Its switch and fake domain are in the **Shadowsocks** group.

!!! warning
    The ShadowTLS service was removed from HiddifyManager in v13. Whether ShadowTLS configs still work is not confirmed, so don't rely on it.

<img width="572" src="https://user-images.githubusercontent.com/125398461/236684908-91bffbe0-96b9-49a7-8dd1-e51534b02b27.png" alt="ShadowTLS settings in an older version">

### Advanced Settings

These settings are for experienced users.

<img width="572" src="https://user-images.githubusercontent.com/125398461/236685004-e2f45048-3dea-48fa-b90e-219905293a23.png" alt="Advanced settings in an older version">

- **Package Update Mode:** choose **Release** (stable) or **Beta** updates.
- **Common Proxy Core:** which engine serves the shared proxies: `xray`, `hiddify_core` or `both`. It replaces the old **Core** setting.
- **uTLS:** which browser fingerprint the configs imitate (for example Chrome, Firefox, Safari, iOS or Android).

The parent panel link and the Telegram bot token moved to **Admin Settings** and **Telegram Configs**.

### Very Advanced Settings

<img width="614" alt="Very advanced settings" src="https://user-images.githubusercontent.com/125398461/236685035-9d878767-98fb-464d-8a99-0f056352c0e5.png">

- **Proxy Path for Admins** and **Proxy Path for Clients:** the secret paths in your admin and user links. They hide your panel and connections from the filter. The panel sets them for you; change them only if you need to. If you change the admin path, your admin link changes.
- **Cloudflare API**.

The per-protocol path settings were hidden in v13.

### WARP and Reality

- **WARP:** see [How to activate WARP](/manager/configuration-and-advanced-settings/How-to-activate-WARP-on-the-Hiddify-panel/).
- **Reality:** see [How to use Reality](/manager/configuration-and-advanced-settings/How-to-use-Reality-on-Hiddify/).

### SSH Proxy

The SSH proxy service was removed in v13 and is no longer installed, even though its settings group may still appear. See [SSH proxy setting](/manager/configuration-and-advanced-settings/SSH-proxy-setting-on-Hiddify-panel/).

## Backup

Open **Settings → Backup** to make a backup of your panel or restore one.

<img width="1220" src="https://user-images.githubusercontent.com/125398461/236685069-22011cc0-ebdd-4e30-9077-c4237242f32b.png" alt="Backup page in an older version">

- **Download backup** saves everything in one `.json` file: settings, users, admins, domains, proxies and certificates. Keep the file safe: it contains passwords and private keys.
- The panel also makes automatic backups on the server every 6 hours. They are listed under **Backups on the server**. If your Telegram bot is connected, each one is also sent to you on Telegram.
- When you restore, you choose which parts to bring back: **Settings**, **Users** and **Domains**.

Details: [How to back up and restore](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/).

## Telegram bot

To set up and use the panel's Telegram bot, see [How to set up and use the Telegram bot](/manager/configuration-and-advanced-settings/How-to-set-up-and-use-Telegram-bot-on-Hiddify-panel/).

## Actions (Apply & status) { #apply-status }

Open **Settings → Actions**. The **Apply & status** page lets you put changes into effect, update the server and see how everything is doing. Each action shows its log while it runs. You can leave the page; the action keeps running on the server.

<img width="97" src="https://user-images.githubusercontent.com/125398461/236685118-f3524067-6251-4835-b50a-4832cb2e5f95.png" alt="Actions menu in an older version">

### Check status

Shows whether each service is running, plus the server's public IP and WARP. It changes nothing.

<img width="1207" src="https://user-images.githubusercontent.com/125398461/236685140-6d0dca77-9d82-4486-92cd-e6020167f9b6.png" alt="Status log">

### Logs

The **Logs** section lists what each action did. Click **View** to read a log.

<img width="607" src="https://user-images.githubusercontent.com/125398461/236685170-1357ea59-4b89-4f29-840e-8e08b536e4b3.png" alt="Logs in an older version">

### Apply changes

Puts your settings, users and domain changes into effect. It is quick, and it is the usual choice after you change something.

<img width="1185" src="https://user-images.githubusercontent.com/125398461/236685205-372dae9c-63c7-4a54-a72d-e2cd0b23f8cf.png" alt="Applying changes in an older version">

- When it finishes, the page shows your admin links on your domains. They may have changed, so copy them before you leave.
- If the panel no longer opens after a change, connect to your server over SSH and run `hiddify admin` to see your current admin links:

```bash
hiddify admin
```

- If that does not help, see [How to connect and troubleshoot via SSH](/manager/configuration-and-advanced-settings/How-to-connect-and-troubleshoot-via-SSH/).

<img width="371" src="https://user-images.githubusercontent.com/125398461/236685271-67ab8704-b3f2-4f08-970d-bf4dceab5ff3.png" alt="Success message in an older version">

### Update Hiddify

Downloads and installs the latest version, then applies it. It takes a while, and the panel restarts at the end. See [How to update HiddifyManager](/manager/configuration-and-advanced-settings/How-to-update-Hiddify-panel/).

<img width="1177" src="https://user-images.githubusercontent.com/125398461/236685314-79d9cdda-c04f-4153-a101-a55c770f91c4.png" alt="Update in an older version">

### Reinstall

Installs everything again and rebuilds all services. Your users and links are not changed. Use it when **Apply changes** is not enough, for example after you change the panel path, protocols or a setting marked **Reinstall**. Connections may drop for a few minutes.

<img width="1182" src="https://user-images.githubusercontent.com/125398461/236685416-c27a0a3e-0a10-49b2-914c-c0765dcadf8d.png" alt="Reinstall in an older version">

### Restart services

Restarts all Hiddify services without reinstalling anything. It is a good first try when something misbehaves. Connections drop for a moment.

<img width="1181" src="https://user-images.githubusercontent.com/125398461/236685466-8f82e0d3-98da-4614-a4ba-37ad3c2d257d.png" alt="Restart in an older version">

## Help

All tutorials and videos are listed on the [HiddifyManager tutorials page](/manager/).

</div>
