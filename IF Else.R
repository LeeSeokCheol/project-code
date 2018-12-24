#### Function creation, IF Else ####
rm(list=ls())

## Function ##
M <- seq(1,5)
mean(M) 
help(mean)
example(mean)

#Function creation#
My_mean <- function(x) {sum(x)/length(x)} 
My_mean(M)

My_mean2 <- function(x,y) {sum(x:y)/length(x:y)}
My_mean2(1,5)

Mat1 <- matrix(1,2,3); Mat1

Mat_dim <- function(x) {c(nrow(x),ncol(x))}
Mat_dim(Mat1)


## IF Else ##
Num1 <- 3
Num2 <- -3
Num3 <- 0

# When the condition is one. #
if(Num1 > 0) {"positive number"}  
if(Num2 > 0) {"positive number"} 
if(Num3 > 0) {"positive number"} 

# When the condition is two. #
if(Num1 > 0) {"positive number"} else {"negative number"}
if(Num2 > 0) {"positive number"} else {"negative number"}
if(Num3 > 0) {"positive number"} else {"negative number"}

# When the condition is three #
if(Num1 > 0) {"positive number"} else if (Num1 <0) {"negative number"} else {"Zero"}
if(Num2 > 0) {"positive number"} else if (Num2 <0) {"negative number"} else {"Zero"}
if(Num3 > 0) {"positive number"} else if (Num3 <0) {"negative number"} else {"Zero"}


# ifelse(a,b,c): If a is true, it returns b. otherwise, it returns c. #
3%%2  # Modulus 
# %% Output the remaining values

ifelse(Num1%%2 == 0, "Even Number", "Odd Number") # X%%Y is X mod Y

ifelse(Num3 > 0, "Positive Number", ifelse(Num3 <0, "Negative Number", "Zero"))



# If A and B are both positive, output A * B  #
# Output A + B if A or B is negative or 0 #
fn1 <- function(A,B) {
  if ((A >= 1) && (B >= 1)){C <- A*B; C}
  else {C <- A+B; C}
}

fn1(2,3)
fn1(2,-1)

fn2 <- function(A,B) {
  if ((A <= 0) || (B <= 0)){C <- A+B; C}  # || means 'or'
  else {C <- A*B; C}
}

fn2(2,3)
fn2(2,-1)

fn3 <- function(A,B) {ifelse((A >= 1) && (B >= 1), C <- A*B, C <- A+B)}

fn3(2,3)
fn3(2,-1)	

#References by Professor LEE.G.W

