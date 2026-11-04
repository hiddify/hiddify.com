# rmux multiplexing

[All Hiddify features](../../index.md)

rmux is one more protocol for sing-box multiplexing: `"multiplex": {"protocol": "rmux"}` on an
outbound. Like `smux`, `yamux` and `h2mux`, it carries many connections inside one connection to
the server. It comes from sing-box-extended (github.com/shtorm-7/rmux).

## Why use it

- Fewer connections to the server: each new connection opens a stream in a session that already
  exists, with no new handshake, so it starts faster and shows fewer connections to the network.
- You want a multiplexer other than the usual ones; rmux is newer and less common on the wire.

## How it gets past filtering

It does not on its own. It runs inside the outbound's protocol and transport, which are what the
network sees.

## How it works

- Data travels in frames of at most 32 KiB, each tagged with its stream.
- A stream can be closed for writing while it still reads, as with `h2mux`.
- Sessions are kept and reused as for the other protocols; keepalive frames are off, as sing-box
  manages idle sessions itself.

## Configuration

```json
{
  "type": "vless",
  "server": "example.com",
  "server_port": 443,
  "uuid": "b831381d-6324-4d53-ad4f-8cda48b30811",
  "multiplex": { "enabled": true, "protocol": "rmux", "max_connections": 4 }
}
```

The server's inbound needs `"multiplex": {"enabled": true}` and Hiddify's sing-box: it accepts
rmux like the other protocols, and an upstream sing-box server refuses it. The other
`multiplex` fields work as for the other protocols. No build tag is needed.

## See also

- [Bond](../protocols/bond.md)
