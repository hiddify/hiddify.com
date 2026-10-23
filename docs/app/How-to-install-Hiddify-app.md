---
title: How to install the Hiddify app
---

<div dir="ltr" markdown="1">

# How to install the Hiddify app

This page shows you how to download and install Hiddify App on your phone or computer. Hiddify App is a free, ad-free and open-source client that connects you to a proxy or VPN server so you can reach the free internet. You need it if someone (or your own Hiddify server) gave you a config or subscription link.

Hiddify App is built on **sing-box** (the engine that makes the connections). It supports many protocols, including VLESS, VMess, Trojan, Reality, TUIC, Hysteria, WireGuard, AmneziaWG, Naive and SSH, and it accepts sing-box, V2ray, Clash and Clash Meta subscription links. See the [full feature list](https://github.com/hiddify/hiddify-app/blob/main/README.md) on GitHub.

The latest stable version is **v4.1.1**.

## Before you start

Check that your device is supported:

| Device | What you need |
|---|---|
| Android | Android 7.0 or later |
| iPhone / iPad | iOS 15 or later |
| Windows | Windows 10 (version 1809) or Windows 11, 64-bit |
| macOS | macOS 10.15 (Catalina) or later, Intel or Apple Silicon |
| Linux | 64-bit (x64) Linux; Debian/Ubuntu-based systems are best supported |

!!! note "Windows 7, Windows 8 and RPM-based Linux"
    Hiddify App does not support Windows 7 or 8. There is also no `.rpm` package any more (it was removed in v4): on Fedora, openSUSE and similar systems, use the AppImage file.

## Which file should I download?

Pick the row for your device. Store versions update themselves; the files from GitHub do not.

| Device | Recommended | Other options |
|---|---|---|
| Android | [Google Play](https://play.google.com/store/apps/details?id=app.hiddify.com) | APK file: [universal](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Android-universal.apk) (works on every phone), [arm64](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Android-arm64.apk), [arm7](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Android-arm7.apk), [x86_64](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Android-x86_64.apk) |
| iPhone / iPad | [App Store](https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532) | — |
| Windows | [Setup file (.exe)](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Windows-Setup-x64.exe) | [Microsoft Store](https://apps.microsoft.com/detail/9pdfnl3qv2s5), [MSIX package](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Windows-x64.msix), [portable ZIP](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Windows-Portable-x64.zip), winget |
| macOS | [DMG file](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-MacOS.dmg) | [PKG installer](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-MacOS-Installer.pkg), [App Store](https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532) (Apple Silicon Macs) |
| Linux | [AppImage](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Linux-x64-AppImage.AppImage) | [.deb package](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Debian-x64.deb) (Debian, Ubuntu, Mint), [AppImage in a .tar.gz](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Linux-x64-AppImage.tar.gz) |

All files are also listed on the [GitHub releases page](https://github.com/hiddify/hiddify-app/releases/latest).

<div align=center>
 <a href="https://play.google.com/store/apps/details?id=app.hiddify.com"><img width=20% alt="Get it on Google Play" src="https://raw.githubusercontent.com/hiddify/hiddify-app/main/docs/google-play-badge.png"></a>
<br>
<br>
<a href="https://www.youtube.com/watch?v=vUaA1AEUy1s"><img width="32%" alt="Video (in Persian): installing Hiddify on Windows" src="https://github.com/hiddify/hiddify-next/assets/125398461/0f1e88a7-ecf0-4ba7-8c12-f24f70c68c3d" /></a>
</div>

## Install the app

Open the section for your device.

<details markdown="1"> <summary><b>Install on Android</b> (click)</summary>

**From Google Play (recommended)**

1. Open [Hiddify on Google Play](https://play.google.com/store/apps/details?id=app.hiddify.com).
2. Tap `Install`.
3. When the install finishes, tap `Open`.

**From an APK file (if you cannot use Google Play)**

1. Download the [universal APK](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Android-universal.apk). It works on every Android phone.
2. Open the downloaded file from your notifications or from the `Downloads` folder.

    <img width=260 alt="The Hiddify APK in the Downloads folder" src="/assets/app-install/android-downloads.webp" style="display:block;margin:0 auto">

3. If Android says it cannot install apps from this source, tap `Settings`, turn on `Allow from this source`, then go back.
4. Android asks "Do you want to install this app?". Tap `Install`.

    <img width=260 alt="Install prompt for Hiddify" src="/assets/app-install/android-install.webp" style="display:block;margin:0 auto">

5. When you see `App installed`, tap `Open`.

    <img width=260 alt="App installed message" src="/assets/app-install/android-installed.webp" style="display:block;margin:0 auto">

</details>
<br>

<details markdown="1"> <summary><b>Install on iPhone or iPad</b> (click)</summary>

1. Open [Hiddify Proxy & VPN on the App Store](https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532).
2. Tap `Get` and confirm with Face ID, Touch ID or your password.
3. Open the app. The first time you connect, iOS asks to add a VPN configuration: tap `Allow`.

!!! note
    The app is not available in the App Store of every country. If you cannot find it, your Apple ID may be set to a country where it is not offered.

</details>
<br>

<details markdown="1"> <summary><b>Install on Windows</b> (click)</summary>

You can also install from the [Microsoft Store](https://apps.microsoft.com/detail/9pdfnl3qv2s5), or open **Command Prompt** and run:

```bash
winget install Hiddify.Next
```

(`Hiddify.Next` is the app's old name; it still installs the current Hiddify App.)

To install with the setup file:

1. Download the [setup file](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Windows-Setup-x64.exe) (`Hiddify-Windows-Setup-x64.exe`).
2. Double-click the downloaded file. When Windows asks "Do you want to allow this app to make changes to your device?", click `Yes`.

    <img width=30% alt="Windows User Account Control prompt" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/e4174de0-10b5-4b46-9baf-2e302162da5a" style="display:block;margin:0 auto">

3. If a blue "Windows protected your PC" window appears, click `More info`.

    <img width=40% alt="Windows protected your PC warning" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/8a3bc452-004d-4be7-a9bb-21aad90db7fc" style="display:block;margin:0 auto">

4. Click `Run anyway`.

    <img width=40% alt="Run anyway button" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/36293a7c-f56a-4811-8302-474874654b70" style="display:block;margin:0 auto">

5. The installer shows where the app will be installed. Keep the default folder (or change it) and click `Next`.

    <img width=60% alt="Choose install location" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/7196a86f-3f74-4177-b611-19b484e0da9a" style="display:block;margin:0 auto">

6. Choose extra options, such as a desktop shortcut or starting the app automatically, and click `Next`.

    <img width=60% alt="Extra install options" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/bcac0d1e-f8d8-46d9-bedc-4fe04571a504" style="display:block;margin:0 auto">

7. Click `Install`.

    <img width=60% alt="Ready to install" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/980314df-c907-407c-aa4d-a94d4d492b66" style="display:block;margin:0 auto">

8. Wait while the app installs.

    <img width=60% alt="Installation progress" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/1aee90d0-dde1-4bf8-b673-058fc0e9204a" style="display:block;margin:0 auto">

9. When you see the window below, click `Finish`. The app starts. If it does not, double-click the Hiddify shortcut on your desktop.

    <img width=60% alt="Installation finished" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/4a8849c5-24f0-4376-be4d-355eb754f395" style="display:block;margin:0 auto">

!!! tip "If the app does not start"
    If Windows shows an error about a missing file such as `MSVCP140.dll`, install the [Microsoft Visual C++ Redistributable (x64)](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist) and try again.

</details>
<br>

<details markdown="1"> <summary><b>Install on macOS</b> (click)</summary>

On a Mac with Apple Silicon (M1 or newer) you can also install from the [App Store](https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532).

To install with the DMG file:

1. Download the [DMG file](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-MacOS.dmg) (`Hiddify-MacOS.dmg`). It works on both Intel and Apple Silicon Macs.
2. Open your `Downloads` folder and double-click the file.

    <img width=60% alt="Downloaded DMG file" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/e6cbdb24-ef18-49a0-9c40-0f4ea4859def" style="display:block;margin:0 auto">

3. Drag the Hiddify icon onto the `Applications` folder. This copies the app to your Mac.

    <img width=60% alt="Drag the app into Applications" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/07fa37b8-fc37-4613-b148-2eb932a3d53a" style="display:block;margin:0 auto">

4. Open `Applications` and double-click Hiddify.

    <img width=60% alt="Hiddify in the Applications folder" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/8a32bcd9-367d-4cf1-8951-c764b5f86795" style="display:block;margin:0 auto">

5. The first time, macOS may say it cannot open the app because it was not downloaded from the App Store. Click `OK` (or `Done`).

    <img width=30% alt="macOS cannot open the app warning" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/a65690ed-e169-4c9d-a908-93a4260fddf1" style="display:block;margin:0 auto">

6. Open **System Settings > Privacy & Security** (on older macOS: **System Preferences > Security & Privacy > General**), scroll down and click `Open Anyway` next to the Hiddify message.

    <img width=60% alt="Open Anyway in Security settings" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/97fa1692-5eb2-436c-9070-804a71c3bc81" style="display:block;margin:0 auto">

7. Click `Open`.

    <img width=60% alt="Confirm Open" src="https://github.com/hiddify/Hiddify-Server/assets/125398461/cbdec7f8-e12e-4613-b51d-9870df2acd49" style="display:block;margin:0 auto">

From now on, you can open Hiddify from `Applications` like any other app.

</details>
<br>

<details markdown="1"> <summary><b>Install on Linux</b> (click)</summary>

**Option 1: AppImage (works on most 64-bit distributions)**

1. Download the [AppImage file](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Linux-x64-AppImage.AppImage) (`Hiddify-Linux-x64-AppImage.AppImage`). You do not need to extract it.
2. Open a terminal and make the file executable. This example assumes the file is in your `Downloads` folder:

    ```bash
    chmod +x ~/Downloads/Hiddify-Linux-x64-AppImage.AppImage
    ```

3. Start the app:

    ```bash
    ~/Downloads/Hiddify-Linux-x64-AppImage.AppImage
    ```

    You can also double-click the file in your file manager.

If nothing happens or you see an error about **FUSE** (a system library that AppImage files need), install it in a terminal and try again.

On Ubuntu 22.04:

```bash
sudo apt install libfuse2
```

On Ubuntu 24.04 and newer:

```bash
sudo apt install libfuse2t64
```

**Option 2: .deb package (Debian, Ubuntu, Linux Mint)**

1. Download the [.deb package](https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Debian-x64.deb) (`Hiddify-Debian-x64.deb`).
2. In a terminal, run:

    ```bash
    sudo apt install ~/Downloads/Hiddify-Debian-x64.deb
    ```

3. Open Hiddify from your applications menu.

</details>
<br>

## First start

The first time you open the app, a welcome screen with three options opens. The app picks the language and region for you. If they are right, just tap `Start`.

<div align=center>
<img width=260 alt="First start: language, region and analytics" src="/assets/app-install/en-first-run.webp">
</div>

1. **Language:** if the app's language is wrong, tap `Language` and choose yours.
2. **Region:** tap `Region` and choose the country you are in (for example `Iran (ir)`). The app uses this to open local websites directly, without the proxy. If your country is not in the list, choose `Other`.
3. **Turn on analytics:** this switch is on by default. While it is on, the app sends anonymous crash and usage data that helps the developers improve it. Turn it off if you do not want that.
4. Tap `Start`.

<div align=center>
<img width=260 alt="Language list" src="/assets/app-install/en-language.webp">
<img width=260 alt="Region list" src="/assets/app-install/en-region.webp">
</div>

You should now see the app's home page. Next time you open the app, it goes straight to this page. The `+` button at the top adds a config or subscription link, and the big button in the middle (`Tap to connect`) connects you.

<div align=center>
<img width=260 alt="Hiddify app home page" src="/assets/app-install/en-home.webp">
</div>

!!! note
    The Android screenshots on this page come from version 5 of the app (a pre-release). On other versions and on computers the steps are the same, but some screens may look a little different.

## Next step

To add your config or subscription link and connect, read [How to use the Hiddify app](How-to-use-Hiddify-app.md).

</div>
