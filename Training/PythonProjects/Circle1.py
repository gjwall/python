#C:\python36\python.exe

'''
Created on 4 Mar 2017

@author: Graham
'''

from math import pi as pi

class Circle1(object):
    
    def __init__(self, radius):
            #self.__radius = radius
            self.setRadius(radius)
            
    def setRadius(self, newValue):
        if newValue >= 0:
            self.__radius = newValue
        else:
            raise ValueError("Value must be positive")
        
    def getRadius(self):
        return self.__radius
        
    def area(self):
        return pi * (self.getRadius() ** 2)
        
