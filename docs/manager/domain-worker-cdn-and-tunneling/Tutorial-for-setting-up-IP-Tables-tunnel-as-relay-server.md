---
title: Tutorial for setting up IP-Table tunnel as relay server
---

# Tutorial for setting up IP-Table tunnel as relay server

<div dir="rtl" markdown="1">

For this you need an relay server to connect to the main server. Usually, this relay server is considered in the country of residence.
<div align=center dir="rtl" markdown="1">
 
![Tunnel usage schematic](https://github.com/hiddify/hiddify.com/assets/125398461/1ac4e9e4-4529-4c79-8ff5-eb40e2efad54)
</div>

It is enough to get a good server with adequate bandwidth and CPU.
Now you can buy several cheap and low-capacity relay servers, for example, with 256 RAM, which have a healthy IP or are located in the country of origin.


## Installation of relay server settings

now just run the following command on the Rails server (relay server):
After running, it will ask you to enter the IP address of the main server.

In the requested place, you must enter the IP of the main server.
<div dir="ltr" markdown="1">
 
```bash
bash <(curl https://gist.githubusercontent.com/hiddify-com/63836c9a158eca29bad6c941610028cf/raw/0e4e2138148ab9d3d678723fd904b1cad461ce62/relay.sh)
```
</div>

## Adding Relay server to HiddifyManager
Now, register a subdomain with the proxy off for your relay server IP and register it in Hiddify Manager on `Relay` mode.
- Put the registered subdomain in the `Domain` field and you can also set a `Alias` to display in the configurations.

<img src="https://github.com/hiddify/hiddify.com/assets/125398461/4c0ade4e-394c-4d52-8067-f15d1778c9ed">

## Adding `Relay` configurations to subscription link

As always in HiddifyManager, it is better to separate the configs from the subscription link. Therefore, for the registered `Relay` domain, you can check the `Relay` domain in the subscription domain settings so that its configurations are added to the subscription domain.

Assuming that the subscription domain is `sublink.hiddify.com`, proceed as shown below to get the job done.

<img src="https://github.com/hiddify/hiddify.com/assets/125398461/3661045d-ced7-4694-916f-6ef160c63230">

Now, if you open the user page with the subscription domain (here `sublink.hiddify.com`), you will see that the connections related to the `relay server` have also been added. You can add and use these connections individually or using subscription links to your client.

## Delete the named configs in the relay server
For this, just run the following command and delete the roles
<div dir="ltr" markdown="1">
 
```bash
iptables -F
```
</div>
Or delete the created chains using this command.
<div dir="ltr" markdown="1">
 
```bash
iptables -X
```
</div>



</div>
