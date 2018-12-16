# -*- coding: utf-8 -*-


# if-else 
# The != operator indicates 'not equal'.
empty_dict = { }
a_dict = {'one':1, 'two':2, 'three':3}
another_dict = {'x':'printer','y':5,'z':['star', 'circle', 9]}
x = 5
if x > 4 or x !=9:
    print("Output #124: {}".format(x))
else:
    print("Output #124: x is not greater than 4")

# if-elif-else 
if x > 6:
    print("Output #125: x is greater than six")
elif x > 4 and x == 5:
    print("Output #125: {}".format(x*x))
else:
    print("Output #125: x is not greater than 4")

# for loop
y = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', \
'Nov', 'Dec']
z = ['Annie', 'Betty', 'Claira', 'Daphne', 'Ellie',\
'Franchesca', 'Greta', 'Holly', 'Isabel', 'Jenny']

print("Output #126:")
for month in y:
    print("{!s}".format(month))
    
print("Output #127: (index value:name in list)")
for i in range(len(z)):
    print("{0!s}: {1:s}".format(i, z[1]))
    
print("Output #128: (access elements in y with z's index value)")
for j in range(len(z)):
    if y[j].startswith('J'):
        print("{!s}".format(y[j]))

print("Output #129:")
for key, value in another_dict.items():
    print("{0:s}, {1}".format(key, value))

# Use list truncation to select specific rows.
my_data = [[1,2,3],[4,5,6],[7,8,9]]
rows_to_keep = [row for row in my_data if row[2] > 5]
print("Output #130 (list comprehension): {}".format(rows_to_keep))

# References Foundations for Analytics with Python.