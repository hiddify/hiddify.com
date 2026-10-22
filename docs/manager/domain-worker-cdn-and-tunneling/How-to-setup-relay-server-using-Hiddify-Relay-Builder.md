---
title: How to setup relay server using Hiddify Relay Builder (all in one app)
---

# How to setup relay server using Hiddify Relay Builder (all in one app)

Hiddify Relay Builder is a menu-driven script that turns a fresh server into a relay server in a few steps. Use it if you want a relay but do not want to type tunnel commands by hand.

A **relay server** is a second server, usually inside your own country, that your users connect to. It forwards their traffic to your main Hiddify server abroad. This helps when the main server's IP is blocked or slow from your country. [Read more about relay servers](/manager/domain-worker-cdn-and-tunneling/How-to-add-relay-domain-to-Hiddify-manager/#what-is-a-relay-server-and-why-use-one).

The script can build the tunnel between the relay and the main server with these methods (a **tunnel** here simply means "a way to pass traffic from one server to the other"):

1. IP-Tables
2. GOST
3. Dokodemo-Door
4. HA-Proxy
5. Socat (old, see below)
6. WST (old, see below)

It also has a few basic tools: DNS settings, a server update and a connectivity test.

!!! warning "Project status"
    The script lives at [github.com/hiddify/hiddify-relay](https://github.com/hiddify/hiddify-relay). Its last change was in October 2024, so treat it as "works, but not actively developed". In the current version, **Socat** and **WST** are marked "No longer supported" and are hidden under **Options** → **DeprecatedTunnel**.

## Prerequisites

- A main server with Hiddify Manager already installed. See the [installation guide](/manager/installation-and-setup/guide/).
- A relay server running Ubuntu or Debian (the script also accepts CentOS, Rocky Linux, AlmaLinux and Fedora).
- SSH access to the relay server as `root`, or as a user that can run `sudo` without typing a password. The script stops with "This user does not have sudo permissions" otherwise. New to SSH? See [how to connect to a server via SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/).
- The IP address (or a direct, non-CDN domain) of your main server.

## ⚙️ Installation and setup

1. Connect to your **relay server** over SSH.
2. Run this command:

    ```bash
    bash <(curl https://raw.githubusercontent.com/hiddify/hiddify-relay/main/install.sh)
    ```

3. Wait while it installs a few helper packages and downloads itself to `/opt/hiddify-relay`. When it finishes, you see the main menu:

<div align=center>

  <img width="80%" src="https://github.com/hiddify/hiddify.com/assets/125398461/713801f1-01fb-4bc7-83ca-e1294fa1b149" alt="Relay Builder main menu" />
</div>

Use the arrow keys to move, `Enter` to select, and `Tab` to jump to the OK/Cancel buttons.

To open the menu again later, log in to the relay server again and type:

```bash
relay
```

!!! tip "Forward both ports 443 and 80"
    Hiddify Manager uses port `443` for most configs, and needs port `80` to get its free TLS certificate for the relay domain. Whichever method you choose, make sure both ports reach the main server. In methods that ask for one port at a time, add `443` first and then use **Add** to add `80`.

Open the section for the method you want:

<details markdown="1" dir="ltr"><summary><h3>🛠️ IP-Tables Tunnel</h3> (click)</summary>
In the main menu, select `IP-Tables`.

<div align=center>

  <img width="80%" src="https://github.com/hiddify/hiddify.com/assets/125398461/80a1ebc9-078b-4e42-844e-6da857e25d62" alt="IP-Tables tunnel menu">

</div>

`Install`

1. Enter the IP of your main server.
2. Enter the ports to forward, separated by commas. The default `80,443` is right for Hiddify Manager.
3. When you see `IPTables installation completed.`, the tunnel is active.

`Status`

Shows the ports used by the IP-Tables tunnel.

`Uninstall`

Deletes the IP-Tables rules.

!!! tip "Tip!"
    If you added your own IP-Tables rules by hand, they may be deleted too.

`Back`

Returns to the main menu.

</details>


<details markdown="1" dir="ltr"><summary><h3>🛠️ GOST tunnel</h3> (click)</summary>
In the main menu, select `GOST`. The script installs the latest GOST (v3) from the official [go-gost](https://github.com/go-gost/gost) installer.

<div align=center>

<img width="80%" src="https://github.com/hiddify/hiddify.com/assets/125398461/ebffa5a5-a19f-4147-8389-8f69e5b48796" alt="GOST tunnel menu">

</div>

`Install`

1. Wait until GOST is installed.
2. Enter the domain or IP of your main server. If you use a domain, it must point straight to the main server (not through a CDN).
3. Enter the port, for example `443`.
4. When you see `GOST tunnel is installed and active.`, the tunnel works.

`Status`

Shows the ports in use and whether the tunnel is running.

`Add`

- Adds another port, or a connection to another main server.
- Enter the main server's domain or IP, then the port. Use this to add port `80`.
- Check the result with `Status`.

`Remove`

Removes one port and its domain from the GOST configuration.

`Uninstall`

Removes the GOST tunnel from the relay server.

`Back`

Returns to the main menu.

</details>

<details markdown="1" dir="ltr"><summary><h3>🛠️ Dokodemo-Door tunnel</h3> (click)</summary>
In the main menu, select `Dokodemo-Door`. This method uses the Xray core, installed with the official [XTLS installer](https://github.com/XTLS/Xray-install).

<div align=center>

<img width="80%" src="https://github.com/hiddify/hiddify.com/assets/125398461/7cdae822-4fe7-40b1-a2ee-49e7bf555fed" alt="Dokodemo-Door tunnel menu">

</div>

`Install`

1. Wait for the Xray core to be installed on the relay server.
2. Enter the IP address or domain of your main server.
3. Enter **one** port, for example `443`.
4. When you see `Xray installed successfully!`, the tunnel is running.

!!! warning "Very important"
    Enter only one port here, so that its `inbound` (the entry point that listens on that port) is created correctly. To add more ports, such as `80`, use `Add` once for each port.

`Status`

Shows the ports in use and the tunnel status.

`Traffic`

Shows how much traffic each inbound has carried.

`Add`

- Adds another inbound, for another port or another main server.
- Enter the IP address or domain of the main server, then the port.
- When you see `Additional inbound added.`, it worked. Check with `Status`.

`Remove`

Removes one inbound.

`Uninstall`

Removes the Dokodemo-Door tunnel and the Xray core from the relay server.

`Back`

Returns to the main menu.
</details>

<details markdown="1" dir="ltr"><summary><h3>🛠️ HA-Proxy tunnel</h3> (click)</summary>
In the main menu, select `HA-Proxy`.

<div align=center>

<img width="80%" src="https://github.com/hiddify/hiddify.com/assets/125398461/8e94e9d5-6229-46da-afd8-0c1c08787308" alt="HA-Proxy tunnel menu">


</div>

`Install`

1. Wait for the HAProxy package to be installed.
2. In **Relay-Server Free Port**, enter the port users will connect to on the relay (recommended: `443`).
3. Enter the IP address or domain of the main server.
4. Enter the port of the main server (Hiddify Manager uses `443`).
5. When you see `HAProxy tunnel is installed and active.`, the tunnel works.

`Status`

Shows the ports in use and the tunnel status.

`Add`

Adds another relay port and main-server port pair. Use it to add port `80` → `80`.

`Remove`

Removes one of these pairs.

`Uninstall`

Removes the HA-Proxy tunnel from the relay server.

`Back`

Returns to the main menu.

</details>

<details markdown="1" dir="ltr"><summary><h3>🛠️ Socat tunnel (no longer supported)</h3> (click)</summary>
Socat is now under **Options** → **DeprecatedTunnel** → `Socat`. The menu labels it "No longer supported"; prefer one of the methods above.

<div align=center>

<img width="80%" src="https://github.com/hiddify/hiddify.com/assets/125398461/1a7af90d-b8aa-4b5b-84a8-af643e835951" alt="Socat tunnel menu">

</div>

`Install`

1. Wait for the Socat package to be installed.
2. Enter the IP and then the port of the main server.
3. When you see `Socat tunnel is installed and active.`, the tunnel works.

`Status`

Shows the ports in use and the tunnel status.

`Uninstall`

Removes the Socat tunnel from the relay server.

`Back`

Returns to the previous menu.

</details>


<details markdown="1" dir="ltr"><summary><h3>🛠️ WST Tunnel (no longer supported)</h3> (click)</summary>
WST is now under **Options** → **DeprecatedTunnel** → `WST`. The menu labels it "No longer supported"; prefer one of the methods above. It installs an old wstunnel release (v5.0) that exists only for x86-64 (amd64) servers.

<div align=center>

<img width="80%" src="https://github.com/hiddify/hiddify.com/assets/125398461/f9686f53-7a34-4085-9504-15aac82a29ce" alt="WST tunnel menu">

</div>

`Install`

1. Wait for wstunnel to be installed.
2. Enter the port for user traffic (for example `443`), the main server's domain or IP, and the port wstunnel itself should use.
3. Enter the SSH details of the main server (IP, user, SSH port, and password when asked). The script uses them to set up the other end of the tunnel on the main server.
4. When you see `Wstunnel tunnel is installed and active.`, the tunnel works.

`Status`

Shows the ports in use and the tunnel status.

`Uninstall`

Removes wstunnel from both servers. It asks for the main server's SSH details again.

`Back`

Returns to the previous menu.

</details>

<details markdown="1" dir="ltr"><summary><h3>🛠️ Options</h3> (click)</summary>
In the main menu, select `Options` for basic server settings and a connection test.

<div align=center>


<img width="80%" src="https://github.com/hiddify/hiddify.com/assets/125398461/aea50ed9-94a8-4884-92dd-24ef15067253" alt="Options menu">

</div>

`DNS`

Sets the DNS servers the relay server uses. Enter two public DNS servers, for example `8.8.8.8` and `1.1.1.1`.

`Update`

Updates all packages on the server.

`Ping`

Tests whether the server can reach the internet.

`DeprecatedTunnel`

Opens the old Socat and WST tunnels (see above).

`Back`

Returns to the main menu.

</details>


## Next step: add the relay to Hiddify Manager

The tunnel alone is not enough: your panel must also know about the relay, so it can give users configs that use it. Follow [How to add a relay server (domain) to HiddifyManager](/manager/domain-worker-cdn-and-tunneling/How-to-add-relay-domain-to-Hiddify-manager/).
