---
title: How to do speed test on server
---

<div dir="ltr" markdown="1">

# How to do speed test on server

In some cases, it is necessary to conduct a speed test on the server to check the conditions more closely and to better diagnose the performance and bandwidth (especially on Iranian servers). Due to the fact that the servers provided by default do not have a graphical user interface (GUI), users do not have access to the browser to perform this test, and they do not know the amount of download and upload of their server, so in this situation, what methods can be used to Did you find out about the stability of the communication port and the bandwidth situation? In this article, we are going to teach how to perform a speed test in the Linux operating system.

## The first method: install and test through the speedtest script

- To start, first [SSH to your server](/manager/installation-and-setup/How-to-connect-to-server-via-SSH/), then use the combination keys `ctrl+c` or select the `Cancel` button to exit the Hiddify menu to access the terminal (command line environment) of your server.

> If the `Hiddify menu` is still displayed after completing the previous steps, type the word `clear` and press enter.

> It should be noted that if you have installed the old `speedtest-cli` script on your server in the past, first remove it using the following command (otherwise, go to the next step).

```
sudo apt-get remove speedtest-cli
```
- To install, run the following commands to download and install the `speedtest` script.

```
sudo apt-get install curl
curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | sudo bash
sudo apt-get install speedtest

```

- After successful installation, enter the following command.

```
speedtest
```

* When you run the program for the first time, the terms and conditions of use, as well as the data collected by the `Speedtest` website, will appear in the form of two messages, for each of which you should enter `yes` as confirmation.

<div align=center markdown=1>
  
![](https://user-images.githubusercontent.com/125398461/243765156-b897f426-e9d6-4f26-b9fb-9e46f6def820.jpg)

</div>

<div align=center markdown=1>

![](https://user-images.githubusercontent.com/125398461/243765299-bab3a3d4-a0c3-478e-8daf-4f3491d44c8b.jpg)


</div>

* After that, you will see that your bandwidth test has been executed and after a short time, its output will be displayed. Whenever you need to re-do this test, just type `speedtest` in the command line and hit enter to re-test.


<div align=center markdown=1>
  
![](https://user-images.githubusercontent.com/125398461/243765887-054e65db-1f12-428b-b9e9-359a69e99044.jpg)

</div>

* In some situations, users need to test from other locations, for this purpose, run the following command to get the list of locations.

```
speedtest --servers
```


<div align=center markdown=1>
  
![](https://user-images.githubusercontent.com/125398461/243766293-c2acefcd-f0f2-43e1-8c90-486b465a7cb4.jpg)

</div>

* As can be seen in the above image, a list of servers with locations close to your server will be displayed to you, in the ID column there is also a 5-digit code for each row, select the desired location for testing and copy its 5-digit code. Then you can use the following command to take a speed test from your desired location, only in the last part replace the ID with the desired code and enter.

```
speedtest --server-id=ID
```

<div align=center markdown=1>
  
![](https://user-images.githubusercontent.com/125398461/243768284-a319cf89-3ed7-4ea5-90dd-0170cd5926c8.jpg)
</div>

## The second method: using the bench.sh tool

* Using the above tool, in addition to testing the speed from different locations, you can easily view the server hardware specifications including CPU, storage space, RAM, processor architecture, network port speed, etc. by running the following command.

```
wget -qO- bench.sh | bash
```

<div align=center markdown=1>
  
![](https://user-images.githubusercontent.com/125398461/243768459-b0815e0e-6348-4c0b-9f82-1ae5e6c53646.jpg)

</div>

* After executing the above command, just wait for a few minutes (about 5 to 8 minutes) until the speed test is taken from several locations in different continents and the results are displayed.
