# Sudoku

[All Hiddify features](../../index.md)

Sudoku is an encrypted proxy over TCP that hides its bytes as clues of small sudoku puzzles. You can
tune the result to look like plain text or to have a fixed, low randomness instead of looking
like random noise. It is the inbound and outbound `"type": "sudoku"`. It carries TCP, and UDP
inside the TCP connection. It is the Sudoku protocol of [saba-futai/sudoku](https://github.com/saba-futai/sudoku),
which mihomo also supports, ported from sing-box-extended.

## Why use it

- The network blocks traffic that looks fully random, the way plain Shadowsocks or VMess does.
- You want the traffic to look like plain text (`prefer_ascii`), or like HTTP from the first byte.
- You want an HTTP or WebSocket tunnel that can run behind a CDN (`stream`, `poll`, `ws`).

The cost is speed: every byte you upload becomes at least four bytes on the wire.

## How it gets past filtering

Some filters block connections whose bytes look completely random, because a normal protocol
shows some structure. Sudoku never sends its encrypted bytes directly. It sends sudoku clues
instead, and you choose how those look:

- `prefer_entropy` (default): the bytes on the wire follow a fixed bit pattern, so the traffic
  is less random than encrypted data.
- `prefer_ascii`: every byte on the wire is a printable character, so the traffic looks like
  text.
- `custom_table`: you choose which bits of each byte carry the clue, so the pattern differs from
  other Sudoku servers.

The HTTP mask adds an HTTP request in front of the connection (`legacy`), or runs the whole
connection as real HTTP or WebSocket requests that a CDN can forward (`stream`, `poll`, `ws`,
`auto`).

Limits:

- A filter can learn the byte pattern of a mode and block it. Tables and the HTTP mask make
  this harder, not impossible.
- The `legacy` mask is one fake HTTP request followed by non-HTTP data. It does not pass a CDN
  or a filter that reads past the first request.
- Without the HTTP mask and TLS, there is no TLS handshake, so a filter that allows only TLS
  blocks it.
- It does not help when the server's IP address is blocked, unless you put it behind a CDN.

## How it works

- Each byte value has its own 4×4 sudoku grid, picked from the 288 possible grids by the key.
  The sender sends four clues, each a cell position and its value, that fit only that grid. The
  receiver finds the grid and gets the byte back. Each byte has many possible sets of clues, and
  the sender picks one at random and in random order.
- Each clue is one byte on the wire, so upload traffic grows four times. Random padding bytes
  are mixed in as well (`padding_min` to `padding_max`).
- Download traffic uses the same encoding by default. With `enable_pure_downlink: false`, it
  uses a packed form that is about one and a third times the data, which is faster.
- Inside the encoding, the data is encrypted with `aead_method`. The handshake makes fresh
  session keys with X25519 and rejects replays.
- The client and server clocks must be within 60 seconds of each other, or the handshake fails.
- With `multiplex: "on"`, many connections share one Sudoku session.

## Configuration

Needs the `with_sudoku` build tag. Without it, a config with `"type": "sudoku"` fails with
"Sudoku is not included in this build, rebuild with -tags with_sudoku".

Server:

```json
{
  "type": "sudoku",
  "tag": "sudoku-in",
  "listen": "::",
  "listen_port": 8443,
  "key": "a long random password",
  "table_type": "prefer_ascii"
}
```

Client:

```json
{
  "type": "sudoku",
  "tag": "sudoku-out",
  "server": "example.com",
  "server_port": 8443,
  "key": "a long random password",
  "table_type": "prefer_ascii"
}
```

### Fields on both sides

These must be the same on the client and the server.

| Field | Type | Default | Meaning |
|---|---|---|---|
| `key` | string | required | The shared key. Either any password, or a key pair (see below). |
| `aead_method` | string | `chacha20-poly1305` | Encryption of the data: `chacha20-poly1305`, `aes-128-gcm` or `none`. |
| `table_type` | string | `prefer_entropy` | How the bytes look on the wire: `prefer_entropy`, `prefer_ascii`, `up_ascii_down_entropy` or `up_entropy_down_ascii`. "up" is client to server, "down" is server to client. |
| `custom_table` | string | `""` | Eight letters that set which bits of each byte carry what: exactly two `x`, two `p` and four `v`, for example `xpxvvpvv`. Used only in the `entropy` direction. |
| `custom_tables` | array of strings | `[]` | Several `custom_table` patterns. The client picks one per connection; the server finds out which one. Replaces `custom_table` when set. |
| `padding_min` | number | `10` | Least share of padding, in percent, `0` to `100`. |
| `padding_max` | number | `30` | Most share of padding, in percent, `0` to `100`. At least `padding_min`. |
| `enable_pure_downlink` | boolean | `true` | `true` encodes download traffic the same way as upload. `false` uses the packed form, which uses less data. |

If you set only one of `padding_min` and `padding_max`, the other one moves to match it when the
defaults would conflict.

When `custom_table` or `custom_tables` is set with an `entropy` upload direction, the server also
accepts clients that use the default table, so clients can switch one by one.

### Server (inbound) fields

The usual listen fields (`listen`, `listen_port`, …), plus:

| Field | Type | Default | Meaning |
|---|---|---|---|
| `handshake_timeout` | number | `5` | Seconds to wait for the client's handshake. HTTP tunnel modes wait at least `15`. |
| `disable_http_mask` | boolean | `false` | `true` turns the HTTP mask off. |
| `http_mask_mode` | string | `legacy` | `legacy`, `stream`, `poll`, `ws` or `auto`. `auto` accepts `stream`, `poll` and `ws` clients. |
| `path_root` | string | `""` | A first path segment put before all HTTP mask paths, for example `aabbcc` gives `/aabbcc/session`. Letters, digits, `_` and `-` only. |

The inbound has no TLS. For HTTPS, put a CDN or a reverse proxy that ends TLS in front of it.

`fallback` is a `host:port`. A connection that is not Sudoku, such as a browser or a prober, is
passed to it with what it already sent, so the server looks like the site there. It works when the
HTTP mask is off (`disable_http_mask`); a connection that sends more than 64 KiB before failing is
closed instead.

### Client (outbound) fields

The usual server and dial fields (`server`, `server_port`, `detour`, …), plus:

| Field | Type | Default | Meaning |
|---|---|---|---|
| `multiplex` | string | `off` | `off`, `auto` or `on`. `on` runs many connections over one Sudoku session. `auto` only reuses HTTP connections in the `stream`, `poll` and `auto` mask modes. |
| `http_mask` | object | mask on, `legacy` | The HTTP mask. Without this object the mask is on in `legacy` mode. |
| `http_mask.enabled` | boolean | `false` | Turns the mask on. Once you add `http_mask`, you must set this to `true`, or the mask is off. |
| `http_mask.mode` | string | `legacy` | `legacy`, `stream`, `poll`, `ws` or `auto`. `auto` tries `stream`, then `poll`. |
| `http_mask.host` | string | `""` | Host header and TLS server name for `stream`, `poll`, `ws` and `auto`. Empty uses `server`. |
| `http_mask.path_root` | string | `""` | Same as the server's `path_root`. |
| `http_mask.multiplex` | string | `""` | Overrides `multiplex` when set. |
| `http_mask.tls` | object | none | A normal outbound TLS block. Used only by `stream`, `poll`, `ws` and `auto`. |

### The HTTP mask on both sides

The client turns the mask on by default, and the server's mask follows `disable_http_mask`, which
is also on by default. Keep both sides the same:

- Client without `http_mask`, server without `disable_http_mask`: both use the `legacy` mask.
- To turn it off, set `"disable_http_mask": true` on the server and give the client
  `"http_mask": { "enabled": false }`.
- For a tunnel mode, set the same mode on both sides (or `auto` on the server), and the same
  `path_root`.

A `legacy` server also accepts clients without the mask. A server with the mask off does not
accept masked clients. A server in `stream`, `poll`, `ws` or `auto` mode does not accept `legacy`
clients.

### Keys

`key` is either:

- A password: the same text on both sides.
- A key pair: the server gets the public key (64 hex characters), and the client gets a private
  key (64 or 128 hex characters). The client can also use the public key itself. Several
  different private keys can belong to one public key, so each user can have their own.

This build has no command to make a key pair.

### Errors

A wrong `table_type`, `custom_table`, `aead_method`, padding, mode, `multiplex` or `path_root`,
or an empty `key`, stops the config from loading, on both sides.

### Compatibility

Tested only between two Hiddify sing-box instances: without the mask, with the HTTP mask, and with
`prefer_ascii`. It has not been tested against the original Sudoku or mihomo.

## See also

- [Mieru](mieru.md)
- [Shadowsocks obfs](../transports/shadowsocks-obfs.md)
- [XHTTP](../transports/xhttp.md)
