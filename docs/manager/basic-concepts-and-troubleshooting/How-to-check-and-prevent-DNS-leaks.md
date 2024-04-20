---
title: How to check and prevent DNS leaks
---

# How to check and prevent DNS leaks
One of the most important issues in the Internet world is security and privacy. We daily provide important information through
We exchange information on the Internet, and the leakage of this information outside the network can cause problems. In this article we
We are going to discuss two of these problems namely DNS Leakage and WebRTC Leakage.

## What is DNS leakage?

Normally, your requests are directed to the DNS servers of your Internet Service Provider (ISP), and the ISP
usually send requests to public DNS servers. But when connected to VPN
Yes, these requests are sent to different servers than the ISP servers. A DNS leak occurs when a
A VPN doesn't protect you properly and exposes your DNS requests, browsing history, and perhaps your device's IP address to others
put


## How to test DNS leak
There are many DNS leak testing websites that you can use. In this article, we examine some examples of them.

### 1. DNSleaktest.com website:
Your IP will be displayed on the first page of [this site](https://dnsleaktest.com/) when you log in. A little below that, there are two options Standard Test and Extended Test. In the Standard Test, only the local DNS servers and the DNS server of your Internet company are checked, but in the Extended Test, in addition to the DNS server of your Internet company and local DNS servers, DNS servers around the world are also tested. As a result, Extended Test helps you better examine your DNS traffic while using a VPN. In the image below, we click on the Extended Test option to start the evaluation process.

![1](https://user-images.githubusercontent.com/125398461/235299493-2a0c4aaf-cd24-4723-b7f6-8ed60845734d.jpg)


After the evaluation is complete, if the list of servers displayed in the results section matches the DNS servers of the server provider, you will not have a DNS leak. In simpler terms, if the list of servers shown all match the location of your VPN server, it means that all DNS traffic has passed through your VPN's DNS server and no DNS leaks have occurred. Otherwise you have a DNS leak.

In the image below, as you can see, the list of servers displayed corresponds to the DNS servers of the server provider and the location of our VPN server. So as a result we don't have a DNS leak here.

![2](https://user-images.githubusercontent.com/125398461/235299505-d9fb313b-28b5-473a-b211-a1533bd0add5.jpg)


### 2. Browserleaks.com website
After entering the [DNS Leakage Test](https://browserleaks.com/dns) section, the website will automatically start evaluating and display the results after the evaluation.

In the image below, like the previous site, the list of servers displayed corresponds to the DNS servers of the server provider and the location of our VPN server. So as a result we don't have DNS leak.


![3](https://user-images.githubusercontent.com/125398461/235299510-6b7fb769-3c3a-49e9-b28f-ef59f52e72e6.jpg)


### 3. ipleak.net website
After logging in, [this website](https://ipleak.net) will automatically start the evaluation and display the results after the evaluation.
In the image below, as in the previous site, the displayed server corresponds to the DNS server of the server provider and the location of our CPN server. So, as a result, we do not have a leak.

![4](https://user-images.githubusercontent.com/125398461/235299557-8dac8205-37e8-4a67-bc2e-c6b0ad83b40d.jpg)



### 4. Dnsleaktest.org website
After entering this website, enter the [DNS Leak Test](https://dnsleaktest.org/dns-leak-test) section to start the evaluation automatically. After evaluation, its results are displayed.

![5](https://user-images.githubusercontent.com/125398461/235299689-1efae131-4ca9-4e49-9b15-6f915695c32c.jpg)



In the following image, unlike the previous sites, in addition to the DNS servers of the server provider, there are servers in the list that do not belong to our VPN server and show our real location; So as a result we have a DNS leak.

> Note: It is always recommended to use several different test sites to check your DNS leak to make sure your DNS is not leaking.

(6)


## DNS leak fix
To fix the DNS leak, you can use the following methods:
### 1. Using secure DNS servers:
It is better to use secure and reliable DNS servers such as Google DNS (8.8.8.8, 8.8.4.4) or Cloudflare DNS (1.1.1.1, 1.0.0.1). You can set your DNS servers on these DNSs.

### Setting DNS on Ubuntu server

To fix the dns problem in Ubuntu, you must first edit the settings file. Run this code in the terminal:

```
sudo nano /etc/resolv.conf
```

The text editor opens the settings file for you. You must put the values of the nameservers on the valid dns. Clear all information Add these two lines:

```
nameserver 8.8.8.8
nameserver 1.1.1.1
```

Press ctrl+s to save and ctrl+x to exit.
The work is done!

### 2. DNS settings in the client:
Check that the DNS settings in your client are configured correctly and valid DNS servers are set in it.

### Disable IPv6:
If you do not use IPV6, you can disable it in your system settings. IPV6 may cause DNS Leakage, so disabling it can help solve the problem.

### 4. Using 3rd party programs:
You can use 3rd party applications such as DNSCryptop or `Simple DNS Crypt 'Simple, allowing you to automatically scan your DNS via DNS safe and encrypted servers.


## What is the Webrtc Protocol?
The word stands for web real time communations and means immediate and real-time communication. Webrtc is an open source project that enables real-time media communication such as sound transmission, video and data naturally between browsers and devices, making it possible to communicate from its main web browser without the need for sophisticated plugins or additional hardware. Typically, applications that use WebRTC are browser -based. However, there are independent applications like Facebook Messenger and WhatsApp that use Webrtc.



## What is a Webrtc leak?
- This leakage is a weak point in web browsers such as Chrom, Firefox and Edge, which makes it possible to disclose your actual IP address despite the use of VPN. When you go to a website with a browser, the browser and the site communicate and information exchange occurs. Now, in some cases, that website can bypass the encrypted VPN tunnel and reach your real IP.

## How webrtc leak test
-There are many sites for this test that you can use. Below we will examine an example of them.

### Browserleaks.com

After logging in to [Webrtc Leak Test](https://browserleaks.com/webrtc), the website will automatically evaluate and then show the results.

In the picture below, we see that despite the use of VPN, the real IP address is recognized, so we have a leak.

![7](https://user-images.githubusercontent.com/125398461/235300245-57e4be56-22fb-4030-989b-a5a49f77d533.jpg)


## Fix Webrtc leak

You can use the following methods in your browser to fix the Webrtc leakage in your browser:

### 1. Firefox browser:
Just type the word `about: config` in the URL address bar and hit Inter. Then click on `Accept the Risk and Continue` button. Now type `media.peerconnection.enabled` in the search bar and click on the item displayed again to make it `False`.

### 2. Chrome and Edge browser:
In these browsers, simply use the plugin [`Webrtc Leak Prevent`](https://chrome.google.com/webstore/detail/weak-leak-prevent/eiadekoaikejlgdbkbdFeijlgfdalmlml=en). After installing put `IP Handling Policy` settings on `Disbale non-prxied upd`.

### 3. Safari browser:
If you are using Safari, you can disable Webrtc in the Preferences menu. When you enter it, go to the `Advanced` tab at the bottom and tick `Show Desktop Menu in Bar Menu`. Then click `Develop` and select `Experimental Features`. Find the `Remove Lagacy WebRTC API` option and click it to disable Webrtc.
