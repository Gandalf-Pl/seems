---
layout: post
title: Django性能调优
---

### {{ page.title }}

+ Django QuerySet
    * QuerySet的特性
        1. QuerySet是惰性的
        2. QuerySet在什么时候赋值
        3. QuerySet的值是如何保存在内存中的
    
+ Django数据库查询优化
    * 连接数
    * 数据库查询次数
    * 数据库返回值的定义
    
+ Django缓存技术
    * Django的缓存相关信息
    
+ Django性能调试工具
    * django_extensions
    * debug_toolbar
   
+ Django数据库查询需要注意的点：
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
            **my_band.members.add(me, my_friend)**
        is perferable to:
            **my_band.members.add(me)  my_band.members.add(my_friend)**

+ Django的MiddleWare
    1. process_request(request):
    2. process_view(request, view_func, view_args, view_kwargs):
    3. process_template_response(request, response):
    4. process_response(request, response):
    5. process_exception(request, exception):

+ Django ORM Complex Query
    - Conert complex django ORM Query to raw_sql:
    
        ~~~
        # django orm
        Userpoint.objects.values(“user”).annotate(user_count=Count(‘user’)).filter(user_count__gt=1).query
        
        # 转换成的raw_sql        
        SELECT “userpoint_userpoint”.”user_id”, COUNT(“userpoint_userpoint”.”user_id”) 
        AS “user_count” FROM “userpoint_userpoint” GROUP BY 
        “userpoint_userpoint”.”user_id” HAVING COUNT(“userpoint_userpoint”.”user_id”) > 1
        ~~~
