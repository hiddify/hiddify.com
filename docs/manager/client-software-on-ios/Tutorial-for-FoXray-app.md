---
title: Tutorial for FoXray app
---

<div dir="ltr" markdown="1">


# Tutorial for FoXray app

This page shows you how to add your Hiddify subscription to the **FoXray** app on iPhone and iPad and how to use its main settings. FoXray comes from the team behind the WingsX app, and replaced WingsX after WingsX was removed from the App Store.

!!! warning "FoXray is no longer on the App Store"
    As of October 2026, FoXray's App Store page (id6448898396) no longer exists, so you can't install it any more. If you already have it, the steps below still describe how it works. For a new install, use the **Hiddify App** ([App Store](https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532), see [How to install Hiddify App](/app/How-to-install-Hiddify-app/)) or another app from the [iOS client list](/manager/client-software-on-ios/).

## Before you start

- FoXray already installed on your iPhone or iPad.
- Your **user page link**. This is the link your server admin sent you. It opens your personal Hiddify page.

A **subscription link** is one link that holds all your connection settings (configs). FoXray can refresh it later to get new settings from the server.

## Add your subscription link

1. Open your user page link.
2. Open the menu and tap **All Configs**.
3. In the **Subscription Links** section, find **Subscription link b64** and tap **Get Link**.
4. Tap **Copy Link**.

    <div align=center markdown=1>
    <img width=30% alt="FoXray section on an older version of the user page" src="https://github.com/hiddify/hiddify-config/assets/125398461/69e8b710-9f38-444b-a3ce-e9acef54b8c8" />
    </div>

    The screenshot shows an older version of the user page, which had an **iOS** tab. The current page looks different.

5. Open FoXray and tap **Subscriptions** in the bottom menu.
6. Tap the **+** button.

    <div align=center markdown=1><img width=30% alt="The + button in Subscriptions" src="https://github.com/hiddify/hiddify-config/assets/125398461/f68c3805-989c-434d-b249-b2dea19ec332"/>

    </div>

7. Type any name you like.
8. Paste the link into the **URL** field.
9. Tap **Subscribe**. Your configs are added to the app.

    <div align=center markdown=1>
    <img width=30% alt="Name and URL fields" src="https://github.com/hiddify/hiddify-config/assets/125398461/f9118614-a8bf-42ae-9341-62c79fd7ffd9" />
    </div>

## Update your subscription

In the **Subscriptions** menu, tap the `↪️` icon. Your links are updated.

<div align=center markdown=1>
<img width=30% alt="Update icon" src="https://github.com/hiddify/hiddify-config/assets/125398461/9a899074-d180-47a4-9eed-cd56dcef3954" />
</div>

## Add a subscription with a QR code

1. In the FoXray menu, tap the QR code button.
2. Point the camera at the QR code of the link or config. It is added to the app.

<div align=center markdown=1>
<img width=30% alt="QR code button" src="https://github.com/hiddify/hiddify-config/assets/125398461/cc0afd0b-5bb5-4215-808c-d9a7e7175dac" />
</div>

If the QR code is saved as a photo on your phone:

1. In the FoXray menu, tap the photo button.
2. Choose the photo. The configs are added.

<div align=center markdown=1>
<img width=30% alt="Photo button" src="https://github.com/hiddify/hiddify-config/assets/125398461/1c3dfddc-b922-4c93-bb25-256c3fc39339" />
</div>

## Add a single config

We don't recommend this, because a single config can't be updated. Use it only if you need to.

1. On your user page, open **All Configs** and copy one config from **Individual Configs**.
2. In FoXray, tap the **Clipboard** icon in the FoXray menu. The copied config is added.

<div align=center markdown=1>
<img width=30% alt="Clipboard icon" src="https://github.com/hiddify/hiddify-config/assets/125398461/02be5d9c-3894-438e-be9b-072489033f2d" />
</div>


## Test the connections

First choose the test type:

1. Go to **Setting**, then the **Speed Test** section.
2. Under **PingType**, choose **TCPPing**, **TLSPing** or **RealPing**. **RealPing** gives the most realistic result.

<div align=center markdown=1>
<img width=30% alt="PingType setting" src="https://github.com/hiddify/hiddify-config/assets/125398461/b6940f2e-5b0d-4c40-a1ab-36ccd6b532d7" />
</div>

Then, on the main page of the app, tap the connection test icon.

<div align=center markdown=1>
<img width=30% alt="Connection test icon" src="https://github.com/hiddify/hiddify-config/assets/125398461/6851f393-45a1-4cdd-ab77-d09119a99476" />
</div>


## Limit memory use

Go to **Setting**, then **ToolBox**, and turn on **Limit Memory Usage**.

<div align=center markdown=1>
<img width=30% alt="Limit Memory Usage" src="https://github.com/hiddify/hiddify-config/assets/125398461/7f0f8830-5b95-4d1a-9afb-7337309238ff" />
</div>

## Add a DNS server

A **DNS server** turns website names into IP addresses.

1. In the FoXray menu, open the **DNS** section.
2. Tap **+**.
3. Type any name.
4. Enter the DNS address you want in the **Default DNS Address** field.
5. Leave the other fields as they are and save.

<div align=center markdown=1>
<img width=30% alt="Default DNS Address field" src="https://github.com/hiddify/hiddify-config/assets/125398461/888f5e36-bf2b-4534-9918-dfd1f4fe2ed1" />
</div>

## Premium features

The following features are only available if you bought the premium version of the app.

### Update subscriptions automatically

Go to **Setting** and turn on **Auto Update Subscription**.

<div align=center markdown=1>
<img width=30% alt="Auto Update Subscription" src="https://github.com/hiddify/hiddify-config/assets/125398461/24534c01-ff41-49fc-acb2-4daa47d36635" />
</div>

### Always On

Go to **Setting**, then **Pro ToolBox**, and turn on **Always On**. Your VPN then stays on all the time.

<div align=center markdown=1>
<img width=30% alt="Pro ToolBox options" src="https://github.com/hiddify/hiddify-config/assets/125398461/ab49fa85-742a-4002-afee-6f518146d9a4" />
</div>

### Show the server location

In **Setting** → **Pro ToolBox**, turn on **Show Location**. After you connect, the app shows where the server is.

### Pin the connected config

In **Setting** → **Pro ToolBox**, turn on **Pin Outbound**. The connected config is pinned to the top of the main page.

### Test configs before connecting

In **Setting** → **Pro ToolBox**, turn on **Test Outbound before Start**. The app tests the configs before it connects.

## Turn on fragment

**Fragment** splits the first TLS packet into small pieces, which can help get past filtering. Read more in [How the TLS trick works](/manager/basic-concepts-and-troubleshooting/How-the-TLS-Trick-works-and-its-usage/).

1. Tap the connection in the app.
2. Turn on **Fragment**.
3. Enter these suggested values:

    ```text
    packets: tlshello
    length: 100-200
    interval: 10-20
    ```

<div align=center markdown=1>
<img src="https://github.com/hiddify/Hiddify-Manager/assets/125398461/184d50de-95c8-4086-a2df-6e01c5c5f6fc" alt="Fragment settings in FoXray" width="30%" />

</div>

Depending on your internet provider, you may need other values. You can also change the packet type from `tlshello` to TCP segments `1-3`, although filtering may detect this mode sooner:

```text
packets: 1-3
```

</div>
