---
title: How to install different versions of Hiddify Manager
weight: -75
---

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
sudo bash -c "apt update; apt install -y curl; bash <(curl -sSL https://raw.githubusercontent.com/hiddify/hiddify-manager/main/common/download.sh) release"
```

* After installation, just restore your backup. [Read more...](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/)


## Install Beta version
* Before installing, if you have already installed another version of the panel, take a backup of the panel. [Read more...](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/)
* Now just run the following one-line command in the terminal.

```
sudo bash -c "apt update; apt install -y curl; bash <(curl -sSL https://raw.githubusercontent.com/hiddify/hiddify-manager/main/common/download.sh) beta"
```

* After installation, just restore your backup. [Read more...](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/)


## Install Develop version
* Before installing, if you have already installed another version of the panel, take a backup of the panel. [Read more...](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/)
* Now just run the following one-line command in the terminal.

```
sudo bash -c "apt update; apt install -y curl; bash <(curl -sSL https://raw.githubusercontent.com/hiddify/hiddify-manager/main/common/download.sh) develop"
```

* After installation, just restore your backup. [Read more...](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/)

## Install the desired version
It is possible to install a custom version. Just follow the instructions below.


```
bash <(curl i.hiddify.com/vVERSION)
```

Here, instead of VERSION, you should enter the desired version. Suppose you want to install version `8`. Just execute the following command to install the latest version `8` for you.

```
bash <(curl i.hiddify.com/v8)
```

From version 10, you can install exactly one specific update. For example, to install `10.7.0` version, just use the following command.

```
bash <(curl i.hiddify.com/v10.7.0)
```
