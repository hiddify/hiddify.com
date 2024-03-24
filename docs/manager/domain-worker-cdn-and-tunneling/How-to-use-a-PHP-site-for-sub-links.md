---
title: How to use PHP site for sub links
---

# Create a PHP site to transfer information of subscription links

## The purpose of creating a PHP site for subscription links
HiddifyManager is based on the principle of reducing the possibility of server filtering as much as possible. One of the practical ways in this field is to separate configurations from subscription links. In this case, your client will always receive the latest configuration information through the subscription link. Now suppose the subscription link was not available for any reason, in this case a PHP site can be brought up and used to transfer the subscription link information (and not the config). The schematic for doing this is as follows.

<div align=center markdown=1>
  
![php site for sub-link](https://github.com/hiddify/hiddify.com/assets/125398461/88db7524-3ccf-40ca-b6f2-ffc351bedf80)
</div>

## Steps to do the work
To create a PHP site and use it for the subscription link, you must first do a [Google search](https://www.google.com/search?q=free+php+hosting) and find free sites that provide free PHP service. find.

- Choose one of the sites.
- Create your account there.
- Then create a PHP hosting service in it. This work has similar steps in different sites and is almost simple. To create this service, you must create a unique address on one of the domains of that provider.
- After that, your service will be created.
- After creating the service, edit its files and place the following two files in the main path of your service.

> - Note: If you don't see any `.htaccess` and `index.php` files, you need to create these files manually.

> - Make sure that `.htaccess` file has a dot before its name and if you create it, consider this point.

**Code for `.htaccess file`**

```php
<?php

if (!isset($_SERVER['HTTPS']) || $_SERVER['HTTPS'] !== 'on') {
     http_response_code(403);
     exit('Access Forbidden - HTTPS is required.');
}

$server_domain = "https://hiddify-sub-only-domain.com";

$domain = $_SERVER['HTTP_HOST'];
$ip = $_SERVER['HTTP_CF_CONNECTING_IP'] ?? $_SERVER['HTTP_X_FORWARDED_FOR'] ?? $_SERVER['REMOTE_ADDR'];
$url = $server_domain . $_SERVER['REQUEST_URI'];
$userAgent = $_SERVER['HTTP_USER_AGENT'];

$ch = curl_init();
curl_setopt_array($ch, [
     CURLOPT_URL => $url,
     CURLOPT_RETURNTRANSFER => true,
     CURLOPT_SSL_VERIFYPEER => false,
     CURLOPT_SSL_VERIFYHOST => 2,
     CURLOPT_HEADERFUNCTION => function($curl, $header) {
         header($header);
         return strlen($header);
     },
]);

$headers = [
     "CF-Connecting-IP: $ip",
     "Host: $domain",
     "User-Agent: $userAgent",
];
foreach ($_SERVER as $key => $value) {
     if (strpos($key, 'HTTP_') === 0) {
         $header = str_replace('_', '-', substr($key, 5));
         $headers[] = "$header: $value";
     }
}
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

$response = curl_exec($ch);
if (curl_errno($ch)) {
     http_response_code(500);
     exit('Internal Server Error');
}

curl_close($ch);
echo $response;

?>

```

Be careful:
> Replace your subscription domain in the above PHP code.

> In the PHP site settings, the PHP version should be 8 or higher.

> The CURL option should be turned on in the PHP settings of your host.


- Then save the settings.
- At this point, if you check the ssl settings for your domain in this PHP provider; You will probably notice that it takes some time for the certificate to be assigned.
- Now to use; Copy the link related to your created domain in this provider and then copy the section after the address from your admin link in the panel and paste it at the end of your PHP link. The panel returns with the PHP address.
For example, suppose your PHP domain is:

https://hello2freeworld.phpsite.com

And the link of your admin panel should be like this:

https://t1.hiddify.com/koZlk3E8P59Ghf8R/ab56bgt8-737c-4fd6-9oe0-6d4fa4bb84c0/admin/

Your PHP address to reach the panel will be as follows:

https://hello2freeworld.phpsite.com/koZlk3E8P59Ghf8R/ab56bgt8-737c-4fd6-9oe0-6d4fa4bb84c0/admin/

> **Very important note:** if your PHP domain is not yet certified on the provider's site; This address does not open with https and you can open it with http for testing, but be sure to use https to use. So you have to wait for the certificate to be assigned.

- After performing the above test, register the domain in your HiFi Manager in the Domains section so that the server will get SSL for it and its connection will be completely secure.

- After doing this, you can add this link as a subscription link to your client apps.
- The work is done. Now you have an address that is connected to your server and is practically unfilterable.
