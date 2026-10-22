---
title: Tutorial for Stash app
---

<div dir="ltr" markdown="1">

# Tutorial for Stash app

This page shows you how to add your Hiddify profile to **Stash** on iPhone and iPad and how to use its main modes. Stash is a paid app based on Clash.

!!! tip "Recommended: Hiddify App"
    The easiest app for a Hiddify server is the free **Hiddify App**. It is on the [App Store](https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532). See [How to install Hiddify App](/app/How-to-install-Hiddify-app/).

## Before you start

- Buy and install **Stash** from the [App Store](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349). The App Store lists iOS 16 or later.
- Have your **user page link** ready. This is the link your server admin sent you. It opens your personal Hiddify page.

In Stash, a **profile** is a file (in YAML format) that holds all your connections (configs) and the rules for which traffic goes through the VPN.

## Add your profile: the quick way

1. On your iPhone, open your user page link in Safari.
2. Tap the large round button in the middle of the page. A window called **Configure your VPN** opens.
3. Under **Choose one of the apps below**, tap **Stash**. If you don't see it, tap **View More**. You can also download the app from here.
4. Tap **Import To App**. Stash opens and adds your profile.

If that doesn't work, add the profile by hand as shown below.

!!! note "Lite and Normal profiles no longer exist"
    Older versions of the user page had an **iOS** tab with two Stash profiles: a green **Lite** profile (only blocked sites go through the VPN) and an orange **Normal** profile (all traffic goes through the VPN). The current panel offers a single **Clash Meta** subscription instead. If you want local sites to open without the VPN, ask your admin; this is set on the server.

<div align=center markdown=1>
<img width=30% alt="Stash section on an older version of the user page" src="https://github.com/hiddify/hiddify-config/assets/125398461/51f5dfdc-102f-4057-8c0b-33b123d6108b" />
</div>

<div align=center markdown=1>
<img width=30% alt="Lite and Normal profiles on an older version of the user page" src="https://github.com/hiddify/hiddify-config/assets/125398461/8f93711d-27ec-473c-a1d9-928ee3656abd" />
</div>

## Add your profile by hand

First get the link:

1. On your user page, open the menu and tap **All Configs**.
2. In the **Subscription Links** section, find **Clash Meta** and tap **Get Link**. A window with a QR code and a **Copy Link** button opens.

### Copy the link into Stash

1. Tap **Copy Link**.
2. Open Stash. On the **Settings** page, tap **Config File**.
3. Tap **Download from URL**.

    <div align=center markdown=1>
    <img width=30% alt="Download from URL" src="https://github.com/hiddify/hiddify-config/assets/125398461/ffbbd7a4-96aa-4331-9987-09f13f46edc8" />
    </div>

4. Paste the link and tap **Download**. The profile is added to the app.

    <div align=center markdown=1>
    <img width=30% alt="Paste the link and tap Download" src="https://github.com/hiddify/hiddify-config/assets/125398461/84e1e1da-2d09-4b59-ac88-91412746e4ee" />
    </div>

### Add the profile with a QR code

1. Keep the QR code from the user page on screen (for example on a computer).
2. Open Stash. On the **Settings** page, tap **Config File**.
3. Tap **Download from QRcode**.

    <div align=center markdown=1>
    <img width=30% alt="Download from QRcode" src="https://github.com/hiddify/hiddify-config/assets/125398461/02ca1ecf-3552-4c8e-9a2f-625be8c8b7ac" />
    </div>

4. Scan the QR code. The profile is added to the app.

## The Policy menu

This menu shows the policies, that is the configs in the profiles you imported.

<div align=center markdown=1>
<img width=30% alt="Policy menu" src="https://github.com/hiddify/hiddify-config/assets/125398461/7fd169ea-18b4-4f7f-85b4-ee2073b8c25f" />
</div>

Each mode in the Policy menu works together with a mode in the **Outbound** section, which is explained further down.

#### Proxy mode
Uses one config that you choose. It is used with the **Global** outbound mode.

#### Automatic mode
The app connects to the config with the best test result. It is used with the **Rule** outbound mode.

#### Sequential mode
The app uses the configs one after another, switching from time to time. This spreads the load over time. It is different from load-balance mode, which uses several configs at the same time. It is used with the **Rule** outbound mode.

#### Auto mode
The automatic config selection used by **Automatic** mode.

#### Load-Balance mode
Uses several connections at the same time, which spreads the load over them. This can help when the server's IP is partly blocked and single connections work badly. It is used with the **Rule** outbound mode.

#### Connection test
Tap the lightning icon to test the connections.

<div align=center markdown=1>
<img width=30% alt="Lightning icon for the connection test" src="https://github.com/hiddify/hiddify-config/assets/125398461/7bdb1519-7179-4c6e-a6e9-ee00c3bc06db" />
</div>

## Update your profiles

1. Go to **Settings**, then **Config File**.
2. Hold your finger on a profile.
3. In the menu that appears, tap **Update Now**.

<div align=center markdown=1>
<img width=30% alt="Update Now" src="https://github.com/hiddify/hiddify-config/assets/125398461/3ecb0ab1-40b9-40e5-8f93-5a37f9b0a1dd" />
</div>

## Update your profiles automatically

1. In **Settings**, tap **More Settings**.

    <div align=center markdown=1>
    <img width=30% alt="More Settings" src="https://github.com/hiddify/hiddify-config/assets/125398461/ab8222a0-b24b-487b-bb62-4c5509d27806" />
    </div>

2. In the **CONFIG FILE** section, set the time between updates in **Update Interval**.
3. Turn on **Auto Update**.

Stash also updates your profiles each time you open the app.

## Choose the Outbound mode

On the **Home** page of the app, the **Outbound** section has three modes.

<div align=center markdown=1>
<img width=30% alt="Outbound modes" src="https://github.com/hiddify/hiddify-config/assets/125398461/51b861c7-2e12-4541-a214-84311270cb8d" />
</div>

#### Rule mode
Uses the rules in the profile to decide which traffic goes through the VPN. For example, if the profile has rules for local sites, their traffic does not go through the VPN.

#### Global mode
Ignores the rules. You pick one config in the **Policy** menu under **Proxy** mode, and all your phone's traffic goes through it. This is useful when you want to use one specific config.

#### Direct mode
Nothing goes through the VPN. It is as if the VPN were off.

## On Demand

Go to **Settings**, then **On Demand**.

<div align=center markdown=1>
<img width=30% alt="On Demand settings" src="https://github.com/hiddify/hiddify-config/assets/125398461/0854f4f3-3628-41a3-a8b4-3a3a08474370" />
</div>

#### Always On
When this is on, your VPN is always on.

#### On Demand
When this is on, the VPN is active only while the phone is unlocked and turns off at other times.

## Troubleshoot connections

To see more details about your connections, open the **Utilities** menu and tap **Network Diagnosis**. It shows a log of all connections, which helps you find problems. The **Connectivity** and **Proxy** subsections are the most useful.

<div align=center markdown=1>
<img width=30% alt="Network Diagnosis" src="https://github.com/hiddify/hiddify-config/assets/125398461/3685baf2-5d0f-4305-a151-12bcc761ab23" />
</div>

</div>
