---
title: How to use HiddifyCli
---

# How to use HiddifyCli or Hiddify command line
This app is developed for cases where there is no desktop, such as servers, and it supports all processors.

## Download
To download this app, go to [here](https://github.com/hiddify/hiddify-core/releases) and download the file related to your processor.

## Execution of config or subscription link in HiddifyCli

To use it, the following command should be used.
<div dir="ltr" markdown="1">
  
```
HiddifyCli run -c <config file or sublink> -d <HiddifyApp config file or URL>
```
</div>

- To connect to a specific configuration, just run the above command as follows.
<div dir="ltr" markdown="1">

```
HiddifyCli run -c <config file>
```
</div>

Here, put your desired configuration instead of `<config file>`.

- You can also run a subscription in the app.
<div dir="ltr" markdown="1">
  
```
HiddifyCli run -c <sublink>
```
</div>

Put your subscription link here instead of `<sublink>`.

## Run config or subscription link in HiddifyCli with HiddifyApp settings
For this, you must first extract the settings related to your HiddifyApp.
<details markdown="1"><summary><h3>Extract HiddifyApp settings</h3></summary>

  - To do this, open HiddifyApp and enter `Config Options` and click the three-dot menu.

<div align=center>

<img alt="config-options" src="https://github.com/hiddify/hiddify.com/assets/125398461/36986f9b-cf00-4aef-a11e-c0461a48d3a8" />

</div>


- Now click the `Export Settings to Clipboard` option to save the settings to the clipboard.
<div align=center>
  
<img alt="export configs" src="https://github.com/hiddify/hiddify.com/assets/125398461/a76e3ed9-cd3d-4746-a5f1-8c8a379856c5" />

</div>


- Now you can save these settings in a file with `json` extension.
  
- You can also put these settings in Github and use its link as `URL`.



</details>

### Run config or subscription link in HiddifyCli with settings extracted from HiddifyApp
- Also, if you want to use your HDIFYAP settings, you should use the following command.
<div dir="ltr" markdown="1">
  
```
HiddifyCli run -c <config file or sublink> -d <HiddifyApp config file>
```
</div>

Here, put your config file or sublink instead of `<config file or sublink>` and enter the configuration file related to HiddifyApp that you extracted in the previous step instead of `<HiddifyApp config file>`.

- Instead of the config file, you can use the link related to the settings in HiddifyApp that you put on Github.
<div dir="ltr" markdown="1">
  
```
HiddifyCli run -c <config file or sublink> -d <HiddifyApp config URL>
```
</div>

Here, put your config file or sublink instead of `<config file or sublink>` and put the link of the desired settings in HiddifyApp instead of `<HiddifyApp config URL>`.
