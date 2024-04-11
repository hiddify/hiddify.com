---
title: Tutorial for setting up Dokodemo-door tunnel as relay server
---

# Tutorial for setting up Dokodemo-door tunnel as relay server

For this you need an intermediate server to connect to the main server. Usually this middle server is considered in Iran.
The tunnel usage diagram is as follows.

<div align="center" markdown="1">
  
![Tunnel usage schematic](https://github.com/hiddify/hiddify.com/assets/125398461/1ac4e9e4-4529-4c79-8ff5-eb40e2efad54)
</div>

Now here, WS tunnel is used for communication between Iran server and main server. After installation, you will connect to the Iranian server, the Iranian server will connect you to the main server, and then you will have free access to the Internet from the main server.

> Note: We tested these scripts on Ubuntu 22.04, so it is better to use this version.

Also, install HiddifyManager on the main server, whose installation guide is available [here](https://hiddify.com/manager/installation-and-setup/guide/).

## Installing the tunnel on the main and relay server
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

- Pay attention, after entering this command, the message ``WAIT for tcp connection on 0.0.0.0:8080'' is given, which means the successful execution of the tunnel and waiting for the link to be established in the middle server, because this tunnel requires communication from both has the position

The work of setting up the tunnel on the main server is also finished.



## Setting up the tunnel on Relay server
To set up the tunnel on the middle server using this command, you must provide both the required ports for downloading and the port that the tunnel uses to communicate.
Here, port 8080 is used for the tunnel itself, which was configured on the main server side. Also, the H program uses ports 443 and 80 automatically, so you can put them in the following command.

- If you change the default ports of H panel, change ports 443 and 80 according to the same formula.

* If you want to download another port, you can do it with the same formula.


```
sudo wstunnel -L 0.0.0.0:80:localhost:80 -L 0.0.0.0:443:localhost:443 ws://[cdn_or_direct_domain_of_main_server]:8080
```



- Please note that [server_adress_or_domain] should be placed with the CDN or direct domain registered in Hidify or the main IP of the server.
- If you do this with the CDN domain, you will also prevent the main server from being filtered.
* Pay attention to the message after typing this command
  ``WAIT for tcp connection on 0.0.0.0:80, WAIT for tcp connection on 0.0.0.0:443'' is given, which means the successful execution of the tunnel and waiting for the connection to be established from the client side.

- If the main tunnel port (here 8080) is filtered on your Iranian data center, you can use other ports.
- Very important note: If you use CDN domains to establish a tunnel, you are only allowed to use Cloudflare ports. That is, you can only use Cloudflare's https ports for connection, and you can use Cloudflare's http ports for the tunnel itself. [List of Cloudflare ports] (https://developers.cloudflare.com/fundamentals/get-started/reference/network-ports/)

Work on setting up the ws tunnel on the middle server is complete.

## Setting up the tunnel service on the main server

You only need to create its service so that if the server is reset, the tunnel will run automatically. To do this, exit the created tunnel with `ctrl+c`, then with a text editor (here nano) create the service file in the main path of the kernel.

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

To exit the text editor, press ctrl+s to save the file, then exit the program with ctrl+x.

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

If for any reason the service is not active, one of the previous steps is probably correct
