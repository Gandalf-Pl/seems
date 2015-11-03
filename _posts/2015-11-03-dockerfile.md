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
        RUN echo ‘we are running some # of cool things’
        ~~~

+ 
