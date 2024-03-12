

# Tutorial for HiddifyClashDesktop software
This software is developed based on Clash and many features are included in it.

## Downloading the software
For this, enter the `Desktop` tab in your user panel and open the section related to `HiddifyClash`.

<div align=center markdown=1>
<img width=80% src="https://github.com/hiddify/hiddify-config/assets/125398461/ae55cc0f-09fe-4569-bcd8-625c68d66fae" />
</div>

You can download the software based on your operating system from the section number 3 indicated in the image above.

## Installing the software

#### Windows
Installing the program is very simple and is completed with a few next steps.

#### Mac
For Mac, you must confirm the program in the privacy section.

#### Linux
For Linux, you only need to give executable access to the downloaded AppImage file and run it.



## Adding a profile to the app
For this, enter the `Desktop` tab in your user panel and open the section related to `HiddifyClash`.

<div align=center markdown=1>
<img width=80% src="https://github.com/hiddify/hiddify-config/assets/125398461/7a1055b3-0313-415b-a00b-2b5301bcd65a" />
</div>


- Here you need to get acquainted with a concept called profile. The profile of a yml file includes all the connections that can be accessed in this section. There are two types of profiles

- Green or lite profile for filtered sites, in which case only filtered sites are passed through the filter breaker and other sites, including Iranian sites, are opened without the filter breaker, which is a better mode. So you don't need to turn off VPN to open these sites.

- The second mode is the orange or normal profile, which sends all traffic from the filter breaker to the server. If Iranian sites are blocked on the server, they will not be opened, or if warp is enabled for all traffic, Iranian sites will be opened with warp.

- Finally, choose one of the two profiles from section number 4.


## Profile
Click on install profile, the profile will be automatically added to the program. You can also import the copied link in the profile section manually in section 1.

<div align=center markdown=1>
<img width=80% src="https://github.com/hiddify/hiddify-config/assets/125398461/3217c5b9-3e18-4bf1-be22-64742e785bbc" />
</div>

In section number 2, the information related to the imported profile, including the expiration date and the total traffic volume and the traffic volume consumed, can be seen.

## Home
In this menu, you can turn the filter breaker on or off with the `Enable anti-censorship` button.

<div align=center markdown=1>
<img width=80% src="https://github.com/hiddify/hiddify-config/assets/125398461/966d10ee-efca-4c33-b15c-cd33fa9f50e1" />
</div>

## Proxy
In this menu, you can specify how to run proxies (configs), which includes 3 main sections.

<div align=center markdown=1>
<img width=80% src="https://github.com/hiddify/hiddify-config/assets/125398461/10db0fa5-9b7a-4ffc-81af-79d8a6448bca" />
</div>

## Rule
This mode executes proxies based on the rules in the imported profile, which contains several sections.

<div align=center markdown=1>
<img width=80% src="https://github.com/hiddify/hiddify-config/assets/125398461/0ecb441a-4270-415e-a09d-3c419f066e48" />
</div>


###### PROXY
This subsection executes the proxies in the profile and connects to the first config that pings.


###### automatic
In this case, it connects to the best configuration that has a lower ping.

###### sequential
In this case, the proxies are connected in turn, that is, the load is divided in a way, but the main difference with Load-balance is that in Load-balance, it is connected to several configurations at the same time, but in this case, it is connected to one configuration at the moment.

###### Sort by location
By using button number 1, you can sort the configurations based on location.

###### Connection test
You can test connections by using button number 2.

#### Global
This mode is for manual configuration selection and is useful when you want to use a specific configuration.

<div align=center markdown=1>
<img width=80% src="https://github.com/hiddify/hiddify-config/assets/125398461/d63a2662-2a02-4141-9a3f-e5befc51aa3b" />
</div>

###### Sort by location
By using button number 1, you can sort the configurations based on location.

###### Connection test
You can test connections by using button number 2.

#### Direct
This mode sends the traffic directly to the Internet and the traffic does not pass through the filter breaker.

<div align=center markdown=1>
<img width=80% src="https://github.com/hiddify/hiddify-config/assets/125398461/8c96c53e-a95c-4af5-bab7-572c0d09c88c" />
</div>

## Settings
In this menu, the general settings of the software are made.

<div align=center markdown=1>
<img width=80% src="https://github.com/hiddify/hiddify-config/assets/125398461/6ab482c8-41fb-4ad0-b37f-6cd88f9426cb" />
</div>

- Button number 1 or TUN Mode is for tunneling the entire system traffic.


> Note: To activate this button, the software must be run with admin access in Windows, i.e. Run as Administrator. It should also be run on Mac and Linux with admin or root access.

- Button number 2 activates the proxy system and is used for software that has proxy capabilities. That is, after activating this button, you should be able to connect to the filter breaker in the proxy section of the software on IP 127.0.0.1 and the default port of the program is 7890.

> This mode is useful when you don't want to pass all your traffic through the VPN.

- Button number 3 or Auto Launch runs the software automatically after the system boots up.

- Button number 4 or Silent Start makes the software run inconspicuously and its icon is displayed in the task bar.

- You can turn off IP version 6 using button number 5.

- In section 6, you can determine the software port, the default of which is 7890.

- In section 7, you can determine the core of the software, the default of which is Clash Meta.

<div align=center markdown=1>
<img width=80% src="https://github.com/hiddify/hiddify-config/assets/125398461/3aedd085-b755-4cbb-a61a-301829b69912" />
</div>

- In section number 8, you can determine the language.

- In section number 9, you can change the theme related to the software.

- The software version can be seen in section 10.


## Connections
In this section, the connections established in the software are displayed. That is, if a program uses a filter, it will be displayed in this section, which is very useful for troubleshooting.

<div align=center markdown=1>
<img width=80% src="https://github.com/hiddify/hiddify-config/assets/125398461/1700bfe0-9a4e-4f4b-ae11-25654d29273b" />
</div>

## Rules
This menu is related to the rules in the imported profile, which can be seen in this file.

<div align=center markdown=1>
<img width=80% src="https://github.com/hiddify/hiddify-config/assets/125398461/72b8c5e1-fca5-4f0a-bad0-2e4738975f24" />
</div>

## Logs
In this section, the log related to the software can be seen, which is very useful during troubleshooting.

<div align=center markdown=1>
<img width=80% src="https://github.com/hiddify/hiddify-config/assets/125398461/deed841f-24f9-452f-b9fb-84301437223a" />
</div>

## Traffic graph
In the specified section below, the graphic related to the traffic passing through the filter breaker is also displayed.

<div align=center markdown=1>
<img width=80% src="https://github.com/hiddify/hiddify-config/assets/125398461/2754c9b1-4072-45d7-8326-c1b86c173686" />
</div>