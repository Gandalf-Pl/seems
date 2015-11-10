# -*- coding: utf-8 -*-

# Broker url
BROKER_URL = "redis://localhost"
# Backend url to store task state and results
CELERY_RESULT_BACKEND = "redis://localhost/1"

# List of modules to import when celery starts
CELERY_IMPORTS = ("proj.tasks",)

# Celery annotations
CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}

# The number of concurrent worker processes/threads/green threads executing
# tasks.
# If you’re doing mostly I/O you can have more processes, but if mostly
# CPU-bound, try to keep it close to the number of CPUs on your machine.
# If not set, the number of CPUs/cores on the host will be used.
# Defaults to the number of available CPUs.
CELERYD_CONCURRENCY = 4

# How many messages to prefetch at a time multiplied by the number of
# concurrent processes. The default is 4 (four messages for each process).
# The default setting is usually a good choice, however – if you have very
# long running tasks waiting in the queue and you have to start the workers,
#  note that the first worker to start will receive four times the number of
# messages initially. Thus the tasks may not be fairly distributed to the
# workers.
# To disable prefetching, set CELERYD_PREFETCH_MULTIPLIER to 1.
# Setting CELERYD_PREFETCH_MULTIPLIER to 0 will allow the worker to
# keep consuming as many messages as it wants.
CELERYD_PREFETCH_MULTIPLIER = 1

#
CELERY_TASK_SERIALIZER = 'json'
# Content-type(MIME)
CELERY_ACCEPT_CONTENT = ['json']  # Ignore other content
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True

# CELERY_ROUTES
CELERY_ROUTES = {
    "proj.tasks.add": {"queue": "hipri"}
}
