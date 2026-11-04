# Custom gRPC paths

[All Hiddify features](../../index.md)

The gRPC transport's `service_name` can be a full custom path, as in Xray. A name that starts with
`/` is read as `/<service>/<stream>`, so `/my/path/Tun` sends requests to the path
`/my/path/Tun`. Any other name works as before and gives the path `/<service_name>/Tun`. This is
the `service_name` field of a `"type": "grpc"` transport, on clients and servers.

## Why use it

- To connect to Xray servers that use a custom gRPC path. Before, sing-box always sent
  `/<service_name>/Tun` and could not reach them.
- To let Xray clients with a custom path connect to a sing-box server.
- To pick a path that fits the site behind a CDN or reverse proxy, instead of one that ends in
  `/Tun`.

## How it gets past filtering

It does not change how gRPC looks; it only lets you choose the request path. A path that matches
the decoy site makes the traffic less distinct for a filter that inspects decrypted traffic (a CDN
or a reverse proxy that routes by path). It does not help against a filter that cannot see inside
TLS.

## How it works

- `/<service>/<stream>`: everything between the first `/` and the last `/` is the service, and
  the part after the last `/` is the stream. `/my/path/Tun` is service `my/path`, stream `Tun`.
- Xray's server form `/<service>/<stream>|<multi stream>` also names the stream of Xray's multi
  mode, which sing-box does not use; the part after `|` is ignored. So a server can use the same
  value as an Xray server, such as `/my/path/Tun|TunMulti`.
- Each path segment is URL-escaped, as in Xray.
- A name without a leading `/` is the service and the stream is `Tun`, as before.
- Both gRPC implementations read the name the same way: the full gRPC one (in builds with the
  `with_grpc` tag) and the built-in gRPC-lite one.

## Configuration

```json
{
  "outbounds": [
    {
      "type": "vless",
      "server": "example.com",
      "server_port": 443,
      "uuid": "bf000d23-0752-40b4-affe-68f7707a9661",
      "tls": { "enabled": true, "server_name": "example.com", "alpn": ["h2"] },
      "transport": { "type": "grpc", "service_name": "/my/path/Tun" }
    }
  ]
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `service_name` | string | `""` | A plain name (the path is `/<name>/Tun`), or a custom path `/<service>/<stream>`, optionally followed by `\|<multi stream>` (ignored). |

Client and server must give the same path. Tested in both directions, with both
implementations, against Xray 26.10.21 and 26.3.27.

## See also

- [XHTTP transport](xhttp.md)
