# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:19:04 2024

@author: Mukta
"""

'''
to ignore the fractional 
this operator is referred as the integer division operator
'''
print(100//20)
print(type(100//20))
''' 
but if we are only intrested in the reminder
part of the division, the integer division operator has lost that?
well in that case you can use the modules operation  %


'''

print('modules division 100 % 13:',100%13)
print('modules division 3%2:',3%2)

'''
a final integer operator we well LOOK at is the power operator that caan be used to raise an integer bya given  power, for
example 5 to the power of 3.
the power operator is '**'
'''
a = 4
b = 8
print(a ** b)


#assignment operator
'''
these assignment operator are actually
'''
x = 0
x += 1# has the same behaviour as x = x+1
x

#None value
#python 
winner = None
print(winner is None)
print(winner is not None)

print('winner:', winner)
print('winner is none:', winner is None)
print('winner is not none:', winner is not None)


#comparision operator
'''
'''
num = int(input('enter a number:'))
if num > 0:
  print(num)#this code indentation error 
#now let us give the indentation
num = int(input('enter a number:'))
if num > 0:
    print(num)
    
#else in an  If statement
num = int(input('enter a number:'))
if num < 0:
    print('Its negative')
else:
    print('its positive')
    
#the use of elif




