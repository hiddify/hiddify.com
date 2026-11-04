# GooseRelay

[All Hiddify features](../../index.md)

GooseRelay sends your traffic through a Google Apps Script web app to your own server. To the
network, your device only talks HTTPS to a Google address with the name `www.google.com`. It is
an outbound: `"type": "gooserelay"` in the `outbounds` list. It is the client side of the
GooseRelayVPN project.

## Why use it

- It works on networks that block most servers but must leave Google reachable.
- It carries any TCP connection, not just web pages, because a real server of yours opens the
  connections.

You need two things set up first: a small server (VPS) running the GooseRelayVPN exit server,
and one or more Google Apps Script deployments of the GooseRelayVPN forwarder script. The
GooseRelayVPN project explains both. Each deployment has a daily limit on how many requests
Google runs for it, so heavy use needs several deployments.

## How it gets past filtering

The outbound connects to a Google address and uses `www.google.com` (or the names in `sni`) as
the TLS server name. Inside that TLS connection, the requests go to `script.google.com`. This is
called domain fronting: the filter sees a connection to Google, and Google sends the request to
your Apps Script. The script passes the data on to your server without reading it.

Everything is encrypted with AES-256-GCM using `tunnel_key`, which only your device and your
server know. Google never has the key.

It does not help when the Google address in `google_host` is blocked, or when Google stops
routing these requests.

## How it works

- After start, the outbound checks every deployment in `script_keys` at once. A check confirms
  that the deployment is public and runs the forwarder, then sends an encrypted probe to check
  that your server is reachable and the key matches. The outbound is ready when one deployment
  passes, and fails when all of them fail. Log messages say what is wrong, for example a wrong
  deployment ID or a key mismatch.
- Each connection becomes a session. Its data is sent in encrypted batches as HTTPS requests,
  and answers come back by long polling. Your server opens the real connection to the
  destination.
- Requests are spread over the deployments in `script_keys`, and over the names in `sni`. Each
  name gets its own TLS connections.

## Configuration

```json
{
  "type": "gooserelay",
  "tag": "goose",
  "script_keys": ["<Apps Script deployment ID>"],
  "tunnel_key": "<64 hex characters, same as on the server>"
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `script_keys` | list of strings | required | Apps Script deployment IDs. Paste only the ID, not the full URL. |
| `tunnel_key` | string | required | AES-256 key as 64 hex characters. It must match the server. |
| `google_host` | string | `"216.239.38.120:443"` | The Google address and port to connect to. Other Google front addresses also work. |
| `sni` | list of strings | `["www.google.com"]` | TLS server names to use. Several names spread the load. |
| `handshake_timeout` | duration | `10s` | How long the startup check may take. |
| `debug_timing` | bool | `false` | Log timing details of the relay. |
| `udp_over_tcp` | object | | The UDP over TCP setting from sing-box. The outbound accepts only TCP from the router, so routed UDP traffic does not use it. |

The carrier makes its own connections to Google, so the dial fields such as `detour` are not
used for them.

## See also

- [Monitoring](../groups/monitoring.md)
- [Fallback](../groups/fallback.md)
