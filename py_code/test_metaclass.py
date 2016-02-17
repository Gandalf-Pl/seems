# -*- coding: utf-8 -*-

from django.db.models import Model


class MySubClass(Model):

    name = "test"

my_class = MySubClass()

print my_class
