---
title: Troubleshooting connectivity issues with HiddifyManager and proxies
---

# Troubleshooting connectivity issues with HiddifyManager and proxies
Why don't my connections connect even though HiddifyManager is installed?

Or, what is the story behind this that it connects with One ISP but does not connect with other one, for example?

Follow this article to the end to answer these questions.


As mentioned in the preliminaries of HiddifyManager configuration installation, there are several reasons for this issue:

> 1. IP or domain is blocked.
> 2. The IP is semi-blocked and placed in the yellow list. For example, it is connected in some ISPs and not in others.
> 3. If a CDN domain is used, the Cloudflare IP is not selected.
>

Therefore, this panel is not going to work miracles. It requires preliminary installation. Before configuring the panel, make sure your IP or domain is clean. [How to test](/manager/basic-concepts-and-troubleshooting/How-to-make-sure-the-server%27s-IP-or-domain-is-clean/)


If a CDN domain is used, you need to find [Cloudflare Clean IP](/manager/domain-worker-cdn-and-tunneling/Guide-for-finding-a-clean-Cloudflare-IP/) and in the mandatory field Enter the domain in the domains menu.


If you have been able to connect from another device, on the same server and the same domain, immediately send us the link of the Trojan or Wi-Las or Wi-Mes so that we can add it to the panel.




# Ways to solve the problem
- Find a healthy IP
- Use a new domain
- You can use CDN
- [You can use Relay](/fa/manager/domain-worker-cdn-and-tunneling/How-to-add-relay-domain-to-Hiddify-manager/)
- Use the Fake domain


# Related content link for this solution

> [1. How to make sure the server's IP or domain is clean](/manager/basic-concepts-and-troubleshooting/How-to-make-sure-the-server%27s-IP-or-domain-is-clean/)
> [2. How to find a clean Cloudflare IP](/fa/manager/domain-worker-cdn-and-tunneling/Guide-for-finding-a-clean-Cloudflare-IP/)
  > [3. Domain types and how to register them](/fa/manager/domain-worker-cdn-and-tunneling/Domain-types-and-how-to-register-them/)
