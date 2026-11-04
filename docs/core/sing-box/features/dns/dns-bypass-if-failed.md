# DNS rules: bypass_if_failed

[All Hiddify features](../../index.md)

`bypass_if_failed` is a field of the DNS `route` action. When the server chosen by the rule
fails, the query goes on to the next matching DNS rule instead of failing. Without it, the error
of that server is the result.

## Why use it

- You send some names to a special server (a local resolver, a server only reachable through one
  outbound, a [DNSCrypt](sdns.md) resolver), and want the normal rules to answer when that
  server is down or blocked.
- You want a chain of servers for the same names, tried in rule order.

For trying several servers at once, use a [DNS group](dns-group.md) instead.

## How it gets past filtering

It does not. It only lets the next rule try another server when one is blocked.

## How it works

- The rule's server is asked as usual. If it answers, that answer is used.
- If it fails, rule matching goes on from the next rule. The next rule that matches picks the
  server, and if no other rule matches, the final server is used.
- For an address lookup made by sing-box itself (for example to resolve a server name of an
  outbound), an empty answer also counts as a failure.
- If the query is canceled, it stops; the next rule is not tried.
- Several rules in a row can each have `bypass_if_failed`.
- A failure that the next rule takes over is logged at debug level, not as an error.

### Limit: legacy DNS rule mode only

sing-box 1.15 has two ways to run DNS rules. `bypass_if_failed` works only in the legacy mode;
in the new mode it is ignored and a failed server is the result.

sing-box uses the legacy mode when at least one DNS rule matches on the answer's address
(`ip_cidr`, `ip_is_private` or `ip_accept_any`, without `match_response`) or sets `strategy` in
its action, and no rule needs the new mode (for example `match_response`, `query_type`,
`ip_version`, or the `evaluate` or `respond` actions). Upstream marks these legacy fields as
deprecated, so sing-box logs a warning for them.

A config that mixes the two (a `strategy` in one rule and a `query_type` in another, for example)
is rejected at startup. In the legacy mode, a fake IP rule therefore cannot match
`query_type: [A, AAAA]`. Give it `bypass_if_failed` instead: the fake IP server fails every other
query type, and the next rule answers it.

## Configuration

```json
{
  "dns": {
    "servers": [
      { "type": "udp", "tag": "office", "server": "10.0.0.53" },
      { "type": "https", "tag": "remote", "server": "1.1.1.1" }
    ],
    "rules": [
      {
        "domain_suffix": ["corp.example"],
        "action": "route",
        "server": "office",
        "strategy": "ipv4_only",
        "bypass_if_failed": true
      }
    ],
    "final": "remote"
  }
}
```

Here `strategy` puts the rules in legacy mode. When the office server does not answer, names
under `corp.example` are resolved by `remote`.

| Field | Type | Default | Meaning |
|---|---|---|---|
| `bypass_if_failed` | bool | `false` | When the rule's server fails, go on to the next matching rule. |

## See also

- [DNS group](dns-group.md)
- [DNSCrypt (SDNS stamps)](sdns.md)
