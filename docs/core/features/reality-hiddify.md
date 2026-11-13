# REALITY in Hiddify

[All Hiddify features](index.md)

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
drop or block such ClientHellos. For those, `key_share: "classical"` sends a small one every time,
and `key_share: "auto"` tests it once per server when hybrid gets no answer (see below).

The default (`key_share` unset) behaves as Chrome: hybrid every time, no fallback. Real Chrome
never retries without its post-quantum key share; when a connection fails, it fails. A client that
retries with a small ClientHello a few seconds after a large one was dropped does something Chrome
does not, and an observer that drops large ClientHellos on purpose can see it. That marks the
client, it does not prove REALITY (a man in the middle cannot read REALITY either way), but it is
why `auto` is opt-in and why it tests only once per server. The classical ClientHello is that of an
older version of the same browser (Chrome 120, Firefox 120, Safari 16), from before it sent the
post-quantum key share: a ClientHello that browsers still in use send, rather than "current Chrome
without it", which no browser sends. The server answers active probes as before in every mode.

## How it works

- The ClientHello is the uTLS fingerprint's own, changed only where REALITY needs it: TLS 1.3 is
  offered, and the key shares are X25519MLKEM768 then X25519 (the share REALITY authenticates
  with), followed by the fingerprint's other shares. Fingerprints that lack TLS 1.3 or an X25519
  share (old browsers, Android OkHttp, 360) get them added, so every fingerprint works.
- With `key_share: "classical"`, the ClientHello is that of an older version of the same browser,
  from before it sent X25519MLKEM768: Chrome 120 for chrome, edge, 360 and qq; Firefox 120 for
  firefox; Safari 16.0 for safari and ios. Other fingerprints (android, random, randomized) keep
  theirs. Any X25519MLKEM768 left is removed. The ClientHello fits one TCP segment, but Xray
  servers from v26.9.8 refuse it.
- With `key_share: "auto"`, the client starts with hybrid and tests classical once per server:
  - After two hybrid handshakes in a row that get no answer (a timeout, a reset, a closed
    connection), it tries classical. A failed REALITY verification does not count: the ClientHello
    got through, so classical would not help, and a man in the middle that answers with its own
    certificate cannot start the test. Failed dials and cancelled connections do not count either.
  - A classical handshake that works settles it on classical. Two failed classical handshakes
    (v26.9.8+ servers refuse classical with a failed verification) settle it on hybrid, and
    classical is never tried again for that server. A settled classical that later fails twice
    (the server was upgraded) goes back to hybrid for good.
  - The result belongs to the server (address, `server_name`, `public_key`), not to the outbound:
    a subscription update or config reload, under any tag, keeps it. It is saved in the
    [cache file](https://sing-box.sagernet.org/configuration/experimental/cache-file/) for 30 days,
    so a restarted core does not test again. Each step is logged as a warning.
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
| `key_share` | string | `""` | `""` or `hybrid`: send the X25519MLKEM768 and X25519 key shares, as current browsers do (works with all Xray versions). `classical`: X25519 only, the ClientHello of an older browser that fits one TCP segment; only Xray servers older than v26.9.8 accept it. `auto`: hybrid, and classical, tested once per server, when hybrid handshakes get no answer (see above). |

Any other `key_share` value is a configuration error.

Compatibility: tested with the chrome, firefox, safari and edge fingerprints against Xray
26.10.21 and 26.3.27. The default works with both; `classical` works with 26.3.27 and is refused
by 26.10.21. `fragment` and `record_fragment` work with both. The older-browser classical
ClientHellos and `auto` are tested against the sing-box REALITY server only so far.

## Sources and credits

Parts of this feature come from these projects. Thanks to their authors.

- [XTLS/REALITY](https://github.com/XTLS/REALITY): the REALITY protocol.
- [Leadaxe/sing-box-lx](https://github.com/Leadaxe/sing-box-lx): `key_share` and fragmentation on REALITY follow it.
- [Leadaxe/utls-lx](https://github.com/Leadaxe/utls-lx): the uTLS fork with current browser fingerprints, a fork of [metacubex/utls](https://github.com/metacubex/utls) and [refraction-networking/utls](https://github.com/refraction-networking/utls).

Related projects:

- [XTLS/Xray-core](https://github.com/XTLS/Xray-core): the REALITY server Hiddify connects to.

## See also

- [TLS fragment](tls-fragment.md)
- [VLESS encryption](protocols/vless-encryption.md)
- [XHTTP transport](transports/xhttp.md)
