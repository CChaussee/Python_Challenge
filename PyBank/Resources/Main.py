#importing modules
import os
import csv
#creating csv path
csvpath = 'budget_data.csv'
#reading csv path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)


#The total number of months included in the dataset


#The net total amount of "Profit/Losses" over the entire period


#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period

#print("Financial Analysis")
#print("------------------")
#print("Total Months")
#print("Total")
#print("Average Change")
#print("Greatest Increase in Profits")
#print("Greatest Decrease in Profits")