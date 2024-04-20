---
title: Tutorial for setting up WST tunnel as relay server
---

# Tutorial for setting up WST tunnel as relay server

For this you need an relay server to connect to the main server. Usually this relay server is considered in Iran.
The tunnel usage diagram is as follows.

<div align="center" dir="ltr" markdown="1">
  
![Tunnel usage schematic](https://github.com/hiddify/hiddify.com/assets/125398461/1ac4e9e4-4529-4c79-8ff5-eb40e2efad54)
</div>

Now here, WS tunnel is used for communication between Iran server and main server. After installation, you will connect to the Iranian server, the Iranian server will connect you to the main server, and then you will have free access to the Internet from the main server.

> Note: We tested these scripts on Ubuntu 22.04, so it is better to use this version.

On the main server, install HiddifyManager, whose installation guide is available at [here](https://hiddify.com/fa/manager/installation-and-setup/guide/).

## Installing the tunnel on the main and relay server (Iran)
You must install this tunnel program on **both servers**. To do this, first connect to the server with root and run the following codes:
First, download the program with the following command.
```
wget "https://github.com/erebe/wstunnel/releases/download/v5.0/wstunnel-linux-x64"
```
Give it execute access.
```
sudo chmod +x wstunnel-linux-x64
```
Rename the program with the command and move it to the bin/ folder.
```
sudo mv wstunnel-linux-x64 /bin/wstunnel
```

## Running the tunnel on the main server

On the main server where HiddifyManager is installed, you need to run the installed tunnel. Activate it on port 8080 with this command.

```
sudo wstunnel --server ws://0.0.0.0:8080 -v
```

> Note: If you change the tunnel port, the ports must be the same on both servers.

- Pay attention, after entering this command, the message ``WAIT for tcp connection on 0.0.0.0:8080'' is given, which means the successful execution of the tunnel and waiting for the link to be established in the relay server, because this tunnel requires communication from both has the position

The work of setting up the tunnel on the main server is also finished.



## Running the tunnel on the relay server
To set up the tunnel on the relay server using this command, you must provide both the required ports for downloading and the port that the tunnel uses to communicate.
Here, port 8080 is used for the tunnel itself, which was configured on the main server side. Also, the HiddifyManager program uses ports 443 and 80 automatically, so you can put them in the following command.

- If you change the default ports of HiddifyManager panel, change ports 443 and 80 according to the same formula.

* If you want to download another port, you can do it with the same formula.


```
sudo wstunnel -L 0.0.0.0:80:localhost:80 -L 0.0.0.0:443:localhost:443 ws://[cdn_or_direct_domain_of_main_server]:8080
```



- Please note that [server_adress_or_domain] should be placed with the CDN or direct domain registered in Hidify or the main IP of the server.
- If you do this with the CDN domain, you will also prevent the main server from being filtered.
* Pay attention to the message after typing this command
  ``WAIT for tcp connection on 0.0.0.0:80, WAIT for tcp connection on 0.0.0.0:443'' is given, which means the successful execution of the tunnel and waiting for the connection to be established from the client side.

- If the main tunnel port (here 8080) is filtered on your Iranian data center, you can use other ports.
- Very important note: If you use CDN domains to establish a tunnel, you are only allowed to use Cloudflare ports. That is, you can only use Cloudflare's https ports for connection, and you can use Cloudflare's http ports for the tunnel itself. [List of Cloudflare ports](https://developers.cloudflare.com/fundamentals/get-started/reference/network-ports/)

Work on setting up the ws tunnel on the relay server is complete.

## Setting up the tunnel service on the main server

You only need to create its service so that if the server is reset, the tunnel will run automatically. To do this, exit the created tunnel with `Ctrl+c`, then with a text editor (here nano) create the service file in the main path of the kernel.

```
sudo nano /etc/systemd/system/wstunnel.service
```

Then in the opened file, copy the following text to define the desired service.

```
[Unit]
Description=wstunnel
After=network.target

[Service]
Type=simple
WorkingDirectory=/bin
ExecStart= wstunnel --server ws://0.0.0.0:8080 -v
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

To exit the text editor, press `Ctrl+s` to save the file, then exit the program with `Ctrl+x`.

Now reset the main kernel service and activate and start the created service.

```
sudo systemctl daemon-reload
sudo systemctl enable wstunnel.service
sudo systemctl start wstunnel.service
```
Now, to check if the service is activated, type this command and check that the service is active.
```
sudo systemctl status wstunnel.service
```

If for any reason the service was not active, one of the previous steps was probably not done correctly.



## Setting up the tunnel service on relay server
You only need to create its service so that if the server is reset, the tunnel will run automatically. To do this, create the service file in the main path of the kernel with a text editor (here nano).
```
sudo nano /etc/systemd/system/wstunnel.service
```
Then in the opened file, copy the following text to define the desired service.

```
[Unit]
Description=wstunnel
After=network.target

[Service]
Type=simple
WorkingDirectory=/bin
ExecStart= wstunnel -L 0.0.0.0:80:localhost:80 -L 0.0.0.0:443:localhost:443 ws://[cdn_or_direct_domain_of_main_server]:8080
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

- Make sure to paste `cdn_or_direct_domain_of_main_server` with your direct domain or CDN specification.
- To exit the text editor, first press `Ctrl + s` to save the file, then exit the program with `Ctrl + x`.

Now reset the main kernel service and activate and start the created service.

```
sudo systemctl daemon-reload
sudo systemctl enable wstunnel.service
sudo systemctl start wstunnel.service
```
Now, to check if the service is activated, type this command and check that the service is active.
```
sudo systemctl status wstunnel.service
```

If for any reason the service was not active, one of the previous steps was probably not done correctly.


## Adding Relay server to HiddifyManager
Now, register a subdomain with the proxy off for your relay server IP and register it in Hiddify Manager on `Relay` mode.
- Put the registered subdomain in the `Domain` field and you can also set a `Alias` to display in the configurations.

<img src="https://github.com/hiddify/hiddify.com/assets/125398461/4c0ade4e-394c-4d52-8067-f15d1778c9ed">

## Adding `Relay` configurations to subscription link

As always in HiddifyManager, it is better to separate the configs from the subscription link. Therefore, for the registered `Relay` domain, you can check the `Relay` domain in the subscription domain settings so that its configurations are added to the subscription domain.

Assuming that the subscription domain is `sublink.hiddify.com`, proceed as shown below to get the job done.

<img src="https://github.com/hiddify/hiddify.com/assets/125398461/e9fa3756-bb3a-4ee9-8adb-77a9f58f6354">

Now, if you open the user page with the subscription domain (here `sublink.hiddify.com`), you will see that the connections related to the `relay server` have also been added. You can add and use these connections individually or using subscription links to your client.

## Remove the tunnel from the relay server and the main server

First you need to stop and disable the service.
```
sudo systemctl daemon-reload
sudo systemctl stop wstunnel.service
sudo systemctl disable wstunnel.service
```
Then delete the app and service.
```
sudo rm -f /etc/systemd/system/wstunnel.service /bin/wstunnel
```

[WS Tunnel project link](https://github.com/erebe/wstunnel)
