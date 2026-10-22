---
title: How to setup Firewall on HiddifyManager
---

<div dir="ltr" markdown="1">

# How to setup Firewall on Hiddify panel

This page explains what a firewall is, how to turn on Hiddify's built-in firewall, and how to open a port by hand when a program that Hiddify does not know about needs one.

## What is a firewall?

A **firewall** is software or hardware that controls which network traffic may reach a computer or server, and blocks the rest. Here we only deal with the software firewall on Linux servers.

<div align=center markdown=1>

![How a firewall works](https://github.com/hiddify/hiddify-config/assets/125398461/2b7c93f0-b868-43c6-8e89-60b36ddb6fb8)

</div>

On Linux, a common firewall tool is **iptables**. You give it a list of rules. Each rule says which traffic (for example, which **port**, a numbered "door" that a service listens on) is allowed through and which is blocked. Hiddify uses iptables.

## The firewall in the Hiddify panel

Hiddify can manage the server's firewall for you. When it is on:

- Only the ports Hiddify needs stay open: SSH (port `22` and the port your SSH server really uses), `80`, `443`, `53`, and every port your enabled proxies use (the same list as the panel's **Public ports** page).
- All other incoming connections are blocked.
- Ping (ICMP) is still allowed, so you can still [test whether your IP is clean](/manager/basic-concepts-and-troubleshooting/How-to-make-sure-the-server%27s-IP-or-domain-is-clean/).
- When you change a port or turn a proxy on or off in the panel, Hiddify updates the rules for you when you apply the changes.

The firewall is **off by default**. We recommend turning it on, because it makes your server harder to attack.

To turn it on:

1. Log in to your Hiddify panel.
2. Open **Settings** → **General Settings**.
3. Turn on **🛡️ Firewall**.
4. Save, and apply the changes when the panel asks you to.

<div align=center markdown=1>

![Firewall setting in the panel (older version)](https://github.com/hiddify/hiddify-config/assets/125398461/0a3dce3a-0658-4ecd-887e-bd74c74fea1a)

</div>

!!! warning "Before you turn it on"
    If you run other programs on the same server that need their own ports (for example another panel or a web server), open those ports by hand first, as shown below. Otherwise they stop working once the firewall is on.

## Open a port by hand

Do this only for programs that Hiddify does not manage. Hiddify opens the ports of its own proxies by itself.

Before you start, connect to your server over **SSH** (a secure way to type commands on a remote server). If you don't know how, see [How to connect to the server via SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/). If the Hiddify menu opens, press `Cancel` (or `Esc`) to close it. If the menu is still on the screen, type `clear` and press Enter.

1. Run this command on your server, over SSH. This example opens TCP port `1234`. Replace `1234` with the port number you need:

    ```bash
    iptables -I INPUT -p tcp --dport 1234 -j ACCEPT
    ```

    If the program uses UDP, run the same command with `-p udp` instead of `-p tcp`. If your server uses IPv6, run the same command again with `ip6tables` instead of `iptables`.

2. Check that the rule was added:

    ```bash
    iptables -L INPUT -n --line-numbers
    ```

    You should see a line with `ACCEPT` and `dpt:1234` (your port).

3. Save the rules so they survive a reboot:

    ```bash
    netfilter-persistent save
    ```

    If the command is not found, install it with `apt install iptables-persistent` and run it again.

## Block ping (optional)

Hiddify's firewall rules always allow ping. Most people should leave it that way, because ping helps you check whether your server is reachable. If you still want to block ping, run this on your server, over SSH:

```bash
iptables -I INPUT -p icmp -j DROP
```

To allow ping again, remove that rule:

```bash
iptables -D INPUT -p icmp -j DROP
```

Remember that online ping tests will fail while ping is blocked. Use a TCP test on port `443` instead.

## Troubleshooting

- **You can't connect over SSH after turning on the firewall:** Hiddify opens port `22` and the port your SSH server is using when the firewall rules are applied. If you changed the SSH port afterwards, apply the panel's configuration again, or log in through your hosting provider's web console and run `hiddify apply`.
- **Another program on the server stopped working:** its port is closed. Open it by hand as shown above.
- **A port you opened by hand is closed again after a reboot:** you did not save the rules. Run `netfilter-persistent save`.

</div>
