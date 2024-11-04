---
title: How to install different versions of Hiddify Manager
weight: -75
---

<div dir="ltr" markdown=1>

# How to install different versions of HiddifyManager
As you know, Hidify Manager is offered in three versions as follows:

* **Develop version:**

This version is a version of the software that is being developed to create the latest features. This version may have bugs, so it is better to install it on test servers.

* **Beta version:**
  
This version is a version after the version under development, and in fact it is the version before the final release, in which part of the bugs have been fixed and it has new features.

* **Release version:**

This version is actually the final version of the software that was released after the final tests and is the most stable version possible. See this figure for a better understanding.

<div align=center markdown=1>
  
![install versions](https://github.com/hiddify/Hiddify-Manager/assets/125398461/6528a2c5-f938-48c3-a88f-f829d7e3a481)

</div>

## Install Release version
* Before installing, if you have already installed another version of the panel, take a backup of the panel. [Read more...](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/)
* Now just run the following one-line command in the terminal.

```
bash <(curl https://i.hiddify.com/release)
```

* After installation, just restore your backup. [Read more...](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/)


## Install Beta version
* Before installing, if you have already installed another version of the panel, take a backup of the panel. [Read more...](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/)
* Now just run the following one-line command in the terminal.

```
bash <(curl https://i.hiddify.com/beta)
```

* After installation, just restore your backup. [Read more...](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/)


## Install Develop version
* Before installing, if you have already installed another version of the panel, take a backup of the panel. [Read more...](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/)
* Now just run the following one-line command in the terminal.

```
bash <(curl https://i.hiddify.com/dev)
```

* After installation, just restore your backup. [Read more...](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/)

## Install the desired version
It is possible to install a custom version. Just follow the instructions below.


```
bash <(curl https://i.hiddify.com/vVERSION)
```

Here, instead of VERSION, you should enter the desired version. Suppose you want to install version `8`. Just execute the following command to install the latest version `8` for you.

```
bash <(curl https://i.hiddify.com/v8)
```

From version 10, you can install exactly one specific update. For example, to install `10.7.0` version, just use the following command.

```
bash <(curl https://i.hiddify.com/v10.7.0)
```

</div>

You can also view and select desired versions for installation via a graphical menu by running the following command:

<div dir=ltr>

```
bash <(curl https://i.hiddify.com/custom)
```
</div>

This will result in the appearance of a graphical menu. Select your desired version to proceed with the installation.

<div align=center markdown="1">
  
![Install Desired Version](https://github.com/user-attachments/assets/fa9c1a28-ef58-44b4-8a9f-9afbdb04c40c)
</div>
