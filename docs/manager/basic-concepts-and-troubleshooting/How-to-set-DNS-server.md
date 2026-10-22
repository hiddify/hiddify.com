---
title: How to set DNS server on HiddifyManager
---

<div dir="ltr" markdown="1">

# How to set DNS server

This page shows you how to choose the DNS server that your Hiddify server uses, and how to check that DNS works. You need it if sites don't open through your proxy, or if a DNS leak test shows the wrong DNS servers.

**DNS** (Domain Name System) turns names into IP addresses. For example, when you open `google.com`, your device first asks a DNS server "what is the IP of google.com?". The DNS server answers with the IP address, and only then does your device connect to the site.

<div align=center markdown=1>
  
<img width=50% src="https://github.com/hiddify/hiddify-config/assets/125398461/8b1ce774-3268-4c42-ae0a-02553feb3b26" alt="How a DNS request turns a name into an IP address" />
</div>

Your server needs a working, trusted DNS server, just like your phone or computer.

## Well-known public DNS servers

Big companies run free DNS servers that work worldwide. These are good choices for your server:

| Address | Provider |
|---|---|
| `1.1.1.1` | Cloudflare |
| `8.8.8.8` | Google |

## Symptoms of a DNS problem on the server

- Sites don't open through the proxy, or open very slowly, while the connection itself works.
- The installer or an update shows the warning `DNS is not working.`
- A [DNS leak test](/manager/basic-concepts-and-troubleshooting/How-to-check-and-prevent-DNS-leaks/) shows DNS servers you didn't choose.

The fix is one or both of the methods below.

## Method 1: set the DNS server in the panel

The panel's **DNS Server** setting is the DNS server that Hiddify's proxy service uses to look up sites for your users. The default is `1.1.1.1` (Cloudflare).

1. Log in to your Hiddify admin panel.
2. Open **Settings**.
3. In the search box (**Search all settings…**), type `DNS Server`. The setting is in the **General Settings** section, among the advanced settings.
4. Enter the DNS server you want, for example `1.1.1.1` or `8.8.8.8`. The description under the field also suggests `1.1.1.2` (blocks malware) and `1.1.1.3` (blocks malware and adult content).
5. Click **Save**.
6. When the panel asks, click **Apply Configs** so the change takes effect.

<div align=center markdown=1>
  
<img src="https://github.com/hiddify/hiddify-config/assets/125398461/1145521a-cfd2-492b-99d0-83559c20ab15" alt="The DNS Server field in the panel settings (older panel version; the new panel looks different)" />
</div>

## Method 2: set the server's own DNS over SSH

The server's operating system also uses a DNS server, for example to download updates. On Ubuntu, Hiddify uses the `systemd-resolved` service for this. If the server's DNS doesn't work, set it with the script that comes with Hiddify (the installer uses the same script).

1. [Connect to your server over SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/). If the Hiddify menu opens, press `Ctrl+C` to leave it.
2. Run this command on your server. It sets the DNS servers to `8.8.8.8` and `1.1.1.1`:

    ```bash
    sudo /opt/hiddify-manager/scripts/common/change_dns.py 8.8.8.8 1.1.1.1
    ```

3. When it finishes, the last line should say `DNS servers set to 8.8.8.8 and 1.1.1.1`.

!!! warning "Don't delete or lock `/etc/resolv.conf`"
    Older guides told you to delete `/etc/resolv.conf`, write it by hand, and lock it with `chattr +i`. Don't do this on a current Hiddify server. On Ubuntu this file is managed by `systemd-resolved`, and locking it can stop Hiddify's installer from repairing DNS. If you locked it before, unlock it with `sudo chattr -i /etc/resolv.conf`.

## Check DNS on the server

Run these commands on your server, over SSH.

1. Check which DNS servers the system uses:

    ```bash
    resolvectl status
    ```

    Look for the line **DNS Servers**. It should list only the servers you chose, for example `8.8.8.8 1.1.1.1`.

2. Check that a name can be resolved:

    ```bash
    nslookup google.com
    ```

    If it works, you see one or more `Address:` lines with Google's IP addresses. The `Server:` line may show `127.0.0.53`. That is normal: it is the local `systemd-resolved` service, which forwards the request to the servers from step 1. If you see an error such as `connection timed out` or `server can't find`, DNS doesn't work: repeat Method 2.

    (If `nslookup` is missing, install it with `sudo apt install dnsutils`.)

<div align=center markdown=1>
  
![Example output of nslookup google.com](https://user-images.githubusercontent.com/125398461/248440247-3ef15d0b-54b0-43ce-8be5-a5229054d1fb.png)
</div>

[Learn more about DNS leaks](/manager/basic-concepts-and-troubleshooting/How-to-check-and-prevent-DNS-leaks/)

</div>
