<div dir="rtl" markdown="1">

[**![Lang_farsi](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png) &nbsp;فارسی**](https://github.com/hiddify/hiddify-next/wiki/%DA%86%DA%AF%D9%88%D9%86%D9%87-%D9%85%DB%8C%E2%80%8C%D8%AA%D9%88%D8%A7%D9%86-%D8%AF%D8%B1-%D8%A7%DB%8C%D9%86-%D9%BE%D8%B1%D9%88%DA%98%D9%87-%D9%87%D9%85%DA%A9%D8%A7%D8%B1%DB%8C-%D9%86%D9%85%D9%88%D8%AF)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-next/wiki"><img width="100" src="https://github.com/hiddify/hiddify-next/assets/125398461/e285886d-21c6-4208-aeed-ecfd28cd20af" /></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/hiddify/hiddify-config/wiki/All-tutorials-and-videos"><img width="100" src="https://github.com/hiddify/hiddify-config/assets/125398461/8ac5b906-105c-4b98-acf5-0e12e39e33f6" /></a>
</div>
<br>


# How to contribute to this project

For this, you just need to install git on your system.


## Install git on the system
Open one of the following based on your operating system.

<br>
<details dir=ltr><summary><b>Install git on Windows</b></summary>

- First, go [here](https://git-scm.com/download/win) and download the Windows version.
- Then unzip the downloaded file and install it.




- Then follow the installation wizard to the end with `Next` and `Yes`. It is recommended not to change the default settings.


- By default, the installation location of `git` is in this path.

`C:/Program Files/Git`

- It means that in the next stages, the projects will be placed in this direction. The work is done. 

- To check the version of `git` installed, open `command prompt` and run the following command.

```
git version
```

- By default, `git` is installed in the user's `Home` folder.

</details>

<br>
<details dir=ltr><summary><b>Install git on Mac</b></summary>

- First, go [here](https://sourceforge.net/projects/git-osx-installer/files/git-2.23.0-intel-universal-mavericks.dmg/download?use_mirror=autoselect) and download the Mac version.
- Then run it. It has a very simple installation.
- After installation, to check the installed `git` version, open the terminal and run the following command.
```
git version
```
</details>

<br>
<details dir=ltr><summary><b>Install git on Linux</b></summary>

In most distributions of the Linux operating system, git is installed by default and you do not need to do anything special. But if you need to install it for any reason, you should search and find the appropriate command for that distribution. Next is the installation command related to the famous Ned distribution.

_**Debian/Ubuntu**_
```
sudo apt-get install git-all
```

_**Fedora**_
```
dnf install git-all
```

_**Arch**_
```
pacman -Syu git-all
```

In all distributions, git is installed in the `Home` path of the user.
- Run this command to check the version of git installed in the terminal.
```
git version
```
</details>

## Using `git` to develop HiddifyNext
- First you need to `fork` the project. For this, if you intend to `fork` the project, execute the following command.

```
git clone https://github.com/hiddify/hiddify-next.git
```
- Wait a while for the project files to be copied.
- Now you have to create a branch of the project to work on it. To do this, first choose a name for the branch. For example, suppose we choose the branch name `Hiddify-develop`. Now run the following commands.

```
git branch Hiddify-develop
git checkout Hiddify-develop
```
- Now apply your desired changes to the files using any tool. It is recommended to use `VSCode`.
- Do not forget that the path of all the files in the mentioned folders is in the installation stage.
- Now, when you have applied your desired changes, you must also register the changes in `git`. Therefore, run the following commands in the terminal in order.
- First, announce the changes to `git` with the following command.

```
git add
```

- Then commit the changes. You need to provide an explanation for the changes here.
```
git commit -m "a short description of the change"
```
For example, if the changes you are looking for are related to the core department, you can write such an explanation.
```
git commit -m "add some features to the core"
```

There is no problem if the explanations of this section are many, and by the way, it is recommended that the explanations be as complete and comprehensive as possible.

At this point, the changes have been successfully imported into the `git` system. Now you need to push the changes to `GitHub`. To do this, run the following command.

```
git push
```

Here, your GitHub account details will be asked. You need to enter your `username` and `password` on GitHub.

- Now log in to your GitHub account and open the forked project. It has a path as follows:

`https://github.com/<your_username>/hiddify-next`

- Now you will see a `banner` that informs you that your `branch` is one step ahead of the main project. To `merge` the changes with the main project, click `Contribute` and `Open a pull request`.
- It's done, the changes have been sent to the project. Now, after the approval of the project manager, your changes will be added to the project.

<br>

**The app is developed using [Flutter](https://flutter.dev) and [Go](https://go.dev). For more information you can read through our [Contribution Guidelines](https://github.com/hiddify/hiddify-next/blob/main/CONTRIBUTING.md) for development.**