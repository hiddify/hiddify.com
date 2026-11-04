# TrustTunnel

[All Hiddify features](../../index.md)

TrustTunnel is a VPN protocol published at [trusttunnel.org](https://trusttunnel.org/). It carries
your traffic as HTTP `CONNECT` requests inside an HTTPS connection, over HTTP/2 on TLS or over
HTTP/3 on QUIC. Hiddify uses the
[sing-trusttunnel](https://github.com/xchacha20-poly1305/sing-trusttunnel) library. In a config it
is the outbound `"type": "trusttunnel"`, and the inbound of the same type runs a server.

## Why use it

Use it to connect to a TrustTunnel server, or run your own server with the `trusttunnel` inbound.
It is a good choice where HTTPS to ordinary sites works but proxy protocols are blocked, and it can
switch between TCP (HTTP/2) and UDP (HTTP/3) with one field.

## How it gets past filtering

To a filter, a TrustTunnel connection is an HTTPS connection to your server's domain: a normal TLS
handshake, then HTTP/2 or HTTP/3. The proxied traffic is inside the encrypted HTTP streams. The
login is a standard `Proxy-Authorization` header inside that encryption.

The protection depends on your TLS setup. A real domain with a valid certificate looks like any
HTTPS site. TLS features such as uTLS fingerprints and ECH come from the `tls` block. It does not
help when the server's IP address or domain is blocked, and QUIC mode does not help where UDP or
QUIC is blocked.

## How it works

- The client opens one TLS (or QUIC) connection to the server and sends each proxied TCP
  connection as an HTTP `CONNECT` request on its own stream. Many connections share the one
  connection.
- UDP traffic goes through one `CONNECT` request to a special address (`_udp2`), with the
  packets framed inside the stream.
- With `health_check` on, the client sends a small check request when the connection has been idle
  for 7 seconds, so a dead connection is found early.
- When the network changes, the client drops its connections and opens new ones.
- The server checks the user name and password of each request and refuses unknown users.

## Configuration

```json
{
  "outbounds": [
    {
      "type": "trusttunnel",
      "tag": "trusttunnel-out",
      "server": "vpn.example.com",
      "server_port": 443,
      "username": "alice",
      "password": "<password>",
      "tls": {
        "enabled": true,
        "server_name": "vpn.example.com"
      }
    }
  ]
}
```

### Outbound fields

| Field | Type | Default | Meaning |
|---|---|---|---|
| `server` | string | required | Server address. |
| `server_port` | number | required | Server port. |
| `username` | string | required | User name. |
| `password` | string | required | Password. |
| `tls` | object | required | Outbound TLS settings. `enabled` must be `true`. |
| `quic` | bool | `false` | Use HTTP/3 over QUIC instead of HTTP/2 over TLS. |
| `quic_congestion_control` | string | `"bbr"` | QUIC congestion control: `bbr`, `cubic` or `reno`. An unknown value means `bbr`. |
| `health_check` | bool | `false` | Check the connection when it has been idle for 7 seconds. |
| Dialer fields | | | The usual outbound dialer fields, such as `detour`. |

### Inbound fields

| Field | Type | Default | Meaning |
|---|---|---|---|
| `users` | list | required | Users, each with `username` and `password`. |
| `network` | string | both | `tcp` (HTTP/2), `udp` (HTTP/3), or empty for both. |
| `quic_congestion_control` | string | `"bbr"` | Congestion control for HTTP/3 clients: `bbr`, `cubic` or `reno`. |
| `tls` | object | | Inbound TLS settings. Required when `network` includes `udp`. |
| Listen fields | | | The usual inbound listen fields, such as `listen` and `listen_port`. |

### Notes

- QUIC needs the `with_quic` build tag. Hiddify's builds include it. Without it, `quic: true`
  fails with a "QUIC is not included" error.
- Without TLS, or without a user name and password, the outbound fails to load. The inbound fails
  to load without at least one user.
- Each user name must have a password.

## See also

- [All Hiddify features](../../index.md)
