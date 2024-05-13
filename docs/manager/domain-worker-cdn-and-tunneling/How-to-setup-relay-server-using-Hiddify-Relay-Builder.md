---
title: How to setup relay server using Hiddify Relay Builder (all in one app)
---

# How to setup relay server using Hiddify Relay Builder (all in one app)
To install and set up the relay server more easily, this application has been created, which starts the server and the tunnel is established using the following methods.<br>
1. IP-Tables method<br>
2. GOST method<br>
3. Dokodemo-Door method<br>
4. HA-Proxy method<br>
5. Socat method<br>
6. WST method<br>
 
Next, follow one of the mentioned methods according to your needs so that the relay server is created in the desired way.

Also, in this tool, it is possible to perform basic settings and test communication.

## ⚙️ Installation and setup
To create a tunnel on your relay server, you just need to run the following command.

```
bash -c "$(curl -L https://raw.githubusercontent.com/hiddify/hiddify-relay/main/install.sh)"
```
<div align=center>

  <img width="80%" src="https://github.com/hiddify/hiddify.com/assets/125398461/713801f1-01fb-4bc7-83ca-e1294fa1b149" alt="Relay-Builder Menu" />
</div>

<details markdown="1" dir="ltr"><summary><h3>🛠️ IP-Tables Tunnel</h3> (click)</summary>
According to the first image above, select the `IP-Tables` option so that you can manage the `IP-Tables tunnel`.

<div align=center>
  
  <img width="80%" src="https://github.com/hiddify/hiddify.com/assets/125398461/80a1ebc9-078b-4e42-844e-6da857e25d62" alt="IP-Tables Tunnel Menu">

</div>
<div align="right">
 
`Install`

After selecting `Install` option in `IP-Tables Menu`, you must select the IP of the main server to enable the tunnel on ports `443` and `80`.

`Status`

This option will show you the ports used in the IP-Tables tunnel.

`Uninstall`

This option deletes all rules created in IP-Tables.

> [Tip!]
>
> Be careful that if you have created special rules next to the tunnel manually, they will be deleted with this command.

`Back`

In order to return to the main menu, select `Back` option.

</details>


<details markdown="1" dir="ltr"><summary><h3>🛠️ GOST tunnel</h3> (click)</summary>
According to the first image above, select the `GOST` option to manage the `GOST tunnel`.

<div align=center>

<img width="80%" src="https://github.com/hiddify/hiddify.com/assets/125398461/ebffa5a5-a19f-4147-8389-8f69e5b48796 alt="GOST Tunnel Menu">

</div>

`Install`

- After selecting `Install` option, wait until the tunnel is installed.
- After the installation, in the first step you have to select the desired ports for the tunnel.
- Then select the subdomain related to Sur Rasli to start the tunnel.
- After starting the tunnel, the message `Gost tunnel is installed and activated` appears on the screen.


`Status`

After selecting this option, the used ports and tunnel status will be displayed on the screen.

`Add`
- This option can be used to connect the relay server to several external servers.
- After selecting the `Add` option, you must enter the new port and the domain of the main server.
- To ensure that this work is done correctly, you can use the `Status` option and check the ports and tunnel status according to this option.


`Uninstall`

Using this option, you can remove the GOST tunnel from the relay server.

`Back`

In order to return to the main menu, select `Back` option.


</details>

<details markdown="1" dir="ltr"><summary><h3>🛠️ Dokodemo-Door tunnel</h3> (click)</summary>
According to the first image above, select `Dekodemo-Door` to manage the `Dekodemo-Door tunnel`.

<div align=center>

<img width="80%" src="https://github.com/hiddify/hiddify.com/assets/125398461/7cdae822-4fe7-40b1-a2ee-49e7bf555fed" alt="Dokodemo-Door Tunnel Menu">

</div>

`Install`
- After selecting `Install` option in this menu, wait for the Xray core to be installed on the relay server.
- After completing the installation, select the IP address or domain of the main server.
- In the section related to ports, select the ports you want to create a tunnel. (Offer: 443,80)
- At the end, the message `Inbound added and tunnel started` appears on the screen, which means that the operation is successful.


`Status`

By selecting `Status` option, the used ports and tunnel status will be displayed on the screen.

