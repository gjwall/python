#!C:\python36\python.exe

'''
Created on 27 Feb 2017

@author: Graham
'''

from sys import argv

script, fileName = argv

txt = open(fileName)

print ("Here is  your file %r" % fileName)
print (txt.read())

txt.close()

