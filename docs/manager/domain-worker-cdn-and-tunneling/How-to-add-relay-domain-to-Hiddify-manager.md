---
title: How to add a relay server (domain) to HiddifyManager
---


# How to add a relay server (domain) to HiddifyManager

This page shows you how to tell your Hiddify Manager panel about a relay server, so that your users get configs that go through it. Read it after you have set up the relay server itself.

## What is a relay server and why use one?

A **relay server** (also called an intermediate or bridge server) is a second, usually cheap, server that sits between your users and your main Hiddify server. Users connect to the relay; the relay passes their traffic on to the main server, and the main server sends it to the internet.

```
User  --->  Relay server (often in your own country)  --->  Main Hiddify server (abroad)  --->  Internet
```

You may want one when:

- the main server's IP is blocked or very slow from your users' country, but a server inside the country can still reach it;
- you want to hide the main server's IP from users;
- you want an address that is cheap to replace if it gets blocked (you only change the relay, not the main server).

The relay does not run Hiddify Manager. It only forwards traffic, using one of the tunnel methods below.

## Prerequisites

- A main server with Hiddify Manager installed. See the [installation guide](/manager/installation-and-setup/guide/).
- A relay server that already forwards ports `443` and `80` to the main server. Set it up with one of these methods:
    1. [Hiddify Relay Builder (all methods in one menu, easiest)](/manager/domain-worker-cdn-and-tunneling/How-to-setup-relay-server-using-Hiddify-Relay-Builder/)
    2. [IP-Tables method](/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-IP-Tables-tunnel-as-relay-server/)
    3. [GOST method](/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-GOST-tunnel-as-relay-server/)
    4. [WST method](/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-WST-tunnel-as-relay-server/)
    5. [Dokodemo-Door method](/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-Dokodemo-Door-tunnel-as-relay-server/)
    6. [HA-Proxy method](/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-HA-Proxy-tunnel-as-relay-server/)
- A domain you control (for example on Cloudflare).

!!! tip "Why forward port 80 too?"
    The panel gets free TLS certificates (Let's Encrypt) by answering a check on port `80`. For a relay domain, that check arrives at the relay server, so the relay must forward port `80` as well as `443` to the main server.

## Step 1: Point a subdomain at the relay server

1. Open your DNS provider (for example the Cloudflare dashboard).
2. Add an `A` record for a new subdomain, for example `relay.example.com`, with the **relay server's IP** as the value.
3. If you use Cloudflare, keep the proxy **off** (grey cloud, "DNS only").

## Step 2: Add the domain in the panel

1. Log in to your Hiddify Manager admin panel.
2. In the side menu, open **Domains** (in the **Settings** group).
3. Click **Add domain**.
4. Type your relay subdomain (for example `relay.example.com`). The panel checks its DNS. It should say the domain "points to another server" (your relay's IP). That is expected.
5. Choose the mode **Relay**.
6. For TLS, keep the default real certificate unless you know you need something else.
7. Enter a **Display name** if you like. Users see this name in their apps instead of the domain.
8. Click **Done**, then apply the changes when the panel asks you to.

If the certificate step fails, check that the relay forwards port `80` to the main server and that the DNS record has had a few minutes to spread.

!!! note "Fake or Reality TLS on a relay domain"
    If you pick a TLS mode other than a real certificate for a relay domain, the panel needs the relay server's IP. Enter it under **Advanced** → **Force configs to use these IPs / domains**, or the panel will not let you save.

## Step 3: Show the relay configs in your subscription link

It is good practice to keep the domain users open their subscription on separate from the domains that carry traffic. To add the relay configs to that subscription domain:

1. In **Domains**, click your subscription domain (for example `sublink.example.com`) to edit it.
2. In **Show configs of**, select your relay domain, and any other domains you want users to get.
3. Save, then apply the changes.

Now open a user's page using the subscription domain. You will see configs that use the relay domain. Users can add them one by one, or simply update their subscription in their app.

??? note "Screenshots from an older panel version"
    These screenshots come from the older admin pages. Labels and layout in current versions differ; follow the steps above.

    Adding a relay domain:

    <img src="https://github.com/hiddify/hiddify.com/assets/125398461/4c0ade4e-394c-4d52-8067-f15d1778c9ed" alt="Adding a relay domain in an older panel version">

    Showing the relay configs on the subscription domain:

    <img src="https://github.com/hiddify/hiddify.com/assets/125398461/3661045d-ced7-4694-916f-6ef160c63230" alt="Selecting the relay domain in the subscription domain settings, older panel version">

## Related pages

- [Domain types and how to register them](/manager/domain-worker-cdn-and-tunneling/Domain-types-and-how-to-register-them/)
- [Using IPv6 to make the relay connection more stable](/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-IPv6-to-improve-Relay-stability/)
