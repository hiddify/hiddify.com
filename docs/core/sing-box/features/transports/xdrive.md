# XDRIVE transport

[All Hiddify features](../../index.md)

XDRIVE is Xray-core's storage transport. The client and the server never connect to each other:
the client writes the connection's data as files in a storage service, and the server reads them
there and writes its replies back. The storage can be Google Drive, any S3 service, a service
described as a "template" of HTTP requests, or a local folder. In this fork it is a V2Ray
transport, set in the `transport` block of a VLESS inbound or outbound with `"type": "xdrive"`.

## Why use it

- It works when every route to the server is blocked: the client only talks to the storage
  service, such as Google's APIs, which a filter rarely blocks.
- It connects to Xray servers that use XDRIVE.
- The server needs no open port and no public address; it only has to reach the storage.

## How it gets past filtering

To a filter, the client is an app syncing files with Google Drive or S3: HTTPS requests to the
service's own domain, with a Chrome TLS fingerprint and Chrome HTTP headers. The server's address
never appears on the client's network. `fronting_address` can send those requests to another
address of the service, for example a Google front IP, while the TLS server name stays the
service's own.

It is slow and costly: every write is a file upload and the other side polls for it, so the
round trip is hundreds of milliseconds or more, and the service's API quota limits how much
passes. Use it as a last resort, not for daily traffic.

## How it works

- The client opens a session by writing an announce file with a random session id in
  `remote_folder`. The server lists the folder, claims the session and answers in it.
- Each direction is a series of segments, files of up to `segment_bytes`. Data written within
  `flush_interval_ms` goes in one segment. The reader polls every `poll_interval_ms`, backing off
  up to `max_poll_interval_ms` when nothing comes.
- On Google Drive, a session uses a ring of slot files that are overwritten instead of new files
  for every segment.
- Old sessions are deleted after `session_ttl_seconds`.
- The requests to the storage are Xray's own client, over h2, or h3 when the TLS `alpn` is
  `["h3"]` alone, with XMUX for connection reuse. Every socket it opens goes through the
  outbound's dialer, so `detour`, the interface options and the outbound's `finalmask` apply.
- One proxy connection is one session. Xray's XDRIVE client always runs Mux.Cool on top so that
  one session carries many connections. This fork's VLESS server accepts that, but its client has
  no Mux.Cool, so it opens a session per connection.

## Configuration

A VLESS client over Google Drive, and the server side in the same folder:

```json
{
  "outbounds": [
    {
      "type": "vless",
      "server": "127.0.0.1",
      "server_port": 1,
      "uuid": "bf000d23-0752-40b4-affe-68f7707a9661",
      "encryption": "mlkem768x25519plus.native.0rtt.…",
      "tls": { "enabled": true, "utls": { "enabled": true, "fingerprint": "chrome" } },
      "transport": {
        "type": "xdrive",
        "service": "google-drive",
        "remote_folder": "1AbCdEfGhIjKlMnOpQrStUvWxYz",
        "secrets": ["<client id>", "<client secret>", "<refresh token>"]
      }
    }
  ],
  "inbounds": [
    {
      "type": "vless",
      "listen": "127.0.0.1",
      "listen_port": 1,
      "users": [{ "uuid": "bf000d23-0752-40b4-affe-68f7707a9661" }],
      "decryption": "mlkem768x25519plus.native.600s.…",
      "transport": {
        "type": "xdrive",
        "service": "google-drive",
        "remote_folder": "1AbCdEfGhIjKlMnOpQrStUvWxYz",
        "secrets": ["<client id>", "<client secret>", "<refresh token>"]
      }
    }
  ]
}
```

The outbound's `server` and `server_port` are required by VLESS but not used. The inbound's
listen port is closed as soon as the transport starts: the server reads the storage instead.

| Field | Type | Default | Meaning |
|---|---|---|---|
| `service` | string | — | `google-drive`, `s3`, `template` or `local`. Required. |
| `remote_folder` | string | — | The folder: a Drive folder id, an S3 key prefix, or a local directory. |
| `secrets` | string list | — | `google-drive`: client id, client secret, refresh token. `s3`: access key id, secret access key and an optional session token. `template`: the values its requests refer to. |
| `s3` | object | — | For `s3`: `endpoint`, `region`, `bucket`, `path_style` (default `true`). |
| `template` | object | — | For `template`: the HTTP requests for put, get, list and delete, as in Xray. |
| `segment_bytes` | number | `524288` | Largest segment file, at most 16 MiB. |
| `flush_interval_ms` | number | `20` | How long writes are gathered into one segment. |
| `poll_interval_ms`, `max_poll_interval_ms` | number | `50`, `500` | First and longest wait between polls. |
| `session_ttl_seconds` | number | `300` | When an idle session's files are deleted. |
| `concurrency` | number | `8` | Requests in flight per session, at most 64. |
| `eager_window_ms` | number | `2000` | How long after the last data the reader keeps polling at the fast rate. |
| `hole_timeout_ms` | number | `30000` | How long to wait for a missing segment before the session fails. |
| `xmux` | object | 4 connections on Google Drive over h2, else 1 | Connection reuse, the same fields as XHTTP's `xmux`. |
| `fronting_address`, `fronting_port` | string, number | — | Dial this address for every host of the service; the TLS server name stays the host's. |

The outbound's `tls` sets the TLS of the requests to the storage: its `server_name`, `alpn` and
uTLS `fingerprint`. A server name equal to the outbound's `server` is ignored, since XDRIVE never
connects there. Without `tls`, or without uTLS, the requests use a Chrome fingerprint and each
host's own name.

## Notes

- Xray allows XDRIVE only for VLESS with `encryption` (run `xray vlessenc` for a key pair) and no
  `flow`. Use the same with an Xray server.
- The transport is built with the `with_xdrive` tag, which the Makefile and hiddify-core turn on.
- Xray has no share link for XDRIVE. hiddify-core writes an Xray JSON outbound with XDRIVE as a
  VLESS link with `type=xdrive` and Xray's `xdriveSettings` as JSON in `xdrive=` (the stream's
  `address` and `port` included, for fronting), and ray2sing reads that link back.
- The `local` service is for tests and for a client and a server on one machine or a shared disk.
- Tested against Xray-core 26.10.31 in both directions over the `local` service
  (`h_xray_xdrive_interop_test.go`).

## See also

- [finalmask](finalmask.md)
- [XHTTP transport](xhttp.md)
