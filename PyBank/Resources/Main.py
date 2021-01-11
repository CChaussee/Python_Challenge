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
total_revenue = []
date = []
prev_row = 0
#Loop for total months/ net total
    for row in csvreader:
        total_months = total_months + 1
        net_total = net_total + int(row[1]) 
        date.append(row[0])
        changes.append(row[0])
        if date == "January 2010":     
            continue 
        else:
            changes = prev_row + 1
average_change = sum(changes)/total_months
#forgot about append function        
       
max_date = max(date)
min_date = min(date)
#trying to find changes in total through loop
average_change = monthly_changes/ total_months
    

        
        
                






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