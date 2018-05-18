#!/usr/bin/python

import subprocess

with open("newlist.in", "r") as hostlist, open("results.txt", "a") as output:
    for host in hostlist:
        host = host.strip()

        print "Tracing", host

        trace = subprocess.Popen(["traceroute", "-w", "100", host], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        while True:
            hop = trace.stdout.readline()

            if not hop: break

            print '-->', hop.strip()
            output.write(hop)

        # When you pipe stdout, the doc recommends that you use .communicate()
        # instead of wait()
        # see: http://docs.python.org/2/library/subprocess.html#subprocess.Popen.wait
trace.communicate()
