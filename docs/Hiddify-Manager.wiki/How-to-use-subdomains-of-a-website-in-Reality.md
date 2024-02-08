<div dir="rtl" markdown="1">

[**![Lang_Farsi](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://github.com/hiddify/Hiddify-Manager/wiki/%D9%86%D8%AD%D9%88%D9%87-%D8%A7%D8%B3%D8%AA%D9%81%D8%A7%D8%AF%D9%87-%D8%A7%D8%B2-%DA%86%D9%86%D8%AF%DB%8C%D9%86-%D8%B2%DB%8C%D8%B1%D8%AF%D8%A7%D9%85%D9%86%D9%87-%DB%8C%DA%A9-%D9%88%D8%A8%D8%B3%D8%A7%DB%8C%D8%AA-%D8%AF%D8%B1-%D8%B1%DB%8C%D8%A7%D9%84%DB%8C%D8%AA%DB%8C)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>


</div>


# How to use subdomains of a website in Reality

One way to help make real traffic less detectable is to split the traffic over different domains. That is, if it is possible to specify all the subdomains of a website and distribute traffic on them, this will help the filtering system to identify your server later.

- First, enter [this website](https://subdomainfinder.c99.nl/) and search for one of the websites you want. For example, this is a list of [all the subdomains related to the Speedtest site](https://subdomainfinder.c99.nl/scans/2023-11-20/speedtest.net) .

<div align=center>

![speedtest_subdomains](https://github.com/hiddify/Hiddify-Manager/assets/125398461/968b94b3-1899-43b2-a45a-19e71379ad17)

</div>

- You can also use [this website](https://crt.sh/) . For example, [the subdomains of the Firefox website](https://crt.sh/?q=mozilla.org) are specified in this website.

<div align=center>

![Firefox_subdomains](https://github.com/hiddify/Hiddify-Manager/assets/125398461/234710c2-dec4-436e-a478-c3bb2b0d2de7)


</div>

- Now you have a list of subdomains of a website. Just separate them with a comma and put them in the field of domain name or Servername or SNI corresponding to your real domain.

- Every time your sub-link is updated, one of these subdomains is selected as the address and in this way the traffic is divided on these subdomains. For example, if your app client automatically updates the subscription every 1 hour, then traffic is sent to one of these subdomains every hour, thus reducing the probability of the server being detected by the filtering system. [More information about Reality domain registration on Hiddify Manager](https://github.com/hiddify/Hiddify-Manager/wiki/How-to-use-Reality-on-Hiddify)