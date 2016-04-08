import tornado.web

import os, os.path
import time, datetime

import sys
sys.path.append('/root/sim-as-a-service/utils/')
from sim_constants import *
import glob

class ResultsApiHandler(tornado.web.RequestHandler):
    def get(self):
    	result_data = { 'status': 200, 'results': []}

        files = glob.glob("/root/sim-as-a-service/sim_output_history/*.out")
        for file in files:
        	f = open(file, 'r')
        	simout = f.read()
        	f.close()
        	data = (file.split('/')[4]).split('-')
        	result_data['results'].append({ 'simout': simout, 'app': data[1], 'email': data[2], 'result_time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(data[3]))) })

        #f = open('/root/sim-as-a-service/utils/history.log', 'r')

        #history_txt = f.read()
        

        #for his in history_txt.split('\n'):
        #	h = his.split(' ')
        # 	print(type(h))
        #	if len(h) == 4:
        # 		history['jobs_his'].append({ 'app': h[0], 'num_cores': h[1], 'email': h[2], 'time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(h[3]))) })

        #f.close()

        print(result_data)
        self.write(result_data)
        self.finish()
