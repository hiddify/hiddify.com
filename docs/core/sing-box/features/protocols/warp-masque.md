# WARP over MASQUE

[All Hiddify features](../../index.md)

WARP over MASQUE connects you to Cloudflare's free WARP VPN with MASQUE, the protocol the
official WARP apps now use. Your IP packets travel inside an HTTP CONNECT-IP request, over
HTTP/3 (QUIC) or HTTP/2 (TLS over TCP). It is an outbound, `"type": "masque"` in the
`outbounds` list, and runs a device enrolled elsewhere: it registers none.

This page is about MASQUE to WARP. The same tunnel runs in two places:

- **The `warp` endpoint with `masque` set** (recommended): one endpoint that registers the
  device, looks up endpoints, and runs WireGuard, AmneziaWG or MASQUE. Its display type is
  `WARP · MASQUE`. See [WARP](warp.md).
- **The `masque` outbound**, described here, which runs the device it is given (`device`) and
  registers none.

For your own MASQUE server, use the `masque-client` and `masque-server` types from upstream
sing-box (RFC 9484 CONNECT-IP, with a path, a username and password, and the usual TLS
settings). They are documented there.

## Why use it

- It works where WireGuard is blocked: the tunnel looks like HTTPS traffic to Cloudflare.
- With `vhttp` set to `auto`, it falls back to HTTP/2 over TCP when UDP or QUIC is blocked.
- Like [WARP](warp.md), it needs no server of your own.

Choose [WARP](warp.md) when WireGuard works on your network. It has less overhead.

## How it gets past filtering

The tunnel is a TLS connection to Cloudflare with the server name
`consumer-masque.cloudflareclient.com`, over QUIC or over TCP. To a filter it looks like any
other HTTPS connection to Cloudflare. Over HTTP/2, the `tls` block can also split the
ClientHello (`fragment`, `record_fragment`).

When HTTP/3 is blocked, `auto` moves to HTTP/2. When an address or port is blocked, the scanner
finds another one that answers.

Limits: a filter that blocks Cloudflare's MASQUE addresses (`162.159.198.0/24` and
`2606:4700:103::/64`) blocks this outbound. The server name is fixed by Cloudflare, so a filter
that blocks that name also blocks it, unless you change `server_name` to one Cloudflare still
accepts.

## How it works

**Device.** The outbound needs `device`: a device Cloudflare enrolled for MASQUE (its key, its
tunnel addresses and the endpoints), as `masque://` share links carry it. It never reaches
Cloudflare's API and never registers a device. A config without `device` fails to load with
"masque outbound needs a device (an enrolled MASQUE key); to register a WARP device, use the warp
endpoint with mode masque".

When Cloudflare refuses the device (a key that was never enrolled, or a device that was deleted),
the tunnel keeps trying, and the outbound reports the refusal as why it is not ready. It does not
register a replacement. The `warp` endpoint with `mode` `masque` takes such a device as
`masque.device` and, once Cloudflare refuses it, goes on with its saved or newly registered
devices; see [WARP](warp.md#how-it-works).

**`masque://` links.** hiddify-core reads a `masque://` link to Cloudflare's WARP (an endpoint in
WARP's ranges or under `cloudflareclient.com`, or Cloudflare's server name, or none) as a `warp`
endpoint with `mode` `masque`, with the link's key as `masque.device`, or with none when the link
has no key. Only a link to another MASQUE server becomes this outbound, and it needs its key.

**HTTP version.** `vhttp` chooses how the tunnel connects:

- `h3`: HTTP/3 over QUIC only.
- `h2`: HTTP/2 over TLS and TCP only.
- `auto`: HTTP/3 starts first. HTTP/2 starts too after 3 seconds, or at once if HTTP/3 fails.
  The first to connect wins, and a late success of the other is closed. Some networks drop QUIC
  without an error, so HTTP/3 would only stall; this keeps the wait short.

