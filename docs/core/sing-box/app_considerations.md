---
weight: 20
---

# App considerations

What hiddify-app and hiddify-core need to change or know because of the v5 work in
hiddify-sing-box. Each item says what changed in the core, and what the app or hiddify-core should
do about it. Items marked **Required** break or misbehave until they are handled.

## Build

- **Submodules.** The core now uses six forks under `replace/`, each a git submodule on its own
  branch: `wireguard-go` (v5), `sing-tun` (dev), `gvisor` (go), `amneziawg-go` (v5), `sing-mux`
  (v5), plus the existing ones. `go.mod` and `test/go.mod` point at them with `replace`.
  **Required:** hiddify-core and every CI or gomobile build must check out submodules recursively
  (`git submodule update --init --recursive`), or the build fails on missing modules.
- **MasterDnsVPN fork.** `replace/MasterDnsVPN` (module `masterdnsvpn-go`, fork
  `github.com/hiddify/MasterDnsVPN`, branch `hiddify`) is the client of the `masterdns` outbound,
  with a library API in `lib/`. **Required:** hiddify-core's `go.mod` (and ray2sing's) need
  `replace masterdnsvpn-go => ./hiddify-sing-box/replace/MasterDnsVPN`, like the other
  `replace/` forks. No build tag.
- **Build tags.** `with_masque` is now in the core Makefile and in hiddify-core's Makefile
  (hiddify-core commit `6bea470`). Four new features are behind tags that are **off** by default:
  `with_kcp` (mKCP), `with_sudoku` (Sudoku), `with_bond` (Bond) and `with_call` (call tunnel). A
  config using one of them fails with "… is not included in this build" unless the tag is set.
  Decide per platform whether to ship them; `with_call` pulls in a large WebRTC stack. rmux needs
  no tag.
- **XDRIVE and the default tags.** The core Makefile's default tags meant to include
  `with_sudoku`, `with_call`, `with_bond` and `with_kcp` but joined them with `/`, so none of the
  four was built; they are now separated by commas, and `with_xdrive` (the XDRIVE transport) is
  added. hiddify-core's `PROTOCOL_TAGS` has `with_xdrive` too. A profile with
  `"transport": {"type": "xdrive"}` fails with "XDRIVE is not included in this build" without it.
- **Go 1.27 required.** Xray-core v26.10.31, which finalmask and XDRIVE use, needs Go 1.27, so
  `go.mod` and `test/go.mod` now say `go 1.27`. Every CI and gomobile build must use Go 1.27.3 or
  newer. (Binaries with Psiphon crashed at start when built with Go 1.27; fixed in `bb18926a9`.)
- **uTLS fork.** `github.com/metacubex/utls` is replaced by `github.com/Leadaxe/utls-lx` in
  `go.mod` and `test/go.mod`. The `firefox` fingerprint is now Firefox 148 and `safari` is
  Safari 26.3; `chrome` stays Chrome 133. Nothing to change in configs.
- **Tailscale.** The core Makefile no longer lists `with_tailscale` (`573719dd5`), so `tailscale`
  configs fail to load in the default build; keep the app from generating them, or build with the
  tag.

## Configuration the app generates

