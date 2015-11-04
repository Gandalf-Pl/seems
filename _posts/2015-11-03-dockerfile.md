---
layout: post
title: 编写Dockerfile
---

### {{ page.title }}

+ Dockerfile的格式

    - Dockerfile中的所有指令都是顺序执行的,第一条指令必须是FROM来指定你从哪个image来build

    - Dockerfile中注释已#号开头,在一行中的#会被当做一个参数

        ~~~python
        # Comment
        RUN echo 'we are running some # of cool things'
        ~~~

+ Dockerfile中设置环境变量

    - ENV 关键字来设置环境变量,在dockerfile中可以${variable_name}或者$variable_name来
      引用变量.同时${variable_name}支持部分*bash*的语法

        - ${variable:-word}表示如果variable已经设置,则结果就是设置的值,否则结果就是word
        - ${variable:+word}表示如果variable已经设置,则结果就是word,否则就是空的字符串

        通过转义字符\可以将${variable_name}或者$variable_name转义为普通的字符串  

        在dockerfile中接受环境变量的指令有:  
          + ENV
          + ADD
          + COPY
          + WORKDIR
          + EXPOSE
          + VOLUME
          + USER
