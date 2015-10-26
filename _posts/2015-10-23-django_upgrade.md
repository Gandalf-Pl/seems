---
layout: post
title: django升级到1.8.5
---

###{{ page.title }}

<href=https://docs.djangoproject.com/en/1.8/releases/>

<href=https://openedx.atlassian.net/wiki/display/tnl/django+1.8+test+plan>

+ manage.py   需要修改 1.4.22 ==> 1.8.5 

+ settings.installed_apps需要修改 [django.contrib.markup]

+ django工具包修改 from django.utils import simplejson  ==> import simplejson 直接修改为内置

+ 需要升级的第三方包

    + [django-nose 1.2 ==>1.4.2]

    + [django-extensions 1.4.6 ==> 1.5.7]

    + [coffin 0.3.8 ==> 2.0.1]

    + add [django-jinja==1.4.1] in installed_apps

+ django内置模块

    + transaction.commit_manuay, 可以重新写一个decorator

        ~~~python
        def commit_manually(fn):
            def _commit_manually(*args, **kwargs):
                set_autocommit(false)
                res = fn(*args, **kwargs)
                commit()
                set_autocommit(true)
                return res
            return _commit_manually
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

        - error1(importerror: no module named defaults):

            ~~~python
            from django.conf.urls.defaults import patterns, url, include
            ~~~
            ==>

            ~~~python
            from django.conf.urls import patterns, url, include
            ~~~

        - error2(no module named simple):

            ~~~python
            from django.views.generic.simple import redirect_to, direct_to_template
            ~~~
            ==>

            ~~~python
            pass
            ~~~
            
        - error3(cannot import name email_re)
            
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

        - error4(cannot import simplejson)

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

            maybe is django_jinjia error
