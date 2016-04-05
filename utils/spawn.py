#!/usr/bin/env python

"""
This is the python script that is responsible for spawning a simulation
"""

import sys
import os
import glob
import shutil
from sim_constants import *
from tornado import gen, httpclient, ioloop
import urllib

destination = 'http://104.200.30.65:5000'
http_client = httpclient.AsyncHTTPClient()

@gen.coroutine
def post():
    with open('/root/sim-as-a-service/test.txt') as f:
        for line in f:
            request = httpclient.HTTPRequest(destination,
                                             body=line,
                                             method="POST")

            response = yield http_client.fetch(request)
            print response

# get GRAPHITE_HOME from environment variable, or use pwd
def get_graphite_home():
    graphite_home = os.environ.get('GRAPHITE_HOME')
    if graphite_home == None:
        cwd = os.getcwd()
        return cwd

    return graphite_home

def handle_sim_request(config, app):
    os.system("touch %s" % RUNNING_SIM_FLAG)
    while True:
        spawn_sim_job(app)
        # Send results back to controller

        num_jobs_queued = len(os.listdir(CONFIG_PATH))
        if num_jobs_queued == 0:
            break
        else:
            # Move next file in the queue
            newest = max(glob.iglob(CONFIG_PATH + '*.cfg'), key=os.path.getctime)
            shutil.move(newest, GRAPHITE_HOME + 'carbon_sim.cfg')

    #ioloop.IOLoop.current().run_sync(post)
    #post_data = {'data': 'test data'}
    #body = urllib.urlencode(post_data)
    #http_client.fetch(destination, handle_request,

    os.remove(RUNNING_SIM_FLAG)
    print "Job done!"

def spawn_sim_job(app):
    graphite_dir = get_graphite_home()
    os.chdir(graphite_dir)
    if app == "cholesky":
        command = "make %s" % CHOLESKY
    elif app == "barnes":
        command = "make %s" % BARNES
    elif app == "helloworld":
        command = "make %s" % HELLOWORLD
    else:
        print "Could not find specified test to run"
    os.system(command)

if __name__ == "__main__":
    handle_sim_request(None, "cholesky")
