#!/usr/bin/env python
# _*_encoding:utf-8_*_
"""
@version: ??
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: 
@software: PyCharm
@file: setDeamon.py
@time: 15/10/16 4:11 PM
"""
__author__ = 'dushibing'

import threading
import time
def run(num):
    if not num ==5:
        time.sleep(1)
    print 'Hi, I am thread {} \n'.format(num)


def main(n):
    print '____runing main thread -----'
    for i in range(n):
        t = threading.Thread(target=run,args=(i,))
        t.start()
    time.sleep(3)
    print "----done main thread ------"

main_thread = threading.Thread(target=main,args=(10,))
main_thread.setDaemon(True)
main_thread.start()
time.sleep(2)
print '\n--------->>>>>>'