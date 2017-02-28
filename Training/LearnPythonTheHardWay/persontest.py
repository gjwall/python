#!C:\python36\python.exe
'''
Created on 28 Feb 2017

@author: Graham
'''

# from LearnPythonTheHardWay.person import Person
from LearnPythonTheHardWay.player import Player
from LearnPythonTheHardWay.person import Person

me = Player("Graham", "Wallace", 1500)
#me.print()
print(me.toString())

peopleList = [ Person("Graham", "Wallace"), Person("Gemma", "Wallace")] 

for person in peopleList:
    print (person.toString())
    