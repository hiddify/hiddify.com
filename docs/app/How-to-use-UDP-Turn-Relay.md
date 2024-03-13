<div dir="rtl" markdown="1">

[**![Lang_Farsi](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://github.com/hiddify/hiddify-next/wiki/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%A7%D8%B3%D8%AA%D9%81%D8%A7%D8%AF%D9%87-%D8%A7%D8%B2-UDP-Turn-Relay)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-next/wiki"><img width="100" src="https://github.com/hiddify/hiddify-next/assets/125398461/e285886d-21c6-4208-aeed-ecfd28cd20af" /></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>
</div>

# How to use UDP Turn Relay
Recently, a feature called UDP Turn Relay is used in messengers to bypass filtering. That is, in this case, messengers are used as intermediate servers (relay) and traffic is sent to the main server through them. This can be used for messengers that are active inside Iran and support this protocol, or for foreign messengers that are not filtered. The diagram of free internet connection in this case is as follows.

<div alifn=center>

![UDP Turn Relay_en](https://github.com/hiddify/hiddify-next/assets/125398461/037262d4-ad89-45c0-bcab-c6504c08d3df)
</div>

Note that this feature only works for configurations that are on the UDP protocol. This means that this feature can be used on Hysteria2 or TUIC v5, but it cannot be used for reality.

To use it, just put the parameters of that messenger at the end of your config link according to the command below.

```
relay=urlencoded(turn://user:pass@host:port?realm=t)
```

Where `user` is the username to connect to the protocol in the desired messenger. `pass` is also the password for this account in that messenger. Also, `host` is the host-name for connecting to the messenger, and `port` is the port for connecting to the messenger. The `realm` parameter is related to the authentication area inside the host-name. That is, which area of the messenger can be authenticated with this account.

For example, in Bale messenger (an Iranian Messenger), these parameters are as follows.

```
relay=urlencoded(turn://balelivekit:GygZPHQSgAV7L5L8@meet-turn.bale.sh:443?realm=bale.ai)
```

First, you convert this information to UTF-8 using an Encoder. For example, you can use [this Encoder](https://www.urlencoder.org/), the output of which is as follows:

```
relay=turn%3A%2F%2Fbalelivekit%3AGygZPHQSgAV7L5L8%40meet-turn.bale.sh%3A443%3Frealm%3Dbale.ai
```

Now if we have a hysteria configuration based on UDP as follows:

```
hysteria2://87543215-15ac-54f6-3895-34e4e931f5b4@45.120.34.46:11464?hiddify=1&obfs=salamander&obfs-password=bdgf!huy678559j89GrTu&sni=www.speedtest.net&insecure=1#test
```

Finally, we add the encoded information related to the relay (messenger) at the end of the hysteria link. For this, we first put an `&` and copy the link exactly before `#` as below:

```
hysteria2://87543215-15ac-54f6-3895-34e4e931f5b4@45.120.34.46:11464?hiddify=1&obfs=salamander&obfs-password=bdgf!huy678559j89GrTu&sni=www.speedtest.net&insecure=1&relay=turn%3A%2F%2Fbalelivekit%3AGygZPHQSgAV7L5L8%40meet-turn.bale.sh%3A443%3Frealm%3Dbale.ai#test
```

You can import this link in the Hiddify-Next program and because this program supports the UDP Turn Relay protocol, you can use this feature.

Note: Bale messenger disabled the said feature after a short time. Based on the contents explained above, you should find a messenger that supports this feature from the [list of internal messengers of Iran](https://eservices.ito.gov.ir/Page/IPListMessenger) or non-filtered external messengers.