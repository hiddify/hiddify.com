# XHTTP transport

[All Hiddify features](../../index.md)

XHTTP is Xray's HTTP transport. It carries a proxy connection as ordinary HTTP requests and
responses: one long download response, and the upload either as many small requests or as one
streaming request. In this fork it is a V2Ray transport, so you set it in the `transport` block of
a VLESS, VMess or Trojan inbound or outbound with `"type": "xhttp"`.

## Why use it

- It works through CDNs and reverse proxies (nginx, Caddy) that pass plain HTTP but break
  WebSocket or gRPC.
- It connects to Xray servers that use XHTTP, so you can use the same server for Xray and
  Hiddify clients.
- It can split upload and download across different addresses or CDNs (`download`).

## How it gets past filtering

To a filter, XHTTP looks like a browser talking to a website over HTTPS: normal GET and POST
requests with a Chrome User-Agent, random padding of random length on every request and response,
and no long-lived upgrade to another protocol. Behind a CDN, the filter only sees a connection to
the CDN. The padding and the obfs options (`x_padding_obfs_mode`) change where the padding and the
session data appear, so a request does not have a fixed shape.

It does not hide the server from a filter that blocks the server's IP address or domain, unless
you put a CDN in front of it. Without TLS (or REALITY), the requests are readable.

## How it works

- The client opens one download request (GET) per proxy connection and reads the server's data
  from its response.
- The upload depends on the mode:
  - `packet-up`: the client sends its data in many POST requests, each with a sequence number.
    This works through almost every CDN and proxy.
  - `stream-up`: the client sends its data in one long streaming POST request. Faster, but the
    path must allow a streaming request body.
  - `stream-one`: upload and download share one streaming request. Needs a path that passes
    streaming in both directions, such as a direct TLS or REALITY connection.
  - `auto`: on the server, it accepts all three modes. On the client, it picks as Xray's client
    does: `stream-one` over REALITY, `stream-up` over REALITY with a separate `download`, and
    `packet-up` otherwise. An empty mode is `auto`.
- The upload and download requests of one connection carry the same random session ID. By
  default it is part of the path; `session_placement` and `seq_placement` move the session ID and
  the sequence number into a query parameter, a header or a cookie.
- The HTTP version follows the TLS ALPN: no TLS or `http/1.1` is HTTP/1.1, `h2` is HTTP/2, and
  `h3` is HTTP/3 over QUIC (UDP). A server whose only ALPN is `h3` listens on UDP.
- XMUX reuses HTTP connections for several proxy connections; the `xmux` options limit how much
  one HTTP connection is reused.

## Configuration

A VLESS client and a matching server:

```json
{
  "outbounds": [
    {
      "type": "vless",
      "tag": "proxy",
      "server": "example.com",
      "server_port": 443,
      "uuid": "bf000d23-0752-40b4-affe-68f7707a9661",
      "tls": {
        "enabled": true,
        "server_name": "example.com",
        "alpn": ["h2"],
        "utls": { "enabled": true, "fingerprint": "chrome" }
      },
      "transport": {
        "type": "xhttp",
        "mode": "packet-up",
        "path": "/assets",
        "x_padding_bytes": "100-1000"
      }
    }
  ]
}
```

```json
{
  "inbounds": [
    {
      "type": "vless",
      "listen": "::",
      "listen_port": 443,
      "users": [{ "uuid": "bf000d23-0752-40b4-affe-68f7707a9661" }],
      "tls": {
        "enabled": true,
        "server_name": "example.com",
        "alpn": ["h2", "http/1.1"],
        "certificate_path": "/etc/ssl/example.com.crt",
        "key_path": "/etc/ssl/example.com.key"
      },
      "transport": { "type": "xhttp", "mode": "auto", "path": "/assets" }
    }
  ]
}
```

A range field takes a string `"from-to"`, a single number, or `{"from": 1, "to": 2}`.

