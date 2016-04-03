#!/usr/bin/env python

"""
This is the python script that is responsible for spawning a simulation
"""

import sys
import os
from sim_constants import *

# get GRAPHITE_HOME from environment variable, or use pwd
def get_graphite_home():
    graphite_home = os.environ.get('GRAPHITE_HOME')
    if graphite_home == None:
        cwd = os.getcwd()
        return cwd

    return graphite_home

def handle_sim_request(config, app):
    if os.path.isfile(RUNNING_SIM_FLAG):
        # Move file in a config folder
        # TODO: make outside of here?
        pass
    else:
        os.system("touch %s" % RUNNING_SIM_FLAG)
        spawn_sim_job(app)
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
    handle_sim_request(None, "helloworld")
