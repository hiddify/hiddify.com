<div dir="rtl">

[**![flag_of_Iran](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://github.com/hiddify/hiddify-config/wiki/%DA%AF%D8%B1%D9%81%D8%AA%D9%86-%DA%A9%D9%84%DB%8C%D8%AF-%D8%AA%D9%88%D8%B3%D8%B9%D9%87-%DA%A9%D9%84%D9%88%D8%AF%D9%81%D9%84%D8%B1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>

</div>

# Get Cloudflare API

The purpose of this work is to connect the panel to the Cloudflare. By doing this, when you create a subdomain in the panel; Cloudflare automatically creates them and gets a certificate for them. Also, the process of creating workers is automated. Follow the steps below in order to get the Cloudflare key token.

1. First of all, log in to your Cloudflare account and register your domain. If you need more information for this, please read [this link](https://github.com/hiddify/hiddify-config/wiki/Domain-types-and-how-to-register-them).

2.  From [here](https://dash.cloudflare.com/profile/api-tokens/) , go to **My Profile** > **API Tokens**.
    
3.  Select `Create Token`.

![](https://user-images.githubusercontent.com/125398461/234880340-5f1abcac-9f10-46eb-bb19-204546e3c453.png)

    
4. Choose a template from available templates or create a custom token. We suggest to use `Edit zone DNS` template as in the example below.

![](https://user-images.githubusercontent.com/125398461/234880943-80462114-58bd-48df-baef-2addfc740062.png)
    
5. In this step, configure Zone permission and resources as follows.
   
![](https://user-images.githubusercontent.com/125398461/235046796-2ea8d0ed-4fe4-4060-ae55-683c9d2c0e7c.png)

    
You can change token permissions from (_Account_, _User_, or _Zone_). Most groups offer "Edit" or "Read" options. "Edit" is full CRUDL (create, read, update, delete, list) access, while "Read" is read and list permission if necessary. See [available token permissions](https://github.com/fundamentals/api/reference/permissions/) for more information.

Proceed as follows to apply changes to your domains and Workers.

* Set the Zone permission to DNS and in Edit mode to allow adding different subdomains.

* Click the `Add more` button and select the `Workers Scripts` option in the `Account` section and give it Edit permission.

* In the `Account Resources` section, select `All accounts`.

* In the `Zone Resources` section, allocate resources to your account. That is, select `All zones from an account` and then select your Cloudflare account.

* Finally, click `Continue to summary`.
    
6. Select **Create Token** to create the token.

![Token summary screen displaying the resources and permissions selected](https://user-images.githubusercontent.com/114227601/229592071-3faf93c3-b246-4a08-823b-4680a3a4cf5e.png)
    
7.  Copy the token.

![](https://user-images.githubusercontent.com/125398461/234892482-293f7505-5c94-4564-b0d6-3337fd435e7c.png)

# Finally, click Continue to summary.

After creating the token; go to the panel and in `Very advanced settings`; paste the token in the specified field as shown in the image below.

![](https://user-images.githubusercontent.com/125398461/235085172-4a076a7f-5a93-4fce-b572-829608b9609f.png)

Now, if you create a new subdomain in the domains section of the panel; Cloudflare settings are done automatically. Also, workers are created automatically.
