---
title: Tutorial for Streisand
---

<div dir="ltr" markdown="1">


# Tutorial for Streisand
This application is one of the free apps for iOS that can be installed on iOS versions 14 and later.


## Download the application

To install the application, you can download and install it [here](https://apps.apple.com/us/app/streisand/id6450534064).

## Add subscription link

There are 2 ways to do this.

### Copy the subscription link

* For this, go to your user panel and open the section related to `auto` in the section of `All Configs`.


<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/09e30aeb-7c73-4235-ab0d-64c1c446f6d2" />

</div>



* Now you can `Copy` the QR code.


<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/eb4d7cf9-4f1f-4910-acc8-1c7d545ee1eb" />

</div>


* Enter the software and press the `+` button.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/78fe4b65-d7f7-4d16-b185-82f8dd67a135" />

</div>

* Then the subscription is added to the software and the configurations are loaded.

### Scan the subscription link
* You can scan the QR code instead of copying the subscription link.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/80eb44cc-aa77-4417-8943-11d055ace933" />

</div>


* Click the `+` button in the software and click the `Scan QRCode` option and scan the QR code.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/58c97e17-3cfa-4c40-9b2d-01de70b1e40d" />

</div>

* Then the subscription is added to the software and the configurations are loaded.

## Subscription settings

To do this, tap and hold on the subscription added to the software. The following options will appear.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/52954cdf-5c76-4fbe-8adb-8371d7fa6747" />

</div>


### Latency
Calculates the amount of delay related to the configurations.
### TCP Ping
It takes TCP ping test from configs.
### ICMP Ping
It takes a normal pinning test from the configs.

> Note: The difference between normal ping test and TCP ping is in the type of protocol used.

### Update
Use this option to update your subscription.

### Edit
Use this option to edit the subscription link.
### Delete
Use this option to delete the subscription.
## DNS Settings
On the main page of the software, there are settings related to DNS, by entering it, you can adjust it and change the server and the type of protocol used.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/152bbbd5-a8a5-4a31-836a-7c2ea7ab3940" />

</div>


### DoH

It is a protocol that provides DNS over HTTPS. It means that DNS requests are sent in web format.
### DoT

In this protocol, DNS requests are sent based on the TCP protocol.
### DoU

In this protocol, DNS requests are sent based on the UDP protocol.

## Settings
On this page, there are general settings of the software, which will be explained later.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/989d8fce-4858-4bd1-b5fb-44c4bdac3895" />

</div>

### Import Configuration
Use this option to add the configuration file from the device manually.

### Export Configuration
This option can be used to transfer the imported configuration from the device to another device.

### Subscription
By activating the `Update On Open` option, the subscription will be updated automatically when the software is opened.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/068a0d24-c0f5-4cfd-9fa0-e37eb50acf20" />

</div>

### Reset
In this section, you can reset the settings related to the application.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/8b336b0b-0c57-49e7-89e4-f86317955061" />

</div>

## Fragment activation
To activate the fragment on TLS connections, you need to click on the connection on this app and activate the Fragment option.
The following parameters are suggested to be specified in the relevant fields.

<div align=center markdown=1>
<img src="https://github.com/hiddify/Hiddify-Manager/assets/125398461/055f8437-0bfa-45ce-96e4-f7cbd0026c4c" width="30%" />

</div>

<div dir=ltr markdown=1>
`packets: tlshello`

`length: 100-200`

`Interval: 10-20`

</div>

Depending on the operator, you may need to change the parameters or change the type of packets from tlshello to ``tcp segment 1-3'' mode. Of course, this condition may be detected earlier.
`packets: 1-3`