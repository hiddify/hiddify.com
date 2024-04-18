---
title: Quick and easy installation on Vultr Servers
weight: -65
---

<div dir="ltr" markdown="1">

# Quick installation on Vultr Servers


Complete installation training video

In the video below, all the steps, including proxy installation and domain and subdomain settings, are described in full detail. This video is in Farsi and if you watch the steps you can get by that. We are considering making some English videos for non-Persian people. Till then you can visit this or follow the instructions in this article.

For using Vultr site and services please use VPN Connection if you live in countries with sanctions enforced, otherwise your account will be closed.

[![vultr](https://img.youtube.com/vi/hRRg10BURJI/maxresdefault.jpg)](https://www.youtube.com/watch?v=hRRg10BURJI)

# Proxy installation steps

1. At the operating system selection stage, be sure to select Ubuntu 22.04.

2. Copy the code below.

{% include 'cloud_init.yml' %}


3. In the server section, check the Enable Cloud-Init User-Data option and put the copied code in it. After a maximum of 10 to 15 minutes, your proxy will be active.

![Group 1](https://user-images.githubusercontent.com/79760104/221190008-239cd200-4184-4c05-82ea-ff00a47e920e.jpg)

4. Now you need to set the domain. Click on [this link](/manager/installation-and-setup/Guide-for-setting-up-the-domain-and-finalizing-the-installation/) to complete the installation.
