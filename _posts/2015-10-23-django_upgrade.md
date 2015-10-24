---
layout: post
title: Django升级到1.8.5
---

## {{ page.title }}

<href=https://docs.djangoproject.com/en/1.8/releases/>

<href=https://openedx.atlassian.net/wiki/display/TNL/Django+1.8+Test+Plan>

+ manage.py   需要修改 1.4.22 ==> 1.8.5 

+ settings.INSTALLED_APPS需要修改 [django.contrib.markup]

+ django工具包修改 from django.utils import simplejson  ==> import simplejson 直接修改为内置

+ 需要升级的第三方包

    + [django-nose 1.2 ==>1.4.2]

    + [django-extensions 1.4.6 ==> 1.5.7]

+ django内置模块

    + transaction.commit_manuay

    + 
