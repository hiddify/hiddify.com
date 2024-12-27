---
title: How to enbale Swap on Linux
---

# How to enable Swap for a Linux VPS Without Interruption

This guide explains how to add Swap memory to a VPS that is currently under load and lacks any Swap. Follow these steps carefully to avoid disruptions.

---

## Step 1: Check Current Swap Status  
First, check the current Swap status:  
<div style="text-align: left; direction: ltr;">

```bash
sudo swapon --show
```

</div>

If the output is empty, it means the server has no active Swap.

---

## Step 2: Check Disk Space  
Ensure there is enough free space on the disk for creating a Swap file. Use the following command:  
<div style="text-align: left; direction: ltr;">

```bash
df -h
```

</div>

---

## Step 3: Create a Swap File  
Create a new Swap file. In this example, we’ll create a 2GB Swap file:  
<div style="text-align: left; direction: ltr;">

```bash
sudo fallocate -l 2G /swapfile
```

</div>

If the above command is not supported, use:  
<div style="text-align: left; direction: ltr;">

```bash
sudo dd if=/dev/zero of=/swapfile bs=1M count=2048
```

</div>

---

## Step 4: Set File Permissions  
Secure the Swap file by restricting access:  
<div style="text-align: left; direction: ltr;">

```bash
sudo chmod 600 /swapfile
```

</div>

---

## Step 5: Configure the File as Swap  
Set the newly created file as a Swap file:  
<div style="text-align: left; direction: ltr;">

```bash
sudo mkswap /swapfile
```

</div>

---

## Step 6: Enable Swap  
Activate the Swap file:  
<div style="text-align: left; direction: ltr;">

```bash
sudo swapon /swapfile
```

</div>

Now verify the Swap status again to ensure it is active:  
<div style="text-align: left; direction: ltr;">

```bash
sudo swapon --show
```

</div>

---

## Step 7: Make Swap Permanent  
To ensure Swap remains active after a reboot, add the Swap file to the `fstab` file:  
<div style="text-align: left; direction: ltr;">

```bash
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

</div>

---

## Final Notes  
- **Appropriate Swap Size**: Choose the Swap size based on your server’s needs and available resources.  
- **Monitor Swap Usage**: After creating the Swap, monitor its usage using tools like `htop` or `free`.  

We hope this guide helps you efficiently manage your server! 😊