`Add`
- By selecting the `Add` option in the Dokodemo-Door tunnel menu, another inbound connection can be set to connect the relay server to another external server.
- After selecting the `Add` option, you must select the IP address or domain of the new main server.
- In the next step, select the port for this server.
- When the message `Additional inbound added` appears, it means that a new inbound has been added.
- To check and ensure the correctness of this step, you can use `Status` option according to the previous option and check the ports and tunnel status.



`Uninstall`

The `Uninstall` option can be used to remove the Dokodemo-Door tunnel and the Xray core from the relay server.

`Back`

To return to the main menu, select `Back` option.
</details>

<details markdown="1" dir="ltr"><summary><h3>🛠️ HA-Proxy tunnel</h3> (click)</summary>
According to the first image above, select the `HA-Proxy` option to manage the `HA-Proxy tunnel`.

<div align=center>
  
<img width="80%" src="https://github.com/hiddify/hiddify.com/assets/125398461/8e94e9d5-6229-46da-afd8-0c1c08787308" alt="HA-Proxy Tunnel Menu">


</div>

`Install`

- After selecting `Install` option, wait for the HA-Proxy package to be installed.
- After installation, select the desired port for the relay server in the Relay server port section. (Recommendation: 443)
- Then select the IP address of the main server.
- In the next step, select the port of the main server. (For example, `HidifyManager` uses port 443)
- After completing this step, if the message ``HA-Proxy tunnel is installed and activated'' is displayed, the tunnel has been installed and activated correctly.


`Status`

By selecting `Status` option, you can check the ports in use and the tunnel status.



`Uninstall`

Use this option to remove the HA-Proxy tunnel from the relay server.

`Back`
In order to return to the main menu, select `Back` option.


</details>

<details markdown="1" dir="ltr"><summary><h3>🛠️ Socat tunnel</h3> (click)</summary>
According to the first image above, select `Socat` to manage `Socat tunnel`.

<div align=center>

<img width="80%" src="https://github.com/hiddify/hiddify-relay/assets/125398461/d0d55310-f06d-44f2-83df-9b698ee9d0fa" alt="Socat Tunnel Menu">

</div>

`Install`

- Wait for the Socat package to be installed by selecting `Install` option.
- Then select the IP and port of the main server.
- After performing the operation correctly, the tunnel will be correctly activated when the message `Socat tunnel is installed and activated` appears.

  
`Status`

By selecting `Status` option, you can check the used ports and tunnel status.


`Uninstall`

By selecting this option, the Socat tunnel can be removed from the relay server.


`Back`
In order to return to the main menu, select `Back` option.
</details>




<details markdown="1" dir="ltr"><summary><h3>🛠️ WST Tunnel</h3> (click)</summary>
According to the first image above, select `WST` option to manage `WST tunnel`.

<div align=center>

<img width="80%" src="https://github.com/hiddify/hiddify.com/assets/125398461/f9686f53-7a34-4085-9504-15aac82a29ce" alt="WST Tunnel Menu">

</div>

`Install`

- Wait for the WST package to be installed by selecting `Install` option.
- Then select the IP and port of the main server.
- Then enter the information related to SSH access to the main server so that the settings related to the tunnel on that server side can be made.
- After performing the operation correctly, the tunnel will be correctly activated when the message `WSTunnel is installed and activated` appears.

  
`Status`

By selecting `Status` option, you can check the used ports and tunnel status.


`Uninstall`

By selecting this option, the WST tunnel can be removed from the relay server.


`Back`
In order to return to the main menu, select ``Back'' option.
</details>

<details markdown="1" dir="ltr"><summary><h3>🛠️ Options</h3> (click)</summary>
According to the first image above, select ``Options'' option to perform basic server settings and connection test.

<div align=center>


<img width="80%" src="https://github.com/hiddify/hiddify.com/assets/125398461/aea50ed9-94a8-4884-92dd-24ef15067253" alt="Options Menu">

</div>

`DNS`

- By selecting the `DNS` option, you can configure DNS settings for the server.
- Enter your desired IPs for DNS here. It is recommended to use valid DNS like `8.8.8.8`, `1.1.1.1`, `4.2.2.4`.

  
`Update`

By selecting the `Update` option, all server packages can be completely updated.


`Ping`

By choosing this option, you can test the server's connection to the Internet.


`Back`
In order to return to the main menu, select `Back` option.
</details>


<br>

!!! tip "Tip"
    If you want to add your relay server to HiddifyManager, read this [article](/manager/domain-worker-cdn-and-tunneling/How-to-add-relay-domain-to-Hiddify-manager/)
