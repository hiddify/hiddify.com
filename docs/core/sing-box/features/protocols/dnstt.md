# DNSTT

[All Hiddify features](../../index.md)

DNSTT carries your traffic inside DNS queries and answers. The client sends queries for names
under a domain you control, through public DNS resolvers, and your DNSTT server answers them. It
is an outbound: `"type": "dnstt"` in the `outbounds` list. The client is built on VayDNS, a
DNSTT fork, and can also talk to original DNSTT servers.

## Why use it

- It works on networks where almost everything is blocked but DNS through public or local
  resolvers still works.
- It finds working resolvers by itself from a built-in list, and remembers which ones worked.

It is slow: each query carries only a little data, and resolvers limit how many queries they
take. Use it when nothing else gets through, not as your everyday connection.

## How it gets past filtering

The filter sees only DNS queries to a resolver, for names under your domain. The resolver
forwards them to your server, because your server is the authority for that domain. The data in
the queries is encrypted with the Noise protocol, so the resolver and the filter cannot read
it. Queries to a resolver can also go over DNS over HTTPS (DoH) or DNS over TLS (DoT), with a
browser TLS fingerprint (`utls`).

It does not help when DNS to every outside resolver is blocked or rewritten, or when the
resolvers you can reach drop long or unusual queries.

## How it works

- **Finding resolvers.** After start, the outbound checks each resolver in `resolvers`, up to
  100 at a time. A check sends a normal DNS query (`pretest-domain`, `pretest-record-type`),
  then opens a real tunnel through that resolver within 5 seconds. Each resolver that passes
  joins the pool, and checking stops adding once more than 10 are in use. The outbound is ready
  as soon as the first resolver passes.
- **History.** Each resolver gets a score from -10 to 10, saved in the cache file. Within the
  built-in list and within your own entries, resolvers with a better score are checked first.
- **Tunnel.** By default one tunnel spreads its queries over every resolver in the pool. With
  `single-resolver`, each resolver gets its own tunnel, and each connection uses one picked at
  random; a tunnel that fails is closed and rebuilt. With `smart_pool`, queries go to a local
  resolver pool that spreads them over the working resolvers, slows down for a resolver that
  rate-limits, and skips one that stops answering (see [Smart resolver pool](../dns/smart-dns-pool.md)).
- **Inside the tunnel.** The data runs over KCP for reliability, Noise for encryption, and smux
  so that many connections share one tunnel.
- **Destination.** The outbound does not choose where a connection goes. Every connection
  reaches your DNSTT server, which forwards it to the one service it is set up for, usually a
  SOCKS or SSH server. To use it, put that kind of outbound in front with `detour`.

TCP only. UDP is not supported.

## Configuration

The DNSTT server forwards to a SOCKS server, so a `socks` outbound runs through the `dnstt`
outbound. The `socks` server address is not used, because the DNSTT server decides where the
connection goes.

```json
{
  "outbounds": [
    {
      "type": "dnstt",
      "tag": "dnstt-out",
      "domain": "t.example.com",
      "pubkey": "<server public key, hex>",
      "resolvers": ["auto", "8.8.8.8:53", "https://dns.google/dns-query"]
    },
    {
      "type": "socks",
      "tag": "proxy",
      "server": "127.0.0.1",
      "server_port": 1080,
      "detour": "dnstt-out"
    }
  ]
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `domain` | string | required | The tunnel domain your DNSTT server is the authority for. |
| `pubkey` | string | required | The server's Noise public key, in hex. |
| `resolvers` | list of strings | required | Resolvers to use. `"1.1.1.1:53"` is plain DNS over UDP, `"https://..."` is DoH, `"dot://host:853"` is DoT. `"auto"` (or an empty string) adds the built-in list of about 58,000 public resolvers. At least one is needed. |
| `pretest-domain` | string | `"www.google.com"` | Name queried to check that a resolver answers. |
| `pretest-record-type` | string | `"a"` | Record type of that query: `a`, `aaaa`, `cname`, `mx`, `ns`, `ptr`, `soa`, `srv` or `txt`. |
| `record-type` | string | `"txt"` | Record type of the answers that carry data back from the server: `txt`, `cname`, `a`, `aaaa`, `mx`, `ns` or `srv`. It must match the server. Another value uses TXT. Each record type keeps its own saved resolver history. |
| `utls` | string | `""` | TLS fingerprint for DoH and DoT, for example `"Chrome"`, `"Firefox"`, `"iOS"` or `"random"`. Empty uses Go's own TLS. |
| `single-resolver` | bool | `false` | One tunnel per resolver instead of one tunnel over all of them. |
| `smart_pool` | bool or object | `false`; on by itself with several resolvers | Send queries through the outbound's own resolver pool, as described above: `true`, or an object with `load_balance`, `deadline`, `per_attempt`, `probe_interval`, `down_after` and `duplicate` (see [Smart resolver pool](../dns/smart-dns-pool.md)). A tunnel runs over one resolver, so with more than one the pool is on whatever this says. |
| `dnstt-compat` | bool | `false` | Use the original DNSTT wire format, for an original DNSTT server. |
| `clientid-size` | int | `2` | Client ID size in bytes. Ignored with `dnstt-compat`, which uses 8. Must match the server. |
| `max-qname-len` | int | `101` (`253` with `dnstt-compat`) | Longest query name to send. |
| `max-num-labels` | int | `0` (no limit) | Most data labels in a query name. |
| `rps` | number | `0` (no limit) | Most queries per second. |
| `mtu` | int | computed | Packet size inside the tunnel. When unset, it is computed from the domain and the two limits above. |
| `idle-timeout` | duration | `60s` (`2m` with `dnstt-compat`) | Close the session after this long with no answer. |
| `keepalive` | duration | `10s` | Interval between keep-alive messages. |
| `open-stream-timeout` | duration | `10s` | How long opening a connection in the tunnel may take. |
| `max-streams` | int | `0` (no limit) | Most connections at once in one tunnel. |
| `reconnect-min` | duration | `1s` | Shortest wait before the tunnel reconnects. |
| `reconnect-max` | duration | `30s` | Longest wait before the tunnel reconnects. |
| `session-check-interval` | duration | `20s` | How often the tunnel checks that its session is alive. |
| `handshake-timeout` | duration | `15s` | How long the Noise handshake may take. |
| `udp-timeout` | duration | `500ms` | For plain UDP resolvers: how long to wait for each answer. |
| `udp-workers` | int | `100`; with `smart_pool`: `300` | For plain UDP resolvers: queries in flight at once. With `smart_pool`, toward the pool, each worker keeps one socket. |
| `udp-shared-socket` | bool | `false` | For plain UDP resolvers: send every query from one socket instead of one socket per query. |
| `udp-accept-errors` | bool | `false` | For plain UDP resolvers: accept answers with an error code instead of dropping them. |
| `tunnel-per-resolver` | int | | Deprecated and ignored. |

The sockets that send the DNS queries use the outbound's socket settings, such as
`bind_interface` and `routing_mark`, and the platform's socket protection. So on a VPN the queries
do not loop back into the tunnel. `detour` is not supported: the queries go out directly, and the
log shows a warning.

`dnstt-compat` and `clientid-size` change the wire format, so they must match your server.

## See also

- [Smart resolver pool](../dns/smart-dns-pool.md)
- [Monitoring](../groups/monitoring.md)
