---
title: How to Reset HiddifyManager to default
weight: -80
---

<div dir="ltr" markdown="1">

# How to Reset HiddifyManager to default
In this article, we are going to teach how to raw the Hiddify panel (complete reset of the panel and database) similar to the initial installation. If you intend to return the Hiddify panel to its initial settings, this tutorial is prepared for you. Follow these steps to the end.

* To begin, first [SSH into your server](/manager/*/*/How-to-connect-to-server-via-SSH).
* Then, by using the combination keys `Ctrl+c` or selecting the `Cancel` button, close the Hidیify menu to access the terminal (command line environment) of your server.

* If after performing these steps, the Hiddify menu is still displayed to you, type the word `clear` and press enter.

> It should be mentioned here that if you need to backup your panel, make a backup of the settings-backup before proceeding.
* Then enter this command in the terminal of your server to completely delete the current database:

```
rm -rf /opt/hiddify-config/hiddifypanel/hiddifypanel.db
```
* Then open the menu again using the following command:

```
bash /opt/hiddify-config/menu.sh
```

* And select `Reinstall` option from the Hiddify menu and wait for the panel to be reinstalled.
* After finishing, you can access the new panel and configure it using the displayed admin links.

In this method, after the re-installation is finished, the panel will be completely retested and similar to the initial installation.

## Fixing common issues
### Solving the problem of reality configs not working
If after entering the subscription link you encounter the problem of reality or ping not working `-1` go to `Advanced settings` and set `TLS` to `1.3` from the following path.

`Settings > Option Setting > v2rayN settings > Enable Security Protocol TLS v1.3 `

<div align=center markdown=1>
![v2raN settings](https://user-images.githubusercontent.com/125398461/251688034-1e0df0d2-508e-4a6a-91da-79a015947fd5.png)

</div>

and finally click `Confirm`.

### Improved performance with unofficial updates

To improve the performance and also update the cores required by the program such as Xray, SingBox, go to the same path as mentioned.

<div align=center markdown=1>
![v2rayN settings](https://github.com/hiddify/hiddify-config/assets/125398461/77180eee-62e9-4a59-8eda-5b9225e6dd87)

</div>

Activate the `Check for pre-release update` option and then update the kernels through the `Check update` option.

<div align=center markdown=1>
![v2rayN settings](https://user-images.githubusercontent.com/125398461/251728362-8ea188b9-e240-48a9-96a8-a1473a9346d3.png)

</div>

### fixing DNS leakage
- For this, you need to activate the `TunMode` option and it is necessary to use the Sing-box core. Therefore, on the main page of the program, download the `Sing-box core` using the `Check update` button.

<div align=center markdown=1>
![Check update](https://user-images.githubusercontent.com/125398461/251811821-c2f94432-0168-40e9-8d8d-43baa2faf0f7.jpg)

</div>

<div align=center markdown=1>
![TunMode settings](https://github.com/hiddify/hiddify-config/assets/125398461/af2b9542-e8b2-49e9-932e-b247ef8dc5af)


</div>

- Then go to the following path.

`Settings > Option Setting > TunMode settings`

- Then enable the `Strict Route` option.
- Set the `Stack` option to `System`.
- Now enable the `TunMode` button from the home screen.
> Note: To activate the `TunMode` button, the program must be opened as `Run as administrator`.
> Note: If `TunMode` does not work for you for any reason, set the `Stack` option on `gvisor`

### Splitting the traffic of domestic websites

If, despite using the `Lite` or green profile prepared in the panel, you need to send the traffic of another site to the destination without going through the filter breaker, you can do it in two ways.

#### Using System proxy settings

To do this, go to this path.

`Settings > Option Setting > v2rayN settings > System proxy settings`

Enter here the addresses you want not to pass through the app. between each address put `;` .

<div align=center markdown=1>
![System proxy settings](https://user-images.githubusercontent.com/125398461/251743253-4c3a9fe5-d641-41e6-8bd1-bd7bfdee19d2.png)

</div>

> Note: Here use `xyz.com` instead of `https://xyz.com` .

#### Using Routing settings

To do this, go to the following path.

`Settings > Routing setting`

<div align=center markdown=1>
![Routing Settings](https://user-images.githubusercontent.com/125398461/251744490-acbd0ec2-104a-4b69-a69b-7f37f35ce5a6.png)

</div>

As you can see, by importing the `Lite` or Green profile, the internal site traffic rules have been added here. If you want to do this mode manually and place your desired sites,

- To do this, turn off `Enable advanced function` option.
- Then select the `direct domain or IP` option.
- You can enter your desired domain. Use `,` to separate multiple sites.
- You can block your desired domains through the `block domain or ip` option.
