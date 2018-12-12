#!/usr/bin/env python3
from math import exp, log, sqrt

print("Output #11:{0:.4f}".format(exp(3)))
print("Output #12:{0:.2f}".format(log(4)))
print("Output #13:{0:.1f}".format(sqrt(81)))

# String
print("Output #14: {0:s}".format('I\'m enjoying learning prthon.'))            
print("Output #15: {0:s}".format("This is a long string. Without the backslash\
it would run off of the page on the right in the text editor and be very\
difficult to read and edit. By using the backslash you can split the long\
string into smaller strings on separate lines so that the whole string is easy\
to view in the text editor."))

print("Output #16: {0:s}".format('''You cna use triple single quotes
for muliti-line comment strings.'''))

print("Output #17:{0:s}".format("""You can also use trople dauble quotes for
multi-line somment strings"""))

#+,-,len
string1 = "This is a "
string2 = "short string."
sentence = string1 + string2
print("Output #17:{0:s}".format(sentence))
print("Output #19:{0:s} {1:s}{2:s}".format("She is","very "*4,"beatiful."))
m = len(sentence)
print("Output #20: {0:d}".format(m))
                
#split 
string1 = "My deliverable is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(" ",2)
print("Output #21: {0}".format(string1_list1))
print("Output #22: FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}"\
.format(string1_list2[0], string1_list2[1], string1_list2[2]))

string2 = "Your,deliverable,is,due,in,June"
string2_list = string2.split(',')
print("Output #23: {0}".format(string2_list))
print("Output #24: {0} {1} {2}".format(string2_list[1], string2_list[5],\
string2_list[-1]))

#join 
print("Output #25: {0}".format(','.join(string2_list))) 

#strip (strip, lstrip, rstrips), Removes unwanted character (s) from the end of the string.
string3 = " Remove  unwanted characters   from this string.\t\t    \n"
print("Output #26: string3: {0:s}".format(string3))
string3_lstrip = string3.lstrip()
print("Output #27: lstrip: {0:s}".format(string3_lstrip))
string3_rstrip = string3.rstrip()
print("Output #28: rstrip: {0:s}".format(string3_rstrip))
string3_strip = string3.strip()
print("Output #29: strip: {0:s}".format(string3_strip))

string4 = "$$Here's another string that has unwanted characters.__---++"
print("Output #30: {0:s}".format(string4))
string4 = "$$The unwanted characters have been removed.__---++"
string4_strip = string4.strip('$_-+')
print("Output #31: {0:s}".format(string4_strip))      

#replace How to replace one character or set in a string with another character or another character set.
string5 = "Let's replace the spaces in this sentence with other characters."
string5_replace = string5.replace(" ", "!@!")
print("Output #32 (with !@!): {0:s}".format(string5_replace))
string5_replace = string5.replace(" ",",")
print("Output #33 (with commas): {0:s}".format(string5_replace))

# lower : Converts all English to lower case, upper - Converts all English to uppercase
# capitalize The first character in the string is upper, and the remaining characters are lower.
string6 = "Here's WHAT Happens WHEN You Use lower."
print("Output #34: {0:s}".format(string6.lower()))
string7 = "Here's what Happens when You Ues UPPER."
print("Output #35: {0:s}".format(string7.upper()))
string5 = "here's WHAT Happens WHEN you use Capitalize."
print("Output #36: {0:s}".format(string5.capitalize()))
string5_list = string5.split()
print("Output #37: (on each word):")
for word in string5_list:
    print("{0:s}".format(word.capitalize()))
    
    
#References by Foudations for Analytics with Python.
