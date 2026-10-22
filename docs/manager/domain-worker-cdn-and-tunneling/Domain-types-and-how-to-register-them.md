---
title: Domain types and how to register them
description: The domain modes in HiddifyManager (Direct, CDN, Relay, Cloudflare Worker, Subscription only, and the TLS modes Fake and Reality) and how to register a domain for each one.
---

<div dir="ltr" markdown="1">

# Domain types and how to register them

This page explains the kinds of domains you can add to HiddifyManager and how to set up each one at your DNS provider. Read it before you add your first domain to the panel.

A **domain** is a name such as `sub.example.com` that points to an IP address. A **subdomain** is the part you add in front of your main domain (`sub` in `sub.example.com`). A **DNS record** is the entry at your DNS provider that tells the internet which IP a name points to. For more basics, see [Basic concepts](/manager/basic-concepts-and-troubleshooting/Basic-Concepts/).

!!! info "Domain types changed in HiddifyManager v13"
    Since v13, every domain has a **Mode** and a **TLS mode**. The old modes were moved automatically when you upgraded:

    - `auto_cdn_ip` became **CDN** (with "Resolve IP" turned on).
    - `fake` became **Direct** with TLS mode **Fake**.
    - `reality` and `special_reality_*` became **Direct** with TLS mode **Reality**.
    - `old_xtls_direct` became **Direct**.
    - "Use only for subscription link" became the **Subscription only** mode.

## Domain modes in the panel

In the panel, open the **Domains** page and select **Add domain**. A short wizard asks for the domain, then "How is it set up?" (the mode), then "Which TLS?" (the TLS mode).

| Mode | When to use it | What your DNS record must do |
|---|---|---|
| **Direct** | Users connect straight to your server. | Point to your server's IP. On Cloudflare, the proxy must be off (**DNS only**, grey cloud). |
| **CDN** | Your server sits behind a CDN such as Cloudflare. This hides your server's IP and keeps working when the IP is blocked. | Go through the CDN. On Cloudflare, the proxy must be on (**Proxied**, orange cloud). It must not resolve to your server's IP. |
| **Relay** | Users connect to another server in between, which passes traffic on to your server. [More about relays](/manager/domain-worker-cdn-and-tunneling/How-to-add-relay-domain-to-Hiddify-manager/) | Point to the in-between (relay) server, not to your server. |
| **Cloudflare Worker** | Traffic reaches your server through a Cloudflare Worker. [More about workers](/manager/domain-worker-cdn-and-tunneling/How-to-use-the-Cloudflare-worker-domain-on-Hiddify/) | The domain must be on Cloudflare. |
| **Subscription only** | Only for users' subscription links, no proxies. If your proxy domains get blocked, users can still update their subscription and get new working configs. [More about subscription domains](/manager/domain-worker-cdn-and-tunneling/How-to-create-subscription-link-on-Hiddify/) | Point to your server or go through a CDN. Behind a CDN is best. |

The **TLS mode** decides which certificate the domain uses:

| TLS mode | Meaning |
|---|---|
| **Valid TLS** | A real certificate that the panel gets and renews for you automatically. Use this in almost all cases. CDN, Cloudflare Worker and Subscription only domains always use it. |
| **Fake** | Decoy TLS with another site's name (for example `soft98.ir`) to pass an SNI whitelist. Not recommended, because it can get your server filtered. Only for Direct or Relay. [More about fake domains](/manager/domain-worker-cdn-and-tunneling/How-to-create-and-use-fake-domain/) |
| **Reality** | Borrows another real site's TLS with the Reality protocol. You do not need to own the domain. Only for Direct or Relay. |
| **DNS** | For DNS tunnels only. |

The panel checks the DNS record when you save. For example, a Direct domain must point to your server's IP, and a CDN domain must **not** point to it directly. If the check fails, fix the DNS record, wait a few minutes, and save again.

!!! tip "Let the panel create the DNS records"
    If your domain is on Cloudflare, you can give the panel a Cloudflare API token. The panel then creates the DNS record for each new domain (proxy on for CDN, off for Direct). See [Get Cloudflare API](/manager/domain-worker-cdn-and-tunneling/Get-Cloudflare-API/).

