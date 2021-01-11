#importing modules
import os
import csv

#creating csv path
csvpath ='budget_data.csv'
#reading csv path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
#Variables/storing variables
    total_months = 0
    net_total = 0
    great_increase = 0
    great_decrease = 0
    average_change = 0
    max_date = 0
    min_date = 0
    total_revenue = 0
    date = []
    prev_row = 0
    theloop = True
    current = 0
#Loop for total months/ net total
    for row in csvreader:
        total_months = total_months + 1
        net_total = net_total + int(row[1]) 
        date.append(row[0])
        if theloop == False:
            current = prev_row - int(row[1])
            total_revenue = total_revenue + current
        


#forgot about append function        
       
max_date = max(date)
min_date = min(date)
#trying to find changes in total through loop

    

        
        
                

#write to .txt file (copied from Pypoll)
analysis.txt = 
with open(analysis.txt ,'w') as analysis.txt:
    print( "Financial Analysis", file=csvbook)
    print("--------------------",file=csvbook)
    print("Total Months:", total_months, file=csvbook)
    print("Total : $", net_total, file=csvbook)
    print("Average Change",file=csvbook)
    print("Greatest Increase in Profits",file=csvbook)
    print("Greatest Increase in Profits",file=csvbook)




#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period

print("Financial Analysis")
print("------------------")
print("Total Months:", total_months)
print("Total: $", net_total)
print("Average Change:", average_change)
print("Greatest Increase in Profits:", max_date, "$" , great_increase)
print("Greatest Decrease in Profits:", min_date, "$" , great_decrease)