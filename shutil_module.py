#!/usr/bin/env python
# _*_encoding:utf-8_*_
"""
@version: ??
@license: Apache Licence 
@site: 
@software: PyCharm
@file: shutil_module.py
@time: 24/11/16 8:04 AM
"""
__author__ = 'dushibing'

import shutil

#shutil.copyfileobj(open('xo.xml','r'), open('new.xml', 'w'))

import zipfile

# 压缩

# z = zipfile.ZipFile('laxi.zip', 'w')
# z.write('new.xml')
# z.write('oooo.xml')
# z.close()
z = zipfile.ZipFile('laxi.zip', 'r')
for item in z.namelist():
    print item
z.close()