In `auto`, an HTTP/2 win is remembered so the next connects go straight to HTTP/2. It is
remembered for 1 second, then 10 seconds, 30 seconds, 5 minutes and 10 minutes, one step longer
for each HTTP/2 win in a row. An HTTP/3 win starts over. This way a short HTTP/3 refusal doesn't
keep the tunnel on HTTP/2 for good. If the remembered HTTP/2 fails, the next connect tries HTTP/3
first again.

**Endpoints.** Without the scanner, the tunnel uses the profile's HTTP/3 endpoint and
`162.159.198.2` for HTTP/2, on port 443, or on the port a `device` endpoint was given with.

**Scanner.** With `scanner.enabled`, the outbound looks for an endpoint that answers before it
connects. The scanner works as in [WARP](warp.md#how-it-works), with these differences:

- A probe is the handshake the tunnel starts with: a QUIC handshake for HTTP/3, or a TLS
  handshake over TCP for HTTP/2. It uses the tunnel's TLS settings and the outbound's dialer.
- HTTP/3 and HTTP/2 endpoints are different servers, so they are scored apart. In `auto`, both
  are scanned.
- The default ranges are what Cloudflare serves. Over QUIC only `162.159.198.1`,
  `162.159.198.2`, `2606:4700:103::1` and `2606:4700:103::2` answer. Over HTTP/2 all of
  `162.159.198.0/24` and `2606:4700:103::/64` answer, except the first address. The default
  ports are 443, 500, 1701, 4443, 4500, 8095 and 8443. UDP 443 is often blocked, so the HTTP/3
  scan mostly searches the ports.
- With `use_ipv6`, only IPv6 endpoints are scanned.

**Failover.** Each connect of the tunnel counts for its endpoint: a success adds to its score, a
failure takes from it. After two failed connects in a row on one HTTP version, the tunnel scans
for the best other endpoint of that version and switches to it. If none answers, it keeps the
current one.

**Network change.** After a network change, the outbound names the new network (for the scores)
and drops the tunnel connection. The next use connects again.

**Connected state.** The outbound counts as connected (no "Connecting...") only while it has a
connection to Cloudflare's server, not as soon as it is set up; when the connection drops,
through a detour or otherwise, it shows as connecting until it reconnects. Its display type is
`WARP · MASQUE`, with the scanner status after it as for [WARP](warp.md).

**Group detour.** When `detour` is a group, the tunnel reconnects when the group moves to
another member.

**Through a proxy.** QUIC reads each packet into a buffer of about one packet. A proxy that
decrypts in place, like Shadowsocks, needs more room, so each packet is read whole from a
proxy's packet connection and then copied. Before, a full packet was cut off and the HTTP/3
tunnel never connected through Shadowsocks, VLESS or Trojan.

## Configuration

```json
{
  "outbounds": [
    {
      "type": "masque",
      "tag": "warp-masque",
      "vhttp": "auto",
      "device": {
        "private_key": "MHcCAQEEI...",
        "ipv4": "172.16.0.2",
        "endpoint_v4": "162.159.198.2:443"
      },
      "scanner": {
        "enabled": true
      }
    }
  ],
  "route": {
    "final": "warp-masque"
  }
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `device` | object | required | A device already enrolled for MASQUE, used as is: no call to Cloudflare's API. See below. |
| `vhttp` | string | `auto` | `h3`, `h2` or `auto`. Empty means `auto`, or `h2` when `use_http2` is on. |
| `use_http2` | bool | `false` | Older way to choose HTTP/2. `vhttp` takes priority. |
| `server_name` | string | `consumer-masque.cloudflareclient.com` | TLS server name. |
| `use_ipv6` | bool | `false` | Connect to Cloudflare over IPv6. The profile has no IPv6 HTTP/2 endpoint, so `auto` uses HTTP/2 only when the scanner finds one and otherwise stays on HTTP/3; `h2` needs the scanner. |
| `scanner` | object | off | Endpoint scanner and failover. Same fields as in [WARP](warp.md#scanner). |
| `tls` | object | | TLS settings. See below. |
| `udp_timeout` | duration | sing-box default | Idle timeout of UDP sessions in the tunnel. |
| `udp_keepalive_period` | duration | `30s` | QUIC keepalive period. |
| `udp_initial_packet_size` | number | QUIC default | QUIC initial packet size. When set, path MTU discovery is off. |
| `mtu` | number | `1280` | MTU of the tunnel, `1280` to `9000`. Over HTTP/3, a packet larger than the path carries gets an ICMP "packet too big" back, so TCP adjusts to it. |
| `reconnect_delay` | duration | `0` | Wait between failed connects of the tunnel. |
| `unique_identifier` | string | the tag | Key of the scanner scores in the cache file. |

Dial fields (`detour`, `bind_interface` and the rest) apply to the tunnel, the scanner probes
and the network name check.

### `device`

A device enrolled elsewhere, as `masque://` share links carry it. Cloudflare's API is not reached, so it works where the API is blocked; the keys must belong to a device that Cloudflare enrolled for MASQUE.

| Field | Type | Default | Meaning |
|---|---|---|---|
| `private_key` | string | | The device's ECDSA key: base64 (standard or URL) of SEC 1 or PKCS #8 DER. |
| `endpoint_public_key` | string | the edge's | The endpoint's key: PEM, or base64 of PKIX DER. Cloudflare's MASQUE edge presents one fixed certificate on every endpoint and port, and its key is built in, so links that carry no key (MahsaNG's) still pin the endpoint. |
| `ipv4`, `ipv6` | string | | Tunnel addresses. At least one. |
| `endpoint_v4`, `endpoint_v6` | string | | HTTP/3 endpoints, an IP or `ip:port`; the port of the first one given is used, 443 without one. At least one. |
| `endpoint_h2_v4`, `endpoint_h2_v6` | string | Cloudflare's | HTTP/2 endpoints. |
| `id`, `license` | string | | The device's ID and license, for information. |

