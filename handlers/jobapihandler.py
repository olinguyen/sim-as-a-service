import tornado.web

import os, os.path
import time, datetime

import sys
sys.path.append('/root/sim-as-a-service/utils/')
from sim_constants import *

class JobApiHandler(tornado.web.RequestHandler):
    def get(self):
        history = { 'status': 200, 'jobs_his': []}

        f = open('/root/sim-as-a-service/utils/history.log', 'r')

        history_txt = f.read()
        

        for his in history_txt.split('\n'):
        	h = his.split(' ')
        	print(type(h))
        	if len(h) == 4:
        		history['jobs_his'].append({ 'app': h[0], 'num_cores': h[1], 'email': h[2], 'time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(h[3]))) })

        f.close()

        self.write(history)
        self.finish()