<div dir="ltr" markdown="1">


# Guide for using mode Auto_CDN_IP on Hiddify
As you know, one of the constant concerns of users when using Cloudflare cdn; Finding clean IPs everyday. We have previously provided tutorials in this regard, which were a step-by-step guide to finding these IPs. You can see it from this link. Many times it is not possible to find these IPs for many reasons. We also provided a solution to solve this problem.

The auto_cdn_ip feature was created to solve this problem for you. Read the description carefully to learn how to set this feature.


## Domain registration in auto_cdn_ip mode
To do this, go to the domains menu and click the create button. The following page will open for you.

![Auto_CDB_IP](https://user-images.githubusercontent.com/125398461/229987959-eab8a7c8-1eec-416d-a543-c6af3385d636.png)

In the following, each part will be explained according to the numbers above.

## 1. Domain
Here you enter your subdomain registered in Cloudflare. It is necessary to explain that the proxy must be turned on. If you need more information about domain registration, see [this link](/manager/wiki/Domain-types-and-how-to-register-them).

## 2. Alias
Using this field you can choose a custom name for this domain. Make sure that the chosen name is not already registered for other domains in the panel. It is better to use standard font characters (letters and numbers) for this field.

## 3. Mode
Set the mode to auto_cdn_ip as specified.

## 4. Force CDN Config to use following IPs  
If this field is empty; It tests the list of clean IPs that are regularly updated by the `ircf.space` site and returns the IP that is on the user's network without problems.

```
mci.ircf.space MCI
mcix.ircf.space MCI
mtn.ircf.space MTN
mtnx.ircf.space MTN
rtl.ircf.space RTL
mkh.ircf.space MKH
hwb.ircf.space HWB
ast.ircf.space AST
sht.ircf.space SHT
prs.ircf.space PRS
mbt.ircf.space MBT
ask.ircf.space ASK
rsp.ircf.space RSP
afn.ircf.space AFN
ztl.ircf.space ZTL
psm.ircf.space PSM
arx.ircf.space ARX
smt.ircf.space SMT
```
Note that there is a space between the subdomain and the network tag, and each row specifies a clean IP for an operator. Rows are separated by spaces.
Also, you can limit the list according to the following format by specifying the desired subdomain and the tag of that network.

```
mcix.ircf.space MCI
mtnx.ircf.space MTN
rtl.ircf.space RTL
```

That is, according to this format, enter the operators you use in field number 4. Separate each row with a space.

If the operator is not in the list; It uses the first line.

Also, if you have a better list of IPs with the previously taught methods, you can use them according to the same format while registering the subdomain (proxy off). For example:

```
mci.yourdomain.com MCI
mtn.yourdomain.com MTN
mkb.yourdomain.com MKB
```
Or you can even enter this list as IP. Suppose the clean IPs for 3 different networks are respectively `1.1.1.1` ; `2.2.2.2` and `3.3.3.3` ; So enter them like this:
```
1.1.1.1 MCI
2.2.2.2 MTN
3.3.3.3 MKB
```
<b><i>Key point: be sure to pay attention; In order for the panel to be able to test and return the correct IP, the VPN connection must be disconnected. So, whenever you change your operator, you have to disconnect the VPN connection and update the connections in the client application so that the test is done and the appropriate IP is set in your connection.</b></i>

## 5. Show Configs of Domains
Using this section, you can limit the configurations of other domains. This field is different for each user and according to different conditions. For non-commercial uses, you usually do not need to use this field in this case.

## 6. Submit
At the end, click the save button to apply the domain settings.

The work is done. Now you can go to the user link and view the configurations related to this domain.