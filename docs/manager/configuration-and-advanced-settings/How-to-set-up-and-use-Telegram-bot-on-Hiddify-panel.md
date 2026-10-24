---
title: How to set up and use Telegram bot on HiddifyManager
weight: -130
---

<div dir="ltr" make ="1">

# How to set up and use Telegram bot on HiddifyManager
This page shows you how to connect your Hiddify Manager panel to your own Telegram bot. With the bot you can create and manage users from Telegram, check the server status, and receive the panel's automatic backups. Your users can also link their Telegram to get notices when their package is about to end.

**Prerequisites**

- Admin access to your Hiddify Manager panel.
- A Telegram account.

!!! note
    The screenshots on this page are from an older version of the panel and the bot. The menus now look different, but the steps are the same.

## Step 1: Create a Telegram bot
1. Open Telegram and search for `@BotFather`. This is Telegram's official bot for creating bots.

    <div align=center markdown=1>
    ![BotFather in Telegram search](https://user-images.githubusercontent.com/125398461/235900298-c2251db5-2b14-4a45-b4c3-1b1c857a64b4.png)
    </div>

2. Tap **Start**.

    <div align=center markdown=1>
    ![Start BotFather](https://user-images.githubusercontent.com/125398461/235900621-1d8143fa-a56d-4c01-9f7c-3b96b1772191.png)
    </div>

3. Send `/newbot` (or choose it from the menu).

    <div align=center markdown=1>
    ![The /newbot command](https://user-images.githubusercontent.com/125398461/235900712-3f6cb0c2-4107-473c-affa-5af47ff1f2d0.png)
    </div>

4. Send a name for your bot. Then send a unique username for it.

    <div align=center markdown=1>
    ![Choosing the bot name and username](https://user-images.githubusercontent.com/125398461/235904011-8d51583c-3c39-4a88-99c5-ee71d0016631.png)
    </div>

    - The username must end with `bot` (for example `my_vpn_bot`).
    - You can use `_` in the username.

5. BotFather now sends you a **token**: a long code like `123456789:AA...`. Copy it. Keep it secret: anyone with the token can control your bot.

    <div align=center markdown=1>
    ![The bot token](https://user-images.githubusercontent.com/125398461/235904260-f6f582d3-f4e6-4829-951b-0f4f7540f4a0.png)
    </div>

## Step 2: Add the token to the panel
1. Open your admin panel.
2. In the sidebar, under **Settings**, click **Settings**.
3. Find the **Telegram Bot Token** field in the **Telegram Configs** section. (You can also type "Telegram" in the search box at the top of the page.)
4. Paste the token you copied.
5. Click **Save**.

    <div align=center markdown=1>
    ![The Telegram Bot Token field](https://user-images.githubusercontent.com/125398461/235904497-84682dd3-8774-4d06-9391-d662d884b64e.png)
    </div>

If it worked, the panel shows "Telegram bot connected: @your_bot_username", and a **Telegram Bot** item appears in the sidebar under **Settings**.

<div align=center markdown=1>

![The Telegram Bot item in the menu](https://user-images.githubusercontent.com/125398461/235912447-776ce7fd-65ed-4c4a-b6c8-b7b828ab8aea.png)

</div>

If you see "Telegram bot could not connect", check that you pasted the whole token with no extra spaces, and that your server can reach Telegram.

## Step 3: Link your admin account to the bot
1. In the panel sidebar, click **Telegram Bot**. Telegram opens your bot.
2. Tap **Start**.

<div align=center markdown=1>
![Starting the bot](https://user-images.githubusercontent.com/125398461/235907744-d16631e7-aa15-477e-9f05-34c5a90c80bf.png)
</div>

For security, the bot only recognises you as an admin when you open it from this link. Each admin can link their own Telegram account in the same way. You can also link it from **My account** → **Connect Telegram**.

## Using the bot
After you start it, the bot shows your admin menu with these buttons:

- **👥 Users**: list your users. You can filter them (for example, users whose package is ending soon) or type a name to search. Open a user to renew their package, add days or data, reset their usage, enable, disable or delete them, and see their links and QR code.
- **➕ New user**: create one or more users.
- **📊 Server status**: CPU, RAM, disk, uptime, traffic and online users.
- **💾 Backup**: get a backup file of the whole panel right now (super admins only).
- **🖥 Open panel**: open your admin panel.

### Create a user from the bot
1. Tap **➕ New user**.
2. Choose how much data the package has.

    <div align=center markdown=1>
    ![Choosing the data amount](https://user-images.githubusercontent.com/125398461/235907850-1e613a61-6506-45a5-bc8c-eda7a718048c.png)
    ![A 4 GB package selected](https://user-images.githubusercontent.com/125398461/235908017-f4c5b463-c40e-4524-a08d-90e7f7e395c2.png)
    </div>

3. Choose how many days the package lasts.

    <div align=center markdown=1>
    ![Choosing the number of days](https://user-images.githubusercontent.com/125398461/235908369-39e536f7-150d-4498-828b-b8861089d7b1.png)
    </div>

4. Choose how many users to create with these limits.

    <div align=center markdown=1>
    ![Choosing the number of users](https://user-images.githubusercontent.com/125398461/235908551-11ca06da-25db-4db2-9ca5-20240b04fd15.png)
    </div>

5. Optional: tap **✏️ Name** and send a name for the user.
6. Tap **✅ Create**.

The bot sends you one card per new user, with the user's links. You can forward the card to the user.

<div align=center markdown=1>
![The new user's card](https://user-images.githubusercontent.com/125398461/235908927-0835b813-14e1-4c8f-9aa8-3c8398eaa6c1.png)
</div>

The new user also appears in the panel's **Users** page.

<div align=center markdown=1>
![The new user in the panel](https://user-images.githubusercontent.com/125398461/235909045-f7581a57-5cb7-4df3-ad3d-9293bbdc8ba2.png)
</div>

Tap **🔄 Refresh** on a user's card to see their latest data usage and remaining days.

<div align=center markdown=1>
![Refreshing a user's status](https://user-images.githubusercontent.com/125398461/235909484-c3b6064d-afb5-4654-8c01-84acb55becd4.png)
</div>

### Automatic backups
When your admin account is linked to the bot, each automatic backup of the panel is also sent to you in Telegram. You can manage backups in the panel under **Settings** → **Backup**. See [How to backup and restore the panel](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/).

## Users and the bot
Your users can link their own Telegram to the bot. To do this, a user opens your bot and taps **Start**, then sends their subscription link or UUID, or taps the Telegram button on their account page. After that:

- They can see their remaining data and days, and their links, in the bot.
- The bot warns them when their package is about to end.
- You can send them messages from the panel: in the sidebar, under **Manager**, click **Send message**. Only users who have started your bot receive messages.

<div align=center markdown=1>
![Sending a message to users](https://user-images.githubusercontent.com/125398461/235909375-a9abc059-c4e1-4fe6-ba65-630e3704ba20.png)
</div>

</div>
