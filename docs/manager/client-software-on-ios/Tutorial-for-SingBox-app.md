---
title: Tutorial for SingBox app
---

<div dir="ltr" markdown="1">


# Tutorial for SingBox app

This page shows you how to add your Hiddify subscription to the official **sing-box** app on iPhone and iPad, and how to connect. It is for users of a Hiddify Manager server who want to use sing-box instead of the Hiddify App.

!!! warning "This page used to be about the SSH proxy"
    Older versions of this page showed how to add the Hiddify panel's **SSH proxy** to sing-box. The SSH proxy service was removed in Hiddify Manager v13, so that part no longer applies. The steps below add your normal Hiddify subscription instead.

!!! tip "Recommended: Hiddify App"
    The easiest app for a Hiddify server is the free **Hiddify App**. It is on the [App Store](https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532). See [How to install Hiddify App](/app/How-to-install-Hiddify-app/).

## Before you start

- An iPhone or iPad with iOS 15 or later.
- Your **user page link**. This is the link your server admin sent you. It opens your personal Hiddify page, where your subscription links are.

A **subscription link** is one link that holds all your connection settings (configs). The app can refresh it later to get new settings from the server.

## Download the app

The official sing-box app for iPhone, iPad and Apple TV is now called **sing-box MT**. The old App Store listing (id6451272673) no longer exists.

- [iOS / iPadOS (App Store: sing-box MT)](https://apps.apple.com/us/app/sing-box-mt/id6785326793)
- [Android (Google Play)](https://play.google.com/store/apps/details?id=io.nekohasekai.sfa)
- Other platforms: see the [official sing-box download page](https://sing-box.sagernet.org/clients/apple/).

## Add your subscription: the quick way

1. On your iPhone, open your user page link in Safari.
2. Tap the large round button in the middle of the page. A window called **Configure your VPN** opens.
3. Under **Choose one of the apps below**, tap **sing-box**. If you don't see it, tap **View More**.
4. Tap **Import To App**. The sing-box app opens and asks to add the profile.
5. Confirm. The new profile now appears in the app's **Profiles** list.

If the app doesn't open, use the manual way below.

## Add your subscription: the manual way

1. On your user page, open the menu and tap **All Configs**.
2. In the **Subscription Links** section, find **Hiddify / Singbox** and tap **Get Link**.
3. Tap **Copy Link**.
4. Open the sing-box app and go to the **Profiles** menu.

    <div align=center markdown=1>
    <img width=30% alt="Profiles menu in sing-box" src="https://github.com/hiddify/hiddify-config/assets/125398461/816fbc46-21c2-4109-b2c9-3d9529a5a0ce" />

    </div>

5. Tap **New Profile**.

    <div align=center markdown=1>
    <img width=30% alt="New Profile button" src="https://github.com/hiddify/hiddify-config/assets/125398461/b9651f36-24db-437e-9a7d-80c2d4a7622a" />

    </div>

6. Set **Type** to **Remote**.

    <div align=center markdown=1>
    <img width=30% alt="Type set to Remote" src="https://github.com/hiddify/hiddify-config/assets/125398461/e68609dd-d294-44cf-8404-7f6e7091d61e" />

    </div>

7. Type any name you like in the **Name** field.
8. Paste the link you copied into the **URL** field.
9. Tap **Create**.

    <div align=center markdown=1>
    <img width=30% alt="Name and URL fields" src="https://github.com/hiddify/hiddify-config/assets/125398461/603f8676-b0cf-4e0d-b31a-b272bd6adc03" />

    </div>

The profile now appears in the list of profiles.

<div align=center markdown=1>
<img width=30% alt="The new profile in the list" src="https://github.com/hiddify/hiddify-config/assets/125398461/8a27f295-0f46-4655-9c28-bd6acd82c6e0" />

</div>

!!! note
    The screenshots on this page come from an older version of sing-box. Menu names in the current app may look slightly different.

## Connect

1. Go to the **Dashboard** menu.
2. Select the profile you added.
3. Turn on the **Enabled** switch. If iOS asks to add a VPN configuration, tap **Allow**.

<div align=center markdown=1>
<img width=30% alt="Enabled switch on the Dashboard" src="https://github.com/hiddify/hiddify-config/assets/125398461/8d911472-b2b4-4fb9-a36b-5e22cca273db" />

</div>

When it works, the VPN icon appears at the top of your iPhone screen and websites open normally. If it doesn't connect, go back to **Profiles**, update the profile, and try again. If it still fails, ask your server admin to check your account.

</div>
