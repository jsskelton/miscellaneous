#!/usr/bin/python
# const_output.py

import sys
from subprocess import Popen

if len(sys.argv) < 2:
    print 'Usage: const_output.py "command to watch"'
    sys.exit(1)

cmd_line = sys.argv[1:]

p = Popen(cmd_line)
p.communicate()[0]
