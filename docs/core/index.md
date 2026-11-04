---
title: Core Guide
description: Hiddify Core, the proxy core of the Hiddify app, as a command-line tool for servers, routers and desktops
weight: -18
comments: false
---

# Hiddify Core

Hiddify Core (`hiddify-core`, the `HiddifyCli` binary) is the proxy core that runs inside the
Hiddify app on Android, iOS, Windows, macOS and Linux. You can also run it on its own, from the
command line, on a server, a router (OpenWrt) or a desktop without a screen.

It is built on **hiddify-sing-box**, Hiddify's fork of [sing-box](https://sing-box.sagernet.org/).
Every sing-box config works in it, and it adds many protocols, transports and anti-censorship
features that upstream sing-box does not have. Around this core, hiddify-core adds a config
builder: give it a share link, a subscription or a config in almost any format, and it builds a
complete client config for you, with a local proxy or a TUN, DNS, routing and proxy groups.

!!! info "Hiddify Core at a glance"
    - **Download:** [hiddify-core releases on GitHub](https://github.com/hiddify/hiddify-core/releases), for Linux, Windows and macOS, many processors, and OpenWrt packages.
    - **Source code:** [hiddify-core](https://github.com/hiddify/hiddify-core) and [hiddify-sing-box](https://github.com/hiddify/hiddify-sing-box).
    - **Command-line reference:** [every command and flag](cli.md).
    - **Features of the core:** [Hiddify sing-box features](sing-box/index.md), with a page for each protocol, transport and DNS feature.

## Install

On Linux (Ubuntu, Debian, CentOS, OpenWrt and others), this command finds your system and
processor, installs `/usr/bin/hiddify-core` and sets up a service (systemd, or procd on OpenWrt):

```bash
bash <(curl https://i.hiddify.com/core)
```

The service runs `hiddify-core -D /var/lib/hiddify-core run -c /etc/hiddify-core/config.json`.
Edit `/etc/hiddify-core/config.json`, then restart it with `systemctl restart hiddify-core`
(`/etc/init.d/hiddify-core restart` on OpenWrt).

Other ways:

- **Download by hand:** take the archive for your system from the
  [releases page](https://github.com/hiddify/hiddify-core/releases) and unpack it. On Linux, keep
  the `lib` folder next to `HiddifyCli`. On Windows, run `HiddifyCli.exe` from a terminal.
- **Docker:** `docker pull ghcr.io/hiddify/hiddify-core:latest`, or `docker-compose up -d` in the
  `docker` folder of the repository.

In the examples on this site the binary is called `HiddifyCli`; after the Linux installer it is
`hiddify-core`. Both are the same program.

## Run a config: `run` or `srun` {#run-or-srun}

hiddify-core has two ways to run a config. Pick the one that matches what you have.

| You have | Use | What happens |
|---|---|---|
| Share links (`vless://`, `hy2://`, `wg://`…), a subscription link, a Clash or Xray config, or only the outbounds of a sing-box config | `run` | hiddify-core reads the proxies, builds the rest of the config (local proxy or TUN, DNS, routing, groups) from the Hiddify settings, and runs it |
| A complete sing-box config that must run exactly as written (inbounds, DNS, route and all) | `srun` | hiddify-core runs the config as it is, like `sing-box run`, with every Hiddify feature available |

### `run`: from proxies to a ready client

```bash
# a file of share links, one per line, or a base64 subscription
HiddifyCli run -c links.txt

# a subscription URL; it is updated again when the server sends profile-update-interval
HiddifyCli run -c https://example.com/sub/abc

# only the outbounds of a sing-box config are used
HiddifyCli run -c outbounds.json
```

By default `run` opens a mixed (HTTP and SOCKS5) proxy on `127.0.0.1:12334`, groups the proxies
under a selector with automatic tests, and sends DNS to `1.1.1.1`. Point your browser or system at
that proxy, or let hiddify-core do it:

```bash
# a system-wide VPN (needs root or administrator)
sudo HiddifyCli run -c links.txt --tun

# set the system proxy of the desktop
HiddifyCli run -c links.txt --system-proxy

# your Hiddify app settings (Settings → ⋮ → Export → "Export all options to file")
HiddifyCli run -c links.txt -d hiddify-settings.json
```

`run` accepts all of these as input:

- share links of every protocol the app supports, one per line, plain or base64;
- subscription links, also inside a file next to other links;
- a sing-box JSON config: a whole config (only its `outbounds` and `endpoints` are taken), a list
  of outbounds, or a single outbound;
- a Clash or mihomo YAML config (its `proxies`);
- an Xray JSON config;
- a WireGuard `.conf` file.

With `--full-config`, `run` also keeps the inbounds, DNS and route rules of a sing-box input and
builds its own parts next to them. When the config must run without any change, use `srun`.

### `srun`: a full sing-box config as it is

```bash
HiddifyCli srun -c config.json
```

`srun` is the `run` command of sing-box. It takes a complete config, with your own inbounds, DNS,
route and experimental sections, and adds nothing to it. All sing-box options work, together with
the Hiddify additions: XHTTP, finalmask, WARP, AmneziaWG, DNS tunnels, the balancer and the rest
(see [Hiddify sing-box features](sing-box/index.md)).

```bash
# several files are merged, in the order of their names
HiddifyCli srun -c base.json -c outbounds.json

# every .json file of a folder
HiddifyCli srun -C /etc/hiddify-core/conf.d

# read the config from standard input
cat config.json | HiddifyCli srun -c stdin
```

Send `SIGHUP` to reload the config without stopping (the new config is checked first); `SIGINT`
or `SIGTERM` stop it. `srun` is also the way to run a **server** with hiddify-core, since a server
config is mostly inbounds.

!!! tip "Turn proxies into a full config, then edit it"
    `HiddifyCli parse links.txt -o outbounds.json` converts links to sing-box outbounds, and
    `HiddifyCli build -c outbounds.json -o config.json` builds the full client config that `run`
    would use. Edit `config.json` and run it with `srun`. See the [CLI reference](cli.md).

## How it differs from sing-box, Xray and mihomo {#differences}

| | hiddify-core | sing-box | Xray-core | mihomo |
|---|---|---|---|---|
| Based on | a fork of sing-box 1.15, with Hiddify's additions | — | its own core, from the V2Ray family | a fork of Clash |
| Config format | sing-box JSON | sing-box JSON | Xray JSON | Clash YAML |
| Inputs it reads | share links, subscriptions, sing-box JSON, Xray JSON, Clash and mihomo YAML, WireGuard `.conf` | sing-box JSON | Xray JSON | Clash YAML, and link subscriptions in proxy providers |
| Builds a client config from bare proxies | yes, with `run` (TUN or proxy, DNS, rules, groups) | no, you write the whole config | no, you write the whole config | no, you write the whole config |
| Control API | gRPC (used by the Hiddify app) and the Clash API | Clash API | gRPC | REST (Clash API) |

### Compared with sing-box

hiddify-core runs every sing-box config, and adds:

- **Xray's transports in sing-box:** [XHTTP](sing-box/features/transports/xhttp.md),
  [mKCP](sing-box/features/transports/kcp.md), [XDRIVE](sing-box/features/transports/xdrive.md),
  [finalmask](sing-box/features/transports/finalmask.md), the
  [raw transport](sing-box/features/transports/raw.md),
  [VLESS encryption](sing-box/features/protocols/vless-encryption.md) and
  [multi-segment gRPC paths](sing-box/features/transports/grpc-custom-path.md), so configs made for
  Xray load as they are.
- **More protocols:** [WARP](sing-box/features/protocols/warp.md) with free account registration,
  an [endpoint scanner and noise](sing-box/features/protocols/warp-scanner.md) and
  [MASQUE](sing-box/features/protocols/warp-masque.md);
  [AmneziaWG](sing-box/features/protocols/amneziawg.md);
  [Psiphon](sing-box/features/protocols/psiphon.md); [Mieru](sing-box/features/protocols/mieru.md);
  [Sudoku](sing-box/features/protocols/sudoku.md);
  [TrustTunnel](sing-box/features/protocols/trusttunnel.md);
  [GooseRelay](sing-box/features/protocols/gooserelay.md);
  [Bond](sing-box/features/protocols/bond.md); a [reverse tunnel](sing-box/features/protocols/tunnel.md);
  an [SSH inbound](sing-box/features/protocols/ssh.md); and the
  [legacy WireGuard outbound](sing-box/features/protocols/wireguard-legacy.md) that upstream removed.
- **DNS tunnels** that find working public resolvers by themselves:
  [DNSTT](sing-box/features/protocols/dnstt.md), [MasterDNS](sing-box/features/protocols/masterdns.md)
  and [Soar](sing-box/features/protocols/soar.md), with a shared
  [smart resolver pool](sing-box/features/dns/smart-dns-pool.md).
- **Anti-censorship tricks:** [TLS fragment](sing-box/features/tls-fragment.md),
  [TLS tricks](sing-box/features/tls-tricks.md) (mixed-case SNI, padding) and
  [REALITY additions](sing-box/features/reality-hiddify.md).
- **Groups and monitoring:** a [balancer](sing-box/features/groups/balancer.md) with several
  strategies, a [fallback](sing-box/features/groups/fallback.md) group,
  [URL test additions](sing-box/features/groups/urltest.md),
  [background monitoring](sing-box/features/groups/monitoring.md) of delay and exit IP, and a
  [unified delay](sing-box/features/groups/unified-delay.md) that compares across protocols.
- **DNS:** a [DNS group](sing-box/features/dns/dns-group.md),
  [bypass_if_failed](sing-box/features/dns/dns-bypass-if-failed.md),
  [DNSCrypt stamps](sing-box/features/dns/sdns.md), [sslip.io names](sing-box/features/dns/sslip-hosts.md)
  and [IPv6 by outbound](sing-box/features/dns/ipv6-by-outbound.md).
- **[Bug fixes](sing-box/bugfix/v5.md)** on top of sing-box 1.15, each with its commit.

### Compared with Xray

hiddify-core has Xray's XHTTP, mKCP, finalmask, XDRIVE, raw transport and VLESS encryption
written into sing-box. An Xray-style VLESS outbound can therefore run next to Hysteria2, TUIC,
WireGuard, WARP and the DNS tunnels in one config, under sing-box's TUN, routing, rule sets and
proxy groups. hiddify-core reads Xray JSON configs and Xray share links (including the `extra`
field of XHTTP), and `HiddifyCli parse --xray` converts share links to Xray JSON.

### Compared with mihomo

hiddify-core reads the `proxies` of a Clash or mihomo YAML config and converts them to sing-box,
so a Clash subscription works with `run` without changes. Its groups cover what mihomo users
expect (select, URL test, fallback, load balancing) and add the monitoring and failover described
above. Configs are written in sing-box JSON, not YAML.

## Read more

- [Command-line reference](cli.md): every command and flag of `HiddifyCli`.
- [Hiddify sing-box features](sing-box/index.md): one page per feature, in English and Persian.
- [App considerations](sing-box/app_considerations.md): what app and core developers need to know
  about the v5 core.
- [Using HiddifyCli on OpenWrt](../app/How-to-use-HiddifyCli-on-OpenWrt.md).
