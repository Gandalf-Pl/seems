---
layout: post
title: 设置django的Cache为Redis
---

### {{ page.title }}

+ 在Django目前的版本中支持了多种的cache backend

    - Memcached
    - Database caching
    - Filesystem caching
    - local-memory caching

    在这些cache之外,你可以自己定制自己的cache后端.

+ Redis Cache Backend

    现在很多公司在需要使用缓存技术时首先考虑的基本都是redis, 
    作为一个使用很广的cache DB, Django官方还没有提供对应的Redis支持,
    但是目前github上面已经有两个还不错的第三库可以直接用来集成到系统中.

   - [django-redis](https://github.com/niwinz/django-redis)
   - [django-redis-cache](https://github.com/sebleier/django-redis-cache)

+ 集成django-redis到Django中

    - 首先需要安装django-redis,根据django版本安装不同的版本,本例中django1.8.7

      ~~~ python
      pip install django-redis==4.3.0
      ~~~

    - 修改django中的cache设置,django-redis库目前支持单节点Redis和多节点的Redis Master-Slave,详情查看对应的文档[django-redis文档](http://niwinz.github.io/django-redis/latest/)

      ~~~ python
      CACHES = {
          "default": {
              "BACKEND": "django_redis.cache.RedisCache",
              "LOCATION": "redis://127.0.0.1:6379/1",
              "OPTIONS": {
                  "CLIENT_CLASS": "django_redis.client.DefaultClient",
              }
          }
      }
      ~~~

    - 如果Redis是通过Sentinel来做的HA,那么django-redis中目前还没有提供,但是github上已经有对应的[SentinelClient](https://github.com/KabbageInc/django-redis-sentinel/blob/master/django_redis_sentinel/sentinel.py)

      ~~~ python
      CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "master_name/sentinel_uri/db",
            "OPTIONS": {
                "CLIENT_CLASS": "path.SentinelClient",
             }
        }
      }
      ~~~

      只需要将上述的SentinelClinet添加到自己的代码库中稍微修改即可,配置上面只需要将之前的连接修改为对应的sentinel的连接即可

+ 迁移之前的cache中的信息到redis_cache中,一般来说就是session需要迁移,其他的信息可以在用户访问的过程中重新缓存到对应的cache中即可

  首先需要查看项目的settings文件，查看之前的session配置

  ~~~ python
  # SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
  SESSION_ENGINE = 'django.contrib.sessions.backends.cached'
  ~~~

  如果是**cached_db**则表示之前的session是在db和cache中都有存储，这种情况下不需要导入对应的session,用户登录获取session会从数据库中读取，然后重新缓存到cache中

  如果是**cache**则需要将对应的session重新导入到redis中，否则可能导致登录的用户需要重新登录的问题,已经部分在session中的数据将会丢失掉
