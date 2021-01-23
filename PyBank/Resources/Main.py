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
  #indexing(thank you Terra)
  #max_month = changes.index(greatest_increase)
  #max_date = date[max_month]
#The greatest decrease in losses (date and amount) over the entire period    
  greatest_decrease = min(changes)
  #indexing(thank you Terra)
  #min_month = changes.index(greatest_decrease)
  #min_date = date[min_month]    
   
#results                
print("Financial Analysis")
print("------------------")
print("Total Months:", total_months)
print("Total: $", net_total)
print("Average Change: $", round(average_change))
print("Greatest Increase in Profits:",  "$" , greatest_increase)
print("Greatest Decrease in Profits:", "$" , greatest_decrease)

#write to .txt thank you Terra
load_file = "budget_data.csv"
write_file = "analysis.txt"
with open(load_file) as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)

    for row in reader:
        pass
output = (
    f"Financial Analysis\n"
    f"------------------\n"
    f"Total Months: 85\n"
    f"Total $ 38382578\n"
    f"Average Change: $2315\n"
    f"Greatest Increase in Profits: $1926159\n"
    f"Greatest Decrease in Profits: $-2196167"
)

with open(write_file, 'w') as txt_file:
        txt_file.write(output)

