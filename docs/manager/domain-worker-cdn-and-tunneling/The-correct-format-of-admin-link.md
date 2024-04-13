---
title: Explanations about admin link in HiddifyManager
---

<div dir="ltr" markdown="1">
  
# Explanations about admin link in HiddifyManager and its changes after version 10
## The correct format of admin link
Or note that the admin link and other program links are made up of different parts and can be changed in the settings; It is necessary to give an explanation about the correct format of the admin link.

In general, the admin link has the following format:

`https://sub.domain.com/DrtGho0n4b8H9D/8bncvfb5-8193-vv76-ab97-4c35965l250m/admin/`

![](https://user-images.githubusercontent.com/125398461/230102115-65b21ce7-bc9f-4a6f-a450-bc531ce19a31.png)


Each part is separated from each other with "/" which will be explained below.

> The beginning of the link that specifies the protocol of the site. If `https` is used; It means that the connection between the client and the server is encrypted by a TLS certificate and the connection is secure. If `http` is used; It means that the connection between the client and the server is established without encryption, which is not recommended. Therefore, it is strongly recommended to use `https` links to connect to the server.

> After that, there is the subdomain address along with the domain, which can be direct, CDN, or Relay. More information about domain types

> After that, there is a hidden proxy path, which is in the settings menu; The advanced settings section is located and can be changed.

> The next part is the admin password or `UUID`, which can be found in the settings menu; Admin settings edited.

> The last part of the admin link is the page address that ends with admin. Now the sub-pages of this page can be added. For example, the users page can be in this format.

Now the sub-pages of this page can be added. For example, the users page can be in this format:

`https://sub.domain.com/DrtGho0n4b8H9D/8bncvfb5-8193-vv76-ab97-4c35965l250m/admin/user/`

- If after the end of the initial installation through the terminal; The given admin links were not in the format mentioned above; It turns out that the installation was not done correctly.

- Also, if there is a change in the admin password, this link will change

- Also, if the hidden proxy path changes, this address will change

## Admin link changes in HiddifyManager version 10
* In version 10, there has been a slight change in the structure of the links, which is in accordance with the following description:
   * By default, after installing the long link format, it appears as above in the terminal. This link is your main admin link.
   * When you open it in the browser, for more security, the admin authentication operation is performed based on the password or `UUID` of that admin, and then the long link is converted to a short link:
     

`https://sub.domain.com/proxy_root/address_of_the_page`

![short link format](https://github.com/hiddify/hiddify.com/assets/125398461/c52bd330-65ee-4c83-b7c7-ddd05f32e6a8)


  * This shortened link is valid for up to 10 days, in other words, your login with admin user is valid for up to 10 days and then it expires.
  * After that, if you refresh the shortened link in the browser, the login page with UUID will be displayed. Here you need to enter the `UUID` of that admin in the `Secret Code` filed to perform the login operation.
  
  <div align=center>
  <img alt="login via UUID" src="https://github.com/hiddify/hiddify.com/assets/125398461/d8c66248-5b57-419e-a12f-4195501ee84c" width=70% />
  </div>
 
  * The alternative solution is to open the long link (the link that appeared in the terminal after installation) once again. In this case, you do not need to enter the UUID.
  > It is recommended to always save the long link in a place where it is available to you when needed and use it.
