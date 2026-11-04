# TLS tricks (tls_tricks)

[All Hiddify features](../index.md)

`tls_tricks` changes the TLS ClientHello an outbound sends: it can send the server name in a
random mix of upper and lower case, and add a padding extension of a chosen size. It is the
`tls_tricks` object inside an outbound's `tls` block.

## Why use it

Some filters match the server name (SNI) exactly, or match the ClientHello by its size. Changing
the case of the name, or making the ClientHello bigger, can get past such filters without any
change on the server.

## How it gets past filtering

- Mixed-case SNI: DNS names do not depend on case, so `ExAmPle.CoM` reaches the same site and the
  certificate still matches. A filter that compares the name byte by byte, in lower case, does not
  see a match. The case is new for every connection.
- Padding: a padding extension of `padding_size` bytes is put right before the SNI extension. It
  makes the ClientHello larger and pushes the server name further in, often into a later TCP
  segment, where a filter that reads only the first packet does not look.

It does not help against filters that compare names without case, reassemble the stream, or block
the server's IP.

## How it works

The tricks are made by the TLS client itself, not as [finalmask](transports/finalmask.md) masks. The
ClientHello is part of the TLS 1.3 handshake transcript, which both sides hash and check, so a
mask that edited it on the wire would break the handshake. Here the TLS library builds the changed
ClientHello and uses it in its own transcript.

- `mixedcase_sni` works with the standard Go TLS client and with uTLS.
- Padding needs uTLS with a fixed fingerprint (such as `chrome` or `firefox`). It replaces the
  fingerprint's own padding extension with one of the chosen size, and leaves the rest of the
  fingerprint as it is. With `random` or `randomized` fingerprints the config does not load.
  Without uTLS, padding is ignored with a warning.
- REALITY builds its own ClientHello and does not use `tls_tricks`.

## Configuration

```json
{
  "outbounds": [
    {
      "type": "vless",
      "server": "example.com",
      "server_port": 443,
      "uuid": "bf000d23-0752-40b4-affe-68f7707a9661",
      "tls": {
        "enabled": true,
        "server_name": "example.com",
        "utls": { "enabled": true, "fingerprint": "chrome" },
        "tls_tricks": {
          "mixedcase_sni": true,
          "padding_mode": "random",
          "padding_size": "800-1200"
        }
      }
    }
  ]
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `mixedcase_sni` | bool | `false` | Send the server name with a random case on each connection. |
| `padding_mode` | string | `""` | `random` adds the padding extension. Empty also adds it when `padding_size` is set. |
| `padding_size` | string | — | Padding length in bytes, a number or a range `"from-to"` (a random length each connection), from 1 to 16000. Required with `random`. |
| `padding_sni` | string | — | Not supported; ignored with a warning. |

The padding modes `sni` and `hello_client` and the field `padding_sni` were never implemented. They
are ignored with a warning, so configs that carry them still load. A `padding_size` that is not a
number or range, or is out of range, is a configuration error.

## See also

- [TLS fragment](tls-fragment.md)
- [finalmask](transports/finalmask.md)
- [REALITY in Hiddify](reality-hiddify.md)
