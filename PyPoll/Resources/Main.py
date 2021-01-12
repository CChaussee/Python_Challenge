#import modules
import os
import csv
#create csv path
csvpath = 'election_data.csv'
#canidate list
Candidates = []
#votes list
Voter_count = []
#defining variables
#option1= 0
#option2 = 0
#option3 = 0
#option4 = 0
votes = 0
#read csv path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
#loop
    for row in csvreader:
        votes = votes + 1
        if row[2] not in Candidates:
            Candidates.append(row[2])
            Voter_count.append(1)
        else: 
           Candidates.index(row[2])
           Voter_count[index] + 1

        



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
print("Winner :", Candidates[0]) 
print("--------------------")


#write to .txt file, there has to be an easier way to do this
#with open(analysis.txt ,'w') as analysis.txt:
 #   with open(csvpath, 'w') as csvbook:
   # print("Election Results", file=csvbook)
  #  print("--------------------",file=csvbook)
    #print("Total Votes:", votes, file=csvbook)
    #print("--------------------", file=csvbook)
    #print(Candidates[0], ":", "{0:.0%}".format(option1/votes), (option1),file=csvbook)
    #print(Candidates[1], ":", "{0:.0%}".format(option2/votes), (option2),file=csvbook)
    #print(Candidates[2], ":", "{0:.0%}".format(option3/votes), (option3),file=csvbook)
    #print(Candidates[3], ":", "{0:.0%}".format(option4/votes), (option4),file=csvbook)
    #print("--------------------",file=csvbook)
    #print("Winner : Kahn",file=csvbook)
    #print("--------------------",file=csvbook) 