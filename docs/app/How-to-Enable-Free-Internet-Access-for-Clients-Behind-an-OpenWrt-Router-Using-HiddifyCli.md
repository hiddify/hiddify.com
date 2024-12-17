---
title: How to Enable Free Internet Access for Clients Behind an OpenWrt Router Using HiddifyCli
---

<markdown ="1">

### **Enabling Free Internet Access for Clients Behind OpenWrt Router Using HiddifyCli**

In [another article](/app/How-to-use-HiddifyCli-on-OpenWrt/), we explained how to download and install HiddifyCli on an OpenWrt router. In this article, we will guide you on enabling free internet access for the clients behind that router.

There are two main methods to allow clients behind the router to use free internet:

---

### **1. Using Proxy for Clients Behind OpenWrt Router**

If you want devices connected to the router (like laptops, phones, and other devices) to use the proxy **127.0.0.1:12334**, you can configure the following settings to make this proxy accessible as a central service for the entire network.

---

#### **1.1 Enabling Port Forwarding on the Router**

The proxy **127.0.0.1:2334** configured on the router is, by default, only accessible on the router itself. To allow clients to access it, the port must be opened on the router’s LAN interface.

1. **Add a NAT Rule:**

You need to direct incoming traffic on this port to the proxy:

```bash
iptables -t nat -A PREROUTING -i br-lan -p tcp --dport 2334 -j DNAT --to-destination 127.0.0.1:12334
iptables -A FORWARD -i br-lan -p tcp --dport 12334 -j ACCEPT
```

**Explanation:**
- `br-lan`: The LAN interface of the router.
- `2334`: HiddifyCli proxy port.

2. **Save the Iptables Rules:**

To save and apply the rules after every reboot, run the following command:

```bash
service firewall restart
```

---

#### **1.2 Configuring Proxy Settings on Clients**

Connected devices need to configure **manual proxy settings**. Follow these steps for different platforms:

- **Windows:**
  1. Go to **Settings**.
  2. Navigate to **Network & Internet** > **Proxy**.
  3. Under **Manual proxy setup**:
     - Set **Address** to the router's LAN IP (usually `192.168.1.1`).
     - Set **Port** to `2334`.
  4. Save the settings.

- **Android:**
  1. Go to the Wi-Fi network settings.
  2. Tap the connected network and select **Modify Network** or **Advanced Settings**.
  3. Set **Proxy** to **Manual**:
     - **Proxy hostname**: LAN IP of the router (e.g., `192.168.1.1`).
     - **Proxy port**: `2334`.
  4. Save the settings.

- **iOS:**
  1. Open Wi-Fi settings.
  2. Tap the connected network and set **Configure Proxy** to **Manual**.
  3. Enter the router IP in **Server** and `2334` as the **Port**.
  4. Save the settings.

- **macOS:**
  1. Go to **System Preferences** > **Network**.
  2. Select your current connection and click **Advanced**.
  3. Under the **Proxies** tab, enable **SOCKS Proxy**:
     - **SOCKS Proxy Server**: Router IP (e.g., `192.168.1.1`).
     - **Port**: `2334`.
  4. Save the settings.

---

#### **1.3 Testing Client Connections**

To verify the proxy settings:
- Open a web browser on the client device and attempt to access a website that is otherwise blocked without a proxy.
- If successful, the configuration was applied correctly.

---

#### **1.4 Additional Notes**
- If clients need automatic proxy configuration, you can use a **PAC (Proxy Auto-Configuration)** file and specify it in client settings.

**PAC File URL:**

```
http://192.168.1.1/proxy.pac
```

The PAC file allows you to define routes and exceptions for using the proxy.

---

### **2. Routing All Traffic via Socks5 Proxy in OpenWrt**

To route all internet traffic through **Socks5 Proxy**, you can use tools like `redsocks` or `iptables`. Follow these steps:

---

#### **2.1 Install Required Tools**

First, install the necessary tools. `redsocks` is used to route traffic through the **Socks5 Proxy**.

1. **Update Package List:**

```bash
opkg update
```

2. **Install Redsocks and Additional Tools:**

```bash
opkg install redsocks iptables-mod-nat-extra iptables-mod-tproxy
```

---

#### **2.2 Configure Redsocks**

Create a configuration file for `redsocks` at `/etc/redsocks.conf`:

```bash
nano /etc/redsocks.conf
```

Add the following content:

```plaintext
base {
log_debug = off;
log_info = on;
log = "syslog:daemon";
daemon = on;
user = "nobody";
group = "nogroup";
redirector = iptables;
}

redsocks {
local_ip = 127.0.0.1;
local_port = 12345; # Local port for proxy traffic
ip = 127.0.0.1;     # Socks5 server address
port = 2334;        # Socks5 server port
type = socks5;
}
```

**Explanation:**
- `local_ip` and `local_port`: Redsocks listens here for traffic.
- `ip` and `port`: Address and port of the **Socks5 Proxy**.

---

#### **2.3 Iptables Rules for Traffic Routing**

Create a script named `redsocks-routing` in `/etc/init.d/`:

```bash
touch /etc/init.d/redsocks-routing
chmod +x /etc/init.d/redsocks-routing
```

Add the following content to the script:

```bash
#!/bin/sh /etc/rc.common
START=99
STOP=10

start() {
iptables -t nat -N REDSOCKS
iptables -t nat -A REDSOCKS -d 0.0.0.0/8 -j RETURN
iptables -t nat -A REDSOCKS -d 127.0.0.0/8 -j RETURN
iptables -t nat -A REDSOCKS -d 192.168.0.0/16 -j RETURN
iptables -t nat -A REDSOCKS -d 10.0.0.0/8 -j RETURN
iptables -t nat -A REDSOCKS -p tcp -j REDIRECT --to-ports 12345

iptables -t nat -A OUTPUT -p tcp -j REDSOCKS
iptables -t nat -A PREROUTING -p tcp -j REDSOCKS
}

stop() {
iptables -t nat -F REDSOCKS
iptables -t nat -X REDSOCKS
}
```

Enable and start the script:

```bash
service redsocks-routing enable
service redsocks-routing start
```

---

#### **2.4 Enable Redsocks**

Enable and start `redsocks`:

```bash
service redsocks enable
service redsocks start
```

---

#### **2.5 Reboot the Router**

To apply the changes, reboot the router:

```bash
reboot
```

---

#### **2.6 Verify Routing**

Check if `redsocks` is working:
- Check process status:

```bash
ps | grep redsocks
```

- View system logs:

```bash
logread | grep redsocks
```

---

### **Conclusion**

By following these configurations:
1. **Proxy Method**: Clients behind the router can manually use the proxy for free internet.
2. **Routing Method**: All TCP traffic from the router and connected clients is routed through the **Socks5 Proxy**.

For UDP traffic, additional tools like `dns2socks` or advanced `redsocks` settings may be required.
