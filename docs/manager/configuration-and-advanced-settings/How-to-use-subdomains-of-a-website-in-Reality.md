---
title: How to use subdomains of a website in Reality
weight: -60
---

<div dir="ltr" markdown="1">


# How to use subdomains of a website in Reality

This page shows you how to spread your Reality traffic over many subdomains of one website. A **subdomain** is a name under a main domain, for example `blog.yahoo.com` under `yahoo.com`. When your traffic uses many names instead of one, it is harder for the filtering system to notice your server.

## Before you start
- You already have a Reality domain in your panel. If not, first follow [How to use Reality on HiddifyManager](/manager/configuration-and-advanced-settings/How-to-use-Reality-on-Hiddify/).

## Steps
1. Find the subdomains of the website you use for Reality. You can use [subdomainfinder.c99.nl](https://subdomainfinder.c99.nl/): search for the website's name. For example, here are [all the subdomains of speedtest.net](https://subdomainfinder.c99.nl/scans/2023-11-20/speedtest.net).

    ![List of speedtest.net subdomains on subdomainfinder.c99.nl](https://github.com/hiddify/Hiddify-Manager/assets/125398461/968b94b3-1899-43b2-a45a-19e71379ad17)

    You can also use [crt.sh](https://crt.sh/). For example, here are [the subdomains of mozilla.org](https://crt.sh/?q=mozilla.org), the Firefox website.

    ![List of mozilla.org subdomains on crt.sh](https://github.com/hiddify/Hiddify-Manager/assets/125398461/234710c2-dec4-436e-a478-c3bb2b0d2de7)

2. In the panel's sidebar, under **Settings**, click **Domains** and open your Reality domain.
3. In the **Server names** field, enter the subdomains, separated by commas. For example: `sub1.example.com,sub2.example.com,sub3.example.com`. Use only subdomains that really open as websites.
4. Click **Save**, then apply the changes (in **Settings** → **Actions**, click **Apply now**).

## What happens next
Each time a user's subscription link updates, one of these subdomains is chosen as the address. This splits the traffic over the subdomains. For example, if a user's app updates the subscription every hour, it uses a different subdomain each hour. This makes it less likely that the filtering system detects your server.

</div>
