# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:17:01 2024

@author: sai
"""

class Human:
    def __init__(self,n,o):   #All classes have a function called __init__(), which is always executed when the class is being initiated.
        self.name=n            #constructor is responsible for create instance
        self.occupation=o
        
    def do_work(self):
        if self.occupation=='tennis player':
            print(self.name,"play tennis")
        if self.occupation=='actor':
            print(self.name,"shoot film")
    
    def speaks(self):
        print(self.name,"says how are you?")

tom=Human("tom_cruise","actor")     #object-instance of class
tom.do_work()
tom.speaks()
    
maria=Human("maria_sherapova","tennis player")
maria.do_work()
maria.speaks()

#######################################################################
#Create a class named Person, use the __init__() function to assign values for name and age:


class person:
    def __init__(self, n=None, a=None):
        self.name = n
        self.age = a
        
    def girl(self, name, age):
        print(name)
    
    def boy(self, name, age):
        print(name, age)
    
p = person()  # Instantiating person without parameters
p.girl("ishwari", 13)
p.boy("adi", 12)

##########################################################################
#Insert a function that prints a welcom ----from ----, and execute it on the p1 object:
class greet:
    def __init__(self,n,c):
        self.name=n
        self.Class=c
        
        
    def func(self):
        print("Welcome",self.name ,"from",self.Class)
        
    
p1=greet("ishwari","TY")
p1.func()


    
    
    
    
    
    
    
    
    
    
    
