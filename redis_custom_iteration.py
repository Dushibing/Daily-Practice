#!/usr/bin/env python
# _*_encoding:utf-8_*_
"""
@version: ??
@license: Apache Licence 
@site: 
@software: PyCharm
@file: redis_custom_iteration.py
@time: 19/11/16 9:50 PM
"""
__author__ = 'dushibing'

import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)
#largelist = range(100)
#r.lpush('ppp', largelist)

# 由于redis类库中没有提供对列表元素的增量迭代，如果想要循环name对应的列表的所有元素，那么就需要：
    # 1、获取name对应的所有列表
    # 2、循环列表
# 但是，如果列表非常大，那么就有可能在第一步时就将程序的内容撑爆，所有有必要自定义一个增量迭代的功能：

def list_iter(name):
    """
    自定义redis列表增量迭代
    :param name: redis中的name，即：迭代name对应的列表
    :return: yield 返回 列表元素
    """
    list_count = r.llen(name)
    for index in xrange(list_count):
        yield r.lindex(name, index)

# 使用
for item in list_iter('ppp'):
    print item