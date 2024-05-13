---
title: Tutorial for setting up local IPv6 for Relay server
---

<div markdown="1">

# Tutorial for setting up local IPv6 for Relay server
In some relay servers, IPv6 may not be provided, and you can create a local IPv6 using this method in your tunnels.


## Relay server

To create local IPv6, you need to first install the iproute2 service on relay server with the following command.

```shell
sudo apt-get install iproute2
```

After installing the above service, create the `tunnel.yaml` file in the `netplan` folder with `nano` editor.

```shell
sudo nano /etc/netplan/tunnel.yaml
```

Then copy the following code in the file.


```yaml
network:
   version: 2
   tunnels:
     tunnel98:
       mode: sit
       local: IPv4-RELAY
       remote: IPv4-Main
       addresses:
         - 2001:db9:900::1/64
  ```


Instead of `IPv4-RELAY` put your relay server IP and instead of `IPv4-MAIN` put your main server IP.

After making the changes, save the file by pressing the `Ctrl+s` button and exit the editor by pressing the `Ctrl+x` button.

At the end, apply the changes made in `netplan` with the following command.


```
sudo netplan apply
```


## Main server
To create local IPv6 on the main server, you need to install the `iproute2` service.

```shell
sudo apt-get install iproute2
```

After installing the above service, create the `tunnel.yaml` file in the `netplan` folder with `nano` editor.

```shell
sudo nano /etc/netplan/tunnel.yaml
```

Then copy the following code into the file.

```yaml
network:
   version: 2
   tunnels:
     tunnel98:
       mode: sit
       local: IPv4-Main
       remote: IPv4-IRAN
       addresses:
         - 2001:db9:900::2/64
```

- Put the relay server IP instead of `IPv4-RELAY` and put your main server IP instead of `IPv4-MAIN`.
- After making changes, save the file by pressing the `Ctrl+s` button and exit the editor by pressing the `Ctrl+x' button.
- At the end, apply the changes made in netplan with the following command.

<code>sudo netplan apply</code>

- The work is finished.
  
In this method, local IPv6s are as follows.

Your relay server:

```
2001:db9:900::1
```

Your main server:

```
2001:db9:900::2
```


## Connection test

To test the connection, just ping the IPv6 local relay server from your main server:

```
ping 2001:db9:900::1
```

!!! tip "Tip!"
     Please note that if the firewall is on on any of the servers, it is not possible to test through ping and it is necessary to turn off the firewall temporarily. [Firewall setup](/manager/basic-concepts-and-troubleshooting/How-to-setup-Firewall-on-Hiddify-panel/)

    
## How to use

You can use [`Dokodemo-Door`](/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-Dokodemo-Door-tunnel-as-relay-server) or use [`GOST`](/fa/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-GOST-tunnel-as-relay-server/) on your relay server and instead of IP or domain, use the local IPv6 that you created for the main server.

Example `Dokodemo-Door`:

```json

{
    "inbounds": [
      {
        "listen": "127.0.0.1",
        "port": 62789,
        "protocol": "dokodemo-Door",
        "settings": {
          "address": "127.0.0.1"
        },
        "tag": "api"
      },
      {
        "listen": null,
        "port": 443,
        "protocol": "dokodemo-Door",
        "settings": {
          "address": "2001:db9:900::2",
          "followRedirect": false,
          "network": "tcp,udp",
          "port": 443
        },
        "tag": "inbound-IPv6-local"
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




If you pay attention, in the example above, the local IPv6 value created for the main server is placed in the `address` field, and 443 is entered in the `port` field, which you can change the `port` to the tunneled port.



</div>
