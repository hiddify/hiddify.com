---
title: How to add relay domain to Hiddify manager
---

<div dir="ltr" markdown="1">

# Domain types

## Direct domain
It means you want to use your server directly (for normal use). In fact, this domain name (subdomain) directly points to the IP address of the server. That is, if you ping it, the IP of the server will be answered.

## CDN domain
It means you are using your server behind a CDN provider. In other words, you register your domain (subdomain) with a CDN provider and then proxy it. Here we discuss how to register on cloudflare. If you want to see a tutorial on how to use GCore CDN on a Cloudflare registered domain, see [this link](/manager/wiki/How-to-use-GCore-CDN-on-Cloudflare-registered-domain).

## Relay domain
This domain is used when you want to use intermediate servers to send user traffic. For example, you have a server in Iran and you have registered a domain (subdomain) for it. You can register this domain in this section so that the relevant settings are applied in the configurations. [More information](https://github.com/hiddify/hiddify-config/discussions/129)

## Fake domain
This domain is used to use the [Header trick](https://github.com/iranxray/hope/blob/main/cloudflare-cdn.md#%D8%B1%D9%88%D8%B4-%D8%A7%D9%88%D9%84-%D8%AD%D9%82%D9%87-%D9%BE%D8%B1%D9%88%DA%A9%D8%B3%DB%8C). A fake domain is used to bypass the SNI whitelist proxy. In this case, you can see the configurations related to this trick by defining this domain. If you use this trick, there is a possibility that the server will be filtered.

# How to register a domain
Now that we are familiar with the types of domains, how to register these domains will be checked

<details><summary><h2>Direct domain registration</h2></summary>
You can register the direct domain in several ways. 

### Direct domain registration for free
Using sites that offer free subdomains: [afarid](https://freedns.afraid.org/) is recommended.
A number of public domains have already been registered on this site. You can register your desired subdomain on these domains.
For this, you must first create a profile from [here](https://freedns.afraid.org/signup/?plan=starter). A real email is required.

![](https://user-images.githubusercontent.com/125398461/221342760-12dc14ed-9a19-45f3-a3f1-bf7d3f969792.png)

After that, the list of domains registered on this site can be seen from [here](http://freedns.afraid.org/domain/registry/). You can choose one of the domains that has fewer hosts. Note that the domain must be public. It is recommended to use `.com`, `.org`, `.net` domains.

![221343189-1fe98d0d-7f05-4639-9b51-fb6926f76f2b2](https://user-images.githubusercontent.com/125398461/234033584-1c26c485-6ceb-4aa9-a6b6-c1b781e767d1.png)

### Register the purchased direct domain
After buying the domain, you can use the sites that provide DNS services. e.g. Cloudflare

#### Direct domain registration purchased on Cloudflare
First, you register using [this link](https://dash.cloudflare.com/signup).

![](https://user-images.githubusercontent.com/125398461/221563866-d520a39d-15c8-4f88-a756-90e5e08c074a.png)


Log in after creating a profile. You must add your domain here. For this, click on `Add Site` button and add your domain.



![PICTURE](https://user-images.githubusercontent.com/125398461/221566504-5ecf714b-940d-4fd5-bc54-be8c37b7c292.png)

In the next step, choose your desired plan. The free plan is enough for this. So you choose according to the photo.

![PICTURE](https://user-images.githubusercontent.com/125398461/221567803-26850724-1bc8-480a-8c6f-29b32a6fcfa6.png)

In the next step, we do next according to the figure.

![PICTURE](https://user-images.githubusercontent.com/125398461/222444475-5596de54-3e7f-4fae-a0f0-94c046a21969.png)

In the last step, put the given DNS servers in your domain settings.

![PICTURE](https://user-images.githubusercontent.com/125398461/221569269-1f4027c7-5815-4dea-876e-326dc0645fe1.png)

Wait a while to register the domain settings. After that, the domain will be activated on the Cloudflare server.

![PICTURE](https://user-images.githubusercontent.com/125398461/221572305-50e819ea-0fa4-4548-8851-aab91b797f57.png)

Now you need to go to the registration section of DNS records.

![PICTURE](https://user-images.githubusercontent.com/125398461/222436778-f80de97b-7d66-4621-8be3-b856fc4e2c75.png)

In this case, to record records related to IP version 4, follow the figure.

![PICTURE](https://user-images.githubusercontent.com/125398461/222444012-2fa4a2c2-ff89-493e-b92c-01a26d7788b7.png)

After clicking on Add record, register the details of the desired subdomain by entering the server IP. Note that the proxy must be turned off for the direct domain.

![PICTURE](https://user-images.githubusercontent.com/125398461/234167251-ceebd61b-5147-4198-98dc-1c5bcd0d9124.png)


If needed, you can change the TTL from automatic mode. The lower this value is; DNS records cached on the user's system are refreshed sooner.

To record the records related to IP version 6 of the server, follow the figure.

![PICTURE](https://user-images.githubusercontent.com/125398461/234167507-996c8480-5cf5-4ede-999f-05f74b22499f.png)


All the things mentioned about IP version 4 also apply in this case. The only difference is the record type, which is AAAA.

#### How to  direct domain registration
The easiest test to ensure domain registration is to use the ping command. Thus, in a terminal, if the desired domain is pinged, the above registered IP must appear in the response. Usually, the DNS record registration process takes some time. More advanced tools such as nslookup and dig can also be used for this test. If you need more information, you can read [this article](https://wikicensorship.github.io/fa/docs/measure-internet-censorship/DNS/).

</details>

<details><summary><h2>CDN domain registration</h2></summary>
This domain is registered behind the servers of a CDN provider or so-called proxy. For this, the services of one of these sites should be used.
### CDN domain registration in Cloudflare
For example, you can use Cloudflare service. So after following the steps mentioned above; Your domain was activated on the site; You should go to the DNS section and register the desired record. This record is type A for IP version 4 and type AAAA for IP version 6. The only difference with the previous step is that you must turn on the proxy.

![PICTURE](https://user-images.githubusercontent.com/125398461/234167748-7121af19-f624-4659-9922-50f8e6d3ea2c.png)


### How to verify CDN domain registration
When you test this domain using various tools such as ping, nslookup, dig; In response, one of the IPs randomly assigned by Cloudflare will return to your domain and there is no more information about your IP. This provides a level of security for your server.

It should be noted that this IP changes in different periods of time and is not fixed.
Sometimes it happens that the IP assigned by Cloudflare is blocked or disrupted in Iran, and in this regard, methods to bypass this type of filtering should be used.

### Certificate settings of CDN domain  
TLS is an algorithm that encrypts all internet traffic and helps the user stay safe online.

to describe precisely; TLS encrypts the communication between the client and the server in the web platform, which uses a set of cryptographic algorithms such as alpn, uTLS, allowInsecure.

Certificates assigned to domains are also based on the TLS protocol.

To do this, go to the SSL/TLS section on the Cloudflare site and set the certificate mode to Full.

![PICTURE](https://user-images.githubusercontent.com/125398461/234168806-26bb12cf-78ad-45a9-89b5-c2f005a9fb86.png)


Also, activate the SSL/TLS Recommender option to increase connection security. This option checks the connection and gives you security suggestions if it is possible to upgrade the TLS version.

Then go to the Network menu. Here you should check that QUIC, gRPC and WebSockets options are enabled.

![PICTURE](https://user-images.githubusercontent.com/125398461/223041843-7b441805-4aab-4547-b318-7dbbda4cc893.png)

![PICTURE](https://user-images.githubusercontent.com/125398461/223042286-e597f169-001e-40a5-b0e8-d34d1b110eab.png)

Checking security status of CDN domain traffic
To do this, go to the SSL/TLS section of the Cloudflare site. A graph is displayed for passing traffic, the more traffic passed based on the higher version TLS; Communication security has been higher. http traffic passes without using TLS encryption.

![PICTURE](https://user-images.githubusercontent.com/125398461/223042939-897b7ec0-9700-4bec-8e28-6d8f961657b6.png)

</details>

## Relay domain registration
In fact, it is a direct domain that is considered for intermediate servers, and therefore the way to register such domains is the same as the direct domain.


## Fake domain registration
As the name suggests, we want to use a fake domain that is not related to us, so we don't need to register it in advance. But we can only use it in the panel. Click [here](https://github.com/hiddify/Hiddify-Manager/wiki/How-to-create-and-use-fake-domain) to see the article on registering and using fake domains.
