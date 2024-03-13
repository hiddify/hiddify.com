<div dir="rtl" markdown="1">

[**![Lang_farsi](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**]()&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-next/wiki"><img width="100" src="https://github.com/hiddify/hiddify-next/assets/125398461/e285886d-21c6-4208-aeed-ecfd28cd20af" /></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>
</div>
<br>

# URL Scheme
We extend the protocol defined [here](https://web.archive.org/web/20230323111527/docs.cfw.lbyczf.com/contents/urlscheme.html#%E4%B8%8B%E8%BD%BD%E9%85%8D%E7%BD%AE).

## Download configuration

Supports quick import of configuration files using URL Scheme:

```
hiddify://import/<sublink>#name

vmess://....
vless://...
ss://...
trojan://...
```

`<sublink>` is either clash link, singbox link, v2ray sublink, or single proxy link 



<details><summary>deprecated</summary>

```
hiddify://install-sub?url=<encoded v2ray config URI>#<name> 
hiddify://install-config?url=<encoded v2ray config URI>#<name>
hiddify://install-proxy?url=<encoded v2ray proxy share link>#<name>
```
</details>


### Examples:
#### Example Deeplink
```
hiddify://import/https://hiddify.com/autosub#name
hiddify://import/trojan://your_password@aws-ar-buenosaires-1.f1cflineb.com:443#name
```

##### Example Sub link content 
###### v2ray format
```
# http_WS_direct_vless تست 
vless://64177752-4266-4e00-94e3-1b8ececc6623@ip.sslip.io:80?security=none&sni=ip.sslip.io&type=ws&alpn=http/1.1&path=/2LBLzR6NsjNkCN830caotU&host=ip.sslip.io&encryption=none&fp=chrome&headerType=None#http_WS_direct_vless_تست

# http_WS_direct_vmess تست 
vmess://64177752-4266-4e00-94e3-1b8ececc6623@ip.sslip.io:80?security=none&sni=ip.sslip.io&type=ws&alpn=http/1.1&path=/2LBLzR6NsjNkCN830caotU&host=ip.sslip.io&encryption=none&fp=chrome&headerType=None#http_WS_direct_vless_تست


# ssconfig
ssconf://s3.amazonaws.com/beedynconprd/ng4lf90ip01zstlyle4r0t56x1qli4cvmt2ws6nh0kdz1jpgzyedogxt3mpxfbxi.json#BeePass",

# Reality
vless://409f106a-b2f2-4416-b186-5429c9979cd9@54.38.144.4:2053?encryption=none&flow=&fp=chrome&pbk=SbVKOEMjK0sIlbwg4akyBg5mL5KZwwB-ed4eEE7YnRc&security=reality&serviceName=xyz&sid=&sni=discordapp.com&type=grpc#رایگان | REALITY | @EliV2ray | FR🇫🇷 | 0️⃣1️⃣

# Vless
vless://25da296e-1d96-48ae-9867-4342796cd742@172.67.149.95:443?encryption=none&fp=chrome&host=vless.229feb8b52a0e7e117ea76f8b591bcb3.workers.dev&path=%2F%3Fed%3D2048&security=tls&sni=vless.229feb8b52a0e7e117ea76f8b591bcb3.workers.dev&type=ws#رایگان | VLESS | @Helix_Servers | US🇺🇸 | 0️⃣1️⃣

# Vmess
vmess://eyJhZGQiOiI1MS4xNjEuMTMwLjE3MyIsImFpZCI6IjAiLCJhbHBuIjoiIiwiZnAiOiIiLCJob3N0IjoiIiwiaWQiOiJkNDNlZTVlMy0xYjA3LTU2ZDctYjJlYS04ZDIyYzQ0ZmRjNjYiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiIiwicG9ydCI6IjgwODAiLCJzY3kiOiJjaGFjaGEyMC1wb2x5MTMwNSIsInNuaSI6IiIsInRscyI6IiIsInR5cGUiOiJub25lIiwidiI6IjIiLCJwcyI6Ilx1MDYzMVx1MDYyN1x1MDZjY1x1MDZhZlx1MDYyN1x1MDY0NiB8IFZNRVNTIHwgQFdhdGFzaGlfVlBOIHwgQVVcdWQ4M2NcdWRkZTZcdWQ4M2NcdWRkZmEgfCAwXHVmZTBmXHUyMGUzMVx1ZmUwZlx1MjBlMyJ9"

# ss
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp0T3dPeXZsWGlZNUFUSkFVT3BYTlBO@5.35.34.107:55990#%D8%B1%D8%A7%DB%8C%DA%AF%D8%A7%D9%86+%7C+SS+%7C+%40iP_CF+%7C+RU%F0%9F%87%B7%F0%9F%87%BA+%7C+0%EF%B8%8F%E2%83%A31%EF%B8%8F%E2%83%A3"

# TUIC
tuic://3618921b-adeb-4bd3-a2a0-f98b72a674b1:dongtaiwang@108.181.24.7:23450?allow_insecure=1&alpn=h3&congestion_control=bbr&sni=www.google.com&udp_relay_mode=native#رایگان | TUIC | @V2rayCollector | CA🇨🇦 | 0️⃣1️⃣

# Hysteria1
hysteria://host:443?protocol=udp&auth=123456&peer=sni.domain&insecure=1&upmbps=100&downmbps=100&alpn=hysteria&obfs=xplus&obfsParam=123456#remarks",

# Hysteria2
hysteria2://letmein@example.com/?insecure=1&obfs=salamander&obfs-password=gawrgura&pinSHA256=deadbeef&sni=real.example.com

# SSH
ssh://user:pass@server:22/?pk=pk&hk=hk"

# Trojan
trojan://your_password@aws-ar-buenosaires-1.f1cflineb.com:443?host=aws-ar-buenosaires-1.f1cflineb.com&path=%2Ff1rocket&security=tls&sni=aws-ar-buenosaires-1.f1cflineb.com&type=ws#رایگان | TROJAN | @VmessProtocol | RELAY🚩 | 0️⃣1️⃣"

#Wireguard
wg://[server]:222/?pk=[private_key]&local_address=10.0.0.2/24&peer_pk=[peer_public_key]&pre_shared_key=[pre_shared_key]&workers=[workers]&mtu=[mtu]&reserved=0,0,0

```
###### v2ray link format
```
#normal exmaple
hiddify://import/https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/fe3637db4ece53e56ac99ea09dbefa34466f280f/sub/normal/mix

#base64 example
hiddify://import/https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/fe3637db4ece53e56ac99ea09dbefa34466f280f/sub/base64/mix
```
###### Singbox format
```
hiddify://import/https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/fe3637db4ece53e56ac99ea09dbefa34466f280f/singbox/sfasfi/mixLite.json
```
##### Clash format
```
hiddify://import/https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/d6ce7b907eeb58abf503c283af192e7bc915d143/clash/mix.yml
```

# Profile Title:
We use the first item from the following list if it is not empty or null

- "Profile-Title" header 
- "content-disposition" header (described bellow)
- URL Fragment (anything after # in the url)
- the last part of the URL as the configuration file name. Any `.txt` `.json` `.yaml` or `.yml` will be removed

### Response headers
#### Profile-Title
You can use base64 encoded UTF8 name for profile title that allows you to have emoji in profile title 😍
However you use also the ascii name in the header. Example:

```
Profile-Title: base64:SSDinaTvuI8gSGlkZGlmeQ==
```
It will show the profile title as `I ❤️ Hiddify`

```
Profile-Title: I love hiddify
```
It will show the profile title as `I love Hiddify`

#### content-disposition

If the `Profile-Title` is not set for backward compatibility with clash configs we use the value corresponding to `filename` as the configuration file name, otherwise use the last part of the URL as the configuration file name. Any `.txt`, `.yaml` or `.yml` will be removed

```
content-disposition: attachment; filename="abc.txt"
```

#### profile-update-interval

If there is a `profile-update-interval` field in the response header, the configuration file automatic update interval is set to the corresponding value, in hours

```
profile-update-interval: 12
```
 
#### subscription-userinfo

If the `subscription-userinfo` field exists in the response header, its corresponding traffic and expiration information will be displayed in the Profiles module, [specification reference here](https://github.com/crossutility/Quantumult/blob/master/extra-subscription-feature.md)

```
subscription-userinfo: upload=455727941; download=6174315083; totl=1073741824000; expire=1671815872
```

#### profile-web-page-url

If the `profile-web-page-url` field exists in the response header, the `Open web page` option will be displayed in the profile, allowing the user to jump to the corresponding portal home page

#### support-url

If the `support-url` field exists in the response header, the `support` option will be displayed in the profile, allowing the user to jump to the corresponding portal home page

#### moved-permanently-to

If the `moved-permanently-to` field exists in the response header, this will update the subscription url. It is useful when your sublink is blocked or you want to change the domain.


#### DNS

If the `DNS` field exists in the response header, and the user did not set his/her own preferred DNS,  the application will use this DNS server. (In the clash profile this setting can be override)

#### Example

<div align=center>

![image](https://user-images.githubusercontent.com/114227601/230938537-db2b697c-fa58-41fb-a2d7-b11f749d5de8.png)
</div>

In this example:
```
پروفایل یک = <name>
usage=<download>+<upload> (if more than 80% of total :yellow,  more than 100% :red)
total=<total>
روزباقیمانه=relative date of <expire> (if less than 7 days: yellow, less than zero: red)
مشاهده= open browser with <profile-web-page-url>
```

The usage information will be fetched by HEAD option whenever user open the application or every 1 minute (when user is focused in the application)
If any of those fields are empty the corresponding data will not be shown.



# if you can not modify HTTP header (e g. In GitHub)
You can add headers in the first 10 lines of the file with skip characters such as `//` for json  or `#` for Yaml and sub links

E.g.,

```
#profile-title: Hiddify
#profile-title: base64:base64string
#profile-update-interval: 1
#subscription-userinfo: upload=455727941; download=6174315083; total=1073741824000; expire=1671815872
#support-url: https://t.me/hiddify
#profile-web-page-url: https://hiddify.com

```

# Fragment Parameters 
If you want to use Fragment in your links, you have to consider the following parameters 

```
&fragment=size,sleep,hellotls
```

For example, you just need to put the following information in your links

`&fragment=10-100,100-200,hellotls`

# MUX parameter 
If you want to setup Mux parameters in your link

```
mux : "smux/h2mux/yamux"
mux_max : "number" e.g. 6
mux_min : "number" e.g. 2
mux_pad : "true/false"
mux_down : "number in mbps" e.g. 100
mux_up : "number in mbps" e.g. 200

```

Here: 

- `mux` can be one of `smux`, `yamux`, `h2mux`




- `mux_max` is the maximum number of connections.

- `mux_min` is the minimum number of streams.

- `mux_pad` is a true or false parameter which turns on or off this feature on MUX. It Should be the same with the server.

- `mux_down` is the download bandwidth for MUX in mbps. 

- `mux_up` is the upload bandwidth for MUX in mbps. 

Example: `mux=smux&mux_max=4&mux_min=0&mix_pad=false&mux_up=10&mux_down=10`