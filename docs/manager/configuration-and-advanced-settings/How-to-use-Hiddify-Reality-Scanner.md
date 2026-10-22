---
title: How to use Hiddify Reality Scanner
---

# How to use Hiddify Reality Scanner
The Hiddify Reality Scanner helps you find good websites to use as a Reality domain. It tests a list of website names (**SNIs**, the website name a client sends when it opens an encrypted connection) from your own network, and tells you which ones work best. This page is for Hiddify Manager admins who are comfortable running commands on a server and on a computer. For more about the project, see its [Contribution Guidelines](https://github.com/hiddify/Hiddify-Reality-Scanner/blob/main/CONTRIBUTING.md).

!!! warning "This tool is not actively maintained"
    The scanner's last release on PyPI is version 1.8.0, from November 2023. It was written for older Hiddify Manager versions and has not been updated for v13 or v14. It may not work as described here. In Hiddify Manager v14, the **Add domain** wizard also checks whether a website is Reality friendly (TLS 1.3 and HTTP/2), see [How to use Reality on HiddifyManager](/manager/configuration-and-advanced-settings/How-to-use-Reality-on-Hiddify/).

## How it works
The scanner has two parts:

- **Server side**: a temporary test Reality server that runs on your server.
- **Client side**: a Python program that runs on your computer, inside the network you want to test (for example, your home internet in Iran).

## Before you start
- A server you can reach over SSH (see [How to connect to the server via SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/)).
- A computer with [Python](https://www.python.org/downloads/) installed.

!!! warning "Your users lose Xray connections during the test"
    If Hiddify Manager is installed on the same server, the steps below stop the `hiddify-xray` service. While it is stopped, your users' Xray configs don't work. Do the test at a quiet time, and start the service again when you finish (last step of this page).

## Server-side setup
Run these commands on your server, over SSH.

1. Remove any old Xray installed with the official XTLS installer, stop Hiddify's Xray, and install Hiddify's custom Xray core:

    ```bash
    # remove old xray
    bash -c "$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)" @ remove

    # only if you have Hiddify Manager on this server
    systemctl stop hiddify-xray

    # install hiddify custom xray
    bash -c "$(curl -L https://github.com/hiddify/Xray-core-custom/raw/main/install-release.sh)" @ install
    ```

2. Download the scanner's server config and print your test links (one for IPv6, one for IPv4):

    ```bash
    curl -o server_config.json https://raw.githubusercontent.com/hiddify/Hiddify_Reality_Scanner/main/server_config.json

    echo "---------------IPV6---------"
    echo "vless://hiddify@$(curl -6 ip.sb):11443/?fp=chrome&security=reality&pbk=Z84J2IelR9ch3k8VtlVhhs5ycBUlXA7wHBWcBrjqnAw&sid=6ba85179e30d4fc2&sni=www.google.com&type=tcp&flow=xtls-rprx-vision&encryption=none#Hiddify"

    echo "---------------IPV4---------"
    echo "vless://hiddify@$(curl -4 ip.sb):11443/?fp=chrome&security=reality&pbk=Z84J2IelR9ch3k8VtlVhhs5ycBUlXA7wHBWcBrjqnAw&sid=6ba85179e30d4fc2&sni=www.google.com&type=tcp&flow=xtls-rprx-vision&encryption=none#Hiddify"
    ```

    Copy the printed `vless://` link. This is your test config. It looks like this, with your server's IP instead of `SERVER_IP`:

    ```text
    vless://hiddify@SERVER_IP:11443/?fp=chrome&security=reality&pbk=Z84J2IelR9ch3k8VtlVhhs5ycBUlXA7wHBWcBrjqnAw&sid=6ba85179e30d4fc2&sni=www.yahoo.com&type=tcp&flow=xtls-rprx-vision&encryption=none#Hiddify
    ```

3. Start the temporary test server. Leave this window open while you scan:

    ```bash
    xray run -c server_config.json
    ```

    The test server listens on port `11443`. If the scan can't connect, make sure this port is open in your server's firewall.

## Client-side setup
On your computer, open a terminal (Command Prompt or PowerShell on Windows) and install the scanner:

```bash
pip install -U hiddify_reality_scanner
```

## Basic usage
On your computer, run one of these commands. Replace `vless_link` with the test link you copied from the server, and keep the quotes:

```bash
python -m hiddify_reality_scanner "vless_link"
```

or

```bash
hiddify_reality_scanner "vless_link"
```

To stop a scan early, press `Ctrl+C`.

## Advanced usage
To choose which SNIs to test and how many results to keep, run:

```bash
hiddify_reality_scanner --jobs 10 --limit 100 --sni yahoo.com,google.com "vless_link"
```

To test a list of SNIs from a file instead, put the file's path after `--sni`:

```bash
hiddify_reality_scanner --jobs 10 --limit 100 --sni path_to_the_list "vless_link"
```

The options mean:

- `--jobs 10`: how many SNIs to test at the same time. Default: 10.
- `--sni`: the SNIs to test, separated by commas, or the path of a file that lists them.
- `--limit 100`: how many working SNIs to keep in the results. Default: 10.

## Results
The scanner saves its results on your computer, in `results.txt` and `results.json`. Use the best SNIs as Reality domains and server names on your server: see [How to use Reality on HiddifyManager](/manager/configuration-and-advanced-settings/How-to-use-Reality-on-Hiddify/).

## Finish: start Hiddify's Xray again
If Hiddify Manager is installed on the server, stop the test server (press `Ctrl+C` in its window). Then run this on your server, over SSH:

```bash
systemctl start hiddify-xray
```

Check that your users can connect again.
