#importing modules
import os
import csv

#creating csv path
csvpath ='budget_data.csv'
#Variables
total_months = 0
net_total = 0
great_increase = 0
great_decrease = 0
current_total= 0
difference = 0
#reading csv path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)



#Loop
    for row in csvreader:
        total_months = total_months + 1
        net_total = net_total + int(row[1])








#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period

print("Financial Analysis")
print("------------------")
print("Total Months:", total_months)
print("Total: $", net_total)
print("Average Change:", average_change)
#print("Greatest Increase in Profits:")
#print("Greatest Decrease in Profits:"