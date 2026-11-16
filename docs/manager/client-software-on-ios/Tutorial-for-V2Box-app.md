---
title: Tutorial for V2Box app
---

<div dir="ltr" markdown="1">

# Tutorial for V2Box app

This page shows you how to add your HiddifyManager subscription to the free **V2Box** app on iPhone and iPad, test the connections, connect, and keep your configs up to date. V2Box works with Xray-based configs.

<div class="hi-get"><img class="ico" src="/assets/logos/apps/v2box.webp" alt="V2Box"><div class="meta"><b>V2Box</b><small><span>v10.2.0</span><span>iOS 15+</span><span>Free</span><span>Nov 2026</span></small></div><div class="stores"><a class="hi-store" href="https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690"><img src="/assets/logos/apple-white.svg" alt=""><span><small>Download on the</small><b>App Store</b></span></a></div></div>
<a class="hi-alt" href="/app/How-to-install-Hiddify-app/"><span class="mk"><img src="/assets/logos/hiddify-mark-white.svg" alt=""></span><span><b>Our suggestion: the Hiddify app</b><small>Free, simpler, and supports every Hiddify Manager protocol</small></span><span class="go">Install →</span></a>

## Before you start

- Install **V2Box** from the [App Store](https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690). It is free.
- Have your **user page link** ready. This is the link your server admin sent you. It opens your personal HiddifyManager page.

A **subscription link** is one link that holds all your connection settings (configs). A **config** is the settings for one connection to the server.

!!! note
    The user page pictures are current (Hiddify Manager v14.5). The app screenshots come from older versions of the app; the current screens look a little different, but the steps are the same. The current screens look different, but the steps are the same.

## Get your subscription link

On the user page, tap the big round button. At the bottom of the window, under **Import Manually**, **Copy Link** copies your subscription link. This app is not in the user page’s app list, so use this button.

<img width=300 alt="V2Box on the user page" src="/assets/manager/Tutorial-for-V2Box-app/en-user-app.webp" style="display:block;margin:0 auto">


V2Box is not in the app list on the HiddifyManager user page, so you add the link by hand.

1. Open your user page link.
2. Open the menu and tap **All Configs**.
3. In the **Subscription Links** section, find **Subscription link b64** and tap **Get Link**. A small window opens with a QR code and a **Copy Link** button.

Now you can either copy the link or scan its QR code.

## Option 1: Copy the link

1. Tap **Copy Link**.

    <img width=300 alt="All Configs on the user page" src="/assets/manager/Tutorial-for-V2Box-app/en-user-configs.webp" style="display:block;margin:0 auto">

2. Open V2Box and tap **Configs** in the bottom menu.
3. Tap the **+** button.

    <img style="display:block;margin:0 auto" width=30% alt="The + button in Configs" src="/assets/manager/Tutorial-for-V2Box-app/gh-c84fd272-2719-4fd2-8397-9a2a0e2013be.webp" />

4. Tap **Add Subscription**.
5. Type any name, for example the name of your server, and paste the link into the **URL** field.

    <img style="display:block;margin:0 auto" width=30% alt="Name and URL of the subscription" src="/assets/manager/Tutorial-for-V2Box-app/gh-2629b6ad-cfcf-4252-846e-9e336493a259.webp" />

6. Tap **Add Subscribe**. Your configs appear in the list, and V2Box tests them by itself.

    <img style="display:block;margin:0 auto" width=30% alt="Configs added to V2Box" src="/assets/manager/Tutorial-for-V2Box-app/gh-f69d8992-7195-4755-b415-330572d5044e.webp" />

## Option 2: Scan the QR code

Use this if the user page is open on another screen, such as a computer.

1. In V2Box, open **Configs** and tap **+**.
2. Tap **Scan QR**.
3. Point your phone's camera at the QR code on the user page. The configs are added and tested, just as with option 1.

<div align=center markdown=1>
<img width=30% alt="Scan QR in V2Box" src="/assets/manager/Tutorial-for-V2Box-app/gh-4b1dff0e-8d27-45bd-9d0f-fef98f57aeac.webp" />
</div>

## Test the connections

In the **Configs** list, tap **Ping All**. The result appears next to each config. Lower numbers are better; a config with an error or a timeout does not work right now.

<div align=center markdown=1>
<img width=30% alt="Ping All in the Configs list" src="/assets/manager/Tutorial-for-V2Box-app/gh-fcf64420-5c53-4b21-816e-1618ff61f226.webp" />
</div>

## Connect

1. In **Configs**, tap a config that tested well to select it.
2. Go to **Home** and slide the button at the bottom to the right. The first time, iOS asks you to allow a VPN configuration; tap **Allow**.

<div align=center markdown=1>
<img width=30% alt="The connect slider on the Home screen" src="/assets/manager/Tutorial-for-V2Box-app/gh-fdbebfae-02f6-4993-99ff-e0cbf37734ef.webp" />
</div>

While you are connected, the Home screen shows your upload, download and memory use.

<div align=center markdown=1>
<img width=30% alt="Connection details on the Home screen" src="/assets/manager/Tutorial-for-V2Box-app/gh-68542ff9-2caa-45a7-9b8a-2ec50a4d32fa.webp" />
</div>

## Update your subscription

When the admin changes something on the server, update the subscription to get the new configs:

1. In **Configs**, tap **+**.
2. Tap **Update All Subscriptions**.

<div align=center markdown=1>
<img width=30% alt="Update All Subscriptions" src="/assets/manager/Tutorial-for-V2Box-app/gh-1db528f9-606f-469d-9ff6-1b4299f057b2.webp" />
</div>

To let V2Box update by itself, tap the menu (three lines) at the top of the **Configs** screen and turn on **Auto Update**.

<div align=center markdown=1>
<img width=30% alt="Auto Update in the Configs menu" src="/assets/manager/Tutorial-for-V2Box-app/gh-f01c924c-23b1-45dd-b937-c47c7dd52a49.webp" />
</div>

## Add a single config

You can also add one config instead of the whole subscription: copy the config link, then in **Configs** tap **+** and **Import V2ray URL from Clipboard**. This is not recommended, because a single config is not updated when the server changes.

<div align=center markdown=1>
<img width=30% alt="Import a config from the clipboard" src="/assets/manager/Tutorial-for-V2Box-app/gh-c579ef08-c5a5-4ec8-8f77-cef0d94824b1.webp" />
</div>

## If it doesn't connect

- Update the subscription and test again. Pick another config that shows a good result.
- Some configs, for example those using newer protocols, may not work in V2Box. Try the [Hiddify app](/app/How-to-install-Hiddify-app/).
- See [Troubleshooting connectivity issues](/manager/basic-concepts-and-troubleshooting/Troubleshooting-connectivity-issues-with-HiddifyManager-and-proxies/).

## Related articles

<div class="hi-related" markdown="1">

- [sing-box](/manager/client-software-on-ios/Tutorial-for-SingBox-app/)
- [Streisand](/manager/client-software-on-ios/Tutorial-for-Streisand/)
- [FoXray](/manager/client-software-on-ios/Tutorial-for-FoXray-app/)
- [Shadowrocket](/manager/client-software-on-ios/Tutorial-for-ShadowRocket-app/)

</div>

</div>
