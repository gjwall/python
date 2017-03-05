#!C:\python36\python.exe

'''
Created on 5 Mar 2017

@author: Graham
'''

import os
import platform

my_login = os.getlogin()

print("My login = " + my_login)

my_system = platform.system()

print ("My OS = " + my_system + " " + os.name)

# print (os.umask())

# print (os.uname())
