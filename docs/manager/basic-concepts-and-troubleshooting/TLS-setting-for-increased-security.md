---
title: TLS setting for increased security
---

<div dir="ltr" markdown="1">

# TLS setting for increased security

This page shows you how to make TLS connections that go through a CDN harder to detect. You need it if you use a Cloudflare CDN domain with Hiddify and your connections are unstable on some Internet providers.

**TLS** is the encryption that protects `https` connections. Filtering systems can study patterns in TLS traffic, and older TLS versions show more of these patterns. **TLS 1.3**, the newest version, encrypts more of the connection setup and is harder to recognise.

## Set the minimum TLS version on Cloudflare

**Symptom:** your CDN (Cloudflare) configs connect on some operators but are unstable or don't connect on others.

**Likely cause:** Cloudflare still accepts older TLS versions for your domain.

**Fix:** tell Cloudflare to accept only TLS 1.3.

1. Log in to your Cloudflare account and select your domain.
2. In the menu, open **SSL/TLS**, then **Edge Certificates**.
3. Find **Minimum TLS Version** and set it to **TLS 1.3**.

<div align=center markdown=1>
![The Minimum TLS Version setting in Cloudflare set to TLS 1.3](https://user-images.githubusercontent.com/125398461/243977858-69edd121-028f-43f5-87ca-35cb5be00c0f.png)
</div>

**What to check:** reconnect from a device on the operator that had problems.

**If it still doesn't work:** try a new subdomain. The filtering system may have already detected the old subdomain.

## TLS 1.3 on your device

The **Hiddify app** and other Xray or sing-box based apps have their own built-in TLS. They don't use your operating system's TLS settings, so you normally don't need to change anything on your phone or computer.

Windows 11, macOS and most recent Linux versions already have TLS 1.3 turned on for their own programs.

??? note "Optional: turn on TLS 1.2 and 1.3 in Windows 10 settings"
    This only affects programs that use Windows' built-in TLS. Microsoft does not officially support TLS 1.3 in Windows 10, so this may have no effect. Change the Windows registry only if you know what you are doing.

    1. Open **Notepad** and paste the text below:

        ```ini
        Windows Registry Editor Version 5.00

        [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client]
        "DisabledByDefault"=dword:00000000
        "Enabled"=dword:00000001

        [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server]
        "DisabledByDefault"=dword:00000000
        "Enabled"=dword:00000001

        [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.3\Client]
        "DisabledByDefault"=dword:00000000
        "Enabled"=dword:00000001

        [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.3\Server]
        "DisabledByDefault"=dword:00000000
        "Enabled"=dword:00000001
        ```

    2. Save the file with a `.reg` extension, for example `tls.reg`. In the **Save as type** list, choose **All files** so the file doesn't end in `.txt`.
    3. Double-click the file and confirm the prompts.
    4. Restart your computer.
    5. To check: press `Win+R`, type `regedit` and press Enter. Go to the path shown in the picture below. The TLS versions you turned on are listed there.

    ![The SCHANNEL Protocols keys in the Windows registry](https://user-images.githubusercontent.com/125398461/243984337-53b259f3-267a-4e7f-90b2-8f5ce3a216ca.png)

!!! warning
    Older versions of this page also turned on **SSL 3.0**. SSL 3.0 is old and insecure. If you used that file, delete the `SSL 3.0` key under the same registry path.

</div>
