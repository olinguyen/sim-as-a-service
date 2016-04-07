import tornado.web

import os, os.path
import time, datetime

import sys
sys.path.append('/root/sim-as-a-service/utils/')
from sim_constants import *

class QueueHandler(tornado.web.RequestHandler):
    def get(self):
        jobs_files_queued = os.listdir(CONFIG_PATH)

        files_q = []
        for idx, job in enumerate(jobs_files_queued):
        	files_q.append({'name': job, 'time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getctime('/root/sim-as-a-service/configs/' + job)))})

        files_q = list(sorted(files_q, key=lambda k: k['time']))

        print(files_q)
        self.render('queue.html', configs=files_q)
