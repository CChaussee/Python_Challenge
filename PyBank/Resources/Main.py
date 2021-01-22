#importing modules
import os
import csv

#creating csv path
csvpath ='budget_data.csv'
#variables
total_months = 0
net_total = 0    
date = []
changes = []
total_changes = 0
#reading csv path
with open(csvpath) as csvfile:
  csvreader = csv.reader(csvfile)
  header = next(csvreader)
  first = next(csvreader)
  previous_total =  int(first[1])
  for row in csvreader:
  #total number of months
    total_months = total_months +1
  #net total
    net_total = net_total + int(row[1])
      
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    current_total = int(row[1])
    
    if current_total == previous_total:
      changes = 0  
      
    else:
      changes.append(current_total - previous_total)  
       
    previous_total = int(row[1])
    average_change = sum(changes)/len(changes)
#The greatest increase in profits (date and amount) over the entire period
  greatest_increase = max(changes)
  #max_date = 
#The greatest decrease in losses (date and amount) over the entire period    
  greatest_decrease = min(changes)
  #min_date =    
#write .txt file        
                









print("Financial Analysis")
print("------------------")
print("Total Months:", total_months)
print("Total: $", net_total)
print("Average Change: $", round(average_change))
print("Greatest Increase in Profits:", "$" , greatest_increase)
print("Greatest Decrease in Profits:", "$" , greatest_decrease)

#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)
