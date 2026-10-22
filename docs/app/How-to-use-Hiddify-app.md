---
title: How to use the Hiddify app
---

<div dir="ltr" markdown="1">


# How to use the Hiddify app

This page shows you how to add your connection link to Hiddify App, connect, pick a server and change the most useful settings. It is for anyone who has installed the app and received a link from their provider or from their own Hiddify server.

## Before you start

You need:

1. Hiddify App installed on your device. If you have not installed it yet, follow [How to install the Hiddify app](How-to-install-Hiddify-app.md).
2. A connection link from your provider. This is usually your **user page** link (a personal web page that a Hiddify panel makes for each user) or a **subscription link**.

A few words you will see on this page:

- **Profile**: one connection link saved in the app. A profile can contain many servers.
- **Subscription link**: a link that gives the app a list of servers and updates it automatically. It must start with `https://`; the app no longer accepts plain `http://` subscription links.
- **Config**: the settings for one single server, for example a link that starts with `vless://` or `vmess://`.
- **Proxy**: one server in your profile that your traffic can go through.

<div align=center>
<a href="https://www.youtube.com/watch?v=EjHjLQbC40E"><img width="32%" alt="Video (in Persian): using the Hiddify app" src="https://github.com/hiddify/hiddify-next/assets/125398461/ea1480af-e7a8-4add-b0f2-600ace5efd4b" /></a>
</div>

!!! note
    The screenshots on this page come from an older version of the app. The steps are the same in v4.1.1, but some screens look different.

## Add a profile to the app

1. Open your user page link (you got it from your provider or panel admin).
2. On the user page, tap the button that opens your profile in Hiddify (in older panels: `Tap to Start Anti-Filter`). The app opens and adds your profile.

    <div align=center>
    <img width=60% alt="User page with the import button" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/d39e775c-4817-427b-b11c-6161ecffc81f">
    </div>

3. If the app does not open by itself, the page below appears. Tap `Copy Link` to copy your profile link.

    <div align=center>
    <img width=60% alt="Copy the profile link" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/e921e0a0-1034-456b-bc9c-fd59fd55503e">
    </div>

4. Open Hiddify App. On the `Home` page, tap the `+` button at the top of the screen. The "Add profile" window opens.

    <div align=center>
    <img width=60% alt="The + button on the Home page" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/279924ad-9f16-424f-9133-b5096329030a">
    </div>

5. Add the copied link in one of these ways:
    - Tap `Clipboard`. The app reads the link you copied and adds it.

        <div align=center>
        <img width=60% alt="Add from clipboard" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/e515d2d7-886f-4e33-9764-76b4398fc83b">
        </div>

    - Or tap `Manually`, type any name in `Name`, paste the link in `URL`, and tap `Add`.

        <div align=center>
        <img width=60% alt="Add a profile manually" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/2931f4c9-c2af-4d61-b0a9-40af563b248f">
        </div>

    - Or, if the link is shown as a QR code, tap `Scan QR` and point your camera at it.

When it worked, your profile appears at the top of the `Home` page. If you see "Invalid URL" or "Failed to add profile", check that you copied the whole link and that it starts with `https://`.

## Add a single config

Use this if you want to add only one server instead of a whole subscription.

1. On your user page, tap `All Configs`.

    <div align=center>
    <img width=60% alt="All Configs on the user page" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/92912b97-38bb-4973-a48d-44a29613598e">
    </div>

2. Find the config you want in the list and tap `Copy`.

    <div align=center>
    <img width=30% alt="Copy a single config" src="https://github.com/hiddify/hiddify-config/assets/125398461/eb4d7cf9-4f1f-4910-acc8-1c7d545ee1eb" />
    </div>

3. Open Hiddify App and tap the `+` button.
4. Tap `Clipboard`. The config is added to the app.

## Connect

1. After you add a profile, the `Home` page looks like this.

    <div align=center>
    <img width=60% alt="Home page with a profile" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/a69b2807-d9df-4a03-b48f-6f96f21ff377">
    </div>

2. Tap the big connect button in the middle of the screen. On Android and iOS, the first time, allow the app to create a VPN connection.

    <div align=center>
    <img width=60% alt="Connected" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/484b1f82-63d8-4a9b-b72d-fb78f8ac6da6">
    </div>

When the connection works, the button turns green and shows `Connected`. To disconnect, tap the button again.

If it stays on `Connecting...` or shows an error, try another server on the `Proxies` page (see below), or tap the update button on your profile to download a fresh server list. If nothing works, contact your provider.

## Manage profiles

- **Update a profile**: tap the update button on the profile card. This downloads the newest server list from your provider.

    <div align=center>
    <img width=60% alt="Update profile button" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/e5faed5f-c373-4acb-a33b-991599e2be5a">
    </div>

- **Switch to another profile**: tap the profile card (`View all profiles`) and choose the profile you want.

    <div align=center>
    <img width=60% alt="List of profiles" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/18f8e9e1-34b8-4a3f-b7bd-a70c9f9d9404">
    </div>

