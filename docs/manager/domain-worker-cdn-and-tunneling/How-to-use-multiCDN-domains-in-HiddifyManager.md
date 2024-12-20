---
title: How to manage multiCDN domains in HiddifyManager
---

### Managing Clean IPs and Multiple CDN and AutoCDN Domains in Hiddify Manager  

In this article, we explore strategies for managing clean IPs tailored to different operators and setting up multiple CDN domains in **Hiddify Manager**. These methods optimize configuration and improve connection stability for users.  

---

### **Using Clean IPs for Different Operators**  

#### **Step 1: Scanning Clean IPs**  
Use the **Morteza Bashsiz Scanner** with the updated **Xray core** to identify clean IPs. For ease of use, an Android version with a user-friendly interface is also available.  

#### **Step 2: Clean IP Format for Operators**  
To define clean IPs for different operators, use the following format:  

```plaintext
1.1.1.1 MCI > Hamrah Aval  
2.2.2.2 MTN > Irancell  
3.3.3.3 RTL > RighTel  
4.4.4.4 MKH > Mokhaberat  
5.5.5.5 SBN > Sabanet  
6.6.6.6 HWB > HiWeb  
7.7.7.7 SHT > Shatel Mobile  
```  

#### **Alternative Methods for Clean IPs**  

1. **Using Cloudflare IPs:**  
   Test IPs using [check-host.net](https://check-host.net). If "Cloudflare" appears in the ISP or Organization field, you can use these IPs for alternative configurations.  

2. **Using the Main Server IP:**  
   Direct server IPs or IPs behind subdomains can work if they perform well with specific operators.  

3. **Using IPv6:**  
   If the operator supports IPv6, this can be an effective solution. Ensure the client settings are adjusted to IPv6/IPv4.  

---

### **Managing Multiple CDN Domains**  

#### **Approach 1: Creating Subdomains with Clean IPs**  

1. **Define CDN Subdomains:**  
   Set up CDN subdomains with the proxy enabled:  
   ```plaintext
   sub1.domain.com (proxy on)  
   sub2.domain.com (proxy on)  
   sub3.domain.com (proxy on)  
   ```  

2. **Assign Clean IPs for Each Operator:**  
   Create subdomains with the proxy disabled for each clean IP:  
   ```plaintext
   mci.domain.com (proxy off)  ==> Clean IP for Hamrah Aval  
   irc.domain.com (proxy off)  ==> Clean IP for Irancell  
   mkb.domain.com (proxy off)  ==> Clean IP for Mokhaberat  
   ```  

3. **Add Subdomains in Hiddify Manager:**  
   Assign each subdomain to its respective operator.  

#### **Approach 2: Using a Second Domain for CDN**  

1. **Set up CDN Subdomains for the First Domain:**  
   ```plaintext
   sub1.domain1.com (proxy on)  
   sub2.domain1.com (proxy on)  
   sub3.domain1.com (proxy on)  
   ```  

2. **Set Clean IP Subdomains for the First Domain:**  
   ```plaintext
   mci.domain1.com (proxy off)  ==> Clean IP for Hamrah Aval  
   irc.domain1.com (proxy off)  ==> Clean IP for Irancell  
   mkb.domain1.com (proxy off)  ==> Clean IP for Mokhaberat  
   ```  

3. **Create CNAME Records for the Second Domain:**  
   ```plaintext
   sub1.domain2.com ==> sub1.domain1.com (proxy off)  
   sub2.domain2.com ==> sub2.domain1.com (proxy off)  
   sub3.domain2.com ==> sub3.domain1.com (proxy off)  
   ```  

#### **Approach 3: AutoCDN with Tags**  

1. **Set Up a Single AutoCDN Subdomain:**  
   ```plaintext
   sub.domain.com (proxy on)  
   ```  

2. **Define Tags for Operators:**  
   ```plaintext
   mci.ircf.space MCI  
   mtn.ircf.space MTN  
   mkh.ircf.space MKH  
   rtl.ircf.space RTL  
   ```  

---

### **Combining Subdomains and Tags for Optimal Configuration**  

To integrate clean IPs with AutoCDN features, follow these steps:  

1. **Create a Subdomain with the Main Server IP (proxy off).**  
2. **Define Multiple Subdomains with Clean IPs for Each Operator:**  
   Ensure that each subdomain is linked to the clean IPs you scanned.  
3. **Set Up a CDN Domain in Hiddify Manager:**  
   Enter three subdomains with distinct clean IPs for different operators in the "Force IP Usage" field.  

4. **Assign Compatible Operator Tags:**  
   Assign operator tags (e.g., MCI, MTN) to each subdomain. This ensures the client scans for the best operator-specific subdomain during configuration.  

---

By applying these methods, you can efficiently manage your domains and IPs in Hiddify Manager, enhancing performance and reliability for your users.
