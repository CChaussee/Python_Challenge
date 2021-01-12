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
winner = max(Voter_count)
votes = 0
 
#read csv path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

#loop
    for row in csvreader:
        votes = votes + 1
        if Candidates not in row[1]:
            Candidates.append(row[1])
            Voter_count.append(row[1])
return list(set(Candidates))

        



#stackoverflow to learn how to format percentage
print("Election Results")
print("--------------------")
print("Total Votes:", votes)
print("--------------------")
#print(Candidates[0], ":", "{0:.0%}".format, Voter_count)
#print(Candidates[1], ":", "{0:.0%}".format, Voter_count)
#print(Candidates[2], ":", "{0:.0%}".format, Voter_count)
#print(Candidates[3], ":", "{0:.0%}".format, Voter_count)
print("--------------------")
#print("Winner :", winner) 
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