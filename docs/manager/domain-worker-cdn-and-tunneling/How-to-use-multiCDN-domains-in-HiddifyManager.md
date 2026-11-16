---
title: How to manage multiCDN domains in HiddifyManager
---

### Managing Clean IPs and Multiple CDN and AutoCDN Domains in Hiddify Manager  

In this article, we explore strategies for managing clean IPs tailored to different operators and setting up multiple CDN domains in **Hiddify Manager**. These methods optimize configuration and improve connection stability for users. This page is for Hiddify Manager v14.5, where all of this is set in the **Force configs to use these IPs / domains** field of a CDN domain (**Domains** › pencil › **Advanced**). Since v13 there is no separate AutoCDN domain mode: see [How to use AutoCDN IP domain](/manager/domain-worker-cdn-and-tunneling/Guide-for-using-mode-Auto_CDN_IP-on-Hiddify/).  

---

### **Using Clean IPs for Different Operators**  

#### **Step 1: Scanning Clean IPs**  
The easiest way is the panel's own **Scanner** (**Tools** › **Scanner**, or **Open the scanner** under the field): it scans Cloudflare IPs on your internet and saves the best ones in the field, per operator. You can also use other scanners, such as the **Morteza Bashsiz Scanner** (it also has an Android version). See [Guide for finding a clean Cloudflare IP](/manager/domain-worker-cdn-and-tunneling/Guide-for-finding-a-clean-Cloudflare-IP/).  

#### **Step 2: Clean IP Format for Operators**  
To define clean IPs for different operators, write the address (an IP, a range such as `104.16.0.0/24`, or a host name), then the operator's code:  

```plaintext
1.1.1.1 MCI
2.2.2.2 MTN
3.3.3.3 RTL
4.4.4.4 MKH
6.6.6.6 HWB
7.7.7.7 SHT
8.8.8.8 OTHER
```  

Some codes: `MCI` Hamrah Aval, `MTN` Irancell, `RTL` RighTel, `MKH` Mokhaberat (TCI), `HWB` HiWeb, `SHT` Shatel, `AST` Asiatech, `PRS` ParsOnline. For an operator without a code, use its AS number (for example `AS12345`). `OTHER` (or an address with no code) is for every other operator.  

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

#### **Approach 3: One CDN domain with operator codes (AutoCDN)**  

1. **Set Up a Single CDN Subdomain:**  
   ```plaintext
   sub.domain.com (proxy on)  
   ```  

2. **Write per-operator addresses in its Force configs to use these IPs / domains field:**  
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
   Enter three subdomains with distinct clean IPs for different operators in the **Force configs to use these IPs / domains** field.  

4. **Assign Compatible Operator Tags:**  
   Assign operator codes (e.g., MCI, MTN) to each subdomain. Each user then gets, in their configs, the subdomain of their own operator (detected from the IP they update their subscription from, so they should update it with the VPN off).  

---

By applying these methods, you can efficiently manage your domains and IPs in Hiddify Manager, enhancing performance and reliability for your users.

## Related articles

- [What is a CDN and how does it help?](/manager/domain-worker-cdn-and-tunneling/What-is-CDN-and-how-does-it-help-us%3F/)
- [Cloudflare CDN](/manager/domain-worker-cdn-and-tunneling/How-to-use-Cloudflare-CDN/)
- [GCore CDN](/manager/domain-worker-cdn-and-tunneling/How-to-use-GCore-CDN-on-Cloudflare-registered-domain/)
- [Amazon CDN (CloudFront)](/manager/domain-worker-cdn-and-tunneling/How-to-use-Amazon-CDN/)
