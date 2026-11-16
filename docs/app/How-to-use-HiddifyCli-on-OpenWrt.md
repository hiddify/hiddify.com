---
title: Hiddify Core on OpenWrt
---

# Hiddify Core on OpenWrt

This page shows how to install **Hiddify Core** on an OpenWrt router, give it your connection link, and send the traffic of your whole home network through it. Hiddify Core (`hiddify-core`, also called HiddifyCli) is the engine of the Hiddify app, without the app: see [Hiddify Core](../core/index.md).

!!! note "Written for Hiddify Core 5.9"
    This page is for Hiddify Core **5.9** (5.9.3) and OpenWrt **23.05 or newer** (OpenWrt 24.10 and 25.12 use the `apk` package manager, older versions `opkg`). Older guides told you to download `hiddify-cli-linux-…tar.gz` and write a service by hand: that is not needed any more, and those files no longer exist.

## Before you start

- **Free space on the router:** Hiddify Core needs about **105 MB** of free storage. Check it on the router:

    ```bash
    df -h /overlay
    ```

    Many small routers have only 16 to 128 MB of flash. If yours has less free space, add a USB drive as extra storage ([extroot](https://openwrt.org/docs/guide-user/additional-software/extroot_configuration)) first, or use a router or mini PC with more storage.

- **SSH access** to the router (`ssh root@192.168.1.1`, or the address of your router).
- **A connection link:** a subscription link or config links, for example from your Hiddify panel.

## Step 1: install

The installer finds your router's processor, downloads the ready package of the latest Hiddify Core release, installs it and starts the service. It needs `bash` and `curl`, which OpenWrt does not have by default.

1. Install `bash` and `curl`.

    On OpenWrt 24.10 and newer (`apk`):

    ```bash
    apk update && apk add bash curl
    ```

    On OpenWrt 23.05 (`opkg`):

    ```bash
    opkg update && opkg install bash curl
    ```

2. Run the installer:

    ```bash
    bash <(curl -fsSL https://raw.githubusercontent.com/hiddify/hiddify-core/main/installer.sh)
    ```

When it finishes, it prints `Installation successful!` and the places of the config and the service.

??? info "Install the package by hand instead"
    Each [Hiddify Core release](https://github.com/hiddify/hiddify-core/releases/latest) has a package for every OpenWrt processor type: `.apk` files for OpenWrt 24.10 and newer, `.ipk` files for OpenWrt 23.05.

    1. Find your router's package architecture: `apk --print-arch` (or, on OpenWrt 23.05, `opkg print-architecture`, the last line). For example `mipsel_24kc`, `aarch64_cortex-a53` or `x86_64`.
    2. Download the file with that name from the release, for example `hiddify-core-5.9.3-r0_mipsel_24kc.apk` or `hiddify-core_5.9.3_mipsel_24kc.ipk`, and copy it to `/tmp` on the router.
    3. Install it: `apk add --allow-untrusted /tmp/hiddify-core-*.apk` (or `opkg install /tmp/hiddify-core_*.ipk`).
    4. Start it: `/etc/init.d/hiddify-core enable && /etc/init.d/hiddify-core restart`.

## Step 2: give it your connection link

Hiddify Core's `run` command reads your links and builds the rest of the configuration by itself. It reads subscription links, single config links (`vless://`, `vmess://` …), and sing-box, Clash and Xray configs: see [what `run` can read](../core/index.md#run-or-srun).

1. Put your subscription link (or your config links, one per line) in a file:

    ```bash
    echo 'https://example.com/your-subscription-link' > /etc/hiddify-core/links.txt
    ```

2. Tell the service to use this file, and restart it:

    ```bash
    uci set hiddify-core.main.conffile='/etc/hiddify-core/links.txt'
    uci commit hiddify-core
    /etc/init.d/hiddify-core restart
    ```

## Step 3: check that it works

- The service log:

    ```bash
    logread -e hiddify-core
    ```

- On a phone or computer connected to the router, open a site that shows your IP address. It should show the IP of your proxy server, not your own.

## Router mode and proxy mode

The service has two modes, set in `/etc/config/hiddify-core` (`option mode`):

- `router` (the default): every device behind the router goes through Hiddify Core, for TCP, UDP and ping, with nothing to set up on the devices. Connections from outside still reach the router and its port forwards. See [Free internet for every device behind the router](How-to-Enable-Free-Internet-Access-for-Clients-Behind-an-OpenWrt-Router-Using-HiddifyCli.md).
- `proxy`: only a local HTTP and SOCKS5 proxy runs on the router itself, at `127.0.0.1:12334`.

To change the mode:

```bash
uci set hiddify-core.main.mode='proxy'
uci commit hiddify-core
/etc/init.d/hiddify-core restart
```

## Manage the service

| You want to | Command |
|---|---|
| Stop or start it | `/etc/init.d/hiddify-core stop` / `start` |
| Restart it after a change | `/etc/init.d/hiddify-core restart` |
| Turn it off at boot | `/etc/init.d/hiddify-core disable` |
| See the log | `logread -e hiddify-core` |
| Update to the newest version | run the installer of step 1 again |
| Remove it | `apk del hiddify-core` (or `opkg remove hiddify-core`) |

The package keeps its settings when you upgrade OpenWrt itself (sysupgrade). Every option of Hiddify Core is explained in [Hiddify Core](../core/index.md) and the [command-line reference](../core/cli.md).

## Related articles

- [Free internet for every device behind an OpenWrt router](How-to-Enable-Free-Internet-Access-for-Clients-Behind-an-OpenWrt-Router-Using-HiddifyCli.md)
- [Hiddify Core](../core/index.md) and its [command-line reference](../core/cli.md)
- [Router mode on Linux](Router-mode-on-Linux.md): the same idea on a Linux gateway, with the Hiddify app

