#!C:\python36\python.exe
'''
Created on 28 Feb 2017

@author: Graham
'''

class Person(object):
    
    def __init__(self, foreName, surName):
        self.foreName = foreName
        self.surName = surName
        
    def print(self):
        print(self.foreName + " " + self.surName)

    def toString(self):
        return self.foreName + " " + self.surName
