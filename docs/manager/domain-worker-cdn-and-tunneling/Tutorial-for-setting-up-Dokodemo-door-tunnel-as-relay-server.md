---
title: Tutorial for setting up Dokodemo-door tunnel as relay server
---

# Tutorial for setting up Dokodemo-door tunnel as relay server

For this you need an relay server to connect to the main server. Usually this middle server is considered in Iran.
The tunnel usage diagram is as follows.

<div align="center" markdown="1">
  
![Tunnel usage schematic](https://github.com/hiddify/hiddify.com/assets/125398461/1ac4e9e4-4529-4c79-8ff5-eb40e2efad54)
</div>

---
title: Tutorial on setting up the Dokodemo-door tunnel as an relay server
---

# Tutorial on setting up the Dokodemo-door tunnel as an relay server

For this you need an relay server to connect to the main server. Usually this relay server is considered in the country of your residence.
<div align=center dir="rtl" markdown="1">
 
<img src="https://user-images.githubusercontent.com/125398461/235339506-bdd76cec-0378-4942-8352-ebebeb006231.png">
</div>


- [SSH to the relay server](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/) and run Xray kernel installation command

```
sudo bash -c "$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)" @ install
```

- After installation, you must create the `config.json` file with the following command.

```
nano /usr/local/etc/xray/config.json
```

- Now see the code below which is related to the ``inbound'' and ``outbound'' traffic of the dokodemo-door tunnel.

```
{
   "inbounds": [
     {
       "listen": "127.0.0.1",
       "port": 62789,
       "protocol": "dokodemo-door",
       "settings": {
         "address": "127.0.0.1"
       },
       "tag": "api"
     },
     {
       "listen": null,
       "port": Main_Server_Port,
       "protocol": "dokodemo-door",
       "settings": {
         "address": "MAIN_SERVER_IP",
         "followRedirect": false,
         "network": "tcp,udp",
         "port": MAIN_SERVER_PORT
       },
       "tag": "inbound-MAIN_SERVER_PORT"
     }
   ],
   "outbounds": [
     {
       "protocol": "freedom"
     },
     {
       "protocol": "blackhole",
       "tag": "blocked"
     }
   ]
}
```

- In the `MAIN_SERVER_PORT` port field, put the port of your main server (HiddifyManager) that you considered for the tunnel connection on that server.
- For example, port 443 is used by HiddifyManager by default for routers.
- In the `MAIN_SERVER_IP` section, you should put your main server's IP address.
- For example, if your server's IP is `10.10.10.10` and its port is `443`, then the `inbound` code will be as follows:

```
{
   "inbounds": [
     {
       "listen": "127.0.0.1",
       "port": 62789,
       "protocol": "dokodemo-door",
       "settings": {
         "address": "127.0.0.1"
       },
       "tag": "api"
     },
     {
       "listen": null,
       "port": 443,
       "protocol": "dokodemo-door",
       "settings": {
         "address": "10.10.10.10",
         "followRedirect": false,
         "network": "tcp,udp",
         "port": 443
       },
       "tag": "inbound-443"
     }
   ],
   "outbounds": [
     {
       "protocol": "freedom"
     },
     {
       "protocol": "blackhole",
       "tag": "blocked"
     }
   ]
}
```


After performing the configuration operation, press `Ctrl + s` button to save the changes and press `Ctrl + x` to exit the `config.json` file.

##### Defining several different inbounds in the relay server to connect to several primary servers

For this, it is enough to define a new `inbound` in the `config.json` code after finishing each `inbound`. For example, suppose we have two main servers, the IP of the first server is `10.10.10.10` and its port is `443`, the IP of the second server is `20.20.20.20` and its port is `8443`. To create two independent tunnels to these servers, two `inbound` must be created as follows.

```
{
   "inbounds": [
     {
       "listen": "127.0.0.1",
       "port": 62789,
       "protocol": "dokodemo-door",
       "settings": {
         "address": "127.0.0.1"
       },
       "tag": "api"
     },
     {
       "listen": null,
       "port": 443,
       "protocol": "dokodemo-door",
       "settings": {
         "address": "10.10.10.10",
         "followRedirect": false,
         "network": "tcp,udp",
         "port": 443
       },
       "tag": "inbound-443"
     }
    {
       "listen": null,
       "port": 8443,
       "protocol": "dokodemo-door",
       "settings": {
         "address": "20.20.20.20",
         "followRedirect": false,
         "network": "tcp,udp",
         "port": 8443
       },
       "tag": "inbound-8443"
     }
   ],
   "outbounds": [
     {
       "protocol": "freedom"
     },
     {
       "protocol": "blackhole",
       "tag": "blocked"
     }
   ]
}
```

- After saving the file, hit restart the Xray kernel.

```
sudo systemctl restart xray
```

## Relay server definition in Hidify
Now, register a subdomain with proxy off for your relay server IP and register it in Hidify on Relay mode.

<img src="https://user-images.githubusercontent.com/125398461/235341283-97c026b7-1d70-4362-8950-1e5c1b79d508.png">

## Adding relay configurations to be used in the subscription link

As always in Hidify, it is better to separate the configs from the subscription link. Therefore, for the registered Relay domain, you can check the Relay domain in the subscription domain settings so that its configurations are added to the subscription domain.

Assuming the domain for the subscription is `t1.hiddify.com`, proceed as shown below to get the job done.
<img src="https://user-images.githubusercontent.com/125398461/235342038-cfda2574-2444-4414-843d-2ed507537d1d.png">

Now if the user page with the subscription domain (here `t1.hiddify.com`)
