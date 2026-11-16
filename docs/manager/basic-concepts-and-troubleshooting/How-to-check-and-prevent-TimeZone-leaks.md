---
title: How to check and prevent time zone leaks
---

# Time zone leak

This page shows you how to check whether your browser reveals your real time zone while you use a VPN, and how to stop it. You only need a browser on your computer.

## What is a time zone leak?

Websites can read your device's **time zone** (for example `Asia/Tehran`) with a few lines of JavaScript. A **time zone leak** happens when this time zone does not match the country of your VPN server. For example, if your VPN server is in Germany but your browser reports Iran's time zone, a website can guess that you are using a VPN and where you really are.

## How to test for a time zone leak

### Method 1: a test website

1. Connect to your VPN.
2. Open [webbrowsertools.com/timezone](https://webbrowsertools.com/timezone/). The site checks your time zone in six different ways. The last one ("aggressive") is the hardest to fool.
3. Compare the time zone the site finds with your VPN server's country. If the site shows your real time zone, you have a leak.

In the picture below, no extension is used, and simple JavaScript on the site detects the Iran time zone. If your VPN server is in another country, this gives you away.

![webbrowsertools.com detecting the Iran time zone](/assets/manager/How-to-check-and-prevent-TimeZone-leaks/gh-d9eee13e-b903-4977-ba05-e8707671f2dd.webp)

### Method 2: the browser console

1. Press `F12` (or right-click the page and choose **Inspect**), then open the **Console** tab.
2. Paste this line and press Enter:

    ```js
    console.log(Intl.DateTimeFormat().resolvedOptions().timeZone);
    ```

3. The console prints your browser's time zone.

![The browser console showing the browser time zone](/assets/manager/How-to-check-and-prevent-TimeZone-leaks/gh-61a3c169-32f0-47e9-b468-c37e1e1d4a4a.webp)

## How to prevent time zone leaks

There are two recommended methods. After each one, run the test again.

### 1. Use the NoScript extension

**NoScript** blocks websites from running JavaScript, so they cannot read your time zone. Install it for [Chrome](https://chromewebstore.google.com/detail/noscript/doojmbjmlfjjnbmnoijecmcbfeoakpjm) or [Firefox](https://addons.mozilla.org/addon/noscript/).

![The NoScript extension blocking the time zone test](/assets/manager/How-to-check-and-prevent-TimeZone-leaks/gh-2238af19-619d-42ad-a7dc-b6bb7a07e0dd.webp)

Keep in mind that many sites need JavaScript, so some features may stop working while NoScript is on.

### 2. Use the Spoof Timezone extension

**Spoof Timezone** makes your browser report a different time zone. Install it for [Chrome](https://chromewebstore.google.com/detail/spoof-timezone/kcabmhnajflfolhelachlflngdbfhboe?hl=en) or [Firefox](https://addons.mozilla.org/en-US/firefox/addon/spoof-timezone/). It has two modes:

- **Mode 1: Greenwich Mean Time (GMT).** If you don't change any settings, the extension reports GMT.
- **Mode 2: match your VPN's IP address.** To turn this on:
    1. Right-click the extension icon and choose **Options**.
    2. Tick **Automatically update timezone based on my IP address**.
    3. Right-click the extension icon again and choose **Update Timezone from IP**.
    4. Each time you switch to a VPN server in a different country, repeat step 3.

![Spoof Timezone options](/assets/manager/How-to-check-and-prevent-TimeZone-leaks/gh-dce0eaef-40a3-4079-92f4-4067ea2bbce9.webp)

!!! warning "Spoof Timezone does not stop every test"
    The sixth ("aggressive") method on the test site is very strict. As the picture below shows, it can still find your real time zone even with Spoof Timezone. NoScript blocks this method completely.

![The aggressive method still detecting the real time zone with Spoof Timezone on](/assets/manager/How-to-check-and-prevent-TimeZone-leaks/gh-f168398e-5073-4ec3-9994-a83bf53b7cb7.webp)

## Related articles

- [Connection problems](/manager/basic-concepts-and-troubleshooting/Troubleshooting-connectivity-issues-with-HiddifyManager-and-proxies/)
- [Is the server's IP or domain clean?](/manager/basic-concepts-and-troubleshooting/How-to-make-sure-the-server's-IP-or-domain-is-clean/)
- [DNS leaks](/manager/basic-concepts-and-troubleshooting/How-to-check-and-prevent-DNS-leaks/)
- [Server speed test](/manager/basic-concepts-and-troubleshooting/How-to-do-speed-test-on-server/)
