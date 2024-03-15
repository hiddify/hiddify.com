---
title: Guide for setting up the domain and finalizing the installation (Initial setting after installation)
---

<div dir="ltr" markdown="1">

# Guide for setting up the domain and finalizing the installation
- [First step: Setting domain and subdomain](/manager/wiki/Guide-for-setting-up-the-domain-and-finalizing-the-installation#1-how-to-set-domain-and-subdomain)
- [Second step: reach the admin page after installing the script](/manager/wiki/Guide-for-setting-up-the-domain-and-finalizing-the-installation#2-reaching-the-admin-page-after-installing-the-script)
- [Step 3: Finalize the installation](/manager/wiki/Guide-for-setting-up-the-domain-and-finalizing-the-installation#step-3-finalize-the-installation)
***
After [installing the script](https://github.com/hiddify/hiddify-config/wiki#installation-guide); You must finalize the installation. This is done in 3 steps. First you need to register a domain.

## 1. How to set domain and subdomain
In the video below, all the steps of setting up the domain and subdomain are described in full detail. This video is in Farsi and if you watch the steps you can handle that. Although We are considering making some English videos for non-Persian people, till then you can visit this or follow the instructions in this article.
<div align=center markdown=1>
[![subdomain](https://img.youtube.com/vi/l-KKRus2KS0/maxresdefault.jpg)](https://www.youtube.com/watch?v=l-KKRus2KS0)
</div>

<details><summary><h3>Steps of setting up domain and subdomain</h3></summary>
- First, go to [this site](https://freedns.afraid.org/signup/) and create an account (It does not need your real information but the email must be correct)
<div align=center markdown=1>
![224300370-52b9a063-9265-4ff1-83e7-23970b6a4ecf](https://user-images.githubusercontent.com/125398461/228727381-0fb49767-a5dc-4e48-a0a5-21c2bb793e73.png)
</div>

- Activate the account via the email sent to you.
- Login to the created account and click on [this link](https://freedns.afraid.org/domain/registry/) and choose one of the publlic domains
<div align=center markdown=1>
![Screenshot_20230330_081052](https://user-images.githubusercontent.com/125398461/228738584-a12bacc8-9039-454b-8921-43ddee18d092.png)

</div>
It is better to choose domains with these extensions:

`com` , `net` , `org`  


- Enter your desired subdomain and the IP of your server.
<div align=center markdown=1>
![224301533-6743a65d-e45f-475c-a94d-7b6c428ffd84](https://user-images.githubusercontent.com/125398461/228729855-a95334af-a87e-4668-be7e-643a4d6a0a83.png)
</div>
 - Copy the created subdomain.

> These steps were only for direct domain if you want to know how to register other types of domain; Click [here](/manager/wiki/Domain-types-and-how-to-register-them).

</details>

## 2. Reaching the admin page after installing the script
You have done [the initial installation](https://github-com/hiddify/hiddify-config/wiki/#installation-guide) i.e. the script stage in 2 ways:
  - You have proceeded through the quick installation script in famous data centers (cloud-init);
  - or you have run the direct installation script on Ubuntu using SSH;

So, continue this step based on the method you have chosen.

> Important note: This program can only be installed on Ubuntu server versions 22.04.

<details markdown="1"><summary><h3>1.2. Continue installation in cloud-init mode</h3></summary>
If you have used quick installation scripts (cloud-init mode) for famous data centers such as Hetzner, Vultr, etc.; Therefore, in this case, a temporary link (valid for one hour) will be created for you.

#### What to do to reach the temporary link?
Wait at least 10 minutes. Then open the IP address in your browser. 

IP is a 4-part number separated by dot. `http://ip`

For example, if your IP is 1.1.1.1, you should enter the following address in your browser: `http://1.1.1.1`

Note: that temporary address is only active for one hour and after that it becomes inactive.
<div align=center markdown=1>
![Screenshot_20230325_144941en](https://user-images.githubusercontent.com/125398461/228808969-e289d4da-8857-45ec-96e6-353729e129ec.png)
</div>

You will reach the admin page by opening one time link.

</details>

<details markdown="1"><summary><h3>2.2. Continue installing directly on Ubuntu</h3></summary>
If you have used the installation method on Ubuntu; At the end of the installation, admin links will be generated in the terminal for you. Please make sure that the admin link is in the correct format. <a href="/manager/wiki/The-correct-format-of-admin-link">More information</a>

Open the link in the browser in order to enter the admin page.

</details>

## Step 3: Finalize the installation
When you open the admin page for the first time, quick installation settings will appears. Place the domain copied in the first step in the specified area as shown in the picture below.

![Screenshot_20230330_114622](https://user-images.githubusercontent.com/125398461/228776688-61847f37-72de-4111-9287-a0a733e62126.png)

Click the Submit button and then click `Apply Configs` to save the settings in the panel. [Go here](/manager/wiki/How-to-configure-Hiddify-Panel-properly#apply-configs) if you have a problem. If the changes are applied successfully; The panel is almost ready to use. 

For making the best use of this panel please view this [article](/manager/wiki/How-to-configure-Hiddify-Panel-properly).

### Reaching the connections for connecting to the proxy
For this, go to the users section in the software menu. Click on the user link to reach that user's page.

![2](https://user-images.githubusercontent.com/125398461/228784909-0e696cbc-b073-4c66-a660-88b5c0b87ee7.png)


On this page, the applications required for connection are introduced.

![apps](https://user-images.githubusercontent.com/125398461/228784738-3e9a2e69-8725-479c-a792-9b84298cb4ff.png)

You can also see the proxies created for that user at the bottom.
![Screenshot_20230330_1237592](https://user-images.githubusercontent.com/125398461/228791254-f968a44f-c18a-454b-9927-ac7fe4c32e6d.png)
Use the QR codes (highlighted yellow) or links for your client.