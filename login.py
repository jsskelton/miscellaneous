#!/usr/bin/python
import time
class Log:
    usernames = ['usernames']
    passwords = ['testpass']
    hostnames = ['hostnames']
    def __init__(self, username, password, hostname):
        self.username = username
        self.password = password
        self.hostname = hostname
        if self.username in self.usernames:
            self.checkPass()
        else:
            self.loginFail()

    def loginSuccessful(self):
        print "Login successful, please enter!"

    def checkPass(self):
        if self.password in self.passwords:
            self.loginSuccessful()
        else:
            self.loginFail()

    def checkhostname(self):
        if self.hostname in self.hostnames:
            self.hostnameSuccessful()
        else:
            self.hostnameFail()

    def loginFail(self):
        print "Login failed, please try again."

username = raw_input("Please enter your username: ")
password = raw_input("Please enter your password: ")
hostname = raw_input("Please enter the hostname: ")


login = Log(username, password, hostname)
