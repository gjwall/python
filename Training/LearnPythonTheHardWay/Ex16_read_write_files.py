#!C:\python36\python.exe

'''
Created on 27 Feb 2017

@author: Graham
'''

from sys import argv

script, fileName = argv

print ("We are goign to erase %r" % fileName)

input("?")

print ("Opening the file")
target = open(fileName, 'w')


print ("Truncating the file")
target.truncate()

print ("Input new text next")

line1 = input ("Line 1: ")

target.write(line1)
target.write("\n")

print ("Close the file like a good citizen")
target.close()


