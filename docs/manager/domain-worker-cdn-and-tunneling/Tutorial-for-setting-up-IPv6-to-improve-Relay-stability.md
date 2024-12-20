---
Title: Using Main Servers' IPV6 for Tunnel Resilience
---

### Using Main Servers' IPV6 for Tunnel Resilience

Using Tunnel with IPv6 for bypassing filtering systems and creating a stable connection has become an effective and popular method. This approach provides high flexibility, especially for relay servers and main servers, and can improve connection quality.

---

### Tunnel Method with IPV6

Using IPV6 can be done in two different ways for connecting between relay servers and main servers:

1. **Creating a local IPV6 on two relay and main servers** and connecting the main server IPV6 to the relay server network.
   
2. **Using the main server's IPV6 on both relay and main servers** and connecting the main server IPV6 to the Iran network. This method requires that both relay servers have IPV6 enabled on their network cards, which can be verified with the `ip a` command in the server's terminal.

**Note:** The best methods for these two approaches are **Gost** and **Decodemodoor**, which have been practically tested.

---

### How to Perform the Process

It doesn’t matter which method you use, for optimal performance, you need to use the relay server mid-scripter on Hiddify Manager.

1. **Review the related mid-scripter article for Hiddify** for installation instructions on the relay server.
   
2. Execute the script installation command, and after installation is complete, the mid-scripter environment will be displayed for you.

![Mid-Scripter Interface](https://github.com/hiddify/hiddify.com/assets/125398461/713801f1-01fb-4bc7-83ca-e1294fa1b149)

This interface contains various tunnel methods and related script settings. Choose either **Gost** or **Decodemodoor**.

3. Select the first option based on your chosen method, then choose **add inbounds** and enter the main server’s IPV6 or local IPV6 in the correct format.

4. After entering the IPV6, proceed to select a port and enter a desired port.

5. Done! Now, log into Hiddify Manager, select the relay option from the domains section, enter Cloudflare, and create a record A with your desired domain and IPV4 server in Iran. Input the subdomain address in the relay domain section and save it.

---

### Suggested Proxies

- http tcp relay vmess
- http httpupgrade relay vmess

These methods can help create a stable and secure connection, especially in filtering conditions.
