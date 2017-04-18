#coding:utf-8

def my_coroutine():
	while True:
		received = yield
		print('received', received)

it = my_coroutine()
next(it)
it.send('First')
it.send('Second')
