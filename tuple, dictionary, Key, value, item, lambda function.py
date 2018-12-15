# -*- coding: utf-8 -*-
     
#!/urs/bin/env python3
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta 
from operator import itemgetter

# Arrange lists according to two index positions using itemgetter () function.
my_list = [[123,2,2,444],[22,6,6444],[354,3,3,678],[236,5,5678]], \
[578,1,1,290],[461,1,1,290]
my_lists_sorted_by_index_3_and_0 = sorted(my_lists, key=itemgetter(3,0))
print("Output #92: {}".format(my_lists_sorted_by_index_3_and_0))
      
# Creating a tuple.
# Use parentheses to create tuple.
my_tuple = ('x', 'y', 'z')
print("Output #93: {}".format(my_tuple))
print("Output #94: my_tuple has {} elements".format(len(my_tuple)))
print("Output #95: {}".format(my_tuple[1]))
longer_tuple = my_tuple + my_tuple
print("Output #96: {}".format(longer_tuple))

# Unpack the tuple
# Unpack the tuple to the left of the assignment operator (=)
one, two, three = my_tuple
print("Output #97: {0} {1} {2}".format(one, two, three))
var1 = 'red'
var2 = 'robin'
print("Output #98: {} {}".format(var1, var2))
# Exchange values ​​between variables
var1, var2 = var2, var1
print("Output #99: {} {}".format(var1, var2))
      
# Convert tuples to lists (or vice versa)
# Convert tuple to lists and lists to tuple.
my_list = [1, 2, 3]
my_tuple = ('x', 'y', 'z')
print("Output #100: {}".format(tuple(my_list)))
print("Output #101: {}".format(list(my_tuple)))

# Creating a dictionary
# Creating a dictionary using curly braces.
# Use a colon between each pair of keys and values.
# The len () function counts the number of key-value pairs in the dictionary.
# (a function that tells the number of elements in len)
empty_dict = { }
a_dict = {'one':1, 'two':2, 'three':3}
print("Output #102: {}".format(a_dict))
print("Output #103: a_dict has {!s} elements".format(len(a_dict)))
another_dict = {'x':'printer','y':5,'z':['star', 'circle', 9]}
print("Output #104: {}".format(another_dict))
print("Output #105: another_dict also has {!s} elements".format(len(another_dict)))
      
# Accessing values ​​in a dictionary.
# Use keys to access specific values ​​in the dictionary.
print("Output #106: {}".format(a_dict['two']))
print("Output #107: {}".format(another_dict['z']))
      
# Copy
# Create a dictionary copy using the copy() function.
a_new_dict = a_dict.copy()
print("Output #108: {}".format(a_new_dict))
      
# Key, value, item
# Access key, value, and key-value 
# pairs in a dictionary using key (), value (), and items ()
print("Output #109: {}".format(a_dict.keys()))
print("Output #110: {}".format(a_dict.values()))
print("Output #111: {}".format(a_dict.items()))

# Use in, not in, get.
if 'y' in another_dict:
    print("Output #114: y is a key in another_dict: {}."\
.format(another_dict.keys()))
if 'c' not in another_dict:
    print("Output #115: c is not a key in another_dict:{}."\
.format(another_dict.keys()))
print("Output #116: {!s}".format(a_dict.get('three')))
print("Output #117: {!s}".format(a_dict.get('four')))
print("Output #118: {!s}".format(a_dict.get('four', 'Not in dict')))
      
# Sorting.
# Organizing dictionaries using the sorted () function.
# If you want to sort the original dictionary without modifying it, make a copy first.
# The lambda (lambda) function is a short function that returns an expression at runtime.
print("Output #119: {}".format(a_dict))
dict_copy = a_dict.copy()
ordered_dict1 = sorted(dict_copy.items(), key=lambda item: item[0])
print("Output #120 (order by key): {}".format(ordered_dict1))
ordered_dict2 = sorted(dict_copy.items(), key=lambda item: item[1])
print("Output #121 (ordered by value): {}".format(ordered_dict2))
ordered_dict3 = sorted(dict_copy.items(), key=lambda x: x[1],reverse=True)
print("Output #122 (order by value, descending): {}".format(ordered_dict3))
ordered_dict4 = sorted(dict_copy.items(), key=lambda x: x[1], reverse=False)
print("Output #123 (ordered by value, ascending): {}".format(ordered_dict4))

# References Foundations for Analytics with Python.
