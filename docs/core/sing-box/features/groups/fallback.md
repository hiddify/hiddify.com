# Fallback

[All Hiddify features](../../index.md)

The fallback group tries its members in order and uses the first one that connects. A member
that fails is set aside for a while, so a dead server does not slow down every connection. It is
an outbound: `"type": "fallback"` in the `outbounds` list.

## Why use it

- You have a main server and one or more backups, and want the backup used only when the main
  one fails.
- You want the switch to happen on the connection that fails, not after the next URL test.

It only sees failures to open a connection. Some outbounds report a connection as open before
the server has answered, and fail later. Those failures are not caught: use a
[balancer](balancer.md) or a URL test group for them, which test the server itself.

## How it gets past filtering

It does not. It only chooses among outbounds that do.

## How it works

- For each connection, the group tries the members in config order and uses the first that
  opens the connection. It works the same way for TCP and UDP.
- A member that fails is skipped for `blacklist_timeout`. It moves to the end of the order, and
  is tried only after all the others fail. So a dead member costs one failed attempt per
  timeout, not one per connection.
- When a member opens a connection, it is taken off the skip list.
- If the connection is canceled while a member is trying, the group stops and does not try the
  next one.
- If every member fails, the connection fails with the error of each member.
- The group reports the member that last opened a connection as its current choice.

## Configuration

```json
{
  "type": "fallback",
  "tag": "fallback",
  "outbounds": ["main", "backup"],
  "blacklist_timeout": "1m"
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `outbounds` | list of strings | required | Tags of the members, in the order to try them. |
| `blacklist_timeout` | duration | `1m` | How long a member that failed is skipped. |

Ported from sing-box-extended.

## See also

- [Balancer](balancer.md)
- [Monitoring](monitoring.md)
