---
title: Features
weight: 10
---

# Core features

Features and fixes in the Hiddify fork that upstream sing-box does not have. Each feature page has
an English and a Persian version.

## Features

- [TLS fragment](tls-fragment.md): split the ClientHello into small pieces with pauses, so DPI cannot read the server name.
- [TLS tricks](tls-tricks.md): a mixed-case server name and a padding extension in the ClientHello.
- [REALITY in Hiddify](reality-hiddify.md): the post-quantum key share, the `key_share` option, and fragmentation on REALITY.
- [PROXY protocol](proxy-protocol.md): inbounds read the PROXY protocol header and the direct outbound sends it.

## Protocols

- [WARP](protocols/warp.md): Cloudflare WARP over WireGuard, AmneziaWG or MASQUE, with free account registration, noise packets and an endpoint scanner that fails over per network.
- [WARP scanner and noise](protocols/warp-scanner.md): how the endpoint scanner, the noise modes and presets (DNS, QUIC, SIP, random), the noise search and auto mode find a way through.
- [WARP over MASQUE](protocols/warp-masque.md): the standalone `masque` outbound for WARP over HTTP/3, HTTP/2 or both, with a device enrolled elsewhere; to register one, use the `warp` endpoint with `mode` `masque`; for a self-hosted MASQUE server, use upstream `masque-client`.
- [AmneziaWG](protocols/amneziawg.md): WireGuard with junk packets, padded handshakes and custom message types that defeat WireGuard fingerprinting.
- [WireGuard: Hiddify additions](protocols/wireguard-hiddify.md): noise packets before handshakes, per-peer user names, socket recovery and UDP fragmentation on by default.
- [WireGuard outbound (legacy format)](protocols/wireguard-legacy.md): the old WireGuard outbound that upstream removed, kept so old configs still load.
- [VLESS encryption](protocols/vless-encryption.md): Xray's post-quantum VLESS encryption, with Vision over it even without TLS.
- [Sudoku](protocols/sudoku.md): an encrypted TCP proxy that sends its bytes as sudoku clues, so traffic looks like text or has low randomness, with optional HTTP tunnels (build tag `with_sudoku`).
- [Mieru](protocols/mieru.md): a fully encrypted, padded proxy over TCP or UDP port ranges with no fixed pattern.
- [TrustTunnel](protocols/trusttunnel.md): proxy traffic as HTTP CONNECT streams over HTTP/2 or HTTP/3.
- [SSH](protocols/ssh.md): an SSH server inbound for port forwarding, plus UDP over TCP and a background connection for the SSH outbound.
- [Psiphon](protocols/psiphon.md): connect through the Psiphon network with no server of your own, and pick the exit country.
- [DNSTT](protocols/dnstt.md): carry traffic inside DNS queries through public resolvers, which it finds by itself.
- [MasterDNS](protocols/masterdns.md): the MasterDnsVPN tunnel over public resolvers, with a small header, packet duplication over several resolvers and MTU tests; the server connects to the destination itself.
- [Soar](protocols/soar.md): Lantern's DNS tunnel, every resolver a path of its own with fast loss recovery and resolver discovery, through the smart pool by default; `soar://` links.
- [GooseRelay](protocols/gooserelay.md): send traffic through Google Apps Script to your own server, so the network sees only HTTPS to Google.
- [Call tunnel](protocols/call.md): carry proxy traffic inside a video call on VK, Telemost, Dion, WB Stream or Bitrix24, so it looks like a call to an allowed domestic service; not tested end to end (build tag `with_call`).
- [Tunnel](protocols/tunnel.md): a reverse tunnel that reaches machines behind NAT through a public server.
- [Bond](protocols/bond.md): split each connection over several outbounds at once and join it on the server, to add up throttled connections (build tag `with_bond`).

## Transports

- [XHTTP](transports/xhttp.md): Xray's XHTTP transport with its modes, padding, placements, XMUX and split download.
- [mKCP](transports/kcp.md): Xray 26's mKCP over UDP for lossy or TCP-throttled networks, hidden by finalmask UDP masks (build tag `with_kcp`).
- [XDRIVE](transports/xdrive.md): Xray's storage transport, a VLESS connection carried in files on Google Drive, S3 or another storage service, so the client never contacts the server (build tag `with_xdrive`).
- [Raw transport](transports/raw.md): the `raw` transport, so configs converted from Xray load.
- [Custom gRPC paths](transports/grpc-custom-path.md): Xray-style multi-segment gRPC paths in `service_name`.
- [finalmask](transports/finalmask.md): Xray's finalmask masks (fragment, noise, header-custom, xdns over UDP, TCP or DoH, udphop, merge, oob and more) on every connection an outbound dials.
- [Shadowsocks simple-obfs server](transports/shadowsocks-obfs.md): a simple-obfs server on Shadowsocks inbounds, with a decoy when obfs or login fails.
- [rmux](transports/rmux.md): one more multiplex protocol for many connections in one, next to smux, yamux and h2mux.

## DNS

