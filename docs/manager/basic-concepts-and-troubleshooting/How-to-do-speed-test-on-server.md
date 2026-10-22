---
title: How to do speed test on server
---

<div dir="ltr" markdown="1">

# How to do speed test on server

This page shows you how to measure your server's download and upload speed from the command line. Use it when your users say the connection is slow and you want to know whether the problem is the server's own bandwidth (how much data its network connection can move per second).

Most servers have no desktop or web browser, so you cannot open a speed-test website on them. Instead, you run a small test program in the server's terminal.

## Before you start

- You can connect to your server over **SSH** (a secure way to type commands on a remote server). If you have never done this, read [How to connect to the server via SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/).
- You are logged in as `root` or as a user who can use `sudo`.

When you log in, the Hiddify menu may open. Press `Cancel` (or `Esc`) to close it and get to the terminal. If the menu is still on the screen, type `clear` and press Enter.

## Method 1: Ookla Speedtest

Speedtest by Ookla is the official command-line version of the speedtest.net website.

1. Only if you installed the old `speedtest-cli` program in the past, remove it first. Run this on your server, over SSH:

    ```bash
    sudo apt-get remove speedtest-cli
    ```

    If it says the package is not installed, that is fine. Go to the next step.

2. Install `curl` and add Ookla's package source:

    ```bash
    sudo apt-get install curl
    curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | sudo bash
    ```

3. Install the `speedtest` program:

    ```bash
    sudo apt-get install speedtest
    ```

4. Run the test:

    ```bash
    speedtest
    ```

5. The first time you run it, it shows the license terms and a note about the data Speedtest collects. Type `yes` and press Enter for each message.

    <div align=center markdown=1>

    ![Speedtest license prompt](https://user-images.githubusercontent.com/125398461/243765156-b897f426-e9d6-4f26-b9fb-9e46f6def820.jpg)

    ![Speedtest data collection prompt](https://user-images.githubusercontent.com/125398461/243765299-bab3a3d4-a0c3-478e-8daf-4f3491d44c8b.jpg)

    </div>

6. Wait a few seconds. You should see the ping, the download speed and the upload speed of your server.

    <div align=center markdown=1>

    ![Speedtest result](https://user-images.githubusercontent.com/125398461/243765887-054e65db-1f12-428b-b9e9-359a69e99044.jpg)

    </div>

To test again later, just run `speedtest` again.

### Test against a specific location

By default, Speedtest picks a test server close to yours. To test against another location:

1. List the nearby test servers:

    ```bash
    speedtest --servers
    ```

    <div align=center markdown=1>

    ![List of Speedtest servers](https://user-images.githubusercontent.com/125398461/243766293-c2acefcd-f0f2-43e1-8c90-486b465a7cb4.jpg)

    </div>

2. In the `ID` column, find the location you want and copy its number.
3. Run the test against that server. Replace `ID` with the number you copied:

    ```bash
    speedtest --server-id=ID
    ```

    <div align=center markdown=1>

    ![Speedtest result for a chosen server](https://user-images.githubusercontent.com/125398461/243768284-a319cf89-3ed7-4ea5-90dd-0170cd5926c8.jpg)

    </div>

## Method 2: the bench.sh script

`bench.sh` is a third-party script. Besides testing speed to several locations around the world, it shows your server's hardware: CPU, disk space, RAM, processor architecture and more.

1. Run this on your server, over SSH:

    ```bash
    wget -qO- bench.sh | bash
    ```

2. Wait about 5 to 8 minutes. The script tests speed from several locations on different continents and then prints the results.

    <div align=center markdown=1>

    ![bench.sh result](https://user-images.githubusercontent.com/125398461/243768459-b0815e0e-6348-4c0b-9f82-1ae5e6c53646.jpg)

    </div>

## What the results mean

- **The speeds are much lower than your hosting plan promises:** the problem is the server or its data center. Contact your hosting provider, or move to another server.
- **The speeds are good, but your users still get slow connections:** the server's bandwidth is not the problem. The slowdown is more likely between your users and the server (for example, filtering or a poor route from their internet provider). See [Troubleshooting connectivity issues](/manager/basic-concepts-and-troubleshooting/Troubleshooting-connectivity-issues-with-HiddifyManager-and-proxies/).

</div>
