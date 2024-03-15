---
title: How to create subscription link on HiddifyManager
---

<div dir="ltr" markdown="1">

# How to create subscription link on Hiddify
Hiddify is based on the principle of reducing the possibility of server filtering as much as possible. One of the practical ways in this field is to separate the configs from the subscription links. In this case, your client will always receive the latest configuration information through the subscription link. The schematic related to this work is as follows.

![sub link schematic](https://github.com/hiddify/hiddify-config/assets/125398461/9046fa04-81dd-4c98-8e65-30e7b5402d66)



As you can see in the figure above, the subscription link is connected separately from the server to the users, and the task of this link is to transfer information about various connections such as CDN, AutoCDN, Relay, etc. That is, the connections themselves establish the connection between the server and the client separately, and the subscription link transfers the information related to these connections from the server to the client. For example, if a new clean IP is placed in the CDN connection, the information about this new IP is transferred to your client through the subscription link. On the other hand, clients go to the free Internet through different connections that are separate from the subscription link. With this method, the information of the subscription links (subscription) is separated from the connections (configs) and because the traffic of the configs is not placed on these links, the use of the subscription links will not be filtered in any way and will always be available.

## How to create domain for subscription link on Hiddify
To do this, go to the `Domains` section in the `Settings` and click on `Create`.

![Domain settings](https://github.com/hiddify/hiddify-config/assets/125398461/b0749490-6e4e-43aa-b9b4-ab721cceb6b8)

- Just set the domain mode to `sub link only`.
- For the `Alias` field, choose a name if you wish. This name is used for display only.

> Make sure to use standard characters such as letters and numbers.

- And finally, using `Show Configs of Domains`, select the domains that you previously created for different connections. That is, for example, you have already created several domains for CDN or worker to provide different connections. From this field, connect those domains to the domain corresponding to the subscription link.
- Then press `Save` and press `Apply Changes` if the message appears. The work is done. You created a separate domain for subscription links and attached it to the configs.

You can also use a PHP site for the subscription link, in which case the schematic will look like this.

![php sub link schematic](https://github.com/hiddify/hiddify-config/assets/125398461/0eb1634e-f6b9-4f67-86ae-9bc8d239a7b4)


For its tutorial, go [here](https://github-com.translate.goog/hiddify/hiddify-config/discussions/689?_x_tr_sl=fa&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp).

