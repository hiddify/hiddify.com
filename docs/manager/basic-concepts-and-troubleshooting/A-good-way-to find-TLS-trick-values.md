---
title: A Suitable Method for Finding TLS Trick Values and How to Configure Them from HiddifyManager and Hiddify app
---

### A Suitable Method for Finding TLS Trick Values and How to Configure Them from HiddifyManager and Hiddify app

---

In recent months, the use of TLS Trick or Fragment has become a nightmare for filtering systems and firewalls in various countries. Unfortunately, many methods have been restricted, and currently, they only work with some ISPs (Internet Service Providers). However, it is possible to find compatible values for each operator using a scanner through a virtual server (VPS).

---

### Finding Fragment Values

To find suitable fragment values, follow these steps:

1. **Access your virtual server or Tremux** and run the following command:
   ```bash
   bash <(curl -fsSL https://raw.githubusercontent.com/Ptechgithub/FragmentScanner/main/install.sh)
   ```

2. After installing the script, three options will be displayed:
   1. `config to fragment`
   2. `fragment scanner`
   3. `exit`

3. Select **1** to upload your desired configuration for testing.

**Important Note:** The script supports only proxies like `tls`, `grpc`, `vless/vmess/torjan`.

4. After submitting the configuration, the script will display and save the fragment format in `config.json` for use in the next scanning step.

5. Choose option **2** and answer four questions to start scanning:

   - **Question 1:** Number of random fragment values to test (default: 10).
   - **Question 2:** Duration of each test in seconds [Time out] (suggested: 4).
   - **Question 3:** If you want to change the config port, enter the new port or press Enter to use the previous port.
   - **Question 4:** Number of test iterations per value.

6. After responding to these questions, the scan will begin, and the results will be displayed. The top values will be listed first. The provided values include packet type, interval, and length.

---

### Configuring TLS Trick Values in Hiddify Manager

If the top values have `tlshello` packets, you can configure them directly from Hiddify Manager. Otherwise, configurations must be made via the client.

**Recommended Tips:**

- Enable TLS Mixed SNI.
- Disable TLS padding.

To configure these settings, go to the TLS Trick settings section in the panel.

---

### Configuring Values in Hiddify Application

Simply open the app and navigate to All Config Options in the settings. Then, search for `Tls Fragment`, enable it, and set the values accordingly.
