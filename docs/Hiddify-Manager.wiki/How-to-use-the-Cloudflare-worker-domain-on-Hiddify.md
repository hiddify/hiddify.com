<div dir="rtl" markdown="1">

[**![flag_of_Iran](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://github.com/hiddify/hiddify-config/wiki/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%A7%D8%B3%D8%AA%D9%81%D8%A7%D8%AF%D9%87-%D8%A7%D8%B2-%D8%AF%D8%A7%D9%85%D9%86%D9%87-%D9%88%D8%B1%DA%A9%D8%B1-%DA%A9%D9%84%D8%A7%D8%AF%D9%81%D9%84%D8%B1-%D8%AF%D8%B1-%D9%87%DB%8C%D8%AF%DB%8C%D9%81%D8%A7%DB%8C)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>
</div>

# How to use the Cloudflare worker domain on Hiddify
Previously, in an [article](https://github.com/hiddify/hiddify-config/wiki/How-to-set-up-and-use-Cloudflare-workers), it was taught how to add Cloudflare workers to the panel. To make it easier to work in version 7, the worker domain was introduced as a separate domain. Follow this article till the end to get familiar with this domain.

## Add Cloudflare API token

For this, you first need to create a Cloudflare development token or key and then add it to the panel. [Follow this article](https://github.com/hiddify/hiddify-config/wiki/Get-Cloudflare-API).


## Add the worker domain to the panel
Enter the panel `Settings` and click on `Create` in the `Domains` section.

<div align=center>

![Screenshot_20230531_143400](https://github.com/hiddify/hiddify-config/assets/125398461/1d3d5365-7598-47fb-8ff1-2fdd44e6c328)

</div>


### Mode
Set domain mode to Cloudflare worker.

### Domain
In this section, choose the domain name you want for the Worker so that this name is automatically added to your Cloudflare account in the workers section.

### Alias
If you want, you can choose a name to display in the configs.

### Force Config to Use Following IPs
In this field, if needed, you can put your Cloudflare clean IPs or use IRCF clean IPs. If you need more information on how to enter IPs in this field, read this [topic](https://github-com.translate.goog/hiddify/hiddify-config/discussions/2009?_x_tr_sl=fa&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp).

Finally, click Save to save the settings. Then click `Apply Changes`.

## Use the configs of this domain
As you probably know, it is recommended that the subscription link be separated from the configurations in Hiddify to prevent the subscription links from being filtered. So if you have already created the subscription link; Here, go to the config settings of that domain and add the new Worker domain in `Show Configs of Domains` field.


<div align=center>

![Screenshot_20230531_142541-2](https://github.com/hiddify/hiddify-config/assets/125398461/d40edd3b-1a13-45c4-94e1-e285f28e236a)

</div>


That is, for example, if `t1.hiddify.com` is your subscription domain, just edit it and in `Show Configs of Domains`, tick the Worker domain.

The work is done. The configs for the new worker domain have been added to your previous configs.
