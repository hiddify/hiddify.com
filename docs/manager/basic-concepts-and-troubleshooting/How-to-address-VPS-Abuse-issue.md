---
title: How to address VPS abuse issue
---

### Resolving Abuse Issues on Virtual Servers

One of the common issues with virtual servers from data centers, especially in the VPN and networking field, is the frequent abuse reports and related warnings. If not managed properly, these issues may lead to account suspension by the data center. To address this problem, the following script is recommended.

---

#### **Script Installation Command**

```bash
bash <(curl -s https://raw.githubusercontent.com/Kiya6955/Abuse-Defender/main/abuse-defender.sh)
```

---

#### **How to Use the Script on Virtual Servers**

1. First, log into your server via **SSH**. If **Hiddify Manager** is installed, exit its menu.

2. Enter the following command to navigate to the server’s root directory:

```bash
cd /
```

3. Execute the script installation command:

```bash
bash <(curl -s https://raw.githubusercontent.com/Kiya6955/Abuse-Defender/main/abuse-defender.sh)
```

4. After running the command and completing the installation, enter the number **1**.

5. The script will begin blocking ranges of IP addresses commonly associated with abuse reports on your server. During this process, the server's firewall will display **two warnings**, which you must approve by selecting **yes** or pressing **Enter**. These confirmations are necessary for the firewall rules to be correctly applied.

6. After approving the two warnings, **two additional questions** will appear. For each, type the letter **y** to ensure the firewall rules are applied successfully.

7. Upon completion, you will be redirected to the script’s main menu.

---

#### **Options Available in the Script Menu**

- **Option 4:** View the applied firewall rules.
- **Option 3:** Manually block a specific range of IP addresses.
- **Option 5:** Remove all firewall rules applied by the script from the server.

---
