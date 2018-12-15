  #!/usr/bin/env python3
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta    
# in and not in 
# Use in and not in to check whether a particular element is included in the list
a_list = [1, 2, 3]
a = 2 in a_list
print("Output #79: {}".format(a))
if 2 in a_list:
    print("Output #80:2 is in {}.".format(a_list))
b = 6 not in a_list
print("Output #81: {}".format(b))
if 6 not in a_list:
    print("Outpet #82: 6 not in {}.".format(a_list))

# append, remove, pop function
# Add an element to the end of the list using the append () function.
# Use the remove () function to remove a specific element from the list.
# Use the pop () function to remove the last element of the list.
a_list.append(4)
a_list.append(5)
a_list.append(6)
print("Output #83: {}".format(a_list))
a_list.remove(5)
print("Output #84: {}".format(a_list))
a_list.pop()
a_list.pop()
print("Output #85: {}".format(a_list))
      
# reverse function
# Reverse the list using the reverse function.
# Since the (in-place) change occurs in the list
# you must first make a copy to reverse the existing list without changing it.
a_list.reverse()
print("Output #86: {}".format(a_list))
a_list.reverse()
print("Output #87: {}".format(a_list))

# sort function
# Use sort() functions to sort the list by in-place.
# This means that the list changes.
# To sort the list without changing the existing list, first make a copy.
# unordered - Unaligned.
unordered_list = [3, 5, 1, 7, 2, 8, 4, 9, 0, 6]
print("Output #88: {}".format(unordered_list))
list_copy = unordered_list[:]
print("Output #89: {}".format(list_copy))
print("Output #90: {}".format(unordered_list))

# sorted function
# Sorting the list according to a specific position of the list using the sorted () function.
my_lists = [[1,2,3,4], [4,3,2,1], [2,4,1,3]]
my_lists_sorted_by_index_3 = sorted(my_lists, key=lambda index_value: index_value[3])
print("Output #91: {}".format(my_lists_sorted_by_index_3))
 
# References Foundations for Analytics with Python.
