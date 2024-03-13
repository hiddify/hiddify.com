<div dir="ltr" markdown="1">

# Guide for finding a clean Cloudflare IP
The largest CDN service provider in the world is Cloudflare, and you probably know; Due to the severe filtering of the Internet in Iran, there is a lot of disruption to its services because it is not possible for the filter to completely filter it, but it can cause disruption.
Here, if you also use CDN Cloudflare services; You will be affected by these disorders. To reduce the impact of these disturbances, you should find clean IPs (IPs that are not disturbed).

Here are some ways of working for this issue. 

Tip:
> Before starting, it is emphasized that all these tests must be done on the client system without connecting to VPN.

**Tables of contents:**
- [Using Bashsiz scanner](#using-bashsizs-scanner)
- [Using Farid scanner](#using-vahid-farids-scanner)
- [Using Safarian scanner](#using-safa-safarians-scanner)
- [What to do after finding a clean IP](#what-to-do-after-finding-a-clean-ip)
<br>
<br>

***
<br>
<br>

## Using Bashsiz's scanner
Mr. Bashsiz is an Iranian engineer who has developed a program called CFScanner, which can be used to test the list of Cloudflare IPs on different networks and reach the clean Cloudflare IPs.

This program has been released in several versions including Linux and Windows. Versions available until the date of editing this article:
- Bash
- Docker
- Windows
- Python
- Golang
- Android

To do this, first download the desired version [here](https://github.com/MortezaBashsiz/CFScanner) and then follow how to run it based on the desired operating system.


<details><summary><h3>Run on Linux version</h3> (Click here)</summary>

Download the program files and first see Mr. Bashsiz's explanation of how to run it in the video below (persian).

[![](https://user-images.githubusercontent.com/125398461/229997889-eaf51d2c-e5e1-4899-aa34-6c2c73375f10.png)](https://www.youtube.com/watch?v=BKLRAHolhvM)

This program has prerequisites that must be installed in advance.
[jq](https://stedolan.github.io/jq/)&nbsp;&nbsp;&nbsp;[git](https://git-scm.com/)&nbsp;&nbsp;&nbsp;[tput](https://command-not-found.com/tput)&nbsp;&nbsp;&nbsp;[bc](https://www.gnu.org/software/bc/)&nbsp;&nbsp;&nbsp;[curl](https://curl.se/download.html)&nbsp;&nbsp;&nbsp;
[parallel](https://www.gnu.org/software/parallel/)


Then first clone it on your system with the following code.
```
git clone https://github.com/MortezaBashsiz/CFScanner.git 
```
Go to the app download folder and run access to it. 
```
cd CFScanner/bash
chmod +x ../bin/*
```
Download the config.real file. 
```
curl -s https://raw.githubusercontent.com/MortezaBashsiz/CFScanner/main/bash/ClientConfig.json -o config.real
```
It is recommended to change the config.real file based on your configuration.
 
![PICTURE](https://user-images.githubusercontent.com/125398461/234565256-4ebeb511-4876-483a-84c5-cb39d62a12ae.png)


If you want to have your own configuration file, save it under a different name that will not change when the script is updated.

#### Run the script
Go to the location of the downloaded script file and then run the script as shown below.

```
bash cfScanner.sh SUBNET DOWN threads tryCount config.real speed custom.subnets
```

![222946688-bcec3d65-7bf1-495a-b1bf-fe517f69f8822](https://user-images.githubusercontent.com/125398461/234751332-e0fa6e6b-5b97-445b-bd50-12c9d603d556.png)


For example:


```
bash cfScanner.sh SUBNET DOWN 8 1 config.real 100 custom.subnets
```
Finally, the test result is placed in the `result` folder, which you can view and use. More information on the program [wiki](https://github.com/MortezaBashsiz/CFScanner/tree/main/bash).

</details>

<details><summary><h3>Run on Windows version</h3> (Click here)</summary>

<details><summary><h4>Prerequisites</h4></summary>
First, there must be prerequisites that will be explained in order:

- Download the Windows scanner app from [the project's GitHub](https://github.com/MortezaBashsiz/CFScanner/tree/main/windows)
- Install .NET Desktop Runtime 6 app from the main application site given below

```
https://dotnet.microsoft.com/en-us/download/dotnet/6.0
```

- Checking TLS Handshake
For this, you must first enter the program folder and open `Command Prompt` inside that folder. That is, `Shift+Right click` on the folder and select `Open in Windows Terminal`.

Run the following command in the terminal environment.

`‍‍.\v2ray.exe tls ping sub.yourdomain.com`

Put your subdomain instead of `sub.yourdomain.com`. If handshake `succeeded` message appears; It means that the scanner is ready to use, otherwise you should make temporary changes in the certificate settings on Cloudflare website.

Set the TLS version to TLS 1.0 and disable the TLS 1.3 option.

![Image](https://user-images.githubusercontent.com/125398461/234774581-c1a07bdb-352f-43cc-97f7-2ce6c87a761d.png)

* Note: Don't forget to return these options to the first state after testing.
* Prepare the config template structures for testing.
If you want to test your configurations, you must apply them in the Json file related to the connection in the program folder. This change needs to be applied in `inbound`.

```

{
  "inbounds": [{
    "port": "PORTPORT", 
    "listen": "127.0.0.1",
    "tag": "socks-inbound",
    "protocol": "socks",
    "settings": {
...
```
And also apply this change in `outbound`.

```
{
"outbounds": [
   {
   "protocol": "vmess",
   "settings": {
     "vnext": [{
       "address": "IP.IP.IP.IP",
...
```

Now, for ease of work, some examples of configuration templates that iSegaro has worked hard to present; You can choose one according to your needs.

* Be careful, in these structures, only in the `outbounds` part, you should change the configuration specifications including 5 parts `Port, UUID, PATH, HOST, SNI`, which are marked with the word `xxxxx`, so wherever there is the word `xxxxx`, change it only depending on your configuration. And do not change the rest of the codes.

- Example template for Vmess+WS+TLS :

```
{
  "inbounds": [{
    "port": "PORTPORT", 
    "listen": "127.0.0.1",
    "tag": "socks-inbound",
    "protocol": "socks",
    "settings": {
      "auth": "noauth",
      "udp": false,
      "ip": "127.0.0.1"
    },
    "sniffing": {
      "enabled": true,
      "destOverride": ["http", "tls"]
    }
  }],
  "outbounds": [
    {
    "protocol": "vmess",
    "settings": {
      "vnext": [{
        "address": "IP.IP.IP.IP", 
        "port": xxxxx,
        "users": [{"id": "xxxxx" }]
      }]
    },
		"streamSettings": {
        "network": "ws",
        "security": "tls",
        "wsSettings": {
            "headers": {
                "Host": "xxxxx"
            },
            "path": "xxxxx"
        },
        "tlsSettings": {
            "serverName": "xxxxx",
            "allowInsecure": false,
			"fingerprint": "chrome",
			"alpn": [
			"http/1.1"
			]
        }
    }
	}],
  "other": {}
}
```

- Example template for Vless+GRPC+TLS :

```
{
  "inbounds": [{
    "port": "PORTPORT", 
    "listen": "127.0.0.1",
    "tag": "socks-inbound",
    "protocol": "socks",
    "settings": {
      "auth": "noauth",
      "udp": false,
      "ip": "127.0.0.1"
    },
    "sniffing": {
      "enabled": true,
      "destOverride": ["http", "tls"]
    }
  }],
  "outbounds": [
    {
    "protocol": "vless",
    "settings": {
      "vnext": [{
        "address": "IP.IP.IP.IP", 
        "port": xxxxx,
        "users": [{"id": "xxxxx",
		"encryption": "none"
			}]
      }]
    },
		"streamSettings": {
        "network": "grpc",
        "security": "tls",
        "tlsSettings": {
          "allowInsecure": false,
          "serverName": "xxxxx",
          "alpn": [
            "http/1.1"
          ],
          "fingerprint": "chrome"
        },
        "grpcSettings": {
          "serviceName": "",
          "multiMode": false
        }
      }
	}],
  "other": {}
}
```

- Example template for Trojan+WS+TLS :

```
{
  "inbounds": [{
    "port": "PORTPORT", 
    "listen": "127.0.0.1",
    "tag": "socks-inbound",
    "protocol": "socks",
    "settings": {
      "auth": "noauth",
      "udp": false,
      "ip": "127.0.0.1"
    },
    "sniffing": {
      "enabled": true,
      "destOverride": ["http", "tls"]
    }
  }],
  "outbounds": [
    {
      "tag": "proxy",
      "protocol": "trojan",
      "settings": {
        "servers": [
          {
            "address": "IP.IP.IP.IP",
            "method": "chacha20",
            "ota": false,
            "password": "xxxxx",
            "port": xxxxx,
            "level": 1,
            "flow": ""
          }
        ]
      },
      "streamSettings": {
        "network": "ws",
        "security": "tls",
        "tlsSettings": {
          "allowInsecure": false,
          "serverName": "xxxxx",
          "alpn": [
            "http/1.1"
          ],
          "fingerprint": "chrome"
        },
        "wsSettings": {
          "path": "xxxxx",
          "headers": {
            "Host": "xxxxx"
          }
        }
      },
      "mux": {
        "enabled": false,
        "concurrency": -1
      }
    }
  ],
  "other": {}
}
```

- Example template for Vless+WS+TLS :

```
{
"inbounds": [{
    "port": "PORTPORT", 
    "listen": "127.0.0.1",
    "tag": "socks-inbound",
    "protocol": "socks",
    "settings": {
      "auth": "noauth",
      "udp": false,
      "ip": "127.0.0.1"
    },
    "sniffing": {
      "enabled": true,
      "destOverride": ["http", "tls"]
    }
  }],
  "outbounds": [
    {
      "tag": "proxy",
      "protocol": "vless",
      "settings": {
        "vnext": [{
        "address": "IP.IP.IP.IP", 
        "port": xxxxx,
        "users": [{"id": "xxxxx",
		"encryption": "none"
			}]
      }]
      },
      "streamSettings": {
        "network": "ws",
        "security": "tls",
        "tlsSettings": {
          "allowInsecure": false,
          "serverName": "xxxxx",
          "alpn": [
            "http/1.1"
          ],
          "fingerprint": "chrome"
        },
        "wsSettings": {
          "path": "xxxxx",
          "headers": {
            "Host": "xxxxx"
          }
        }
      }
    }
  ],
	"other": {}
}
```

Finally, present your configuration according to the examples for the next step or use the default configuration.




</details>

Now suppose you have completed the prerequisites; All you need is the config file of the sample program or the config file created by yourself, which is in Json format; From the menu `Tools > Add custom v2ray config`, put it in the program so that the scan is done based on it, otherwise the program will scan with the default configuration.

![App](https://user-images.githubusercontent.com/125398461/234803794-7c7f5bb9-0967-4f1b-b519-9db266b7a0e7.png)

1. From `Tools > Add custom v2ray config`, you can give the desired file according to the described pattern to the software so that the scan can be done based on it.

2. You can specify the download or upload test type or both.

3. In this section, you can specify the number of simultaneous IPs to be tested by the scanner. It is suggested to increase this number step by step and increase or decrease it based on the CPU processing power of your system. Its default value is 4.

4. The fastest IP will be displayed after the scan is completed

5. The range of tested IPs is displayed

6. From this section, you can give the software the IP range you want to scan based on it.

* **Suggestion:** You can set the software to scan the entire default IP range once. For the next time, you can just scan this output (with higher accuracy), you will probably get a better result. Also, if you take an upload test, you will probably get a better result. All this depends on your efforts and creativity.

</details>
<br>
<br>

***
<br>
<br>

## Using Vahid Farid's scanner
This program has been prepared in different versions based on different platforms that you can use according to your needs.

Versions available until the date of editing this article:
* Mac
* Windows
* Android
* Web
<details><summary><h3>Prerequisites</h3></summary>
- First, [download Python](https://www.python.org/downloads/) according to your operating system.
- Download the compressed file of the code [here](https://github.com/vfarid/cf-ip-scanner-py) and then extract it.
- Now you need to install requests.

```
pip install requests
```

</details>

<details><summary><h3>Run the program</h3></summary>
- Open the terminal program to run in the extracted folder. That is, for example, in Windows, enter the program folder and `Shift+Right click` and then click `Open in Command Prompt` to enter the terminal from that folder. 

- Now type the following command to run the program.

```
python start.py
```
- At first, you enter the required IP number.
- In the next step, enter the maximum delay you want in milliseconds. For example, 500 means 500 milliseconds
- You can choose the range you want to scan. Use comma to select multiple ranges and use `-` to ignore one range.
- You can exclude multiple sufferings from the search. Use comma to select multiple ranges and use `-` to ignore one range.
- In the next step, you can specify the size of the packets sent for scanning in kilobytes. The higher the volume, the higher the scanning accuracy, but on the other hand, the volume of traffic also increases.
- Set the download speed according to your needs so that it finds the IPs whose download speed is higher than this value. Enter the speed in Mbps.
- In the next step, set the upload speed according to your needs so that it finds the IPs whose upload speed is higher than this value. Enter this value in Mbps.
- In the next step, if needed, you can enter the scanned results directly into Cloudflare or ignore it until the scan starts.
- If you have typed `y` in the answer to the previous step, you must enter the email connected to your Cloudflare account here.
     Then copy the `Zone ID` in the next step. To find the `Zone ID`, enter the domain settings in your account, then find and copy the `Zone ID` as shown in the image below.

![Image](https://user-images.githubusercontent.com/125398461/235452066-9be0f0d9-e314-47cc-9565-4e05158b9d00.png)

- In this step, you need to give your global token to the software. For this, click on `Get your API token` on the main page of the dashboard.

![Image](https://user-images.githubusercontent.com/125398461/235454090-7a23c21a-fd1a-4fe8-9eb9-d9343402929b.png)

- Then, on the tokens page in `Global API Key`, select the `View` option.

![Image](https://user-images.githubusercontent.com/125398461/235454894-4e8bad4d-6561-4dec-9d5a-859ef0f64932.png)

- Here it will ask you for your account password and then display your token.

![Image](https://user-images.githubusercontent.com/125398461/235455122-9d39781e-bb9b-4abb-8c77-a4b68a07f048.png)

- Copy this token into the software.
- Then give the desired subdomain to register these IPs on your domain. For example, `cf.yourdomain.com`
- After that, the scanner will start scanning and at the end, the IPs will be displayed to you based on the given specifications. Also, if you have completed the IP registration section in Cloudflare, these IPs will also be registered in Cloudflare on the desired subdomain. That is, you will have subdomains in Cloudflare that are automatically registered with the name `cf.yourdomain.com` and with the IPs found by the scanner with the proxy turned off.

</details>

<br>
<br>

***
<br>
<br>

## Using Safa Safarian's scanner
This scanner has been developed in several versions that you can use according to your needs.

Versions available until the date of editing this article:
- Windows
- Mac
- Android

<details><summary><h3>Script installation</h3></summary>

<details><summary><h4>Windows</h4></summary>
* First, download Python from [this link](https://www.python.org/downloads/windows/).
* When installing Python, don't forget to check pip installation and add Python to PATH.
* Download the [original compressed scanner](https://github.com/SafaSafari/ss-cloud-scanner/archive/refs/heads/main.zip) file and extract it.
* Open a `Command Prompt` terminal in the extracted path. That is, enter the extracted path. Press `Shift+Right click` to open terminal.
* Use the following command to install the prerequisites.

```
pip install -r ./requirements.txt
```

- After installing the prerequisites, the work is finished and it is time to run the program.

</details>

<details><summary><h4>Android</h4></summary>

- To install on the Android operating system, you need a program called Termux, which you can download [here](https://github.com/termux/termux-app/releases/).
- Here you will come across several apk files from which you should select one based on your device type. If you do not know the type of your Android device, download and install armeabi-v7a version.
- Next, by opening the Termux program, the command line will be shown to you, enter the following commands in order.
- In the installation process, answer all the questions with `y`.

```
pkg update -y; pkg install -y python python-pip openssl python-cryptography
```

- Then run the following command.


```
curl -sLo main.zip https://github.com/SafaSafari/ss-cloud-scanner/archive/refs/heads/main.zip && unzip -qq main.zip && rm main.zip
```

- After that enter the program folder and install the prerequisites.


```
cd ss-cloud-scanner-main
pip install -r ./requirements.txt
```

- After installing the prerequisites, the work is finished and it is time to run the program.

</details>

</details>



<details><summary><h3>Run the script</h3></summary>

- With the following command, the program starts.


python main.py


* As soon as it runs, the program will ask you for the number of required IPs.
* In the next step, the type of scan can be specified.
* Then it will ask you to scan with `https` or `http`.
* And then it starts scanning and after some time healthy IPs (if any) will appear on the screen.
* If type 2 is selected, it will ask you for the `uuid`, `domain`, `port`, and `path` of the proxy used, and as soon as you enter them in the desired places, the scanning operation will begin. Thus mode 2 will scan with your config settings.

**Speed mode**

This type of scanning uses an alternative worker due to the whitelist of SNI in Iran, which greatly increases the efficiency of this scanning model.

**Vmess mode**
This scanning model practically simulates a proxy connection by creating a Vmess packet and sending it to the server with Websocket. Alternative scanners do this using V2ray or Xray kernels, but this scanner does this purely with Python. has implemented

[Refrence](https://github.com/SafaSafari/ss-cloud-scanner)

</details>





<br>
<br>

***
<br>
<br>

## What to do after finding a clean IP?
After finding a clean IP; You can register it with a DNS record without . That is, create a subdomain on Cloudflare. Turn off the proxy and enter the IP.

![PICTURE](https://user-images.githubusercontent.com/125398461/234565984-a2560018-7106-421f-850d-fb9db5687b26.png)

If you need more information about the domain, [click here](/manager/wiki/Domain-types-and-how-to-register-them).



Then in the Hiddify panel, you can put it in the CDN domain settings in the `Force to use host field in the CDN configuration`. [More details](/manager/wiki/How-to-configure-Hiddify-Panel-properly#cdn-domain)

![Screenshot_20230427_0656192](https://user-images.githubusercontent.com/125398461/234752684-280b90e8-0b00-4106-b744-b06117821b0f.png)
