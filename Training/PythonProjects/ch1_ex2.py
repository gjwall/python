#!:C\python36\python.exe
'''
Created on 3 Mar 2017

@author: Graham
'''

def straightLine(gradient, x, constant): 
    ''' returns y coordinate of a straight line
        gradient * x + constant'''
    return (gradient * x) + constant


ans = straightLine(2, 4, -3)

print (ans)

