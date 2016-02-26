# -*- coding: utf-8 -*-

import barcode
from barcode.writer import ImageWriter


EAN = barcode.get_barcode_class("ean13")

ean = EAN("1234567891234", writer=ImageWriter())

fullname = ean.save("ean13_barcode")
