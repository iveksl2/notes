#Perform the t-test, assuming the variances are equal in the treatment groups
t.test(pct.month12~treatment.group, var.equal=TRUE, data = Acupuncture)

#Use the compareGroups function to save a summary of the results in pct.month12.test
pct.month12.test<-compareGroups(treatment.group ~ pct.month12 , data = Acupuncture)

#Use the createTable function to summarize and store the results saved in pct.month12.test.
pct.month12.table<- createTable(pct.month12.test, show.ratio = FALSE, show.p.overall=TRUE)

#Display the results of pct.month12.table
pct.month12.table


# Randomized blocks
#Use the blockrand function for 14 patients, two arms and block size 2.
set.seed(123)
block2 <- blockrand(n=14, num.levels = 2,  block.prefix='B', block.sizes = c(1,1))

#Display the list.
block2

#Tabulate the numbers per treatment arm.
table(block2$treatment)
