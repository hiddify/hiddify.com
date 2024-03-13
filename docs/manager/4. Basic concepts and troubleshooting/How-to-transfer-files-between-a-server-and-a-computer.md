


# How to transfer files between a server and a computer
Many times you need to transfer files to/from server. For example, you want to remove the backup file or import a file from your system to the server. There are several methods for this.


## prerequisites

To do this, open one of the following programs according to your operating system.

- Windows: `PowerShell`
- Mac: `Terminal`
- Linux: `Terminal`
> Note: In Windows, if SSH is not installed, run the following command in PowerShell to install it.

```
Add-WindowsCapability -Online -Name OpenSSH.Client
```

<div align=center markdown=1>
<img src="https://user-images.githubusercontent.com/114227601/222904870-e709f69e-1a8d-4a6d-ad6a-3d7bdcd917c3.png" />
</div>

## Viewing the list of backup files on the server

To be able to see the list of backup files on the server, first SSH to the server and run the following command.

```
ls /opt/hiddify-config/hiddify-panel/backup
```

The output of this command is as follows.

<div align=center markdown=1>
<img src="https://github.com/hiddify/hiddify-config/assets/125398461/924b149e-6ec8-4b48-8fbb-ad99a234ee5e" />
</div>

Select one of the backup files to transfer.

## Transfering the file from the server to the system via scp command
Use this command in the terminal.

`scp <user>@<Server's IP>:<path/to/your/file> "Path\in\your\PC"`

For example, if the user of your server is `root` and its IP is `1.1.1.1`, you want to remove the backup panel file from your server and enter it into the `Backup` folder in the `C` drive of your system, in this case you must enter the following command.

```
scp root@1.1.1.1:/opt/hiddify-config/hiddify-panel/backup/2023_05_06__06_00_03.json "C:\Backup"\
```

The work is done. The desired file was copied to the Backup folder.

## Transfering the file from the system to the server via scp command
For this, suppose your server user is `root` and its IP is `1.1.1.1`. Also suppose that the `text.txt` file is located in `C:\File` and you want to transfer it to the server. In this case, use the following command.

```
scp "C:\File\text.txt" root@1.1.1.1:/opt/hiddify-config
```
In this case, the `text.txt` file will be copied on the server in the desired path and you can view it with the following command.

```
ls /opt/hiddify-config
```
## Using the web to transfer files

Another way to transfer files is to use SSH service sites. To do this, first enter the details of your server for SSH, and after connecting, the File Manager of the system will open. You can easily transfer your desired files through the web.

