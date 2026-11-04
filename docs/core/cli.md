---
title: Command-line reference
description: Every command and flag of HiddifyCli, the hiddify-core command line
weight: -10
---

# HiddifyCli command-line reference

`HiddifyCli` (installed as `hiddify-core` by the Linux installer) is the command line of
[Hiddify Core](index.md). This page lists every command and flag. `HiddifyCli help` and
`HiddifyCli <command> --help` print the same list from the program itself.

```text
HiddifyCli [global flags] <command> [flags]
```

## Global flags

These work with every command.

| Flag | Default | Meaning |
|---|---|---|
| `-D`, `--directory <dir>` | current folder | Working folder. It is created if missing, and relative paths (configs, `data/`, `tmp/`) are read from it. |
| `--disable-color` | off | Print logs without colors. |
| `-h`, `--help` | | Help for any command. |

## Commands at a glance

| Command | What it does |
|---|---|
| [`run`](#run) | Run share links, a subscription or the proxies of a config, with a client config built around them |
| [`srun`](#srun) | Run a complete sing-box config as it is |
| [`parse`](#parse) | Convert links or any config format to sing-box outbounds (or to Xray JSON) |
| [`build`](#build) | Build the full client config that `run` would use, without running it |
| [`instance`](#instance) | Start a small test instance with a SOCKS port and ping through it |
| [`health`](#health) | Test DNS, HTTP or QUIC through a proxy |
| [`speedtest`](#speedtest) | Measure download, upload, ping and jitter through a proxy |
| [`warp`](#warp) | Register a free WARP account and print its WireGuard outbound |
| [`vlessenc`](#vlessenc) | Make a VLESS encryption key pair |
| [`version`](#version) | Print the versions and build details |
| [`admin_bgservice`](#admin_bgservice) | Manage the background service the desktop app uses for VPN mode |
| [`grpcweb`](#grpcweb) | A small web page to start and control the core from a browser |
| [`extension`](#extension) | A test server for Hiddify extensions |
| [`ezytel`](#ezytel) | A viewer for public Telegram channels |
| [`gen-cert`](#gen-cert) | Make TLS certificates for the core's gRPC server |
| [Developer commands](#developer-commands) | `gen`, `profile`, `command` |
| `completion` | Print a shell completion script (bash, zsh, fish, powershell) |

## run

```text
HiddifyCli run -c <file or URL> [flags]
```

Reads proxies from the input, builds a complete client config from the Hiddify settings, and runs
it until you press Ctrl+C. See [Run a config](index.md#run-or-srun) for when to use
`run` and when to use `srun`.

The input can be:

- a file of share links (one per line, plain or base64), which may also hold subscription links;
- an `http://` or `https://` subscription link. When the server sends a `profile-update-interval`
  header (or the body has a `#profile-update-interval:` line), the subscription is fetched again
  every that many hours and the core restarts if it changed;
- a sing-box JSON config, a list of outbounds or one outbound. Only `outbounds` and `endpoints` are
  taken, unless `--full-config` is given;
- a Clash or mihomo YAML config, an Xray JSON config, or a WireGuard `.conf` file.

While it runs, the core's gRPC server listens on `127.0.0.1:17078` and the Clash API on
`127.0.0.1:16756` (`0.0.0.0:16756` when `allow-connection-from-lan` is set in the settings file).

### Flags of `run`, `build` and `instance` {#run-flags}

| Flag | Default | Meaning |
|---|---|---|
| `-c`, `--config <path or URL>` | required | The proxies: a file, or a subscription URL (`run` only). |
| `-d`, `--hiddify <file>` | | A Hiddify settings JSON file (see [below](#settings-file)). When given, the file decides every setting and the flags below are ignored. |
| `--full-config` | off | Keep the inbounds, DNS and route rules of a sing-box input, next to the ones hiddify-core builds. |
| `--tun` | off | Capture all traffic of the system with a TUN (a system-wide VPN). Needs root or administrator. |
| `--tun-service` | off | Use the Hiddify background service for the TUN, as the desktop app does. |
| `--system-proxy` | off | Set the system proxy of the desktop to the local proxy. |
| `--in-proxy-port <port>` | `12334` | Port of the local mixed (HTTP and SOCKS5) proxy. |
| `--dns-remote <server>` | `1.1.1.1` | DNS server used through the proxy: `1.1.1.1`, `tcp://…`, `tls://…`, `https://…/dns-query`. |
| `--dns-direct <server>` | `1.1.1.1` | DNS server used for direct connections. |
| `--fragment` | off | Turn on [TLS fragment](sing-box/features/tls-fragment.md). |
| `--fragment-size <range>` | `2-4` | Size of each fragment in bytes. |
| `--fragment-sleep <range>` | `2-4` | Pause between fragments in milliseconds. |
| `--padding` | off | Add a TLS padding extension ([TLS tricks](sing-box/features/tls-tricks.md)). |
| `--padding-size <range>` | `1300-1400` | Size of the padding. |
| `--mixed-sni-case` | off | Send the server name in mixed upper and lower case. |
| `--log`, `--log-level <level>` | `warn` | `trace`, `debug`, `info`, `warn`, `error`, `fatal` or `panic`. |
| `--web-port <port>` | `6756` | Clash API port written by `build`. `run` always uses `16756`. |
| `--web-secret <secret>` | | Clash API secret written by `build`. |

Examples:

```bash
HiddifyCli run -c links.txt
HiddifyCli run -c https://example.com/sub/abc --in-proxy-port 1080 --log info
sudo HiddifyCli run -c links.txt --tun --dns-remote https://1.1.1.1/dns-query
HiddifyCli run -c links.txt --fragment --fragment-size 10-100 --fragment-sleep 50-200
HiddifyCli run -c sing-box.json --full-config
HiddifyCli -D /var/lib/hiddify-core run -c /etc/hiddify-core/config.json -d settings.json
```

### The Hiddify settings file {#settings-file}

`-d` takes the settings of the Hiddify app as JSON. In the app, open Settings, tap the ⋮ menu
and choose Export → "Export all options to file" ("Export anonymous options to file" leaves out
private values). Settings missing from the file are not filled from the defaults, so start from
an exported file. The main keys:

| Key | Meaning |
|---|---|
| `log-level` | Log level. |
| `enable-full-config` | Same as `--full-config`. |
| `mixed-port`, `tproxy-port`, `redirect-port`, `direct-port` | Local ports; `enable-mixed-port` and the like turn each on or off. |
| `enable-tun`, `enable-tun-service`, `set-system-proxy` | VPN and system proxy, as the flags. |
| `tun-implementation`, `mtu`, `strict-route`, `auto-redirect` | TUN stack and options. |
| `allow-connection-from-lan`, `lan-sharing-port`, `lan-sharing-password` | Share the connection with the local network. |
| `remote-dns-address`, `direct-dns-address`, `remote-dns-domain-strategy`, `direct-dns-domain-strategy`, `enable-fake-dns`, `independent-dns-cache` | DNS. |
| `ipv6-mode`, `bypass-lan`, `block-quic`, `resolve-destination`, `region`, `block-ads`, `route-rule` | Routing. |
| `connection-test-url`, `connection-test-urls`, `url-test-interval`, `ipinfo-url` | Proxy tests. |
| `balancer-strategy`, `default-proxy`, `keep-top`, `keep-tags` | Which proxy is used and how many run. |
| `tls-tricks` | `enable-fragment`, `fragment-size`, `fragment-sleep`, `mixed-sni-case`, `enable-padding`, `padding-size`. |
| `mux` | `enable`, `padding`, `max-streams`, `protocol`. |
| `warp`, `warp2` | WARP settings. |
| `extra-security`, `unblocker`, `chain-status` | Chain a proxy through WARP, Psiphon or another profile. |
| `enable-clash-api`, `clash-api-port`, `web-secret` | Clash API. |

## srun

```text
HiddifyCli srun -c <file> [-c <file>…] [-C <folder>…]
```

Runs a complete sing-box config without changing it, like `sing-box run`. Every Hiddify addition
to sing-box is available ([features](sing-box/index.md)).

| Flag | Meaning |
|---|---|
| `-c`, `--config <path>` | A config file. Repeat it to merge several files; they are merged in the order of their paths. `stdin` reads the config from standard input. |
| `-C`, `--config-directory <dir>` | Read every `.json` file of a folder. Can be repeated. |

Signals: `SIGHUP` checks the config and reloads it without stopping (a broken config is reported
and the running one stays); `SIGINT` and `SIGTERM` stop it.

```bash
HiddifyCli srun -c config.json
HiddifyCli srun -c base.json -c outbounds.json
HiddifyCli srun -C /etc/hiddify-core/conf.d
HiddifyCli -D /var/lib/hiddify-core srun -c /etc/hiddify-core/server.json
```

## parse

```text
HiddifyCli parse <file> [-o <file>] [--xray]
```

Reads a file in any format `run` understands and prints the proxies as sing-box JSON
(`outbounds` and `endpoints`), then checks the result. Subscription links inside the file are
fetched. Use it to see how a link is understood, or as the first step of a hand-made config.

| Flag | Meaning |
|---|---|
| `-o`, `--output <file>` | Write the result to a file (relative to `-D`) instead of the screen. |
| `--xray` | Convert share links to Xray JSON instead, with libxray. |

```bash
HiddifyCli parse links.txt
HiddifyCli parse clash.yaml -o outbounds.json
HiddifyCli parse links.txt --xray -o xray.json
```

## build

```text
HiddifyCli build -c <sing-box json> [-d <settings>] [flags] [-o <file>]
```

Builds the full client config, the one `run` would start, from sing-box outbounds and the
Hiddify settings, and prints it. The input must be sing-box JSON; convert other formats with
`parse` first. It takes the [flags of `run`](#run-flags) and:

| Flag | Meaning |
|---|---|
| `-o`, `--output <file>` | Write the result to a file (relative to `-D`) instead of the screen. |

```bash
HiddifyCli parse links.txt -o outbounds.json
HiddifyCli build -c outbounds.json --tun -o config.json
HiddifyCli srun -c config.json
```

## instance

```text
HiddifyCli instance -c <file> [flags]
```

Starts a small instance of the given proxies with a SOCKS5 port, pings Cloudflare through it a
few times, prints the SOCKS address and waits for Ctrl+C. Useful to test a config quickly. Takes the
[flags of `run`](#run-flags).

## health

```text
HiddifyCli health [target] [flags]
```

Checks connectivity to a target (default `google.com`), directly or through a SOCKS proxy. With
none of `--dns`, `--http`, `--quic`, it tests HTTP.

| Flag | Default | Meaning |
|---|---|---|
| `--proxy <url>` | direct | Proxy to test through: `socks://[user:pass@]host:port`. |
| `--dns` | off | Resolve the target. |
| `--http` | off | Fetch the target over HTTP on TCP. |
| `--quic` | off | Open a QUIC connection over UDP. |
| `--dns-server <addr>` | `1.1.1.1:53` | DNS server: `host:port`, `udp://host:port` or `tcp://host:port`. |
| `--timeout <duration>` | `15s` | Time limit of each check. |
| `-v`, `--verbose` | | Debug logs; `-vv` for more. |

```bash
HiddifyCli health --proxy socks://127.0.0.1:12334 --dns --http --quic cloudflare.com
```

## speedtest

```text
HiddifyCli speedtest [flags]
```

Runs a speedtest.net test, directly or through a SOCKS proxy.

| Flag | Default | Meaning |
|---|---|---|
| `--proxy <url>` | direct | `socks://[user:pass@]host:port`, or just `host:port`. |
| `--distance <km>` | `2000` | Distance of the test server to pick. |
| `--no-download` | off | Skip the download test. |
| `--no-upload` | off | Skip the upload test. |
| `--no-ping` | off | Skip the ping test (and jitter). |
| `--no-jitter` | off | Do not print jitter. |
| `-v`, `--verbose` | | Debug logs; `-vv` for more. |

```bash
HiddifyCli speedtest --proxy 127.0.0.1:12334
```

## warp

```text
HiddifyCli warp
```

Registers a new free Cloudflare WARP account and prints a sing-box WireGuard outbound for it.
The Hiddify way to use WARP in a config is the [`warp` endpoint](sing-box/features/protocols/warp.md),
which registers by itself.

## vlessenc

```text
HiddifyCli vlessenc [--json]
```

Makes a new key pair for [VLESS encryption](sing-box/features/protocols/vless-encryption.md)
(`mlkem768x25519plus`): the `decryption` value for the server and the `encryption` value for the
client. `--json` prints them as JSON.

## version

```text
HiddifyCli version [-n]
```

Prints the hiddify-core and hiddify-sing-box versions, Go version, system, build tags, commit and
whether CGO is on. `-n`, `--name` prints only the sing-box version name.

## admin_bgservice

```text
HiddifyCli admin_bgservice <action> [argument]
```

Also called `tunnel`. The desktop app (Windows, macOS, Linux) runs VPN mode through a background
service with administrator rights; this command manages it. You do not need it to run a config
yourself.

| Action | Meaning |
|---|---|
| `install [owner]` | Install the service. On Linux the owning user can be given. |
| `uninstall` | Remove the service. |
| `start`, `stop` | Start or stop the service. |
| `run` | Run the service in the foreground. |
| `activate`, `deactivate` | Turn the service's VPN on (with IPv6, mixed port 12334) or force it off. |
| `connect <request.json>` | Ask the service to connect with a request file. |
| `disconnect` | Ask the service to disconnect. |
| `exit` | Ask the service to exit. |
| `build-id` | Print the build ID, which the app compares with the running service. |

## grpcweb

```text
HiddifyCli grpcweb [flags]
```

Starts a core and serves a small HTML page and the core's gRPC API on the same port, to start,
stop and choose proxies from a browser. Open `http://127.0.0.1:18088`.

| Flag | Default | Meaning |
|---|---|---|
| `--listen <addr>` | `0.0.0.0:18088` | Address of the page and of the gRPC API. |
| `--workdir <dir>` | a temporary folder | Working folder of the core. |
| `--config <path>` | | Config path shown in the page. |
| `--mixed-port <port>` | `12334` | Local proxy port of the core it starts. |
| `--connect` | off | Start no core; control the one at `--grpc`. |
| `--grpc <addr>` | | gRPC address of the core to control, with `--connect`. |

## extension

```text
HiddifyCli extension
```

Starts a test server for [Hiddify extensions](https://github.com/hiddify/hiddify-app-example-extension),
so you can try an extension's interface in a browser at `https://127.0.0.1:12346`.

## ezytel

```text
HiddifyCli ezytel <command> [flags]
```

Reads public Telegram channels through their web preview, as the app's channel viewer does.

| Command | Flags | Meaning |
|---|---|---|
| `info` | `--channel <id>`, `--last-read <post id>`, `--disable-inline-images`, `--json` | The channel's details, with the unread count after `--last-read`. |
| `messages` | `--channel <id>`, `--before <post id>`, `--disable-inline-images`, `--html-only`, `--json` | The channel's messages as HTML, page by page. |
| `proxy-image` | `--hex <url>`, `-o <file>`, `--json` | Download an image of a post. |
| `parse-channels` | `--raw <text>`, `-f <file>`, `--json` | Read a list of channels, one per line. |
| `serve` | `--listen <addr>` (default `127.0.0.1:17079`) | Run the viewer's gRPC server. |

All of them take `--cache-dir <dir>` (default: a folder in the system's temporary folder).

```bash
HiddifyCli ezytel messages --channel hiddify --html-only
```

## gen-cert

```text
HiddifyCli gen-cert
```

Makes a server and a client certificate for the core's gRPC server in `data/cert/`
(`server-cert.pem`, `server-key.pem`, `client-cert.pem`, `client-key.pem`).

## Developer commands

These are for developing hiddify-core and may change:

- `gen <file>`: build a config the way the app does and log it at debug level.
- `profile <url>`: add a profile from a URL, as the app does, and print the result.
- `command`: connect to a running core's gRPC API (`127.0.0.1:17078`) and print its status,
  outbounds and logs.
