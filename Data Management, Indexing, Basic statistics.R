
## Data Management ##
## Import data ##
# Save admission.csv to your working folder #

list.files()   # Represents a file in the working folder. 

admission <- read.csv("admission.csv") #Import data
head(admission) # View the beginning of the data.


## Data management basics ##

# Understanding your data #
View(admission)   
str(admission)     # View data structure
summary(admission) # Output basic statistics for variables 

colnames(admission) #Variable name output
dim(admission)      #Data size output


# Indexing #
head(admission[,2])
head(admission[, 'gre'])
head(admission$gre)

admission[3,]
admission[c(1,3),]
admission[,c(1,4)]
admission[,1:3]
admission[1:2, 3:4]

# Subset #
admission[admission$gpa > 3.5,]    #GPA > 3.5
subset(admission, gpa > 3.5)       #GPA > 3.5   

admission[admission$rank == 4,] 
subset(admission, rank == 4)       

admission[(admission$gpa > 3.5 & admission$gre > 780), ] 
subset(admission, gpa > 3.5 & gre > 780) 

admission[(admission$gpa > 3.5 | admission$gre > 780), ] 
subset(admission, gpa > 3.5 | gre > 780) 



# Basic statistics #
mean_gpa   <- mean(admission$gpa); mean_gpa
median_gpa <- median(admission$gpa); median_gpa
sd_gpa     <- sd(admission$gpa); sd_gpa
min_gpa    <- min(admission$gpa); min_gpa
max_gpa    <- max(admission$gpa); max_gpa
range_gpa  <- range(admission$gpa); range_gpa


# frequently #
freq <- table(admission$rank); freq

# Variable transformation #
gre_gpa <- admission$gre * admission$gpa; head(gre_gpa) 

# Add row / column #
admission_new <- cbind(admission, data.frame(GRE_GPA = gre_gpa))
head(admission_new)

admission_new2 <- rbind(admission_new, data.frame(admit = 0, gre = 590,
                                                  gpa = 2.92, rank = 4, GRE_GPA = 590*2.92))

head(admission_new2)
ncol(admission_new2)
nrow(admission_new2)

# Data output #
write.csv(admission_new2, file="admission_new.csv")

write.csv(admission_new2, file="admission_new2.csv", row.names=FALSE)

References by Professor LEE.G.W