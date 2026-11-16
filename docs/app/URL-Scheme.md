---
title: URL scheme in Hiddify app
---

# URL scheme and subscription format of the Hiddify app

This page is for people who make subscription links, panels or bots for the Hiddify app: the links that open the app, what a subscription may contain, and the headers and link parameters the app reads.

!!! info "Written for Hiddify app 5.9"
    Everything on this page was checked against the code of Hiddify app 5.9.2 and the Hiddify Core it ships with.

## Links that open the app { #download-configuration }

When the Hiddify app is installed, a link of this form opens the app and asks the user to add the profile:

```
hiddify://import/<link>#<name>
```

- `<link>` is a subscription link (in any format the app reads, see [below](#subscription-content)) or a single proxy link such as `vless://…`.
- `#<name>` (optional) is the profile name. The app asks the user before it adds a profile from an external link.

Examples:

```
hiddify://import/https://example.com/sub/abc123#My VPN
hiddify://import/trojan://password@example.com:443?security=tls&type=ws&path=%2Fws#Server 1
```

### Other forms the app understands { #deprecated }

These forms are read when the user adds them in the app (from the clipboard or with **Add profile › Manually**). As a link that opens the app, use `hiddify://import/…` above.

```
hiddify://install-sub?url=<URL-encoded link>#<name>
hiddify://install-config?url=<URL-encoded link>#<name>
hiddify://install-proxy?url=<URL-encoded link>#<name>
v2ray://install-config?url=<URL-encoded link>&name=<name>
clash://install-config?url=<URL-encoded link>&name=<name>
sing-box://import-remote-profile?url=<URL-encoded link>#<name>
```

The schemes `hiddify`, `v2ray`, `v2rayn`, `v2rayng`, `clash`, `clashmeta` and `sing-box` all work with a `url=` parameter. A `name=` parameter, when given, is used instead of the `#name` part. A plain `https://…` link may also carry `?name=…`.

### Sharing routing rules { #routing-rules }

In **Settings › Routing**, the ⋮ menu has **Copy rules to clipboard**. It copies a link of this form:

```
hiddify:///settings/routing-options?routeRule=<base64 of the rules as JSON>
```

Opening it on another device opens **Routing** and, after a warning ("Import route rule?"), adds the rules.

## What a subscription may contain { #subscription-content }

The content of a subscription link (or of a file the user imports) can be:

- **Share links**, one per line, plain or as one base64 block. The core reads: `vless`, `vmess`, `trojan`, `ss`, `ssconf`, `tuic`, `hysteria`, `hysteria2` (`hy2`), `ssh`, `naive` (`naive+https`, `naive+quic`), `anytls`, `snell`, `mieru` (`mierus`), `socks`, `http`/`https` (also `phttp`/`phttps`), `wg`/`wireguard`/`awg`, `warp`, `psiphon`, `tor`, `ovpn`, `dnstt`, `dnst`, `masterdns`, `soar`, `slipnet`, `masque`, `aether` and `direct`. The `x` prefix (`xvless://`, `xvmess://`, `xtrojan://`) runs a link with the Xray core, and the `s` prefix (`svless://`, …) with sing-box.
- **A sing-box JSON config**, a **Clash / mihomo YAML config**, an **Xray JSON config**, a **WireGuard `.conf`** file or an **OpenVPN `.ovpn`** file.
- **Other subscription links**: a line with an `http(s)://` address that has a path is downloaded, and its content takes the place of the line. A line that fails to download is dropped.

Example of share links:

```
#profile-title: My VPN
vless://11111111-2222-3333-4444-555555555555@example.com:443?security=tls&sni=example.com&type=ws&path=%2Fws#WebSocket TLS
hysteria2://password@example.com:443?sni=example.com&obfs=salamander&obfs-password=secret#Hysteria2
tuic://11111111-2222-3333-4444-555555555555:password@example.com:443?alpn=h3&congestion_control=bbr&sni=example.com#TUIC
```

## Profile name { #profile-title }

The app uses the first of these that is not empty:

1. A name the user typed when editing the profile.
2. The `profile-title` header.
3. The file name in the `content-disposition` header.
4. The `#name` part of the subscription link.
5. The last part of the link, without `.json`, `.yaml`, `.yml` or `.txt`.
6. "Remote Profile".

## Subscription headers { #response-headers }

The server can send these HTTP response headers with the subscription. If you can't set headers (for example a file on GitHub), put them as comments in the **first 10 lines** of the content, starting with `#` or `//`:

```
#profile-title: base64:SSDinaTvuI8gSGlkZGlmeQ==
#profile-update-interval: 12
#subscription-userinfo: upload=455727941; download=6174315083; total=1073741824000; expire=1767225600
#support-url: https://t.me/hiddify
#profile-web-page-url: https://hiddify.com
```

A real HTTP header wins over the same header in the content. The app reads only these headers:

| Header | Value | What the app does |
|---|---|---|
| `profile-title` | text, or `base64:` + UTF-8 text in base64 | The profile name. Use base64 for emoji or non-Latin names: `base64:SSDinaTvuI8gSGlkZGlmeQ==` shows "I ❤️ Hiddify". |
| `content-disposition` | `attachment; filename="name.txt"` or `filename*=UTF-8''<percent-encoded>` | The profile name, when there is no `profile-title`. |
| `profile-update-interval` | hours, a whole number above 0 | How often the app updates the profile, unless the user changed it. |
| `subscription-userinfo` | `upload=…; download=…; total=…; expire=…` | Shows the used and total traffic (bytes) and the days left (`expire` is a Unix time in seconds). `total=0` or no `total` means unlimited; `expire=0` or no `expire` means no expiry. |
| `profile-web-page-url` | a URL | Shows a button that opens your web page (for example the user page). |
| `support-url` | a URL | Shows a support button. |
| `ipinfo-url` | a URL | The address the app uses to show the exit IP and its country. |
| `extra-security` | `psiphon` or `warp` | Turns on [Extra security](Chain-Extra-security-and-Proxy-unblocker.md) through Psiphon or WARP for this profile. The user's own choice in the app wins. |
| `fragment` | `size,sleep,method` or `tlshello,size,sleep` | Turns on TLS fragment for this profile, read like the link parameter [below](#fragment-parameters). The user's own setting wins. |
| `keep-top` | a number, or `-1` | How many of the fastest proxies the app keeps running (default 5). `-1` keeps all. The user's own choice wins. |

!!! note "Not read any more"
    `moved-permanently-to` and `DNS` were read by older versions. Hiddify app 5.9 ignores them.

## Link parameters { #link-parameters }

Besides the usual parameters of each protocol, Hiddify reads these in a share link. Parameter names don't care about case, `_` or `-`: `mux_type`, `mux-type` and `muxtype` are the same.

### TLS fragment { #fragment-parameters }

```
&fragment=<size>,<sleep>,<method>
&fragment=tlshello,<size>,<sleep>
```

`size` is the size of each piece in bytes and `sleep` the pause between pieces in milliseconds, each a number or a range such as `10-100`. All three parts are needed. Example: `&fragment=10-100,100-200,tlshello`. You can also give `fgsize=` and `fgsleep=` on their own. See [How the TLS trick works](/manager/basic-concepts-and-troubleshooting/How-the-TLS-Trick-works-and-its-usage/).

### Other TLS tricks { #tls-tricks-parameters }

- `mc=1`: mixed-case SNI (for example `ExAmPle.com`).
- `padsize=<range>`: adds a padding extension of this many bytes before the SNI, for example `padsize=100-200`. It needs a browser fingerprint (`fp=chrome` or another).

### MUX { #mux-parameter }

| Parameter | Meaning |
|---|---|
| `muxtype` | `smux`, `yamux` or `h2mux`. MUX is on only when this is set. |
| `muxmaxc` | the maximum number of connections |
| `muxsmax` | the maximum number of streams in one connection |
| `mux` | the minimum number of streams in one connection |
| `muxpad` | `true` to add padding (the server must use it too) |
| `muxup`, `muxdown` | upload and download speed in Mbps for TCP Brutal; both are needed |

Example: `&muxtype=h2mux&muxmaxc=4&muxpad=false&muxup=10&muxdown=50`

!!! warning "Old parameter names"
    Older versions of this page wrote `mux=smux`, `mux_max`, `mux_min`, `mux_up` and `mux_down`. The app does not read those names: use the table above.

## Related articles

- [Import, export and reset settings, and edit a profile in the Hiddify app](/app/Import-export-settings-and-edit-profile/)
- [How to use the Hiddify app](/app/How-to-use-Hiddify-app/)
- [Free profiles in the Hiddify app](/app/Free-profiles-in-Hiddify-app/)
