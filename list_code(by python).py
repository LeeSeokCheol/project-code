# -*- coding: utf-8 -*-
# Create a list using square brackets.
# Count the number of elements in the list through the len () function.
# Find max / min values ​​of max () and min () functions.
# The count () function calculates the number of occurrences of a particular value in the list.

a_list = [1, 2, 3]
print("Output #58:{}".format(a_list))
print("Output #59: a_list has {} elemets.".format(len(a_list)))
print("Output #60: the maximum value in a_list is {}.".format(max(a_list)))
print("Output #61: the minimum value in a_list is {}.".format(min(a_list)))
another_list = ['print', 5, ['star', 'circle', 9]]
print("Output #62: {}".format(another_list))
print("Output #63: another_list also has {} element.".format(len(another_list)))
print("Output #64: 5 is in another_list {} time.".format(another_list.count(5)))
#Use index to access specific elements in list
# [0] is the first element. [-1] is the last element.
print("Output #65: {}".format(a_list[0]))
print("Output #66: {}".format(a_list[1]))
print("Output #67: {}".format(a_list[2]))
print("Output #68: {}".format(a_list[-1]))
print("Output #69: {}".format(a_list[-2]))
print("Output #70: {}".format(a_list[-3]))
print("Output #71: {}".format(another_list[2]))
print("Output #72: {}".format(another_list[-1]))
# Splitting the list
# Create a subset of list elements using list partitioning
# If splitting from the beginning, omit the first index.
# When splitting a list to the end, the last index is omitted.
print("Output #73: {}".format(a_list[0:2]))
print("Output #74: {}".format(another_list[:2]))
print("Output #75: {}".format(a_list[1:3]))
print("Output #76: {}".format(another_list[1:]))
      
# Copy the list
# Copying a list using [:]
a_new_list = a_list[:]
print("Output #77: {}".format(a_new_list))
      
# Merge lists
# Use the + operator to merge two or more lists
a_longer_list = a_list + another_list
print("Output #78: {}".format(a_longer_list))
      
      
#reference by Foudations for Analytics with Python