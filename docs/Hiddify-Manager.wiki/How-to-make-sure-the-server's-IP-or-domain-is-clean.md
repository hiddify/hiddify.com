
<div dir="rtl" markdown=1>
[**![flag_of_Iran](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://github.com/hiddify/hiddify-config/wiki/%D9%86%D8%AD%D9%88%D9%87-%D8%A7%D8%B7%D9%85%DB%8C%D9%86%D8%A7%D9%86-%D8%A7%D8%B2-%D8%AA%D9%85%DB%8C%D8%B2-%D8%A8%D9%88%D8%AF%D9%86-%D8%A2%DB%8C%D9%BE%DB%8C-%DB%8C%D8%A7-%D8%AF%D8%A7%D9%85%D9%86%D9%87-%D8%B3%D8%B1%D9%88%D8%B1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>
</div>

# How to make sure the server's IP or domain is clean
## 1. Using the site Check-Host
First, check the server's IP or domain on the Check-Host site.

![222417159-c62e65e4-b67c-48ca-9f4b-8f1870276308](https://user-images.githubusercontent.com/125398461/229691501-94fd331f-82ed-4b29-9a84-187fe3b89ee5.png)



After entering the IP or domain in the specified field; You must specify the type of test.

### Ping test
This test is useful when you have created the server for the first time and has nothing installed on it. In this case, you can use this option.

![Screenshot_20230302_151252](https://user-images.githubusercontent.com/125398461/222420082-2a380c2f-803e-4426-a529-8c09b997c76a.png)

If the result of the test was 4/4, it means that the server's IP is most likely clean. Otherwise, you need to change the IP.

### TCP test
This test is used when the operating system is installed and the firewall is active. In this case, you can test the server via the port on which service is running. For example, VPN panels mostly use TCP port 443. Therefore, this port can also be used for testing.

![Screenshot_20230302_153627](https://user-images.githubusercontent.com/125398461/222426843-82605bb3-d51e-407a-8d92-90bddef896ba.png)

If the result of the test was like the picture above, the server's IP is probably without any problems. Otherwise, you need to change the IP.


### UDP test
This test is used when the operating system is installed and the firewall is active. In this case, you can test the server via the port on which service is running. For example, all servers use DNS service, which works on UDP port 53. This port can also be used for testing.

![Screenshot_20230302_154522](https://user-images.githubusercontent.com/125398461/222426567-20464d00-cb53-4d8d-87f3-6ab28a45bce3.png)

If the result is like the image above, it means that the connection is not established on the UDP protocol and it is likely the server's IP is not clean.

## 2. Using the site Host-Tracker
First, open the site [from here](https://www.host-tracker.com/en/ic).

![Screenshot_20230302_155901](https://user-images.githubusercontent.com/125398461/222429170-dbe08724-771e-4910-bbd4-19e3b5bc78f8.png)
Ping and TCP tests can be used to check the IP or domain of the server on this site, which according to the previous explanations, the use of each is clear.

### Ping test

![222430534-01d5f14e-bf3e-421e-93f5-832ac68307ab](https://user-images.githubusercontent.com/125398461/229689843-3d68ac6b-2eeb-4154-a445-23a5f4b24b49.png)

Please note that you have to choose the location based on your region. If the results are all good, it is very likely that your server's IP has no problem.

### TCP test

![222432212-4a496ba1-aa71-4841-949c-449636b94d84](https://user-images.githubusercontent.com/125398461/229689470-005f8fdc-86d6-4ee8-8283-d2c2c5c766f3.png)

If the result was shown as OK, there is a high probability that your server's IP has no problem.

## The story of the yellow list
Why is it that even though the above test was without problems when buying the server and the IP of the server was healthy, but as soon as the panel was installed, after some time the IP is no longer healthy?

Here we get acquainted with a concept called `the yellow list`.

<div align=center markdown=1>
<img width=40% src="https://github.com/hiddify/hiddify-config/assets/125398461/242a64b6-8075-4892-bb0f-de13b158a33a" />
</div>

IPs that have already been used and detected by the filtering system; They are placed in the red list and filtered. Now, when they do not have traffic for a while, they are placed in the yellow list. As soon as their traffic picks up again, they get blocked or slowed down again.

## Final point
Consider a small point. When you install the Hiddify panel, the firewall is turned on by default for added security. Here you should use `tcping` or `http` test to test the IP health, Or turn off the firewall temporarily and do a normal ping test. [More information about configuring the server firewall](https://github.com/hiddify/hiddify-config/wiki/How-to-setup-Firewall-on-Hiddify-panel)