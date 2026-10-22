---
title: The admin link in HiddifyManager and its format
description: What each part of the HiddifyManager admin link means, how sign-in and Admin V2 work, and what to do if you lose the link.
---

<div dir="ltr" markdown="1">

# The admin link in HiddifyManager and its format

This page explains what each part of your admin link means, what happens when you open it, and how to get it back if you lose it. It is for anyone who manages a HiddifyManager panel.

## The format of the admin link

The installer prints your admin link at the end of the installation. It looks like this:

```text
https://sub.example.com/DrtGho0n4b8H9D/8bncvfb5-8193-vv76-ab97-4c35965l250m/
```

The general form is:

```text
https://<domain>/<admin proxy path>/<admin UUID>/
```

![Parts of the admin link](https://user-images.githubusercontent.com/125398461/230102115-65b21ce7-bc9f-4a6f-a450-bc531ce19a31.png)

The parts are separated by `/`:

1. **`https://`**: the connection is encrypted with TLS. Always use `https` links. An `http` link sends everything without encryption.
2. **Domain** (`sub.example.com`): one of the domains you added in the panel (Direct, CDN or Relay). See [Domain types](/manager/domain-worker-cdn-and-tunneling/Domain-types-and-how-to-register-them/).
3. **Admin proxy path** (`DrtGho0n4b8H9D`): a secret path that hides the panel from bots and filtering systems. It is the setting **Proxy Path for Admins**. Users have a different path (**Proxy Path for Clients**).
4. **Admin UUID** (`8bncvfb5-...`): your personal secret ID. Each admin has their own. Treat it like a password.

!!! warning "Keep your admin link private"
    Anyone who has your admin link can manage your panel, unless you set a password for your admin account.

The link changes if you change your domain, the admin proxy path, or your admin UUID. Save the new link before you change any of them.

## What happens when you open the link

1. You open the admin link in your browser.
2. The panel signs you in and opens **Admin V2**, the new admin panel. The address in your browser changes to:

    ```text
    https://sub.example.com/DrtGho0n4b8H9D/admin/v2/
    ```

    The UUID is removed from the address bar, so it is not shown on your screen.

3. Your sign-in lasts up to 10 days in that browser. After that, or in a new browser, you see the **Sign in** page.

On the **Sign in** page:

- In **Admin ID or username**, enter the UUID from your admin link (or the username you were given).
- In **Password**, enter your password. Leave it empty if your admin account has no password.
- Select **Sign in**.

The easiest way is to open your full admin link again. It fills in your ID automatically.

![Old short link format (before Admin V2)](https://github.com/hiddify/hiddify.com/assets/125398461/c52bd330-65ee-4c83-b7c7-ddd05f32e6a8)

<div align=center>
  <img alt="Sign-in page (older version)" src="https://github.com/hiddify/hiddify.com/assets/125398461/d8c66248-5b57-419e-a12f-4195501ee84c" width=70% />
</div>

The screenshots above are from an older version. The sign-in page now has separate fields for the ID and the password.

## If you lost your admin link

Connect to your server over SSH and run:

```bash
hiddify admin
```

It prints your admin links. Use a **Secure** `https` link with your domain. The link with the server's IP is "Not Secure"; use it only if the domain links do not work.

If you set a password and forgot it, reset the owner admin's password on the server with:

```bash
hiddify reset-password
```

!!! tip
    Save your full admin link somewhere safe, such as a password manager, so you always have it when you need it.

## How to change the parts of the link

- **Admin proxy path**: in the panel, open **Settings**, search for "Proxy Path for Admins", change it, and apply the changes. The panel then shows the new admin address.
- **Admin UUID**: open the **Admins** page, edit the admin, and change the UUID field. The old admin link for that admin stops working.

</div>
