---
title: Explanations about admin link in HiddifyManager
---

<div dir="ltr" markdown="1">

# The correct format of admin link
Or note that the admin link and other program links are made up of different parts and can be changed in the settings; It is necessary to give an explanation about the correct format of the admin link.

In general, the admin link has the following format:

https://sub.domain.com/DrtGho0n4b8H9D/8bncvfb5-8193-vv76-ab97-4c35965l250m/admin/
![](https://user-images.githubusercontent.com/125398461/230102115-65b21ce7-bc9f-4a6f-a450-bc531ce19a31.png)


Each part is separated from each other with "/" which will be explained below.

> The beginning of the link that specifies the protocol of the site. If `https` is used; It means that the connection between the client and the server is encrypted by a TLS certificate and the connection is secure. If `http` is used; It means that the connection between the client and the server is established without encryption, which is not recommended. Therefore, it is strongly recommended to use `https` links to connect to the server.

> After that, there is the subdomain address along with the domain, which can be direct, CDN, or Relay. More information about domain types

> After that, there is a hidden proxy path, which is in the settings menu; The advanced settings section is located and can be changed.

> The next part is the admin password, which can be found in the settings menu; Admin settings edited.

> The last part of the admin link is the page address that ends with admin. Now the sub-pages of this page can be added. For example, the users page can be in this format.

Now the sub-pages of this page can be added. For example, the users page can be in this format:

https://sub.domain.com/DrtGho0n4b8H9D/8bncvfb5-8193-vv76-ab97-4c35965l250m/admin/user/

- If after the end of the initial installation through the terminal; The given admin links were not in the format mentioned above; It turns out that the installation was not done correctly.

- Also, if there is a change in the admin password, this link will change

- Also, if the hidden proxy path changes, this address will change