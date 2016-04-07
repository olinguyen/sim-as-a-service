import tornado.web

class SystemHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', section='system')
