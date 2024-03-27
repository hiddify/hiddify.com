---
title: How to import X-UI to HiddifyManager
---

# How to import X-UI to HiddifyManager

In HiddifyManager version 10, this feature has been added so that the X-UI panel can be imported. For this, just follow the steps below until the end.

- First, transfer the database file related to that panel to your server. We have already taught in [this article](/fa/manager/basic-concepts-and-troubleshooting/How-to-transfer-files-between-a-server-and-a-computer/) how to/from the server did the file transfer.
- Then use the following command to import the X-UI panel database file.

```bash
cd /opt/hiddify-manager/hiddify-panel/&&hiddifypanel xui-importer -x /path/to/db/file.db
```


   Instead of `</path/to/db/file.db>`, you should put the path of the database file.
  
   Suppose the database file is in the `root/` folder, in this case, use the above command as follows.

```bash
cd /opt/hiddify-manager/hiddify-panel/&&hiddifypanel xui-importer -x </root/file.db>
```

- The work is finished. The X-UI panel has been successfully moved to HiFi Manager.
> [!NOTE] 
> Due to the different structure of the X-UI panel, users and the amount of traffic consumed by them, which is the most important data related to that panel, are transferred.
