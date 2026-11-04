# DNSCrypt (SDNS stamps)

[All Hiddify features](../../index.md)

The `sdns` DNS server sends queries to a DNSCrypt resolver, given by its DNS stamp (a string that
starts with `sdns://`). DNSCrypt encrypts and signs each query and answer. It is a DNS server:
`"type": "sdns"` in the `dns.servers` list.

## Why use it

- Your network changes or blocks plain DNS answers, and you want encrypted DNS that does not use
  TLS or HTTPS.
- A resolver you trust publishes a DNSCrypt stamp, for example from the public DNSCrypt resolver
  lists.

## How it gets past filtering

A filter cannot read DNSCrypt queries, and cannot change the answers without the change being
detected. So DNS poisoning, a common way to block sites, does not work against it.

It does not hide that you use DNSCrypt. The resolver's address is in the stamp and the traffic
has a known shape, so a filter can block the resolver or the protocol. When that happens, send
the queries through a proxy with `detour`.

## How it works

- The stamp holds the resolver's address, its provider name and its public key.
- Before the first query, the server asks the resolver for its current certificate and checks it
  with the public key from the stamp. Then it sends the encrypted query and decrypts the answer.
- The server keeps the certificate for later queries, so they take one round trip. It fetches a
  new one when the certificate expires, when a query fails, or when the network changes.
- Queries go over UDP. Each step gives up after 10 seconds.
- Only DNSCrypt stamps work. A stamp for DNS over HTTPS, DNS over TLS or plain DNS is refused when
  the config loads. Use the `https`, `tls` or `udp` server type for it.

## Configuration

```json
{
  "dns": {
    "servers": [
      {
        "type": "sdns",
        "tag": "dnscrypt",
        "stamp": "sdns://AQcAAAAAAAAA..."
      }
    ],
    "final": "dnscrypt"
  }
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `stamp` | string | required | The DNSCrypt stamp of the resolver, starting with `sdns://`. |

The dial fields of other remote DNS servers work here too, for example `detour` to send the
queries through an outbound. The server address comes from the stamp: `server` and `server_port`
are not used.

## See also

- [DNS group](dns-group.md)
- [Smart resolver pool](smart-dns-pool.md)
