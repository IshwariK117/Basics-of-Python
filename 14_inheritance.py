# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 20:07:41 2024

@author: sai
"""

#########   inheritance in python
'''
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
'''


class vehicle:
    def general_usage(self):
        print("general use:transporatation")
        
class car(vehicle):
    def __init__(self):
        print("I am car")
        self.wheels=4
        self.has_roof=True
        
        
    def specific_usage(self):
        self.general_usage()
        print("vacation with family")
        

class motorcycle(vehicle):
    def __init__(self):
        print("i am motorcycle")
        self.wheel=2
        self.has_roof=False
    
    def specific_usage(self):
        self.general_usage()
        print("vacation with me only")
    
    

c=car()
m=motorcycle()

m.general_usage()   #general use:transporatation
c.specific_usage() 
 #general use:transporatation
 #vacation with family
m.specific_usage() 
#general use:transporatation
#vacation with me only

print(issubclass(car,  motorcycle))           #parameter - issubclass(subclass,superclass)

##############################################################################
#super class
class Person:
    def __init__(self,name,age):
        self.nm=name
        self.ag=age
        
    def myfunc(self):
        print("my name",self.nm,"and my age is",self.ag)
        
class Student(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        
s=Student("ishwari",23)
s.myfunc()
#my name ishwari and my age is 23

##############################################################################

#multiple Inheritance

class Father:
    def skills(self):  #This is not constructor
        print("I like gardening and programmimg")
        
class Mother:
    def skills(self):     #This is not constructor
        print("I like cooking art")
        
class child(Father,Mother):   #child class
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("I like sports")
        
c=child()
c.skills()





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        




















