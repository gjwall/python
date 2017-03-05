#!:C\python36\python.exe
'''
Created on 3 Mar 2017

@author: Graham
'''

def straightLine(gradient, x, constant): 
    ''' returns y coordinate of a straight line
    ->  gradient * x + constant'''
    return (gradient * x) + constant


ans = straightLine(2, 4, -3)

print (ans)

help(straightLine)

for x in range(10): 
    print(x, straightLine(2, x, -3))

# Generator functions
print ("Generator functions")
def odds(start=1):
    ''' return all odd numbers from start upwards '''
    if int(start) % 2 == 0: 
        start = int(start) + 1
    while True:
        yield start
        start += 2
        
for n in odds():
    if n > 7:
        break
    else:
        print(n)

# Lambda functions
print ("\nLambda functions\n")
lambdaStraightLine = lambda m, x, c: (m * x) + c
print(lambdaStraightLine(2, 4, -3))

#Classes and objects 
print("\nClasses and objects\n")

class MyClass(object):
    
    instanceCount = 0
    
    def __init__(self, value):
        self.__value = value
        MyClass.instanceCount += 1
        print("Instance number {} created".format(MyClass.instanceCount))
    
    def aMethod(self, aValue):
        self.__value *= aValue
        
    def __str__(self, *args, **kwargs):
        return "A MyClass instance with value: " + str(self.__value)
    
    def __del__(self):
        MyClass.instanceCount -= 1

print(MyClass.instanceCount)
myInstance = MyClass(42)

myInstance.aMethod(66)
print(MyClass.instanceCount)

print(myInstance)

del(myInstance)
print(MyClass.instanceCount)


# Circle test


