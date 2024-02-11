<div dir="rtl" markdown=1>
[**![Lang_Farsi](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://docs.hiddify.com/fa/Hiddify-Manager.wiki/%D8%A7%D8%B3%D8%AA%D9%81%D8%A7%D8%AF%D9%87-%D8%A7%D8%B2-CDN-%D8%A2%D9%85%D8%A7%D8%B2%D9%88%D9%86)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>
</div>

# How to use Amazon CDN or Cloudfront

## Domain registration

- To do this, first point an A record to your server address in DNS. Suppose you have pointed sub1.domain.com to the IP address of your server.

- Go to [Amazon AWS](https://aws.amazon.com/) and search for Cloudfront service.
- Create a destination by clicking create distribution.
- Enter the values in the opened page according to the image below.

<div align=center markdown=1>
<img alt="aws settings" src="https://github.com/hiddify/Hiddify-Manager/assets/125398461/9e1623b7-ffdc-4881-be24-b7223c63cb90" width=70% />
</div>

All values on this page are default except for the following which should be set as shown in the images.

<div align=center markdown=1>
<img alt="protocols policy" src="https://github.com/hiddify/Hiddify-Manager/assets/125398461/322d696e-cc53-4272-87ec-b5f77baa1546" width=70% />
</div>

<div align=center markdown=1>
<img alt="cache policy" src="https://github.com/hiddify/Hiddify-Manager/assets/125398461/404b3134-de2d-4dca-a942-a524b43ed883" width=70% />
</div>

<div align=center markdown=1>
<img alt="waf settings" src="https://github.com/hiddify/Hiddify-Manager/assets/125398461/3139e115-5c4f-41df-9d49-766e973a4d14" width=70% />
</div>

- At the end, click on `create distribution` to perform the creation operation.
- In the next step, go to the location of your DNS records. Assuming that you have registered in Cloudflare, enter the DNS section of your domain and create a cname record. Suppose you create `sub2.domain.com` and set its value equal to the domain created in the previous step in AWS. This value can be seen in the `details` section under `Distribution domain name`.

In fact, this subdomain will be used for our CDN domain.

- Go back to the AWS panel and click on the `edit` option in the `General` tab of the `setting` section and click on `Add item` in the `Alternate domain name (CNAME) - optional` section that opens. and enter the cname domain from the previous step, `sub2.domain.com`.

## Getting a certificate

- Enter the `Custom SSL certificate - optional` section and get an `ssl certificate` for the desired domain. For this, click on `Request certificate`.
- In the newly opened page, continue the process of receiving the certificate and in the `domain name` section and the address field, enter the details of the subdomain registered in the previous step, namely `sub2.domain.com` and set the other values as default. and click on `Request`.

- On the certificate list page, you can see that the desired domain status is `pending validation`. Click on the ID and see the `Domains` section on the opened page.

<div align=center markdown=1>
<img alt="domain settings" src="https://github.com/hiddify/Hiddify-Manager/assets/125398461/e2a5d38a-efde-45c5-b55b-d2f395aa846a" width=70% />
</div>

- In this section, two values of this section, `Cname name` and `Cname value` are needed to complete the certificate status.
- Go to your DNS records (presumably Cloudflare) and create a `Cname name` record and enter the values you had in the previous step in AWS. In Cloudflare, enter `Cname name` instead of `name` and `Cname value` instead of `Target`.
- Now if you go back to AWS and the certificate list page and refresh the page, you will see that the status has changed from `pending` to `issues`, which means that our domain has received the certificate correctly.
- Now it is back to the `distribution` settings page and the certificate derivation stage, and if you click the refresh button for `custom ssl`, you can see the certificate you received in the previous stage. Select it and leave the other values of this page as default.

> [!tip]
> Note: Be careful not to tick the `Legacy client support` because this option costs $600 per month.

- At the end, click the save changes option to save the changes.
- Now wait until the changes are applied and according to the image below, the state of `Last modified` will change from `Depoloying` to done to the date and time.

<div align=center markdown=1>
<img alt="done page" src="https://github.com/hiddify/Hiddify-Manager/assets/125398461/893cfd82-7ccc-4fe6-9b25-09da4272e9a3" width=70% />
</div>

- It usually takes between 2-5 minutes for these changes to be applied, which can be followed by refreshing the screen. Always remember that at any stage you make changes, it should change to this state, which means that the changes are fully applied and usable.

- Congratulations, the work is done. Amazon Cloudfront CDN is successfully launched. Now just register your CDN domain in your HiFi Manager.
