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
import httplib
import urllib
import requests
import json
from parse_output import *

destination = 'http://45.79.178.142:8889/results'

# get GRAPHITE_HOME from environment variable, or use pwd
def get_graphite_home():
    graphite_home = os.environ.get('GRAPHITE_HOME')
    if graphite_home == None:
        cwd = os.getcwd()
        return cwd

    return graphite_home

def handle_sim_request(app, email):
    print "Starting jobs"
    os.system("touch %s" % RUNNING_SIM_FLAG)
    while True:
        spawn_sim_job(app)
        # Send results back to controller
        data = generate_output_dict()

        # Send post request to controller
        headers = {"Content-type": "application/json", "Accept": "text/plain"}
        response = requests.post(destination, data=json.dumps(data), \
                                 headers=headers)

        # Email user that simulation finished
        send_simple_message(email)

        # Save sim.out
        save_output(app, email)

        num_jobs_queued = len(os.listdir(CONFIG_PATH))
        if num_jobs_queued == 0:
            break
        else:
            # Move next file in the queue
            oldest = min(glob.iglob(CONFIG_PATH + '*.cfg'), key=os.path.getctime)
            shutil.move(oldest, GRAPHITE_HOME + 'carbon_sim.cfg')

    os.remove(RUNNING_SIM_FLAG)
    print "Job done!"

def save_output(app_name, email):
    shutil.copyfile(SIM_OUTPUT_PATH + '/sim.out', SIM_HIST_PATH + 'sim-%s-%s-%d-.out' % (app_name, email, int(time.time())))

def spawn_sim_job(app):
    graphite_dir = get_graphite_home()
    os.chdir(graphite_dir)
    if app == "cholesky":
        command = "make %s" % CHOLESKY
    elif app == "barnes":
        command = "make %s" % BARNES
    elif app == "ping_pong":
        command = "make %s" % PINGPONG
    elif app == "fft":
        command = "make %s" % FFT
    else:
        print "Could not find specified test to run"
    os.system(command)

def send_simple_message(email):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox0b783b0de07744d29f52597d3423ebfc.mailgun.org/messages",
        auth=("api", "key-ab35a192ec8788bf2d0678d2a996304f"),
        files=[("attachment", open(SIM_OUTPUT_PATH + '/sim.out')), \
               ("attachment", open(SIM_OUTPUT_PATH + '/carbon_sim.cfg'))],
        data={"from": "Mailgun Sandbox <postmaster@sandbox0b783b0de07744d29f52597d3423ebfc.mailgun.org>",
              "to": "COEN498 <%s>" % email,
              "subject": "Simulation Complete!",
              "text": "Hello, \n\nYour simulation has just completed. Here are the results!\n\nHave a nice day!"})

if __name__ == "__main__":
    app_name = sys.argv[1]
    email = sys.argv[2]
    handle_sim_request(app_name, email)
