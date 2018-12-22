rm(list=ls())  

## Task 1 ##
#Step 0#
index       <- c('P01', 'P02', 'P03', 'P04')
name     <- c('Monitor', 'Mouse', 'Keyboard', 'Printer')
unit_price    <- c(300.99, 50.50, 40.38, 75.52)
quantity      <- c(9,30,25,9)
discount_rate <- c(50,20,0,30)

Sales2 <- data.frame(ID=index, Product=name, Price=unit_price, QTY=quantity, Discount=discount_rate); Sales2

#Step 1#
Sales2 <- rbind(Sales2, data.frame(ID='P05',Product='Speaker', Price=39.99, QTY=9, Discount=15)); Sales2

#Step 2#
f_price <- ((1-(Sales2$Discount/100))*Sales2$Price)

Sales2 <- cbind(Sales2,data.frame(Final_Price=f_price)); Sales2

#Step 3#
Sales2[Sales2$Final_Price < mean(Sales2$Final_Price), "Product"]




