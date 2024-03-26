# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:20:10 2024
@author: sai
"""

import pandas as pd

#1.An absolute path specifies the complete location of a file or directory in the file system.
#2.A relative path specifies the location of a file or directory relative to the current working directory. 
# Read 'buzzers.csv' using pandas
f1 = pd.read_csv('buzzers.csv')     #relative path
######################################

# Open the file using with statement
import os
with open('C:/Users/sai/1-Python/buzzers.csv') as raw_data:  #absolute path
    # Read and print the contents of the file
    print(raw_data.read())

#######################################
#reading csv data as a list
import csv
with open('C:/Users/sai/1-Python/buzzers.csv') as raw_data:
    for line in csv.reader(raw_data):
        print(line)
        
'''
['ï»¿"TIME', 'DESTINATION"']
['09:35,FREEPORT']
['17:00,FREEPORT']
[]
['19:00,WEST END']
['10:45,TREASURE CAY']
[]
['11:45,ROCK SOUND']
['17:55,ROCK SOUND']
'''
#########################################
#read data in form of dictionary
import csv
with open('buzzers.csv') as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)
        
#########################################
'''
flights = {}  # Initialize an empty dictionary to store flights data

# Open the CSV file using with statement
with open('buzzers.csv') as data:
    # Iterate over each line in the file
    for line in data:
        # Split the line into key and value using comma as separator
        k, v = line.strip().split(',')
        #key,value,split(delimiter=,)
        # Store the key-value pair in the flights dictionary
        flights[k] = v

# Print the flights dictionary
print(flights)
'''

#####################################################

#####################################################
#DECORATORS
def plus_one(number):
    # Inside the function, add 1 to the input number
    number1 = number + 1
    
    # Return the result of the addition
    return number1

# Call the function with an argument of 5
result = plus_one(5)

# Print the result
print(result)


###############################################
#nested function 
def plus_one(number):
    def add_one(number):
        number1 = number + 1
        return number1
    
    result=add_one(number)
    return result
plus_one(4)

##############################################
#passing function as argument
def plus_one(number):
    result=number+1
    return result

def function_call(function):
    result1=function(6)
    return result

function_call(plus_one)

###############################################
#function returning other function
def hello_function():
    def say_hi():
        return "hi"
    return say_hi

hello=hello_function()
hello()           #'hi'

################################################
#need for decorators
import time
def calc_square(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"Total time for execution square is {total_time}")
    return result

def calc_cube(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"total time for execution cube is {total_time}")
    return result

array=range(1,100000)
out_square=calc_square(array)
out_cube=calc_cube(array)

#output depend on configuration and which operating system we are using
#Total time for execution square is 15.651702880859375
#total time for execution cube is 31.247377395629883




    