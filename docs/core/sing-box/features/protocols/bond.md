# Bond

[All Hiddify features](../../index.md)

Bond splits every connection over several connections at once, called legs, and joins them
again on the server. The legs can be any outbounds: different protocols, servers, ports or
networks. It is the outbound and inbound `"type": "bond"`, and it needs the `with_bond` build
tag.

## Why use it

- One connection is throttled to a low speed, but several in parallel are not: bond adds them up.
- You want each part of the traffic to take a different path, so no single connection carries
  the whole stream.

It does not make a connection more reliable: when one leg fails, the bonded connection fails.

## How it gets past filtering

Each leg is an ordinary connection of its own protocol (VLESS, Trojan…), so each looks like that
protocol. A censor that reads one leg sees only part of the data. Bond adds no obfuscation of its
own; the legs' protocols and transports do that.

## How it works

- For each connection, the client opens one connection through every leg at once and sends a
  short header on each: a connection ID, the leg's number, the number of legs, the ratios and the
  destination.
- The server waits for all legs of a connection (up to the connect timeout; legs that never all
  arrive are closed), then routes the joined connection to the destination.
- Data goes in frames of at most 64 KiB. Each frame is split over the legs by the ratios: with
  upload ratios 60 and 40, the first leg carries 60% of each frame.
- UDP travels over TCP (UDP over TCP) inside the bonded connection.

## Configuration

Outbound:

```json
{
  "type": "bond",
  "tag": "bond",
  "outbounds": [
    { "outbound": { "type": "vless", "server": "a.example.com", "server_port": 443, "uuid": "…" },
      "download_ratio": 30, "upload_ratio": 60 },
    { "outbound": { "type": "vless", "server": "b.example.com", "server_port": 443, "uuid": "…" },
      "download_ratio": 70, "upload_ratio": 40, "count": 1 }
  ]
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `outbounds` | list | required | The legs. |
| `outbounds[].outbound` | outbound | required | A full outbound, written inline as in `outbounds`. |
| `outbounds[].download_ratio` | number | `0` | Percent of the download this leg carries. |
| `outbounds[].upload_ratio` | number | `0` | Percent of the upload this leg carries. |
| `outbounds[].count` | number | `1` | How many legs of this outbound to open; each gets the ratios above. |

The download ratios of all legs must add up to 100, and so must the upload ratios, counting each
leg made by `count`. At most 255 legs.

Inbound:

```json
{
  "type": "bond",
  "tag": "bond-in",
  "inbounds": [
    { "type": "vless", "listen": "::", "listen_port": 443, "users": [{ "uuid": "…" }] },
    { "type": "vless", "listen": "::", "listen_port": 8443, "users": [{ "uuid": "…" }] }
  ]
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `inbounds` | list of inbounds | required | The inbounds the legs arrive on, written inline. Other connections on them are routed as usual. |

Route rules see bonded connections as coming from the bond inbound's tag. Ported from
sing-box-extended, with fixes: writes larger than 64 KiB, ratio totals, legs that never all
arrive.

## See also

- [Balancer](../groups/balancer.md)
- [Fallback](../groups/fallback.md)
