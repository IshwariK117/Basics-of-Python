# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:18:30 2024

@author: Mukta
"""
#list comprehension
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

##########################################
#we can write same method with  list omprehension
lst =[num for num in (0,20)]
print(lst)
##########################################
names=['dada','mama','kaka']
lst=[name.capitalize() for name in names]
print(lst)
#################################################
#list comrehension with if statement
def is_even(num):
    return num%2==0 
lst =[num for num in range(10) if is_even(num) ]
print(lst)
################################################

#for loop inside for loop 
lst =[f"{x}{y}" for x in range(3)for y in range(3)]
print(lst)
##################################################
#Dictionary Comprehension
dict ={x:x*x for x in range(3)}
print(dict) 
###############################################
#generator
'''
It is another way of creating iterators
in a simple way where it uses the keyword "yeild"
instead of returning it in a defind function.
Generator are implemented using a function
'''
gen =(x for x in range(3))
print(gen)
for num in gen:
    print(num)
#############################################
gen=(x
     for x in range(3)
     )
next(gen)
next(gen)
#############################################
#function which return multiple value
#we write here function which return multiple value
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):#passing value in the function itself
    print(num)
#########################################
#now instead of using for loop we can write our own
gen =range_even(6)
next(gen)
next(gen)
next(gen)
###########################################3
#chaining generators
#when we want to write generator inside a generator then we use this
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
'''
ele* appears to be a placeholder for an element
from an iterable.The asterisk (*) is likely
just a character used to represent a  plsceholder
or a wildcard.
for instance,if you're iterating
over a list of element,"ele*"
could symbolize any element in that list.
It is a generic representation 
that doesn't correspond to any specific syntax
in python or itertools

'''
passwords=["not-good","give'm-pass","00100=100"]
for password in hide(lengths(passwords)):
    print(password)
#############################################

def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
import string
adjectives =['milky','sleepy','slow','smelly','wet','orange']
#pick the noun
nouns =['apple','mango','banana','dragon','ball','panda']
import random
adjective = random.choice(adjectives)
noun =random.choice(nouns)
number = random.randrange(1,100)
#spacial_char= random.choice(string.punctuation)
special_char=random.choice(string.punctuation)
password= adjective+noun+str(number)+special_char
for password in hide(lengths(passwords)):
    print(password)




'''
print('Welcome to password picker!')
while True:
    adjectives =['milky','sleepy','slow','smelly','wet','orange']
    nouns =['apple','mango','banana','dragon','ball','panda']
    
    adjective = random.choice(adjectives)
    noun2=noun.upper()
    noun =random.choice(nouns)
    number = random.randrange(1,100)
    #spacial_char= random.choice(string.punctuation)
    special_char=random.choice(string.punctuation)
    passoword= adjective+noun+noun2+str(number)+special_char
    print("your password is ",passoword)
    
    response=input('would you like to generate another password?')
    if response== 'n':
        break
'''
#########################################3
#########################################
#Enumerate
#printing list with index
lst=["milk","egg","bread"]
for index in range(len(lst)):
    print(f'{index}+1 {lst[index]}')
##########################################
#same code can be implemented using enumerate
lst=["milk","egg","bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")
#################################################
#use of zip function
#zip function means combine 2 or more list
name  =['dada','mama','kaka']
info=[8745,2345,1234]
for nm,inf in zip(name,info):
    print(nm,inf)
##############################################
#zip function with mi smatch list
name  =['dada','mama','kaka','baba']
info=[8745,2345,1234]
for nm,inf in zip(name,info):
    print(nm,inf)
#it will not display excess mis,match item in name
#i.e baba
#########################################
#zip_longest
from itertools import zip_longest
name  =['dada','mama','kaka']
info=[8745,2345,1234,5637]
for nm,inf in zip_longest(name,info):
    print(nm,inf)
##########################################3
#use of all(),if all the value are true then it will produce output

lst =[2,3,-6,7,9]
if all(lst):
    print('all values are true')
else:
    print('there  are zero values')
    
#################################
lst =[2,3,0,7,9]
if all(lst):
    print('all values are true')
else:
    print('there  are zero values')
###################################3
#use of any if any one non zero values
lst =[0,0,0,0,0,0]
if any(lst):
    print('it has some value')
else:
    print('all values are zero in the list')
############################
lst =[0,0,0,0,0,9]
if any(lst):
    print('it has some value')
else:
    print('all values are zero in the list')
#######################################
#count
from itertools import count
counter =count()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
#######################################
#now let us start from 1
from itertools import count
counter=count(start=7)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
#########################################3
#cycle()

#suppose you have repeated tasks to be done then you
#use in real time machine learning application
import itertools
instructions=("Eat","code","sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)
##############################################
#repeat()
from itertools import repeat
for msg in repeat("keep patience", times=3):
    print(msg)
########################################
#cobinationss() 
#combination is a arrangement
from itertools import combinations
players=['john','jani','janardhan']
for i in combinations(players, 2):
    print(i)
######################3##################3
from itertools import combinations
players=['john','mukta','prita','rushi','prince','jani','janardhan']
for i in combinations(players, 2):
    print(i)
####################################3
#permutations
from itertools import permutations
players=['john','mukta','prita','rushi','prince','jani','janardhan']
for seat in permutations(players,2):
    print(seat)
##############################3
#product()
from itertools import product
team_a=['Rohit','pandya','bumrah']
team_b=['virat','manish','sami']
for  pair in product(team_a,team_b):
    print(pair)
##############################
#filter
#when we want to select and apply some ligic then use filter
#when we want spacific output then use map
age=[23,54,56]
adult=filter(lambda age:age>=18,age)
print([age for age in adult])
#####################################
'''
in pyhton ,assignment statement (obj_b=obj_a)
do not create real copies
It only creates a new  variable with the samr references
so when you want

-shallow copies:only one level deep.It creates a new colle
and popilates it with refernces to the nested object.
This means modyfing a nested object in the copy deeper than

'''
#assignment operator
#this will only a new variable with the same reference
list_a=[1,2,4,5]
list_b=list_a
list_a[0]=-10
print(list_a)
print(list_b)


    