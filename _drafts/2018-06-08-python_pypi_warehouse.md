搭建私有的PyPI仓库源
--------------------

通常我们使用pip安装python包，都会默认从https://pypi.python.org/pypi 上安装，非常方便。
但是有些时候，我们公司内部的项目是不方便放到外网的，然而我们依然希望能够拥有使用pip安装的便利，
所以我们需要搭建自己的PyPi仓库。


### 如果搭建一个private的PyPI仓库

网上有很多如何搭建一个PyPI仓库的教程，本文使用了其中比较容易搭建的一种来创建自己的private的PyPI仓库。
本文的所有指令都是在ubuntu系统下操作的，而且假设是一个全新的ubuntu系统。

* 首先，我们需要一个虚拟环境，默认我们使用pip来进行安装

```
sudo apt-get install python-pip
pip install virtualenv
virtualenv py2
soutce py2/bin/activate
```
这样，我们就已经将相关的虚拟环境安装完毕，下面我们就开始安装pypi-server.

```
pip install pypiserver
```
安装完毕之后，就可以启动一个自己的PyPI服务了。



