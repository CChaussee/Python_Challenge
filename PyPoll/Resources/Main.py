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
votes = 0
percent_votes = []
 
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
            index = Candidates.index(row[2])
        else:
            index = Candidates.index(row[2])
            Voter_count[index] + 1
winner = max(Voter_count)        
#trying to make my voter count list into an interger, thanks Google
#tester1 = Voter_count
#stringit = ''.join(tester1)
#print(stringit)
#percent_votes =  (votes/(Voter_count)*100)



#stackoverflow to learn how to format percentage
print("Election Results")
print("--------------------")
print("Total Votes:", votes)
print("--------------------")
print(Candidates[0], ":", percent_votes)
print(Candidates[1], ":", percent_votes)
print(Candidates[2], ":", percent_votes)
print(Candidates[3], ":", percent_votes)
print("--------------------")
print("Winner :", winner) 
print("--------------------")


#write to .txt file, there has to be an easier way to do this
#with open(analysis.txt ,'w') as analysis.txt:
 #   with open(csvpath, 'w') as csvbook:
  #  print("Election Results", file=csvbook)
   # print("--------------------",file=csvbook)
    #print("Total Votes:", votes, file=csvbook)
    #print("--------------------", file=csvbook)print(Candidates[0], ":", "{0:.0%}".format(option1/votes), (option1),file=csvbook)
    #print(Candidates[1], ":", ), (option2),file=csvbook)
    #print(Candidates[2], ":", , (option3),file=csvbook)
    #print(Candidates[3], ":", , (option4),file=csvbook)
    #print("--------------------",file=csvbook)
    #print("Winner :", winner,file=csvbook)
    #print("--------------------",file=csvbook) 