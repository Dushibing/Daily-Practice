#!/usr/bin/env python
# _*_encoding:utf-8_*_
"""
@version: ??
@license: Apache Licence 
@site: 
@software: PyCharm
@file: subprocess_module.py
@time: 24/11/16 8:33 AM
"""
__author__ = 'dushibing'
import subprocess

#执行命令，返回状态码
ret = subprocess.call(["ls", "-l"], shell=False)
ret = subprocess.call("ls -l", shell=True)

#执行命令，如果执行状态码是 0 ，则返回0，否则抛异常
# subprocess.check_call(["ls", "-l"])
# subprocess.check_call("exit 1", shell=True)

#执行命令，如果状态码是 0 ，则返回执行结果，否则抛异常
# subprocess.check_output(["echo", "Hello World!"])
# subprocess.check_output("exit 1", shell=True)


# obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
# obj.stdin.write("print(1)\n")
# obj.stdin.write("print(2)")
#
# out_error_list = obj.communicate()
# print(out_error_list)

# obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
# out_error_list = obj.communicate('print("hello")')
# print(out_error_list)