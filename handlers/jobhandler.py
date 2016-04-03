from tornado import gen, ioloop, web
from datetime import timedelta
from utils import config_pb2
import sys
sys.path.append('/root/sim-as-a-service/utils/')
from sim_constants import *
import os

@gen.coroutine
def start_job():
    pass

class JobHandler(web.RequestHandler):
    def post(self):
        # Config coming from controller
        self.write({"status": "Received job request from controller"})
        data = self.request.body
        self.write(data)

        # Generate config file
        num_jobs_queued = len(os.listdir(CONFIG_PATH))
        os.system("touch %scarbon_sim%d.cfg" % (CONFIG_PATH, num_jobs_queued))

        """
        # Move to config folder if current sim running
        if os.path.isfile(RUNNING_SIM_FLAG):

        else:


        # start job process
        proc = subprocess.Popen(command, shell=True)
        """

        self.finish()

    def read_config(self, path):
        config = config_pb2.Config()
        with open(path, "rb") as f:
            config.ParseFromString(f.read())

    def write_protobuf_result(self, path):
        with open(path, "wb") as f:
            f.write(result.SerializeToString())
