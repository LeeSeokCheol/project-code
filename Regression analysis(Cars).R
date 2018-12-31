#### Regression analysis ####
rm(list=ls())

## Step 2: Import data ##
Cars <- read.csv("cars.csv")

## Step 3: Understanding your data ## 
head(Cars) 
summary(Cars[ , c('mpg','hp','cyl','am')])

# Correlation analysis #
Cars_Correlation <- cor(Cars[ , c('mpg','hp','cyl','am')])
Cars_Correlation

## Steps 5 & 6: Regression model estimation, Model Evaluation ##
Cars_Regression <- lm(mpg ~ hp + cyl + am, data=Cars)
summary(Cars_Regression)

# Log Using transformed variables #
mpg_log <- log(Cars$mpg) 
hp_log  <- log(Cars$hp)

Cars_Regression_Log <- lm(mpg_log ~ hp_log + cyl + am, data=Cars)
summary(Cars_Regression_Log)

# Reference Professor LeeGW #