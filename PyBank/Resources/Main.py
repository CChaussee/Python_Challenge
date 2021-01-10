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
#reading csv path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)



#Loop, The total number of months included in the dataset
    for row in csvreader:
        total_months = total_months + 1

        





#The net total amount of "Profit/Losses" over the entire period


#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period

print("Financial Analysis")
print("------------------")
print("Total Months", total_months)
#print("Total")
#print("Average Change")
#print("Greatest Increase in Profits")
#print("Greatest Decrease in Profits"