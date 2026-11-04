# mKCP transport

[All Hiddify features](../../index.md)

mKCP carries a proxy protocol (VLESS, VMess, Trojan…) over UDP with KCP, a reliable protocol
that resends lost packets fast. It is the V2Ray transport `"type": "mkcp"` (or `"kcp"`) of an
outbound or inbound, and it is the same mKCP as in Xray 26.

## Why use it

- The network drops or throttles TCP but lets UDP through.
- The link loses many packets: KCP resends sooner than TCP and keeps the speed up, at the cost
  of more traffic.
- You connect to an Xray server that offers mKCP.

## How it gets past filtering

On its own, mKCP is plain UDP with a recognizable header. To hide it, give the outbound a
[finalmask](finalmask.md) UDP mask, as Xray does since mKCP's `header` and `seed` moved
there:

- `mkcp-legacy` with `value` encrypts every packet with AES-GCM (the old `seed`).
- `mkcp-legacy` with `header` (`dns`, `dtls`, `srtp`, `utp`, `wechat`, `wireguard`) makes each
  packet look like that protocol (the old `header`).
- Other UDP masks (`noise`, `salamander`, …) work as well.

The server must use the same masks. TLS can run inside mKCP with the outbound's `tls` block.

## How it works

- The client opens one UDP socket per connection and runs one KCP session on it.
- The server reads all sessions from the inbound's UDP port and tells them apart by the sender
  and the session number.
- There is no handshake of its own: the proxy protocol inside starts at once.

## Configuration

Needs the `with_kcp` build tag. Without it, a config with mKCP fails with "mKCP is not included
in this build".

```json
{
  "type": "vless",
  "server": "example.com",
  "server_port": 4443,
  "uuid": "b831381d-6324-4d53-ad4f-8cda48b30811",
  "transport": { "type": "mkcp", "uplink_capacity": 20, "downlink_capacity": 100 },
  "finalmask": { "udp": [{ "type": "mkcp-legacy", "settings": { "value": "a password" } }] }
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `mtu` | number | `1350` | Largest packet, in bytes. At least `21`. |
| `tti` | number | `50` | Update interval in milliseconds, `10` to `1000`. Lower is faster and uses more traffic. |
| `uplink_capacity` | number | `5` | Upload speed to aim for, in MB/s. |
| `downlink_capacity` | number | `20` | Download speed to aim for, in MB/s. |
| `cwnd_multiplier` | number | `1` | Scales the congestion window. |
| `max_sending_window` | number | `2097152` | Largest send buffer, in bytes. At least `mtu`. |

The fields and defaults are Xray 26's `kcpSettings`. Tested in both directions against Xray
26.10.21 and 26.3.27, plain and with the `aes128gcm` and `wechat` masks. Xray 26.3 names these
masks `mkcp-aes128gcm` and `header-wechat`; they are the same on the wire.

Inbounds do not take finalmask, so a Hiddify mKCP server works only without masks.

## See also

- [finalmask](finalmask.md)
- [XHTTP](xhttp.md)
