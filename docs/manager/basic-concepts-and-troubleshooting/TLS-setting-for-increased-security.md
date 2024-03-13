<div dir="ltr" markdown="1">

# TLS setting for increased security
Due to the intensity of filtering and the ability to detect patterns of Internet packets on TLS-based protocols, it is necessary to devise measures that prevent this. Here are some solutions for this issue.

## Set the TLS version on CDN

To use CDN-based connections, you need to set the TLS version to the highest setting in your domain settings.

Log in to your `Cloudflare` account and select `SSL/TLS` in the `Domain` section. Then, in `Edge Certificates`, set the minimum TLS version to `TLS 1.3` using the `Minimum TLS Version` field.

<div align=center markdown=1>
![](https://user-images.githubusercontent.com/125398461/243977858-69edd121-028f-43f5-87ca-35cb5be00c0f.png)


</div>

> Please note that if this section is not on the TLS 1.3 option, you may have problems with some operators.

> If you still have problems after changing the TLS version, try a new subdomain, because the previous subdomain may have been detected by the filtering system.

## Enable TLS 1.3 on the client

TLS 1.3 is enabled by default on Windows 11, Mac OS, and most recent versions of Linux. Here's how to enable this version of TLS for Windows 10.

### Enable TLS 1.3 on Windows 10

- First, open a `notepad` file and copy the following registry commands into it.

```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols]

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0]

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0\Client]
"DisableBy Default"=dword:00000000
"Enabled"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0\Server]
"DisabledByDefault"=dword:00000000
"Enabled"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2]

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client]
"DisableBy Default"=dword:00000000
"Enabled"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server]
"DisableBy Default"=dword:00000000
"Enabled"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.3]

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.3\Client]
"DisabledByDefault"=dword:00000000
"Enabled"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.3\Server]
"DisableBy Default"=dword:00000000
"Enabled"=dword:00000001

```
- Now save the file with the `.reg` extension so that it becomes executable.

- Make sure that the file does not have a `.txt` extension.

- Now run it by double clicking on the file.

- The work is done. `TLS 1.3` is enabled on Windows 10. You only need to restart the system once.

- To check the correctness of the work, you can enter the Windows registry. To do this, type `regedit` in `Run` and press enter.

- Now go in the path indicated in the image below. TLS-enabled versions are visible like this.

<div align=center markdown=1>

![](https://user-images.githubusercontent.com/125398461/243984337-53b259f3-267a-4e7f-90b2-8f5ce3a216ca.png)

</div>
