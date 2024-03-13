<div dir="ltr" markdown="1">


# Installing Hiddify using Docker
Before installation please pay attention that Docker version is still experimental and may have some problems, please let us know about bugs. Docker version is not recommended for permanent use.

For installation this way, just use the following code:

```
git clone https://github.com/hiddify/hiddify-config
cd hiddify-config
touch hiddify-panel/hiddifypanel.db
docker-compose up -d
```
Please note that the Docker version is still experimental and may have some bugs, please let us know about errors using [this link](https://github.com/hiddify/hiddify-config/issues). 
Now we need to setup the domain and finalize the installation. [(visit this article)](/manager/wiki/Guide-for-setting-up-the-domain-and-finalizing-the-installation)

For making the best use of this panel visit this [page](/manager/wiki/How-to-configure-Hiddify-Panel-properly)