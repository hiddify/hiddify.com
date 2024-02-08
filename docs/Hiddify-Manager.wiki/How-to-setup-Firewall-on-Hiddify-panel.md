<div dir="rtl" markdown="1">

[**![flag_of_Iran](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://github.com/hiddify/hiddify-config/wiki/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%AA%D9%86%D8%B8%DB%8C%D9%85-%D9%81%D8%A7%DB%8C%D8%B1%D9%88%D8%A7%D9%84-%D8%AF%D8%B1-%D9%BE%D9%86%D9%84-%D9%87%DB%8C%D8%AF%DB%8C%D9%81%D8%A7%DB%8C)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>
</div>



# How to setup Firewall on Hiddify panel
## What is a firewall?

Firewall refers to software or hardware that prevent access to computers or servers and control the traffic exchanged in the network. A firewall is actually a security tool that can be a software program or a dedicated network device. Here we are dealing with software firewall on Linux servers.

<div align=center>

![How Firewall works](https://github.com/hiddify/hiddify-config/assets/125398461/2b7c93f0-b868-43c6-8e89-60b36ddb6fb8)

</div>


The firewall of Linux servers can be managed in several ways, one of these methods is using a tool called IP Tables.

In this tool, a series of rules can be defined, by using which information packets are allowed to pass through different protocols.

## Automatic firewall settings through the panel

By default, Hiddify turns on and controls the system firewall. For example, if you change the `TLS` or `HTTP` protocols in the `Settings`, the panel will automatically create the necessary rules for them. Even if you change the `SSH` port, the panel detects the new port and automatically changes the firewall settings according to your needs.

The settings related to the firewall panel can be accessed from the `Settings` section, in the `General Settings` section.

<div align=center>

![Firewall settings](https://github.com/hiddify/hiddify-config/assets/125398461/0a3dce3a-0658-4ecd-887e-bd74c74fea1a)

</div>

Very important advice: Do not turn off the firewall panel. Turning off the firewall compromises your security.

## Manual configuration of server firewall

- If you need to open the port manually, `SSH` to your server first. If you don't know how to `SSH`, [see this tutorial](https://github.com/hiddify/hiddify-config/wiki/How-to-connect-to-server-via-SSH).

- After `SSH` connection, you enter the `Hiddify menu`. Here, exit this menu by pressing `Cancel` or `ctrl+c` to enter the terminal. If the menu is still displayed after this, type the word `clear` and enter.

- Use the following command in the terminal.

```
iptables -A INPUT -p tcp --destination-port PORT -j ACCEPT
```

- Just replace the desired port with `PORT` in the above command. Suppose you want to open port `1234`. Just change the above command like this and enter it in the terminal.

```
iptables -A INPUT -p tcp --destination-port 1234 -j ACCEPT
```


* Although it is not recommended  to open the `ICMP` protocol in terms of security, if you want to provide access to ping or `ICMP` packets; Just run the following command.

<div dir=ltr>

```
iptables -A INPUT -p ICMP -j ACCEPT
```
</div>

* Use the following command to drop the `ICMP ` protocol.

<div dir=ltr>

```
iptables -A INPUT -p icmp -j DROP
```

</div>


- The work is done.


