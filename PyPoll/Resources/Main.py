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




print("Election Results")
print("--------------------")
print("Total Votes:")
print("--------------------")
#print("Candidate 1 results")
#print("Candidate 2 resutls")
#print("Candidate 3 results")
#print("Candidate 4 results")
print("--------------------")
print("Winner :")
print("--------------------")