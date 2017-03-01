#!C:\python36\python.exe

'''
Created on 1 Mar 2017

@author: Graham
'''

aString = "I love spam"
anotherString = "I love spam"
anInt = 6
intAlias = anInt

print (aString == anotherString)

print (aString is anotherString)

print (anInt == intAlias)

print (anInt is intAlias)

s1 = "0123456789"

# Print all members
print (s1[:])

# Print members starting at 3, steps of 1
print (s1[3:])

# Print members ending at 3, steps of 1
print (s1[:3])

# Print members from 3 - 7
print (s1[3:7])

# Print members from 3-7 in steps of 2
print (s1[3:7:2])

# Print all members in steps of 3 
print (s1[::3])


# Tuples, immutable
print( divmod(12,7))
q, r = divmod(12,7)
print (q)
print (r) 

def straightLine(gradient, x, constant):
    ''' returns y coordinate of a straight line gradient * x  constant '''
    return ( gradient * x ) + constant

print (straightLine(2, 4, -2))

for x in range(10):
    print(x, straightLine(2, x, -3))

help(straightLine)
