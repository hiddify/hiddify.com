---
title: How to set DNS server on HiddifyManager
---

<div dir="ltr" markdown="1">

# How to set DNS server

As you probably know, DNS is a service whose task is to convert names to IPs. That is, when you want to open google.com, for example, this letter is first sent to the DNS server set on your computer. Then that server returns the corresponding IP address to your system. And finally, the request to open the site is sent using IP.

<div align=center markdown=1>
<img width=50% src="https://github.com/hiddify/hiddify-config/assets/125398461/8b1ce774-3268-4c42-ae0a-02553feb3b26" />
</div>

Therefore, it is very important to set up the DNS server on the server and the client and wherever you intend to use Internet services.

## Famous global DNS servers
These servers that serve globally belong to big companies including Google and Cloudflare. It is recommended to use these servers for easy access to your VPN.

`1.1.1.1` related to Cloudflare
`8.8.8.8` related to Google

## Setting DNS server through the Hiddify panel
To do this, go to the panel settings and in the general settings section, put the desired server in the DNS server field. The work is done.

<div align=center markdown=1>
<img src="https://github.com/hiddify/hiddify-config/assets/125398461/1145521a-cfd2-492b-99d0-83559c20ab15" />
</div>


The panel has automatically set the Cloudflare server for you, and of course, it has also put suggestions at the bottom that you can apply if needed.

## Setting DNS server via SSH
If for any reason you wanted to use SSH to do this setup, [connect to your server via SSH](/manager/wiki/How-to-connect-to-server-via-SSH) and then press `ctrl+c` to exit the Hiddify menu.
* In the terminal environment, type this command to open the DNS server settings with the nano text editor.

```
sudo nano /etc/resolv.conf
```
* Then edit nameservers, which refers to the DNS server here, and change it as follows.

```
nameserver 8.8.8.8
nameserver 1.1.1.1
```
* Press `ctrl+s` to save and `ctrl+x` to exit.
* Now you have to make this file cannot be changed by the system. For this, use the following command.

```
chattr +i /etc/resolv.conf
```
* The work is done.

## DNS leak test on server
The easiest tool to test leaks on the server is to use `nslookup`.

- First, if `nslookup` is not installed, install it with this command.

```
sudo apt install dnsutils
```
To test, you must test a domain such as google.com using this tool.

```
nslookup google.com
```
If the output of the command was as follows, it means that the work is done correctly and DNS leak does not happen on the server.
<div align=center markdown=1>
![](https://user-images.githubusercontent.com/125398461/248440247-3ef15d0b-54b0-43ce-8be5-a5229054d1fb.png)
</div>

As you can see, in the `Server` section, the first server, `8.8.8.8`, placed in the settings file, is displayed. Here you should not see anything other than the designated servers. Otherwise, you have to do the above steps correctly again. [Learn more about DNS leaks](https://github-com.translate.goog/hiddify/hiddify-config/discussions/859?_x_tr_sl=fa&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp)