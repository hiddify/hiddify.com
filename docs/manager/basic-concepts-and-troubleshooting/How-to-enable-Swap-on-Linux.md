---
title: How to enable Swap on Linux
---

<div dir="ltr" markdown="1">

# How to enable Swap on a Linux VPS

This page shows you how to add **swap** to a Linux server that has none. You can do it while the server is running, without stopping Hiddify.

**Swap** is space on the disk that Linux uses as extra memory when the RAM is full. It is much slower than RAM, but it stops programs from crashing when memory runs out.

## When you need this

- **Symptom:** installing or updating Hiddify Manager stops with `Building the admin UI ran out of memory (needs ~1.2 GB free RAM or swap)`, or services on a small server stop or restart for no clear reason.
- **Likely cause:** the server has little RAM (for example 1 GB) and no swap.
- **Fix:** add a swap file using the steps below, then run the install or update again.

## Before you start

- You can connect to your server over SSH. See [How to connect to the server via SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/).
- The disk has at least a few GB free. This page creates a 2 GB swap file as an example.

## Steps

Run all commands **on your server, over SSH**.

1. Check whether the server already has swap:

    ```bash
    sudo swapon --show
    ```

    If the output is **empty**, there is no swap; continue. If it lists a swap file or partition, you already have swap and do not need this page (you can check its size with `free -h`).

2. Check the free disk space:

    ```bash
    df -h /
    ```

    Look at the **Avail** column. You need more free space than the swap size you want, plus some room to spare.

3. Create a 2 GB file for swap:

    ```bash
    sudo fallocate -l 2G /swapfile
    ```

    If this prints an error such as `fallocate failed: Operation not supported`, use this command instead:

    ```bash
    sudo dd if=/dev/zero of=/swapfile bs=1M count=2048
    ```

    If it says the file already exists, run `sudo swapon --show` again: the file may already be in use.

4. Allow only the system administrator to read the file:

    ```bash
    sudo chmod 600 /swapfile
    ```

5. Prepare the file as swap:

    ```bash
    sudo mkswap /swapfile
    ```

6. Turn the swap on:

    ```bash
    sudo swapon /swapfile
    ```

7. Check that it worked:

    ```bash
    sudo swapon --show
    ```

    **It worked if** you see `/swapfile` with a size of about `2G`.

8. Keep the swap after a reboot by adding it to `/etc/fstab` (the file that lists what Linux turns on at startup). This command adds the line only if it is not there yet:

    ```bash
    grep -q '^/swapfile ' /etc/fstab || echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
    ```

## Notes

- **Size:** pick the swap size based on your server's RAM and free disk space. 2 GB is enough for the Hiddify installer on a small server.
- **Watch usage:** check memory and swap use at any time with `free -h` or `htop`. If swap is always heavily used, the server needs more RAM. See [How to monitor server resources](/manager/basic-concepts-and-troubleshooting/How-to-monitor-server-resources-on-Hiddify/).
- **Some servers cannot use swap.** On some container-based VPS types (such as OpenVZ or LXC), `swapon` fails with `Operation not permitted`. In that case, ask your provider or choose a plan with more RAM.

</div>
