---
title: How to use GCore CDN
description: Set up Gcore CDN for a subdomain whose DNS is on Cloudflare, and add it to HiddifyManager.
---

<div dir="ltr" markdown="1">

# How to use GCore CDN on Cloudflare registered domain

Cloudflare is sometimes disrupted in Iran. One alternative is Gcore's CDN. In this tutorial your domain's DNS stays on Cloudflare, and only one subdomain (for example `gcore.yourdomain.com`) is handed to Gcore with a `CNAME` record.

Before you start, you need an active domain on Cloudflare. See [How to use Cloudflare CDN](/manager/domain-worker-cdn-and-tunneling/How-to-use-Cloudflare-CDN/).

!!! info "Cost"
    According to [Gcore's pricing page](https://gcore.com/pricing/edge-network), the pay-as-you-go (PAYG) plan includes 1 TB of free CDN traffic a month; more than that is paid. Prices can change, so check that page before you start.

## 1. Make an account and a CDN resource on Gcore

1. Make an account on the [Gcore website](https://gcore.com) and open the dashboard.
2. Open **CDN** in the side menu. The first time, you see **Welcome to Gcore CDN**: click **Get started for free** (no credit card needed).

    <img style="display:block;margin:0 auto" width=700 alt="Welcome to Gcore CDN and the Get started for free button" src="/assets/manager/How-to-use-GCore-CDN-on-Cloudflare-registered-domain/gcore-welcome.webp">

3. The **Set up your Edge Network resource** form opens:
    - Under **Domain**, click **Use your own domain** and type your subdomain, for example `gcore.yourdomain.com`.
    - Under **Origin**, choose **URL / IP** and enter your server's IP.
4. Click **Set up your resource**.

    <img style="display:block;margin:0 auto" width=700 alt="The CDN resource form: your own domain, your server IP and Set up your resource" src="/assets/manager/How-to-use-GCore-CDN-on-Cloudflare-registered-domain/gcore-create.webp">

5. You see **Edge Network resource is created!**. The **DNS change required** box shows the `CNAME` record you need: **Host** is your subdomain and **Value** looks like `cl-xxxxxxxx.gcorecdn.com`. Copy the **Value**.

    <img style="display:block;margin:0 auto" width=700 alt="Resource created: the DNS change required box with the CNAME record, and Open resource settings" src="/assets/manager/How-to-use-GCore-CDN-on-Cloudflare-registered-domain/gcore-created.webp">


## 2. Make the CNAME record on Cloudflare

1. On Cloudflare, select the domain, go to **DNS** > **Records** and click **Add record**.
2. Fill it in like this and click **Save**:
    - **Type**: `CNAME`
    - **Name**: the subdomain, for example `gcore`
    - **Target**: the value you copied from Gcore
    - **Proxy status**: off (**DNS only**, grey cloud). If it is on, the traffic goes through Cloudflare instead of Gcore.

    ![CNAME record on Cloudflare with the proxy off](https://github.com/hiddify/hiddify.com/assets/125398461/519004ac-c33e-4489-a224-47cc9d35b3b1)

3. On Gcore, in the resource's **Setup guide** (at the top of the resource settings), click **Check DNS setup status**. When you see **DNS record has been successfully set up**, the DNS is right. This can take up to 24 hours.

    <img style="display:block;margin:0 auto" width=450 alt="Setup guide: the CNAME record and Check DNS setup status" src="/assets/manager/How-to-use-GCore-CDN-on-Cloudflare-registered-domain/gcore-setup-guide.webp">

## 3. Set up the CDN resource on Gcore

On the same page click **Open resource settings** (or open the resource from **CDN** > **CDN resources**) and set these three things. Click **Save changes** after each change; applying it on all Gcore servers takes about 15 minutes.

1. **Protocol to your server**: in the **OPTIONS** tab > **General**, under **Origin pull protocol**, choose **HTTPS**.

    <img style="display:block;margin:0 auto" width=700 alt="Origin pull protocol with HTTPS chosen, and Save changes" src="/assets/manager/How-to-use-GCore-CDN-on-Cloudflare-registered-domain/gcore-origin-https.webp">

2. **SSL certificate**: in the **SSL** section, turn on **Enable HTTPS**, choose **Free Let's Encrypt certificate** and click **Get SSL certificate**. Issuing takes up to 15 minutes and only works once the `CNAME` record from step 2 is right.

    <img style="display:block;margin:0 auto" width=700 alt="SSL section: Enable HTTPS, Free Let's Encrypt certificate and Get SSL certificate" src="/assets/manager/How-to-use-GCore-CDN-on-Cloudflare-registered-domain/gcore-ssl.webp">

3. **WebSockets**: in **Content** > **WebSockets**, turn on **Enable WebSockets** and click **Save changes**. It is off by default, and WebSocket configs don't connect without it.

    <img style="display:block;margin:0 auto" width=700 alt="WebSockets section: Enable WebSockets and Save changes" src="/assets/manager/How-to-use-GCore-CDN-on-Cloudflare-registered-domain/gcore-websockets.webp">

!!! note "WAAP protection"
    Gcore turns on WAAP protection for a new resource in "monitoring mode". If you later switch it to blocking, WebSocket connections may be refused with a `403` error.

## 4. Add the subdomain to HiddifyManager

1. In the panel side menu, in the **Settings** group, open **Domains** and click **Add domain**.
2. In the **Domain** step, enter the subdomain (for example `gcore.yourdomain.com`) and click **Check**.
3. In the **Mode** step, under **How is it set up?**, choose **CDN**, keep **Valid TLS** and click **Next**.

    <img style="display:block;margin:0 auto" width=600 alt="Add a domain wizard, Mode step: CDN selected" src="/assets/manager/How-to-use-GCore-CDN-on-Cloudflare-registered-domain/en-domain-mode.webp">

4. Finish the **Name** and **Certificate** steps to add the domain.

If **Show configs of** on your user-page domain is set to **All domains**, the new configs are added to the subscription link by themselves. Ask your users to update the subscription in their app.

</div>
