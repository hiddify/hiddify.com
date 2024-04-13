---
title: How to add a relay server (domain) to HiddifyManager
---


# How to add a relay server (domain) to HiddifyManager
Let's assume that you have set up your middle server using one of the following methods or any other method.

1. [Setting up a relay server using Hiddify Relay Builder](/manager/domain-worker-cdn-and-tunneling/How-to-setup-relay-server-using-Hiddify-Relay-Builder/)
2. [Setting up a relay server using the IP-Tables method](/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-IP-Tables-tunnel-as-relay-server/)
3. [Setting up a relay server using the GOST method](/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-GOST-tunnel-as-relay-server/)
4. [Setting up a relay server using the WST method](/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-WST-tunnel-as-relay-server/)
5. [Setting up a relay server using the Dokodemo-door method](/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-Dokodemo-door-tunnel-as-relay-server/)
6. [Setting up a relay server using the HA-Proxy method](/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-HA-Proxy-tunnel-as-relay-server/)

To add that server to HiFi Manager and use its configurations, just follow the steps below.

## Adding Relay server to HiddifyManager
Now, register a subdomain with the proxy off for your relay server IP and register it in Hiddify Manager on `Relay` mode.
- Put the registered subdomain in the `Domain` field and you can also set a `Alias` to display in the configurations.

<img src="https://github.com/hiddify/hiddify.com/assets/125398461/4c0ade4e-394c-4d52-8067-f15d1778c9ed">

## Adding `Relay` configurations to subscription link

As always in HiddifyManager, it is better to separate the configs from the subscription link. Therefore, for the registered `Relay` domain, you can check the `Relay` domain in the subscription domain settings so that its configurations are added to the subscription domain.

Assuming that the subscription domain is `sublink.hiddify.com`, proceed as shown below to get the job done.

<img src="https://github.com/hiddify/hiddify.com/assets/125398461/3661045d-ced7-4694-916f-6ef160c63230">

Now, if you open the user page with the subscription domain (here `sublink.hiddify.com`), you will see that the connections related to the `relay server` have also been added. You can add and use these connections individually or using subscription links to your client.
