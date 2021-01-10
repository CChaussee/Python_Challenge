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
        



#stackoverflow to learn how to format percentage
print("Election Results")
print("--------------------")
print("Total Votes:", votes)
print("--------------------")
print(Candidates[0], ":", "{0:.0%}".format(option1/votes), (option1))
print(Candidates[1], ":", "{0:.0%}".format(option2/votes), (option2))
print(Candidates[2], ":", "{0:.0%}".format(option3/votes), (option3))
print(Candidates[3], ":", "{0:.0%}".format(option4/votes), (option4))
print("--------------------")
print("Winner : Kahn")
print("--------------------")


#write to .txt file, there has to be an easier way to do this
