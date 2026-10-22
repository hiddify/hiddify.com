# How to use WARP in the Hiddify app

This page explains how to use Cloudflare **WARP** in Hiddify App: the easy way (one switch in the settings) and the advanced way (writing your own `warp://` config). Use it if you want a free connection, or if you want to hide your proxy traffic behind WARP.

**WARP** is a free VPN service from Cloudflare. It is based on **WireGuard**, a fast and simple VPN protocol. Hiddify App can create a WARP account for you and add "noise" (extra fake packets) so that WARP traffic is harder for filters to detect and block.

## Before you start

- Install Hiddify App: see [How to install the Hiddify app](How-to-install-Hiddify-app.md).
- For the advanced way, you should already know how to add a profile: see [How to use the Hiddify app](How-to-use-Hiddify-app.md).

## The easy way: turn on WARP in the settings

1. Open `Settings` and then `WARP`.
2. Turn on `Enable WARP`. Read the "Cloudflare WARP consent" message and tap `Agree`.
3. Tap `Generate WARP config`. When it is done, the app shows "Warp config is generated".
4. Choose a `Detour mode`:
    - `Detour proxies through WARP` ("Unblock proxies by WARP"): your proxy server is reached through WARP. Use this if your proxy server's IP is blocked.
    - `Detour WARP through proxies` ("Extra security by WARP"): you connect to your proxy first and then to WARP. Websites see a Cloudflare IP instead of your proxy's IP.
5. Go back to `Home` and connect as usual. When it works, the connect button turns green.

You can also turn WARP on and off from the quick settings on the `Home` page (the sliders button at the top).

The other options on the `WARP` page are `License key` (a WARP+ key, if you have one), `Clean IP` and `Port` (which Cloudflare address to connect to; `auto` by default), and `Noise count`, `Noise mode`, `Noise size` and `Noise delay`. These four noise options work like the `ifp`, `ifpm`, `ifps` and `ifpd` parameters explained below.

!!! tip "Quick test"
    To try a ready-made WARP profile, open [hiddify.com/warp](../warp/index.md) on a device that has Hiddify App and tap the link there.

## The advanced way: write your own WARP config

You can build a `warp://` link yourself and add it to the app like any other config (copy it, then tap `+` and `Clipboard`). The parts of the link are explained below.

### Noise modes (`ifpm`)

There are 6 main modes and 2 advanced modes. Each one adds a fake header (noise) in front of WARP traffic to help it get past filtering.

- `m1`: the header is random.
- `m2`: the header is random and stays the same, with no trace of WireGuard or WARP in it.
- `m3`: the header uses the QUIC protocol.
- `m4`: the header uses QUIC and stays the same, with no trace of WireGuard or WARP in it.
- `m5`: the header uses LQUIC.
- `m6`: the header uses LQUIC and stays the same, with no trace of WireGuard or WARP in it.
- `h_HEX`: an advanced mode. You choose the first byte of the fake packet as a hex number (from `00` to `FF`). For example, `ifpm=h_30` makes every fake packet start with `0x30`.
- `g_HEX_HEX…`: an advanced mode. The app picks one of the hex bytes you list at random each time. For example, `ifpm=g_10_20_30` uses `0x10`, `0x20` or `0x30`.

!!! tip "Tip"
    The recommended mode is `m4`. It is also the app's default.

### Number, size and delay of noise packets

Each of these is a range (`min-max`). Each time, the app picks a random value inside the range.

- `ifp`: how many noise packets to send. For example, `ifp=40-80` sends between 40 and 80 noise packets.
- `ifps`: the size of each noise packet, in bytes. For example, `ifps=40-100` makes each packet between 40 and 100 bytes.
- `ifpd`: the delay between noise packets, in milliseconds. For example, `ifpd=4-8` waits between 4 and 8 ms. Smaller delays usually work better.

### Which Cloudflare IP to use

- `auto4`: Cloudflare gives the config an IPv4 address automatically.
- `auto6`: Cloudflare gives the config an IPv6 address automatically.
- `auto`: Cloudflare can give either an IPv4 or an IPv6 address.
- A clean IPv4 address: type it directly. For example: `188.114.97.170`
- A clean IPv6 address: put it inside `[]`. For example: `[2a01:4ef:f0:10a5::1]`

A **clean IP** is a Cloudflare IP address that is not blocked on your network.

!!! tip "Tip"
    You can find clean IPs with a scanner, for example: [CFScanner](https://github.com/MortezaBashsiz/CFScanner), [Quick WARP on WARP](https://github.com/azavaxhuman/Quick_WARP_on_WARP), [Ptechgithub WARP](https://github.com/Ptechgithub/WARP). These are community tools, not made by Hiddify.

### Name of the config

To give the config a name, add `#` and the name at the end. The name must be one word (no spaces). For example:

```text
warp://auto#NAME
```

### WARP in WARP (WoW)

You can chain two WARP connections: you connect to the first WARP, and from there to the second one. Websites then see the IP of the second WARP. Add `&&detour=` after the first WARP config, followed by the second one. For example:

```text
warp://auto&&detour=warp://auto
```

### Putting it all together

The general form of a WARP config is:

```text
warp://License@IP:port?ifp=n1-n2&ifps=s1-s2&ifpd=d1-d2&ifpm=mode#name
```

Example:

```text
warp://auto?ifp=40-80&ifps=40-100&ifpd=4-8&ifpm=m4#m4
```

This adds a WARP config named `m4` to the app.

You can also chain two WARPs. For example:

```text
warp://auto?ifp=40-80&ifps=40-100&ifpd=4-8&ifpm=m4#m4&&detour=warp://188.114.97.170:894?ifp=40-80&ifps=40-100&ifpd=4-8&ifpm=m3#m3
```

This adds a config named `m4` that goes through a second WARP (WARP in WARP) named `m3`.

For more examples, see the official sample files [warp](https://raw.githubusercontent.com/hiddify/hiddify-app/refs/heads/main/test.configs/warp) and [warp2](https://raw.githubusercontent.com/hiddify/hiddify-app/refs/heads/main/test.configs/warp2).

!!! tip "Final tips"
    - Use one of the scanners above to find a clean IP that works on your network, then build your config with the formula above.
    - If it does not connect, change the ranges (`ifp`, `ifps`, `ifpd`) or try another mode, and test again.
