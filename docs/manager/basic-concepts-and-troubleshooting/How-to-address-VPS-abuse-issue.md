---
title: How to address VPS abuse issue
---

<div dir="ltr" markdown="1">

# How to fix abuse reports on your VPS

This page helps you if your server provider (datacenter) has sent you an **abuse report** about your Hiddify server. It explains the usual causes, what to check, and how to stop new reports.

An **abuse report** is a warning from your provider saying that traffic from your server looks harmful, for example like a network scan or an attack. If the reports continue, the provider can suspend your server or your account.

## Symptom

- You receive an email from your provider with words like "abuse", "netscan", "port scan" or "suspicious traffic".
- Your server is suddenly suspended or its network is limited.

## Likely causes

1. **Your server sends traffic to private or reserved IP ranges.** Addresses such as `10.0.0.0/8`, `172.16.0.0/12` and `192.168.0.0/16` belong to local networks and should never be reached over the internet. When your users' devices (or apps on them) try to reach these addresses through your proxy, the traffic leaves your server and the provider sees it as a network scan.
2. **IP addresses are used directly in the "Force IPs" field.** Users have reported abuse reports after they put Cloudflare clean IPs, the server's IPv6 address, or relay server IPs directly in the domain field **Force configs to use these IPs / domains**.

## What to check

1. Read the abuse email. Note the destination IPs or IP ranges it lists.
2. In the Hiddify panel, open **Domains**, open each domain, and look at **Advanced → Force configs to use these IPs / domains**. Note any raw IP addresses there.

## How to fix it

### Fix 1: Put forced IPs behind subdomains

Instead of raw IPs in the Force field, use subdomains:

1. In your DNS provider (for example Cloudflare), create a subdomain for each IP, such as `ip1.example.com` pointing to the IP.
2. In the Hiddify panel, replace each raw IP in **Force configs to use these IPs / domains** with its subdomain.
3. Click **Save** and apply the changes.
4. If you use Cloudflare, check that the SSL/TLS settings of your domain are set up correctly.

### Fix 2: Block outgoing traffic to abuse-prone ranges with Abuse Defender

**Abuse Defender** is a free script that adds firewall rules to stop your server from sending traffic to private and reserved IP ranges and to some other ranges known to cause abuse reports. You can also block or allow ranges by hand.

!!! note
    Abuse Defender is a third-party script by [Kiya6955](https://github.com/Kiya6955/Abuse-Defender). It is not made or maintained by Hiddify. Read it first if you want to know exactly what it changes.

1. Connect to your server over SSH. If you are not logged in as `root`, switch to root:

    ```bash
    sudo -i
    ```

2. Run the script **on your server**:

    ```bash
    bash <(curl -s https://raw.githubusercontent.com/Kiya6955/Abuse-Defender/main/abuse-defender.sh)
    ```

3. A menu appears. Type `1` (**Block Abuse IP-Ranges**) and press **Enter**.
4. If the server asks whether to save the current IPv4 and IPv6 rules (this happens only if the `iptables-persistent` package is being installed), choose **Yes** both times.
5. Answer the script's questions:
    - "Are you sure about blocking abuse IP-Ranges?": type `y`.
    - "Do you want to delete the previous rules?": type `y`.
    - "Do you want to enable Auto-Update every 24 hours?": type `y` to keep the list up to date.

    **It worked if** you see `Abuse IP-Ranges blocked successfully.`

6. Press **Enter** to return to the menu, then type `6` to exit.

You can run the same command again at any time to open the menu. Its options are:

| Option | What it does |
|---|---|
| 1 | Block the abuse IP ranges |
| 2 | Allow (whitelist) an IP or range by hand |
| 3 | Block an IP or range by hand |
| 4 | Show the rules the script added |
| 5 | Remove all rules the script added |
| 6 | Exit |

If a service you need stops working after this, use option 4 to see the rules and option 2 or 5 to undo them.

## If you still get reports

Reply to your provider's abuse email, explain what you changed, and ask which traffic caused the report. Also make sure your server itself is secure: [turn off SSH password login](/manager/basic-concepts-and-troubleshooting/Disable-SSH-Password-Authentication/), because a hacked server is another common cause of abuse reports.

</div>
