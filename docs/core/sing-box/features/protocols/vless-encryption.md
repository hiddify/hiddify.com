# VLESS encryption

[All Hiddify features](../../index.md)

VLESS encryption is Xray's encryption layer for VLESS, `mlkem768x25519plus`. It encrypts the
VLESS stream with keys agreed through a hybrid post-quantum handshake (ML-KEM-768 and X25519), so
VLESS can run safely without TLS, or inside any transport. It is the `encryption` field of a VLESS
outbound and the `decryption` field of a VLESS inbound. The strings are the same as Xray's.

## Why use it

- To connect to Xray servers that require VLESS encryption.
- To run VLESS without TLS, or behind a CDN or proxy that ends TLS, and still have the content
  encrypted end to end between client and server.
- To add Vision (`xtls-rprx-vision`) on top of the encryption when there is no TLS.

## How it gets past filtering

With the `random` mode, everything on the wire, including the handshake, looks like random bytes,
with no protocol header for a filter to match. `xorpub` hides only the public keys in the
handshake; `native` sends the handshake as is. Padding settings in the string change the sizes of
the first packets.

Random-looking traffic is itself blocked on some networks. In those places, use encryption inside
a transport that looks like normal web traffic (such as [XHTTP](../transports/xhttp.md) or WebSocket with
TLS) rather than bare.

## How it works

- The client string lists the server's public keys; the server string has the matching private
  keys. Several keys in a row form a chain, and both sides must list the same number in the same
  order.
- `1rtt` does the full handshake on every connection. `0rtt` reuses a ticket from the server, so
  later connections send data at once. The server decides how long tickets last.
- The encryption runs inside TLS and the transport, right under VLESS, so it works with every
  transport. On a server, kTLS is turned off when `decryption` is set.
- If the handshake fails or the connection's context ends first, the connection is closed.

## Configuration

Client:

```json
{
  "outbounds": [
    {
      "type": "vless",
      "server": "203.0.113.1",
      "server_port": 8443,
      "uuid": "bf000d23-0752-40b4-affe-68f7707a9661",
      "encryption": "mlkem768x25519plus.random.0rtt.<server public key>"
    }
  ]
}
```

Server:

```json
{
  "inbounds": [
    {
      "type": "vless",
      "listen": "::",
      "listen_port": 8443,
      "users": [{ "uuid": "bf000d23-0752-40b4-affe-68f7707a9661" }],
      "decryption": "mlkem768x25519plus.random.600s.<server private key>"
    }
  ]
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `encryption` (outbound) | string | `""` | `none` or empty: no encryption. Otherwise `mlkem768x25519plus.<mode>.<rtt>[.<padding>…].<key>[.<key>…]`. |
| `decryption` (inbound) | string | `""` | `none` or empty: no encryption. Otherwise `mlkem768x25519plus.<mode>.<seconds>[.<padding>…].<key>[.<key>…]`. |

Parts of the string, separated by dots:

| Part | Values | Meaning |
|---|---|---|
| `<mode>` | `native`, `xorpub`, `random` | `native`: plain handshake. `xorpub`: the public keys in the handshake are hidden. `random`: all bytes look random. Both sides must use the same mode. |
| `<rtt>` (client) | `0rtt`, `1rtt` | Reuse server tickets, or do the full handshake every time. |
| `<seconds>` (server) | such as `600s` or `300-600s` | How long a ticket stays valid. |
| `<padding>` | Xray padding segments | Optional; sizes and delays of padding on the first packets, as in Xray. |
| `<key>` (client) | base64url | X25519 public key (32 bytes) or ML-KEM-768 encapsulation key (1184 bytes). |
| `<key>` (server) | base64url | X25519 private key (32 bytes) or ML-KEM-768 seed (64 bytes). |

Keys and complete strings can be made with Xray's `xray vlessenc` command. A string with a wrong
prefix, mode, RTT value or key length is a configuration error.

Vision: in Hiddify, `flow: "xtls-rprx-vision"` on the outbound also works over VLESS encryption
with no TLS or REALITY; it needs one of the two. With `random` mode Vision does not splice
(copy directly between sockets). When `multiplex` is enabled, the flow is turned off, since Vision
cannot run over a multiplexed connection.

## See also

- [REALITY in Hiddify](../reality-hiddify.md)
- [XHTTP transport](../transports/xhttp.md)
