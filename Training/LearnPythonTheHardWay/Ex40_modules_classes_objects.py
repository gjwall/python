#!C:\python36\python.exe

'''
Created on 28 Feb 2017

@author: Graham
'''

#from mystuff import MyStuff
from LearnPythonTheHardWay.mystuff import MyStuff as ms

mystuff2 = { 'apple' : "I LOVE APPLES!" }

print ( mystuff2['apple'] )

#mystuff.apple()
#
#print ( mystuff.tangerine )

#myvar = MyStuff()
myvar = ms()
print (myvar.tangerine)

