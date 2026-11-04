# IPv6 by outbound

[All Hiddify features](../../index.md)

Gives the apps IPv6 only through an outbound that carries it, and never lets them see an IPv6
connection die. The monitoring learns, for every outbound, whether its exit carries IPv6: from
the URL test (`verify_ipv6`), from the link (`ipv6_declared`), and from the connections the
router carries. A DNS rule with `ipv6_by_outbound` leaves AAAA questions unanswered while the
outbound the traffic goes through is known to have no IPv6; a route rule with
`ipv6_unavailable_via` refuses such an outbound's IPv6 connections before their handshake, so
the app falls back to IPv4 at once; and the route option `ipv6_fallback` carries over IPv4,
inside the connection, an IPv6 connection that an outbound not yet known turns out not to carry.

## Why use it

- Google, YouTube and most large sites are IPv6-first: a browser that gets an AAAA answer
  connects over IPv6. Through a proxy without IPv6 the proxy accepts the connection and then
  closes it, which Chrome shows as "unexpectedly closed the connection" (`ERR_CONNECTION_CLOSED`)
  and never retries over IPv4, while apps that use IPv4 work (hiddify-app #2307, #2420). A reset
  at that point is no better: an app falls back only when the connect itself fails, and through
  a TUN the connect succeeds locally before the proxy has tried anything.
- With this, a proxy that carries IPv6 gives IPv6, a proxy that does not is never asked for it,
  and the first connections that teach the difference reach their destination anyway, over IPv4.
- The TUN keeps its IPv6 route, so nothing leaves the device outside the VPN, and a server
  with only an IPv6 address still routes: no family is ever refused outright.

## How it gets past filtering

It does not; it keeps a working proxy from looking broken.

## How it works

- **Verification at the URL test** (`experimental.monitoring.verify_ipv6`): after an outbound
  answers its URL test, the monitoring fetches the same test URL once more through it, from the
  IPv6 address of the URL's host (resolved by the box's DNS). An answer says the exit carries
  IPv6; no connection or no answer says it does not. Once per outbound per run; the answer is
  cached with the URL test results (`URLTestHistory.IPv6`) and is known again at the next start,
  before any test, until verified again. No new destination is contacted: it is the user's own
  test URL. A test URL whose host has no IPv6 address verifies nothing.
- **Declaration by the link** (`experimental.monitoring.ipv6_declared`, by outbound tag): a
  share link with `ipv6=1` says its exit carries IPv6, `ipv6=0` that it does not; ray2sing turns
  the parameter into this option. A declaration is known from the start.
- **Learning from the connections** (`route.ipv6_fallback`): a TCP connection to an IPv6 address
  through an outbound not known yet is watched. The router dials the IPv6 address as asked,
  sends on the app's first bytes (the request header goes at once, so the exit tries the
  destination even for an app that waits for the server to speak first), and waits up to 10 s for
  the destination's first byte. Nothing back, or a refused dial, and the same outbound is dialed
  again with the domain the app named (sniffed from its client hello or request; the proxy
  resolves it as it can), the bytes the app sent are said again (up to 64 KiB), and the
  connection goes on; the app never sees the failure. The destination answering over IPv4 after
  nothing over IPv6 is one failure against the outbound; two in a row with no success between
  them say the outbound has no IPv6. A destination that answers over neither family says nothing
  about the outbound. An outbound known not to carry IPv6 is not asked again: its IPv6 connections
  go straight over the domain. One known to carry IPv6 is watched like the rest, which costs no
  traffic, so an exit that loses IPv6 is noticed and its connections carried over anyway.
  Without a domain there is nothing to carry the connection over with, and it ends as it would
  have.
- An outbound found without IPv6 stays so for 10 minutes, then is let an IPv6 connection again
  (carried over IPv4 if it still cannot), since nothing else can tell when its exit gains IPv6.
- A group answers for the member it leads to; a group with no single selection (a balancer that
  hashes or rotates) carries IPv6 only when every live member is known to, and lacks it as soon
  as one is known to.
- `ipv6_by_outbound` on a DNS rule: while the named outbound is known to have no IPv6, the query
  runs with the `ipv4_only` strategy (AAAA gets an empty answer); otherwise the rule's own
  strategy applies.
- `ipv6_unavailable_via` on a route rule: matches a connection to an IPv6 address while the
  named outbound is known to have no IPv6. With `"action": "reject"` the TUN refuses it before
  the handshake, the client gets a reset and tries IPv4. Put the rule before any `sniff` rule:
  the TUN judges a TCP connection before its handshake only up to the first rule that needs the
  stream.

## Configuration

```json
{
  "dns": {
    "rules": [
      { "action": "route", "server": "remote", "strategy": "prefer_ipv4", "ipv6_by_outbound": "select" }
    ]
  },
  "route": {
    "ipv6_fallback": true,
    "rules": [
      { "ip_version": 6, "ipv6_unavailable_via": "select", "action": "reject" },
      { "action": "sniff" }
    ]
  },
  "experimental": {
    "monitoring": {
      "verify_ipv6": true,
      "ipv6_declared": { "my-proxy § 0": true }
    }
  }
}
```

| Field | Where | Type | Default | Meaning |
|---|---|---|---|---|
| `ipv6_by_outbound` | DNS rule action `route`, `route_options` | string | | An outbound, or a group; while it is known to have no IPv6, AAAA questions get an empty answer. |
| `ipv6_unavailable_via` | route rule | string | | An outbound, or a group; the rule matches an IPv6 destination while it is known to have no IPv6. |
| `ipv6_fallback` | `route` | bool | `false` | A TCP connection to an IPv6 address through an outbound not known yet is carried over IPv4 (the sniffed domain) when the outbound gives nothing, and teaches the outbound's IPv6. |
| `verify_ipv6` | `experimental.monitoring` | bool | `false` | After each outbound's URL test, the same URL is fetched over the host's IPv6 address through it, once per run; the answer is cached with the URL test results. |
| `ipv6_declared` | `experimental.monitoring` | object, tag to bool | | Outbounds whose IPv6 the link declared (`ipv6=1`, `ipv6=0`); known from the start. |
| `ipv6_probe` | `experimental.monitoring` | | | Retired, no effect: the probe of a public address it replaced. |

## Notes

- hiddify-core turns all of this on when the IPv6 mode gives the apps IPv6 at all ("on, IPv4
  first" or "on, IPv6 first"); the default, IPv4 only, answers the apps with `ipv4_only` and
  refuses every IPv6 destination before the sniff rule, with nothing to verify or carry over.
- The verification is one more request per outbound per run to the test URL the user already
  chose; through a proxy, that is one more connection its server sees.
- The carry-over is one failed round trip through the proxy per IPv6 connection while an
  outbound is not known yet: at most a couple of connections after a start without a cached
  answer, since two failures settle it and the verification at the first URL test usually
  settles it first.

## See also

- [Monitoring](../groups/monitoring.md)
- [DNS group](dns-group.md)
