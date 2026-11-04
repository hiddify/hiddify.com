# Raw transport

[All Hiddify features](../../index.md)

`raw` is a V2Ray transport that adds nothing: the protocol runs straight over TCP, or over TLS
when the `tls` block is enabled. It is the same as having no `transport` block, and matches
Xray's `raw` (formerly `tcp`) network. Set it with `"transport": {"type": "raw"}` on a VLESS,
VMess or Trojan inbound or outbound.

## Why use it

It lets configs converted from Xray, or written by tools that always fill in a transport, load
without change. A node whose Xray network is `raw` or `tcp` can be written as `"type": "raw"`. You never
need it in a config you write by hand.

## How it gets past filtering

It does not. It adds no framing or disguise; what the filter sees is the protocol itself and its
TLS or REALITY layer.

## How it works

- Client: dials the server over TCP, does the TLS handshake if TLS is enabled, and hands the
  connection to the protocol.
- Server: accepts TCP connections, does the TLS handshake if TLS is enabled, and hands each one to
  the protocol. It does not listen on UDP.

## Configuration

```json
{
  "outbounds": [
    {
      "type": "vless",
      "server": "example.com",
      "server_port": 443,
      "uuid": "bf000d23-0752-40b4-affe-68f7707a9661",
      "tls": { "enabled": true, "server_name": "example.com" },
      "transport": { "type": "raw" }
    }
  ]
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `type` | string | — | `raw`. The transport has no other fields. |

## See also

- [XHTTP transport](xhttp.md)
