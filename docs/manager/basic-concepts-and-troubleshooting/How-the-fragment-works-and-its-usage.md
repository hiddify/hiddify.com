---
title: How the TLS Trick works and its usage
---

<div dir="ltr" markdown="1">

# How the TLS Trick works and its usage

## TLS Fragment
Normally, when you want to send a request to open sites and apps to the Internet, SNI may be detected by the filtering system. SNI or server name is actually the main destination of the sent packets that we try to keep hidden from the filtering system with different protocols. But many times it can be detected for various reasons, including the use of weak SNI protocols.

Now the fragment breaks the sent packets into pieces. In this case, SNI is sent in several pieces and thus cannot be detected by the filtering system. And

In the picture below, you can see that the request to open `www.bbc.com` is filtered, and if this request is sent normally, the desired page will probably be blocked by the filtering system and a fake page will be opened for you.

Now, if this request is sent in several pieces, it can bypass this system and after passing through the filtering system, these pieces will join each other on the server.

<div align=center markdown=1>
<img width=70% src="https://github.com/hiddify/hiddify-config/assets/125398461/de4c0b72-cf9b-42a6-a8ea-63990b7f7ddb" />
</div>


#### Different fragment modes
###### Default
The fragment is considered based on the default in the config.

###### SNI or domain mode
It splits the packets into two pieces and sends them.

###### Random mode
It transforms the packets into random chunks,that is, the packets are divided into very small pieces and then sends them.

#### How to use fragment in HiddifyN and HiddifyNG applications

Just set the fragment setting in the HiddifyN and HiddifyNG application settings in the advanced menu.


## The size of the TLS Fragment
This parameter is the size of the fragmented packets. It is recommended that the length be one less than the number of characters in the domain to always ensure that the domain is fragmented.

## TLS Fragment Interval
This option determines the time interval between packets.

## TLS Mixed SNI Case
In this case, domain characters are sent as uppercase, lowercase and uppercase letters (randomly). For example, the domain `www.bbc.com` is sent as `wWw.bBc.cOM` and this can also be effective in bypassing filtering.

## TLS Padding
This option adds a set of random characters to the domain characters and causes filtering to be bypassed.

## Size of TLS Padding
This option determines the size of packets to be added to the domain.

## Determining TLS trick values for HidifyApp
In this application, according to the different conditions, different numbers should be determined for each section, but the following tests have given a relatively good answer:
<div dir=ltr>
 
`TLS Fragment Size: 100-200`

`TLS Fragment Sleep: 10-20`

</div>

**Be careful:**
    > Depending on the operator, you may need to change the parameters.
    > Do not use the TLS fragment and TLS Padding parameters at the same time because they cancel each other out.
