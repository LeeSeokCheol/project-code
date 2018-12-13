### R Training ###

# comment R "#" does not execute the beginning sentence
## value ##
1          #Number
a          #Use Character is "" or ''. 
'a'        #Character
'1'        #Character? number?

class (1)     # Type of value
class ('1')   # '1' is a character

1; 2; 'a'     # To execute multiple commands at once ; use

## Arithmetic operation ##
2 + 1    # addition
2 - 1    # subtraction
2 * 1    # multiplication
2 / 1    # division


## logical Expression ##
3 < 2                  # True, False
3 == 1+2               # Is it the same?
3 != 1+2               # != Not the same.
'A' == 'a'             # R recognizes lower case and upper case differently.


## Variable ##
a <- 3  #  3 is stored in the variable a. 
a

var1 <- "aaa"    #character  
var2 <- 111      #number

var1
var2

class(var1)
class(var2)

num1 <- 1; num2 <- 2
num1 + num2    # Operation is possible using variables.

num3 <- '3'    # character '3'
num1 + num3    # number + character = error

num1 + as.numeric(num3) # Convert characters to numbers

## Vectors ##
vec1 <- 1:5; vec            # The numbers 1 through 5 are stored.
vec2 <- seq(1,5); vec2      # The seq (start, end) function generates a number as a permutation.
vec3 <- c(4,5,6,7,8);vec3   # Numbers can be entered directly into the vector.
vec4 <- c('a','b','c');vec4 # The vector may contain a character value.
vec5 <- c(4,'a');vec5       # The values stored in the vector are the same type!

class(vec5)            # R recognizes vec5 as a character value.

vec1*3                 # Vector * Constant operation

vec6 <- vec1 * 3; vec6    # The vector can store the result of operation between different vectors. 


vec6[3]           # 3rd value output
vec6[-3]          # Outputs values other than the third value 
vec6[2:4]         # Outputs 2nd to 4th values
vec6[c(3,5)]      # Output only the third 5th value



vec6[4] <- 20 ; vec6   # Convert fourth value to 20 

vec6 < 15              # Evaluate whether the value stored in vec6 is less than 15
vec6[vec6 < 15]        # Only values less than 15 out of the values stored in vec6 are output 


length(vec6)      # Number of values of vector Output




## Variable / Vector Management  ##

objects()              # All generated variable / vector output
rm(a)                  # Delete variable a from memory
rm(vec1)               # Remove vector vec1 from memory
objects()              # 'a' and 'vec1' deleted

rm(list=ls())          # Delete all variables / vectors stored in memory
objects()              



## function ##
log(10)                # Function to output log value for 10 
help(log)              # Usage for log function
log(4, base=2)
example(log)           # An example of using the log function             

#For reference, Professor Lee K.W
