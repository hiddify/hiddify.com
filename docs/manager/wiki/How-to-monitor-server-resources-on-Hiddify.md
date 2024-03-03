<div dir="rtl" markdown="1">

[**![flag_of_Iran](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](/manager/wiki/%DA%A9%D9%86%D8%AA%D8%B1%D9%84-%D9%85%D9%86%D8%A7%D8%A8%D8%B9-%D8%B3%D8%B1%D9%88%D8%B1-%D8%AF%D8%B1-%D9%87%DB%8C%D8%AF%DB%8C%D9%81%D8%A7%DB%8C)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/manager/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>
</div>



# How to monitor server resources on Hiddify
Many times you need to check the status of your server's CPU and RAM resources. For example, when there is a regiment. For this purpose, you can monitor these resources in several ways.

## Using the dashboard section in the panel

To know the status of your CPU and RAM usage, go to the dashboard section in the Hiddify panel. Here, various and useful information about the status of system resources as well as network card traffic information and online users can be seen in an integrated manner.

<div align=center markdown=1>
![dashboard](https://github.com/hiddify/hiddify-config/assets/125398461/0e3c9cd4-ea9b-4e0e-83a6-425f4fdc212c)
</div>

## Resource control using the htop tool
One of the tools that can be used to control resources in Linux servers is htop.

- First, connect via [SSH to the server](/manager/wiki/How-to-connect-to-server-via-SSH).

- and exit Hiddify menu by clicking `Cancel` or pressing `ctrl+c` keys at the same time. If the menu is still displayed after this, type the command `clear` and enter.

- Then if htop is not installed on your server, install it through the following command

```
apt install htop
```

> Usually, this program is installed by default on Ubuntu 20.04 and 22.04.

- Then run this command to open `htop`.

```
htop
```

<div align=center markdown=1>
![](https://user-images.githubusercontent.com/125398461/243195292-38c5ab1f-8fed-49c9-9455-04c7a7e83917.jpg)

</div>

From this program, you can see the consumption of your server resources by each process.

- To see the amount of `CPU` consumption of each process, click on the `CPU` to sort accordingly and see which process has allocated a higher percentage of `CPU` to itself.

- Also, to see how much `RAM` is consumed by each process, click on `MEM` to sort accordingly.

- If the most resources are used by Hiddify services (such as hiddify-panel, hiddify-nginx, hiddify-xray, etc.), exit htop.

- To exit the htop environment, you must press `ctrl+c` or `q`.

- Then enter Hiddify menu once through the following command.

```
bash /opt/hiddify-config/menu.sh

```
- Select the `restart` option using the arrow keys (up and down) and wait until the services are restarted and exit the [Hiddify menu](/manager/wiki/How-to-connect-and-troubleshoot-via-SSH) again and check `htop`.

## Free up RAM memory
RAM memory is actually a temporary memory whose space is occupied by running services. Part of the memory is occupied by the operating system itself.

The amount of RAM is not directly related to the number of users on the panel. No matter how many users are defined in the panel, a series of services must be running in order for the operating system and peripheral services to work. Therefore, the number of users on the panel does not have a direct and linear relationship with the amount of RAM, but the running services have a direct relationship with the amount of RAM used.

The operating system is always in charge of managing the server's resources, and if the RAM in your server is filled up to 80%, it is a completely normal thing and you should not worry.

> In Linux servers, do not reboot the system to solve the RAM filling problem.

- One of the ways to improve the server's RAM status is to empty the RAM cache. You can empty the cache with this command in the terminal server when you are logged in as the root user.

```
sync && systemctl -w vm.drop_caches=3
```
> Be sure to log in as the root user and then execute this command.

## Hard disk management
- In addition to Hiddify panel dashboard that displays the status of the hard disk, the following command can also be used in the terminal.

```
df -h --total
```

whose output is as follows.

<div align=center markdown=1>
![](https://user-images.githubusercontent.com/125398461/248637861-f3552ab5-a105-40b5-8210-65487903c6ba.png)

</div>

Here, the space related to `sda1` should be checked according to the figure. If for any reason this space was full and you need to free up some space, you can delete the information related to the logs with the following command.

```
rm-rf /opt/hiddify-config/log/system/*
```

- The work is done