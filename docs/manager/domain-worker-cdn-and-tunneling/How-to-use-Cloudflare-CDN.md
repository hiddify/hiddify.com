---
title: How to use Cloudflare CDN
---

<div dir="ltr" markdown="1">


# How to use Cloudflare CDN
Cloudflare is the largest provider of CDN services, which has several services that can be used to bypass Internet restrictions. The most important services are explained below.

## Site or domain service
It means you are using your server behind a CDN provider. In other words, you register your domain (subdomain) with a CDN provider and then proxy it. Here we discuss how to register on cloudflare. If you want to see a tutorial on how to use GCore CDN on a Cloudflare registered domain, see [this link](/manager/wiki/How-to-use-GCore-CDN-on-Cloudflare-registered-domain).

### Direct domain registration purchased on Cloudflare
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



### CDN domain registration in Cloudflare
This domain is registered behind the servers of a CDN provider or so-called proxy.

For example, you can use Cloudflare service. So after following the steps mentioned above; Your domain was activated on the site; You should go to the DNS section and register the desired record. This record is type A for IP version 4 and type AAAA for IP version 6. The only difference with the previous step is that you must turn on the proxy.

![PICTURE](https://user-images.githubusercontent.com/125398461/234167748-7121af19-f624-4659-9922-50f8e6d3ea2c.png)


### How to verify CDN domain registration
When you test this domain using various tools such as ping, nslookup, dig; In response, one of the IPs randomly assigned by Cloudflare will return to your domain and there is no more information about your IP. This provides a level of security for your server.

It should be noted that this IP changes in different periods of time and is not fixed.
Sometimes it happens that the IP assigned by Cloudflare is blocked or disrupted in Iran, and in this regard, methods to bypass this type of filtering should be used.

## Certificate settings of CDN domain  
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

## Worker service
To see details about this service, read [this article](/manager/wiki/How-to-set-up-and-use-Cloudflare-workers).

## Domain fronting service
To see details about this service, read [this article](/manager/wiki/Guide-for-domain-fronting).

This service is currently disabled in Cloudflare.



## gRPC service
This service was introduced by Google in 2015 and is based on `TLS` and `HTTP/2`, and because its packet size is smaller, it requires less bandwidth and is therefore faster. This service is also active in Cloudflare and is compatible with many of its other services. Therefore, you can activate it on the domain service and use this feature to bypass filtering.

- To do this, go to the `Network` section and then enable the `gRPC` option.

![](https://user-images.githubusercontent.com/125398461/223042141-c2456322-7cac-44be-be9c-044a307eeb52.png)

After that, it is possible to send `gRPC` packets from the client to Cloudflare. After the packets reach Cloudflare, they are forwarded to the original destination, which is your server.

## WebSocket wervice
Another cloudflare service is `WebSocket`, which allows stable communication between the client and the main server. In this case, the client and server can exchange information without the need to re-establish communication and have a stable connection. This service can also be used to bypass filtering.

- For this, go to the `Network` section and then activate the `WebSockets` option.

![](https://user-images.githubusercontent.com/125398461/223042141-c2456322-7cac-44be-be9c-044a307eeb52.png)

After that, it is possible to send `WebSocket` packets from the client to Cloudflare. After the packets reach Cloudflare, they are forwarded to the original destination, which is your server.


## QUIC service
This service is based on HTTP/3 and works with TLS1.3. That's why it's so fast because its handshake is much faster than TCP.

<div align=center markdown=1>
<img width="60%" alt="http-request-over-quic" src="https://github.com/hiddify/hiddify-config/assets/125398461/5793c28e-7785-4ea5-998d-9695cc11b341" />

</div>

- For this, go to the `Network` section and then activate the `HTTP/3 (with QUIC)` option.

![QUIC](https://user-images.githubusercontent.com/125398461/223041843-7b441805-4aab-4547-b318-7dbbda4cc893.png)