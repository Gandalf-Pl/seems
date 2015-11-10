# -*- coding: utf-8 -*-

from celery import Celery
from proj import celeryconfig
# first argument to Celery is the name of the current module, this is needed so
# that names can be automatically generated.
# if you want to keep track of the task's stats, Celery needs to store or send
# status somewhere, you must set backend argument
# input ==> broker output ==> backend
app = Celery("tasks")

app.config_from_object(celeryconfig)


if __name__ == '__main__':
    app.start()
