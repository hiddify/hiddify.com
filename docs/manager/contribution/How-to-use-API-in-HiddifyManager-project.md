---
title: How to use API in HiddifyManager project
---

<div dir="ltr" markdown="1">
    
# How to use API in HiddifyManager project

The HiddifyManager project provides two versions of its APIs for compatibility reasons. However, it is highly recommended to use version two, as version one may be deprecated in the future. This blog post aims to guide you through the process of using the self-documented version two APIs, which can be explored in the Admin Panel -> Settings -> API section.

## API Authentication
To use the APIs, authentication is required, which involves using the admin/user UUID (corresponding to the API) as a key.

This key must be included in the request as the "Hiddify-API-Key" header value.

## API Structure version two 
This structure is divided into three main sections:
- Panel section, This section offers operations such as:
    - Retrieving the panel version
    - Ping with panel itself


  > The base URL for this section is:
  > 
  > domain.com/<admin_proxy_path>/api/v2/panel/

- Admin section, This section offers operations such as:
    - Retrieving information about the current admin (logged-in admin)
    - Managing (get/create/edit/delete) admins and users
    - Accessing current server statistics
    - Viewing the contents of the Hiddify log files

  > The base URL for this section is:
  >
  > domain.com/<admin_proxy_path>/api/v2/admin/

- User section, This section offers operations such as:
    - Access information about the current user (logged-in user)
    - Obtain suggested clients and their relevant details
    - Retrieve links for all active subscriptions
    - Get Mtproto proxy links
    - Acquire temporary (short) links for the user's panel
  > Notice: Although it is possible to enter the key in the URL section, it is strongly recommended to enter it in the header.
  > 
  > The base URL for this section has two options:
  > 
  >> domain.com/<user_proxy_path>/api/v2/user/
  >> 
  >> domain.com/<user_proxy_path>/<uuid>/api/v2/user/

### Additional Information
To learn more about each API, its inputs, and outputs, please refer to the API section within the HiddifyManager panel.

In conclusion, HiddifyManager's version two API offers a wide range of features and functionality to make managing your panel, admins, users, and more as seamless and efficient as possible.


> [!NOTE]
>
> There is a possibility of endpoint or input/output changes in the APIs, and developers should familiarize themselves with API-related guidelines through updates and changes of HiddifyManager.

</div>
