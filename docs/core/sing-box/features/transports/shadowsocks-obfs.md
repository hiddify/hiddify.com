# Shadowsocks simple-obfs server and fallback

[All Hiddify features](../../index.md)

The Shadowsocks inbound can run the server side of simple-obfs (`obfs-server`), so clients using
the `obfs-local` plugin in `http` or `tls` mode can connect to sing-box directly. It can also pass
every connection that is not a valid client to a decoy server, so a probe sees a real website
instead of a closed connection. These are the `obfs_mode` and `obfs_fallback` fields of a
`"type": "shadowsocks"` inbound, and they work with one user, many users (`users`) and relay
(`destinations`) inbounds.

## Why use it

- To serve Shadowsocks clients that use `obfs-local` (Shadowsocks apps, and sing-box's own
  Shadowsocks outbound with `"plugin": "obfs-local"`) without running a separate `obfs-server`.
- To make the server look like an ordinary web server to anyone who connects to it without the
  right password.

## How it gets past filtering

- simple-obfs wraps the start of each connection in an HTTP WebSocket upgrade request (`http`) or
  a TLS ClientHello (`tls`), so plain Shadowsocks traffic, which looks random, starts like web
  traffic.
- Filters often probe suspected servers: they connect and send their own data, or replay a
  recorded client request, and watch the reply. With `obfs_fallback`, such a probe is connected to
  the decoy, for example a real website on the same port, and gets its normal answer.

simple-obfs is old and its HTTP and TLS forms are easy to recognize for a filter that checks them
closely; the TLS form is not real TLS. Use it for clients that cannot use anything else.

## How it works

- With `obfs_mode` set, the inbound reads the client's first request. For `http`, it must be a GET
  with `Upgrade: websocket`; for `tls`, a ClientHello with simple-obfs' exact layout. The server
  replies with an HTTP 101 or a TLS ServerHello, and the Shadowsocks data inside is passed on.
- With `obfs_fallback` set, the inbound keeps a copy of what the client sent (up to 16 KB) until
  Shadowsocks has authenticated the client. If anything fails before that, the connection and the
  copied bytes go to the fallback address. This covers:
  - connections that are not simple-obfs, such as a browser or a scanner (like `obfs-server
    --failover`);
  - connections that pass obfs but fail Shadowsocks: an unknown user, a wrong password or a
    replayed request. So a probe that copies a real client's obfs request also gets the decoy.
- After authentication, nothing more is recorded, and a later error closes the connection.
- The fallback connection is routed like any other connection from the inbound, with the fallback
  address as its destination, so your route rules decide which outbound reaches it (usually
  `direct`).
- obfs applies to TCP only. Shadowsocks UDP is not changed.

## Configuration

```json
{
  "inbounds": [
    {
      "type": "shadowsocks",
      "listen": "::",
      "listen_port": 443,
      "method": "2022-blake3-aes-128-gcm",
      "password": "8JCsPssfgS8tiRwiMlhARg==",
      "users": [{ "name": "alice", "password": "PCD2Z4o12bKUoFa3cC97Hw==" }],
      "obfs_mode": "tls",
      "obfs_fallback": { "server": "www.example.com", "server_port": 443 }
    }
  ]
}
```

A matching client:

```json
{
  "outbounds": [
    {
      "type": "shadowsocks",
      "server": "203.0.113.1",
      "server_port": 443,
      "method": "2022-blake3-aes-128-gcm",
      "password": "8JCsPssfgS8tiRwiMlhARg==:PCD2Z4o12bKUoFa3cC97Hw==",
      "plugin": "obfs-local",
      "plugin_opts": "obfs=tls;obfs-host=www.example.com"
    }
  ]
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `obfs_mode` | string | `""` | `http` or `tls`: run the simple-obfs server. Empty: no obfs. |
| `obfs_fallback` | object | — | Decoy server for connections that fail obfs or Shadowsocks authentication: `server` and `server_port`. Needs `obfs_mode`. |
| `obfs_host` | string | `""` | Hosts the client may use, comma-separated. When set, a client whose HTTP `Host` or TLS server name is not listed is treated as not simple-obfs: it goes to `obfs_fallback`, or is closed. Empty allows any host. Needs `obfs_mode`. |

Errors: an `obfs_mode` other than `http` or `tls`, `obfs_fallback` without `obfs_mode`, or a
fallback without a valid address and port is a configuration error. Without `obfs_fallback`, a
failed connection is closed.

## See also

- [finalmask](finalmask.md)
