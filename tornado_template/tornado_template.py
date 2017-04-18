# coding:utf-8
import tornado.ioloop
import tornado.httpserver
import tornado.options
import tornado.web
import os 

from tornado.options import define, options

define("port",default=8000,help="run on the given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		jsondata = {"A1":'hello world'}
		self.render("index.html", backenddata = jsondata)

	def head(self):
		self.set_status(200)


if __name__ == '__main__':
	SETTINGS=dict(
		template_path = os.path.join(os.path.dirname(__file__),"templates"),
		static_path = os.path.join(os.path.dirname(__file__),"static")
		)
	urls = [(r"/",IndexHandler),
	]
	tornado.options.parse_command_line()
	app = tornado.web.Application(handlers=urls,**SETTINGS)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()