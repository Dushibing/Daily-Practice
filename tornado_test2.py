#coding:utf-8
import tornado.ioloop
import tornado.httpserver
import tornado.options
import tornado.web

from tornado.options import define, options

define("port",default=80000,help="run on the given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		greeting = self.get_argument('greeting','hello')
		edu = self.get_argument('edu','funck')
		self.write(greeting + edu + 'friendly user!')

	def head(self):
		self.set_status(200)


if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application(handlers=[(r"/",IndexHandler)])
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()