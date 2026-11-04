# WARP scanner and noise

[All Hiddify features](../../index.md)

How a [WARP](warp.md) endpoint finds a way through a network that blocks it: the **endpoint
scanner** looks for a Cloudflare address and port that answers, **noise** sends a few decoy
packets before each WireGuard handshake, the **noise search** tries ready-made noises when the
configured one gets no answer, and **auto mode** races WireGuard, AmneziaWG and MASQUE. This page
explains how they work together. The fields are listed on the [WARP](warp.md) page.

## Why use it

- Many filters block WARP by the first packets of a flow: a WireGuard handshake initiation is
  easy to recognise (fixed size, fixed first bytes). Noise changes what the flow starts with.
- Filters block some Cloudflare addresses or ports and not others; the scanner finds one that
  works and remembers it for each network.
- A noise that works on one network can fail on another. The noise search finds one that works on
  the network you are on, and remembers it too.
- Auto mode does the same for the tunnel: on a network where UDP is throttled MASQUE may win,
  elsewhere WireGuard.

## How it gets past filtering

A filter that classifies a UDP flow by its first packets sees something else first:

| Noise | What the filter sees first |
|---|---|
| random (default) | short packets that start like a QUIC long header, then random bytes |
| `raw` | random bytes of random sizes, no structure at all |
| `quic` | a real QUIC version 1 Initial, with a TLS ClientHello for `www.google.com` |
| `packets` | whatever the templates build: a DNS query, a SIP request, a QUIC packet |

The WireGuard handshake follows in the same flow. A filter that only looks at the start lets it
through; one that keeps watching the whole flow can still find WireGuard, and then MASQUE (HTTPS
to Cloudflare) is the way out.

## How it works

### Noise modes

The noise of the `wireguard` and `warp` endpoints (`noise.fake_packet`) is sent before each
handshake initiation, `count` packets with a random `delay` between them:

- **Default mode** (no `mode`): each packet is one byte from `header` (or none), the bytes
  `00 00 00 01 08`, 8 random bytes, `00 00 44 D0`, then `size` random bytes. This came from
  GFW-knocker; it starts like a QUIC long header.
- **`raw`**: `size` random bytes, nothing else. This is Xray's WARP noise (`wnoise=random`) and
  AmneziaWG's junk packets.
- **`quic`**: real QUIC Initials for `sni` (`www.google.com` by default): the first carries the
  ClientHello, the others PING frames, as QUIC retransmissions would.
- **`packets`**: templates sent first, in order, in the AmneziaWG `i1`–`i5` syntax: `<b 0xHEX>`
  bytes, `<r N>` random bytes, `<rc N>` random letters and digits, `<rd N>` random digits, `<t>`
  the Unix time (4 bytes), `<qi SNI>` a QUIC Initial. Then the `count` packets of the mode.

With `awg`, AmneziaWG sends its own noise instead: `i1`–`i5`, then `jc` junk packets of `jmin` to
`jmax` bytes. Cloudflare only accepts standard WireGuard messages, so for WARP the AmneziaWG
headers `h1`–`h4` stay 1–4 and `s1`–`s4` stay 0: only the packets before the handshake change.

### Noise presets

Taken from WARP configs that work (Xray links and AmneziaWG "WG Mimic" configs). Each works as
WireGuard noise and as AmneziaWG settings.

| Preset | Sends before the handshake | Looks like |
|---|---|---|
| `xray-random` | 5 random packets of 5 to 10 bytes, 2 to 5 ms apart | nothing in particular: tiny packets break a size-based fingerprint |
| `quic` | 2 to 4 QUIC Initials for `www.google.com` | the start of an HTTP/3 connection to Google |
| `dns-google` | 3 DNS queries for `google.com` (A, AAAA, HTTPS), each with a random id, then 6 junk packets of 56 to 160 bytes | DNS traffic |
| `dns-cloudflare` | 2 DNS queries for `cloudflare.com` (A, AAAA), then 9 junk packets of 81 to 224 bytes | DNS traffic to Cloudflare |
| `dns-www-cloudflare` | 2 DNS queries for `www.cloudflare.com` (A, AAAA), then 6 junk packets of 43 to 109 bytes | DNS traffic to Cloudflare |
| `quic-mimic` | a recorded QUIC Initial (1,210 bytes: 276 recorded, 934 random) and a short-header packet, then 4 junk packets of 60 to 199 bytes | a QUIC connection |
| `sip` | a SIP `INVITE` and its `100 Trying` answer, then 10 junk packets of 42 to 224 bytes | a VoIP call setup |
| `stun` | 2 STUN Binding Requests, each with a random transaction id, then 4 junk packets of 40 to 120 bytes | a video call or WebRTC client checking its address |

As AmneziaWG settings, a preset's templates become `i1`, `i2`, … and its junk `jc`, `jmin`,
`jmax`; `quic` becomes `<qi www.google.com>` packets. `awg` mode without `awg` settings uses
`dns-google`.

The presets are not only for WARP: any [WireGuard](wireguard-hiddify.md) endpoint takes one
as its noise `mode` (`"mode": "sip"`), and any [AmneziaWG](amneziawg.md) endpoint as its `ip`
(`"ip": "sip"`). `dns` and `random` are short for `dns-google` and `xray-random`.

### Endpoint scanner

