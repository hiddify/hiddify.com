---
title: How to contribute to this project
---

# How to contribute to this project
For this, you just need to install git on your system.

## Install git on the system
Open one of the following based on your operating system.
<details dir=ltr markdown="1"><summary><h3>Windows</h3></summary>

- First, go to [here](https://git-scm.com/download/win) and download the version for Windows.
- Then unzip the downloaded file and install it.
<div align=center>

![location-git-windows-download](https://github.com/hiddify/Hiddify-Manager/assets/125398461/cd883726-f340-441c-bbca-df98f0389de2)

</div>

- Then follow the installation wizard until the end with next and yes. It is recommended not to change the default settings.

<div align=center>

![read-and-accept-git-license-agreement](https://github.com/hiddify/Hiddify-Manager/assets/125398461/c8220a90-4f88-451f-ac60-ca6280feef20)

</div>
By default, the installation location of git is in this path.

```
C:/Program Files/Git
```

It means that in the next stages, the projects will be placed in this direction. The work is done.
- To check the version of `git` installed, open `command prompt` and run the following command.


```
git version
```


- By default, `git` is installed in the user's `Home` folder.
</details>

<details dir=ltr markdown="1"><summary><h3>Mac</h3></summary>

- First, download the installation file from [here](https://sourceforge.net/projects/git-osx-installer/files/git-2.23.0-intel-universal-mavericks.dmg/download?use_mirror=autoselect) .
- Then run it. It has a very simple installation.
- After installation, to check the installed `git` version, open `terminal` and run the following command.


```
git version
```



</details>

<details dir=ltr markdown="1"><summary><h3>Linux</h3></summary>

In most distributions of the Linux operating system, git is installed by default and you do not need to do anything special. But if you need to install it for any reason, you should search and find the appropriate command for that distribution. Next is the installation command related to the famous Ned distribution.

**Debian/Ubuntu**

```
sudo apt-get install git-all
```

**Fedora**

```
dnf install git-all
```

**Arch**
````
pacman -Syu git-all
````

In all distributions, git is installed in the home path of the user.
- Run this command to check the version of git installed in the terminal.


```
git version
```

</details>




## Using git to develop HiddifyManager project

- First you have to fork the project. For this, if you intend to fork the panel, execute the following command.


```
git clone https://github.com/hiddify/HiddifyPanel.git
```


If you want to fork Hiddify-Manager, run the following command.


```
git clone https://github.com/hiddify/Hiddify-Manager.git
```


For other repositories in the same way, it is enough to enter the repository and click on ``Code'' and in the ``Local'' tab, copy the address placed in ``HTTPS'' and put it in the above command.

<div align=center>

![Screenshot_20230807_180159](https://github.com/hiddify/Hiddify-Manager/assets/125398461/483dde4e-e4fd-470a-be94-552d5c72c2a8)

</div>

- Wait for a while until the project files are copied.

<div align=center>

![Screenshot_20230807_172554](https://github.com/hiddify/Hiddify-Manager/assets/125398461/b4730f3a-3f86-4792-8ccc-6a5789056c1d)

</div>

- Now you have to create a branch of the project to work on it. To do this, first choose a name for the branch. For example, suppose we choose the name of the branch ``Hiddify-develop''. Now run the following commands.


```
git branch Hiddify-develop
git checkout Hiddify-develop
```



- Now apply your desired changes to the files using any tool. It is recommended to use ``VSCode''.
- Do not forget that the path of all the files in the said folders is in the installation stage.
-
- Now, when you have applied the desired changes, you must also register the changes in ``git''. Therefore, run the following commands in the terminal in order.
- First, announce the changes to ``git'' with the following command.



```
git add
```


- Then commit the changes. You need to provide an explanation for the changes here.


```
git commit -m "a short description of the change"
```


For example, if the changes you are looking for are related to the bot development department, you can write such an explanation.



```
git commit -m "add some features to the telegram bot"
```


There is no problem if the explanations of this section are many, and by the way, it is recommended that the explanations be as complete and comprehensive as possible.
At this point, the changes have been successfully imported into the git system. Now you need to push the changes to GitHub. To do this, run the following command.


```
git push
```

Here, your GitHub account details will be asked. You need to enter your ``Username'' and ``Password'' in GitHub.


- Now log in to your GitHub account and open the forked project.
It has a path as follows:


`https://github.com/<your_username>/Hiddify-Manager`


- Now you see a banner that informs you that your branch is one step ahead of the main project. To merge the changes with the main project, click ``Contribute'' and click ``Open a pull request''.
- The work is done, the changes have been sent to the project. Now, after the approval of the project manager, your changes will be added to the project.
