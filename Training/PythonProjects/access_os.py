#!C:\python36\python.exe

'''
Created on 5 Mar 2017

@author: Graham
'''

import os
import platform
import subprocess as sub

my_login = os.getlogin()

print("My login = " + my_login)

my_system = platform.system()

print ("My OS = " + my_system + " " + os.name)

# print (os.umask())

# print (os.uname())

print (os.getpid())

print (os.getppid())

print (os.getcwd())

print (len(os.environ))

for key in os.environ.keys():
    print ("%30s %s \n" % (key,os.environ[key]))    
    
# Old way
# sub.call(["cmd", "/c", "dir", "/b"])

sub.run(["cmd", "/c", "dir", "/b"])

print("POpen with Shell")
sub.Popen(["cmd /c dir "], shell = True)

print ("POpen with shell and pipe")
my_dir = sub.Popen(["cmd /c dir "], shell = True, stdout=sub.PIPE)

for f in my_dir.stdout: 
    print (f)
#b' means a bytestring

print("\nListing a directory in Python\n")
print(os.listdir("."))
print (os.stat("ch1_ex1.py"))

    
