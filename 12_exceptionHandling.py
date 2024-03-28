# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 04:09:43 2024

@author: sai
"""

#exception handling

try:
    numerator=50
    denom=int(input("enter the denominator"))
    quotient=(numerator/denom)
    print(quotient)
    print("division perform successfully")
except ZeroDivisionError:
    print("divide by zero error")
print('outside try....except')


######################################################
#multiple except block for single try block
try:
    numerator=50
    denom=int(input("ENter denominator"))
    print(numerator/denom)
    print("perform division successfully")
except ZeroDivisionError:
    print("divide by zero error")
except ValueError:
    print("denom should be integer type")
    
#######################################################
#handling exception without name
#even we not mention any unknown exception it raised 
#all other exception handled by this if exception is not present
try:
    numerator=50
    denom=int(input("enter denominator"))
    print(numerator/denom)
    print("perform successfully")
except ValueError:
    print("denom should be of integer type")
except:
    print("some error occur")
    
#enter denominator 0
#some error occur
    
########################################################
#else block- if try block not has any error then it will go in else block to show output
#otherwise it will go to raised an exception

try:
    numerator=50
    denom=int(input("enter denominator"))
    quo=numerator/denom
    print("perform successfully")
except ValueError:
    print("denom should be of integer type")
except:
    print("some error occur")
else:
    print("the result is ",quo)
    
'''
enter denominator 5
perform successfully
the result is  10.0
'''
##############################################################
#handling exception using try..except..else..finally
#finally block-always executed even irrespective
# of it raised exception or not and it run successfully
try:
    numerator=50
    denom=int(input("enter denominator"))
    quo=numerator/denom
    print("perform successfully")
except ValueError:
    print("denom should be of integer type")
except:
    print("some error occur")
else:
    print("the result is ",quo)
finally:
    print("OVER AND OUT")
    
'''
enter denominator10
perform successfully
the result is  5.0
OVER AND OUT
'''
#################################################################


    
    
    
