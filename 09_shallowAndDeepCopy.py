# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 08:15:44 2024

@author: sai
"""

#shallow copy and deep copy
#shallow copy applicable to one level deep , 
#-differ between shallow copy and deep copy
#use copy.copy() , or object specific copy functions
import copy
list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)

#top level structure not affect the original list
list_b[0]=-10
print(list_a)        #[1, 2, 3, 4, 5]
print(list_b)       #[-10, 2, 3, 4, 5]


####################################################
#but when we change inner object then it affect original list also
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.copy(list_a)

#affect the original list
list_a[0][0]=-10
print(list_a)
print(list_b)
#[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]


####################################################
####################################################

#Deep copy#
#full independent clones we use copy.deepcopy()
import copy 
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.deepcopy(list_a)

#not affect the list_b even we change top level structure or inner object
list_a[0][0]=-21
print(list_a)             #[[-21, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print(list_b)             #[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]


###########       Example       #############
import copy

# Original list of lists
original_list = [[1, 2], [3, 4]]

# Perform a shallow copy
shallow_copy = copy.copy(original_list)

# Perform a deep copy
deep_copy = copy.deepcopy(original_list)

# Modify the top-level object in the original list
original_list.append([5, 6])

# Modify the inner object in the original list
original_list[0][0] = 0

print("Original list after modifications:")
print(original_list)   # Output: [[0, 2], [3, 4], [5, 6]]
print("Shallow copy after modifications:")
print(shallow_copy)    # Output: [[0, 2], [3, 4]]
print("Deep copy after modifications:")
print(deep_copy)       # Output: [[1, 2], [3, 4]]





