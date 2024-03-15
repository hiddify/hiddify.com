---
title: Quick installation on Vultr Servers
---

<div dir="ltr" markdown="1">


# How to use GCore CDN on Cloudflare registered domain

As you probably know, in order to use the Hiddify panel optimally, you need to use a CDN provider so that filtering can be bypassed using its services. In other articles, we introduced Cloudflare and taught how to work with it. This service is due to widespread disruptions that are applied on it; Sometimes it makes things difficult for users. An alternative way is to use GCore's CDN service. Read this article to the end to learn how to set it up.

1. First, go [here](https://gcore.com/) and create your account on GCore website. Then log in to the created account and click on the CDN option in your dashboard.

![](https://user-images.githubusercontent.com/125398461/235283540-83a44dbc-6b81-45d2-a04f-be2749cf0429.jpg)

2. In the next step, choose the free plan and click `Next`.

![](https://user-images.githubusercontent.com/125398461/235283581-a392f93e-4d8a-44d9-9521-be83fb09564b.jpg)

3. After completing the requested information, click on the `Get started` option.

![](https://user-images.githubusercontent.com/125398461/235283590-6654cae1-cc3b-42c6-ae8c-d4cc26b71a15.jpg)

4. In the next step, click on `Create CDN resource`.

![](https://user-images.githubusercontent.com/125398461/235283617-042ee013-e1a1-4567-aa6c-fcbf1080fa99.jpg)

5. Now click on `Confirm` on the opened page.

![](https://user-images.githubusercontent.com/125398461/235283626-b7923519-ffbc-425b-a65b-3063e19595a1.jpg)

6. In this step, enter the domain you have registered in Cloudflare along with the desired subdomain.

![](https://user-images.githubusercontent.com/125398461/235283639-ef21b5ba-5efd-48d5-a852-7aa8050b4316.jpg)

7. Then enter your server's IP and click on `Add` button.

![](https://user-images.githubusercontent.com/125398461/235283674-400d9213-029a-429b-9985-699c0bd40ba3.jpg)

8. In the next step, click on `Confirm` again.

![](https://user-images.githubusercontent.com/125398461/235283679-fbb415e0-5b12-4880-be94-3f2a17ba5895.jpg)

9. Since you are going to use GCore's CDN, you don't need to register GCore's nameservers on your domain and just click on `Confirm`.

![](https://user-images.githubusercontent.com/125398461/235283686-69d71bb4-2c27-4375-8a04-3a7f2f1fac21.jpg)

10. In this step, click on `Confirm` again.

![](https://user-images.githubusercontent.com/125398461/235283803-1ca531c7-efb6-4bf2-ba21-5f68de3cc9df.jpg)

11. Then click on `Open resource settings` option.

![](https://user-images.githubusercontent.com/125398461/235283807-225d6325-b388-4a21-9b41-5da3f7457ba9.jpg)

12. In the opened page, click on the `DNS` option.

![](https://user-images.githubusercontent.com/125398461/235283814-711cf947-256c-4cda-8cc5-236abe8a6b31.jpg)

13. Now click on your domain to display the list of registered records.

![13](https://user-images.githubusercontent.com/125398461/235283822-62ce802c-d7c2-44e8-8fd6-a418fe6a04c2.jpg)

14. Next, click the pencil button to edit the CDN record.

![](https://user-images.githubusercontent.com/125398461/235283921-81cfdb21-b00b-4e94-907d-3a6b95f7b650.jpg)

15. In this step, click on the `CDN Integration` option to integrate CDNs.

![](https://user-images.githubusercontent.com/125398461/235284019-0301d8e3-d882-4482-9c75-23a30e4fb2f1.jpg)

16. Now copy the domain that is in the `CDN Integration` section.

![](https://user-images.githubusercontent.com/125398461/235284138-6355a421-a7da-46c8-803a-b4b65cdc8fb1.jpg)

17. Now log in to your Cloudflare account, enter your domain settings and register a `CNAME` record in the DNS section using the domain you copied in the previous section.

![17](https://user-images.githubusercontent.com/125398461/235284172-560987a3-8528-497a-89c9-58927fddc327.jpg)

18. Go your dashboard on the GCore site again and in the CDN section, after making sure it is Active, click on the domain on your domain.

> Note: It may take some time to become active.

![](https://user-images.githubusercontent.com/125398461/235284405-71b9fe26-e25c-4750-b349-1fac9cd34efb.jpg)

19. Then, in the `Origin` section, set the `Origin pull protocol` setting to `HTTPS`.

![](https://user-images.githubusercontent.com/125398461/235284438-6d4e0c6e-79dc-4175-8718-8a85b68b46d1.jpg)

20. Now, to get the certificate in the `SSL` tab, click on the `Get SSL certificate` option.

![](https://user-images.githubusercontent.com/125398461/235284577-e0ee7fbb-31d9-476b-9901-f2fb78c5c22d.jpg)

21. Receiving the certificate may take about 15 minutes. After getting the certificate, you will see a message about its use and automatic renewal.

![](https://user-images.githubusercontent.com/125398461/235284579-898335c0-28d3-477f-b900-3f8a381bcdda.jpg)

22. Now we can use this subdomain as a CDN domain in Hiddify panel.

![](https://user-images.githubusercontent.com/125398461/235284966-63477444-51d0-45dd-be27-2307f43df54f.jpg)

* Final and important point: Don't forget that CDN GCore has a limit of 1000 GB in the free plan.