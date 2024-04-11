---
title: How to manage multiCDN domains in HiddifyManager
---

<div dir="ltr" markdown="1">
  
# How to manage multiple CDN domains in HiFiManager

When we have several domains, especially the CDN domain, and our users are also on different mobile networks; Irancell; Telecommunications and... are; How can you manage them better and make better configurations by using the capabilities of the HiddifyManager?

## The first proposed method
It is recommended for this
Define several different CDN subdomains for your panel in Cloudflare. Note that the proxy tick must be enabled. [How to define a domain](/manager/domain-worker-cdn-and-tunneling/Domain-types-and-how-to-register-them/)

For example:

sub1.domain.com (proxy on)

sub2.doamin.com (proxy on)

sub3.domain.com (proxy on)


After that, we find the clean IPs of Cloudflare in different networks. that is, on the client that is connected to the first mobile network; We find the clean IP of Cloudflare. If you are not familiar with the method of finding clean IP; [here](/manager/domain-worker-cdn-and-tunneling/Guide-for-finding-a-clean-Cloudflare-IP/).
  for Irancell; We continue in the same way with telecommunications and... Finally, you have a few clean cloudflare IPs for each operator.

Now again for the IPs found; We create a normal subdomain. It means that the proxy tick is off.

For example:

mci.domain.com (proxy off) ==> Cloudflare's clean IP on the first mobile network

irc.domain.com (proxy off) ==> Cloudflare's clean IP in Irancell network

mkb.domain.com (proxy off) ==> Cloudflare's clean IP in the telecommunications network


Finally, go to the domains menu in the HiddifyManager. Create a domain for each of the registered records.

Very important point:

- You can remove other CDN domains from the list in the **show domain configurations** field. In this case, the configurations of the same domain are only displayed. It makes registered clean ip work properly.



## The second proposed method

In this method, we need 2 domains. We use the first domain according to the previous method, that is, define several different CDN subdomains for your panel in Cloudflare. Note that the proxy tick must be enabled. [How to define a domain] (/manager/domain-worker-cdn-and-tunneling/Domain-types-and-how-to-register-them/)

For example:

sub1.domain1.com (proxy on)

sub2.doamin1.com (proxy on)

sub3.domain1.com (proxy on)


Then proceed in the same way as above for clean IPs. For example:

mci.domain1.com (proxy off) ==> Cloudflare's clean IP on the first mobile network

irc.domain1.com (proxy off) ==> Cloudflare's clean IP in Irancell network

mkb.domain1.com (proxy off) ==> Cloudflare's clean IP in the telecommunications network


Finally, here we have a difference from the previous method. We define a cname record for each record of the first domain using the second domain. This is to prevent the first domain and subdomains from being leaked and filtered. That is, for example:

sub1.domain2.com ==> sub1.domain1.com (proxy off)

sub2.domain2.com ==> sub2.domain1.com (proxy off)

sub3.domain2.com ==> sub3.domain1.com (proxy off)

mci.domain2.com ==> mci.domain1.com (proxy off)

irc.domain2.com ==> irc.domain1.com (proxy off)

mkb.domain2.com ==> mkb.domain1.com (proxy off)

Finally, go to the domains menu in the Hidify panel. Create a domain for each of the registered records.

For example, for **MCI**

Domain: sub1.domain2.com

Type: CDN

Force CDN host: mci.domain2.com


or for Irancell

Domain: sub2.domain2.com

Type: CDN

Force CDN host: irc.domain2.com


or for **communication network**

Domain: sub3.domain2.com

Type: CDN

Force CDN host: mkb.domain2.com

**very important point:**

- You can remove other CDN domains from the list in the domain configuration display field. In this case, the configurations of the same domain are only displayed. It makes registered clean ip work properly.

**And note:**

- All these methods are innovative solutions and you can

## The third proposed method
For this case, you can use the AutoCDN domain feature. That is, create a subdomain with proxy enabled in Clafler. Like this: sub.domain.com (proxy on) then set the domain mode to AutoCDN. In the Force to use the following IPs field, enter the tags related to your desired networks from the suggested template. For example: mci.ircf.space MCI mtn.ircf.space MTN mkh.ircf.space MKH rtl.ircf.space RTL and then save the settings. Read this article to better understand how to use this template.

Finally, with this method, you will have an AutoCDN domain to use on several different networks.
