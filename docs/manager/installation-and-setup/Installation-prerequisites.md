---
title: Installation prerequisites
weight: -82
---

<div dir="ltr" markdown="1">



# Installation prerequisites

This page lists what you need before you [install Hiddify Manager](/manager/installation-and-setup/guide/): a server, the right operating system, and a way to connect to it.

## 1. A virtual server (VPS)

A **VPS** (virtual private server) is a computer in a data center that you rent and control over the internet. You can get one in several ways:

- **With a credit card or another payment method**, directly from well-known data centers. Search for [inexpensive servers](https://www.google.com/search?q=buy+cheap+and+good+quality+vps+server), or see [our list of providers](https://github.com/hiddify/awesome-freedom/blob/main/vps-providers.md).
- **With cryptocurrency.** Many providers accept it; [search for them](https://www.google.com/search?q=purchase+vps+using+crypto) or check [our list](https://github.com/hiddify/awesome-freedom/blob/main/vps-providers.md), which marks the providers that accept crypto.
- **From Iranian providers**, if you are in Iran ([search](https://www.google.com/search?q=%D8%AE%D8%B1%DB%8C%D8%AF+%D8%B3%D8%B1%D9%88%D8%B1+%D9%85%D8%AC%D8%A7%D8%B2%DB%8C)). The video below (in Persian) shows how to buy a server from Iran.

<div align=center markdown=1>

<a href="https://youtu.be/tcd1wBUR3cY"><img width="50%" src="https://user-images.githubusercontent.com/125398461/229348575-c564efe9-02dc-4b97-bf66-410060934a94.png" alt="Video: how to buy a server from Iran" /></a>

</div>

## 2. Server resources

Suggested minimum:

- 1 GB RAM
- 1 CPU core
- 10 GB storage

If the server has little memory, the installer adds temporary swap space (disk space used as extra memory) during installation.

## 3. Operating system

The server must run **Ubuntu 22.04, 24.04 or 26.04** (amd64/x86_64 or arm64). Ubuntu is a popular version of Linux; its logo looks like this: ![Ubuntu logo](https://img.shields.io/badge/Ubuntu--E95420?style=flat-square&logo=ubuntu)

Ubuntu 20.04 and older, and other Linux distributions, are not supported. Choose a fresh server with nothing else installed on it.

## 4. Ports

Hiddify needs ports **80** and **443** free; nothing else on the server should use them. If your provider has its own firewall, allow at least ports 22 (SSH), 80 and 443.

## 5. SSH access

To run the installation command, you connect to your server over SSH. See [How to connect to the server via SSH](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/).

To make SSH access safer, read:

- [Disable SSH password authentication](/manager/basic-concepts-and-troubleshooting/Disable-SSH-Password-Authentication/)
- [How to change the SSH port on your server](/manager/basic-concepts-and-troubleshooting/How-to-change-SSH-port-on-your-server/)

When you are ready, continue with the [main installation guide](/manager/installation-and-setup/guide/).

</div>
