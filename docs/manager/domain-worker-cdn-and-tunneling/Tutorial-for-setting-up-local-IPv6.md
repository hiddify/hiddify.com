---
title: Tutorial for setting up local IPv6 for Relay server
---

<div markdown="1">

# Tutorial for setting up local IPv6 for Relay server
In some relay servers, IPv6 may not be provided, and you can create a local IPv6 using this method in your tunnels.



!!! note
    The addresses below (`fd00:900::1` and `fd00:900::2`) are private (local) IPv6 addresses; you can use other ones from the `fd00::/8` range. Older versions of this guide used `2001:db9:900::`, which is a public range: change it to a private one if you set it up that way.

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
       remote: IPv4-MAIN
       addresses:
         - fd00:900::1/64
```


- Instead of `IPv4-RELAY` put your relay server IP and instead of `IPv4-MAIN` put your main server IP.

- After making the changes, save the file by pressing the `Ctrl+s` button and exit the editor by pressing the `Ctrl+x` button.

- At the end, apply the changes made in `netplan` with the following command.


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
       local: IPv4-MAIN
       remote: IPv4-RELAY
       addresses:
         - fd00:900::2/64
```

- Put the relay server IP instead of `IPv4-RELAY` and put your main server IP instead of `IPv4-MAIN`.
- After making changes, save the file by pressing the `Ctrl+s` button and exit the editor by pressing the `Ctrl+x' button.
- At the end, apply the changes made in netplan with the following command.

```shell
sudo netplan apply
```

- The work is finished.
  
In this method, local IPv6s are as follows.

Your relay server:

```
fd00:900::1
```

Your main server:

```
fd00:900::2
```


## Connection test

To test the connection, just ping the IPv6 local relay server from your main server:

```
ping fd00:900::1
```

!!! tip "Firewall"
    The tunnel uses IP protocol 41 (SIT). If the HiddifyManager firewall (**Settings** › **General Settings** › **Firewall**) or another firewall is on, it drops the tunnel. Allow the other server on both sides, for example on the main server: `iptables -I INPUT -p 41 -s IPv4-RELAY -j ACCEPT` (and `-s IPv4-MAIN` on the relay server). If the tunnel stops after you apply changes in the panel, run it again. [Firewall setup](/manager/basic-concepts-and-troubleshooting/How-to-setup-Firewall-on-Hiddify-panel/)
    
## How to use

You can use [`Dokodemo-Door`](/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-Dokodemo-Door-tunnel-as-relay-server/) or use [`GOST`](/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-GOST-tunnel-as-relay-server/) on your relay server and instead of IP or domain, use the local IPv6 that you created for the main server.

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
          "address": "fd00:900::2",
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

To learn how to add a relay server (domain) to HiddifyManager, read [this article](/manager/domain-worker-cdn-and-tunneling/How-to-add-relay-domain-to-Hiddify-manager/) do it

## Related articles

- [The server's IPv6 for steadier tunnels](/manager/domain-worker-cdn-and-tunneling/Tutorial-for-setting-up-IPv6-to-improve-Relay-stability/)
- [4to6 tunnel](/manager/domain-worker-cdn-and-tunneling/Setup-ip4toip6-tunnel/)
- [Domain types and how to add them](/manager/domain-worker-cdn-and-tunneling/Domain-types-and-how-to-register-them/)
- [Fake domain](/manager/domain-worker-cdn-and-tunneling/How-to-create-and-use-fake-domain/)

</div>
