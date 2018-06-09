import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver
from tornado.options import define, options
from handlers import main,auth


define('port', default=8888, help='run port', type=int )


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', main.IndexHandler),
            (r'/explore', main.ExploreHandler),
            (r'/post/(?P<post_id>[0-9]+)', main.PostHandler),
            (r'/upload', main.UploadHandler),
            (r'/login', auth.LoginHandler),
            (r'/logout', auth.LogoutHandler),
            (r'/signup',auth.SignupHandler)
        ]
        settings = dict(
            debug = True,
            template_path='templates',
            static_path='static',
            cookie_secret='qwertyuiop',
            login_url='/login',
            pycket={
                'engine': 'redis',
                'storage': {
                    'host': 'localhost',
                    'port': 6379,
                    'db_sessions': 5,
                    'db_notifications': 11,
                    'max_connections': 2 ** 33,
                },
                'cookies': {
                    'expires_days': 30,
                },
            },
        )

        super(Application,self).__init__(handlers, **settings)

application = Application()


if __name__ == '__main__':
    tornado.options.parse_command_line()
    application.listen(options.port)
    print("Server start on port {}".format(str(options.port)))
    tornado.ioloop.IOLoop.current().start()