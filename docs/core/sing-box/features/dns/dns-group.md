# DNS group

[All Hiddify features](../../index.md)

A DNS group asks several DNS servers for one query and returns the best answer. It can drop
answers that point into blocked ranges, so a poisoned reply from a filtered resolver does not
win. It is a DNS server: `"type": "group"` in the `dns.servers` list. Upstream sing-box has the
group type; Hiddify adds `mode`, `ignore_ranges`, `error_ttl`, `win_ttl` and `member_timeout`, and keeps the
older `multi` type as an alias.

## Why use it

- Your resolvers are unreliable or slow, and you want an answer from whichever one works.
- Your network's resolvers return fake addresses (for example a censor's block page) for some
  names, and you want those answers thrown away.
- You want one server used most of the time, with the others taking over only when it fails.

## How it gets past filtering

DNS filtering usually answers a blocked name with a fixed address, such as a block page in a
private range. `ignore_ranges` drops A and AAAA records in those ranges. A response with no
address left is not an answer, so the group waits for another server, for example an encrypted
one through the proxy. It does not help when the filter drops the query or answers with an
address you don't list.

## How it works

The group has four modes:

| Mode | What it does |
|---|---|
| `parallel` (default) | Asks every server at once and returns the first good answer. |
| `sequential` | Asks the servers one at a time, in order, until one gives a good answer. A server that failed is asked after the others for `error_ttl`, and each server gets a bounded share of the query's time. |
| `stable` | Asks only its current server. When that server fails, asks the others at once; the first to answer becomes the current server. |
| `fastest` | Like `stable`, but keeps the current server only for `win_ttl`. Then it asks every server at once again and the fastest becomes the current server. |

In every mode:

- A good answer still has records after `ignore_ranges`. An A or AAAA query needs an address:
  a CNAME left alone after filtering is not enough.
- SERVFAIL and REFUSED count as failures.
- A response without an answer, such as NXDOMAIN, is kept and returned only if no server gives a
  good answer.

In `sequential` mode:

- A server that fails, or whose answer `ignore_ranges` empties, is asked after the others for
  `error_ttl`; it is still asked when they all fail. So a dead first server does not open every
  query. When the network changes, the group forgets its failures.
- Each server is waited for at most `member_timeout`, or, when that is unset, the query's time
  left shared among the servers still to ask, at least 2 s each. A server that hangs, as a
  TCP or TLS server behind a port that drops packets does, no longer spends the whole query
  on its own and leaves the servers behind it unasked.

In `stable` and `fastest` mode:

- The current server gets half of the time left for the query, so the others still have time
  to answer when it does not.
- A server that fails, or whose answer `ignore_ranges` empties, is skipped for `error_ttl`. When
  every server failed recently, they are all asked.
- When the network changes, the group forgets its failures and its current server.

## Configuration

```json
{
  "dns": {
    "servers": [
      { "type": "udp", "tag": "local", "server": "192.168.1.1" },
      { "type": "https", "tag": "remote", "server": "1.1.1.1", "detour": "proxy" },
      {
        "type": "group",
        "tag": "dns-group",
        "servers": ["local", "remote"],
        "mode": "stable",
        "ignore_ranges": ["10.10.34.0/24"],
        "error_ttl": "1m",
        "win_ttl": "10m"
      }
    ]
  }
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `servers` | list of strings | required | Tags of the DNS servers in the group, in order. A group cannot hold another group or a `fakeip` server. |
| `mode` | string | `parallel` | `parallel`, `sequential`, `stable` or `fastest`. |
| `ignore_ranges` | list of IP prefixes | | A and AAAA records in these ranges are dropped from answers. |
| `error_ttl` | duration | `1m` | `sequential`: how long a failed server is asked last; `stable` and `fastest`: how long it is skipped. |
| `member_timeout` | duration | | `sequential`: the longest one server is waited for. Unset shares the query's time left among the servers still to ask, at least 2 s each. |
| `win_ttl` | duration | `10m` | `fastest`: how long the fastest server stays current. |

The deprecated `"type": "multi"` still loads: `"parallel": true` means `"mode": "parallel"`,
and otherwise `"mode": "sequential"`.

The `stable` and `fastest` modes follow sing-box-lx.

## See also

- [Smart resolver pool](smart-dns-pool.md)
- [Fallback](../groups/fallback.md)
