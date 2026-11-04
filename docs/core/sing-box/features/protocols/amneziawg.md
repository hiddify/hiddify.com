# AmneziaWG

[All Hiddify features](../../index.md)

AmneziaWG is WireGuard with obfuscation added. It sends junk packets before the handshake, pads
the handshake messages with random bytes and replaces the fixed WireGuard message types with your
own numbers, so the traffic no longer matches the WireGuard pattern. In a config it is the
endpoint `"type": "awg"`.

## Why use it

Plain WireGuard is easy to detect and block, and many networks do that. If a WireGuard server is
blocked but an AmneziaWG server with the same keys and peers is reachable, use this endpoint. The
server must run AmneziaWG with the same obfuscation values. A plain WireGuard server does not
understand the changed packets.

## How it gets past filtering

DPI recognizes WireGuard by its first packet: a 148-byte handshake initiation that starts with the
message type `1`, answered by a 92-byte response with type `2`. AmneziaWG breaks each part of that
pattern:

- Junk packets of random size go out before each handshake, so the first packet of the flow is not
  the handshake.
- Random bytes before the initiation and response change their sizes.
- Custom message types (h1–h4) replace the values `1`–`4`.
- Optional special packets (i1–i5) let the first packets imitate another protocol, such as a QUIC
  or DNS packet you captured.

It does not hide that the traffic is UDP to one server, and it does not help when all UDP is
blocked or throttled. The encryption is the same as in WireGuard.

## How it works

