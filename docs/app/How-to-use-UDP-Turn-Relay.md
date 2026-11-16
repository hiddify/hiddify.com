---
title: How to use UDP Turn Relay in Hiddify app
---

# How to use UDP Turn Relay

!!! warning "Not supported in Hiddify app 4 and later"
    The `relay=` parameter described here works only in the old Hiddify app 2.x (Hiddify Next). Since version 4.0 (February 2026), when the app's core moved to sing-box 1.13, the parameter is ignored, and it is still ignored in Hiddify app 5.9: a link with `relay=` connects directly to the server, without the relay. This page is kept for reference.

## What it was

UDP Turn Relay uses the TURN server of a messenger as a relay. TURN servers carry the voice and video calls of messengers. When a messenger works inside a filtered network (a domestic messenger, or a foreign one that is not blocked), its TURN server can pass your traffic on to your own server. The connection looked like this:

<div align=center>

<img width=100% alt="UDP Turn Relay diagram" src="https://github.com/hiddify/hiddify-next/assets/125398461/037262d4-ad89-45c0-bcab-c6504c08d3df">

</div>

It worked only with configs that run over UDP, such as Hysteria2 and TUIC v5. It did not work with Reality or other TCP configs.

## The link format

The relay was added to the end of a Hysteria2 or TUIC link as a URL-encoded `relay` parameter:

```
relay=urlencoded(turn://user:pass@host:port?realm=realm)
```

- `user` and `pass`: the username and password of the messenger's TURN server.
- `host` and `port`: the address of the TURN server.
- `realm`: the TURN realm (the authentication area) of the server.

For example, `turn://user:pass@turn.example.com:443?realm=example.com` URL-encoded is:

```
relay=turn%3A%2F%2Fuser%3Apass%40turn.example.com%3A443%3Frealm%3Dexample.com
```

It goes before the `#` of the link, after an `&`:

```
hysteria2://password@server.example.com:443?obfs=salamander&obfs-password=secret&sni=www.speedtest.net&insecure=1&relay=turn%3A%2F%2Fuser%3Apass%40turn.example.com%3A443%3Frealm%3Dexample.com#test
```

Messengers close their TURN servers to this kind of use quickly: the one used in the first examples (Bale) did so within a short time.

## What to use instead

To reach your server through another path with the current app, see [Chain, Extra security and Proxy unblocker](Chain-Extra-security-and-Proxy-unblocker.md) (WARP or Psiphon before or after your server) and, on the server side, [relay servers](/manager/domain-worker-cdn-and-tunneling/How-to-setup-relay-server-using-Hiddify-Relay-Builder/).

## Related articles

- [How to use the Hiddify app](How-to-use-Hiddify-app.md): add a profile, connect, the basic settings
- [How to install the Hiddify app](How-to-install-Hiddify-app.md)
