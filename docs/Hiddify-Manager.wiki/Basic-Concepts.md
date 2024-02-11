<div dir="rtl" markdown="1">

[**![Lang_Farsi](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://docs.hiddify.com/fa/Hiddify-Manager.wiki/%D9%85%D9%81%D8%A7%D9%87%DB%8C%D9%85-%D9%BE%D8%A7%DB%8C%D9%87)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>

</div>

# Basic concepts

Because some of the concepts used in the contents of this wiki and also the world of proxies may be unfamiliar to many people; In this article, we try to explain these things in simple language.

## IP address

An IP address is a unique address that identifies a device on the Internet or local network, and through which the Internet or local network can be accessed. In other words, IP addresses are identifiers that allow sending information between devices in the network; because they contain the geographical location information of the device; Hence, they make devices available to each other to communicate.

We have two IP versions. One IP version 4 and one IP version 6

### IP version 4 or IPv4

IP version 4 consists of sections, each section is separated by a `dot`. For example, w.x.y.z, each of which can be between 0 and 255. Finally, an IP version 4 is like this. `54.78.11.14`

### IP version 6 or IPv6

This IP address is the new version of IPs based on hex or 16 numbers. It consists of 6 sections, each section is separated by `:` An IP version 6 is like this.

`2017:c569:54ed:f141:ec49:0567`
In this version, IPs are reducted in some places. For example, pay attention to the following IP. `2017:c569:0000:0000:0000:0567`
In this version, you can remove the consecutive zeros and take the factor and finally write it like this. `2017:c569::0567`

## HTTP

It is the basic protocol of the Internet and is the foundation of information communication for the web, where documents, including links and texts, are connected to other resources that the user can easily access, for example, with a click or a tap on the screen in a web browser. . This protocol uses a url or web address for addressing, and we call these addresses domains, which are defined below.

The HTTP protocol uses handshaking to send and receive information. In this method, several requests and responses are exchanged between the server and the client to start and end the information exchange operation. Imagine that the client (browser) is a person who intends to receive information about a site. At first, he must send a request to the server of that site. Then he has to wait to receive a response from the server to his request. If the requested information is available on the server, a response will be sent to the person agreeing to send the information. Then again, a message is sent from the client requesting information data to the server. At this stage, the server receives the message and divides the requested data into smaller data packets. Finally, these packets are sent to the person sequentially by the Handshaking protocol. Communication between client and server in this protocol is usually done through port 80.

## HTTPS

This protocol is actually the security version of the HTTP protocol. Because information and data are not encrypted in the HTTP protocol, it can be easily hacked and misused. Based on this, if someone like the internet service provider has access to the information exchange route, he can easily see the information that is being exchanged. But in HTTPS, the information exchanged between the website and the user is encrypted. That is, even if someone can access the information exchanged on the site, they cannot use the content on the other side. Because this information is encrypted and can only be seen by someone who has the key to decrypt it. It uses one of two SSL or TLS protocols to encrypt communications, which will be explained later.

## Domain

In very simple language, in defining what is domain, it should be said that the same address that you enter in your browser to enter any site is the domain. Domains are connected to your website host via IP. Each server is identified by an IP address in the Internet world. IP addresses are defined on your domain through a service called DNS or Domain Name System.

## SSL

This protocol encrypts information using private and public keys. The information encrypted by this protocol is decrypted on the other side. Security in this protocol is maintained at the source and destination of the information, that is, the encryption and decryption process is performed on both sides. Websites that use this protocol to encrypt data usually communicate with clients through the HTTPS protocol. To have a secure HTTPS connection for your site, you need to obtain a valid ssl certificate. In this protocol, the information exchanged between the server and the client is encrypted; Accordingly, this information will not be visible to third parties. Of course, it is still possible to access these data, but due to the fact that they are encrypted, they need to be decrypted to view their data. Decrypting this data is not possible without the key used in the secure communication session. Therefore, this protocol is practically impenetrable.
TLS

It is a security protocol based on the SSL protocol. TLS is an improved version of the SSL protocol, although it has very few differences with SSL, but most of it remains the same. Of course, TLS uses a stronger encryption algorithm than SSL protocol, and TLS is safer and more efficient than SSL in creating public keys and authenticating messages. More precisely, TLS is a protocol used to encrypt web-based communications between a client and a server, using a set of cryptographic algorithms (uTLS, alpn, allowInsecure). Important: "User identification is based on message fields during TLS handshaking."

By analyzing TLS traffic, the filter can guess which website the user is visiting and what the server information is (IP, location, etc.). The things we must do carefully, to use TLS algorithms correctly and the filter cannot see the domain name (SNI).

uTLS: Using the browser's own fingerprint. "To avoid relying on one fingerprint and possible errors, it is recommended to use multiple fingerprints, Randomized."

alpn: Predetermines the conversation protocol between the client and the server, thereby speeding up data loading and TLS encryption.

allowInsecure: prevents the use of fake certificates.

Settings to keep in mind about connections:

`uTLS = Randomized, Chrome. Firefox, etc`

`alpn = H2,HTTP/1.1`

`allowInsecure = false`

Note: The settings of these 3 items can be different according to the type of configuration and the state of the Internet.

## Xray

Hiddify panel uses this platform to pass the filtering system. In fact, Hiddify is recommended by Xray. This platform, which was introduced in 2020, is a modified and better version of the famous V2ray! Due to being more up-to-date and fixing defects, V2ray became the dominant and common platform. In the Xray platform, all v2ray protocols have been added in addition to newer protocols such as Vless.

## Vmess

It was one of the first protocols of the V2ray and Xray subcategory, which encodes and sends information packets based on system time, although this protocol can be detected by the filtering system due to weaknesses in its algorithm, and it is recommended not to use it wherever possible.

## Vless

Vless protocol is a modified version of Vmess! In Vless, all the disadvantages of Vmess have been fixed and due to the difference in encryption in Vless and its lighter weight, it provides the possibility to have more users than vmess on the same server.

## Trojan

This protocol is another safe way to pass through the filtering system. The trojan introduced in 2017 has always been used alongside vless, a powerful protocol to pass through the filtering system.

For more security and speed, we suggest you to use these two protocols, Vless and Trojan. According to the received reports, it is recommended to use these protocols in the following situations

## Reality

REALITY is used instead of TLS and it can eliminate the TLS fingerprint characteristics of the server, still have forward secrecy, etc. Moreover the certificate chain attack is invalid, and the security exceeds that of conventional TLS.
You can point to other websites without having to buy a domain name or configure a TLS server, which is more convenient and realizes the full real TLS of specifying SNI to the middleman.

Note: although Hiddify supports all protocols related to Xray, we suggest using more robust protocols such as Reality, Vless and Trojan like these ones.

`Reality XTLS`

`Vless CDN WS`

`Vless CDN GRPC`

`Vless CDN WS H2`

`Vless CDN GRPC H2`

`Trojan CDN WS`

`Trojan CDN GRPC`

`Trojan CDN WS H2`

`Trojan CDN GRPC H2`
