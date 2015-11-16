---
layout: post
title: django升级到1.8.6
---

###{{ page.title }}

相关改动详情可查看:

[django](https://docs.djangoproject.com/en/1.8/releases/)
[django_upgrade](https://openedx.atlassian.net/wiki/display/tnl/django+1.8+test+plan)

+ manage.py   需要修改 1.4.22 ==> 1.8.6 

+ INSTALLED_APPS需要更新的第三方包

    - Upgrade
        1. [django-nose 1.2 ==>1.4.2]
        2. [django-extensions 1.4.6 ==> 1.5.7]
        3. [coffin 0.3.8 ==> 2.0.1]
        4. [django-tinymce 1.5.3 ==> 2.0.5]
        5. [django-appconf 0.6 ==> 1.0.1]
        6. [wfgfw 0.0.6]
        7. [django-compressor 1.4 ==> 1.5]

    - Add
        1. [django-jinja==1.4.1]

    - Delete
        1. [django.contrib.markup]

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
                commit()
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
                fields = "__all__"
        ~~~

    + django的template重新设计了,需要更新django的template,在django1.8中默认支持两种模板引擎,DjangoTemplates, Jinja2 Template.

        详细文档参见[django template](https://docs.djangoproject.com/en/1.8/ref/templates/upgrading/)
        在settings中配置相应的模板信息 
        
        ~~~python
        TEMPLATES = [
            {
                "BACKEND": "django_jinja.backend.Jinja2",
                "APP_DIRS": True,
                "OPTIONS": {
                    # 以jinja2结尾的相应的模板引用Jinja2引擎
                    "match_extension": ".jinja2",
                    "extensions": DEFAULT_EXTENSIONS + [
                        "jinja2.ext.do",
                        "jinja2.ext.loopcontrols",
                        "jinja2.ext.with_",
                        "jinja2.ext.autoescape",
                        "django_jinja.builtins.extensions.CsrfExtension",
                        "django_jinja.builtins.extensions.CacheExtension",
                        "django_jinja.builtins.extensions.TimezoneExtension",
                        "django_jinja.builtins.extensions.UrlsExtension",
                        "django_jinja.builtins.extensions.StaticFilesExtension",
                        "django_jinja.builtins.extensions.DjangoFiltersExtension",
                        "compressor.contrib.jinja2ext.CompressorExtension",
                    ],
                    "context_processors": [
                        "django.contrib.auth.context_processors.auth",
                        "django.template.context_processors.debug",
                        "django.template.context_processors.i18n",
                        "django.template.context_processors.media",
                        "django.template.context_processors.static",
                        "django.template.context_processors.tz",
                        "django.contrib.messages.context_processors.messages",
                    ],
                    "autoescape": True,
                }
            },
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [
                    os.path.join(_DIRNAME, "templates"),
                    os.path.join(_DIRNAME, "..")
                ],
                # When APP_DIRS is True, DjangoTemplates engines look for templates
                # in the templates subdirectory of installed applications.
                # 'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.contrib.auth.context_processors.auth',
                        'django.template.context_processors.debug',
                        'django.template.context_processors.i18n',
                        'django.template.context_processors.media',
                        'django.template.context_processors.static',
                        'django.template.context_processors.tz',
                        'django.contrib.messages.context_processors.messages',
                    ],
                    'loaders': [
                                    ('django.template.loaders.cached.Loader', [
                                        'django.template.loaders.filesystem.Loader',
                                        'django.template.loaders.app_directories.Loader',
                                    ]),
                    ],
                },
            },
        ]
        ~~~

    + django1.8在启动的时候添加了对form, model的检测

        - manytomany: null has no effect on manytomany fields(remove null=true if null is set true in manytomany field) 

        - foreignkey: unique=true has same effect as using onetoonefield(remove unique=true if unique is set true in foreignkey field)

    + django1.8中已经修改的模块
        1. Error1(importerror: no module named defaults):

            ~~~python
            from django.conf.urls.defaults import patterns, url, include
            # 修改为
            from django.conf.urls import patterns, url, include
            ~~~
        2. Error2(no module named simple):

            ~~~python
            # 在1.8中已经废弃
            from django.views.generic.simple import redirect_to, direct_to_template
            ('^about/$', direct_to_template, {'template': 'about.html'})
            # replace with generic classes
            from django.views.generic.base import TemplateView, RedirectView
            ('^about/$', TemplateView.as_view('template': 'about.html'})
            ~~~
        3. Error3(cannot import name email_re)
            
            django的validators中的email_re已经删除了,需要自己定义
            
            ~~~python
            from django.core.validators import email_re
            # 在django1.8中可以自己实线email_re
            email_re = re.compile(
                r"(^[-!#$%&‘*+/=?^_`{}|~0-9a-z`]+(\.[-!#$%&‘*+/=?^_`{}|~0-9a-z`]+)*"  # dot-atom
                # quoted-string, see also http://tools.ietf.org/html/rfc2822#section-3.2.5
                r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"'
                r')@((?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,6}\.?\z)'  # domain
                r'|\[(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\]\z', re.ignorecase) 
            ~~~
        4. Error4(cannot import simplejson)

            ~~~python
            from django.utils import simplejson
            # 在django1.8中直接使用标准库中的simplejson或者json来代替django.utils中的simplejson
            import simplejson
            ~~~
        5. Error5(got an unexpected keyword argument 'mimetype')
            
            mimetype="application/json" ==> content_type="application/json"
        6. Error6(Invalid block tag: 'set', expected 'endblock')

            django8中内置了对jinja2模板的引擎,可以使用django_jinja模块来直接使用jinja2引擎
        7. Error7('User' object has no attribute 'customer_set')

            在django1.8中,request.user.customer_set的写法已经不行
        8. Error8(field is Foreignkey and is unique)
            
            Foreignkey(unique=True) ==> OneToOneField 
            同时需要修改对应的module的对象的调用方式
        9. Error9(NoReverseMatch: Reverse for '' with arguments '()' and keyword arguments '{}' not found. 0 pattern(s) tried: [])

            在django1.4中,模板中可以使用url reverse_name, 此处的reverse_name可以不用引号扩起来,
            但是在django1.8中需要将reverse_name 用引号扩起来.
        10. Error10(select_related())

            在django1.8中,select_related中对应的值必须是该model中存在的,否则就会有异常抛出,而在之前的版本中，则是可以是不存在的属性的
        11. Error11(get_query_set ==> get_queryset)

            在django1.6中就已经修改get_query_set == > get_queryset了,在Manager中和Admin中对应的查询都需要修改为get_queryset

    + settings.ALLOWED__HOSTS
        
        需要在新的版本中添加的配置,在DEBUT=False的时候,django允许访问的hosts,是一个列表信息

