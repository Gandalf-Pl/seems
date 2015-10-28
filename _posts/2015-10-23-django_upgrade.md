---
layout: post
title: django升级到1.8.5
---

###{{ page.title }}

相关改动详情可查看:

[django](https://docs.djangoproject.com/en/1.8/releases/)
[django_upgrade](https://openedx.atlassian.net/wiki/display/tnl/django+1.8+test+plan)

+ manage.py   需要修改 1.4.22 ==> 1.8.5 

+ settings.installed_apps需要修改 [django.contrib.markup]

+ django工具包修改 from django.utils import simplejson  ==> import simplejson 直接修改为内置

+ 需要升级的第三方包

    + [django-nose 1.2 ==>1.4.2]

    + [django-extensions 1.4.6 ==> 1.5.7]

    + [coffin 0.3.8 ==> 2.0.1]

    + add [django-jinja==1.4.1] in installed_apps

    + [django-tinymce 1.5.3 ==> 2.0.5]

    + [django-appconf 0.6 ==> 1.0.1]

    + [wfgfw 0.0.6]

+ django内置模块

    + transaction.commit_manuay, 可以重新写一个decorator

        ~~~python
        def commit_manually(func):
            """
            构造一个手动提交的事务的函数
            :param func:
            :return:
            """

            @functools.wraps(func)
            def _inner(*args, **kwargs):
                set_autocommit(False)
                res = func(*args, **kwargs)
                set_autocommit(True)
                return res

            return _inner
        ~~~

    + transaction.commit_on_success ==> transaction.atomic

    + south ==> 已经内置在django中,可以删除installed_apps中的south信息

    + form ==> 1.8中form不允许fileds 或者exclude都是空

        ~~~python
        class userlocalform(forms.modelform):
            class meta:
                model = user
                # 此处必须要要加上对应的fileds 或者exclude
                fields = “__all__”
        ~~~

    + django的template重新设计了,需要更新django的template.

        详细文档参见[django template](https://docs.djangoproject.com/en/1.8/ref/templates/upgrading/)

    + django1.8在启动的时候添加了对form, model的检测

        - manytomany: null has no effect on manytomany fields(remove null=true if null is set true in manytomany field) 

        - foreignkey: unique=true has same effect as using onetoonefield(remove unique=true if unique is set true in foreignkey field)

    + django1.8中已经修改的模块

        - Error1(importerror: no module named defaults):

            ~~~python
            from django.conf.urls.defaults import patterns, url, include
            ~~~
            ==>

            ~~~python
            from django.conf.urls import patterns, url, include
            ~~~

        - Error2(no module named simple):

            ~~~python
            from django.views.generic.simple import redirect_to, direct_to_template
            ~~~
            ==>

            ~~~python
            pass
            ~~~
            
        - Error3(cannot import name email_re)
            
            django的validators中的email_re已经删除了,需要自己定义
            
            ~~~python
            from django.core.validators import email_re
            ~~~
            ==>

            ~~~python
            email_re = re.compile(
                r”(^[-!#$%&‘*+/=?^_`{}|~0-9a-z`]+(\.[-!#$%&‘*+/=?^_`{}|~0-9a-z`]+)*”  # dot-atom
                # quoted-string, see also http://tools.ietf.org/html/rfc2822#section-3.2.5
                r’|^”([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*”’
                r’)@((?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,6}\.?\z)’  # domain
                r’|\[(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\]\z’, re.ignorecase) 
            ~~~

        - Error4(cannot import simplejson)

            ~~~python
            from django.utils import simplejson
            ~~~
            ==>

            ~~~python
            import simplejson
            ~~~

        - Error5(got an unexpected keyword argument ‘mimetype’)
            
            mimetype=”application/json” ==> content_type=”application/json”

        - Error6(Invalid block tag: ‘set’, expected ‘endblock’)

            django8中内置了对jinja2模板的引擎,可以使用django_jinja模块来直接使用jinja2引擎
            
        - Error7(‘User’ object has no attribute ‘customer_set’)

            在django1.8中,request.user.customer_set的写法已经不行

        - Error8(field is Foreignkey and is unique)
            
            Foreignkey(unique=True) ==> OneToOneField 
            同时需要修改对应的module的对象的调用方式

        - Error9(NoReverseMatch: Reverse for ‘’ with arguments ‘()’ and keyword arguments ‘{}’ not found. 0 pattern(s) tried: [])

            在django1.4中,模板中可以使用{% url reverse_name %}, 但是在django1.8中需要将reverse_name 用引号扩起来.

+ Django1.8 south模块内置到django中,需要修改之前的migrate文件,使之能后在新的版本继续使用    

    流程如下[upgrading from south](https://docs.djangoproject.com/en/1.8/topics/migrations/#upgrading-from-south):
        +_首先需要确保当前的模块的migrate都是正确的，文件和model都是相同的

        + 将”south”模块从INSTALLED_APPS中删除

        + 删除掉你的所有的migration文件，但是不要删除文件夹和__init__.py文件,同时需要保证删除你的.pyc文件

        + 然后执行python manage.py makemigrations. Django会找到migration文件目录，然后创建新的初始化migrations

        + 执行python manage.py migrate --fake-inital.

            todo
