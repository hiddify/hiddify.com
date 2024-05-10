---
title: Tutorial for setting up HA-Proxy tunnel as relay server
---

# Tutorial for setting up HA-Proxy tunnel as relay server

For this you need an relay server to connect to the main server. Usually, this relay server is considered in the country of residence.

<div align="center" markdown="1">
  
![Tunnel usage schematic](https://github.com/hiddify/hiddify.com/assets/125398461/1ac4e9e4-4529-4c79-8ff5-eb40e2efad54)
</div>

Now, HA-proxy tunnel is used here for the communication between the relay server and the main server. After installation, you will connect to the relay server, that server will connect you to the main server, and then you will have free access to the Internet from the main server.

> Note: We tested these scripts on Ubuntu 22.04, so it is better to use this version.

## Installing the HA-proxy tunnel on the relay server and connecting it to the external server

- For this you need an relay server to connect to the main server through it. Usually, this relay server is considered in the country of residence.

- (Connect via SSH to the relay server)[/manager/installation-and-setup/How-to-connect-to-server-via-SSH/] and run the HA-proxy installation command.

```bash
sudo apt-get install haproxy
```

- After installation, you need to change the `haproxy.cfg` file, run the command to open the `haproxy.cfg` file with the `nano` text editor.

```bash
nano /etc/haproxy/haproxy.cfg
```

- When the `haproxy.cfg` file opens, go to the end of the file and add the following example:

```bash
frontend myfrontend
     bind *:RELAY_PORT
     mode tcp
     default_backend mybackend

backend mybackend
     mode tcp
     server target_server MAIN_SERVER_IP:MAIN_SERVER_PORT
```

- In the `RELAY_PORT` section, put the port of your relay server that you consider for sending requests to the main server.

- In the field `MAIN_SERVER_IP:MAIN_SERVER_PORT`, you should put the IP and port of your main server. For example, port 443 is used by HiddifyManager by default.

- For example, if the IP of your main server is `10.10.10.10`, in this case, to transfer user traffic on port `443` through the relay server to the main server, the desired file should be as follows:

```bash
frontend myfrontend
     bind *:443
     mode tcp
     default_backend mybackend

backend mybackend
     mode tcp
     server target_server 10.10.10.10:443
```

- After making the changes, save the changes by pressing `Ctrl + s` buttons and exit the file by pressing `Ctrl + x`.

- After saving the file, press the command to restart HAProxy.

```bash
sudo systemctl restart haproxy
```
## Adding Relay server to HiddifyManager
Now, register a subdomain with the proxy off for your relay server IP and register it in Hiddify Manager on `Relay` mode.
- Put the registered subdomain in the `Domain` field and you can also set a `Alias` to display in the configurations.

<img src="https://github.com/hiddify/hiddify.com/assets/125398461/4c0ade4e-394c-4d52-8067-f15d1778c9ed">

## Adding `Relay` configurations to subscription link

As always in HiddifyManager, it is better to separate the configs from the subscription link. Therefore, for the registered `Relay` domain, you can check the `Relay` domain in the subscription domain settings so that its configurations are added to the subscription domain.

Assuming that the subscription domain is `sublink.hiddify.com`, proceed as shown below to get the job done.

<img src="https://github.com/hiddify/hiddify.com/assets/125398461/e9fa3756-bb3a-4ee9-8adb-77a9f58f6354">

Now, if you open the user page with the subscription domain (here `sublink.hiddify.com`), you will see that the connections related to the `relay server` have also been added. You can add and use these connections individually or using subscription links to your client.

## Removing the HA-Proxy tunnel from the relay server

To do this, first run this command.

```bash
sudo systemctl stop haproxy && systemctl disable haproxy
````

Finally, click this command to completely remove the program and service.

```bash
sudo apt remove haproxy
```
