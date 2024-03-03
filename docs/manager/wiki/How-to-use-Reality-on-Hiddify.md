
<div dir="rtl" markdown=1>
[**![flag_of_Iran](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](/manager/wiki/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%A7%D8%B3%D8%AA%D9%81%D8%A7%D8%AF%D9%87-%D8%A7%D8%B2-Reality-%D8%AF%D8%B1-%D9%87%DB%8C%D8%AF%DB%8C%D9%81%D8%A7%DB%8C)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/manager/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>

</div>

# How to use Reality on Hiddify
Reality is one of the new protocols provided by Xray, which does not have the prerequisites of the previous protocols. This protocol is based on Vless and therefore cannot be used for Vmess or Trojan. On Hiddify, the emphasis is still on simplification, so most of the work is done behind the scenes.

* Very important point: because this protocol is based on TCP, it does not support CDN, so it can only be used in direct or rail modes, and for this reason, it needs a server with a clean IP. If you need information on how to test the server, refer to [this link](/manager/wiki/How-to-make-sure-the-server's-IP-or-domain-is-clean).


## Reality setup in settings
If you go to the panel settings page and enter the Reality settings, you will see the general settings related to this protocol.
</div>

<div align=center markdown=1>
![](https://github.com/hiddify/hiddify-config/assets/125398461/854639a1-01a3-48d8-be28-1d85b715d6dc)

</div>


These settings include the following.

## Short IDs
This ID is also used for encryption and please do not change it.

## Private key
This key is used to encrypt the connection and please do not change it.

## Public key
This key is also used to encrypt the connection between the server and the client, and please do not change it.
Settings in the domain section

Go to the `Settings` menu, then `Domains`, and click `Create`.

## Mode

Here, set the mode to reality so that you can make specific settings related to this protocol.

> Important note: Before continuing, you can click on the domain review and suggestion link to open the domains review page. Here, the panel offers you several sites based on your server location and sites that have TLS1.3. You can choose the sites that have better ping.


<div align=center markdown=1>
![](https://user-images.githubusercontent.com/125398461/233787191-cd855014-0ab2-4872-bce2-05d1ae705082.png)

</div>


## Fallback Domain 
This domain, which is also known as Diggs such as Fallback or Destination, is used when the filtering system is visiting your website to be directed to this address if it does not have a valid key. You can put one of the addresses of the review page that had a lower ping time in this field, which is the same as the address in the Server Names or SNI field.

You can also put the address of the site that is supposed to be hosted in the country of origin and supports tls1.3 and H2. By doing this, this site actually plays the role of an intermediate server.
## Alias
If you want, enter a custom name to display in the configs.

> Note: It is better to use standard characters such as letters and numbers.

## Reality Server Names
The server name used to simulate the destination of your traffic. You can choose one or more sites from the list on the review page. To use multiple sites, use `,` . Finally, suppose that the sites `www.yahoo.com` and `www.microsoft.com` are in your data center and have a good test result; Put these addresses in this field and leave a comma between them.

To learn how to use multiple server names or SNI, read [this article](https://github.com/hiddify/Hiddify-Manager/wiki/How-to-use-subdomains-of-a-website-in-Reality).

## gRPC
Turn on this button if you need to use gRPC in this protocol.

## Force Config to Use Following IPs
If you want a specific IP instead of the server's main IP in the configuration, enter that IP in this field. One of the uses of this field is for rail servers. If you want to use Reality on Relay servers , you must enter the IP of those servers here.

> Tip: If you have more than a few IPs, you can put each IP in a row and connect between them.

Finally, press save to save the settings and don't forget to `Apply Changes`.

Yellow messages may be given as a result of the server checking your completed fields.

- In Reality, in order not to be recognized, it is better that the selected domain is in your data center, and also note that the server name field and the returned domain must be on the same server.

- That is, you cannot set the return domain to `www.yahoo.com` , but the server name is `www.google.com`. But if you put the name of the server as `blog.yahoo.com`, it is ok.

<div align=center markdown=1>
<img src="https://github.com/hiddify/hiddify-config/assets/125398461/2cf9e13b-8091-4a95-ac30-d5a3f9106a58" />
</div>

Considering the above, it is better to make the settings so that these messages do not appear, but if you did not receive an error message (red) and only received warning messages (yellow warning); You can ignore them and move on.

<div align=center markdown=1>
![](https://user-images.githubusercontent.com/125398461/235890855-5b159244-1e83-4eaf-97d5-fef455168911.png)
</div>



## Enabling or disabling Reality Proxy
For this, go to the proxies menu and view and control Reality proxies in the direct section.


> If you still do not receive its connections in the subscription link despite the Reality options being turned on in this section, check the domain settings used for the subscription link. You probably need to tick the direct domain.

- Important note: because this protocol uses a different algorithm, its settings may be different for different networks, so if you see that it does not work for you, first make sure that your IP server is healthy, and then change the return addresses and the server name. to achieve the desired result.

## Why don't I see these configs in the proxy menu despite enabling the reality protocol?
If you still don't see these connections in the configuration list despite activating the Reality protocol in the proxies section, you need to go to the subscription domain settings and add your direct domain to that domain.
</div>

<div align=center markdown=1>
![](https://github.com/hiddify/hiddify-config/assets/125398461/9269f0ee-78af-4db6-a75d-64ea01f527fc)


</div>


Suppose your subscription domain is `t1.hiddify.com` and your realty domain is `google.com`. You need to go to the `t1.hiddify.com` domain settings and in `Show Configs of Domains` field; Check the `google.com` domain. Now if you open your subscription link on the `t1.hiddify.com` domain; You will see that there are Reality configs.