With `scanner.enabled`, before it connects WARP probes endpoints (address and port) with a real
WireGuard handshake made with the device's own key, after the same noise the tunnel will send,
through the endpoint's dialer (so `detour` applies). Endpoints are tried in this order: the ones
that worked on this network, by score; then ones that scored well elsewhere; then random addresses
in `cidrs` on `ports`; the lowest scores last. The scan stops when an endpoint with a score of 3 or
more answers, or 4 have answered, and the best is used. Scores (-10 to 10 per endpoint and
network) are kept in the cache file; a network is named by its interface type, country and public
address range. After a network change, and when traffic goes out with no handshake for 3 minutes,
the endpoint in use is probed again and replaced when it no longer answers.

For MASQUE the scanner probes with a TLS handshake to the MASQUE endpoints, over HTTP/3 and HTTP/2
apart.

### Noise search

With `scanner.search_noise`, the scanner also looks for a noise:

1. It scans with the noise that got through on this network before, if any.
2. If no endpoint answers, with the configured noise (`noise`, or the `awg` settings).
3. If still none, with each preset of `noise_presets` (all, in the order above, by default), on at
   most 16 endpoints each: the endpoints known to answer come first, so a few are enough to tell.
4. The first noise that gets an answer is used: the tunnel starts with it, and it is saved for the
   network and tried first there next time.

The probe always sends what the tunnel sends, so a noise that gets the probe through gets the
tunnel through. Each search costs at most the number of presets times 16 probes, run 8 at once.

### Auto mode

With `"mode": "auto"`, WARP has a WireGuard, an AmneziaWG and a MASQUE device of its own, and
starts by racing the three tunnels:

1. One handshake with each at once, to the device's own endpoint: WireGuard with the endpoint's
   `noise`, AmneziaWG with its `awg` settings (or `dns-google`), MASQUE with a TLS handshake. Two
   tries each, within 5 seconds.
2. The fastest that answered becomes the inner tunnel. `WARP · Auto 🔍 Searching...` shows during
   the race, then `WARP · WG`, `WARP · AWG` or `WARP · MASQUE`.
3. The chosen tunnel then runs as in its own mode: the scanner and the noise search apply to it
   (the WireGuard scanner for WireGuard and AmneziaWG, the MASQUE scanner for MASQUE).
4. The chosen tunnel has 20 seconds to connect. An answer to one handshake does not prove that
   the tunnel carries traffic: when it does not connect, the race runs again without it, and when
   every tunnel failed it starts over.
5. When none answered, WireGuard is used, so the scanner and the noise search can still look for
   an endpoint and a noise.
6. When a group `detour` moves to another member, the race runs again: the new proxy may carry
   another tunnel better, or only one (a proxy without UDP, such as SOCKS4, carries MASQUE over
   HTTP/2 only). After a selector the user moved, at once; after a group that moved by itself (a
   URL test, a balancer), at most every 30 seconds, through a new tunnel next to the one in use
   that replaces it only once it connects (see [group detour](warp.md)). A network change
   forgets which tunnels failed.
7. While the endpoint has not been connected for 3 minutes, it races again, at most every 10
   minutes, and moves to another tunnel that answers.

The race uses the configured noise, not the presets: the noise search runs inside the tunnel that
was chosen.

## Configuration

Search endpoints and noise, with auto mode:

```json
{
  "experimental": {
    "cache_file": { "enabled": true, "store_warp_config": true }
  },
  "endpoints": [
    {
      "type": "warp",
      "tag": "warp",
      "mode": "auto",
      "noise": {
        "fake_packet": { "enabled": true, "mode": "quic", "count": "2-4", "delay": "10-30" }
      },
      "scanner": { "enabled": true, "search_noise": true }
    }
  ]
}
```

Only some presets, in this order:

```json
"scanner": { "enabled": true, "search_noise": true, "noise_presets": ["dns-google", "sip", "quic-mimic"] }
```

A DNS-looking noise for plain WireGuard, written by hand:

```json
"noise": {
  "fake_packet": {
    "enabled": true,
    "packets": ["<r 2><b 0x0100000100000000000106676f6f676c6503636f6d00000100010000291000000000000000>"],
    "mode": "raw",
    "count": "6",
    "size": "56-160"
  }
}
```

| Field | Where | Meaning |
|---|---|---|
| `scanner.enabled` | warp | Scan for an endpoint that answers, and fail over. |
| `scanner.search_noise` | warp | Also look for a noise preset that gets through. |
| `scanner.noise_presets` | warp | The presets to try, in order; all when empty. An unknown name is a config error. |
| `noise.fake_packet.mode` | warp, wireguard | `""`, `raw` or `quic`. |
| `noise.fake_packet.packets` | warp, wireguard | Templates sent first, in the AmneziaWG `i1`–`i5` syntax. |
| `mode` | warp | `wg`, `awg`, `masque` or `auto`. |

The other scanner fields (`ports`, `cidrs`, `max_rtt`, `timeout`, `count`, `concurrency`) are on the
[WARP](warp.md) page.

## Notes

- The scores and the noise found are kept in the cache file; without `cache_file`, every start
  scans from nothing.
- The scanner is off when `server` is set.
- Noise does not help against a filter that blocks all UDP, or all of Cloudflare's WARP ranges:
  then auto mode, or `masque` with `vhttp` `auto` (HTTP/2 over TCP), is the way.

## See also

- [WARP](warp.md)
- [WARP over MASQUE](warp-masque.md)
- [WireGuard: Hiddify additions](wireguard-hiddify.md)
- [AmneziaWG](amneziawg.md)
