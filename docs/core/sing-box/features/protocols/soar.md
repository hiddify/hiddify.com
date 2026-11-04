# Soar

[All Hiddify features](../../index.md)

Soar carries your TCP connections inside DNS queries and answers, through recursive resolvers,
to a [Soar](https://github.com/getlantern/soar) server that you run as the authority for a
delegated zone. It is an outbound: `"type": "soar"` in the `outbounds` list. The client is the
Soar Go library from the Lantern team (`github.com/getlantern/soar`), used as it is.

## Why use it

- It works on networks where almost everything is blocked but DNS still passes, like the other
  DNS tunnels ([DNSTT](dnstt.md), [MasterDNS](masterdns.md)).
- It was designed against what censors and resolvers do: every resolver is a path with its own
  round-trip time, loss record, name and answer size limits and congestion window; losses are
  found fast at both ends and only the lost packets are sent again; the server holds idle
  queries and answers the moment it has data. Its project measures it ahead of the other DNS
  tunnels on lossy, rate-limited and Iran- and Russia-like networks, and it connects in about a
  second.
- It finds working resolvers by itself (discovery): from the device's own, a curated list for
  the country, and public resolvers. A resolver is used only once the server's signed answer
  came back through it, so hijacking resolvers are left out by the same test.
- The server connects to the destination itself: no SOCKS or SSH outbound behind it.

It is still a DNS tunnel: slow next to a direct proxy. The reference server only reaches public
addresses on ports 80 and 443 unless it is started with `-allow-ports`.

## How it gets past filtering

The filter sees DNS queries for names under your zone, sent to ordinary resolvers, which forward
them to your server. Every session starts with an X25519 key exchange signed by the server's
Ed25519 key, so a forged answer cannot authenticate and is ignored; data is sealed with
ChaCha20-Poly1305. Names start at 101 characters, which networks that drop long names still
pass, and grow only where they go through. Where UDP/53 is intercepted, DNS over TCP is used;
where TXT records are refused, AAAA records carry the answers.

It does not help when no resolver you can reach forwards queries for your zone.

## How it works

- **Session.** The client handshakes at the first connection, then carries every connection as
  a stream of one session. A session without connections ends after `session_idle`, and the next
  connection opens a new one.
- **Resolvers written in the config.** They go through the outbound's own
  [smart resolver pool](../dns/smart-dns-pool.md), on unless `smart_pool` is `false`: each is
  first sent a plain query (`pretest_domain`, `pretest_record_type`), and the ones that answer
  join the pool, up to 10 working, more when some go down. The client sees the pool as one
  resolver, on the loopback. Resolvers may then also be `tcp://`, DoT (`dot://host:853`) or DoH
  (`https://host/dns-query`). With `smart_pool: false`, each resolver is a path of the client's
  own, plain UDP (and TCP, see `tcp`) only.
- **`auto`, or no resolvers.** The client's own discovery runs, the code of the Soar library: it
  tries the resolvers it verified on earlier runs (saved in the cache file), then the device's own
  (where the system lets it read them), the curated list of the country that Soar bundles
  (Iran, China, Russia), and global public resolvers; with `sample_ranges`, also addresses of the
  country's ranges. It keeps `want` working and looks for more when some stop. Its settings are
  `smart_pool.discovery`, the block every DNS tunnel shares; DNSTT and MasterDNS take the same
  candidates for their `auto`. These resolvers are paths of the client's own, next to the pool
  when the config also writes resolvers. hiddify-core sets `discovery.country` from the app's
  region when it is empty.
- **Sockets.** The queries go out with the outbound's socket settings (`bind_interface`,
  `routing_mark`) and the platform's protection, so on a VPN they do not loop back into the
  tunnel; queries to the pool on the loopback use a plain socket. `detour` is not supported.

TCP only. UDP is not carried.

## Configuration

