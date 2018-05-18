#!/usr/bin/python
from pexpect import pxssh
import getpass 
import sys
from subprocess import call 
import re

i = open("newlist.in", 'r')
x = i.readlines()
username = "de616491"  			# Insert your Linux user ID here
password = "kpTOc24MzpBR"  		# Insert your Linux password here
f = open("splunkcheck.out", 'w')
s = pxssh.pxssh()
pat = re.compile("^###")
pat0 = re.compile("^SunOS")
pat1 = re.compile("^Linux")
for syshost in x:
    call('traceroute', syshost) # > traceroute.log
#    if not pattern.match(item):
#        continue
#    else:
#        print item	
    s = pxssh.pxssh()
    hostname = syshost 
    # hostname = raw_input('hostname: ')
    # username = raw_input('username: ')
    # password = getpass.getpass(p)
    try:
        s.login (hostname, username, password)
        hn = os.system("hostname")
#        s.sendline ('hostname -a')
#        s.prompt()
        f.write(hn)
        un = os.system("uname -a")
        s.sendline ('uname -a')   		# run a command
        s.prompt()             			# match the prompt
        f.write(un)          		# print everything before the prompt.
        if pat0.match(un):
            sunos = os.system("pkginfo -l | grep splunk")
#            s.sendline ('pkginfo -l | grep splunk')
#            s.prompt()
            f.write(sunos)
            continue
        elif pat1.match(s.before):
            s.sendline ('rpm -qa | grep splunk')
            s.prompt()
            f.write=(s.before)
            continue
#        s.sendline ('lsb_release -a')
#        s.prompt()
#        f.write(s.before)
#        s.sendline ('ps -ef|grep splunk')
#        s.prompt()
#        f.write(s.before)
	s.sendline ('\n\n')
	s.prompt()
	f.write(s.before)
        sys.stdout = f
        s.logout()
    except s.login, e:
        print("Hostname: {0:s} pxssh failed on login.".format(hostname))
        print str(e)

f.close()


#def ssh(host, cmd, user, password, timeout=30, bg_run=False):
#"""SSH'es to a host using the supplied credentials and executes a command.
#Throws an exception if the command doesn't return 0.
#bgrun: run command in the background"""

#fname = tempfile.mktemp()
#fout = open(fname, 'w')

#options = '-q -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oPubkeyAuthentication=no'
#if bg_run:
#    options += ' -f'
#ssh_cmd = 'ssh %s@%s %s "%s"' % (user, host, options, cmd)
#child = pexpect.spawn(ssh_cmd, timeout=timeout)
#child.expect(['password: '])
#child.sendline(password)
#child.logfile = fout
#child.expect(pexpect.EOF)
#child.close()
#fout.close() 

#fin = open(fname, 'r')
#stdout = fin.read()
#fin.close()

#if 0 != child.exitstatus:
#    raise Exception(stdout)

#return stdout
