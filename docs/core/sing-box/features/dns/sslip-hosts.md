# sslip.io names in the hosts server

[All Hiddify features](../../index.md)

A name under `sslip.io` carries its own IP address, such as `1-2-3-4.sslip.io` for `1.2.3.4`.
Hiddify's `hosts` DNS server (`"type": "hosts"` in the `dns.servers` list) reads the address from
such a name and answers with it, without asking any DNS server. There is no new field: every
`hosts` server does this.

## Why use it

- A server has no domain, but the client needs one, for example for a TLS server name or a
  certificate issued for an `sslip.io` name.
- On a filtered network, a DNS query for the name can fail or get a false answer. Reading the
  address from the name needs no query at all.

## How it gets past filtering

No DNS query leaves the device for these names, so DNS blocking or poisoning cannot affect them.
The connection itself still goes to the IP address in the name, which a filter can block.

## How it works

- The `hosts` server first looks in `predefined`, then in its hosts files. Only when neither has
  the name does it read the address from the name.
- An IPv4 address is written with dots or dashes: `1.2.3.4.sslip.io` and `1-2-3-4.sslip.io` both
  mean `1.2.3.4`. A prefix before the address is allowed: `www.1.2.3.4.sslip.io` and
  `app-1-2-3-4.sslip.io` also mean `1.2.3.4`.
- An IPv6 address is written with dashes for colons: `2a01-4f8-c17-b8f--2.sslip.io` means
  `2a01:4f8:c17:b8f::2`, and `--1.sslip.io` means `::1`.
- The answer has a TTL of 10 minutes. An A query gets only an IPv4 address and an AAAA query only
  an IPv6 address; the other gets an empty answer.
- A name that does not hold a valid address, such as `foo.sslip.io`, gets "no such name", like any
  other name the `hosts` server does not know.

## Configuration

The `hosts` server answers only the names it knows, so send only `sslip.io` names to it with a
DNS rule:

```json
{
  "dns": {
    "servers": [
      { "type": "hosts", "tag": "hosts" },
      { "type": "https", "tag": "remote", "server": "1.1.1.1" }
    ],
    "rules": [
      { "domain_suffix": ["sslip.io"], "server": "hosts" }
    ],
    "final": "remote"
  }
}
```

The `hosts` server fields (`path`, `predefined`) work as in upstream sing-box.

## See also

- [DNS group](dns-group.md)
