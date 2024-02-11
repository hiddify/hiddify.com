<div dir="rtl" markdown="1">

[**![flag_of_Iran](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://docs.hiddify.com/fa/Hiddify-Manager.wiki/%DA%A9%D8%A7%D8%B1%D8%A8%D8%B1%D8%AF-%D9%88-%D9%86%D8%AD%D9%88%D9%87-%D8%B9%D9%85%D9%84%DA%A9%D8%B1%D8%AF-%D9%81%D8%B1%DA%AF%D9%85%D9%86%D8%AA)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>

</div>

# What is the fragment and how does it work?

Normally, when you want to send a request to open sites and apps to the Internet, SNI may be detected by the filtering system. SNI or server name is actually the main destination of the sent packets that we try to keep hidden from the filtering system with different protocols. But many times it can be detected for various reasons, including the use of weak SNI protocols.

Now the fragment breaks the sent packets into pieces. In this case, SNI is sent in several pieces and thus cannot be detected by the filtering system. And

In the picture below, you can see that the request to open `www.bbc.com` is filtered, and if this request is sent normally, the desired page will probably be blocked by the filtering system and a fake page will be opened for you.

Now, if this request is sent in several pieces, it can bypass this system and after passing through the filtering system, these pieces will join each other on the server.

<div align=center markdown=1>
<img width=70% src="https://github.com/hiddify/hiddify-config/assets/125398461/de4c0b72-cf9b-42a6-a8ea-63990b7f7ddb" />
</div>

## Different fragment modes

#### Default

The fragment is considered based on the default in the config.

#### SNI or domain mode

It splits the packets into two pieces and sends them.

#### Random mode

It transforms the packets into random chunks,that is, the packets are divided into very small pieces and then sends them.

## How to use fragment

Just set the fragment setting in the HiddifyN and HiddifyNG application settings in the advanced menu.
