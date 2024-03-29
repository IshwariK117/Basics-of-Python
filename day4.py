# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:14:49 2024

@author: sai
"""

# python program  to print odd numbers in given range
start, end = 4, 19

# iterating each number in list
for num in range(start, end+1):

    # checkinh condition
    if num % 2 != 0:
        print(num, end=" ")


# 333
# python program to print even number

start, end = 2, 20

for num in range(start, end+1):
    if num % 2 == 0:
        print(num, end=" ")

###############################
x, y, z = 5, 6, 7
print(x)
print(y)
print(z)
# it is wrong beacuse we can assign value to only one variable
x, y, z = 5
print(x)
print(y)
print(z)

##############################

# lgobal variables
x = "awesome"


def my_function():
    print("python is " + x)


my_function()

###############################
# global local varaible
x = "awesome"


def my_function():
    x = "fantasctic"
    print("python is " + x)


my_function()
print("python is " + x)
###############################

# getting data types
x = 5
print(type((x)))

###################
x = range(6)
print(type(x))

#######################
x = {"name": "ram", "age": 34}
print(type(x))

#########################

# assigning values

x = 1
y = 2.3
z = 2+3j
print(type((x)))
print(type((y)))
print(type((z)))

#############################

str1 = "heloo"
str2 = 2
str3 = str1+str2
# here you will error:can only concatenate str (not "int)
##########################

# string
# if you want multiple strings
x = """This is pythonn.It is verypowerful"""
print(x)
#############################
# string slicing
x = """This is python,It is very powerful"""
# from 2 to 8 i.e 8-1 means 2 to 7
print(x[2:8])
#################################
# slice from start
print(x[:3])

################################
# slicing to the end
print(x[4:])

###################

# negative indexing
print(x[-5:-2])

#####################
# modify string
print(x.upper())
#################
x = x.upper()
print(x.lower())

########################
x="   this is python"
print(x.strip())


x="   this is python"
print(x.lstrip())  #left

x="this is python      "
print(x.rstrip()) #right


########################
x="Hello World"
print(x.replace("Hello","gello"))

########################
x= "hello ,world"
print(x.split(",")) #delimiter is ,

############################
x= "hello  world"
print(x.split("  ")) #delimiter is double  space

##############################
# String reversing


x="Hello world"
string1=x[::-2]
print(string1)

###################################
x="Hello world"
string1=x[::-1]
print(string1)

#######################################
#find method
#find loaction of word
x="this is python and it is powerful"
print(x.find("and"))

###################################
#string concatenation
x="hello"
y="world"
print(x+y)

##################################
#to add white space
x="hello"
y="world"
print(x+" "+y)

#################################
#string format
x=21
y="my name is anthony"
print(x+y)
#it will give error

print(f"my name is deepti and my age is {x}")

#####################################
quantity=3
item_no=54
price=67
print(f"I want {quantity} peices and item number is {item_no}, its price is {price}" )

######################################
my_order="I want {} pieces and item number is {}, its price is {}"
print(my_order.format(quantity,item_no,price))
#########################################

quantity=3
item_no=54
price=67
my_order="I want {0} pieces and item number is {1}, its price is {2}"
print(my_order.format(quantity,item_no,price))
#########################################

#the escape character aloows you to use double quotes when 
text="this is funfair and it has got big \"round rigo\""
print(text)

##########################
#opartor precedance
print(3*3+3/3-3)
"""
Rule for mathmetical operations
PEMDAS
p-paranthesis 
e-exponential
m-multiplication
d-division
a-addition
s-sub

"""
##################################
#identity operators
a=3
b=4
print(a is b)
print(a is not b)

##############################
#list oprtion
lst=["cherry","banana","apple"]
print(lst)

print(lst[0])
print(lst[1])

############################

#append()
#adds an elemnt at the end of the list
lst=["cherry","banana","apple"]

lst.append("Mango")
print(lst)

##############################
#clear removes all itens from list

lst=["cherry","banana","apple"]
lst.clear()
print(lst)

############################
#copy() method
lst=["cherry","banana","apple"]
lst2=lst.copy()
print(lst2)

###########################
#count() return the number of times the value"cherry"
lst=["cherry","cherry","bananaa"]
lst.count("cherry")

###############################
#extend()
#add elements of cars to the fruits
lst=[1,2,3]
lst1=[4,5,6]
lst.extend(lst1)
print(lst)

#################################

#insert()
lst=["cherry","cherry","banana"]
lst.insert(1,"mango")
print(lst)

######################
#pop()
lst=["cherry","cherry","banana"]
lst.pop(1)
print(lst)

lst=["cherry","cherry","banana"]
lst.pop(2)
print(lst)
##################
#remove()
lst=["cherry","cherry","banana"]
lst.remove("cherry")
print(lst)
###############################
lst=["cherry","cherry","banana"]
lst.reverse()
print(lst)

##############################

lst=["cherry","orange","banana"]
lst.sort()
print(lst)

######################3333333

#tuple opartion
tup=("cherry","cherry","banana")
print(tup)
print(tup[2])
###############################
x=("apple","banana","cherry")
x[1]='kiwi'
#it will show ereeor so make it list
#first convert into list
y=list(x)
y[1]="kiwi"

#convert list to tuple
x=tuple(y)
print(x)
###############################
#to join two or moe tuples
tuple1=("a","b","c")
tuple2= (1,2,3)
tup1=tuple1+tuple2
print(tup1)

################################

#dictionary
dict1={"brand":"maruti","model":"2345","year":2011}
print(dict1)
print(len(dict1))
print(type(dict1))

######################################
dict1={ "brnd":["maruti","mahendra","toyota"], "Md":["a","b","c"]  ," year":[2011.2012,2013]}
print(dict1)
print(len(dict1))
print(type(dict1))
###########################
#to get particular key 
dict1.get("brnd")
dict1.keys()

