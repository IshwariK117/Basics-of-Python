# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:53:53 2024

@author: Mukta
"""

x= 1
z=float(x)
print(z)

str1='hello'
str2=2
str3=str1+str2
#here we will error:can only concatenate str(not 'int')
########################
#if you want multiple strings
x ='''this is python.it is very powerful'''
print(x)
#string slicing
x ='''this is pyhton.it is very powerful'''
print(x[2:8])
#slice from the start
print(x[:3])
##slicing to the end
print(x[4:])

#negative indexing
print(x[-5:-2])
####################################
####modify string
print(x.upper())
########################
x=x.upper()
print(x.lower())
############################
#remove white space ,removes white space from initial to
x='      this is pyhton      '
print(x.strip())
print(x.rstrip())
#replace
x="hello world"
print(x.replace("hello", "gello"))

#use of split which replace white space/or ,
x="Hello world"
print(x.split(" "))
print(x.split(" ,"))

