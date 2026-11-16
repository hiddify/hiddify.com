# Lazy outbounds and keep top

[All Hiddify features](../index.md){ .hi-back }

A **lazy outbound** (`"lazy": true`) is in the config, in its groups and in the app's list from
the start, but the core keeps only its options: the real outbound is created when a connection
or a test first goes through it, and closed again when nothing uses it. **Keep top**
(`experimental.monitoring.keep_top`) uses only the fastest few of the lazy outbounds and leaves
the others at rest, so a profile of hundreds of proxies costs the memory of the few in use.

## Why use it

- A subscription has hundreds of proxies. Running them all takes more memory than the iOS
  network extension is allowed, and the system stops it.
- You want the fastest three, not all of them tested every few minutes: less battery, less data.
- You want that without the config changing under the app. The proxies stay in the config, so
  the list, the selection and the groups stay as they are, and no reload cuts connections.

## How it gets past filtering

It does not. It only decides which outbounds exist and which are used.

## How it works

### Lazy outbounds

- The outbound is under its tag from the start. Its type is the type of the real outbound, and
  its detours are known, so groups and the monitoring treat it like any other.
- The first connection or test creates and starts the real outbound. Everything that uses it is
  counted: each connection until it closes, and a URL test over all its connections.
- When the last connection closes, the real outbound stays for 30 seconds, for the next
  connection of the same browsing, then it is closed. After a test it is closed at once, so
  testing a whole profile keeps as many created as are tested at a time (the monitoring's
  `workers`, 10).
- It is never closed under a connection.
- If the real outbound cannot be created (its options are wrong), the connection fails with
  that error, the outbound shows as failed with the reason, and it is tried again after 30
  seconds.
- A hot reload leaves an unchanged lazy outbound alone, and replaces a changed one.
- Groups, `direct`, `block` and endpoints (WireGuard, WARP, ...) are never lazy; the option is
  ignored on a group, `direct` and `block`, and endpoints do not have it.

### Keep top

- It manages the lazy outbounds, and only them. The ones it does not use **rest**: the cycles do
  not test them and no balancer sees their results, so nothing dials through them and they are
  never created. The app still sees them, with their last ping.
- It finds the fastest a few at a time, a stage: the best `count` found so far plus the next
  `batch` still to test. As each ping comes in, the one that does not answer, or is too slow for
  the top, goes back to rest, and the next one takes its place in the batch, so a proxy that
  takes its whole timeout does not hold the others.
- The order is the order of the monitoring's cycles: by last ping, fastest first, the ones never
  tested in every other place, the ones that failed last. Of the failed, the ones that answered
  at some time come first. The pings of the last run are in the cache file, so the next run
  starts with the fastest of this one.
- With `quick`, the pick ends once the outbounds still to test were slower at their last test
  (in the last 24 hours) than the ones found. Otherwise it ends when all were tested.
- The outbound selected in a selector, and the ones listed in `pinned`, are always used,
  whatever their ping, beside the `count` fastest. Selecting or pinning one that
  rests takes it out of rest and tests it.
- An outbound that goes to rest keeps its connections until they end.
- When every kept outbound has timed out, a new pick goes through them again; the ones that
  answer stay in use while it looks. When none answers at all, it goes through them again after
  30 seconds, then 1, 2, 4 and at most 5 minutes, and goes on at once when one of those in use
  answers (after a network change the monitoring tests them again).
- A kept outbound stops answering when two tests in a row failed: after the first failed test
  it is tested once more 5 seconds later, so one lost test does not cost it its place.
- With a `count`, a kept outbound that stops answering is replaced: a pick that only fills its
  place keeps the ones that answer, tests the ones at rest in the order of their last pings, and
  ends as soon as `count` answer. With `answering`, the one that stopped goes to rest.
- While fewer are kept than may be (`count`, or all of them with `answering`) and others rest,
  the ones at rest are tested again 10 minutes after the last time, then 30 minutes, then 1, 2, 4
  and every 6 hours while none of them answers; once one does, the wait is 10 minutes again. The ones
  in use are not tested for it.
- An outbound at rest that answers a test asked for by its tag (the user tests the list) is used
  at once, while there is a place for it.
- An outbound with no result 30 seconds into its stage counts as not answering (10 seconds more
  for every 10 outbounds of a batch above 10).
- A hot reload keeps the pick while the kept outbounds are unchanged; a replaced or removed one
  starts a new pick, which keeps the ones that answer. The `keep_top` options themselves can be
  changed, added or removed by a hot reload.
- A test of a group tests the members in use. A test of one outbound by its tag runs also when
  it rests.
- When there are no more lazy outbounds than `count`, and neither `answering` nor `countries`
  is set, nothing rests.

Log lines start with `KEEP TOP`.

## Configuration

```json
{
  "outbounds": [
    {"type": "vless", "tag": "p1", "lazy": true, "server": "..."},
    {"type": "trojan", "tag": "p2", "lazy": true, "server": "..."},
    {"type": "balancer", "tag": "lowest", "strategy": "lowest-delay", "outbounds": ["p1", "p2"]},
    {"type": "selector", "tag": "select", "outbounds": ["lowest", "p1", "p2"]}
  ],
  "experimental": {
    "monitoring": {
      "keep_top": {
        "count": 3,
        "batch": 10,
        "quick": true
      }
    }
  }
}
```

Outbound field:

| Field | Type | Default | Meaning |
|---|---|---|---|
| `lazy` | bool | `false` | Create the outbound when it is first used and close it when it is idle. |

`experimental.monitoring.keep_top`:

| Field | Type | Default | Meaning |
|---|---|---|---|
| `count` | int | `0` | How many lazy outbounds to keep in use: the fastest. `0`, with `answering` or `countries`, is all that fit those. |
| `answering` | bool | `false` | Keep every lazy outbound that answers, and put one that stops answering to rest. `count` is not used. |
| `countries` | list of strings | | Keep only outbounds whose exit is in one of these countries (two-letter codes), by the IP lookup of the test, or by the flag in the tag before it. |
| `batch` | int | `10` | How many outbounds are tested at a time, beside the best so far. Below `0`: all at once. |
| `quick` | bool | `false` | End the pick once the outbounds still to test were slower at their last test than the ones found. |
| `pinned` | list of strings | | Tags of lazy outbounds that are always in use beside the `count` fastest, whatever their ping, like the one selected in a selector. |

## Notes

- Use a balancer for the automatic choice. The `urltest` group tests its members by itself and
  does not know which of them rest.
- Do not mark as lazy an outbound that needs a long time before it works (Psiphon, Tor, the DNS
  tunnels): it would start again at every use.
- Without `keep_top`, lazy outbounds are tested by the cycles like the others: each is created
  for its test and closed after it.

## Related articles

- [Monitoring](monitoring.md)
- [Balancer](balancer.md)