- [DNS group](dns/dns-group.md): ask several DNS servers at once, in turn, or stick to the one that works, and drop poisoned answers.
- [DNS rules: bypass_if_failed](dns/dns-bypass-if-failed.md): when a DNS rule's server fails, the query goes on to the next matching rule.
- [Smart resolver pool](dns/smart-dns-pool.md): the resolver pool each DNS tunnel outbound runs for itself with `smart_pool`, shared by DNSTT, MasterDNS and Soar, with `auto` resolvers, saved scores and DoT/DoH.
- [DNSCrypt (SDNS stamps)](dns/sdns.md): the `sdns` server, which sends encrypted queries to a DNSCrypt resolver given by its stamp.
- [sslip.io names](dns/sslip-hosts.md): the `hosts` server answers `sslip.io` names with the address written in the name.
- [IPv6 by outbound](dns/ipv6-by-outbound.md): IPv6 only through outbounds known to carry it, verified at the URL test and learned from the connections; a connection an outbound cannot carry is carried over IPv4 inside, so no app sees it die.

## Groups and monitoring

- [Balancer](groups/balancer.md): spread connections over members by round robin, lowest delay, consistent hashing, sticky sessions or a sticky pool.
- [Fallback](groups/fallback.md): try members in order and skip one that failed for a while.
- [URL test: Hiddify additions](groups/urltest.md): more test URLs, a `failover` mode, and a move to another member on the first failed connection.
- [Monitoring](groups/monitoring.md): background tests of every outbound for delay and exit IP, which feed the groups.
- [Lazy outbounds and keep top](groups/keep-top.md): outbounds created when first used and closed when idle, and only the fastest few of them in use, found a few at a time, so a profile of hundreds of proxies fits in the memory of a phone.
- [Unified delay](groups/unified-delay.md): URL tests time one HTTP round trip on an open connection, so delays compare across protocols.

## For app developers

- [App considerations](../app_considerations.md): what hiddify-app and hiddify-core need to change or know because of the v5 work.

## Credits

Hiddify's features build on these projects. Each feature page names what it takes from them, under "Sources and credits". Thanks to their authors.

- [SagerNet/sing-box](https://github.com/SagerNet/sing-box): the upstream this fork is built on.
- [shtorm-7/sing-box-extended](https://github.com/shtorm-7/sing-box-extended): call tunnel, bond, fallback, Sudoku, rmux.
- [Leadaxe/sing-box-lx](https://github.com/Leadaxe/sing-box-lx): URL test additions, REALITY `key_share`, MASQUE failover, DNS group modes.
- [reF1nd/sing-box](https://github.com/reF1nd/sing-box): DNS group, WireGuard recovery and other fixes.
- [kyochikuto/sing-box-plus](https://github.com/kyochikuto/sing-box-plus): the WARP scanner's WireGuard probe.
- [XTLS/Xray-core](https://github.com/XTLS/Xray-core): XHTTP, mKCP, XDRIVE, finalmask, VLESS encryption.
- [patterniha/Xray-core](https://github.com/patterniha/Xray-core): the `merge` and `oob` masks.
- [PoriyaVali/mirage](https://github.com/PoriyaVali/mirage): the `mirage` mask.
- [amnezia-vpn/amneziawg-go](https://github.com/amnezia-vpn/amneziawg-go): AmneziaWG.
- [enfein/mieru](https://github.com/enfein/mieru): Mieru.
- [SUDOKU-ASCII/sudoku](https://github.com/SUDOKU-ASCII/sudoku): the Sudoku protocol.
- [TrustTunnel/TrustTunnel](https://github.com/TrustTunnel/TrustTunnel): the TrustTunnel protocol.
- [xchacha20-poly1305/sing-trusttunnel](https://github.com/xchacha20-poly1305/sing-trusttunnel): the TrustTunnel library.
- [Psiphon-Labs/psiphon-tunnel-core](https://github.com/Psiphon-Labs/psiphon-tunnel-core): Psiphon.
- [dnstt](https://www.bamsoftware.com/software/dnstt/): the original DNSTT.
- [net2share/vaydns](https://github.com/net2share/vaydns): the DNSTT client.
- [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN): MasterDNS.
- [getlantern/soar](https://github.com/getlantern/soar): Soar.
- [Kianmhz/GooseRelayVPN](https://github.com/Kianmhz/GooseRelayVPN): GooseRelay.
- [kulikov0/headless-client](https://github.com/kulikov0/headless-client): Chrome fingerprints for the call tunnel.
- [Diniboy1123/connect-ip-go](https://github.com/Diniboy1123/connect-ip-go): CONNECT-IP for WARP over MASQUE.
- [Leadaxe/utls-lx](https://github.com/Leadaxe/utls-lx): current browser TLS fingerprints.
- [ameshkov/dnscrypt](https://github.com/ameshkov/dnscrypt): DNSCrypt.
- [pires/go-proxyproto](https://github.com/pires/go-proxyproto): the PROXY protocol.
- [shadowsocks/simple-obfs](https://github.com/shadowsocks/simple-obfs): simple-obfs.

## Bug fixes

- [v5 bug fixes](../bugfix/v5.md): bugs fixed on top of sing-box v1.15, newest first, each with its commit.
