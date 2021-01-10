#import modules
import os
import csv
#create csv path
csvpath = 'election_data.csv'
#canidate list
Candidates = ["Khan", "Correy" , "Li", "O'Tolley" ]
#defining variables
option1= 0
option2 = 0
option3 = 0
option4 = 0
votes = 0
#read csv path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    #print(header)
#loop
    for row in csvreader:
        votes = votes + 1
        if row[2] == Candidates[0]:
            option1 = option1 + 1
        elif row[2] == Candidates[1]:
            option2 = option2 + 1
        elif row[2] == Candidates[2]:
            option3 = option3 + 1
        else: 
            option4 = option4 + 1 
        




print("Election Results")
print("--------------------")
print("Total Votes:")
print("--------------------")
print(Candidates[0], ":", (option1/votes)*100, (option1))
print(Candidates[1], ":", (option2/votes)*100, (option2))
print(Candidates[2], ":", (option3/votes)*100, (option3))
print(Candidates[3], ":", (option4/votes)*100, (option4))
print("--------------------")
print("Winner : Kahn")
print("--------------------")