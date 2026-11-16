---
title: How to use AutoCDN IP domain
---

<div dir="ltr" markdown="1">


# How to use AutoCDN IP domain
One of the constant concerns of Cloudflare CDN users is finding clean IPs, and a clean IP that works on one operator often does not work on another. The AutoCDN IP feature solves this: you give the panel a list of clean IPs (or host names) per operator, and each user gets, in their configs, the IP for **their own** operator.

!!! info "Since v13 there is no separate auto_cdn_ip mode"
    In older versions this was a domain mode called `auto_cdn_ip`. Since v13 it is part of the normal **CDN** domain: the field **Force configs to use these IPs / domains**. This page is for Hiddify Manager v14.5.

One big advantage: if the hostname you list the IPs with is itself blocked (for example `ircf.space`), a user with a normal CDN config cannot resolve it and cannot connect; here the panel resolves it itself and puts the IP in the config.

## Domain registration
1. Register your subdomain on Cloudflare with the proxy turned on (orange cloud). See [Domain types and how to register them](/manager/domain-worker-cdn-and-tunneling/Domain-types-and-how-to-register-them/).
2. In the panel, open **Domains**, click **Add domain**, type the subdomain and click **Check**.
3. Choose **CDN** and **Valid TLS**, then finish the wizard. Give it a **Display name** if you like: it is shown in the users' apps instead of the domain.
4. Click the pencil next to the domain and open **Advanced**. The field **Force configs to use these IPs / domains** is there (see below).
5. Save, then click **Apply now** on the **Actions** page.

More about the CDN domain and its other fields: [CDN domain](/manager/configuration-and-advanced-settings/How-to-configure-Hiddify-panel-properly/#cdn-domain).

## Force configs to use these IPs / domains
Whatever you put here goes into the users' links instead of the domain's own IP. You can write:

- **One or more IPs or host names**, separated by commas or new lines: everyone gets them.
- **Per operator:** an IP, a range (CIDR) or a host name, then the operator's code, for example `1.1.1.1 MCI`. Each user gets the address of their operator. Addresses with no code are for every other operator.

For example, the list of clean-IP host names kept up to date by `ircf.space` (paste the lines of the operators you need):

```
mci.ircf.space MCI
mcix.ircf.space MCI
mtn.ircf.space MTN
mtnx.ircf.space MTN
mkh.ircf.space MKH
rtl.ircf.space RTL
hwb.ircf.space HWB
ast.ircf.space AST
sht.ircf.space SHT
prs.ircf.space PRS
mbt.ircf.space MBT
ask.ircf.space ASK
rsp.ircf.space RSP
afn.ircf.space AFN
ztl.ircf.space ZTL
psm.ircf.space PSM
arx.ircf.space ARX
smt.ircf.space SMT
```

Or your own records (DNS only, proxy off), or IPs:

```
mci.yourdomain.com MCI
mtn.yourdomain.com MTN
1.1.1.1 MKH
```

If the field is empty, the configs use the domain itself.

!!! tip "Find clean IPs with the panel's scanner"
    Under the field, **Open the scanner** opens the panel's **Scanner** (Tools › Scanner). It scans Cloudflare IPs on your own internet and saves the best ones in this field, per operator. See also [Guide for finding a clean Cloudflare IP](/manager/domain-worker-cdn-and-tunneling/Guide-for-finding-a-clean-Cloudflare-IP/).

<b><i>Key point: the panel picks the operator from the IP the user updates their subscription from. So update the subscription in the app with the VPN disconnected; after changing operator (for example from Wi-Fi to mobile data), disconnect the VPN and update the subscription again.</i></b>

## Show Configs of Domains
**Show configs of** (in the same dialog) limits which domains' configs users see when they open their page on this domain. For non-commercial use you usually do not need it.

The work is done. Now you can go to the user link and view the configurations related to this domain.

## Related articles

- [What is a CDN and how does it help?](/manager/domain-worker-cdn-and-tunneling/What-is-CDN-and-how-does-it-help-us%3F/)
- [Cloudflare CDN](/manager/domain-worker-cdn-and-tunneling/How-to-use-Cloudflare-CDN/)
- [GCore CDN](/manager/domain-worker-cdn-and-tunneling/How-to-use-GCore-CDN-on-Cloudflare-registered-domain/)
- [Amazon CDN (CloudFront)](/manager/domain-worker-cdn-and-tunneling/How-to-use-Amazon-CDN/)

</div>
