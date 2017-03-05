#C:\python36\python.exe

'''
Created on 4 Mar 2017

@author: Graham
'''

from math import pi as pi

class Circle2(object):
    
    def __init__(self, radius):
            #self.__radius = radius
            self.__setRadius(radius)
            
    def __setRadius(self, newValue):
        if newValue >= 0:
            self.__radius = newValue
        else:
            raise ValueError("Value must be positive")
        
    radius = property(None, __setRadius)
        
    @property
    def area(self):
        return pi * (self.__radius ** 2)
        