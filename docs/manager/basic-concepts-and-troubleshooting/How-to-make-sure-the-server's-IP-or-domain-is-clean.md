---
title: How to make sure the server's IP or domain is clean
---

<div dir="ltr" markdown="1">

# How to make sure the server's IP or domain is clean

This page helps you check whether your server's IP address or domain is reachable from your country, or whether it has been blocked. Do this check before you install Hiddify Manager on a new server, and again whenever your users suddenly cannot connect.

An IP address or domain is **clean** when the filtering system in your country does not block it. It is **blocked** (or "dirty") when it does.

## Symptoms

- No config connects, from any device, even though the panel shows the server is running.
- The server works with one internet provider (ISP) but not with another.
- The server worked for a while after installation, and then stopped working or became very slow.

## Likely causes

- The server's IP address or domain is blocked.
- The IP address is on the "yellow list" (see [The yellow list](#the-yellow-list) below): it works on some ISPs but not on others, or it slows down once traffic grows.

## What to check

You test your server from computers in other places, using free websites. Use both websites below if you can. In our experience, Host-Tracker's results are more reliable than Check-Host's.

### 1. Check-Host

1. Open [Check-Host](https://check-host.net/).
2. Type your server's IP address or domain in the box.

    ![Check-Host home page](https://user-images.githubusercontent.com/125398461/229691501-94fd331f-82ed-4b29-9a84-187fe3b89ee5.png)

3. Choose the type of test. Each test is explained below.

#### Ping test

Use this test on a new server that has nothing installed on it yet. A **ping** sends a tiny message to the server and waits for a reply.

![Check-Host ping test result](https://user-images.githubusercontent.com/125398461/222420082-2a380c2f-803e-4426-a529-8c09b997c76a.png)

- **Result `4/4` from the locations in your country:** the IP is most likely clean.
- **Anything else:** the IP is probably blocked. Ask your hosting provider for a new IP.

#### TCP test

Use this test when a service is already running on the server, for example after you installed Hiddify Manager. It checks whether a **port** (a numbered "door" that a service listens on) is reachable. Hiddify uses TCP port `443`, so test with `your-ip:443`.

![Check-Host TCP test result](https://user-images.githubusercontent.com/125398461/222426843-82605bb3-d51e-407a-8d92-90bddef896ba.png)

- **The result looks like the picture above (connected, with a time in ms):** the IP is probably fine.
- **Timeouts or errors from your country:** the IP is probably blocked. Ask for a new IP.

#### UDP test

Use this test to check a service that uses **UDP** (another way of sending data, used for example by DNS on port `53`).

![Check-Host UDP test result](https://user-images.githubusercontent.com/125398461/222426567-20464d00-cb53-4d8d-87f3-6ab28a45bce3.png)

If the result looks like the picture above, UDP connections do not get through, and the IP may not be clean.

### 2. Host-Tracker

1. Open [Host-Tracker](https://www.host-tracker.com/en/ic).

    ![Host-Tracker home page](https://user-images.githubusercontent.com/125398461/222429170-dbe08724-771e-4910-bbd4-19e3b5bc78f8.png)

2. Type your server's IP address or domain.
3. Choose the locations in your country (for example, Iran). Results from other countries do not tell you whether your users can reach the server.
4. Run a Ping test or a TCP test. They work the same way as on Check-Host.

#### Ping test

![Host-Tracker ping test result](https://user-images.githubusercontent.com/125398461/229689843-3d68ac6b-2eeb-4154-a445-23a5f4b24b49.png)

If all locations show `Good`, the IP is very likely clean.

#### TCP test

![Host-Tracker TCP test result](https://user-images.githubusercontent.com/125398461/229689470-005f8fdc-86d6-4ee8-8283-d2c2c5c766f3.png)

If the result is `OK`, the IP is very likely clean.

!!! note "The firewall and ping tests"
    Hiddify's firewall setting (**Settings** → **General Settings** → **🛡️ Firewall**) is off by default. Even when you turn it on, Hiddify still lets ping through, so ping tests keep working. If ping fails but the TCP test on port `443` works, someone may have blocked ping by hand on the server. Use the TCP test in that case. See [How to set up the firewall](/manager/basic-concepts-and-troubleshooting/How-to-setup-Firewall-on-Hiddify-panel/).

## How to fix it

- **The IP is blocked:** ask your hosting provider for a new IP, or create a new server, and test again before you install anything.
- **The domain is blocked:** register a new domain. See [Domain types and how to register them](/manager/domain-worker-cdn-and-tunneling/Domain-types-and-how-to-register-them/).
- **The IP is blocked but you want to keep the server:** put a CDN in front of it. See [What is CDN and how does it help us?](/manager/domain-worker-cdn-and-tunneling/What-is-CDN-and-how-does-it-help-us%3F/).
- For more options, see [Troubleshooting connectivity issues](/manager/basic-concepts-and-troubleshooting/Troubleshooting-connectivity-issues-with-HiddifyManager-and-proxies/).

## The yellow list

Why can an IP pass every test when you buy the server, and then stop working some time after you install the panel? The answer is the **yellow list**.

<div align=center markdown=1>

<img width=40% src="https://github.com/hiddify/hiddify-config/assets/125398461/242a64b6-8075-4892-bb0f-de13b158a33a" alt="Red, yellow and green lists of IP addresses" />
</div>

- When the filtering system detects an IP that is used for a proxy, it puts the IP on the **red list** and blocks it.
- After the IP has had no traffic for a while, it moves to the **yellow list** and looks clean again.
- As soon as the IP gets heavy traffic again, it is blocked or slowed down again.

So an IP that "tests clean" may still be on the yellow list. If a new server stops working soon after you start using it, ask for a new IP.

</div>
