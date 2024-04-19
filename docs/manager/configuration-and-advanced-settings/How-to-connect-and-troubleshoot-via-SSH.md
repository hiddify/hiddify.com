---
title: How to connect and troubleshoot via SSH (Working with Hiddify Menu)
weight: -145
---

<div dir="ltr" markdown="1">


<details markdown="1"><summary><h1>Prerequisite: Installing ssh on Windows</h1></summary>
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
- Android: `Termius`
-  Windows: `PowerShell`
- Mac: `Terminal`
- Linux: `Terminal`

Then connect to the server by running the following command: `ssh user@<IP_Address>`

Usually, when you purchase a VPS you get the user ``root'' on the server. suppose your server's IP is 1.1.1.1, so the command is as follows:
```
ssh root@1.1.1.1
```
After connecting to the server, the panel menu will be shown like this.

![Hiddify-Manager](https://github.com/hiddify/hiddify.com/assets/125398461/5b3b47fb-4437-4388-b22d-0d2df6359620)

For more information, each part will be explained separately.

## Cancel 
By selecting cancel, you can exit the menu and reach the normal terminal of the server.

Note: To return to the menu, you must run this command in the terminal.
```
bash /opt/hiddify-config/menu.sh
```
## Status
This menu is used to know the status of the system, if everything is normal, the result should be displayed like this.

![Status](https://github.com/hiddify/hiddify.com/assets/125398461/bb5072e7-635b-486e-9dce-024b8479adb8)

To return to the main menu, you must press the `q` key.

## Admin
This section displays admin links. If you need these links for any reason, use this option.

![Admin](https://github.com/hiddify/hiddify.com/assets/125398461/d15fb764-45b4-40ec-84f2-7dc0ea134f13)

Press a key to return to the main menu.

Most used:
> > > If you installed the panel but forgot to copy the admin links.

## Log
Used to view system logs. After selecting it, you must also select the desired log type.

![Log](https://github.com/hiddify/hiddify.com/assets/125398461/4fa52e34-1f2a-4378-ae1a-881dc81e1269)

For example, if we want to see the logs related to the installation, we can choose the `install-log` option.

![0-install.log](https://github.com/hiddify/hiddify.com/assets/125398461/6a980bbf-9d7a-4ef6-aa92-7a4bfeeb34e3)

Here, the installation logs are displayed as above, at the end of which the system status and admin links are displayed.

Most used:
> > > If one of the services is not working properly and you need to check its log.

# Restart
This option resets all panel services without changing the settings.

![Restart](https://github.com/hiddify/hiddify.com/assets/125398461/d0caf625-9f09-4543-bc22-ae3843bf289a)

You can return to the main menu by pressing any of the buttons on the keyboard.

Most used:
> > > If one of the services is disabled and you need to reset all services at once.

## Apply Configs
This section is used to apply saved settings. After selecting it, the panel will start resetting the values.

![Apply Configs](https://github.com/hiddify/hiddify.com/assets/125398461/76446e31-8efd-4d0e-84b9-a1358887a027)

Press any key to return to the main menu.

Most used:
> > > If you registered changes in the panel, but for any reason you lost web access

## Update
This option is used to update the system. If you select that panel, it will be updated to the latest version available on the project's GitHub. There are three options here as follows.

![Update](https://github.com/hiddify/hiddify.com/assets/125398461/9b24004d-cb44-4137-a573-76eb59d8930a)

### Default
By selecting this option, the program will be updated according to the setting of the web panel.
### Release
By selecting this option, the program will be updated to the latest stable version.
### Develop
By selecting this option, the program will be updated to the latest development version.

In all three cases, you will see something like this in the terminal.

![Develop](https://user-images.githubusercontent.com/125398461/222898474-0d72f442-f19a-40a9-9f35-fcad96807fc4.png)

Most used:
> > > If you lost access during the update through the panel.


### Advanced
This submenu contains several options.

![advanced](https://github.com/hiddify/hiddify.com/assets/125398461/61336508-2dbf-43d8-893c-8d9adbdf3a51)

### add_remote
This option is for when you want to send access to [Hiddifybot](https://t.me/hiddifybot)

### remove_remote
By using this option you can remove SSH access sent to the [bot](https://t.me/hiddifybot)

### Enable
This option is for when you have previously disabled the display of this window and want to re-enable its automatic display at server startup.

### Disable
By selecting this option, the display of this window will be disabled at startup. That is, if the server is restarted, this window will no longer be displayed automatically.

### Uninstall
If you need to remove the installed panel from the server, use this option. Also, keep in mind that this option does not remove all uninstalled items. If you need the server to return to the default settings before installation; It is better to rebuild it.

### Purge
Select this option to completely remove the program and database from the server.
> If this method did not work for you for any reason, you can `Rebuild` the server through your data center. This will delete all server data.
