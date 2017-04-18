#coding:utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.httpclient

import os 
import json 

from tornado.options import define,options

define("port",default=8000, help="run on the given port", type=int)


class BaseHandler(tornado.web.RequestHandler):
	def get_current_user(self):
		return self.get_secure_cookie('username')


class LoginHandler(BaseHandler):
	def get(self):
		self.render('login.html')

	def post(self):
		self.set_secure_cookie("username", self.get_argument("username"))
		self.redirect("/")


class WelcomeHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		self.render('weclome.html',username=self.current_user)



class LogoutHandler(BaseHandler):
	def get(self):
		self.clear_cookie("username")
		self.redirect("/")

if __name__ == '__main__':
	SETTINGS= {
		"template_path":os.path.join(os.path.dirname(__file__),"templates"),
		"static_path":os.path.join(os.path.dirname(__file__),"static"),
		"cookie_secret":"ydaukhbdjkasjdlkasheuwqaigdajkbdnlkandlkasndaslkdn23789y234",
		"login_url":"/login"
		}
	urls = [(r"/",WelcomeHandler),
			(r"/login",LoginHandler),
			(r"/test", WelcomeHandler),
			(r"/logout",LogoutHandler)
	]

	tornado.options.parse_command_line()
	app = tornado.web.Application(handlers=urls,**SETTINGS)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()	
