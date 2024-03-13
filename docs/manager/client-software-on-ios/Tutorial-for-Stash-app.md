
<div dir="ltr" markdown="1">

# Tutorial for Stash app
This program is written based on Clash for iOS and must be purchased to use it.

## Copy profile to the app
- For this, enter the `iOS` tab in your user panel and open the `Stash` section.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/51f5dfdc-102f-4057-8c0b-33b123d6108b" />
</div>



- Here you can click on the download link from the app store and download the app.

- Here you need to get acquainted with a concept called profile. The profile is a yml file includes all the connections that are enabled in this section. There are two types of profiles.
- Green or `Lite` profile for filtered sites, in which case only filtered sites are passed through the VPN and other sites, including domestic sites, are opened without the VPN, which is a better mode. So you don't need to turn off VPN to open these sites.

- The second mode is the orange or `Normal` profile, which sends all traffic from the VPN to the server. If domestic sites are blocked on the server, they will not be opened, or if WARP is enabled for all traffic, domestic sites will be opened via the WARP.
- Finally, choose one of the two profiles.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/8f93711d-27ec-473c-a1d9-928ee3656abd" />
</div>



## Copy profile to Stash app
- Copy the desired profile from the user page.
- Enter the Stash application, select the `Config File` section on the `Settings` page.
- Select the `Download from URL` option.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/ffbbd7a4-96aa-4331-9987-09f13f46edc8" />
</div>

- Enter the copied link and click `Download`. By doing this, the desired profile will be added to the program.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/84e1e1da-2d09-4b59-ac88-91412746e4ee" />
</div>


## Add profile via QR code
- Click on your desired profile from the user page until the QR code appears.
- Enter the Stash application, select the `Config File` section on the `Settings` page.
- Select `Download from QRcode` option.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/02ca1ecf-3552-4c8e-9a2f-625be8c8b7ac" />
</div>

- Scan the desired QR code to add the profile to the program.


## Policy menu
In this menu, the policies or the configs in the profiles imported to the program are restored and displayed.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/7fd169ea-18b4-4f7f-85b4-ee2073b8c25f" />
</div>


#### Proxy mode
In this case, a special proxy is used, and you can choose the proxy you want. This mode is used for `outbound` in `Global mode`, which is explained below.

#### Automatic mode
In this case, the app automatically connects to the best tested configuration, which is related to the `Rule mode` in `Outbound`.

#### Sequential mode
In this case, the software chooses from different configurations in order. That is, it periodically connects one of the configs. This mode causes asynchronous load distribution, but it is different from the load balance mode, which uses configs simultaneously. This is related to `Rule mode` in `Outbound`.

#### Auto mode
It is related to automatic config selection mode.

#### Load-Balance mode
In this case, it is possible to use several connections at the same time, which spreads the load on several connections and can be useful for times when the IP is dirty and individual connections do not work well. This is also related to `Rule mode` in `Outbound`.

#### Connection test
To do this, click on the lightning icon to test the connection.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/7bdb1519-7179-4c6e-a6e9-ee00c3bc06db" />
</div>

## Update imported profiles
For this, enter `Config File` from the `Settings` menu and hold your finger on one of the profiles. In the menu that appears, click `Update Now`.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/3ecb0ab1-40b9-40e5-8f93-5a37f9b0a1dd" />
</div>

## Automatic update for imported profiles
- For this, select `More Settings` option in `Settings`.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/ab8222a0-b24b-487b-bb62-4c5509d27806" />
</div>


- In the `CONFIG FILE` section of the `Update Interval` field, you can specify the time between automatic updates.
- By activating `Auto Update`, this feature is activated.
- Also, profiles are updated every time you open the Stash app.

## Select the mode in the Outbound section
On the `Home` page of the app and in the `Outbound` section, you can choose three modes.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/51b861c7-2e12-4541-a214-84311270cb8d" />
</div>



#### Rule mode

which uses the policies based on the roles in the profile, that is, if, for example, the Lite profile is in use, using this mode, traffic from domestic sites will not automatically pass through the VPN.

#### Global mode
It is a mode where the roles are no longer executed and you can select one of the configs in the `Policy` menu on the `Proxy mode` so that all the traffic of your phone connects via that config. This mode is useful when you want to use a specific config.

#### Direct mode
In this case, the traffic is not passed through the VPN, it is as if you have turned off the VPN.


## On Demand feature
To use, enter `On Demand` in `Settings`.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/0854f4f3-3628-41a3-a8b4-3a3a08474370" />
</div>


#### Always On

If you enable this option, your filter will always be active.


#### On Demand

If you enable this option, the filter breaker will be active only when the phone screen is not locked and will be turned off at other times.


## Troubleshooting connections

If you need to check more details of the connections, you can enter the `Network Diagnosis` section in the `Utilities` menu. Here, the log is displayed for all connections, which can be useful for troubleshooting. This section contains several subsections that are useful, including `Connectivity` and `Proxy`.

<div align=center markdown=1>
<img width=30% src="https://github.com/hiddify/hiddify-config/assets/125398461/3685baf2-5d0f-4305-a151-12bcc761ab23" />
</div>
