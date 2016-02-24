from tornado import gen, ioloop, web
from datetime import timedelta
from utils import config_pb2
import os

@gen.coroutine
def start_job():
    pass

class JobHandler(web.RequestHandler):
    def post(self):
        # Config coming from controller
        self.write({"status": "Received job request from controller"})
        #data = self.get_argument("config", "No data received")
        data = self.request.body
        self.write(data)

        # start job process
        self.finish()

    def read_config(self, path):
        config = config_pb2.Config()
        with open(path, "rb") as f:
            config.ParseFromString(f.read())

    def write_protobuf_result(self, path):
        with open(path, "wb") as f:
            f.write(result.SerializeToString())
