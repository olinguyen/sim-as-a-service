from tornado import gen, ioloop, web
from datetime import timedelta
import os

@gen.coroutine
def start_job():
    pass

class JobHandler(web.RequestHandler):
    def post(self):
        # Config coming from controller
        self.write({"status": "Received job request from controller"})
        data = self.get_argument("config", "No data received")
        print data
        # start job process
        self.finish()
