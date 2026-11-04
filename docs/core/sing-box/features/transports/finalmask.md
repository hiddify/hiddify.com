# finalmask

[All Hiddify features](../../index.md)

`finalmask` applies Xray-core's finalmask masks to the connections an outbound opens. A mask
changes the bytes on the wire: it splits them, adds noise packets, adds headers, or wraps them in
another protocol (DNS, ICMP, a Minecraft-like stream and more). It is the `finalmask` field of the
dial fields, so you can set it on any outbound that dials (and on DNS servers and other places that
take dial fields). The JSON is the same as Xray's `streamSettings.finalmask`.

## Why use it

- To use an Xray server that is set up with finalmask masks: the client must apply the same
  masks, or the server cannot read the traffic.
- To change how a connection looks on the wire without changing the protocol: split the TLS
  ClientHello (`fragment`), send junk UDP packets before a WireGuard or QUIC handshake (`noise`),
  or obfuscate UDP with a password (`salamander`).

## How it gets past filtering

Filters match on the first bytes and packets of a connection, their sizes and their timing.
Masks change exactly that. `fragment` cuts the ClientHello into small pieces so a filter that does
not reassemble them cannot read the SNI. `noise` sends random packets first, so the real handshake
does not start the flow. Header and wrapping masks make the traffic look like another protocol, or
like random bytes.

Masks that only change sizes and timing (`fragment`, `merge`, `oob`, `mirage`, `noise`) work with any
server. Masks that change the content (headers, `salamander`, `sudoku`, `xdns`, `xicmp`, `xmc`,
`mkcp-legacy`, `realm`) need the same mask on the server, which means an Xray server configured
for it. `udphop` needs a server that listens on every port it hops to. A mask does not help when
the filter blocks the server's IP address, except `xdns`: it reaches the server through public
DNS resolvers, so the server's own address is never contacted.

## How it works

- `tcp` masks wrap every TCP connection the outbound opens, and `udp` masks every UDP socket and
  connected UDP connection.
- Masks run in list order: the first mask gets the bytes the outbound writes, and the last mask's
  output goes on the wire. Replies pass through them in reverse.
- The masks sit under the protocol and its TLS layer, so they see exactly what would go on the
  wire. With `detour`, they wrap the connection made through the detour outbound.
- The connection is dialed through the masks, as in Xray. A mask that opens sockets of its own
  (`xdns` to its resolvers, `udphop` to each new port) opens them with the outbound's dialer, so
  they take the same `detour`, interface and routing mark as the connection. `xdns`, `xicmp` and
  `udphop` replace the socket to the server: they must be the last `udp` mask.
- Only the client side is implemented: inbounds do not take `finalmask`.
- The masks are Xray-core's own code (from Xray-core v26.10.31), except `merge` and `oob`, which
  come from patterniha's Xray-core; their behavior and settings follow Xray's documentation for
  `finalmask`. Xray's inbound-only `filter` mask is not available.

## Configuration

A VLESS outbound whose ClientHello is fragmented, and a WireGuard endpoint that sends noise before
each handshake:

