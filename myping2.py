#!/usr/bin/python

import subprocess

with open("newlist.in", "r") as hostlist, open("pings.txt", "a") as output:
    for host in hostlist:
        host = host.strip()

        # print "Tracing", host
        print "Pinging", host

	trace = subprocess.Popen(["ping", "-c", "1", "-n", host], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#        trace = subprocess.Popen(["traceroute", "-w", "100", host], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        while True:
            hop = trace.stdout.readline() 
	    hop = hop.splitlines()[0]
            if not hop: break
            
#	    hop = hop2.strip()
            print hop.strip()
            output.write(hop + '\n')

        # When you pipe stdout, the doc recommends that you use .communicate()
        # instead of wait()
        # see: http://docs.python.org/2/library/subprocess.html#subprocess.Popen.wait
trace.communicate()
