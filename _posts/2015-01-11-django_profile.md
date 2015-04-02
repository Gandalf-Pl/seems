---
layout: post
title: Django性能调优
---

## {{ page.title }}

#### Django QuerySet
    * QuerySet的特性
        1. QuerySet是惰性的
        2. QuerySet在什么时候赋值
        3. QuerySet的值是如何保存在内存中的
    
#### Django数据库查询优化
    * 连接数
    * 数据库查询次数
    * 数据库返回值的定义
    
#### Django缓存技术
    * Django的缓存相关信息
    
#### Django性能调试工具
    * django_extensions
    * debug_toolbar
   
Django数据库查询需要注意的点：

1. Django cached attributes
    
2. Don’t overuser count() and exists()

3. Use with tag in templates

4. Use QuerSet.update() and delete()

5. Use foreign key values directly
    such as entry.blog_id insted of entry.blog.id

6. Don’t order results if you don’t care
    if a model has a default ordering(Meta.ordering) and you don’t need it,
    remove it on a  QuerySet by calling order_by() with no parameters.

7. Insert in bulk
    when creating objects,where possible,use bulk_create() method to reduce
    the number of SQL queries.

    This also applies to ManyToManyFields,so doing:
    *my_band.members.add(me, my_friend)*
    is perferable to:
    *my_band.members.add(me)*
    *my_band.members.add(my_friend)*

Django的MiddleWare



    1. process_request(request):
        “””
        @parameters request HttpRequest object    
        @return None OR HttpResponse    
        ”””
        
        process_request is called on each request, before Django decides which
        view to execute.
        It return either None or an HttpResponse object.
    
    2. process_view(request, view_func, view_args, view_kwargs):
        “””
        @parameters request HttpRequest object
        @parameters view_func  the Python function that Django is about to use.
        @return None Or HttpResponse 
        ”””
        this method is called just before Django calls the view.
        
    3. process_template_response(request, response):
        “””
        @parameters request HttpRequest object
        @parameters response TemplateResponse object
        @return a response object that implements a render method or a New TemplateResponse
        ”””
        this method is called just after the view has finished executing.
    
    4. process_response(request, response):
        “””
        @parameters request HttpRequest object
        @parameters response HttpResponse or StreamingHttpResponse object.
        @return  HttpResponse or StreaminghttpResponse object
        ”””
        this method is called on all responses before they’re returned to browser.
        this method is always called,even if the process_request and process_view 
        were skipped.
        During the response phase,middleware are applied in reverse order,from the
        bottom up.This means classes defined at the end of MIDDLEWARE_CLASSES will
        be run first.
    
    5. process_exception(request, exception):
        “””
        @parameters request HttpRequest object
        @parameters exception Exception
        @return None or HttpResponse
        ”””
