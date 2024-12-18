---
title: IPv6 Usage Guide
---

### IPv6 Usage Guide

---

#### **What is IPv6?**
IPv6 stands for "Internet Protocol Version 6" and is designed as a replacement for IPv4. Due to its 128-bit addressing, it offers significantly higher security compared to IPv4. In current filtering systems, detecting and limiting IPv6 is costly and challenging, making it virtually unrestricted.

---

#### **Prerequisites for Using IPv6**
1. **Activating IPv6 on the Server:**
   - IPv6 must be enabled by the datacenter. Please contact your server provider to ensure this.

2. **Operator Support:**
   - IPv6 is only supported by certain operators (Irancell and Rightel). It may not be available on others, like Hamrah Aval and Telecommunication Company of Iran, either regionally or entirely.

3. **Valid IPv6 Format:**
   - If IPv6 is enabled on the server, its correct format will be displayed on the homepage of Hiddify Manager after installation. Be sure to note it down for use.

---

#### **Steps to Use IPv6 in the Panel**

##### **Method 1: Direct (Recommended)**
1. In the panel's domain section, click "Create" and set the mode to "Direct" (no intermediary).
2. In Cloudflare, create a record with type **AAAA** and set the server's main IPv6 address to it (proxy off).
3. Enter the subdomain address you created into the domain field and click save.

**Recommended Proxies:**
- HTTP TCP Direct Vmess
- XTLS WS Direct Vless

##### **Method 2: Reality**
1. Create a domain with "Reality" mode in the panel's domain section.
2. In the "Fallback Domain" field, enter your desired address (recommended: www.speedtest.net).
3. In the "Reality Server Name" field, enter the fallback domain or subdomain (recommended: www.speedtest.net).
4. In the "Force to Use..." field, enter the server's IPv6 address in the following format:
   ```
   [IPv6]
   ```

**Recommended Proxies:**
- Reality XTLS Direct Vless

##### **Method 3: Legacy Direct XTLS**
1. Log in to your Cloudflare account.
2. Go to the domain management section and open the DNS menu.
3. Create a DNS record with type **AAAA** and choose a custom name.
4. Save the record.
5. In Hiddify Manager, create a domain with "Legacy Direct XTLS" mode.
6. Enter the subdomain created in Cloudflare into the domain field and save.

**Recommended Proxies:**
- TLS_H2 WS Direct Vless
- TLS WS Direct Vless
- XTLS WS Direct Vless

---

#### **Client Device Configuration for IPv6**

##### **On Android:**
1. Search for "APN" in the mobile settings.
2. Open the default APN and set "Internet Protocol" to "IPv4/IPv6."

##### **On Windows:**
1. Open the Control Panel.
2. Find "Network and Internet Settings" and navigate to "Network and Sharing Center."
3. Click "Change Adapter Settings" from the side menu.
4. Right-click on the connected network, select "Properties."
5. Tick the "Internet Protocol Version 6" checkbox and save.

##### **On iOS:**
1. Visit [this website](https://mobileconfig.azurewebsites.net)
2. Enter "google.com" in the first two fields and check "IPv4/IPv6."
3. Download the generated profile and install it from the "Profile Downloaded" section in mobile settings.
4. Search for "APN" in settings and reset network settings from the bottom of the page.

---

By following these steps, you can fully enable IPv6 functionality.

