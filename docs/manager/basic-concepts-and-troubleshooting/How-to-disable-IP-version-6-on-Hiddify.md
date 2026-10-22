---
title: How to disable IP version 6 on HiddifyManager
---

<div dir="ltr" markdown="1">

# How to disable IP version 6 on Hiddify

This page shows you how to turn off IPv6 on your Hiddify server. You need it when IPv6 causes problems, for example when Google shows errors to your users.

## What is IPv6?

**IPv6** (IP version 6) is the newer kind of IP address that came after IPv4. An IPv6 address is 128 bits long. It is written as 8 groups of 4 **hexadecimal** characters (digits `0`–`9` and letters `a`–`f`), separated by `:`. For example:

`2001:0db8:85a3:0000:0000:8a2e:0370:7334`

Because there are so many IPv6 addresses, they are harder to block than IPv4 addresses. Still, sometimes you need to turn IPv6 off.

## When should you turn off IPv6?

- **Symptom:** your users see Google errors (for example **403** or "unusual traffic") or some sites don't open, while other sites work.
- **Likely cause:** the server's IPv6 address is blocked or flagged by that site, or IPv6 doesn't work properly at your server provider.
- **Fix:** turn off IPv6 so the server uses only IPv4. Use Method 1 (the panel) first. Use Method 2 only if you can't use the panel.

## Method 1: in the panel

1. Log in to your Hiddify admin panel.
2. Open **Settings**.
3. In the search box (**Search all settings…**), type `IPv4`. The setting **Only IPv4** is in the **General Settings** section, among the advanced settings.
4. Turn **Only IPv4** on.
5. Click **Save**.
6. When the panel asks, click **Apply Configs** so the change takes effect.

When this option is on, Hiddify turns off IPv6 on the server's network interfaces and stops adding IPv6 addresses to your users' configs.

<div align=center markdown=1>
  
<img src="https://github.com/hiddify/hiddify-config/assets/125398461/6f2d4977-6e79-4849-9d10-0c765051306c" alt="The Only IPv4 option in the panel settings (older panel version; the new panel looks different)" />
</div>

## Method 2: over SSH

Use this method only if you need to turn IPv6 off for the whole operating system.

1. [Connect to your server over SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/). If the Hiddify menu opens, press `Ctrl+C` to leave it.
2. Open the system settings file in the **nano** text editor:

    ```bash
    sudo nano /etc/sysctl.conf
    ```

3. Go to the end of the file and add these three lines:

    ```ini
    net.ipv6.conf.all.disable_ipv6=1
    net.ipv6.conf.default.disable_ipv6=1
    net.ipv6.conf.lo.disable_ipv6=1
    ```

4. Press `Ctrl+S` to save and `Ctrl+X` to exit.
5. Load the new settings:

    ```bash
    sudo sysctl -p
    ```

    The command prints the three lines you added. If you see an error, open the file again and check for typos.

IPv6 is now off, and the server works only with IPv4. Hiddify detects this and also treats the server as IPv4-only.

To turn IPv6 back on later, delete the three lines, run `sudo sysctl -p` again, and restart the server.

</div>