```json
{
  "type": "soar",
  "tag": "soar-out",
  "domain": "t.example.com",
  "public_key": "<soar-server pubkey key>",
  "resolvers": ["8.8.8.8", "1.1.1.1", "auto"],
  "smart_pool": {
    "enabled": true,
    "discovery": { "country": "ir" }
  }
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `domain` | string | required | The tunnel zone delegated to the server (`soar-server -zone`). |
| `public_key` | string | required | The server's Ed25519 public key, as `soar-server pubkey` prints it (base64; base64url and hex are read too). |
| `resolvers` | list of strings | `auto` | Resolvers: `"8.8.8.8"`, `"1.1.1.1:5353"`, or `"auto"` for Soar's discovery. With the smart pool also `tcp://`, `dot://host:853` and `https://host/dns-query`. |
| `smart_pool` | bool or object | on | The smart pool for the resolvers written, as described above; `false` turns it off. The object takes the [pool's settings](../dns/smart-dns-pool.md), among them `discovery`, which also steers Soar's own discovery: `country`, `sample_ranges`, `want` (default 16 here), `concurrency` (16), `pace` (`20ms`). With the pool off, write `{"enabled": false, "discovery": {...}}`. |
| `pretest_domain` | string | `"www.google.com"` | With the pool: the name queried to check a resolver. |
| `pretest_record_type` | string | `"a"` | With the pool: the record type of that query. |
| `tcp` | string | `"auto"` | DNS over TCP: `auto` (for a resolver whose UDP never answers), `on`, `only` or `off`. `off` with the pool alone. |
| `safe_qname` | int | `101` | Name length every resolver starts at. |
| `max_qname` | int | `253` | Longest name a resolver is probed up to. |
| `max_answer` | int | `1232` | Largest DNS answer probed up to, in bytes. |
| `hold` | duration | `500ms` | How long the server may hold an idle query. |
| `max_inflight` | int | `128` | Queries outstanding over all resolvers (at most 1024). |
| `max_path_window` | int | `32`; `max_inflight` with the pool alone | Queries outstanding over one resolver. |
| `max_streams` | int | `64` | Connections open at once (at most 256). |
| `stream_window` | int | `262144` | Each connection's receive window, in bytes. |
| `send_buffer` | int | `65536` | Each connection's send buffer, in bytes. |
| `session_idle` | duration | `90s` | A session without connections ends after this; keep it below the server's 2 minutes. |
| `connect_timeout` | duration | `90s` | How long a connection waits for the session. |

## Links

Soar defines no share link. hiddify-core's ray2sing reads `soar://` in two forms:

- The profile link of [WhiteDNS](https://github.com/WhiteDNS/WhiteDNS-Android), which exports
  and imports `soar://<base64url JSON>` with schema `whitedns.profile`: the server's `domain` and
  `public_key`, its `resolvers` and `soarSettings` (transport, discovery, country, name and answer
  sizes, windows, timeouts). Discovery on adds `auto` to the resolvers.
- A URL: `soar://t.example.com?pk=<public key>&resolvers=8.8.8.8,1.1.1.1&country=ir#name`, or the
  key before the host, `soar://<public key>@t.example.com?...`. The key is written in base64url,
  or percent-encoded in the query. Every field of the table is a parameter, `country`,
  `sample_ranges`, `discovery_want`, `discovery_concurrency` and `discovery_pace` go into
  `smart_pool.discovery`, `smart_pool=0` turns the pool off, `discovery=1` adds `auto` to written
  resolvers; no resolvers means `auto`. masterdns and dnstt links take the same discovery
  parameters.

## Notes

- Soar is pre-release: its protocol may still change, and client and server must be of versions
  that speak the same one.
- Anyone with the zone and the public key can use the server. Share them only with people you
  trust: a published zone is soon blocked.
- The pool is one path for the client, so its per-resolver tuning (name length, answer size,
  window) applies to the pool as a whole. Without resolvers in the config, or with
  `smart_pool: false`, the client tunes every resolver separately.

## See also

- [Smart resolver pool](../dns/smart-dns-pool.md)
- [MasterDNS](masterdns.md)
- [DNSTT](dnstt.md)
