---
layout: post
title: Ubuntu和vim中设置sdcv
---

### {{ page.title }}

+ 需要安装sdcv

    ~~~
    sudo apt-get install sdcv
    ~~~
+ 安装对应的词典信息 

    ~~~
    sudo mkdir -p /usr/share/stardict/dic/
    ~~~

    然后将下载的stardict-langdao-ec-gb-2.4.2.tar.bz2解压到上面的目录

    ~~~
    sudo tar -xvjf stardict-langdao-ec-gb-2.4.2.tar.bz2 -C /usr/share/stardict/dic/
    ~~~

    然后就可以在commandline下面直接查询单词的意思

    ~~~
    sdcv word
    ~~~

+ 在vim中调用sdcv信息

   在vimrc(位于 ~/.vimrc 或者 /etc/vim/vimrc)中加入 

   ~~~
   nmap <C-k> : !sdcv <C-R>=expand(“<cword>”)<CR><CR></CR></CR></cword>) 
   ~~~
   然后在vim的普通模式下面Ctrol-k就可以查看当前单词的字典信息
