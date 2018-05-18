#!/usr/bin/python

import os
import csv


with open("/Users/stuartskelton/Documents/Alstom_UX_List.csv") as csvfile:
   readCSV = csv.reader(csvfile, delimiter=',')
   hostname = []
   for row in readCSV:
        domain = '.dom1.ad.sys'
        hostname = row[0]

#        hostname.append(name)
        response = os.system("ping -c 1 " + str(hostname) + domain)
        
        #and then check the response...
        if response == 0:
           print hostname, 'is up!'
        else:
           print hostname, 'is down!'


