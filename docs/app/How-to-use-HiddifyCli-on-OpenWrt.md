---
title: How to use HiddifyCli on OpenWrt  
---

### **Complete Guide to Installing and Setting Up HiddifyCli on OpenWrt**

To install **HiddifyCli** on OpenWrt, follow all the steps below in order. This guide includes downloading, extracting, installing, and full configuration.

---

#### 1. **Download HiddifyCli File**  
To download the version suitable for your router’s architecture, use the following command for direct download:  
<div dir="ltr">  
   ```bash  
   wget -O /tmp/HiddifyCli.tar.gz https://github.com/hiddify/hiddify-core/releases/download/{VERSION}/HiddifyCli-{ARCH}.tar.gz  
   ```  
</div>  
**Explanation:**  
- Replace `{VERSION}` with the desired version (e.g., `v1.0.0`).  
- Replace `{ARCH}` with your router’s architecture (e.g., `mips`, `arm`, or `x86_64`).  

---

#### 2. **Extract the File**  
After downloading, extract the file using the following command:  

<div dir="ltr">  
```bash  
tar -xvzf /tmp/HiddifyCli.tar.gz -C /tmp  
```  
</div>  
**Command Explanation:**  
- `x-` extracts the file.  
- `v-` displays extraction details.  
- `z-` opens gzip-compressed files.  
- `f-` specifies the file name.  
- `/tmp/` is the extraction path (you can replace it with your preferred directory).  

---

#### 3. **Move the Executable to the Appropriate Directory**  
Move the `HiddifyCli` executable file to `/usr/bin/` using:  

<div dir="ltr">  
```bash  
mv /tmp/HiddifyCli /usr/bin/  
```  
</div>  

---

#### 4. **Set Execution Permissions**  
To enable execution for the file, enter the following command:  

<div dir="ltr">  
```bash  
chmod +x /usr/bin/HiddifyCli  
```  
</div>  

---

#### 5. **Create an Init Script**  
To create an automatic service:  
1. Create a file named `HiddifyCli` in `/etc/init.d/`:  

<div dir="ltr">  
   ```bash  
   touch /etc/init.d/HiddifyCli  
   ```  
</div>  

2. Fill the file with the following content:  

<div dir="ltr">  
   ```bash  
   #!/bin/sh /etc/rc.common  
   START=91  
   USE_PROCD=1  

   start_service() {  
       procd_open_instance  
       procd_set_param command /usr/bin/HiddifyCli run -c /root/config.conf  
       procd_set_param stdout 1  
       procd_set_param stderr 1  
       procd_set_param respawn  
       procd_close_instance  
   }  
   ```  
</div>  

3. Set the file permissions:  

<div dir="ltr">  
   ```bash  
   chmod 755 /etc/init.d/HiddifyCli  
   ```  
</div>  

---

#### 6. **Enable and Start the Service**  
Run the following commands to enable and start the service:  

<div dir="ltr">  
```bash  
service HiddifyCli enable  
service HiddifyCli start  
```  
</div>  

---

#### 7. **Configure the Settings**  
1. **Extract the Configuration from Hiddify Desktop App:**  
   - Set up your desired configurations in the app.  
   - Export the config and save it as a text file.  
   - Rename the file extension to `.conf` (e.g., `config.conf`).  

2. **Move the Config File to `/root/` on the Router:**  

<div dir="ltr">  
   ```bash  
   mv config.conf /root/  
   ```  
</div>  

---

#### 8. **Reboot the Router**  
Restart the router to apply the changes:  

<div dir="ltr">  
```bash  
reboot  
```  
</div>  

After rebooting, the HiddifyCli service will be active, and the **Socks5 Proxy** will be available at:  

<div dir="ltr">  
```plaintext  
127.0.0.1:12334  
```  
</div>  

---

### Additional Notes:  
- To check the router’s architecture, run the following command:  

<div dir="ltr">  
  ```bash  
  uname -m  
  ```  
</div>  

- If any issues arise during the process, check the service logs using:  

<div dir="ltr">  
  ```bash  
  logread | grep HiddifyCli  
  ```  
</div>  
