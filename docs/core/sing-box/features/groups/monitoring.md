# Monitoring

[All Hiddify features](../../index.md)

Monitoring tests every outbound and endpoint in the background: it measures the delay through
each one and finds the IP address and country it exits from. Groups such as the
[balancer](balancer.md) choose members from these results, and the app shows them. It is
always on. Its settings are the `monitoring` field of the `experimental` block.

## Why use it

- Groups that use it share one test schedule for the whole config.
- You see the exit IP address, country and provider of each server, not only its delay.
- Tests run only while you use the connection, so an idle device does not keep testing.
- Results are saved, so groups can make a choice right after start, before new tests finish.

## How it gets past filtering

It does not. It finds out which outbounds work, so groups can avoid the blocked ones.

## How it works

### What is tested

- Every outbound and endpoint is tested, except groups. A test opens the URL test address
  through the outbound and measures the delay, as the URL test group does. A test that fails or
  takes longer than `url_test_timeout` marks the outbound as failed.
- A group's result is the result of its selected member. When it has none, it is the best
  result among its members.
- After a successful test, monitoring asks an IP information service, through the same outbound,
  for the exit IP address, country, region, city and network. It does this when the outbound
  has no IP information yet, or only information loaded from the cache. If that request is
  faster than the URL test, its time becomes the delay.
- An outbound that dials through a detour is tested, for its delay and its IP, only once the
  outbound the detour leads to (for a group, its selected member) has a result of this run and
  is not being tested again. Before that, its test would fail or measure a path that is about to
  change.

### When tests run

- Tests start with sing-box. First, the outbound each group's selection leads to (a selector's
  pick, a balancer's current member, through nested groups) is tested ahead of everything else:
  the ping the user looks at shows at once. Then tests run in cycles every `interval`. Each
  cycle tests the outbounds whose result is older than `interval` or marked for testing, fastest
  first (by the last result, cached or not), then the untested ones, `workers` at a time. So the
  first cycle tests last run's fastest member first, and a group on that member confirms it
  before the others arrive.
- When no connection has gone through sing-box for `idle_timeout`, testing stops. The next
  connection starts it again.
- An outbound that is not ready yet, for example Psiphon still connecting, or whose detour has no
  result yet, is skipped and tried again 3 seconds later. After 10 tries it is tested anyway.
- When an outbound works after failing, the outbounds already tested through it are tested
  again.
- Some events test at once: a connection that fails through a balancer member, a selector that
  switches to another outbound (the new selection is tested, and so are the outbounds that
  depend on the selector), or an outbound that finished connecting, such as Psiphon or DNSTT.
  Such a test runs right away, beside the cycle's tests, not behind them: it does not wait for
  one of the `workers`, which a cycle of timeouts can hold for seconds. Its result reaches the
  groups' subscribers at once, past `debounce_window`.
