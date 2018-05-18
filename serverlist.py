#!/usr/bin/env python

import sys, csv

with sys.stdin as f:
    reader = csv.reader(f)
    for row in reader:
        for col in row:
            print col+'\t',
        print
