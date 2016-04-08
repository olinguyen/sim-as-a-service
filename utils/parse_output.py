#!/usr/bin/env python

import re
import sys
from optparse import OptionParser
from sim_constants import *
import time

global output_file_contents
global num_cores

def searchKey(key, line):
   global num_cores
   key += "(.*)"
   match_key = re.search(key, line)
   if match_key:
      counts = line.split('|')
      event_counts = counts[1:num_cores+1]
      for i in range(0, num_cores):
         if (len(event_counts[i].split()) == 0):
            event_counts[i] = "0.0"
      return map(lambda x: float(x), event_counts)
   return None

def rowSearch1(heading, key):
   global output_file_contents
   heading_found = False
   for line in output_file_contents:
      if heading_found:
         value = searchKey(key, line)
         if value:
            return value
      else:
         heading_found = (re.search(heading, line) != None)

   print "ERROR: Could not find key [%s,%s]" % (heading, key)
   sys.exit(1)

def rowSearch2(heading, sub_heading, key):
   global output_file_contents
   heading_found = False
   sub_heading_found = False
   for line in output_file_contents:
      if heading_found:
         if sub_heading_found:
            value = searchKey(key, line)
            if value:
               return value
         else:
            sub_heading_found = (re.search(sub_heading, line) != None)
      else:
         heading_found = (re.search(heading, line) != None)

   print "ERROR: Could not find key [%s,%s,%s]" % (heading, sub_heading, key)
   sys.exit(1)

def getTime(key):
   global output_file_contents

   key += "\s+([0-9]+)\s*"
   for line in output_file_contents:
      match_key = re.search(key, line)
      if match_key:
         return float(match_key.group(1))
   print "ERROR: Could not find key [%s]" % (key)
   sys.exit(2)

def generate_output_dict():
    global output_file_contents
    global num_cores
    # Read Results Files
    try:
       output_file_contents = open("%s/sim.out" % (SIM_OUTPUT_PATH), 'r').readlines()
    except IOError:
       print "ERROR: Could not open file (%s/sim.out)" % (SIM_OUTPUT_PATH)
       sys.exit(3)

    print "Parsing simulation output file: %s/sim.out" % (SIM_OUTPUT_PATH)
    num_cores = 4
    # Total Instructions
    target_instructions = rowSearch1("Core Summary", "Total Instructions")

    # Completion Time - In nanoseconds
    target_time = rowSearch1("Core Summary", "Completion Time \(in nanoseconds\)")

    # Host Time
    host_time = getTime("Shutdown Time \(in microseconds\)")
    host_initialization_time = getTime("Start Time \(in microseconds\)")
    host_working_time = getTime("Stop Time \(in microseconds\)") - getTime("Start Time \(in microseconds\)")
    host_shutdown_time = getTime("Shutdown Time \(in microseconds\)") - getTime("Stop Time \(in microseconds\)")

    memory = rowSearch1("Core Summary", "Memory")
    execution_units = rowSearch1("Core Summary", "Execution Unit")
    total_mem_accesses = rowSearch1("Shared Memory Model Summary", "Total Memory Accesses")

    l1cache_accesses = rowSearch2("Cache Summary", "Cache L1-I",  "Cache Accesses")
    l1cache_misses = rowSearch2("Cache Summary", "Cache L1-I",  "Cache Misses")
    l1miss_rate = rowSearch2("Cache Summary", "Cache L1-I",  "Miss Rate \(%\)")

    l2cache_accesses = rowSearch2("Cache Summary", "Cache L2",  "Cache Accesses")
    l2cache_misses = rowSearch2("Cache Summary", "Cache L2",  "Cache Misses")
    l2miss_rate = rowSearch2("Cache Summary", "Cache L2",  "Miss Rate \(%\)")

    total_packets_sent = rowSearch2("Network Summary", "Network \(Memory\)",  "Total Packets Sent")
    total_flits_sent = rowSearch2("Network Summary", "Network \(Memory\)",  "Total Flits Sent")
    total_bits_sent = rowSearch2("Network Summary", "Network \(Memory\)",  "Total Bits Sent")
    total_flits_received = rowSearch2("Network Summary", "Network \(Memory\)",  "Total Flits Received")
    total_bits_received = rowSearch2("Network Summary", "Network \(Memory\)",  "Total Bits Received")
    avg_packet_latency = rowSearch2("Network Summary", "Network \(Memory\)",  "Average Packet Latency \(in nanoseconds\)")

    total_dram_accesses = rowSearch1("Dram Performance Model Summary", "Total Dram Accesses")
    avg_dram_latency = rowSearch1("Dram Performance Model Summary", "Average Dram Access Latency \(in nanoseconds\)")

    data = {
      "num_cores": num_cores,
      "target_instructions": target_instructions,
      "target_time": target_time,
      "host_time": host_time,
      "host_initialization_time": host_initialization_time,
      "host_working_time": host_working_time,
      "host_shutdown_time": host_shutdown_time,
      "memory": memory,
      "execution_units": execution_units,
      "total_mem_accesses": total_mem_accesses,
      "l1cache_accesses": l1cache_accesses,
      "l1cache_misses": l1cache_misses,
      "l2cache_accesses": l2cache_accesses,
      "l2cache_misses": l2cache_misses,
      "l2miss_rate": l2miss_rate,
      "total_packets_sent": total_packets_sent,
      "total_flits_sent": total_flits_sent,
      "total_bits_sent": total_bits_sent,
      "total_flits_received": total_flits_received,
      "total_bits_received": total_bits_received,
      "avg_packet_latency": avg_packet_latency,
      "total_dram_accesses": total_dram_accesses,
      "avg_dram_latency": avg_dram_latency,
      "creation_time": int(time.time())
    }
    return data