- A test asked for runs in stages, `on_demand_timeouts` (1 s, 3 s and 10 s unless set). The
  first attempt starts at once. When it fails, or has not answered by the first mark, the
  outbound shows as unavailable for now. A failed attempt is tried again at the next mark, and
  so at every mark but the last, which is the deadline of them all; an attempt still running at
  a mark is left to answer, so a proxy is pinged once unless its ping failed. The answer shows
  at once, however late: an answer at 1.5 s replaces the miss shown at 1 s. When the last
  attempt has failed and no mark is left to try at, it is over without waiting for the deadline.
  A test asked for while a test of the same outbound runs (the cycle's, or an earlier tap) joins
  it and takes its result: one ping at a time per outbound. Two at once pinged the proxy twice,
  and the one that ended last wrote the result, so a late failure replaced a fresh answer. A
  group's new selection is not tested again when it was measured in the last 15 s: under load,
  that second ping read 2549 ms for a 59 ms member and the group moved on.
- The log says why every test runs and what every lowest-delay group decides: lines prefixed
  `MONITORING` (test, result, cycle, the stages of a staged test) and `LOWEST` (the member kept
  or taken, with the fastest one and the reason), at the info level.
  The first mark is for an outbound nothing is known of yet: no result of this run, or only the
  one cached from the previous run. An outbound that worked in this run keeps its result past
  it, instead of showing as unavailable after one slow answer, and its stages start at the
  second mark (3 s, then the 10 s deadline).
  Groups never see the miss, only the last confirmed result, so a balancer does not take a slow
  member for dead, move away from it and cut its connections, on a miss its next attempt answers.
- A test's delay is published as soon as the URL test answers. The IP lookup that follows it,
  which can take as long again, brings the IP information when it is done.
- When the network changes, every outbound is tested again 2 seconds after the last change.
  A test broken by the network reset runs again.
- A test that has not returned after three times `url_test_timeout` plus 2 seconds (an outbound
  whose dial ignores its deadline, as one into a native library may) counts as failed, and its
  worker goes on. Otherwise a few such outbounds would hold every worker, and the cycle, for
  good, and nothing would be tested again.

### URLs

The tests use the first address in `urls`. If a whole cycle has no successful test, the cycle
runs again with the next address, until one works or the list ends. The address that worked is
used from then on.

### Saved results

Results are saved in the cache file and loaded at the next start. A loaded result is marked as
"from cache" until the outbound is tested again. The balancer adds 20,000 ms to such results,
so a fresh test wins.

The IP information is loaded too, so the app can show the last run's exit IP and country before
any test. It stays marked as from the cache (`IpInfoFromCache`) until an IP lookup of this run
succeeds; a failed test does not change it. The exit IP of WARP, Psiphon or a rotating proxy can
change between runs, so the app should show such an IP as not confirmed yet.

A failed test keeps its error in the result (`Error`), so the app can say why the proxy failed:
a refused handshake, a timeout, a DNS failure. A test that answers clears it. An outbound that is
not ready is not tested, so it has no test error; WARP and MASQUE say why they are not ready
through `adapter.StatusError` instead (a refused registration, a tunnel that does not connect).

Groups that subscribe to monitoring get one update for a burst of results, after
`debounce_window`.

### IP information services

If `ipinfo_url` is set, it is tried first. It must return JSON like ipapi.co's, with fields such
as `ip`, `country_code`, `region`, `city`, `asn` and `org`. If it fails, these services are
tried in turn, starting from a random one:

- ipapi.co
- ip-api.com
- ipinfo.io
- api.ip.sb
- ipwho.is
- api.country.is
- api.my-ip.io

When every one of them fails, as they do on a busy network where they rate-limit or time out,
Cloudflare's own `cloudflare.com/cdn-cgi/trace` is asked, along with api.country.is and
api.my-ip.io: it answers the address and the country only, with no rate limit.

## Configuration

```json
{
  "experimental": {
    "monitoring": {
      "interval": "5m",
      "urls": [
        "https://www.gstatic.com/generate_204",
        "https://cp.cloudflare.com"
      ],
      "url_test_timeout": "5s",
      "on_demand_timeouts": ["1s", "3s", "10s"],
      "idle_timeout": "10m"
    }
  }
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `interval` | duration | `5m` | How often outbounds are tested. |
| `urls` | list of strings | `["https://www.gstatic.com/generate_204"]` | Test addresses, in order of preference. |
| `ipinfo_url` | string | `""` | An IP information service to try first, for example from your subscription. |
| `verify_ipv6` | bool | `false` | After each outbound's URL test, the same URL is fetched once more over the host's IPv6 address through it, once per run, to learn whether the outbound carries IPv6; see [IPv6 by outbound](../dns/ipv6-by-outbound.md). |
| `ipv6_declared` | object, tag to bool | | Outbounds whose IPv6 the link declared (`ipv6=1`, `ipv6=0`); known from the start. |
| `ipv6_probe` | | | Retired, no effect. |
| `workers` | int | `10` | Tests that run at once. |
| `url_test_timeout` | duration | `5s` | Longest time for one test of the cycle, and for one IP information request. |
| `on_demand_timeouts` | list of durations | `["1s", "3s", "10s"]` | The marks of a test asked for: unavailable for now at the first with no answer, a failed attempt tried again at each but the last, which is the deadline. The first mark is skipped for an outbound that worked in this run. |
| `idle_timeout` | duration | `10m` | Stop testing after this long with no connections. |
| `debounce_window` | duration | `500ms` | How long to collect results before groups get an update. |

The IP information services see a request from the exit IP address of each outbound.

## See also

- [Balancer](balancer.md)
- [Fallback](fallback.md)
- [Psiphon](../protocols/psiphon.md)
- [DNSTT](../protocols/dnstt.md)