- The endpoint is a full WireGuard device, built on the
  [AmneziaWG Go library](https://github.com/amnezia-vpn/amneziawg-go) through Hiddify's fork
  (`github.com/hiddifydeveloper/amneziawg-go`).
- Before each handshake initiation it sends the i1–i5 packets (when set), then `jc` junk packets
  with random sizes between `jmin` and `jmax` bytes.
- The initiation gets `s1` random bytes in front of it and the response gets `s2`. The four
  message types are written as `h1`–`h4`.
- Both sides must use the same `s1`, `s2` and `h1`–`h4`, or they cannot read each other's
  packets. `jc`, `jmin`, `jmax` and i1–i5 only affect what one side sends.
- The endpoint can dial out (a client with one peer) and accept peers (set `listen_port`).
  Connections from a peer are routed like any inbound connection.
- When the endpoint has started, Hiddify runs a URL test on it right away.

## Configuration

```json
{
  "endpoints": [
    {
      "type": "awg",
      "tag": "awg-out",
      "private_key": "<base64 private key>",
      "address": ["10.8.0.2/32"],
      "mtu": 1408,
      "awg": {
        "jc": 4,
        "jmin": 40,
        "jmax": 70,
        "s1": 15,
        "s2": 18,
        "h1": "1111111",
        "h2": "2222222",
        "h3": "3333333",
        "h4": "4444444"
      },
      "peers": [
        {
          "address": "203.0.113.10",
          "port": 51820,
          "public_key": "<base64 server public key>",
          "allowed_ips": ["0.0.0.0/0", "::/0"],
          "persistent_keepalive_interval": 25
        }
      ]
    }
  ]
}
```

### Endpoint fields

| Field | Type | Default | Meaning |
|---|---|---|---|
| `private_key` | string | required | Your WireGuard private key, base64. |
| `address` | list of prefixes | required | Addresses of this side inside the tunnel, such as `10.8.0.2/32`. |
| `mtu` | number | `1408` | MTU of the tunnel. |
| `listen_port` | number | random | UDP port to listen on. Set it when peers connect to you. |
| `useIntegratedTun` | bool | `false` | Create a real system TUN interface for the tunnel instead of the built-in user-space network stack. |
| `awg` | object | none | Obfuscation values. See below. |
| `peers` | list | none | The peers. See below. |
| `mtu_discovery` | bool | `true` | Find the MTU that gets through the network and the `detour`, as the [WireGuard endpoint](wireguard-hiddify.md) does: ICMP echo requests of every size through the tunnel, the largest answered becomes the MTU. `false` keeps `mtu`. Not with `useIntegratedTun`. |
| `fallback_address` | list of IPs | none | Other addresses of the only peer, on its port, tried in turn when the one in use gets no handshake, as in the WireGuard endpoint. Needs a single peer given by an IP address. |
| Dialer fields | | | The usual outbound dialer fields, such as `detour` and `bind_interface`. |

### Obfuscation fields (`awg`)

All values must match the server where noted. A value of `0` or `""` leaves that part as in plain
WireGuard.

| Field | Type | Default | Meaning |
|---|---|---|---|
| `jc` | number | `0` | How many junk packets to send before each handshake. |
| `jmin` | number | `0` | Smallest junk packet, in bytes. |
| `jmax` | number | `0` | Largest junk packet, in bytes. Must not be smaller than `jmin`. |
| `s1` | number | `0` | Random bytes in front of the handshake initiation. Must match the server. |
| `s2` | number | `0` | Random bytes in front of the handshake response. Must match the server. `148 + s1` must differ from `92 + s2`. |
| `s3` | number | `0` | Random bytes in front of the cookie reply. Must match the server. |
| `s4` | number | `0` | Random bytes in front of each data packet. Must match the server. |
| `h1` | string | `""` | Message type of the handshake initiation: a number, or a range `"min-max"` from which each packet takes a random value. Must match the server. |
| `h2` | string | `""` | Message type of the handshake response. Must match the server. |
| `h3` | string | `""` | Message type of the cookie reply. Must match the server. |
| `h4` | string | `""` | Message type of data packets. Must match the server. |
| `i1` … `i5` | string | `""` | Special packets sent before each handshake, in order. Each is built from tags, see below. |

The four `h` values must be different from each other, and their ranges must not overlap. Each
is a number from `5` to `4294967295`, or a range of them.

AmneziaWG 3.x adds these settings. A range is a number or `"min-max"`; each use takes a random
value from it.

| Field | Type | Default | Meaning |
|---|---|---|---|
| `header_protection_key` | string | `""` | 64 hex digits. Encrypts the message headers, so the message types cannot be read. Each of `s1`–`s4` must then be at least `12`. Must match the server. |
| `content_padding_addition` | range | | Random bytes added to each data packet. |
| `rekey_after_time` | range | | Seconds before a new handshake. |
| `rekey_timeout` | range | | Seconds to wait for a handshake response before trying again. |
| `reject_after_time` | range | | Seconds after which keys are no longer used. |
| `keepalive_timeout` | range | | Seconds without a packet before a keepalive is sent. |
| `max_handshake_attempts` | range | | Handshake attempts before giving up. |
| `random_trailers` | bool | `false` | Adds random bytes at the end of packets. |
| `disable_cookies` | bool | `false` | Turns off cookie replies under load. |

Empty values keep amneziawg-go's defaults, which match WireGuard's timings.

Each `i` packet is a list of tags joined together, for example `<b 0xc0ffee><r 16><t>`:

| Tag | Adds |
|---|---|
| `<b 0x…>` | These bytes, in hex. |
| `<r N>` | `N` random bytes (at most 1000). |
| `<t>` | The current Unix time, 8 bytes. |
| `<c>` | A packet counter, 8 bytes. |
| `<wt N>` | No bytes; waits `N` milliseconds (at most 5000) before the packet is sent. |

### Masquerade (`ip`, `id`, `ib`)

Instead of writing `i1` by hand, the first decoy packet can be generated. With `"ip": "quic"`,
`i1` becomes a QUIC v1 client Initial for the domain in `id`: a real, decryptable TLS 1.3
ClientHello for that domain with ALPN h3, as a browser opening an HTTP/3 connection sends. It is
built afresh before every handshake, with new connection IDs, random and key share, so a censor
never sees the same blob twice.

```json
"awg": { "jc": 4, "jmin": 40, "jmax": 70, "ip": "quic", "id": "www.google.com" }
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `ip` | string | `""` | The protocol to look like: `quic`, or the name of a [noise preset](warp-scanner.md#noise-presets) such as `sip`, `dns`, `stun`, `random` or `quic-mimic`. |
| `id` | string | `""` | The domain in the decoy. Required with `quic`; a preset has its own. |
| `ib` | string | `""` | The client profile: `chrome`, `firefox` or `curl`, accepted for configs written for sing-box-lx. This build sends one browser-like ClientHello for all of them. |

Any other `ip` names a noise preset: its packets fill `i1`, `i2`, … and its junk fills `jc`,
`jmin` and `jmax` when they are not set, so `"awg": { "ip": "sip" }` alone looks like a VoIP
call setup.

`ip`, `id` and `ib` replace `i1`: a config with both fails to start. `i2`–`i5` still apply.
The server needs no change: it ignores the decoy, as it ignores every `i` packet.

### Peer fields (`peers`)

| Field | Type | Default | Meaning |
|---|---|---|---|
| `address` | string | none | Server IP address or domain. A domain is resolved once at start with the system resolver. |
| `port` | number | none | Server UDP port. |
| `public_key` | string | required | The peer's public key, base64. |
| `preshared_key` | string | none | Optional preshared key, base64. |
| `allowed_ips` | list of prefixes | none | Addresses routed to this peer, and accepted from it. |
| `persistent_keepalive_interval` | number | `0` | Seconds between keepalive packets. `0` turns them off. |
| `name` | string | none | User name for connections from this peer. Stats and `auth_user` rules see this name. |
| `reserved` | 3 bytes | none | Written into bytes 1–3 of each message, where WireGuard has them; Cloudflare WARP reads them as the client id. Write it as `[124, 245, 25]` or base64. It needs `s1`–`s4` at `0`, no `header_protection_key`, `h1`–`h4` from `1` to `255`, and one peer. Received messages have the bytes cleared. |

### Notes

- The endpoint needs the `with_awg` build tag. Hiddify's builds include it. Without it, starting
  the config fails with "Awg is not included in this build, rebuild with -tags with_awg".
- Each AmneziaWG endpoint has its own values, so endpoints in one config can talk to servers
  with different settings.
- If a value is invalid (for example `jmax` smaller than `jmin`, or two `h` values the same), the
  endpoint fails to start and the log names the value.
- WireGuard UDP packets from this endpoint may be fragmented by the system, as with official
  WireGuard. Set `"udp_fragment": false` to turn that off.
- The `warp` endpoint uses this endpoint when its `awg` block has any value set. It then talks to
  Cloudflare WARP with junk packets and the other values you give. Cloudflare's servers run plain
  WireGuard, so changed `s1`–`s4`, `h1`–`h4` or a `header_protection_key` make the handshake
  fail. For WARP, set only the
  values that change what the client sends: `jc`, `jmin`, `jmax` and i1–i5.

## See also

- [WireGuard: Hiddify additions](wireguard-hiddify.md)
- [WARP](warp.md)
