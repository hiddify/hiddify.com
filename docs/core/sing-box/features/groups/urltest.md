# URL test: Hiddify additions

[All Hiddify features](../../index.md)

The URL test group (`"type": "urltest"`) tests its members and sends traffic through the fastest.
Hiddify adds more test URLs, a `failover` mode, and a reaction to failed connections, after
sing-box-lx.

## Why use it

- One test URL can be blocked on some networks. With several, a working member is not marked
  dead because of it.
- Upstream reacts only to tests: when the selected member dies, connections fail until the next
  test, up to `interval` later. Hiddify moves to another member on the first failed connection.
- `failover` keeps one member for as long as it works, so your exit address does not change
  every few minutes, and it tests one member per interval instead of all of them.

## How it gets past filtering

It does not. It chooses among outbounds that do, and notices sooner when one is blocked.

## How it works

**Test URLs.** Each member is tested with `url` and every entry of `urls` at once. The first
URL that answers gives the delay. A member is down only when none answers.

**Failed connections.** When a connection through a member fails because the path is dead (a
timeout, or an unreachable network or host):

- The member gets a penalty.
- The group tries the connection once more, through the best other member. When that works,
  the group selects it. Live connections are not closed.
- If the second try fails too, the first error goes back to the app, but the selection has
  already moved, so the app's own retry goes another way.

A refused or reset connection gives no penalty and no second try: the destination refused it,
and another member would meet the same answer. A connection the app canceled gives none either.

A penalty is cleared only by proof that the member works: a connection or a test through it
that succeeds. It does not expire with time.

When the fastest member has 3 penalties, members are ranked by penalties first, then by delay.
When every member that has a test result has 3 penalties, all members are tested at once, at
most once every 2 minutes, counted from the end of the last such test.

**`failover` mode.**

- The first choice is the fastest member.
- Each `interval`, only the selected member is tested (the TCP one, and the UDP one when it
  differs). While it answers, it stays selected, even when another member is faster.
- Unless it slowed down: when it is more than 2 times slower than the fastest other member (by
  their last results), it is tested once more. If it is still that slow, all members are tested,
  and the group moves when one is more than 1.5 times faster.
- When it fails, all members are tested and the fastest is selected.
- A manual test tests all members and selects the fastest.
- `tolerance` does not apply.

## Configuration

```json
{
  "type": "urltest",
  "tag": "auto",
  "outbounds": ["proxy-a", "proxy-b", "proxy-c"],
  "url": "https://www.gstatic.com/generate_204",
  "urls": ["https://cp.cloudflare.com/", "http://connectivitycheck.platform.hicloud.com/generate_204"],
  "mode": "failover",
  "interval": "3m"
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `urls` | list of strings | | More URLs to test. A member is up when any of `url` and `urls` answers. |
| `mode` | string | `""` | `failover` keeps the selected member until it fails. Empty selects the fastest at every test. |

The other fields are upstream's: `outbounds`, `url`, `interval`, `tolerance`, `idle_timeout`,
`interrupt_exist_connections`. Penalties apply in both modes and need no option.

lx's `round_robin` mode is not included: the [balancer](balancer.md) group covers it.

## See also

- [Balancer](balancer.md)
- [Fallback](fallback.md)
- [Monitoring](monitoring.md)
- [Unified delay](unified-delay.md)
