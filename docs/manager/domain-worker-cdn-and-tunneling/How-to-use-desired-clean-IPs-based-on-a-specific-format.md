---
title: Insert the desired clean IPs based on the specified format (for the forced to use host field)
---

# Insert the desired clean IPs based on the specified format (for the forced to use host field)
As you probably know, one of new features of HiddifyManager is AutoCDN which depends on the subdomains of Cloudflare's clean IPs collected by IRCF. To use it, you must use a suitable format. How to use this format?

Also, what if you want to use your clean IP range for different operators?

To do this, first go to [here](https://ip-format.hiddify.com/).

Here you will enter the IRCF domain name format page. Choose the domains you want based on your needs and delete the domains you don't need.

<div align=center>

<img alt="ip-format site" src="https://github.com/hiddify/hiddify.com/assets/125398461/e15b0d7f-8f46-47aa-b0fc-703754fbf088" />
</div>


- Use the trash can icon to delete the networks you don't need.
- Change the IP or domain of your networks if needed. For example, it works better for you than `mcix.ircf.space`; Put this subdomain for MCI network.
- Also, if you want to enter your clean IP range for each operator, just enter the IP or subdomains in the fields on the right. Select the tag related to the operator.
- Finally, click on `Copy IPs` to copy the final format.
- Place the copied template in the `Force the use of the following IPs` field in the settings related to your domain in the Hidify panel.
- The work is done.
