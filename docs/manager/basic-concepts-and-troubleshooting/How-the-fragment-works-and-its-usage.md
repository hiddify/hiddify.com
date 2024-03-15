---
title: How the fragment works and its usage
---

<div dir="ltr" markdown="1">

# What is the fragment and how does it work?
Normally, when you want to send a request to open sites and apps to the Internet, SNI may be detected by the filtering system. SNI or server name is actually the main destination of the sent packets that we try to keep hidden from the filtering system with different protocols. But many times it can be detected for various reasons, including the use of weak SNI protocols.

Now the fragment breaks the sent packets into pieces. In this case, SNI is sent in several pieces and thus cannot be detected by the filtering system. And

In the picture below, you can see that the request to open `www.bbc.com` is filtered, and if this request is sent normally, the desired page will probably be blocked by the filtering system and a fake page will be opened for you.

Now, if this request is sent in several pieces, it can bypass this system and after passing through the filtering system, these pieces will join each other on the server.

<div align=center markdown=1>
<img width=70% src="https://github.com/hiddify/hiddify-config/assets/125398461/de4c0b72-cf9b-42a6-a8ea-63990b7f7ddb" />
</div>


## Different fragment modes
#### Default
The fragment is considered based on the default in the config.

#### SNI or domain mode
It splits the packets into two pieces and sends them.

#### Random mode
It transforms the packets into random chunks,that is, the packets are divided into very small pieces and then sends them.


## How to use fragment
Just set the fragment setting in the HiddifyN and HiddifyNG application settings in the advanced menu.