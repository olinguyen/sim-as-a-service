import tornado.web
import tornado.ioloop

import os
import sys

sys.path.insert(0, os.path.join(os.getcwd(), "handlers"))

from jobhandler       import JobHandler
from systemhandler    import SystemHandler
from sysdatahandler   import SysdataHandler
from queuehandler     import QueueHandler

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True
)

application = tornado.web.Application([
    (r"/", JobHandler),
    (r"/system", SystemHandler),
    (r"/sysdata", SysdataHandler),
    (r"/queue", QueueHandler),
# static cfg files handlers
    (r"/(.*)", tornado.web.StaticFileHandler, {'path': '/root/sim-as-a-service/configs/'}),
], **settings)

if __name__ == "__main__":
    print("[Simulator] Server running...")
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()
