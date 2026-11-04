# Tunnel (reverse tunnel)

[All Hiddify features](../../index.md)

The tunnel endpoints connect several sing-box instances through one public server, so that a
machine without a public address (behind NAT or a firewall) can still be reached. The server runs
the endpoint `"type": "tunnel_server"` and each other machine runs `"type": "tunnel_client"`.
Each client keeps connections open to the server, and the server sends traffic for that client
back down those connections. Every party has a UUID, and route rules choose the party that
traffic goes to.

## Why use it

- Reach a home or office machine that has no public IP address, through a server that has one.
- Connect two clients that cannot reach each other directly, through the server.
- Use any proxy protocol between the clients and the server, for example VLESS with REALITY, so
  the tunnel gets that protocol's protection.

## How it gets past filtering

The tunnel adds no obfuscation of its own. Its traffic travels inside the outbound you give the
client and the inbound you give the server, so it looks exactly like that protocol. Choose a
protocol that works on your network. Because the client always dials out to the server, it also
works where incoming connections to the client are blocked.

## How it works

- **Identities.** Each client has a `uuid` (its public name, used in route rules) and a `key` (a
  secret, also in UUID format). The server has its own `uuid` and a list of users, each with the
  `uuid` and `key` of one client.
- **Standby connections.** After start, each client opens 5 connections to the server through its
  `outbound` and keeps them ready. The server keeps up to 10 per client and closes the oldest when
  a new one arrives. If a connection fails, the client waits 5 seconds and tries again.
- **Control address.** Tunnel connections go to the address `sp.tunnel.sing-box.arpa:444` inside
  the outbound protocol. The server's `inbound` handles them. Other connections that reach that
  inbound are routed as usual, so the same inbound can also serve normal proxy users.
- **Sending traffic.** A connection routed to the `tunnel_client` endpoint is sent to the server
  with the UUID of the party it is for (its tunnel destination). On the server it is routed again,
  with `tunnel_source` set to the sending client and `tunnel_destination` set to the target:
  - If the target is the server's own `uuid`, the server routes it like any other connection (for
    example to the internet).
  - If the target is another client, a rule sends it to the `tunnel_server` endpoint, which hands
    it to that client over one of its standby connections. The target client routes it with
    `tunnel_source` set to the sender.
- Only TCP is carried. UDP is refused.
- A connection whose destination is the sender itself is refused as a routing loop.

## Configuration

Server:

```json
{
  "endpoints": [
    {
      "type": "tunnel_server",
      "tag": "tunnel",
      "uuid": "00000000-0000-0000-0000-000000000001",
      "users": [
        {
          "uuid": "11111111-1111-1111-1111-111111111111",
          "key": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
        },
        {
          "uuid": "22222222-2222-2222-2222-222222222222",
          "key": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb"
        }
      ],
      "inbound": {
        "type": "vless",
        "tag": "tunnel-in",
        "listen": "::",
        "listen_port": 443,
        "users": [{ "uuid": "cccccccc-cccc-cccc-cccc-cccccccccccc" }]
      }
    }
  ],
  "route": {
    "rules": [
      {
        "tunnel_destination": ["22222222-2222-2222-2222-222222222222"],
        "outbound": "tunnel"
      }
    ]
  }
}
```

Client:

```json
{
  "endpoints": [
    {
      "type": "tunnel_client",
      "tag": "tunnel",
      "uuid": "11111111-1111-1111-1111-111111111111",
      "key": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
      "outbound": {
        "type": "vless",
        "tag": "tunnel-out",
        "server": "203.0.113.10",
        "server_port": 443,
        "uuid": "cccccccc-cccc-cccc-cccc-cccccccccccc"
      }
    }
  ]
}
```

### `tunnel_client` fields

| Field | Type | Default | Meaning |
|---|---|---|---|
| `uuid` | string | required | This client's UUID. Others use it as a tunnel destination. |
| `key` | string | required | This client's secret, in UUID format. It must match a user `key` on the server. |
| `outbound` | object | required | A full outbound (with `type`, `tag` and its fields) that reaches the server's `inbound`. |

### `tunnel_server` fields

| Field | Type | Default | Meaning |
|---|---|---|---|
| `uuid` | string | required | The server's UUID. Traffic for this UUID leaves through the server. |
| `users` | list | none | The clients, each with `uuid` and `key`. |
| `inbound` | object | required | A full inbound (with `type`, `tag` and its fields) that the clients connect to. |
| `connect_timeout` | duration | `5s` | How long to wait for a free standby connection of the target client. |

### Route rule fields

| Field | Where | Meaning |
|---|---|---|
| `tunnel_source` | route and DNS rules, rule sets | Matches the UUID of the party that sent the connection. |
| `tunnel_destination` | route and DNS rules, rule sets | Matches the UUID the connection is for. |
| `override_tunnel_destination` | `route` and `route-options` actions | Sets the UUID a connection is for. |

### Notes

- A new connection gets its tunnel destination from the `override_tunnel_destination` of a
  `route` or `route-options` action. Both endpoints refuse a connection without one
  ("tunnel destination not set").
- An unknown client key, or a target UUID that is not a user, is refused and logged.
- All UUIDs and keys must be valid UUIDs, or the config fails to load.

## See also

- [All Hiddify features](../../index.md)
