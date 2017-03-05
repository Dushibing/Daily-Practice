#coding:utf-8
import collections
fifo = collections.deque()
fifo.append(1)
fifo.append(2)
fifo.append(3)
print("fifo {0}".format(fifo))
print("fifo.pop() {0}".format(fifo.pop()))
print("fifo {0}".format(fifo))
print("fifo.popleft() {0}".format(fifo.popleft()))
print("fifo {0}".format(fifo))
a = collections.OrderedDict


'''
In [4]: a = collections.OrderedDict()

In [5]: a['foo'] = 1

In [6]: a['bar'] = 2

In [7]: b = collections.OrderedDict()

In [8]: b['foo'] = 'red'

In [9]: b['bar'] = 'blue'

or values1, values2 in zip(a.values(), b.values()):
    ...:     print (values1, values2)
    ...:     
(1, 'red')
(2, 'blue')
'''
