<div dir="rtl" markdown=1>
[**![Lang_Farsi](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://github.com/hiddify/hiddify-config/wiki/%D9%86%D8%AD%D9%88%D9%87-%D8%AA%D9%86%D8%B8%DB%8C%D9%85-%D9%88-%D8%A7%D8%B3%D8%AA%D9%81%D8%A7%D8%AF%D9%87-%D8%A7%D8%B2-%D9%88%D8%B1%DA%A9%D8%B1%D8%B2)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>

</div>

# How to set up and use Cloudflare workers
Workers is one of Cloudflare's famous CDN services, which is actually a server-less service, through which programming codes can be executed without the need for server or infrastructure configuration. In fact, this service is a type of cloud computing based on SaaS.

In other words, the working method of Workers is that instead of trying to open your website (here Hidify panel) directly; You send requests to workers and then workers re-send requests to your domain and server.

![](https://user-images.githubusercontent.com/125398461/224561104-dafc3e89-1c0d-4afc-82eb-cce1cec6933a.png)

The purpose here is to hide the domain behind the workers.

## How to use a Workers?
To use a Worker you need to have an active domain on the Cloudflare.

## Domain and subdomain registration on Cloudflare
Here you need a purchased domain and you need to register it in the Cloudflare. If you have any ambiguity about the domain and how it is registered; Read [this](https://github.com/hiddify/hiddify-config/wiki/Domain-types-and-how-to-register-them).

Sign in to your account in your account according to the description of how to register your domain.

![](https://user-images.githubusercontent.com/125398461/224561629-dd0be4b5-9345-43b7-aa81-a3bfaaaf5899.png)

Enter the registered domain and register a new subdomain in the DNS section.

![](https://user-images.githubusercontent.com/125398461/224561952-cbb99885-46f7-49e2-874d-f48e5b0c9b0d.png)

There is no need for the proxy to be `ON`. The Worker works with both proxy modes (ON and OFF).


![](https://user-images.githubusercontent.com/125398461/236729724-3c4c85e9-046b-4285-9d92-4bc4d9506091.png)

After registering a sub domain, you must change certificate settings.

## Setting up domain certificate
Set the certificate setting of your domain to `Full`.

<div align=center markdown=1>
![](https://user-images.githubusercontent.com/125398461/235835085-8d9c9ea5-16f2-4782-bfa2-4cc010d7367c.png)
</div>

## Creating Worker service
Go to the Worker section on your dashboard page on Cloudflare.

![](https://user-images.githubusercontent.com/125398461/224562657-f433fff0-d4a1-4fe6-95e0-5f4e17337c3d.png)

Then select the `Create a Service` option.

![](https://user-images.githubusercontent.com/125398461/224562813-20dc1a02-8d93-446b-a7d9-d90fbae3cda3.png)

Here you can choose the name of your Worker service. Cloudflare also offers you a name. You can change it, but note that this name should be unique.

![Picture](https://user-images.githubusercontent.com/125398461/236729831-7ecba946-b031-46c1-b370-0df1dae47385.png)

The `Starter` option should be also on `HTTP Handler`. Finally, by selecting the `Create service`, your Worker service will be created.

Then you need to click the `Quick Edit` button to put your favorite code in the Worker.


![Imgage](https://user-images.githubusercontent.com/125398461/236729939-ca4f2378-91a2-447f-80fd-9f1ff79f83fe.png)


On the editing page of the Worker, wipe the default codes on the left side.


![Image](https://user-images.githubusercontent.com/125398461/236730008-7ffa12a1-84de-44d2-8c16-ae8e757d77b6.png)

Then put the following code in its place.

```
addEventListener(
   "fetch", event => {
       
       const ip = event.request.headers.get('cf-connecting-ip') || event.request.headers.get('x-forwarded-for') || (event.request.socket && event.request.socket.remoteAddress);
       let url = new URL(event.request.url);
       const worker_domain=url.hostname;
       url.hostname = "sub.domain.com";                        
       url.protocol = event.request.headers.get('x-forwarded-proto') || "https";
       let request = new Request(url, event.request);
       if (ip)
        request.headers.set('cf-connecting-ip', ip);
        request.headers.set('Host', worker_domain);
       event.respondWith(
           fetch(request)
       )
   }
)

```

Note:
- In the sixth line, you must put the registered domain for the `url.hostname` value. That is, for example, you have registered the subdomain `sub.domain.co`m in Cloudflare according to the description of the first step; Here you need to put that domain for the `url.hostname` value.

![Image](https://user-images.githubusercontent.com/125398461/236730073-2d3a5e99-9a38-4e73-b3b6-9d962acee957.png)


Click the `Save and deploy` button.

**A very important note: Do not worry if an error is displayed in the section that displays the result of the code execution (shown in the upper right of the image) at the stage of saving the code. Save the code and continue.**

On the workers page, copy your workers address without `https`. For example, like this:

![Image](https://user-images.githubusercontent.com/125398461/236730138-16641a29-82e8-4276-8f8e-9c16f1bd4348.png)


This step was completed successfully. Now you have to register the address of your Workers service on Hiddify panel.


## Workers setting up on Hiddify
Go to the Domains menu and click `Create`.

![Image](https://user-images.githubusercontent.com/125398461/236730761-5b3ae32d-c67f-4e54-96b4-fe1a034da834.png)


Make the settings according to the picture above and save it.

> Note: You can use CDN and AutoCDN modes

Work is finished. A CDN/AutoCDN domain with the details of your workers has been added to your previous domains and you can use its connections.


> Important point:
Workers in the free plan only processes 100,000 requests per day, so this service is useful for those who do not have high traffic on their server.



<div align=center markdown=1>
![](https://user-images.githubusercontent.com/125398461/235835675-e454ba05-29ad-4b53-9cf9-f23f4c225ef6.png)


</div>

## Adding the configurations of Workers to the domain related to subscription links

As you probably know, in Hiddify you can put subscription links on a separate domain and add other domains that are set for connections to this domain. The advantage of this is that the domain of subscription links will always be available and will not be filtered because this way separates connections from subscription links.

Well, suppose the domain of our subscription links that you have already registered is `t1.hiddify.com`. Go to the settings related to this domain and in the `Show Configs of Domains` field, check the new domain that you added in the previous step for Workers as shown below.

![](https://github.com/hiddify/hiddify-config/assets/125398461/e0037530-fcb7-4aed-968f-a75d2978c2bb)

Finally, if you go to the users' page and click on the user link as shown below,

![](https://github.com/hiddify/hiddify-config/assets/125398461/72bcfe5a-4761-49a7-b68e-e4e3f75fed48)

You will see that the new configs related to Workers have been added to the previous configs.

![](https://github.com/hiddify/hiddify-config/assets/125398461/9c1f324a-acf1-46b1-9dfe-10fc1313051b)
