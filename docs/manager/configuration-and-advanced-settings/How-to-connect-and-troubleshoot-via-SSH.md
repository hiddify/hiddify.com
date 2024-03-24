---
title: How to connect and troubleshoot via SSH (Working with Hiddify Menu)
weight: -145
---

<div dir="ltr" markdown="1">

# How to connect and troubleshoot via SSH

<details><summary><h1>Prerequisite: Installing ssh on Windows</h1></summary>
- If your client is Windows; You can use Powershell. First, if you haven't installed the OpenSSH module yet; Open PowerShell with admin access, that is, right-click PowerShell and click Run as Administrator.

![image](https://user-images.githubusercontent.com/114227601/222904592-cd26b3bf-a014-4253-9488-ee9717f006fe.png)

Then run this command:

```
Add-WindowsCapability -Online -Name OpenSSH.Client
```
After that you should see something like this:

![image](https://user-images.githubusercontent.com/114227601/222904870-e709f69e-1a8d-4a6d-ad6a-3d7bdcd917c3.png)

Congratulations, ssh installation is complete.

</details>

# How to connect and troubleshoot via SSH
If for any reason access to the panel is not available through the web or your access is cut off and you do not have the emergency link; In this case, the only way to control and apply changes, as well as restore web access, is through the terminal.

In this case, you need to ssh to the server first.
for this job:
According to your operating system, open one of the following programs
- Windows: `PowerShell`
- Mac: `Terminal`
- Linux: `Terminal`

Then connect to the server by running the following command: `ssh user@<IP_Address>`

Usually, when you purchase a VPS you get the user ``root'' on the server. suppose your server's IP is 1.1.1.1, so the command is as follows:
```
ssh root@1.1.1.1
```
After connecting to the server, the panel menu will be shown like this.

![](https://user-images.githubusercontent.com/125398461/230082495-f2b63ae0-7129-4384-b356-e3c6a94459d6.png)

For more information, each part will be explained separately.

## Cancel 
By selecting cancel, you can exit the menu and reach the normal terminal of the server.

Note: To return to the menu, you must run this command in the terminal.
```
bash /opt/hiddify-config/menu.sh
```
## Status
This menu is used to know the status of the system, if everything is normal, the result should be displayed like this.

![Screenshot_20230304_111551](https://user-images.githubusercontent.com/125398461/222884460-e8f2a7fd-5b24-4c2f-93a4-c4b184f2df78.png)

To return to the main menu, you must press the `q` key.

## Admin
This section displays admin links. If you need these links for any reason, use this option.

![Screenshot_20230304_112037](https://user-images.githubusercontent.com/125398461/222898931-e5cf9dfb-e0f0-4d61-8541-f5db6888c682.png)

Press a key to return to the main menu.

Most used:
> > > If you installed the panel but forgot to copy the admin links.

## Log
Used to view system logs. After selecting it, you must also select the desired log type.

![Screenshot_20230304_111751](https://user-images.githubusercontent.com/125398461/222884675-918601fc-223a-4786-9a45-7287fbb526a6.png)

For example, if we want to see the logs related to the installation, we can choose the `install-log` option.

![Screenshot_20230304_111851](https://user-images.githubusercontent.com/125398461/222884949-50a22e73-3b77-4962-8042-498104dbcf78.png)

Here, the installation logs are displayed as above, at the end of which the system status and admin links are displayed.

Most used:
> > > If one of the services is not working properly and you need to check its log.

# Restart
This option resets all panel services without changing the settings.

![Screenshot_20230304_111723](https://user-images.githubusercontent.com/125398461/222884596-1b8cc61e-619b-4729-b6dd-acd4deb57195.png)

You can return to the main menu by pressing any of the buttons on the keyboard.

Most used:
> > > If one of the services is disabled and you need to reset all services at once.

## Apply Configs
This section is used to apply saved settings. After selecting it, the panel will start resetting the values.

![Screenshot_20230304_111935](https://user-images.githubusercontent.com/125398461/222897786-8173ae47-bcf5-43e7-999c-c0598383b6dc.png)

Press any key to return to the main menu.

Most used:
> > > If you registered changes in the panel, but for any reason you lost web access

## Update
This option is used to update the system. If you select that panel, it will be updated to the latest version available on the project's GitHub. There are three options here as follows.

![Screenshot_20230405_160338](https://user-images.githubusercontent.com/125398461/230083991-e90d579a-5301-49f3-ae5c-645ae5cb6d18.png)

### Default
By selecting this option, the program will be updated according to the setting of the web panel.
### Release
By selecting this option, the program will be updated to the latest stable version.
### Develop
By selecting this option, the program will be updated to the latest development version.

In all three cases, you will see something like this in the terminal.

![Screenshot_20230304_112008](https://user-images.githubusercontent.com/125398461/222898474-0d72f442-f19a-40a9-9f35-fcad96807fc4.png)

Most used:
> > > If you lost access during the update through the panel.

## Install
If you need to reinstall the system, use this option. At the end, the system status and admin links are displayed.

![Screenshot_20230304_111851](https://user-images.githubusercontent.com/125398461/222899750-3392fdde-95b0-4101-9e94-365c3c5c1eb7.png)

To return to the main menu, you must press the `q` key.

Most used:
> > > If during installation one of the scripts is not executed correctly and the panel does not open.

### Submenu
This submenu contains several options.

![Screenshot_20230405_160357](https://user-images.githubusercontent.com/125398461/230084850-c874bcb2-1843-46fb-8b9d-0ae271165dad.png)

### Enable
This option is for when you have previously disabled the display of this window and want to re-enable its automatic display at server startup.

### Disable
By selecting this option, the display of this window will be disabled at startup. That is, if the server is restarted, this window will no longer be displayed automatically.

### Uninstall
If you need to remove the installed panel from the server, use this option. Also, keep in mind that this option does not remove all uninstalled items. If you need the server to return to the default settings before installation; It is better to rebuild it.

### Purge
Select this option to completely remove the program and database from the server.
> If this method did not work for you for any reason, you can `Rebuild` the server through your data center. This will delete all server data.
