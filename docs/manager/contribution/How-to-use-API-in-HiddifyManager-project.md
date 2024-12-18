---
title: How to use API in HiddifyManager project
---

# How to use API in HiddifyManager project
### Comprehensive Documentation for API in Hiddify Manager

---

#### **Introduction**

The API in Hiddify Manager is designed to enable remote control of the panel and provide easier access through programming and integration with applications and bots. This document will introduce you to how to use version 2 APIs, along with security considerations and definitions required for their implementation.

---

#### **Accessing API Documentation**

To view and utilize the API documentation, navigate to:  
`Admin Panel -> Settings -> API`  
Here, you can explore different sections of the API and obtain request codes tailored to your programming language.

---

#### **Definitions Needed for API Usage**

1. **Hiddify-API-Key**  
   This value represents the admin or user UUID, which must be obtained through the admin or settings section and used in the header of requests.

2. **Admin Proxy Path**  
   Admin proxy path is used for secure communication with the admin panel. This value can be obtained from:  
   `Settings -> Advanced Settings -> Admin Proxy Path`

---

#### **Structure of Version 2 API**

Version 2 API is divided into three main sections:

##### **1. Panel Section**  
This section handles operations related to the panel, such as:
- Retrieving panel version
- Pinging to ensure panel is running  

**Base URL:**  
```plaintext
/domain.com/admin_proxy_path/api/v2/panel
```

##### **2. Admin Section**  
This section manages admin and server operations:
- Retrieving current admin information
- Managing admins (create/edit/delete)
- Accessing server statistics
- Viewing Hiddify logs  

**Base URL:**  
```plaintext
/domain.com/admin_proxy_path/api/v2/admin
```

##### **3. User Section**  
This section provides functionalities for users:
- Retrieving current user information
- Fetching suggested clients
- Viewing MTProto proxy links and subscription links
- Generating a temporary link for user panel  

**Base URL:**  
```plaintext
/domain.com/user_proxy_path/api/v2/user/
```

**Note:** For enhanced security, it is recommended to include the `Hiddify-API-Key` in the header of requests rather than directly in the URL.

---

#### **Security and Development Notes**

- Always use version 2 of the API, as version 1 may be deprecated in the future.  
- Changes in **endpoints**, inputs, and outputs may occur in each API version, so developers should continuously review the most up-to-date panel documentation.

---

#### **Authentication Example**

```bash
curl -X GET "https://domain.com/admin_proxy_path/api/v2/panel/version" \
-H "Hiddify-API-Key: YOUR_ADMIN_UUID"
```

---

### Conclusion

Version 2 of Hiddify Manager API provides a comprehensive set of tools for managing panels, admins, and users. By using these APIs, you can maintain a more integrated and controlled approach to your project. For more information, refer to the documentation within the admin panel.

If you have any questions or suggestions for improving this documentation, please let us know! 😊
