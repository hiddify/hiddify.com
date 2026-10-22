---
title: How to monitor server resources on HiddifyManager
---

<div dir="ltr" markdown="1">


# How to monitor server resources on HiddifyManager

This page shows you how to check your server's CPU (processor), RAM (working memory) and disk space, and what to do when one of them is full. Use it when the panel or the connections become slow, freeze, or stop responding.

## Symptoms

- The panel loads very slowly or does not open.
- Connections become slow or drop, even though the server's IP is clean.
- Installing or updating Hiddify Manager fails with an out-of-memory or "no space left on device" error.

## Likely causes

- A process is using most of the CPU or RAM.
- The disk is full, often because of large log files or old backups.

## Check 1: the dashboard in the panel

The quickest check needs no commands.

1. Log in to your Hiddify panel. The dashboard opens first.
2. Look at the health card of your server (a "node"). It shows CPU use per core, RAM, swap, disk use, load, uptime, network traffic and connections. It also lists the top processes and the largest folders.

<div align=center markdown=1>

![Hiddify panel dashboard](https://github.com/hiddify/hiddify-config/assets/125398461/0e3c9cd4-ea9b-4e0e-83a6-425f4fdc212c)
</div>

!!! note
    The screenshot above is from an older version of the panel. Your dashboard looks different, but it shows the same kind of information.

## Check 2: CPU and RAM with htop

`htop` is a program that shows, live, how much CPU and RAM each running program (each **process**) uses.

Before you start, connect to your server over **SSH** (a secure way to type commands on a remote server). See [How to connect to the server via SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/). If the Hiddify menu opens, press `Cancel` (or `Esc`) to close it. If the menu is still on the screen, type `clear` and press Enter.

1. If `htop` is not installed, install it. Run this on your server, over SSH:

    ```bash
    apt install htop
    ```

    On Ubuntu it is usually installed already.

2. Open `htop`:

    ```bash
    htop
    ```

    <div align=center markdown=1>

    ![htop showing processes](https://user-images.githubusercontent.com/125398461/243195292-38c5ab1f-8fed-49c9-9455-04c7a7e83917.jpg)

    </div>

3. To sort the processes by CPU use, click the `CPU%` column header. The process at the top uses the most CPU.
4. To sort by RAM use, click the `MEM%` column header.
5. To exit `htop`, press `q` (or `Ctrl+C`).

## How to fix it

### A Hiddify service uses too much CPU or RAM

Hiddify's services have names that start with `hiddify-`, for example `hiddify-panel`, `hiddify-xray`, `hiddify-core` and `hiddify-haproxy`. Older guides mention `hiddify-nginx` and `hiddify-singbox`: nginx was removed in v14, and `hiddify-singbox` is now `hiddify-core`.

If one of these services uses most of the CPU or RAM, restart the services. Run this on your server, over SSH:

```bash
hiddify restart
```

You can also run `hiddify` with no options to open the Hiddify menu and choose `restart` with the arrow keys. See [How to connect and troubleshoot via SSH](/manager/configuration-and-advanced-settings/How-to-connect-and-troubleshoot-via-SSH/).

When the restart is done, check that every service is running:

```bash
hiddify status
```

Then open `htop` again and check whether the usage has gone down. If it goes up again soon, ask for help in the [Hiddify Telegram group](https://t.me/hiddify_board).

### RAM looks full

RAM is short-term memory that running programs and the operating system use. Some facts that help you read the numbers:

- How much RAM is used does not depend directly on how many users you have. Hiddify's services and the operating system need memory whether you have 10 users or 1,000.
- Linux uses spare RAM as a **cache** (a temporary copy of files, to make things faster). So RAM use of up to about 80% is normal. You do not need to do anything.
- Do not reboot the server just because RAM looks full.

If you still want to empty the cache, run these commands as the `root` user, on your server, over SSH:

```bash
sync && sysctl -w vm.drop_caches=3
```

If that command gives an error, use this one instead. It also prints the free memory before and after:

```bash
free && sync && echo 3 > /proc/sys/vm/drop_caches && free
```

If your server has very little RAM, adding swap (disk space used as extra memory) can help. See [How to enable Swap on Linux](/manager/basic-concepts-and-troubleshooting/How-to-enable-Swap-on-Linux/).

### The disk is full

1. Check disk space. Run this on your server, over SSH:

    ```bash
    df -h --total
    ```

    You should see a table like this:

    <div align=center markdown=1>

    ![df command output](https://user-images.githubusercontent.com/125398461/248637861-f3552ab5-a105-40b5-8210-65487903c6ba.png)

    </div>

2. Look at the line for your main disk (the one mounted on `/`, often called `sda1` or `vda1`). If `Use%` is close to 100%, free some space.
3. Hiddify keeps its logs in `/opt/hiddify-manager/data/log` (older versions used `/opt/hiddify-manager/log/system`, which no longer exists). To empty all the log files without breaking the services that write to them:

    ```bash
    find /opt/hiddify-manager/data/log -type f -name "*.log" -exec truncate -s 0 {} +
    ```

    Since v14, Hiddify limits its own logs (each log file is emptied when it grows past 100 MB, and the system journal is capped at 500 MB), so logs rarely fill the disk on their own.

4. Hiddify also keeps automatic backups in `/opt/hiddify-manager/data/backup`. If that folder is large, download the backups you want to keep, then delete the old ones. Do not delete the rest of `/opt/hiddify-manager/data`: it holds your database and settings.
5. Run `df -h --total` again to check that space has been freed.

</div>
