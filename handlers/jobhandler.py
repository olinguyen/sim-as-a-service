from tornado import gen, ioloop, web
from datetime import timedelta
import sys
sys.path.append('/root/sim-as-a-service/utils/')
import subprocess
from sim_constants import *
import os
import json
import time

from config import setupConfigFile

class JobHandler(web.RequestHandler):
    def post(self):
        # print(self.request.body)
        # QueueConfig(configDic) This gets the config file ready and queued under /configs
        # Get config file
        try:
            data = json.loads(self.request.body)
            app_name = data['app']
            email = data['email']
            num_cores = data['total_cores']
            self.log_history(app_name, num_cores, email)
        except ValueError:
            pass

        # Move to config folder if current sim running
        if os.path.isfile(RUNNING_SIM_FLAG):
            num_jobs_queued = len(os.listdir(CONFIG_PATH))
            print "Simulation currently running, adding job to queue..."
            print CONFIG_PATH + "carbon_sim%d.cfg" % num_jobs_queued
            setupConfigFile(data, CONFIG_PATH + "carbon_sim%d.cfg" % num_jobs_queued)
        else:
            #start job process
            setupConfigFile(data, GRAPHITE_HOME + "carbon_sim.cfg")
            proc = subprocess.Popen("python %s %s %s" % \
                            (SPAWN_APP, app_name, email), shell=True)

        # Alert controller that job was started
        self.write({
          "status": 200,
          "message": "job has been succesfully started"
        })
        self.finish()

    def log_history(self, app_name, num_cores, email):
        with open(HISTORY_LOG, "a") as f:
            f.write("%s %s %s %d\n" % (app_name, num_cores, email, int(time.time())))