- **Edit, share or delete a profile**: open the menu of a profile in the list.

    <div align=center>
    <img width=60% alt="Edit a profile" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/c5520e82-aeae-4213-b55b-ecce33bfed0e">
    </div>

## Check and choose a server (Proxies)

1. Connect first, then open the `Proxies` page.

    <div align=center>
    <img width=60% alt="Proxies page" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/919020e5-0ed6-4523-8f2f-ece7e6d74219">
    </div>

2. You see every server in your profile, with its **delay** next to it. Delay is how long the server takes to answer, in milliseconds (ms): lower is faster.
3. By default the app picks the fastest working server for you. To use a specific one, tap it.
4. To measure the delay again, tap the `Test delay` button.

    <div align=center>
    <img width=60% alt="Test delay button" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/265bd648-4716-4791-80d4-666a2dc4b0b7">
    </div>

5. To sort the list, tap the sort button and choose `Default`, `Alphabetically`, `By delay` or `By usage`.

    <div align=center>
    <img width=60% alt="Sort proxies" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/95ca6072-96b5-4282-be66-bc8980befded">
    </div>

## Quick settings

On the `Home` page, tap the sliders button at the top of the screen (next to `+`). From here you can:

- Choose the **service mode** (see [VPN mode on a computer](#vpn-mode-on-a-computer) below):
    - `Proxy`: the app only runs a local proxy. Other apps must be set up to use it.
    - `System proxy` (computers only): browsers and most apps use the proxy automatically. This is the default on computers.
    - `VPN`: all traffic of the device goes through the app. This is the default on phones.
- Turn **WARP** on or off. See [How to use WARP in the Hiddify app](How-to-use-WARP-on-Hiddify-App.md).

## General settings

Open `Settings` and then `General`. The most useful options are:

<div align=center>
<img width=60% alt="General settings" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/4a00ed21-8988-419e-86a2-4ba102d8893f">
</div>

- `Language`: the language of the app.
- `Theme mode`: `System default`, `Light mode`, `Dark mode` or `Black mode` (fully black, which saves battery on some phone screens).
- `Start at login` (computers): start the app when you log in.
- `Start minimized` (computers): start the app hidden in the system tray (the small icons next to the clock) instead of opening its window.
- `Enable analytics`: send anonymous crash reports to help the developers.
- `Disable battery optimization` (Android): stops Android from closing the VPN in the background.

Other settings are grouped into `Routing`, `DNS`, `Inbound`, `TLS tricks` and `WARP`. Leave them at their defaults unless your provider tells you to change them.

!!! note "Removed in v4"
    The old `Config Options` page, `Enable TUN` switch, `Routing Assets` (GeoIP/GeoSite), `MultiPlexer` (Mux) settings and the `Experimental` switches no longer exist in Hiddify App v4. Their useful parts moved into the sections above.

## VPN mode on a computer

On Windows, macOS and Linux, the app starts in `System proxy` mode. Some apps (for example games or some desktop programs) ignore the system proxy. To send **all** traffic through Hiddify, use `VPN` mode. (In older versions this was called "TUN mode".)

`VPN` mode needs administrator rights (called **root** on Linux and macOS). If the app shows "Missing privilege" or does not connect in `VPN` mode, first open the app with administrator rights:

<details markdown="1"> <summary><b>Open the app as administrator on Windows</b></summary>

1. If the app is open, close it completely: right-click the Hiddify icon in the system tray (next to the clock) and click `Exit`.
2. Right-click the Hiddify icon on the desktop or in the `Start` menu and click `Run as administrator`.

    <div align=center>
    <img width=30% alt="Run as administrator" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/9db385ec-8aba-47f5-a5b7-d2c34899fbc1">
    </div>

3. Click `Yes` when Windows asks for permission.

</details>
<br>

<details markdown="1"> <summary><b>Open the app as administrator on macOS</b></summary>

1. If the app is open, close it completely: click the Hiddify icon in the menu bar at the top of the screen and click `Exit`.
2. Open the **Terminal** app.
3. Run this command and type your Mac password when asked (the password does not show while you type):

    ```bash
    sudo /Applications/Hiddify.app/Contents/MacOS/Hiddify
    ```

Keep the Terminal window open while you use the app.

</details>
<br>

<details markdown="1"> <summary><b>Open the app as root on Linux</b></summary>

1. If the app is open, close it completely: right-click the Hiddify icon in the system tray and click `Exit`.
2. Open a terminal and run the app with `sudo`. This example is for the AppImage in your `Downloads` folder; change the path if your file is somewhere else:

    ```bash
    sudo ~/Downloads/Hiddify-Linux-x64-AppImage.AppImage
    ```

</details>
<br>

Then switch to `VPN` mode:

1. On the `Home` page, open quick settings (the sliders button) and choose `VPN`. You can also go to `Settings` > `Inbound` > `Service mode` and choose `VPN`.

    <div align=center>
    <img width=60% alt="VPN (TUN) setting in an older version of the app" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/d624876a-bca9-4d52-b169-cf8f42b86f70">
    </div>

2. Go back to `Home` and tap the connect button. When it turns green, all your traffic goes through Hiddify.

</div>
