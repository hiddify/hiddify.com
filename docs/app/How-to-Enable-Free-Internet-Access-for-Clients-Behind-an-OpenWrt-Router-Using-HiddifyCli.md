---
title: Free internet for every device behind an OpenWrt router
---

# Free internet for every device behind an OpenWrt router

With Hiddify Core on your OpenWrt router, every phone, laptop, TV and game console at home can use your proxy, without installing anything on them. This page explains how.

!!! note "Written for Hiddify Core 5.9"
    This page is for Hiddify Core **5.9** (5.9.3). Older versions of this guide set this up by hand with `redsocks` and `iptables` rules. That is not needed any more: the Hiddify Core package has a **router mode** that does it, and the old `iptables` commands do not work on OpenWrt 22.03 and newer, which use nftables.

## Before you start

Install Hiddify Core on the router and give it your connection link: follow [Hiddify Core on OpenWrt](How-to-use-HiddifyCli-on-OpenWrt.md), steps 1 and 2.

## Router mode (the default)

The Hiddify Core package starts in **router mode**. In this mode:

- every device behind the router goes through the proxy, for TCP, UDP and ping;
- nothing needs to be set up on the devices: they keep using the router as usual;
- connections from outside still reach the router and its port forwards.

To check it, connect a phone or computer to the router's Wi-Fi or cable and open a site that shows your IP address. It should show the IP of your proxy server.

If router mode was turned off, turn it on again:

```bash
uci set hiddify-core.main.mode='router'
uci commit hiddify-core
/etc/init.d/hiddify-core restart
```

## If it does not work

- Look at the log: `logread -e hiddify-core`. Errors about the config or the subscription mean the link in step 2 is wrong or can't be downloaded.
- Check that the service runs: `/etc/init.d/hiddify-core status`.
- Restart it: `/etc/init.d/hiddify-core restart`.
- If only the router itself should use the proxy, use proxy mode instead (`option mode 'proxy'`): the proxy then runs at `127.0.0.1:12334` on the router only. See [Router mode and proxy mode](How-to-use-HiddifyCli-on-OpenWrt.md#router-mode-and-proxy-mode).

## Related articles

- [Hiddify Core on OpenWrt](How-to-use-HiddifyCli-on-OpenWrt.md): install, modes and managing the service
- [Hiddify Core](../core/index.md)
- [Router mode on Linux](Router-mode-on-Linux.md)
- [Share your connection](Share-your-connection.md): share the Hiddify app's connection from a phone or computer instead

