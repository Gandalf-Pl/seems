# coding: utf8

import random
import string


random_string = "".join(random.sample(string.ascii_letters + string.digits, 8))

print random_string
