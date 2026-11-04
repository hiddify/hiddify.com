# REALITY in Hiddify

[All Hiddify features](../index.md)

Hiddify changes how the REALITY client builds its ClientHello so it connects to current Xray
servers, and adds one option, `key_share`, in the `reality` object of an outbound's `tls` block.
This page covers only those changes; the rest of REALITY works as in sing-box.

## Why use it

Xray servers from v26.9.8 reject a REALITY ClientHello without the hybrid post-quantum key share
(X25519MLKEM768). Upstream sing-box removes that key share from REALITY ClientHellos, so it cannot
connect to those servers. Hiddify sends it, and still connects to older servers.

## How it gets past filtering

REALITY makes the connection look like a TLS 1.3 visit to a real website (the `server_name`),
with the ClientHello of a real browser. Sending the hybrid key share, as current Chrome, Firefox,
Safari and Edge do, keeps it close to what those browsers send.

The hybrid key share makes the ClientHello about 1.7 KB, which is two TCP segments. Some networks
drop or block such ClientHellos. For those networks, `key_share: "classical"` or the
[fragment options](tls-fragment.md) can help.

## How it works

- The ClientHello is the uTLS fingerprint's own, changed only where REALITY needs it: TLS 1.3 is
  offered, and the key shares are X25519MLKEM768 then X25519 (the share REALITY authenticates
  with), followed by the fingerprint's other shares. Fingerprints that lack TLS 1.3 or an X25519
  share (old browsers, Android OkHttp, 360) get them added, so every fingerprint works.
- With `key_share: "classical"`, X25519MLKEM768 is removed from the groups and key shares. The
  ClientHello fits one TCP segment, but Xray servers from v26.9.8 refuse it.
- The client reports itself to the server as Xray 26.10.17. Servers compare this with their
  minimum client version; the old version sing-box sent (1.8.1) is refused by servers that set
  one.
- `tls.fragment` and `tls.record_fragment` now apply to REALITY. Upstream accepted them on a
  REALITY node and did nothing.
- A `short_id` longer than 16 hex digits is a configuration error. Before, it crashed the client
  or server when the config loaded.
- The `unsafe` uTLS fingerprint cannot be used: REALITY needs uTLS.

## Configuration

```json
{
  "outbounds": [
    {
      "type": "vless",
      "server": "203.0.113.1",
      "server_port": 443,
      "uuid": "bf000d23-0752-40b4-affe-68f7707a9661",
      "flow": "xtls-rprx-vision",
      "tls": {
        "enabled": true,
        "server_name": "www.example.com",
        "utls": { "enabled": true, "fingerprint": "chrome" },
        "reality": {
          "enabled": true,
          "public_key": "jNXHt1yRo0vDuchQlIP6Z0ZvjT3KtzVI-T4E7RoLJS0",
          "short_id": "0123abcd",
          "key_share": "hybrid"
        }
      }
    }
  ]
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `key_share` | string | `""` | `""` or `hybrid`: send the X25519MLKEM768 and X25519 key shares (works with all Xray versions). `classical`: X25519 only, a smaller ClientHello; only Xray servers older than v26.9.8 accept it. |

Any other `key_share` value is a configuration error.

Compatibility: tested with the chrome, firefox, safari and edge fingerprints against Xray
26.10.21 and 26.3.27. The default works with both; `classical` works with 26.3.27 and is refused
by 26.10.21. `fragment` and `record_fragment` work with both.

## See also

- [TLS fragment](tls-fragment.md)
- [VLESS encryption](protocols/vless-encryption.md)
- [XHTTP transport](transports/xhttp.md)
