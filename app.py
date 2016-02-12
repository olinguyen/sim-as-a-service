import tornado.web
import tornado.ioloop

import os
import sys

sys.path.insert(0, os.path.join(os.getcwd(), "handlers"))

from jobhandler import JobHandler

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True
)

application = tornado.web.Application([
    (r"/", JobHandler),
    ])

if __name__ == "__main__":
    print("[Simulator] Server running...")
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()
