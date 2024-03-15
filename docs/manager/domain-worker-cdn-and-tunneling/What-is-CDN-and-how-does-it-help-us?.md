---
title: What is CDN and how does it help us?
---

<div dir="ltr" markdown="1">


# What is CDN and how does it help us?

Ever wondered what a `CDN` is and why we need it to implement some filter breakers? In general, what does `CDN` help us to bypass filtering? In this article, we are going to take a general look at the `CDN` structure and how it works and at the end answer this question so that you can configure and implement it with a more open mind. So if you are not familiar with how it works, stay with us until the end of this post.

## CDN performance overview
CDN or `Content Delivery Network` is a set of connected servers around the world that are responsible for fast data transfer. In the content distribution network, the data placed on the website or applications is cached or stored in the `CDN` servers and allows users around the world to exchange information with that website or application at a faster rate. It also reduces ping and jitter by its very nature, but how is this possible? Suppose you need to visit a website in Iran or exchange information through a special program with America. If your destination platform does not use a `CDN`, to exchange information, the sent packet must travel the entire network path to the destination to deliver the request, and this process must be done again to return the packets. Naturally, in this scenario, due to the long distance between the user and the main server, it will not be possible to send and receive at high speed, and the delay in loading and loading pages is clearly visible. However, if the content distribution network is used in the above scenario, all the data of that platform is stored in the Origin servers or the edge server and the user is connected to the nearest edge server based on their geographical area and with faster speed and less delay than exchanging information with The destination takes action. In the picture below, you can see the overview of this scenario.

<div align=center markdown=1>
![photo_2023-06-07_20-03-37](https://github.com/hiddify/hiddify-config/assets/125398461/d0e44fdf-b494-4881-ad99-13d5824a9f83)
</div>



Now the question may be raised to you, what is the need to use this content distribution network in setting up the filter breaker with this account? Above we mentioned one of the benefits of using this technology, but the story does not end here. The important and vital thing that is used to set up filtering servers on this platform is that your server's IP is not identified from the point of view of regulatory bodies and filtering systems. As mentioned above, during the exchange of information with the destination server, the user is connected to the Origin Servers instead of direct communication, and these edge servers are responsible for exchanging information with the main server. With this account, the IP of your server remains hidden from the eyes of government monitoring institutions, and its filtering becomes remarkably impossible! Let's see the test and the result practically. Here we create an A record in Cloudflare and turn off the proxy (the ability to use CDN) for it so that the created subdomain does not use the `CDN` ability and is directly connected to the main server.

<div align=center markdown=1>
![photo_2023-06-07_20-04-15](https://github.com/hiddify/hiddify-config/assets/125398461/09f0c5f3-e5d0-41c6-81da-ac3e016ebc6b)

</div>


Then ping the created subdomain:

<div align=center markdown=1>
![244136935-16868a83-6991-43f2-9969-1802801eb12f](https://github.com/hiddify/hiddify-config/assets/125398461/bc5757b6-001a-4b08-a678-5264fe60e51b)

</div>



As you can see in the image above, the main IP of the server can be identified and filtered easily. In the next test, we enable the proxy option for the created subdomain and compare the results:

<div align=center markdown=1>
![photo_2023-06-07_20-04-54](https://github.com/hiddify/hiddify-config/assets/125398461/0705bdaf-2e9a-4f3a-9c76-e966d5b2db6c)
</div>

<div align=center markdown=1>
![photo_2023-06-07_20-05-11](https://github.com/hiddify/hiddify-config/assets/125398461/fa4c2070-3d9c-4e04-9fce-46d3bf501998)

</div>


In this case, the test output is no longer the IP of the main server, but the IP of the edge servers that are closest to you and connected to. Also, in order to better understand how to reduce ping and jitter and increase speed when using CDN, we checked the route taken by packets by `Tracing Route`. The images below show that when using a CDN, the access path to the server is much shorter, so that in this example, the packets pass through more than 10 routers in direct mode, and this problem causes more delay and decreases its speed and performance.

<div align=center markdown=1>
![photo_2023-06-07_20-05-37](https://github.com/hiddify/hiddify-config/assets/125398461/a257a199-b7f7-48a5-8734-2364c9338326)
</div>

<div align=center markdown=1>
![photo_2023-06-07_20-05-46](https://github.com/hiddify/hiddify-config/assets/125398461/ebca35d6-0ffa-4ec1-8bf7-87fda03aed7c)
</div>


## The reason why Cloudflare is not completely filtered
Now, you may be wondering why government institutions have not completely filtered Cloudflare and other disruptions have been applied to the IPs under its control? It should be noted that Cloudflare is one of the largest and most unique content distribution networks in the world, which provides many services and tools to users. Many Iranian websites and service providers also use its services, and if Cloudflare is completely filtered, access to a large part of Iranian services will be blocked. For this reason, regulatory bodies act through other methods to disrupt this platform.