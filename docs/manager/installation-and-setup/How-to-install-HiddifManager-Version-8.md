---
title: How to install HiddifyManager Version 8
---

### Hiddify Manager Version 8 Installation Guide

To install Hiddify Manager Version 8, follow these essential steps:

---

#### **Prerequisites**
1. **Clean Server:**
   - The server must be completely clean with no other versions of the panel or additional scripts installed.

2. **Linux Version:**
   - The server’s operating system must be **Ubuntu 22.04**.

---

#### **Installation Steps**

To install Version 8, execute the following commands in order:

1. **Install pip:**
   ```bash
   pip install python-pip
   ```
   - **Description:** This command installs Python’s package manager (pip), which is required for the subsequent steps. This tool is not pre-installed on many servers.

2. **Install Telegram Library:**
   ```bash
   pip install pyTelegramBotAPI==4.22.0
   ```
   - **Description:** This command installs a specific version of the **pyTelegramBotAPI** library. Hiddify Manager Version 8 is only compatible with this version (4.22.0).

3. **Install Hiddify Manager Version 8:**
   ```bash
   bash <(curl i.hiddify.com/v8.99.0)
   ```
   - **Description:** This command installs the latest release of Hiddify Manager Version 8. It also properly detects and configures the associated database.

---

#### **Important Notes**
- Ensure that the server has no conflicts with other installed versions before executing the commands.
- Follow the steps carefully and in the correct order to avoid errors.

---

By following this guide, Hiddify Manager Version 8 will be correctly installed on your server.

