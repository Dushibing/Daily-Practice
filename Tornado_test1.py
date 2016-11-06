import os 
import tornado.web
import tornado.ioloop



class MainHandler(tornado.web.RequestHandler):

	def get(self):
		self.write("hello get\n ")

	def post(self):
		self.write("hello post\n")


	def put(self):
		self.write("hello put\n")


	def delete(self):
		self.write("hello delete\n")



if __name__ == '__main__':

	settings = {
	'debug': True,
	'static_path': os.path.join(os.path.dirname(__file__), 'static'),
	'template_path': os.path.join(os.path.dirname(__file__), 'template'),
	}


	application = tornado.web.Application([
		(r'^/$',MainHandler),
		], **settings)
	application.listen(8000)
	tornado.ioloop.IOLoop.instance().start()
