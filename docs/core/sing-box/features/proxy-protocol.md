# PROXY protocol

[All Hiddify features](../index.md)

The PROXY protocol is a short header at the start of a TCP connection that says which client
address the connection really comes from. Upstream sing-box removed it in version 1.6. Hiddify
brings it back in two places: inbounds can read the header (`proxy_protocol` in the listen
fields), and the direct outbound can send it (`proxy_protocol` of `"type": "direct"`).

## Why use it

- **Inbound:** your server sits behind a load balancer, a CDN edge or a relay such as HAProxy or
  nginx stream. Without the header, every connection seems to come from the relay. With it, logs,
  stats and route rules on `source_ip_cidr` see the real client address.
- **Direct outbound:** sing-box forwards connections to a backend that expects the header, for
  example nginx or another proxy server with PROXY protocol turned on, so the backend sees the
  client address.

## How it gets past filtering

It does not. It only passes the client's address between servers you run.

## How it works

### Inbound

- When `proxy_protocol` is on, the inbound reads a version 1 (text) or version 2 (binary) header
  at the start of each TCP connection. The source and destination in the header become the
  connection's addresses.
- The header must arrive within 10 seconds. A slow client does not hold up the others, because
  headers are read in parallel.
- A connection without a valid header is closed. With `proxy_protocol_accept_no_header`, a
  connection that does not start with a header is used as it is, with its real addresses. A
  client that sends nothing until the server speaks is still closed after 10 seconds.
- A header with the LOCAL command (sent by health checks) keeps the connection's own addresses.
- It works for every inbound that listens on TCP. UDP is not affected.

### Direct outbound

- When `proxy_protocol` is `1` or `2`, the outbound writes a header of that version at the start
  of each new TCP connection, before any data. UDP is not affected.
- The source in the header is the address of the original client, as the inbound saw it. The
  destination is the address the outbound connected to.
- Both addresses must be of the same family. If the client used IPv4 and the destination is IPv6,
  or the other way round, the outbound's own local address is used as the source. If no pair
  matches, a LOCAL header is sent, so the backend uses the connection's own addresses.
- If the header cannot be written, the connection is closed and fails.

## Configuration

Inbound behind a load balancer:

```json
{
  "inbounds": [
    {
      "type": "vless",
      "tag": "vless-in",
      "listen": "::",
      "listen_port": 443,
      "proxy_protocol": true,
      "users": [{ "uuid": "<uuid>" }]
    }
  ]
}
```

Direct outbound that sends the header to a backend:

```json
{
  "outbounds": [
    {
      "type": "direct",
      "tag": "to-backend",
      "proxy_protocol": 2
    }
  ]
}
```

| Field | Where | Type | Default | Meaning |
|---|---|---|---|---|
| `proxy_protocol` | inbound listen fields | bool | `false` | Read a PROXY protocol header on each TCP connection, and close connections without one. |
| `proxy_protocol_accept_no_header` | inbound listen fields | bool | `false` | Read the header, and also accept connections that do not start with one. Turns the reading on by itself. |
| `proxy_protocol` | `direct` outbound | int | `0` | `0` sends nothing, `1` sends a version 1 header, `2` a version 2 header. Other values are an error. |

Turn on `proxy_protocol` on an inbound only when every client reaches it through a relay that
sends the header. Otherwise anyone can send a header and claim any source address.

## See also

- [SSH: inbound and Hiddify additions](protocols/ssh.md)
