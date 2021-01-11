#importing modules
import os
import csv

#creating csv path
csvpath ='budget_data.csv'
#Variables/storing variables
total_months = 0
net_total = 0
great_increase = 0
great_decrease = 0
average_change = 0
max_date = 0
min_date = 0
total = []
date = []
prev_month = 0

#reading csv path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
#Loop for total months/ net total
    for row in csvreader:
        total_months = total_months + 1
        net_total = net_total + int(row[1])
#googled python functions        
        date.append(row[0])
        total.append(row[1])
    max_date = max(date)
    min_date = min(date)
#trying to find changes in total through loop
    for change in total:
        changes = int(total+1) - int(total)
                






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