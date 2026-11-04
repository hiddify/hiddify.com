# Unified delay

[All Hiddify features](../../index.md)

With unified delay, a URL test measures one HTTP round trip over a connection that is already
open, instead of the time to open the connection and get the first answer. It is a switch in
the `experimental` block: `"unified_delay": {"enabled": true}`.

## Why use it

A normal URL test includes the handshakes: TCP, the proxy protocol, and TLS to the test site.
Protocols with longer handshakes look slower even when they carry traffic just as fast, and the
numbers jump with the cost of each new connection.

With unified delay, every outbound is measured the same way, on an open connection. The numbers
are lower, steadier and easier to compare between protocols. Turn it off when you care about the
time to open a new connection, for example for many short connections.

## How it gets past filtering

It does not. It only changes how delay is measured.

## How it works

- The test opens the connection and sends its HEAD request, as usual.
- After the answer, it sends the same request again on the same connection, and reports the time
  of this second request only.
- If either request fails, the test fails.
- It applies to every URL test that sing-box runs: URL test groups, [monitoring](monitoring.md)
  (and with it the [balancer](balancer.md)), and the tests the app asks for. The delay test of
  the Clash API is not affected.

## Configuration

```json
{
  "experimental": {
    "unified_delay": {
      "enabled": true
    }
  }
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `unified_delay.enabled` | bool | `false` | Report the time of a second request on the open connection. |

The test site must keep the connection open after the first answer. Common test addresses such
as `https://www.gstatic.com/generate_204` do.

## See also

- [Monitoring](monitoring.md)
- [Balancer](balancer.md)
