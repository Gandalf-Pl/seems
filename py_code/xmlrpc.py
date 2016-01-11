# coding: utf8

import xmlrpclib

service_url = "http://192.168.1.10:8078"

db_name = "stable_160106"

username = "admin"
password = "a"

common = xmlrpclib.ServerProxy("{}/xmlrpc/common".format(service_url))

print common.version()

uid = common.authenticate(db_name, username, password, {})

print uid

models = xmlrpclib.ServerProxy("{}/xmlrpc/object".format(service_url))


print models.execute_kw(db_name, uid, password, "res.partner", "check_access_rights", ["read"], {"raise_exception": False})


results = models.execute_kw(db_name, uid, password, "res.partner", "search", [[["is_company", "=", True], ["customer", "=", True]]])

print results
