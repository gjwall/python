#!C:\python36\python.exe

'''
Created on 4 Mar 2017

@author: Graham
'''

#import PythonProjects.Circle1 as Circle1
from PythonProjects.Circle1 import Circle1 as Circle1

from PythonProjects.Circle2 import Circle2 as Circle2

#use () when a function
c1 = Circle1(42)
print (c1.area())

# print (c1.__radius)
print (c1.getRadius())

c1.setRadius(66)
print (c1.area())
#c1.setRadius(-4)


# use NO () when defined as @property
c2 = Circle2(42)
print (c2.area)

# print (c2.__radius)
#print (c2.getRadius())

c2.radius = 12
print (c2.area)
#c2.radius = -4

help(property)
