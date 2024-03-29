# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:17:50 2024

@author: Mukta
"""

#very important for interview
#mario pyramid
for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()
####################
for i in range(4):
    for j in range(i+1):
        print("#",end=" ")
    print()
#######################3
#diamond
for i in range(5):
    for j in range(5):
        print("#",end=" ")
        
        ##for (int i=n;i>=1;i--){
            ##for (int j=1;j<=i;j++)
##########################
#min And max function
lst =[23,45,22,34,67,89]
def min_max(lst):
    min=lst[0]
    for i in lst:
        if i<min:
            min=i
    print("the minimum value ",min)
    max=lst[0]
    for i in lst:
        if i>max:
            max=i
    print("maximum value",max)
min_max(lst)
########################################
#palindrome Program
def is_palindrome(input):
    if input==" " :
        str2=reversed(input)
        if (str2==input):
            print("given string is palindrome")
        else:
            print("given string kis not palindrome")
    else:
        print("enter valid input")
is_palindrome("step on no pets")
############################
def is_palindrom(input):
    if input=="":
        return "you entered wrong input"
    else:
        string=input[::-1]
        if string==input:
            return True
    return False
print(is_palindrom("step on no pets"))
########################################
#assigning password
#user =["admin","emp","staff","worker"]
user = input("Enter user name:")
if user=="admin":
    print("hello admin would you like to check status")
elif user=="staff":
    print("Hello staff")
elif user=="worker":
    print("hello worker")
elif user=="emp":
    print("hello emp")
elif user=="worker":
    print("hello worker")
else:
    print("Thank you ")
####################################
#design passoword
#pick the adjective
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
passoword= adjective+noun+str(number)+special_char
print("your password is ",passoword)
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
#####################################