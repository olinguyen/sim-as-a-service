from tornado import gen, ioloop, web
from datetime import timedelta
import sys
sys.path.append('/root/sim-as-a-service/utils/')
import subprocess
from sim_constants import *
import os

class JobHandler(web.RequestHandler):
    def post(self):
        # Config coming from controller
        configDic = self.get_argument("", {})

        # Get config file
        data = self.request.body
        self.write(data)
        with open("/root/sim-as-a-service/test.txt", 'w') as f:
            f.write(data)

        # Move to config folder if current sim running
        if os.path.isfile(RUNNING_SIM_FLAG):
            print "Simulation currently running, adding job to queue..."
            num_jobs_queued = len(os.listdir(CONFIG_PATH))
            os.system("touch %scarbon_sim%d.cfg" % (CONFIG_PATH, num_jobs_queued))
        else:
            # start job process
            proc = subprocess.Popen("python %s" % SPAWN_APP, shell=True)

        # Alert controller that job was started
        self.write({
          "status": 200,
          "message": "job has been succesfully started"
        })
        self.finish()
