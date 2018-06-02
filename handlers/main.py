import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    """
    Home page for use,photo feeds
    """
    def get(self):
        self.render('index.html')