---
title: Tutorial for Fair VPN app
---

<div dir="ltr" markdown="1">

# Tutorial for Fair VPN app

This page shows you how to add your HiddifyManager subscription to the free **Fair VPN** app on iPhone and iPad, test the connections, and share your VPN with other devices.

<div class="hi-get"><img class="ico" src="/assets/logos/apps/fairvpn.webp" alt="Fair VPN"><div class="meta"><b>Fair VPN</b><small><span>v1.3.4</span><span>iOS 12+</span><span>Free</span><span>Nov 2026</span></small></div><div class="stores"><a class="hi-store" href="https://apps.apple.com/us/app/fair-vpn/id1533873488"><img src="/assets/logos/apple-white.svg" alt=""><span><small>Download on the</small><b>App Store</b></span></a></div></div>
<a class="hi-alt" href="/app/How-to-install-Hiddify-app/"><span class="mk"><img src="/assets/logos/hiddify-mark-white.svg" alt=""></span><span><b>Our suggestion: the Hiddify app</b><small>Free, simpler, and supports every Hiddify Manager protocol</small></span><span class="go">Install →</span></a>

## Before you start

- Install **Fair VPN** from the [App Store](https://apps.apple.com/us/app/fair-vpn/id1533873488). It is free.
- Have your **user page link** ready. This is the link your server admin sent you. It opens your personal HiddifyManager page.

A **subscription link** is one link that holds all your connection settings (configs). A **config** is the settings for one connection to the server.

## Get your subscription link

On the user page, tap the big round button. At the bottom of the window, under **Import Manually**, **Copy Link** copies your subscription link. This app is not in the user page’s app list, so use this button.

<img width=300 alt="Fair VPN on the user page" src="/assets/manager/Tutorial-for-Fair-VPN-app/en-user-app.webp" style="display:block;margin:0 auto">


Fair VPN is not in the app list on the HiddifyManager user page, so you add the link by hand.

1. Open your user page link.
2. Open the menu and tap **All Configs**.
3. In the **Subscription Links** section, find **Subscription link b64** and tap **Get Link**. A small window opens with a QR code and a **Copy Link** button.

<div align=center markdown=1>
<img width=300 alt="All Configs on the user page" src="/assets/manager/Tutorial-for-Fair-VPN-app/en-user-configs.webp" style="display:block;margin:0 auto">
</div>

!!! note
    The screenshots of the user page come from an older panel version. The current page looks different, but the link is the same.

Now you can either copy the link or scan its QR code.

## Option 1: Copy the link

1. Tap **Copy Link**.

    <img style="display:block;margin:0 auto" width=30% alt="Copy button" src="/assets/manager/Tutorial-for-Fair-VPN-app/gh-a31600a9-58ef-4156-ad24-b095142162ba.webp" />

2. Open Fair VPN. In the **VPN** tab, tap **Import VPN Configs**.

    <img style="display:block;margin:0 auto" width=30% alt="Import VPN Configs" src="/assets/manager/Tutorial-for-Fair-VPN-app/gh-3631c51e-15d7-44a6-bda0-c8df0b61c9d0.webp" />

3. Paste the link and tap **OK**.

    <img style="display:block;margin:0 auto" width=30% alt="Paste the link and tap OK" src="/assets/manager/Tutorial-for-Fair-VPN-app/gh-16c4e038-ab2f-4f01-86d6-8ed147180c93.webp" />

After a few seconds, your configs appear in the app.

## Option 2: Scan the QR code

Use this if the user page is open on another screen, such as a computer.

1. In Fair VPN, open the **VPN** tab and tap **Add VPN by QR Code** in the bottom menu.

    <img style="display:block;margin:0 auto" width=30% alt="Add VPN by QR Code" src="/assets/manager/Tutorial-for-Fair-VPN-app/gh-1107964d-22ff-4fd8-854c-32c09be13b1e.webp" />

2. Point your phone's camera at the QR code on the user page. The configs are added, just as with option 1.

    <img style="display:block;margin:0 auto" width=30% alt="Scanning the QR code" src="/assets/manager/Tutorial-for-Fair-VPN-app/gh-3e468c42-e0a6-41c6-9869-2e7f88ff2d3c.webp" />

## Test the connections

1. Tap **Test VPN Latency**.
2. Tap **Test Web Latency**.

The app makes a real test through each config and shows the result next to it. **Latency** is how long a reply takes; lower is better.

<div align=center markdown=1>
<img width=30% alt="Test results next to each config" src="/assets/manager/Tutorial-for-Fair-VPN-app/gh-322b3680-e908-4a9d-8423-47ef3c50c1ff.webp" />
</div>

## Sort configs by test result

1. Tap **Test VPN Latency**.
2. Tap **Sort by Latency**.

The configs are now sorted by their test result, best first.

<div align=center markdown=1>
<img width=30% alt="Sort by Latency" src="/assets/manager/Tutorial-for-Fair-VPN-app/gh-04ef4c98-8dde-4da0-b0dd-2250ec32b8c7.webp" />
</div>

## Update your subscription

Fair VPN cannot refresh a subscription by itself. To get the latest configs:

1. Tap **Delete All VPN** to remove all configs.
2. Add the subscription link again, as shown above.

!!! note "If your admin uses Auto CDN"
    To get a new clean IP, delete all configs with **Delete All VPN**. Then turn the VPN off, reload your user page, and add the subscription link again.

<div align=center markdown=1>
<img width=30% alt="Delete All VPN" src="/assets/manager/Tutorial-for-Fair-VPN-app/gh-6aef8018-ee10-414f-b889-f1dde61bdbe9.webp" />
</div>

## Share your VPN with other devices

You can share your phone's VPN with another device on the same Wi-Fi network, for example a device that can't install a VPN app.

1. In Fair VPN, turn on **Local Sharing**. The app shows an IP address and a port.

    <img style="display:block;margin:0 auto" width=30% alt="Local Sharing message with IP and port" src="/assets/manager/Tutorial-for-Fair-VPN-app/gh-781db733-df3f-4190-baaa-5dd4dc529727.webp" />

2. On the other device, open its network **proxy settings**.
3. Enter the IP address and port shown by Fair VPN, and save.

The other device now uses your phone's VPN connection.

## Related articles

<div class="hi-related" markdown="1">

- [sing-box](/manager/client-software-on-ios/Tutorial-for-SingBox-app/)
- [Streisand](/manager/client-software-on-ios/Tutorial-for-Streisand/)
- [V2Box](/manager/client-software-on-ios/Tutorial-for-V2Box-app/)
- [FoXray](/manager/client-software-on-ios/Tutorial-for-FoXray-app/)

</div>

</div>
