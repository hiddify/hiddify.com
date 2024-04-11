---
title: Tutorial for setting up GOST tunnel as relay server
---

# Tutorial for setting up GOST tunnel as relay server
What is? iptables is the best alternative solution for IP Forwarding with**

For this you need a relay server to connect to the main server. Usually, this relay server is considered in the country of residence.

<div align="center" dir="ltr" markdown="1">
  
![Tunnel usage schematic](https://github.com/hiddify/hiddify.com/assets/125398461/1ac4e9e4-4529-4c79-8ff5-eb40e2efad54)
</div>





One of the best ways to replace IP-Forwarding with IP-Tables is to use GOST tunnel.

This tunnel is much better than IP Forwarding in many ways. (or the normal tunneling that everyone uses)
In this method, unlike IP forwarding, you can use the domain or subdomain name instead of IP, which makes your server's IP less recognizable.
Another advantage of this method is that it passes through an encrypted data tunnel.
This tunnel is Open Source.
It is compatible with V2Ray - VMess - Vless - Trojan protocols.
Both WebSocket and gRPC work in this tunnel
Because this tunnel has its own service, it is executed when the server is rebooted, and there is no need to enter the command again.
If you want, you can forward both TCP and UDP ports. Just enter UDP instead of TCP in the command.
You can forward as many ports as you want

To install in Relay mode, proceed according to this tutorial.

- Log in to your relay server, that is, SSH to your server.
- First, download the desired program source with the following code and unzip it.

```
sudo apt install wget nano -y && wget https://github.com/ginuerzh/gost/releases/download/v2.11.5/gost-linux-amd64-2.11.5.gz && gunzip gost-linux-amd64-2.11. 5.gz
```

- Then transfer its files to the executable folder and execute access to it.

```
sudo mv gost-linux-amd64-2.11.5 /usr/local/bin/gost && sudo chmod +x /usr/local/bin/gost
```

- Now you have to create its service as well.
- First, create the service file using the nano editor.

```
sudo nano /usr/lib/systemd/system/gost.service
```

Then copy the following code completely in the opened file.

```
[Unit]
Description=GO Simple Tunnel
After=network.target
Wants=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/gost -L=tcp://:443/domain.com:443 -L=tcp://:80/domain.com:80

[Install]
WantedBy=multi-user.target
```

After copying, you should put your domain name instead of domain.com. Note that the domain name you enter must be the main IP address of your server. (Delete both domain.com and enter your domain name)

Well, the work is almost done.
Now start the gost service with the following code. And then you enable the service to run every time the service is restarted:

```
sudo systemctl start gost && systemctl enable gost
```

The work is finished and you can use the tunnel.

## Relay server definition in HiddifyManager
Now register **a subdomain with proxy off** for your relay server IP and register it in HiddifyManager on Relay mode.

 
![](https://user-images.githubusercontent.com/125398461/235341283-97c026b7-1d70-4362-8950-1e5c1b79d508.png)

## Adding relay configurations to be used in the subscription link
As always in HiddifyManager, it is better to separate the configs from the subscription link. Therefore, for the registered Relay domain, you can check the Relay domain in the subscription domain settings so that its configurations are added to the subscription domain.

Assuming the domain for the subscription is t1.hiddify.com, proceed as shown below to get the job done.

![Screenshot_20230430_1104341](https://user-images.githubusercontent.com/125398461/235342038-cfda2574-2444-4414-843d-2ed507537d1d.png)


Now, if you open the user page with the subscription domain (here t1.hiddify.com), you will see that Relay connections have been added. You can add and use these connections one by one or using normal subscription links or b64 subscription to your client.



## Removing the GOST configuration from relay server

To do this, first run this command.

```
systemctl daemon-reload
```
And then stop and disable the GOST service.
```
sudo systemctl stop gost && systemctl disable gost
```
Finally, press these commands to completely remove the program and service.

```
sudo rm -f /usr/lib/systemd/system/gost.service /usr/local/bin/gost
```
[GOST project source] (https://github.com/ginuerzh/gost)
