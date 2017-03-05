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
