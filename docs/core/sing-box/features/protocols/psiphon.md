# Psiphon

[All Hiddify features](../../index.md)

The Psiphon outbound connects to the Psiphon network through the official Psiphon tunnel core,
built into sing-box. Psiphon runs the servers, so you only need this outbound. It is an
outbound: `"type": "psiphon"` in the `outbounds` list.

## Why use it

- You get a working proxy with no server of your own and no account.
- It is a good last resort when your own servers are blocked: Psiphon keeps many servers and
  many ways to reach them, and updates its server list by itself.
- You can pick the country the traffic leaves from with `egress_region`.

Psiphon is shared by many users. It is often slower than your own server, and it carries TCP
only.

## How it gets past filtering

Psiphon does the work, not sing-box. The tunnel core knows many Psiphon servers and several
obfuscated protocols to reach them. It tries them until one connects, and downloads a signed,
updated server list once it is in. When one server or protocol is blocked, it moves to another.

It does not help when the network blocks all traffic to the outside, or when every Psiphon
server it knows is blocked and it cannot fetch a new list.

## How it works

- At start, the outbound builds a Psiphon config (see `config` below), opens its data store in
  `data_directory`, and starts the tunnel core in the background. Startup does not wait for the
  tunnel.
- Until the tunnel is up, the outbound shows "Connecting..." and connections through it fail.
  When the first tunnel is up, the mark goes away, and Hiddify's
  [monitoring](../groups/monitoring.md) tests it at once.
- The tunnel core makes its own connections to Psiphon servers. These go through this
  outbound's dial settings (for example `detour`), through a local SOCKS bridge, so they do
  not loop back into your VPN. If you set `upstream_proxy_url`, that proxy is used instead.
- When the network changes, the outbound tells the tunnel core to reconnect.
- When the tunnel core stops (it gives up after `establish_tunnel_timeout`, or fails), it is
  started again after 5 seconds, then twice as long each time, up to every 5 minutes; a
  connection resets the wait.
- Several Psiphon outbounds can run at once, for example one per `egress_region`. Each keeps its
  downloads in `data_directory/<tag>`; what an earlier version kept in `data_directory` itself is
  moved there. The tunnel core reports its state without saying which outbound it is about, so
  next to other Psiphon outbounds each one checks its own tunnel before it shows as connected.
- Each TCP connection is opened through the Psiphon tunnel to its real destination. UDP is not
  supported.

## Configuration

```json
{
  "type": "psiphon",
  "tag": "psiphon",
  "egress_region": "DE"
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `config` | string | `""` | A Psiphon config to start from. `"hiddify"` uses the config built into the Hiddify app, if this build has one; otherwise a warning is logged and the defaults are used. Any other value is the Psiphon JSON config, either encrypted with this build's key or in base64. Empty means the defaults. |
| `data_directory` | string | `"data/psiphon"` | Where Psiphon keeps its data: each outbound in a folder named after its tag. |
| `egress_region` | string | `""` | Two-letter country code of the exit server, for example `"US"` or `"DE"`. Empty lets Psiphon choose. |
| `propagation_channel_id` | string | `"FFFFFFFFFFFFFFFF"` | Psiphon client identity value. |
| `sponsor_id` | string | `"FFFFFFFFFFFFFFFF"` | Psiphon client identity value. |
| `network_id` | string | `"test"` | Psiphon network ID. |
| `client_platform` | string | built-in value | Platform string sent to Psiphon. |
| `client_version` | string | `""` | Version string sent to Psiphon. |
| `remote_server_list_url` | string | Psiphon's public list URL | Where to download the server list. |
| `remote_server_list_download_filename` | string | `"remote_server_list"` | File name for the downloaded list. |
| `remote_server_list_signature_public_key` | string | Psiphon's public key | Key that checks the list's signature. |
| `upstream_proxy_url` | string | `""` | Send Psiphon's own connections through this proxy, for example `socks5://127.0.0.1:1080`. Empty uses the outbound's dial settings. |
| `allow_default_dns_resolver_with_bind_to_device` | bool | `true` | Let Psiphon use the system DNS resolver while bound to a network interface. |
| `establish_tunnel_timeout` | duration | `1m` | How long the tunnel core tries to connect before it gives up. Values under one second count as one second. |

The usual dial fields (`detour`, `bind_interface` and the rest) also apply, as described above.
The `network` field is accepted but has no effect: the outbound is TCP only.

For each identity and server list field, the order is: the value set in the outbound, then the
value in `config`, then the default.

## See also

- [Monitoring](../groups/monitoring.md)
- [Balancer](../groups/balancer.md)
