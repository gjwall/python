#!C:\python36\python.exe

'''
Created on 27 Feb 2017

@author: Graham
'''

from sys import argv

script, userName = argv

prompt = "> "

print ("Hi %s, I'm the %s script" % (userName, script))
likes = input("Do you like me %s? " % userName)

print ("You said '%s' about liking me" % likes)


