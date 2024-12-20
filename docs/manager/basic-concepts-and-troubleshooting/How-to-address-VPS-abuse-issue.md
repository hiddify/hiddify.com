---
title: How to address VPS abuse issue
---

### Resolving Abuse Issues on Virtual Servers

### Preventing Abuse on Virtual Servers Using Advanced Methods  

Abuse on virtual servers is a common issue in the **VPN** and network field, potentially leading to account suspension by datacenters. This article explores the reasons behind this issue and provides optimized solutions, including proper IP management and the use of the **Abuse Defender** script.  

---

### **The Problem with Direct IP Usage**  
One primary reason for abuse reports is the direct use of Cloudflare clean IPs or IPv6 server IPs or Relay server IPs connected to the main server in the "Force IP Usage" field in the **HiddifyManager**.  

This approach leads to outgoing traffic being sent or received directly and without encryption on the IPs, lacking the protective layer of HTTP/HTTPS. Datacenters often identify such unprotected activity as suspicious, resulting in abuse reports.  

---

### **Proposed Solutions for Managing IPs**  

1. **Using Subdomains:**  
   Place the relevant IPs behind the subdomains of your domain. Then, enter these subdomains in the "Force IP Usage" field.  

2. **Configuring TLS/SSL:**  
   Properly configured TLS/SSL settings in Cloudflare can enhance security and reduce abuse incidents. Ensure these settings are correctly applied.  

---

### **Using the Abuse Defender Script**  
To reduce security risks and prevent abuse caused by suspicious IP ranges, you can use the **Abuse Defender** script. This script helps enforce appropriate firewall rules to block unwanted IP ranges.  

---

#### **Step 1: Installing the Script**  
To install the script, follow these steps:  

```bash
bash <(curl -s https://raw.githubusercontent.com/Kiya6955/Abuse-Defender/main/abuse-defender.sh)
```

---

#### **Step 2: Running the Script**  

1. Log in to your server via **SSH** and exit any applications like **Hiddify Manager**.  

2. Navigate to the root directory:  
```bash
cd /
```

3. Run the installation command:  
```bash
bash <(curl -s https://raw.githubusercontent.com/Kiya6955/Abuse-Defender/main/abuse-defender.sh)
```

4. Once installed, enter **1** to initiate the script, which will start blocking suspicious IP ranges.  

---

#### **Important Notes During Usage**  

- **Firewall Warnings:** The firewall will display two warnings during the process. Press **Enter** or select **yes** to confirm them.  
- **Additional Questions:** Two additional questions will follow. Answer both by entering **y** to ensure firewall rules are applied correctly.  

---

### **Script Menu Features**  

Once the script completes its operation, you’ll see a menu with the following options:  

- **Option 4:** View the applied firewall rules.  
- **Option 3:** Manually block a specific IP range.  
- **Option 5:** Remove all rules applied by the script.  

---

### **Conclusion**  
By implementing these solutions, including proper IP management and the installation of the **Abuse Defender** script, you can significantly enhance the security of your virtual servers and prevent abuse reports from datacenters. These straightforward yet effective actions ensure the stability and performance of your servers.  
