import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver
from tornado.options import define, options
from handlers import main

define('port', default=8888, help='run port', type=int )


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            ('/index', main.IndexHandler),
        ]
        settings = dict(
            debug = True,
            template_path='templates'
        )

        super(Application,self).__init__(handlers, **settings)

application = Application()

if __name__ == '__main__':
    tornado.options.parse_command_line()
    application.listen(options.port)
    print("Server start on port {}".format(str(options.port)))
    tornado.ioloop.IOLoop.current().start()