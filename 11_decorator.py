# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:23:34 2024

@author: sai
"""

#a python decorator is a function
#that takes in a function and 
#returns by adding some functionality

def say_hello():
    return 'hello_there'

def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper

decorate=uppercase_decorator(say_hello)
decorate()

###############################################
#the above same function we can use decortaor by adding @ symbol
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def say_hello():
    return 'hello there'
say_hello()

################################################
#apply multiple decorators
#we can apply multiple decorators to a single function,
#decorator will apply in order


def split_string(function):
    def wrapper():
        func=function()
        splitted_string=func.split()
        return splitted_string
    return wrapper
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
@split_string
@uppercase_decorator
def say_hello():
    return "hello ishwari"
say_hello()

###############################################

import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        total_time=(end-start)*1000
        print(func.__name__+f"took{total_time}mil sec")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
    return result

array=range(1,100000)
out_square=calc_square(array)
out_cube=calc_cube(array)














