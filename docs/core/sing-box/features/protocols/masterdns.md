# MasterDNS

[All Hiddify features](../../index.md)

MasterDNS carries your TCP connections inside DNS queries and answers, through public DNS
resolvers, to a [MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) server that you run.
It is an outbound: `"type": "masterdns"` in the `outbounds` list. The client is the MasterDnsVPN
Go client, embedded as a library.

## Why use it

- It works on networks where almost everything is blocked but DNS to public or local resolvers
  still passes, including the national-intranet mode where only domestic resolvers answer and
  they forward your queries abroad.
- Compared with [DNSTT](dnstt.md), its own protocol has a much smaller header, so each query
  carries more data; it sends every packet over several resolvers at once (duplication), moves a
  connection away from a resolver that drops its packets, measures the MTU each resolver passes
  and keeps testing failed resolvers in the background. The project reports several times the
  throughput of DNSTT.
- The server opens the connection to the destination itself, so no SOCKS or SSH outbound is
  needed behind it (`mode: socks5`).

It is still a DNS tunnel: slow next to a direct proxy, and limited by how many queries the
resolvers accept. Use it when nothing else gets through.

## How it gets past filtering

The filter sees DNS queries to a resolver for names under your tunnel domain, and the resolver
forwards them to your server, which is the authority for that domain. The data in the names and
in the answers is encrypted with a key only your device and your server know (`encryption`,
`key`): XOR (light, no extra bytes), ChaCha20 or AES-GCM. Resolvers that alter binary answers can
be given base64 answers (`base_encode`).

It does not help when the resolvers you can reach refuse long names, or when every outside
resolver is blocked and the domestic ones do not forward.

## How it works

- **Start.** The client sends MTU probes to every pair of tunnel domain and resolver in
  `resolvers`, `mtu_test_parallelism` at a time, with `mtu_test_retries` tries of
  `mtu_test_timeout` each. A resolver passes when the server's answers come back through it; the
  smallest upload and download sizes that passed become the MTU of the tunnel. With
  `auto_remove_low_mtu_resolvers`, a few resolvers that would pull the shared MTU down are
  dropped instead. Then the client opens one session with the server. The outbound is ready
  once the session is open; a connection made before that waits up to `ready_timeout`.
- **Resolvers.** Each query goes to a resolver chosen by `balancing`, and is sent
  `packet_duplication` times over different resolvers, so one lossy resolver does not lose it.
  A connection that keeps resending on its resolver moves to another. A resolver that only times
  out is set aside (`auto_disable_timeout_resolvers`) and tested again later
  (`recheck_inactive_resolvers`).
- **Smart pool.** With `smart_pool`, the client sees one resolver: the outbound's own
  [smart resolver pool](../dns/smart-dns-pool.md), the same code as [DNSTT](dnstt.md)'s. Each
  resolver in `resolvers` is first sent a plain query (`pretest_domain`, `pretest_record_type`),
  the ones that worked before first, and those that answer join the pool until 10 work; when
  some go down, the next ones are checked. The pool spreads
  the tunnel's queries over them, slows down for a resolver that rate-limits, and skips one that
  stops answering. Resolvers may then also be DoT (`dot://host:853`), DoH
  (`https://host/dns-query`) or `auto`, the built-in list of public resolvers. Each resolver's
  score is saved in the cache file. The MasterDnsVPN client's own balancing, duplication and
  per-resolver MTU then apply to the pool as a whole, so a pool of resolvers with different
  limits gets the MTU of the smallest; without `smart_pool` the client does all of this itself,
  over plain UDP resolvers only.
- **Inside the tunnel.** Every connection is a stream with its own reliable delivery (ARQ:
  acknowledgements, retransmission, a window of `arq_window` packets). Control messages are
  packed together, and data can be compressed (`upload_compression`, `download_compression`).
