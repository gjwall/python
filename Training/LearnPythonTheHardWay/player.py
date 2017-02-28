'''
Created on 28 Feb 2017

@author: Graham
'''
from LearnPythonTheHardWay.person import Person

class Player(Person):
    '''
    classdocs
    '''

    def __init__(self, foreName, surName, rating):
        super().__init__(foreName, surName)
        self.rating = rating
        
    def print(self):
        super().print()
        print(", rating = " + str(self.rating))

    def toString(self):
        return super().toString() + ", rating = " + str(self.rating)
