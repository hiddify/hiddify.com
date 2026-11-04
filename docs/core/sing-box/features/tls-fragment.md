# TLS fragment (tls_fragment)

[All Hiddify features](../index.md)

`tls_fragment` splits the TLS ClientHello an outbound sends into many small pieces, with an
optional pause between them. It is the `tls_fragment` object in the dial fields of an outbound
(next to `detour`, not inside `tls`). Hiddify keeps it for existing configs; inside, it is applied
as the first [finalmask](transports/finalmask.md) `fragment` mask.

## Why use it

Some filters read the server name (SNI) from the ClientHello and block the connection when they
see a blocked name. Splitting the ClientHello can get a connection through such a filter without
any change on the server. Use it when a TLS or REALITY node connects only sometimes, or fails right
after the ClientHello.

## How it gets past filtering

The ClientHello is cut into TLS records of a few bytes, each written separately, so the SNI is
spread over many records and TCP segments. A filter that looks at single packets, or does not
reassemble TLS records, cannot read the name. The server's TLS stack puts the pieces back
together, so it needs no setting.

It does not help against filters that reassemble the stream, or that block the server's IP. Small
pieces and long pauses make the handshake slower.

## How it works

- `method` `tlsHello` (the default) splits only the ClientHello. `range` splits the writes named in
  `range` (such as the first three) into pieces of `size` bytes, whatever they contain.
- Each piece is `size` bytes (a random size from the range), with a pause of `sleep` milliseconds
  between pieces.
- It wraps the outbound's TCP connections under the TLS layer, so it works for every protocol that
  uses TLS on that outbound, including REALITY.
- It is added in front of the outbound's own `finalmask.tcp` masks, so it gets the bytes the TLS
  stack writes before any other mask.

### Compared with tls.fragment and tls.record_fragment

Upstream sing-box has two switches inside the `tls` block:

- `tls.fragment` splits the ClientHello into TCP segments at the server name and waits for each
  segment to be acknowledged (`fragment_fallback_delay` when it cannot tell).
- `tls.record_fragment` splits the ClientHello into several TLS records, also inside the server name.

They take no sizes or delays. In this fork both also work with REALITY (upstream ignored them on
REALITY nodes). `tls_fragment` is Hiddify's own option: it sets the piece size and the pause, and
can split writes other than the ClientHello. Use one of them, not several at once.

## Configuration

```json
{
  "outbounds": [
    {
      "type": "trojan",
      "server": "example.com",
      "server_port": 443,
      "password": "secret",
      "tls": { "enabled": true, "server_name": "example.com" },
      "tls_fragment": {
        "enabled": true,
        "size": "10-30",
        "sleep": "2-8"
      }
    }
  ]
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `enabled` | bool | `false` | Turn fragmentation on. |
| `size` | string | `1-10` | Piece size in bytes, a number or a range `"from-to"`. |
| `sleep` | string | `0` | Pause between pieces in milliseconds, a number or a range. |
| `method` | string | `tlsHello` | `tlsHello` splits the ClientHello; `range` splits the writes in `range`. |
| `range` | string | — | With `range`, which writes to split, such as `"1-3"`. Required for that method. |

Errors: with `tcp_fast_open` on the same outbound, the config does not load (the first data is
sent with the TCP handshake, before it can be split). An unknown `method`, or `range` without a
`range`, is also a configuration error.

Old templates put `tls_fragment` inside the `tls` block. When the outbound is created, an enabled
`tls_fragment` there is moved to the outbound's dial fields and applied, unless the outbound
already has its own enabled `tls_fragment`. Then the one in the `tls` block is ignored.

## See also

- [finalmask](transports/finalmask.md)
- [TLS tricks](tls-tricks.md)
- [REALITY in Hiddify](reality-hiddify.md)