```json
{
  "outbounds": [
    {
      "type": "vless",
      "server": "example.com",
      "server_port": 443,
      "uuid": "bf000d23-0752-40b4-affe-68f7707a9661",
      "tls": { "enabled": true, "server_name": "example.com" },
      "finalmask": {
        "tcp": [
          { "type": "fragment", "settings": { "packets": "tlshello", "length": "100-200", "delay": "10-20" } }
        ]
      }
    }
  ],
  "endpoints": [
    {
      "type": "wireguard",
      "tag": "wg",
      "address": ["10.0.0.2/32"],
      "private_key": "...",
      "peers": [{ "address": "203.0.113.1", "port": 51820, "public_key": "...", "allowed_ips": ["0.0.0.0/0"] }],
      "finalmask": {
        "udp": [
          { "type": "noise", "settings": { "noise": [{ "rand": "10-50", "delay": "5-10" }] } }
        ]
      }
    }
  ]
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `finalmask.tcp` | array | — | Masks for TCP connections, in order. |
| `finalmask.udp` | array | — | Masks for UDP, in order. |
| `finalmask.quicParams` | object | — | Accepted so Xray configs load; not used. QUIC protocols have their own options in sing-box. |
| `…[].type` | string | — | Mask type (see below). Case does not matter. |
| `…[].settings` | object | `{}` | The mask's settings, exactly as in Xray. |

Supported mask types:

| Type | `tcp` | `udp` | What it does | Main settings |
|---|---|---|---|---|
| `fragment` | yes | — | Splits the first writes (or the TLS ClientHello) into small pieces with delays. | see below |
| `merge` | yes | — | Holds quick writes and sends them as one, for the first writes of the connection. From patterniha's Xray-core. | see below |
| `oob` | yes | — | Sends each of the first writes with one more byte as TCP urgent (out-of-band) data, which the server drops and a filter may misread. Xray's (patterniha's) `dialMode` `oob.<bytes>`. | see below |
| `mirage` | yes | — | Splits the TLS ClientHello into two TLS records, written on their own or in one write, so a filter cannot match the server name. PoriyaVali's Mirage library. | `offset`, `layout` |
| `header-custom` | yes | yes | Adds custom bytes the server expects (a fake protocol header). | TCP: `clients`, `servers`, `errors`; UDP: `mode`, `client`, `server` |
| `sudoku` | yes | yes | Sudoku obfuscation, keyed by a password. | `password`, `ascii`, `customTable`, `customTables`, `paddingMin`, `paddingMax` |
| `xmc` | yes | — | Makes the stream look like a Minecraft connection. | `hostname`, `profiles`, `password` |
| `noise` | — | yes | Sends random or fixed packets before the real ones; a `type` `exp` packet is built from an expression. | `noise` (list of `rand`, `randRange`, `type`, `packet`, `delay`), `reset`, `script` |
| `salamander` | — | yes | Hysteria2's Salamander obfuscation; with `packetSize`, the Gecko variant that also changes packet sizes. | `password`, `packetSize` (at most 2048) |
| `mkcp-legacy` | — | yes | mKCP's old packet headers (`dns`, `dtls`, `srtp`, `utp`, `wechat`, `wireguard`) or its AES-GCM layer. | `header`, `value` |
| `xdns` | — | yes | Carries UDP in DNS queries to the server's domain, through DNS resolvers over UDP, TCP or DoH. | see below |
| `xicmp` | — | yes | Carries UDP in ICMP echo packets. | `ips`, `dgram` |
| `realm` | — | yes | Connects to the peer through NAT hole punching, using STUN servers and a rendezvous URL. | `url` (`realm://` or `realm+http://`), `stunServers`, `tlsConfig` |
| `udphop` | — | yes | Port hopping: moves the UDP flow to another server port, and another local socket, every few seconds or per connection. | see below |

An unknown type, a TCP-only type in `udp` (or the other way round) or bad settings is a
configuration error that names the mask, such as `finalmask.tcp[0] fragment`.

`fragment` settings:

| Field | Type | Default | Meaning |
|---|---|---|---|
| `packets` | string | — | `tlshello` splits the TLS ClientHello; a range such as `"1-3"` splits those writes of the connection. |
| `length` | range | — | Size of each piece in bytes. |
| `delay` | range | `0` | Wait between pieces in milliseconds. |
| `lengths` | range list | — | One length per piece, in place of `length`. |
| `delays` | range list | — | One delay per piece, in place of `delay`. |
| `maxSplit` | range | — | Largest number of pieces. |

A range is `"from-to"` or a number; a range list is an array of them, or a single one.

`noise` with `"type": "exp"` takes `packet` as an expression of segments: `<b 0x1700>` fixed
bytes in hex, `<r 10-20>` random bytes, `<rc 8>` random letters, `<rd 4>` random digits, `<t>` a
timestamp, `<c>` a counter, `<n>` a nonce. `script` is the path of a local `.lua` file that makes
the packets instead of `noise` (Xray has turned inline scripts off for now).

`xdns` settings, for the client:

