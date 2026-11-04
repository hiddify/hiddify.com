# Mieru

[All Hiddify features](../../index.md)

Mieru is a proxy protocol from the [mieru project](https://github.com/enfein/mieru). Every byte it
sends is encrypted, with random padding, so the traffic has no fixed header or pattern to match.
It runs over TCP or UDP. In a config it is the outbound `"type": "mieru"`; Hiddify also has a
`mieru` inbound for running a server.

## Why use it

Use it to connect to a mieru server (the official `mita` server, or a sing-box `mieru` inbound).
It needs no TLS certificate and no domain, and it can use a range of ports. It is a good choice
where TLS-based protocols are blocked by SNI or certificate checks but random-looking traffic
still gets through.

## How it gets past filtering

Mieru does not imitate another protocol. Instead it gives a filter nothing to recognize: there is
no plain-text handshake, no protocol header and no fixed packet size, because everything,
including the first packet, is encrypted and padded. The server answers only clients that have a
valid key, so a probe that sends random data gets no useful reply.

This does not help on networks that block traffic they cannot classify, or that allow only known
protocols. Such networks often block fully random traffic, so test it on your network.

## How it works

- The encryption key comes from the user name, the password and the current time. The time is
  rounded to 2-minute steps, so the clocks of the client and the server must be within a few
  minutes of each other. If they are not, the connection fails.
- The client connects to one of the server's port bindings, over TCP or UDP as the binding says.
- Several proxied connections can share one underlying connection (`multiplexing`).
- UDP traffic is carried inside the mieru stream, so UDP works on a TCP binding too.
- With `handshake_mode` set to `HANDSHAKE_NO_WAIT`, the client sends the first data together with
  the connect request (0-RTT). With `HANDSHAKE_STANDARD` it waits until the server has connected
  to the destination (1-RTT).

## Configuration

```json
{
  "outbounds": [
    {
      "type": "mieru",
      "tag": "mieru-out",
      "server": "203.0.113.10",
      "portBindings": [
        { "protocol": "TCP", "portRange": "2012-2022" }
      ],
      "username": "alice",
      "password": "<password>",
      "multiplexing": "MULTIPLEXING_LOW"
    }
  ]
}
```

### Outbound fields

| Field | Type | Default | Meaning |
|---|---|---|---|
| `server` | string | required | Server IP address or domain. |
| `server_port` | number | none | A single server port. If set, `portBindings` must hold exactly one binding with the same `port`. Usually leave it out and use `portBindings`. |
| `portBindings` | list | required | The server's ports. See below. |
| `username` | string | required | User name. |
| `password` | string | required | Password. |
| `multiplexing` | string | `""` | How many connections share one underlying connection: `""`/`DEFAULT`, `LOW`, `MIDDLE` (or `MEDIUM`), `HIGH`. The `MULTIPLEXING_` prefix is optional. |
| `handshake_mode` | string | `""` | `""`/`DEFAULT`, `STANDARD` or `NO_WAIT`. The `HANDSHAKE_` prefix is optional. |
| `network` | string | both | `tcp`, `udp`, or empty for both. Which kinds of proxied traffic this outbound accepts. |
| Dialer fields | | | The usual outbound dialer fields, such as `detour`. |

### Port binding fields (`portBindings`)

| Field | Type | Default | Meaning |
|---|---|---|---|
| `protocol` | string | required | `TCP` or `UDP`. |
| `port` | number | none | One port. |
| `portRange` | string | none | A range of ports, such as `"2012-2022"`. |

Each binding must have either `port` or `portRange`, not both. Ports are from 1 to 65535.

### Inbound fields

The `mieru` inbound runs a mieru server. It takes the usual listen fields and:

| Field | Type | Default | Meaning |
|---|---|---|---|
| `users` | list | required | Users, each with `username` and `password`. |
| `portBindings` | list | required | Ports to listen on, same format as above. |
| `network` | string | both | `tcp`, `udp`, or empty for both. |

If `listen_port` is set, `portBindings` must hold exactly one binding with the same `port`.

### Notes

- Values are case-insensitive. An unknown `multiplexing` or `handshake_mode` value, a missing user
  name or password, or a bad port binding stops the config from loading with an error that names
  the problem.
- Mieru does not use TLS, so the `tls` block does not apply.

## See also

- [All Hiddify features](../../index.md)
