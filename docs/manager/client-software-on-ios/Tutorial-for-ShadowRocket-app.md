---
title: Tutorial for ShadowRocket app
---

<div dir="ltr" markdown="1">


# Tutorial for ShadowRocket app

This page shows you how to add your Hiddify subscription to **Shadowrocket** on iPhone and iPad, and how to use its most useful settings. Shadowrocket is a paid app that works with Xray-based configs.

!!! tip "Recommended: Hiddify App"
    The easiest app for a Hiddify server is the free **Hiddify App**. It is on the [App Store](https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532). See [How to install Hiddify App](/app/How-to-install-Hiddify-app/).

## Before you start

- Buy and install **Shadowrocket** from the [App Store](https://apps.apple.com/us/app/shadowrocket/id932747118).
- Have your **user page link** ready. This is the link your server admin sent you. It opens your personal Hiddify page.

A **subscription link** is one link that holds all your connection settings (configs). Shadowrocket can refresh it later to get new settings from the server.

## Add your subscription: the quick way

1. On your iPhone, open your user page link in Safari.
2. Tap the large round button in the middle of the page. A window called **Configure your VPN** opens.
3. Under **Choose one of the apps below**, tap **Shadowrocket**. If you don't see it, tap **View More**. You can also download the app from here.
4. Tap **Import To App**. Shadowrocket opens and adds your subscription.

If that doesn't work, add the link by hand as shown below.

!!! note "Lite and Normal configs no longer exist"
    Older versions of the user page offered two kinds of configs in an **iOS** tab: **Lite** (only blocked sites go through the VPN) and **Normal** (all traffic goes through the VPN). The current user page has no iOS tab and no Lite/Normal choice. If you want local sites to open without the VPN, ask your admin; this is set on the server. If your admin turned on [WARP](/manager/configuration-and-advanced-settings/How-to-activate-WARP-on-the-Hiddify-panel/), local sites can open through WARP.

<div align=center markdown=1>
<img width=30% alt="Shadowrocket section on an older version of the user page" src="https://github.com/hiddify/hiddify-config/assets/125398461/24520888-2489-499d-b0a4-46c297e9f83f" />
</div>

<div align=center markdown=1>
<img width=30% alt="Lite and Normal configs on an older version of the user page" src="https://github.com/hiddify/hiddify-config/assets/125398461/61500b2d-2947-493e-8a9d-3d8f48cb5e7a" />
</div>

## Add your subscription by hand

First get the link:

1. On your user page, open the menu and tap **All Configs**.
2. In the **Subscription Links** section, find **Subscription link** and tap **Get Link**. A window with a QR code and a **Copy Link** button opens.

Then add it to Shadowrocket in one of two ways.

### Copy and paste the link

1. Tap **Copy Link**.
2. Open Shadowrocket and tap the **+** button in the top-right corner.

    <div align=center markdown=1>
    <img width=30% alt="The + button in Shadowrocket" src="https://github.com/hiddify/hiddify-config/assets/125398461/d116347f-31bc-4ca9-a1fc-bdb9364e5e74" />
    </div>

3. Set **Type** to **Subscribe**.
4. Paste the link into the **URL** field.
5. Tap **Save**.

    <div align=center markdown=1>
    <img width=30% alt="Type Subscribe and the URL field" src="https://github.com/hiddify/hiddify-config/assets/125398461/c087970e-aebc-479d-8b8a-bc54a78cc7f8" />
    </div>

All your configs now load in the app.

### Scan the QR code

1. On the Shadowrocket home screen, tap the scanner button.

    <div align=center markdown=1>
    <img width=30% alt="Scanner button" src="https://github.com/hiddify/hiddify-config/assets/125398461/cee3abfe-db05-4e2c-925d-fa57010d3465" />
    </div>

2. Scan the QR code shown on your user page. Your configs are added to the app.

## Test the configs

On the home screen, tap **Connectivity Test**. The app tests each config.

<div align=center markdown=1>
<img width=30% alt="Connectivity Test" src="https://github.com/hiddify/hiddify-config/assets/125398461/49a37a3c-b1f7-48ba-91e2-0a4ac7dc3e5f" />
</div>

For more realistic results:

1. Tap **Settings** in the bottom menu.
2. Set **Test Method** to **Connect**.
3. Run the test again.

<div align=center markdown=1><img width=30% alt="Test Method set to Connect" src="https://github.com/hiddify/hiddify-config/assets/125398461/8760fd19-9056-4c0c-a4a0-aeebd728656f" />
</div>


## Update your subscription

Tap the update icon above the configs of a subscription. The configs are updated with the latest settings from the server.

<div align=center markdown=1>
<img width=30% alt="Update icon above the configs" src="https://github.com/hiddify/hiddify-config/assets/125398461/0878e805-a24e-4f19-831a-f526b475db4a" />
</div>


## Subscription settings

Go to **Settings** and tap **Subscribe** near the bottom. Here you can set:

### Update when the app opens

Turn on **Update on Open**.

<div align=center markdown=1>
<img width=30% alt="Update on Open" src="https://github.com/hiddify/hiddify-config/assets/125398461/aeb08d16-20d3-424e-8c6d-7d13f06aeb8d" />
</div>

### Update automatically in the background

Turn on **Auto Background Update**. The app then refreshes your subscriptions at regular intervals.

<div align=center markdown=1>
<img width=30% alt="Auto Background Update" src="https://github.com/hiddify/hiddify-config/assets/125398461/97540ef0-399f-4260-85a1-af0c0594533b" />
</div>

### Sort by ping

Turn on **Sort by ping** to list the configs by their test result, best first.

<div align=center markdown=1>
<img width=30% alt="Sort by ping" src="https://github.com/hiddify/hiddify-config/assets/125398461/afeb9a4d-a12f-49f1-aca7-f5eae5c6bed2" />
</div>


## Prevent IP leaks

An **IP leak** means a website can see your real IP address even though the VPN is on.

1. Go to **Settings**, then **UDP**.
2. Turn on **Disable STUN**.

<div align=center markdown=1>
<img width=30% alt="Disable STUN" src="https://github.com/hiddify/hiddify-config/assets/125398461/3bd81556-4119-4659-8db7-0826bbdbd6ee" />
</div>


## Fix missing sound in some apps

If some apps (for example Clubhouse) play no sound:

1. Go to **Settings**, then **TCP**.
2. Change the **Fingerprint** value.

<div align=center markdown=1>
<img width=30% alt="Fingerprint setting" src="https://github.com/hiddify/hiddify-config/assets/125398461/fe7a7a27-016c-45b9-92b5-2e9427ba165a" />
</div>


## Shortcuts

Go to **Settings**, then **Shortcuts**. Here you can set a voice command for an action, for example to start the VPN.

## Keep the VPN on (On Demand)

Go to **Settings**, then **On Demand**.

<div align=center markdown=1>
<img width=30% alt="On Demand settings" src="https://github.com/hiddify/hiddify-config/assets/125398461/af641742-dc91-468e-9135-78de911e6703" />
</div>

#### Always On
When this is on, your VPN always stays on.

#### On Demand
When this is on and your connection drops, Shadowrocket blocks all internet traffic so your real IP address is not exposed.

#### Disconnect on Sleep
When this is on, the VPN disconnects when the phone goes to sleep.

## Share your VPN with other devices

You can share your VPN with another device on the same network, for example a device that can't install a VPN app.

1. Go to **Settings**, then **Proxy**.
2. Tap **Proxy Share**.
3. Turn on **Enable Share**. The app shows an IP address and a port.

    <div align=center markdown=1>
    <img width=30% alt="Proxy Share with IP and port" src="https://github.com/hiddify/hiddify-config/assets/125398461/d764b726-6ddd-4a5a-aa76-f9ad8165e4f1" />
    </div>

4. On the other device, open its network proxy settings and enter that IP address and port.

The other device now uses your VPN without installing anything.

## Create a load balancer

A **load balancer** spreads your traffic over several configs, so one slow or blocked config doesn't stop you.

1. On the home screen, hold your finger on the screen and swipe down. A hidden menu opens.

    <div align=center markdown=1>
    <img width=30% alt="Hidden menu" src="https://github.com/hiddify/hiddify-config/assets/125398461/59872f56-e9ff-4c50-85a0-65ccd488e704" />
    </div>

2. Tap the **+** button.

    <div align=center markdown=1>
    <img width=30% alt="The + button for a new load balancer" src="https://github.com/hiddify/hiddify-config/assets/125398461/b67bc883-e643-465c-85dc-e6eeb719723c" />
    </div>

3. Type any name.
4. Set **Type** to **load-balance**.
5. Under **Policy**, select the configs to use: the ones with the best ping, or all of them.
6. Leave **Interval** (time between tests) and **Timeout** (how long a config may fail and still count as working) at their default values, unless you know what you need.
7. Tap **Save**.

    <div align=center markdown=1>
    <img width=30% alt="Load balancer settings" src="https://github.com/hiddify/hiddify-config/assets/125398461/be6e132b-d9d4-45ff-ab8a-94b72d764139" />
    </div>

8. Tap the new load balancer, then tap **Test**. This tests it and connects through it.

    <div align=center markdown=1>
    <img width=30% alt="Testing the load balancer" src="https://github.com/hiddify/hiddify-config/assets/125398461/819da751-8a46-4ab3-88e2-00a5e0b3f724" />
    </div>

When you turn Shadowrocket on or off, the load balancer turns on or off with it.

## Fix sites or apps that don't open

If some sites or apps don't open, or Telegram GIFs don't load:

1. Go to **Settings**.
2. Open **TCP**.
3. Set **TLS** to **Network**.
4. Set **Fingerprint** to **Safari15_5**.
5. Set **Max Read Length** to **16384**.
6. Go back to **Home**.
7. Set **Global Routing** to **Proxy**.

</div>