- **Required — WARP by id and auth_token.** A `warp` profile given by `id` and `auth_token` now
  needs `private_key` (the device's own key); without it the endpoint fails at start. Before, it
  started without a key and never worked.
- **Required — AmneziaWG on a wireguard endpoint.** A `wireguard` endpoint with an `awg` block now
  fails to load ("use type awg"); before, the block was ignored and the connection was plain
  WireGuard. Generate `"type": "awg"` for AmneziaWG, or a `warp` endpoint with an `awg` block.
- **Required — sdns stamps.** The `sdns` server accepts only DNSCrypt stamps, and now refuses a
  DoH, DoT or plain stamp when the config loads. Convert those stamps to `https`, `tls` or `udp`
  servers.
- **SSH and UDP.** The SSH outbound offers UDP only with `udp_over_tcp`; without it, UDP goes to
  another outbound. Set `udp_over_tcp` if UDP should go through SSH. On the SSH inbound,
  `host_key_algorithms` and `network` now take effect.
- **XHTTP mode.** An empty or `auto` mode now behaves as Xray's client: `stream-one` over REALITY,
  `stream-up` over REALITY with a separate `download`, `packet-up` otherwise. Before, the client
  always used `packet-up`, and an empty mode was an error. Configs that relied on `packet-up` over
  REALITY should set it explicitly.
- **tls_fragment in the tls block.** The core now moves a `tls_fragment` written inside an
  outbound's `tls` block to the dialer (unless the dialer has its own). hiddify-core's config
  patching that does the same can stay or be removed.
- **REALITY and fragmentation.** `tls.fragment` and `tls.record_fragment` now work with REALITY.
  hiddify-core skips fragmentation for REALITY nodes; that skip can be removed. The new
  `tls.reality.key_share` (`""`, `hybrid`, `classical`) is available; `classical` is refused by
  Xray 26.9.8 and newer servers.
- **TLS tricks.** `tls.tls_tricks` (mixed-case SNI, padding extension) now works for uTLS clients;
  padding with a `random` fingerprint is a config error.
- **Balancer.** `delay_acceptable_ratio` now defaults to 2 when unset or 0 (the app sends 2
  already). With `interrupt_exist_connections`, the hashing strategies interrupt only when the
  set of usable members changes, not on every test round.
- **Balancer connections are stable.** `lowest-delay` now honours `tolerance` (50 ms when unset;
  hiddify-core sends 20, with `tolerance_ratio` 0.3, so the rule is mostly relative) and
  `tolerance_ratio` (a tenth of the selected member's delay when unset),
  and keeps its member until one is faster by more than the larger of the two or it fails a
  test. Connections are closed only for a member that died (its own connections) and once, 30
  seconds after start, for the members the first tests left out. A faster member takes new
  connections only, so `interrupt_exist_connections: true` no longer cuts calls or downloads on
  every test round. The balancer starts from the cached results, and the first cycle tests the
  cached fastest member first.
- **Balancer `pool` strategy.** `strategy: "pool"` with `pool` and `sticky_hash` gives a fixed
  set of slots with sticky keys that do not move when another member dies (lx's `round_robin`).
  `tolerance` and `tolerance_ratio` let a faster member outside take a slot, as for lowest-delay;
  unset, the first working members keep their slots, so hiddify-core sends them to the
  lowest-delay group only. `sticky_hash` is `sticky-sessions`' key too.
- **URL test failover.** A failover member that is more than 2 times slower than the fastest
  other one, twice in a row, is now left for one more than 1.5 times faster.
- **A tapped or selected proxy answers at once.** The outbound a group's selection leads to is
  tested before the first cycle and again when the selection moves; a test asked for runs at
  once beside the cycle, in stages (`experimental.monitoring.on_demand_timeouts`, 1 s, 3 s,
  10 s by default): the app sees the proxy as unavailable after the first mark with no answer,
  then the answer, however late. A proxy is pinged once; only a failed attempt is tried again,
  at the next mark. A tap while the proxy is being tested joins that test instead of a second
  ping, and a selection measured in the last 15 s is not tested again. A ping cached from the
  previous run decides nothing and is not shown: it orders the members until the real pings
  arrive, and the app's proxy list sorts by `sort_delay`, which carries it, while
  `url_test_delay` stays 0 for it. hiddify-core sets the
  lowest-delay groups' `tolerance` to 20 ms and `tolerance_ratio` to 0.3: an absolute 100 ms
  kept a 59 ms member over a 25 ms one. The `MONITORING` and `LOWEST` log lines say why each
  test ran and what the group decided. hiddify-core keeps a profile's proxy tags stable across
  its updates (an unchanged proxy keeps the tag it had, whatever its new position in the list),
  so a hot reload after a subscription update keeps the unchanged proxies and their pings and
  tests only what changed; keep top keeps its pick while every kept proxy is unchanged and none
  timed out. A proxy that worked in this run skips the first mark: it keeps its ping
  through a slow answer rather than flicker to unavailable after one second. The delay is
  published before the IP
  lookup, so the IP arrives after the ping. Nothing to set; the core's defaults are these.
- **IPv6 for the apps is off by default, and verified per proxy when on.** hiddify-core answers
  the apps with `ipv4_only` DNS rules and rejects every IPv6 destination before the sniff rule
  (so before the handshake) unless the IPv6 mode turns IPv6 on; the app's routing page says why
  (most exits have no IPv6, and a connection the proxy cannot carry dies after it opened, which
  browsers never retry). When on, the core sets `verify_ipv6` (each proxy's URL test is followed
  once per run by the same URL over IPv6, cached per proxy), `route.ipv6_fallback` (an IPv6
  connection through a proxy not known yet is carried over IPv4 inside the connection and
  teaches the proxy's IPv6), `ipv6_by_outbound` on the DNS rules answering the apps and an
  `ipv6_unavailable_via` reject rule on the main selector, both fail-open. A subscription turns
  IPv6 on for its profile with an `ipv6-mode: prefer_ipv4` header (the app's override list), and
  a share link declares its proxy with `ipv6=1` or `ipv6=0` (ray2sing, `ipv6_declared`). No
  probe of a public address is made (`ipv6_probe` is retired): the verification uses the user's
  own test URL. See [IPv6 by outbound](features/dns/ipv6-by-outbound.md).
- **MasterDNS outbound.** `"type": "masterdns"` (display name `MasterDNS`) is a new outbound
  type for MasterDnsVPN servers: `domains`, `resolvers`, `encryption`, `key`, `mode` and tuning
  fields, see [MasterDNS](features/protocols/masterdns.md). TCP only; in `socks5` mode it needs
  no outbound behind it, in `tcp` mode the app chains a `socks` or `ssh` outbound with `detour`
  as for DNSTT. Its status is CONNECTING until the resolvers are tested and the session is open,
  which can take several seconds; the app should show that rather than an error. ray2sing reads
  `masterdns://` links, `slipnet://` links (SlipNet profiles for DNSTT, NoizDNS and VayDNS) as
  `dnstt` outbounds with a `socks` or `ssh` outbound in front, and `dnst://` links (the dnst URL
  spec, github.com/net2share/dnst-url-spec) for the dnstt, vaydns and masterdns transports.
- **Soar outbound.** `"type": "soar"` (display name `Soar`) is a new outbound type for Soar
  servers (`github.com/getlantern/soar`): `domain`, `public_key`, `resolvers` and tuning fields,
  see [Soar](features/protocols/soar.md). TCP only, no outbound behind it. The resolvers
  written go through its smart pool, on by default; `auto` or no resolvers runs Soar's own
  discovery. The session
  opens at the first connection, so the status is CONNECTING until then. ray2sing reads
  `soar://` links: WhiteDNS's profile link (base64url JSON, schema `whitedns.profile`) and a URL
  form. The JSON editor offers a `soar` template.
- **Links turn the masterdns smart pool on.** ray2sing gives a `masterdns://` or `dnst://`
  masterdns outbound `smart_pool` unless the link says `smart_pool=0` or lists an address range,
  and a link without resolvers gets `auto`. It also reads WhiteDNS's `masterdns://` profile link.
- **Shared resolver discovery.** `smart_pool.discovery` (`country`, `sample_ranges`, `want`,
  `concurrency`, `pace`) is the same block for `dnstt`, `masterdns` and `soar`: their `auto`
  starts with the candidates of Soar's discovery (device resolvers, the country's bundled list,
  global resolvers), then the built-in list. hiddify-core fills `discovery.country` from the
  app's region when it is empty. Links take `country`, `sample_ranges`, `discovery_want`,
  `discovery_concurrency` and `discovery_pace`.
- **Soar fork.** `replace/soar` (module `github.com/getlantern/soar`, to be forked as
  `github.com/hiddify/soar`, branch `hiddify`) adds `Discovery.List()`, so the pool takes Soar's
  discovery candidates from Soar's own code. hiddify-core's `go.mod` needs
  `replace github.com/getlantern/soar => ./hiddify-sing-box/replace/soar`, like the other forks.
- **Smart resolver pool, per outbound.** `dnstt`, `masterdns` and `soar` take `smart_pool`, `true` or an
  object (`load_balance`, `deadline`, `per_attempt`, `probe_interval`, `down_after`); the
  resolver list, scores, probe and pool of every DNS tunnel are one shared package,
  `common/dnspool`, and each outbound runs its own pool. With it, `auto`, DoT and DoH resolvers
  work for both tunnels. See [Smart resolver pool](features/dns/smart-dns-pool.md).
  **Required:** the `smart_dns_pool` service is removed; a config with it fails to load. Set
  `smart_pool` on the outbound instead.
- **New options worth exposing:**
  - DNS group: `mode` `stable` and `fastest`, `error_ttl`, `win_ttl`.
  - URL test: `urls` (more test URLs) and `mode: "failover"`.
  - WARP: `scanner` (endpoint scanner with per-network scores) with `search_noise` (it also
    looks for a noise preset that gets through, see the WARP page) and `noise_presets`;
    `noise.fake_packet.mode` `"quic"` and `"raw"`, `noise.fake_packet.packets` (AmneziaWG-style
    templates, for the "WG Mimic" DNS, QUIC and SIP configs); the `awg`
    block with AmneziaWG 3.x settings and the QUIC masquerade (`ip`, `id`, `ib`).
  - MASQUE: `vhttp` (`h3`, `h2`, `auto`), `server_name`, `scanner`, `mtu`, `unique_identifier`.
  - AmneziaWG: 3.x settings (`header_protection_key`, `content_padding_addition`, the timers,
    `random_trailers`, `disable_cookies`), `s3`/`s4` and `h1`–`h4` ranges now work.
  - Multiplex: `protocol: "rmux"`.
  - New types (build-tagged): `mkcp` transport, `sudoku`, `bond`, `call`; new `fallback` group.
- **WARP mode.** A `warp` endpoint takes `mode`: `wg`, `awg`, `masque` or `auto`. `auto` races
  one handshake per tunnel and runs the fastest; it needs `with_masque` for the MASQUE leg. The app
  can offer `auto` as the default WARP choice. Its display type is `WARP · Auto` until it chose,
  then the chosen tunnel's.
- **WARP behind a detour.** Searching for a way in through a detour only measures the detour, so
  for every `warp` endpoint with a `detour` (the extra security hop, WARP in WARP) hiddify-core
  sets `rotate_ports: false`, turns the scanner off and gives an IPv6 WARP address as
  `fallback_address`: the endpoint tries the profile's IPv4 address, then that IPv6 one. It also
  turns off the scanner of a `masque` outbound with a `detour`. MTU discovery is on for every
  WireGuard and AmneziaWG tunnel; a config can turn it off with `"mtu_discovery": false`.
- **WARP devices are kept, in a pool.** Registered devices are kept in one pool in the cache file
  (key `warp-profiles`), shared by every warp endpoint; each endpoint leases devices of its own,
  so several warp endpoints in one config never share one. A device is only replaced when
  Cloudflare says it is gone, disabled or out of quota, not when the network blocks it. Keep
  `store_warp_config` on, and a stable `unique_identifier` per endpoint (it takes its own device
  back first), or every start registers again (and Cloudflare limits registrations).
- **Status in OutboundInfo.** `OutboundInfo.status` (field 18, enum `Status`: READY, CONNECTING,
  RECONNECTING, SEARCHING, FAILED, REGISTERING) mirrors `adapter.Status`, so the app can show the
  state without parsing the label (in hiddify-core, uncommitted at the time of writing).
- **IP information from the cache.** At start every outbound shows the exit IP and country of
  the last run, from the cache, until a working test of this run looks them up again (a failed
  test leaves them as they are). The exit IP of WARP, Psiphon or a rotating proxy can change
  between runs, so `URLTestHistory.IpInfoFromCache` says which they are, and hiddify-core sends it
  as `IpInfo.from_cache`. Show such an IP as not confirmed yet (dimmed, or with a mark).
- **Core STARTED and a single proxy.** hiddify-core moves WAITING → STARTED from the ping of the
  `lowest` (lowest-delay) balancer when the profile has 2+ proxies. With only one proxy, `lowest`
  is not built; connectivity then uses that proxy's own ping (the select leaf) so the core does
  not stay WAITING ("Connecting") forever.
- **MASQUE devices from links.** The `masque` outbound never registers a WARP device: it needs
  `device`, and a config without one fails to load ("use the warp endpoint with mode masque").
  A device needs no `endpoint_public_key`: the edge's fixed key is built in. The port of an
  endpoint written as `ip:port` is used. A `masque://` link to WARP (an endpoint in WARP's ranges
  or under `cloudflareclient.com`, or Cloudflare's server name, or none) is a `warp` endpoint with
  `mode` `masque` (ray2sing): the link's key goes to `masque.device`, and a link without a key gets
  a saved or registered device from the WARP pool. When Cloudflare refuses `masque.device`, WARP
  remembers it in the cache file (`<unique_identifier>/refused-masque-device`) and takes a pool
  device, so the cache file matters for such configs too. ray2sing sets `unique_identifier` from
  the link's device id, else a hash of its key or endpoints, so renaming the profile keeps its
  devices. Only a link to another MASQUE server stays a `masque` outbound, and needs its key.
- **WARP over MASQUE in the warp endpoint.** A `warp` endpoint can now run MASQUE instead of
  WireGuard: `"masque": {"enabled": true}`, or any MASQUE setting (`vhttp`, `server_name`,
  `use_ipv6`, `tls`, …). Prefer this to a separate `masque` outbound: one endpoint handles
  registration, the scanner and failover for all three tunnels. An empty `"masque": {}` is
  dropped by the config parser and gives WireGuard, so always write `enabled` or a setting.
  `awg` and `masque` together fail the config. MASQUE needs the `with_masque` tag. The MASQUE
  device is saved apart from the WireGuard one (`<unique_identifier>/masque`), so switching an
  endpoint between the two does not break either.
- **Enrolled MASQUE devices (`device`).** A `masque` outbound can use a device enrolled
  elsewhere, as `masque://` share links carry it, instead of registering one through Cloudflare's
  API (often blocked). ray2sing writes `masque://` links to this option, and their `inner=` link as
  a second outbound whose detour is the first.
- **Self-hosted MASQUE.** Use upstream's `masque-client` (and `masque-server`). The Hiddify
  `masque` type is WARP only.
- **Display types.** WARP shows `WARP · WG`, `WARP · AWG` or `WARP · MASQUE`; the `masque`
  outbound shows `WARP · MASQUE`. After them comes the endpoint the scanner chose
  (` · 🔍 <address:port>`, or ` · 🔍 Not found`). If the app maps display types to icons or
  labels, match on the prefix.
- **Status, for every outbound and endpoint.** `IsReady() bool` is replaced by
  `Status() adapter.Status`: `StatusReady`, `StatusConnecting`, `StatusReconnecting`,
  `StatusSearching`, `StatusFailed` and `StatusRegistering`; `adapter.IsReady(o)` is the yes/no.
  `adapter.DisplayType(o)` is the type and what the status cannot say, nothing more: the
  resolvers a DNS tunnel uses (`MasterDNS · 3 resolvers`), the endpoint the WARP scanner chose.
  It has no status mark (no ` ⏳ Connecting...`, no `✔️`): hiddify-core sends the status on its
  own (`OutboundInfo.status`) and the app shows it. A failed outbound adds why it failed,
  `adapter.StatusError(o)`: `Invalid: bad uuid`, `WARP · WG: <error>`. While it is only
  connecting, the error of its last attempt goes to `OutboundInfo.error` and not to the type
  (SSH's last connection error, for example). The app's `typeWithoutStatus` still strips the
  marks an older core sends.
- **WARP registration fallback.** When registration through `profile.detour` fails, WARP (all
  three tunnels) tries again through every other outbound, direct included. That was already so
  for WireGuard and is kept; it lets a cold detour group not block registration, but it means
  Cloudflare's API can be reached outside the detour. If the app must never do that, it should
  not rely on `profile.detour` alone, or ask for an option to turn the fallback off. The `masque`
  outbound only uses its `profile.detour`.
- **MASQUE profile key.** The saved MASQUE profile is still keyed by the tag unless
  `unique_identifier` is set. If the app renames outbounds, set `unique_identifier` so the device
  is not registered again.
- **Schema.** `docs/schema.json` is generated again (`make schema`) and now covers the Hiddify
  options. Editors or validators that use it should take the new file.

## Security

- **MPTCP is off unless asked.** Inbounds and outbounds use Multipath TCP only with
  `tcp_multi_path: true`; the Go default (on, for listeners, since Go 1.24) is overridden in
  the code and by `godebug multipathtcp=0` in `go.mod`. A main module that builds sing-box
  into its own binary needs the same `godebug` line in its `go.mod`, as hiddify-core has, or
  `-X runtime.godebugDefault=multipathtcp=0` in its link flags; `internal/godebug.defaultGODEBUG`
  is not a symbol and does nothing. Keep inbounds on `127.0.0.1` unless the LAN really needs
  them, and keep the Linux kernel updated.

## Network changes and caches

- **Network change callbacks.** WARP and MASQUE now react to network changes: they check the
  current endpoint and only rescan when it fails, and they name the network by asking
  `cloudflare.com/cdn-cgi/trace` (or `speedtest.net`), not by SSID, so no location permission is
  needed. The DNS group clears its record of failed servers. All of this relies on the platform
  reporting interface changes as it does today; keep that working.
- **Cache file.** Scanner scores, the WARP config and the MASQUE profile are kept in the cache
  file. Keep `experimental.cache_file` enabled, with `store_warp_config` and `store_masque_config`
  where wanted; without the cache file, every start registers a new WARP/MASQUE device and scans
  from scratch.

## Reports

- **Crash, OOM and power reports are not encrypted.** The `encrypt` request is accepted and
  ignored, and archives are always named `.zip` (no more `.age`). Instead the archive leaves out
  the configuration and the list of open connections, and scrubs logs and other text of IP
  addresses, proxy links and DNS stamps, URL paths and queries, UUIDs, emails and key=value
  secrets. The app's "include configuration" option no longer adds the configuration. The app
  should stop showing an "encrypted" state for reports.

## Behaviour the app should know about

- **finalmask follows Xray v26.10.** `xdns` takes `domains` as `{"names": [...]}` and
  `resolvers` as `{"addrs": [...]}`, with DoH resolvers (`https://…` plus `tlsConfig`); the older
  string forms still load. New masks: `udphop`, noise `type: "exp"` and `script`. Masks are now
  dialed through: `xdns` and `udphop` open their own sockets with the outbound's dialer. Links
  carry finalmask as JSON (`fm=`), which ray2sing passes through unchanged, so nothing to change
  in link parsing for the new masks.
- **XDRIVE.** The `xdrive` transport needs VLESS with `encryption` for an Xray server. The
  outbound's `server` and `server_port` are required but unused; the app may show them as
  meaningless for such a profile. Each proxy connection is its own storage session, since the
  client has no Mux.Cool: a profile on Google Drive is slow and spends API quota, so a URL test
  every few minutes costs a session each time.

- **URL test.** A dial that fails because the path is dead moves the group to another member
  immediately, without closing live connections, so the selected member can change between tests.
  `failover` keeps a member until it fails. A URL test or balancer that moves now signals
  monitoring at once, as a selector does, so the proxy list stream updates without waiting for
  the next test.
- **WARP behind a group.** WARP (and the `masque` outbound) moves at once when the user changes a
  selector in its detour, but follows a URL test or balancer at most every 30 seconds, through a
  new tunnel that replaces the old one only once it connects. hiddify-core's chain mode
  `selectable` relies on this: in Extra Security its WARP hops dial through `select`, and the user can move both
  `select` and the hop selector on the fly. The app offers `selectable` as a
  mode of both hops; the proxy list then has a selectable group named after the hop (`🔒 Extra
  Security · Selectable` or `🔓 Unblocker · Selectable`; its tag ends in `§hide§` like every chain
  hop, so do not hide it) whose items are `Lowest → <hop>` (the
  default, a lowest-delay balancer) and each WARP tunnel and Psiphon, moved with `SelectOutbound`.
- **Why a proxy failed.** The URL test history keeps the error of a failed test (`Error`), and an
  outbound that is not ready says why through `adapter.StatusError` (WARP and MASQUE: a refused
  registration, a tunnel that does not connect, with the tunnel's last connect error). hiddify-core
  passes either to the app as `OutboundInfo.error`, for the proxy's details. A result loaded from
  the cache keeps its error only until the next test. See
  [Monitoring](features/groups/monitoring.md).
- **Fake DNS rule.** The DNS rules hiddify-core generates set `strategy`, which keeps sing-box in
  legacy DNS mode. A `query_type` (or `ip_version`) matcher in any DNS rule then makes the router
  refuse to start, with "Legacy `strategy` DNS rule action option is deprecated", and the app
  stays on Connecting. The fake IP rule therefore matches every query with `bypass_if_failed`;
  queries other than A and AAAA fail at the fake IP server, at debug level only, and go on to
  the remote rule. See [bypass_if_failed](features/dns/dns-bypass-if-failed.md).
- **DNS predefined answers.** In legacy DNS mode, A/AAAA records in 10.0.0.0/8 and
  2001:4188:2:600::/64 are removed from `predefined` answers (`dns/blocked_checker.go`). This is
  deliberate and tested, but a predefined answer in those ranges returns nothing; keep it in mind
  when generating predefined rules.
- **Rule sets.** A remote rule set without a cached copy starts empty and is downloaded once the
  service is up; a failed download is retried after 1 s, 10 s, 30 s, 1 min, 5 min, 10 min, then
  every 30 min. Rules that depend on it apply only once it arrives.
- **Reverse tunnel.** `tunnel_server` / `tunnel_client` now carry traffic: route rules must set
  `override_tunnel_destination` on the server.

## Call tunnel (if shipped)

- The call link is the tunnel's only key: anyone with it can read the tunnel or use the server as a
  proxy. Treat join links as secrets in the UI, in shared configs and in logs. The server logs the
  link of a call it creates, which is how the user learns it.
- Account cookies and the Dion password are stored in the config in plain text; store configs
  that contain them with the same care as other credentials.
- Only the server side (inbound) needs an account; the client joins as a guest. Bitrix24 has no
  server side in this build.
- Not tested end to end in Hiddify.

## Deferred, needs the app

- **Android auto-redirect rework** (from reF1nd 74f12fb8) is not ported: it changes the gomobile
  `PlatformInterface`, so it needs matching changes in hiddify-app's Android code.

## Repositories

All forks have GitHub repos under `github.com/hiddify/` (`sing-tun`, `gvisor`, `wireguard-go`,
`amneziawg-go`, `sing-mux`, and the older ones). Nothing has been pushed yet: push each fork's
branch before pushing hiddify-sing-box, or the submodule commits cannot be fetched.
