---
title: Guide for setting up the domain and finalizing the installation (Initial setting after installation)
weight: -85
---

<div dir="ltr" markdown="1">

# Guide for setting up the domain and finalizing the installation

After you [install Hiddify Manager](/manager/installation-and-setup/guide/), you need to finish the setup. This page walks you through it in three steps:

1. Get a domain (or subdomain) that points to your server.
2. Open the admin panel.
3. Enter your domain in the panel and get your connection links.

A **domain** is a name like `example.com` that points to your server's IP address, so you and your users don't have to use the bare IP. A **subdomain** is a name under a domain, like `vpn.example.com`.

!!! note "Screenshots"
    The screenshots on this page come from older versions of the panel. Your screens may look different, but the steps are the same.

## Step 1: Get a domain and subdomain

If you already have a domain, create a subdomain for your server's IP address in your domain's DNS settings and skip to step 2.

If you don't have a domain, you can get a free subdomain from FreeDNS. The video below (in Persian) shows all the steps.

<div align=center markdown=1>

[![Video: registering a subdomain](https://img.youtube.com/vi/l-KKRus2KS0/maxresdefault.jpg)](https://www.youtube.com/watch?v=l-KKRus2KS0)

</div>

<details markdown=1><summary>Steps to get a free subdomain from FreeDNS</summary>

1. Go to [freedns.afraid.org](https://freedns.afraid.org/signup/) and create an account. You don't need to give real personal information, but the email address must be correct.

    ![FreeDNS sign-up page](https://user-images.githubusercontent.com/125398461/228727381-0fb49767-a5dc-4e48-a0a5-21c2bb793e73.png)

2. Open the email FreeDNS sent you and click the activation link.
3. Log in, open the [domain registry](https://freedns.afraid.org/domain/registry/) and choose one of the public domains. Domains ending in `.com`, `.net` or `.org` are a good choice.

    ![FreeDNS public domain list](https://user-images.githubusercontent.com/125398461/228738584-a12bacc8-9039-454b-8921-43ddee18d092.png)

4. Enter the subdomain name you want and your server's IP address, then save.

    ![Adding a subdomain with the server IP](https://user-images.githubusercontent.com/125398461/228729855-a95334af-a87e-4668-be7e-643a4d6a0a83.png)

5. Copy the subdomain you created. You need it in step 3.

</details>

These steps create a **direct** domain (it points straight to your server). To learn about other domain types, such as CDN domains, see [Domain types and how to register them](/manager/domain-worker-cdn-and-tunneling/Domain-types-and-how-to-register-them/).

## Step 2: Open the admin panel

How you open the panel depends on how you installed Hiddify.

<details markdown="1"><summary>If you used cloud-init (Hetzner, Vultr, OVH, ...)</summary>

The installer creates a temporary link that works for **one hour**.

1. Wait at least 10 minutes after the server starts.
2. Open your server's IP address in your browser. An IP address is four numbers separated by dots. For example, if your IP is `1.1.1.1`, open `http://1.1.1.1`.
3. Click the link on that page to reach the admin panel.

<div align=center markdown=1>

![Temporary setup page opened by IP address](https://user-images.githubusercontent.com/125398461/228808969-e289d4da-8857-45ec-96e6-353729e129ec.png)

</div>

If the hour has passed, use the SSH method below to get the admin links.

</details>

<details markdown="1"><summary>If you installed over SSH</summary>

At the end of the installation, the installer shows your admin links in the terminal. Open one of them in your browser.

- Prefer the links marked **Secure** (with your domain and `https://`). Use the **Not Secure** IP link only if the others don't work yet.
- An admin link looks like `https://your-domain/admin-path/your-admin-id/`. More about this: [The correct format of the admin link](/manager/domain-worker-cdn-and-tunneling/The-correct-format-of-admin-link/).

To see the admin links again, connect to your server over SSH and run:

```bash
hiddify admin
```

If you forgot the admin password, you can reset it with:

```bash
hiddify reset-password
```

</details>

## Step 3: Finalize the installation

1. The first time you open the admin panel, a quick setup wizard opens. It asks for the panel language, an admin password and your domain.
2. Enter the domain you copied in step 1 in the domain field.

    ![Quick setup: entering the domain](https://user-images.githubusercontent.com/125398461/228776688-61847f37-72de-4111-9287-a0a733e62126.png)

3. Save. If the panel says that changes need to be applied, apply them and wait until it finishes.

If something goes wrong, read [How to configure the Hiddify panel properly](/manager/configuration-and-advanced-settings/How-to-configure-Hiddify-panel-properly/).

## Get your connection links

1. In the admin panel, go to the **Users** section.
2. Click a user's link to open that user's page.

    ![Users list in the admin panel](https://user-images.githubusercontent.com/125398461/228784909-0e696cbc-b073-4c66-a660-88b5c0b87ee7.png)

3. The user page shows the apps you can use to connect.

    ![Apps listed on the user page](https://user-images.githubusercontent.com/125398461/228784738-3e9a2e69-8725-479c-a792-9b84298cb4ff.png)

4. Lower on the page you see the proxies created for that user. Scan a QR code (highlighted in yellow) with your app, or copy a link into it.

    ![User proxies with QR codes](https://user-images.githubusercontent.com/125398461/228791254-f968a44f-c18a-454b-9927-ac7fe4c32e6d.png)

We recommend [Hiddify App](/app/How-to-install-Hiddify-app/) to connect; it works on Android, iOS, Windows, macOS and Linux.

This page only covers a quick start. The panel can do much more: read [How to configure the Hiddify panel properly](/manager/configuration-and-advanced-settings/How-to-configure-Hiddify-panel-properly/) to get the most out of it.

</div>