# How to register a domain

<details markdown="1"><summary><h2>Direct domain registration</h2></summary>

You can get a free subdomain or use a domain you bought.

### Free subdomain (FreeDNS)

[FreeDNS (afraid.org)](https://freedns.afraid.org/) lets you create a subdomain on domains that other people have shared publicly.

1. [Create an account](https://freedns.afraid.org/signup/?plan=starter). You need a real email address.

    ![FreeDNS sign-up page](https://user-images.githubusercontent.com/125398461/221342760-12dc14ed-9a19-45f3-a3f1-bf7d3f969792.png)

2. Open the [domain registry](https://freedns.afraid.org/domain/registry/). Pick a **public** domain that has few hosts. Domains ending in `.com`, `.org` or `.net` are best.

    ![FreeDNS domain registry](https://user-images.githubusercontent.com/125398461/234033584-1c26c485-6ceb-4aa9-a6b6-c1b781e767d1.png)

3. Create your subdomain on that domain and set its address to your server's IP.

### A domain you bought, on Cloudflare

You can manage a domain you bought with any DNS provider. These steps use Cloudflare.

1. [Create a Cloudflare account](https://dash.cloudflare.com/signup) and log in.

    ![Cloudflare sign-up page](https://user-images.githubusercontent.com/125398461/221563866-d520a39d-15c8-4f88-a756-90e5e08c074a.png)

2. Go to **Domains** and select **Onboard a domain**. Enter your main domain (for example `example.com`) and select **Continue**. Older screenshots show this button as **Add Site**.

    ![Adding a domain to Cloudflare](https://user-images.githubusercontent.com/125398461/221566504-5ecf714b-940d-4fd5-bc54-be8c37b7c292.png)

3. Choose a plan. The **Free** plan is enough.

    ![Choosing the free plan](https://user-images.githubusercontent.com/125398461/221567803-26850724-1bc8-480a-8c6f-29b32a6fcfa6.png)

4. Review the DNS records Cloudflare found and select **Continue**.

    ![Reviewing DNS records](https://user-images.githubusercontent.com/125398461/222444475-5596de54-3e7f-4fae-a0f0-94c046a21969.png)

5. Cloudflare shows you two **nameservers**. Go to the site where you bought the domain and replace its nameservers with these two.

    ![Cloudflare nameservers](https://user-images.githubusercontent.com/125398461/221569269-1f4027c7-5815-4dea-876e-326dc0645fe1.png)

6. Wait until Cloudflare shows the domain as active. This can take from a few minutes to a day.

    ![Domain active on Cloudflare](https://user-images.githubusercontent.com/125398461/221572305-50e819ea-0fa4-4548-8851-aab91b797f57.png)

7. Open your domain and go to **DNS** > **Records**.

    ![DNS records page](https://user-images.githubusercontent.com/125398461/222436778-f80de97b-7d66-4621-8be3-b856fc4e2c75.png)

8. Select **Add record**.

    ![Add record](https://user-images.githubusercontent.com/125398461/222444012-2fa4a2c2-ff89-493e-b92c-01a26d7788b7.png)

9. Fill in the record:
    - **Type**: `A` (for the server's IPv4 address).
    - **Name**: the subdomain you want, for example `sub`.
    - **IPv4 address**: your server's IP.
    - **Proxy status**: turn it **off** (**DNS only**, grey cloud). A Direct domain must not be proxied.
    - **TTL**: leave it on Auto. A lower TTL makes changes reach users sooner.

10. Select **Save**.

    ![A record with proxy off](https://user-images.githubusercontent.com/125398461/234167251-ceebd61b-5147-4198-98dc-1c5bcd0d9124.png)

11. If your server also has an IPv6 address, add a second record the same way, with **Type** `AAAA` and the IPv6 address.

    ![AAAA record](https://user-images.githubusercontent.com/125398461/234167507-996c8480-5cf5-4ede-999f-05f74b22499f.png)

### Check that the direct domain works

DNS changes can take a few minutes to spread. Then, on your own computer, run:

```bash
ping sub.example.com
```

You should see your server's IP in the answer. You can also use `nslookup` or `dig`. If you see a different IP or "unknown host", check the record and wait a little longer. To learn more, read [this article on DNS](https://wikicensorship.github.io/fa/docs/measure-internet-censorship/DNS/) (Persian).

</details>

<details markdown="1"><summary><h2>CDN domain registration</h2></summary>

A **CDN** (content delivery network) is a network of servers that sits between your users and your server. Users connect to the CDN, and the CDN passes the traffic to your server. [What is CDN and how does it help us?](/manager/domain-worker-cdn-and-tunneling/What-is-CDN-and-how-does-it-help-us%3F/)

These steps use Cloudflare. For other CDNs, see [GCore](/manager/domain-worker-cdn-and-tunneling/How-to-use-GCore-CDN-on-Cloudflare-registered-domain/) and [Amazon CloudFront](/manager/domain-worker-cdn-and-tunneling/How-to-use-Amazon-CDN/).

### Add the CDN record on Cloudflare

1. Add your domain to Cloudflare as described in the direct domain section above (steps 1 to 6).
2. Go to **DNS** > **Records** and select **Add record**.
3. Use **Type** `A` (or `AAAA` for IPv6), a new subdomain name, and your server's IP.
4. Turn **Proxy status** **on** (**Proxied**, orange cloud). This is the only difference from a direct domain.
5. Select **Save**.

![A record with proxy on](https://user-images.githubusercontent.com/125398461/234167748-7121af19-f624-4659-9922-50f8e6d3ea2c.png)

### Check that the CDN domain works

When you `ping` this subdomain, you should see one of Cloudflare's IPs, not your server's IP. This hides your server. The Cloudflare IP can change over time.

Sometimes the Cloudflare IPs that your users get are blocked or slow in Iran. In that case, see [Guide for finding a clean Cloudflare IP](/manager/domain-worker-cdn-and-tunneling/Guide-for-finding-a-clean-Cloudflare-IP/).

### Cloudflare SSL/TLS settings

**TLS** is the encryption that protects the connection between the user and the server. A **certificate** proves that a server really owns a domain. HiddifyManager gets a real certificate for your domain, so Cloudflare can connect to your server over TLS.

1. Open your domain in Cloudflare and go to **SSL/TLS** > **Overview**.
2. Choose the encryption mode **Full** or **Full (strict)**. Do not use **Flexible**. If the mode is set to **Automatic SSL/TLS**, Cloudflare picks the most secure mode that works; you can leave it.

    ![SSL/TLS encryption mode](https://user-images.githubusercontent.com/125398461/234168806-26bb12cf-78ad-45a9-89b5-c2f005a9fb86.png)

3. Go to **Network** and turn on **WebSockets** and **gRPC**. HiddifyManager's CDN proxies use WebSocket, gRPC, HTTPUpgrade and XHTTP.

    ![Network settings](https://user-images.githubusercontent.com/125398461/223041843-7b441805-4aab-4547-b318-7dbbda4cc893.png)

    ![WebSockets and gRPC toggles](https://user-images.githubusercontent.com/125398461/223042286-e597f169-001e-40a5-b0e8-d34d1b110eab.png)

Older guides told you to turn on **SSL/TLS Recommender**. Cloudflare is replacing it with Automatic SSL/TLS, so you do not need it.

The SSL/TLS section of Cloudflare also shows a chart of your traffic by TLS version. More traffic on newer TLS versions means safer connections.

![Traffic by TLS version](https://user-images.githubusercontent.com/125398461/223042939-897b7ec0-9700-4bec-8e28-6d8f961657b6.png)

</details>

## Relay domain registration

A relay domain is registered like a direct domain, but its record points to the in-between (relay) server instead of your main server. [Read more](/manager/domain-worker-cdn-and-tunneling/How-to-add-relay-domain-to-Hiddify-manager/)

## Fake and Reality domains

With the **Fake** or **Reality** TLS mode, you use the name of another site that you do not own, so you do not register anything at a DNS provider. You only add the name in the panel. See [How to create and use fake domain](/manager/domain-worker-cdn-and-tunneling/How-to-create-and-use-fake-domain/).

</div>
