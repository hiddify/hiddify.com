<div dir="rtl" markdown=1>

[**![flag_of_Iran](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://docs.hiddify.com/fa/Hiddify-Manager.wiki/SSH-%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%A7%D8%AA%D8%B5%D8%A7%D9%84-%D8%A8%D9%87-%D8%B3%D8%B1%D9%88%D8%B1-%D8%A7%D8%B2-%D8%B7%D8%B1%DB%8C%D9%82)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>

</div>

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

# How to connect to server via SSH

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

If you have changed the default SSH port, then you should change the above command like this.

```
ssh root@<IP_Address> -p <port_number>
```

For example, if your IP is `1.1.1.1` and the port is `2222`, you should execute the command in this way.

```
ssh root@1.1.1.1 -p 2222
```
