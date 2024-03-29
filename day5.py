# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:16:13 2024

@author: sai
"""
#add elemt in dict
car={
     "brand": "Ford",
     "model":"Mustang",
     "year":1964
     }

x=car.keys()
print(x)
car["color"]="white"
car
x=car.keys()
print(x)

#################################
#remove elemnt from dict
car={
     "brand": "Ford",
     "model":"Mustang",
     "year":1964
     }
car.pop("model")
print(car)

###########################
#accessing keys in dictionary
for x in car:
    print(x)

#accessing  values in dictionary
for x in car:
    print(car[x])
    
###############################

#accesiing both keys and values pair
car={
     "brand": "Ford",
     "model":"Mustang",
     "year":1964
     }
for key,value in car.items():
    print("%s == %s" % (key, value))

###############################

#copyindig ctionary
car={
     "brand": "Ford",
     "model":"Mustang",
     "year":1964
     }
car2=car.copy()
car2

###################################
#another way of copying dict
car={
     "brand": "Ford",
     "model":"Mustang",
     "year":1964
     }
dict1=dict(car)
dict1

##################################
#a dictionary can contain dictionaries, 
#this is called nested dictionaries
our_famimly={
    "child1":{
        "name" : "deepti",
        "Dob"  : "21-05-2008"
        },
    
    "child2":{
        "name" : "Trupti",
        "Dob"  : "01-01-2008"
        }
    
    }
our_famimly
##################################
#dictionary methods
#clear(): Remove all keys and values
car={
     "brand" : "Ford",
     "model" : "mustang",
     "year" : 1964}
car.clear()
car

###############################

#fromkey()
#create a dictonary with 3 keys,all with
x={'key1', 'key2' , 'key3'}
y=0
thisdict=dict.fromkeys(x,y)
thisdict
##############################
#get() : to get the value of dictionary
car={
     "brand": "Ford",
     "model":"Mustang",
     "year":1964
     }
car.get("model")
##########################
#items()
#return the dictionary lyey values
car={
     "brand": "Ford",
     "model":"Mustang",
     "year":1964
     }
car.items()

#################################
#values(): display all values of dictionary
car={
     "brand": "Ford",
     "model":"Mustang",
     "year":1964
     }
car.values()


####################################
#update(): Insert an item to the dictinary
car={
     "brand": "Ford",
     "model":"Mustang",
     "year":1964
     }
car.update({"color":"white"})
car
###########################
fruits=["apple","Banana","orange"]
for i in fruits:
    print(i)
##################################
#break stmt
fruits=["apple","Banana","orange"]
for i in fruits:
    print(i)
    if(i=="Banana"):
        break

##################################
#here it will print only apple
fruits=["apple","Banana","orange"]
for i in fruits:
    if(i=="Banana"):
        break
    print(i)
    
#############################

#continue
fruits=["apple","Banana","cherry"]
for x in fruits:
    if(x=="Banana"):
        continue
    print(x)
    #initally it will take 0
    #which is apple,check condtion
    
#######################################
#range () function
for x in range (2,6):
    print(x)

#############################
#range () function
#2=start
#30=end-1
#3=gap of 3
for x in range (2,30,3):
    print(x)

######################################

#a nested loop is a loop inside a loop
#the inner loop will be  exceuted one time

colors=["green","yellow","red"]
fruits=["guava","banana","apple"]
for x in colors:
    for y in fruits:
        print(x,y)

##################################
def my_function():
    print("Helloo from a function")

my_function()

######################################
def my_function(name):
    print("Hello " +name)
my_function("Deepti")

#####################################
#positional arguments
#more than 2 arguments are called as positional argument
def my_function(name1,name2):
    print(name1+ " "+name2)
my_function("Deepti","khond")

def my_function(name1,name2):
    print(name2+ " "+name1)
my_function("Deepti","khond")
################################
#arbitary arguments 
#  *args
#if we dont know how many argument use * befire paramter

def my_function(*kids):
    print(kids[0]+ " "+kids[2])

my_function("Hello","world","India")

################################

#kwargs
#write ** it allows us to pass keyword arguments 

def myfun(**kwargs):
    for key,value in kwargs.items():
        print("%s == %s" % (key,value))
        
myfun(first="papaplala", mid="mohanlal" , last="Goyal")
        
############################################
#if we call the function withoit agument then its uses
#default value:
def myfun(country="norway"):
    print("I am from " +country)

myfun("sweden")
myfun("India")
myfun()
myfun("brazil")

#####################################
#passing list as an argument
#you can send any data types of argument to a fnction

fruits=["orange","banana","guava"]
def my_function(fruits):
    for x in fruits:
        print(x)
        
my_function(fruits)

#####################################
#return values
#to let aa function return a value use return statment
def myfun(x):
    return x*5
myfun(5)

################################
#pass function
def my_fun():
    pass
#having an empty function definition
#like this would raise an error withut pass statement


###################################

#factorial of a number is product of all integer
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
factorial(3)
factorial(6)

#####################################

# a lambda function also called anynomous functio
#when call fun in code memory sace will be aloocate to function
#lambda fun can take any number of arguments ,but can only
#hav oone expression
def add(a):
    sum=a+10
    return sum
add(20)

#lambda function
add=lambda a:a+10
print(add(20))
#####################################

#lambda fn can take any no of args
add=lambda a,b:a+b
print(add(5,6))
################################
#finding odd no from list
lst=[34,23,45,67,10,20]
odd_lst=list(filter(lambda x:(x%2!=0),lst))
print(odd_lst)
#filter: () methodd accepts two arguments in python:
    #a function and an itearble such as a list

###############################
lst=[34,23,45,67,10,20]
even_lst=list(filter(lambda x:(x%2==0),lst))
print(even_lst)

############################
#square of number in list
lst=[2,6,4,5,10,12,13,14,20,8]

sqr_lst=list(map(lambda x:(x**2),lst))
print(sqr_lst)










       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        