+ Django1.8 south模块内置到django中,需要修改之前的migrate文件,使之能后在新的版本继续使用    

    流程可以参考官方文档: [upgrading from south](https://docs.djangoproject.com/en/1.8/topics/migrations/#upgrading-from-south):
    1. 首先需要确保当前的模块的migrate都是正确的，文件和model都是相同的
    2. 将”south”模块从INSTALLED_APPS中删除
    3. 删除掉你的所有的migration文件，但是不要删除文件夹和\_\_init\_\_.py文件,同时需要保证删除你的.pyc文件
    4. 然后执行python manage.py makemigrations. Django会找到migration文件目录，然后创建新的初始化migrations
    5. 执行python manage.py migrate --fake-inital. **需要注意的是,如果migrate有对其他外部的引用,
       则可能会产生多个migrate文件,此时直接执行该命令会报错,需要对有多个文件的app单独执行命令
       python manage.py migrate --fake yourapp**
       
    执行完上述命令后,在数据库中可以看到,django会新生成一张表django_migrate来取代老的south_migrationhistory表,其中的数据是重新开始的migrate的记录.

+ Django Warnings 

    升级到django1.8.6之后，在启动检查的过程中会有一些警告产生, 通过命令**python -W “error:django.utils.importlib:DeprecationWarning” manage.py runserver**
    可以看到traceback信息
    - Warning1(django.utils.importlib will be removed in Django 1.9)

        upgrade django-appconf from version 0.6.6 to 1.0.1 

        upgrade django-compressor-1.4 ==> django-compressor-1.5

        from django.utils.importlib import import_module ==> from importlib import import_module
    - Warning2(ngo.contrib.contenttypes.generic is deprecated and wi be removed in Django 1.9)

        Its contents have been moved to the fields, forms, and admin submodules of django.contrib.contenttypes.
    - Warning3(The django.db.backends.util module has been renamed)

        Use django.db.backends.utils instead.
    - Warning4(Redirectview.permanent will change from True to False in Django1.9) 

        ~~~python
        url(r'^$', RedirectView.as_view(url='your_url'))
        # modify to
        url(r'^$', RedirectView.as_view(url='your_url', permanent=True))
        ~~~

+ Django Session

    在django1.4中,session的默认序列化格式是"django.contrib.sessions.serializers.PickleSerializer",但是在django1.6之后，出于安全考虑修改为"JSONSerializer"

+ Django Form提交
    
    request.POST will no longer include data posted via HTTP requests with non form-specific content-types in the header. 
    In prior versions, data posted with content-types other than multipart/form-data or 
    application/x-www-form-urlencoded would still end up represented in the request.POST attribute. 
    Developers wishing to access the raw POST data for these cases, should use the request.body attribute instead.
