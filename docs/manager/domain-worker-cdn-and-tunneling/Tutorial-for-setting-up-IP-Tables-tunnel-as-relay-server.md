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

## relay server definition in HiddifyManager
Now register **a subdomain with off proxy** for your relay server IP (Iran) and register it in HiddifyManager on Relay mode.

 
![](https://user-images.githubusercontent.com/125398461/235341283-97c026b7-1d70-4362-8950-1e5c1b79d508.png)

## Adding relay configurations to be used in the subscription link
As always in HiddifyManager, it is better to separate the configs from the subscription link. Therefore, for the registered Relay domain, you can check the Relay domain in the subscription domain settings so that its configurations are added to the subscription domain.

Assuming the domain for the subscription is `t1.hiddify.com`, proceed as shown below to get the job done.

![Screenshot_20230430_1104341](https://user-images.githubusercontent.com/125398461/235342038-cfda2574-2444-4414-843d-2ed507537d1d.png)


Now if you open the user page with the subscription domain (here `t1.hiddify.com`) you will see that the Relay connections have also been added. You can add and use these connections one by one or using normal subscription links or b64 subscription to your client.

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
