# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:54:33 2024

@author: Mukta
"""

#else in an  If statement
num = int(input('enter a number:'))
if num < 0:
    print('Its negative')
else:
    print('its positive')
    
#the use of elif
savings = float(input('enyter  how much your savings:'))
if savings == 0:
    print('sorry no savings')
elif savings < 500:
    print('well done')
elif savings < 1000:
    print('thats tidy sum')
elif savings < 10000:
    print('welcome sir')
else:
    print('thank you')
    
marks = int(input('Enter your marks:'))
if marks <= 35:
    print('fail')
elif marks > 60:
    print('first class')
else :
    print('first class dist')
    