- **Destination.** In `socks5` mode (the server's default) the server connects to the address of
  each connection, so the outbound carries any TCP connection by itself. In `tcp` mode the
  server forwards every connection to the one target it is set up for, and the destination is
  ignored; put the matching outbound (for example `socks` or `ssh`) in front with `detour`.
  The MasterDnsVPN server refuses connections to private and loopback addresses.

TCP only. Routed UDP does not use this outbound; `udp_over_tcp` carries UDP over a stream for
servers that support it.

## Configuration

```json
{
  "type": "masterdns",
  "tag": "masterdns-out",
  "domains": ["v.example.com"],
  "resolvers": ["8.8.8.8", "1.1.1.1", "9.9.9.9:53"],
  "encryption": "xor",
  "key": "<the server's encrypt_key.txt>"
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `domains` | list of strings | required | The tunnel domains the server is the authority for, the server's `DOMAIN`. All must belong to the same server. |
| `resolvers` | list of strings | required | Plain DNS resolvers: `"8.8.8.8"`, `"1.1.1.1:5353"`, `"10.0.0.0/30"`, `"10.0.0.0/30:5353"` or `"[2001:db8::1]:53"`. A range adds every address in it. With `smart_pool` (no ranges): also `"dot://host:853"`, `"https://host/dns-query"` and `"auto"`. |
| `encryption` | string | `"xor"` | The server's `DATA_ENCRYPTION_METHOD`: `none`, `xor`, `chacha20`, `aes-128-gcm`, `aes-192-gcm` or `aes-256-gcm`, or its number 0 to 5. |
| `key` | string | required unless `none` | The server's key, the content of its `encrypt_key.txt`. |
| `mode` | string | `"socks5"` | The server's `PROTOCOL_TYPE`: `socks5` or `tcp`, as described above. |
| `smart_pool` | bool or object | `false` | Run the outbound's own resolver pool, as described above: `true`, or an object with `load_balance`, `deadline`, `per_attempt`, `probe_interval` and `down_after` (see [Smart resolver pool](../dns/smart-dns-pool.md)). Needed for DoT, DoH and `auto` resolvers. |
| `pretest_domain` | string | `"www.google.com"` | With `smart_pool`: the name queried to check that a resolver answers. |
| `pretest_record_type` | string | `"a"` | With `smart_pool`: the record type of that query: `a`, `aaaa`, `cname`, `mx`, `ns`, `ptr`, `soa`, `srv` or `txt`. |
| `balancing` | string | `"round-robin"` | How the resolver of each query is chosen: `random`, `round-robin`, `least-loss`, `lowest-latency`, `hybrid`, `loss-then-latency`, `least-loss-top-random` or `least-loss-top-round-robin`, or the number 1 to 8 of `RESOLVER_BALANCING_STRATEGY`. `least-loss` suits lossy links with many resolvers. |
| `packet_duplication` | int | `2` | How many times each packet is sent, over different resolvers (1 to 10). More is more reliable and uses more bandwidth. |
| `setup_packet_duplication` | int | `2` | The same for the packets that open a connection (up to 12). |
| `upload_compression` | string | `"off"` | `off`, `zstd`, `lz4` or `zlib`. |
| `download_compression` | string | `"off"` | `off`, `zstd`, `lz4` or `zlib`. |
| `base_encode` | bool | `false` | Ask for base64 answers, for resolvers that damage binary records. |
| `min_upload_mtu` | int | `38` | Smallest accepted upload MTU, in bytes. |
| `max_upload_mtu` | int | `150` | Largest tried upload MTU. |
| `min_download_mtu` | int | `100` | Smallest accepted download MTU. |
| `max_download_mtu` | int | `500` | Largest tried download MTU. Resolvers that pass large answers allow more. |
| `mtu_test_timeout` | duration | `2s` | How long one MTU probe may take. |
| `mtu_test_retries` | int | `2` | How many times a probe is sent. |
| `mtu_test_parallelism` | int | `16` | How many resolvers are tested at once. |
| `auto_remove_low_mtu_resolvers` | bool | `true` | Drop the few resolvers that would pull the shared MTU down. |
| `recheck_inactive_resolvers` | bool | `true` | Test failed resolvers again in the background. |
| `auto_disable_timeout_resolvers` | bool | `true` | Stop using a resolver that only times out. |
| `workers` | int | `4` | UDP read and write workers. |
| `process_workers` | int | from the machine | Packet processors. |
| `arq_window` | int | `600` | The reliable delivery window, in packets. |
| `ready_timeout` | duration | `30s` | How long a connection waits for the tunnel to be ready before it fails. |
| `connect_timeout` | duration | `30s` | How long a connection waits for the server to reach the destination. |
| `log_level` | string | `"info"` | Level of the MasterDnsVPN client's own messages: `debug`, `info`, `warn` or `error`. They appear in the sing-box log. |
| `udp_over_tcp` | object | | The UDP over TCP setting from sing-box, for a server that terminates it. |

The sockets that send the DNS queries use the outbound's socket settings, such as
`bind_interface` and `routing_mark`, and the platform's socket protection, so on a VPN the queries
do not loop back into the tunnel. `detour` is not supported: the queries go out directly, and the
log shows a warning.

Every other setting of the MasterDnsVPN client keeps the default of its sample configuration.
The client's own resolver finder (`client_resolvers.txt` with ranges) is replaced by `resolvers`.
hiddify-core's ray2sing reads two links into this outbound: `masterdns://`, which carries the same
fields, and the `dnst://` URL of the dnst URL spec (`dnst://v.example.com/masterdns/socks?mkey=…&encryption=5`),
where the `socks` backend is this outbound alone and any other backend sets `mode: tcp` with that
outbound in front. It also reads the `masterdns://` profile link of WhiteDNS (base64url JSON,
schema `whitedns.profile`). A link turns `smart_pool` on unless it says `smart_pool=0` or lists
an address range, and a link without resolvers (a `dnst://` link names none) uses `auto`
through the pool, or a list of well-known public resolvers without it.

## Notes

- With many resolvers the start takes longer, because every one is MTU-tested first. Keep a
  list of resolvers that passed, and put the best ones first.
- The key and the encryption method must match the server exactly, or the server drops every
  packet and the client never becomes ready.
- Share links with the tunnel domain only with people you trust: a published domain is blocked
  within hours.

## See also

- [DNSTT](dnstt.md)
- [Smart resolver pool](../dns/smart-dns-pool.md)
- [Monitoring](../groups/monitoring.md)
- [Fallback](../groups/fallback.md)
