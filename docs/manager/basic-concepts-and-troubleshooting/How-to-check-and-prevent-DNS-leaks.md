---
title: How to check and prevent DNS leaks
---

# How to check and prevent DNS leaks

This page helps you check whether your VPN or proxy is leaking information that can reveal who you are, and how to fix it. It covers two common leaks: **DNS leaks** and **WebRTC leaks**. You can do every test from your phone or computer; no server access is needed for the tests.

## What is a DNS leak?

**DNS** (Domain Name System) is the "phone book" of the Internet: it turns a name such as `google.com` into the IP address of the server behind it. Every time you open a site, your device first sends a DNS request.

- Without a VPN, these requests go to your Internet provider (ISP).
- With a VPN or proxy, these requests should go through the VPN to the VPN's DNS server.

A **DNS leak** happens when DNS requests skip the VPN and still go to your ISP. Your ISP (and anyone watching your connection) can then see which sites you visit, even though the rest of your traffic is hidden.

**Symptom:** a DNS leak test (below) shows DNS servers from your own country or your own ISP while you are connected to the VPN.

## How to test for a DNS leak

Connect to your VPN or proxy first, then open one or more of the sites below. Use more than one site, because each site tests a little differently.

### 1. dnsleaktest.com

1. Open [dnsleaktest.com](https://dnsleaktest.com/). The first page shows your current IP address.
2. Tap **Extended test**. (The **Standard test** checks fewer servers; the extended test is more thorough.)

    ![The dnsleaktest.com home page with the Standard test and Extended test buttons](https://user-images.githubusercontent.com/125398461/235299493-2a0c4aaf-cd24-4723-b7f6-8ed60845734d.jpg)

3. Wait for the test to finish and look at the list of servers:
    - **No leak:** every server belongs to your VPN server's provider or is in your VPN server's country. All your DNS traffic went through the VPN.
    - **Leak:** one or more servers belong to your own ISP or show your real country.

In the picture below, all servers match the VPN server's provider and location, so there is no leak.

![dnsleaktest.com results with no DNS leak](https://user-images.githubusercontent.com/125398461/235299505-d9fb313b-28b5-473a-b211-a1533bd0add5.jpg)

### 2. browserleaks.com

Open the [DNS Leak Test page on browserleaks.com](https://browserleaks.com/dns). The test starts by itself and shows the results when it finishes. Read the results the same way as above.

![browserleaks.com DNS test results with no leak](https://user-images.githubusercontent.com/125398461/235299510-6b7fb769-3c3a-49e9-b28f-ef59f52e72e6.jpg)

### 3. ipleak.net

Open [ipleak.net](https://ipleak.net). The test starts by itself. In the picture below, the DNS server matches the VPN server's provider and location, so there is no leak.

![ipleak.net results with no DNS leak](https://user-images.githubusercontent.com/125398461/235299557-8dac8205-37e8-4a67-bc2e-c6b0ad83b40d.jpg)

### 4. dnsleaktest.org

Open the [DNS Leak Test page on dnsleaktest.org](https://dnsleaktest.org/dns-leak-test). The test starts by itself.

![The dnsleaktest.org DNS leak test page](https://user-images.githubusercontent.com/125398461/235299689-1efae131-4ca9-4e49-9b15-6f915695c32c.jpg)

In the picture below, the list contains servers that do **not** belong to the VPN server and show the user's real location. This means there **is** a DNS leak.

![dnsleaktest.org results showing a DNS leak](https://user-images.githubusercontent.com/125398461/235299716-b3d0d789-84be-499c-b03a-b1cd5d2e1c58.jpg)

## How to fix a DNS leak

**Likely causes:** the client app sends DNS requests outside the tunnel, the device's own DNS settings override the VPN, or IPv6 traffic goes around the VPN.

Try these fixes in order, and run a leak test again after each one.

### 1. Check the DNS settings in your client app

In the **Hiddify app** (v4):

1. Open **Settings** and go to the **DNS** section.
2. Make sure **Remote DNS** is set to a trusted public DNS server, for example Cloudflare (`1.1.1.1`) or Google (`8.8.8.8`). Remote DNS is the DNS server used for requests that go through the proxy.
3. Reconnect and run a leak test again.

In other apps, look for a similar DNS setting and set it to a trusted public DNS server.

### 2. Disable IPv6 if you don't use it

**IPv6** is the newer kind of IP address. If your VPN only carries IPv4 traffic, IPv6 requests can go around it. If you don't need IPv6, turn it off in your device's network settings. In the Hiddify app, you can also change the **IPv6 route** option in **Settings > Routing**.

On the server side, see [How to disable IP version 6 on HiddifyManager](/manager/basic-concepts-and-troubleshooting/How-to-disable-IP-version-6-on-Hiddify/).

### 3. Set a trusted DNS server on your Hiddify server

Your server also needs a working, trusted DNS server. In HiddifyManager you can set it in the panel. See [How to set DNS server on HiddifyManager](/manager/basic-concepts-and-troubleshooting/How-to-set-DNS-server/) for the steps and for how to test DNS on the server.

### 4. Use an encrypted DNS app

On a computer, you can use tools such as **DNSCrypt** or **Simple DNS Crypt**. They send your DNS requests to secure servers over an encrypted connection, so your ISP cannot read them.

## What is WebRTC?

**WebRTC** (Web Real-Time Communication) is a browser feature for live voice, video and data, for example video calls in a web page. It works without plugins and is built into most browsers.

## What is a WebRTC leak?

To set up calls, WebRTC can ask your device for its IP addresses. In some cases a website can use this to find your **real IP address**, even when you use a VPN. This is a weakness in browsers such as Chrome, Firefox and Edge.

**Symptom:** a WebRTC test (below) shows your real IP address while you are connected to the VPN.

## How to test for a WebRTC leak

1. Connect to your VPN or proxy.
2. Open the [WebRTC Leak Test page on browserleaks.com](https://browserleaks.com/webrtc). The test runs by itself.
3. Compare the IP addresses on the page with your real IP. If your real IP appears, you have a leak.

In the picture below, the real IP address is visible even though a VPN is in use, so there is a leak.

![browserleaks.com WebRTC test showing a leak of the real IP address](https://user-images.githubusercontent.com/125398461/235300245-57e4be56-22fb-4030-989b-a5a49f77d533.jpg)

## How to fix a WebRTC leak

Fix it in each browser you use, then run the test again.

### Firefox

1. Type `about:config` in the address bar and press Enter.
2. Tap **Accept the Risk and Continue**.
3. In the search box, type `media.peerconnection.enabled`.
4. Double-click the setting so its value changes from `true` to `false`.

### Chrome and Edge

1. Install the [WebRTC Leak Prevent](https://chrome.google.com/webstore/detail/webrtc-leak-prevent/eiadekoaikejlgdbkbdfeijglgfdalml?hl=en) extension.
2. Open the extension's options.
3. Set **IP handling policy** to **Disable non-proxied UDP**.

### Safari

1. Open **Preferences** and go to the **Advanced** tab.
2. Turn on **Show Develop menu in menu bar**.
3. In the menu bar, open **Develop** and choose **Experimental Features**.
4. Find **Remove Legacy WebRTC API** and click it to turn WebRTC off.

Menu names can differ between Safari versions.