| Field | Type | Default | Meaning |
|---|---|---|---|
| `domains[].names` | string list | — | The server's domains; queries go to their subdomains. Required. |
| `domains[].types` | number list | `[16]` | DNS record types to ask for: 1 (A), 5 (CNAME), 16 (TXT), 28 (AAAA). |
| `domains[].edns0` | number | `0` | EDNS0 UDP size to announce. The same value on the server lets a reply carry more: without it a reply holds about 500 bytes, too few for mKCP segments. |
| `domains[].lenLimit`, `labelLimit` | number | `255`, `63` | Longest query name and label. |
| `resolvers[].addrs` | string list | — | Resolvers: `8.8.8.8` or `udp://8.8.8.8:53`, `tcp://9.9.9.9:53`, `https://1.1.1.1/dns-query`. Required. |
| `resolvers[].worker` | number | `32` | Queries in flight per resolver. |
| `resolvers[].tlsConfig` | object | — | TLS of a DoH resolver, as Xray's `tlsSettings`: `serverName`, `alpn` (`["h3"]` for DoH over QUIC), `fingerprint`, `pinnedPeerCertSha256`, `verifyPeerCertByName`, `echConfigList` and the like. Required for `https://`. |
| `resolvers[].quicConfig` | object | — | QUIC settings of a DoH resolver over h3, as Xray's `quicParams`. |
| `extraPoll` | number | `0` | Extra empty queries per write, 0 to 3, so replies come back sooner. |

The settings of earlier Xray versions still load: `"resolvers": ["t.example.com+udp://8.8.8.8:53"]`
becomes the domain `t.example.com` with the resolver `udp://8.8.8.8:53`, and `{"name": ...}` and
`{"type": ..., "addr": ...}` become `names` and `addrs`.

`udphop` settings:

| Field | Type | Default | Meaning |
|---|---|---|---|
| `mode` | string | — | Comma separated: `intervalLocal` changes the local socket, `intervalRemote` the server port on a timer, `perConnRemote` picks a server port per connection. Required. |
| `interval` | range | `30` | Seconds between hops, at least 5. |
| `remotePorts` | port list | — | Server ports to hop between: `"20000-20100,443"`. |
| `remoteIPs` | string list | — | Server addresses or prefixes to hop between as well. |

`merge` settings:

| Field | Type | Default | Meaning |
|---|---|---|---|
| `times` | number | `0` | How many merged writes to send; then writes pass through. `0` or less merges for the whole connection. |
| `delayMs` | number | `30` | A held write goes out when no new one comes for this many milliseconds. |
| `maxBytes` | number | `16384` | Held bytes go out at once when they reach this size. |

`oob` settings:

| Field | Type | Default | Meaning |
|---|---|---|---|
| `bytes` | number list | — | One byte (0 to 255) per write: write `i` is sent with `bytes[i]` as urgent data. Required. |

`mirage` settings:

| Field | Type | Default | Meaning |
|---|---|---|---|
| `offset` | number | `5` | Size of the first record's handshake bytes (1 to 16383). Safe sizes depend on the network: 1, 2, 4 and 5 passed in Iran in 2026, 3 and 6 or more were dropped. |
| `layout` | string | `separate` | `separate` writes each record on its own (what MCI and Irancell let through in September 2026); `single` writes both in one write (what Iran let through in August 2026). |

`mirage` only changes the first write when it is one complete ClientHello with a server name; any
other first write goes out unchanged. Put it last in `tcp`, or after the masks that need the plain
ClientHello. A bad `offset` can make the filter drop the whole connection, even for an allowed name.

`oob` works on the socket, so put it last in `tcp`; a share link's `dialMode=oob.0,32` becomes
`{"type": "oob", "settings": {"bytes": [0, 32]}}` after the link's other masks. It needs a real
TCP socket: through a `detour` it does nothing.

Related options: the outbound's [`tls_fragment`](../tls-fragment.md) is added as the first
`fragment` mask. [`tls_tricks`](../tls-tricks.md) changes the ClientHello itself and is not a mask.
`tls_fragment` cannot be used with `tcp_fast_open`.

## See also

- [XDRIVE transport](xdrive.md)
- [TLS fragment](../tls-fragment.md)
- [TLS tricks](../tls-tricks.md)
- [XHTTP transport](xhttp.md)
