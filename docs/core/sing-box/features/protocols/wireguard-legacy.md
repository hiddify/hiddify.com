# WireGuard outbound (legacy format)

[All Hiddify features](../../index.md)

Upstream sing-box removed the WireGuard outbound in version 1.13; WireGuard is now an endpoint.
Hiddify brings the outbound back under a new type name, so configs written in the old format keep
working. It is an outbound: `"type": "wireguard_legacy"` in the `outbounds` list. The fields are
those of the old `wireguard` outbound.

## Why use it

- You have a config or a converter that writes the old WireGuard outbound, and you do not want to
  rewrite it as an endpoint.

For new configs, use the [WireGuard endpoint](wireguard-hiddify.md). It has the Hiddify
additions (noise packets, recovery, peer names), and this outbound does not.

## How it gets past filtering

It does not. It is plain WireGuard, which a filter can recognize by its handshake. For
obfuscation, use the [WireGuard endpoint](wireguard-hiddify.md) with noise, or
[AmneziaWG](amneziawg.md).

## How it works

- It runs the same WireGuard engine as the endpoint, with a user-space network stack, or with a
  system interface when `system_interface` is set.
- With `peers`, each peer has its own address, keys and allowed IPs. Without `peers`, the
  top-level `server`, `server_port`, `peer_public_key`, `pre_shared_key` and `reserved` make one
  peer that receives all traffic (`0.0.0.0/0` and `::/0`).
- A domain as destination is resolved with the default DNS rules, then the connection goes
  through the tunnel. A peer given by domain is resolved the same way.
- TCP, UDP and ping go through the tunnel. `network` limits TCP and UDP; ping is always offered.
- The type is still reported as `wireguard`, so the app shows it as WireGuard.

## Configuration

```json
{
  "outbounds": [
    {
      "type": "wireguard_legacy",
      "tag": "wg-out",
      "server": "203.0.113.10",
      "server_port": 51820,
      "local_address": ["10.8.0.2/32"],
      "private_key": "<base64 private key>",
      "peer_public_key": "<base64 server public key>"
    }
  ]
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `local_address` | list of prefixes | required | Addresses of this side of the tunnel. |
| `private_key` | string | required | Private key, base64. |
| `server` | string | none | Server address, when `peers` is empty. |
| `server_port` | int | none | Server port, when `peers` is empty. |
| `peer_public_key` | string | none | Server public key, base64, when `peers` is empty. |
| `pre_shared_key` | string | none | Pre-shared key, base64, when `peers` is empty. |
| `reserved` | list of 3 bytes | none | Reserved bytes for the peer, when `peers` is empty. Cloudflare WARP uses them. |
| `peers` | list of objects | none | Several peers. Each has `server`, `server_port`, `public_key`, `pre_shared_key`, `allowed_ips` (required) and `reserved`. |
| `mtu` | int | `1408` | MTU of the tunnel. |
| `workers` | int | number of CPUs | WireGuard worker count. |
| `system_interface` | bool | `false` | Use a system network interface instead of the user-space stack. |
| `interface_name` | string | none | Name of the system interface. |
| `network` | `"tcp"` or `"udp"` | both | Networks the outbound accepts, as in upstream's old outbound. Ping is always accepted. |
| `gso` | bool | `false` | Accepted for old configs, but not used. It cannot be used with `detour`. |

The dial fields (`detour`, `bind_interface` and the rest) work as for other outbounds. There is no
keepalive option, as in upstream's old outbound.

## See also

- [WireGuard: Hiddify additions](wireguard-hiddify.md)
- [AmneziaWG](amneziawg.md)
- [WARP](warp.md)