| Field | Type | Default | Meaning |
|---|---|---|---|
| `mode` | string | `auto` | `auto`, `packet-up`, `stream-up` or `stream-one`. On a server, a mode other than `auto` rejects requests of the other modes. |
| `host` | string | TLS server name, then server address | HTTP Host of the requests. On the server, requests for another host are refused. |
| `path` | string | `/` | Request path. It may carry a query (`/path?ed=2048`), which is sent with every request. |
| `headers` | object | — | Extra request headers. Must not contain `Host`. A `User-Agent` is set to Chrome's if missing. |
| `x_padding_bytes` | range | `100-1000` | Length of the random padding added to each request and response. It cannot be 0. |
| `x_padding_obfs_mode` | bool | `false` | Use the four options below for the padding. Off, the padding goes into the `Referer` query (client) and the `X-Padding` header (server), as older Xray does. |
| `x_padding_placement` | string | `queryInHeader` | Where the padding goes: `queryInHeader`, `header`, `query` or `cookie`. |
| `x_padding_key` | string | `x_padding` | Query or cookie name of the padding. |
| `x_padding_header` | string | `X-Padding` | Header that carries the padding (for `header` and `queryInHeader`). |
| `x_padding_method` | string | `repeat-x` | `repeat-x` (a run of `X`) or `tokenish` (random base62 text that looks like a token). |
| `session_placement` | string | `path` | Where the session ID goes: `path`, `query`, `header` or `cookie`. |
| `session_key` | string | `x_session` (query, cookie), `X-Session` (header) | Name of the session ID's query, header or cookie. |
| `seq_placement` | string | `path` | Where the packet-up sequence number goes: `path`, `query`, `header` or `cookie`. Must be `path` when `session_placement` is `path`. |
| `seq_key` | string | `x_seq` (query, cookie), `X-Seq` (header) | Name of the sequence number's query, header or cookie. |
| `uplink_http_method` | string | `POST` | HTTP method of upload requests. `GET` is allowed only in `packet-up`. |
| `uplink_data_placement` | string | `body` | Where upload data goes: `body`, or `header` / `cookie` (only in `packet-up`). |
| `uplink_data_key` | string | `x_data` (cookie), `X-Data` (header) | Name of the header or cookie that carries upload data. |
| `uplink_chunk_size` | integer | 4096 (header), 3072 (cookie) | Size of each upload data chunk in a header or cookie. At least 64. |
| `no_grpc_header` | bool | `false` | Do not send `Content-Type: application/grpc` on upload requests. |
| `no_sse_header` | bool | `false` | Server: do not send `Content-Type: text/event-stream` on download responses. |
| `sc_max_each_post_bytes` | range | `1000000` | Largest packet-up upload request, in bytes. |
| `sc_min_posts_interval_ms` | range | `30` | Client: least time between two packet-up uploads, in milliseconds. |
| `sc_max_buffered_posts` | integer | `30` | Server: packet-up uploads kept while waiting for a missing one. |
| `sc_stream_up_server_secs` | range | `20-80` | Server: how often, in seconds, it sends padding on a stream-up response so proxies keep it open. |
| `xmux` | object | see below | Reuse of HTTP connections. |
| `download` | object | — | Client: send the download request somewhere else. See below. |

`xmux` fields (all ranges). When `xmux` is not set, `max_concurrency` is 1,
`h_max_request_times` is 600-900 and `h_max_reusable_secs` is 1800-3000.

| Field | Type | Default | Meaning |
|---|---|---|---|
| `max_concurrency` | range | `0` | Proxy connections per HTTP connection. Cannot be set with `max_connections`. |
| `max_connections` | range | `0` | Number of HTTP connections to open and share. |
| `c_max_reuse_times` | range | `0` | How many proxy connections one HTTP connection serves before it is retired. |
| `h_max_request_times` | range | `0` | How many HTTP requests one HTTP connection sends before it is retired. |
| `h_max_reusable_secs` | range | `0` | Seconds after which an HTTP connection is no longer reused. |
| `h_keep_alive_period` | integer | HTTP/2: Chrome's; HTTP/3: quic-go's | Keepalive period in seconds. Negative turns it off. |

A `0` means no limit.

`download` takes the same fields as the transport (except `mode`) plus `server`, `server_port`,
`tls` (the same form as the outbound's `tls`) and `detour` (an outbound tag to dial through).
The upload goes to the outbound's server and the download to this one; both servers must reach
the same XHTTP server behind them, for example two CDNs in front of one origin.

Compatibility: tested in both directions against Xray 26.3.27 and 26.10.21. Option names are the
snake_case forms of Xray's names (`xPaddingBytes` is `x_padding_bytes`). Both sides must use the
same path, padding placement and session/seq placement. A wrong option is a configuration error
when the config loads.

## See also

- [REALITY in Hiddify](../reality-hiddify.md)
- [VLESS encryption](../protocols/vless-encryption.md)
- [finalmask](finalmask.md)
