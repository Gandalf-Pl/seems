---
layout: post
title: Jekyll中设置python语法高亮
---

### {{ page.title }}

+ 首先需要安装pygments

    pip install pygments

+ 其次配置Jekyll的配置文件,添加下面这行

    highlighter: pygments

+ 配置完成之后生成对应的css文件

    pygments -S [default|monokal|manni|colorful|...] -f html > your_path/pygments.css

    pygments的样式可以在python命令中查看

    ~~~python
    from pygments.styles import STYLE_MAP
    STYLE_MAP.keys()
    ~~~

+ 在Jekyll中\_includes/header.html中添加对css的调用

    ~~~python
    <link href="{{ site.baseurl }}/css/pygments.css" rel="stylesheet">
    ~~~

+ 在post中使用

    使用的方法就是如下所示,以~~~python开头,已~~~结尾

    ~~~
        ~~~python 
        # code
        ~~~
    ~~~