A device that cannot work (a key that does not parse, no address, no endpoint) fails the config.
A device Cloudflare refuses is not replaced; see "How it works". `profile` is no longer read:
the outbound registers no device.

### `scanner` defaults for MASQUE

| Field | Default |
|---|---|
| `ports` | 443, 500, 1701, 4443, 4500, 8095, 8443 |
| `cidrs` | HTTP/3: `162.159.198.1/32`, `162.159.198.2/32`, `2606:4700:103::1/128`, `2606:4700:103::2/128`. HTTP/2: `162.159.198.0/24`, `2606:4700:103::/64`. |

The other scanner fields and their defaults are the same as in [WARP](warp.md#scanner).

### `tls`

| Field | Type | Default | Meaning |
|---|---|---|---|
| `insecure` | bool | `false` | Don't check that the server's key is the one in the profile. |
| `certificate_public_key_sha256` | list of strings | | Check the server by the SHA-256 (hex) of its certificate's public key instead, one of these; Xray's `pinnedPeerPublicKeySha256`. |
| `cipher_suites` | list of strings | | TLS cipher suites to offer. |
| `curve_preferences` | list of strings | | Key exchange curves to offer. |
| `fragment` | bool | `false` | Split the ClientHello into TCP segments (HTTP/2). |
| `fragment_fallback_delay` | duration | | As in a TLS block's `fragment_fallback_delay`. |
| `record_fragment` | bool | `false` | Split the ClientHello into TLS records (HTTP/2). |
| `kernel_tx`, `kernel_rx` | bool | `false` | Use kernel TLS. Linux only. |

Notes:

- The outbound needs the `with_masque` build tag. It is in the default tags of the Makefile.
  Without it, the config fails to load with "MASQUE outbound is not included in this build".
- The scanner scores live in the cache file, under `unique_identifier` or the tag. Without
  `cache_file`, the scanner starts with no history.
- The tunnel starts in the background. Connections wait for the first start to finish. If it
  failed, they fail with "tunnel not initialized".
- When a connect fails, the tunnel logs the error and tries again after `reconnect_delay`.

## See also

- [WARP](warp.md)
