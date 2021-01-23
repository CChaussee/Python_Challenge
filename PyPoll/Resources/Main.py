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
kvotes = 0
cvotes = 0
livotes = 0
ovotes = 0 
#read csv path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

#loop
    for row in csvreader:
#The total number of votes cast 
        votes = votes + 1
        Candidates.append(row[2])
        Voter_count.append(row[2])
            
#The total number of votes each candidate won   
total_k = Candidates.count("Khan")
total_c = Candidates.count("Correy")
total_li = Candidates.count("Li")
total_o = Candidates.count("O'Tolley") 
#The percentage of votes each candidate won
percent_votesk = Candidates.count("Khan")/ (votes) * 100
percent_votesc = Candidates.count("Correy")/ (votes) * 100
percent_votesli = Candidates.count("Li")/ (votes) *100
percent_voteso = Candidates.count("O'Tolley")/ (votes) *100 
 
        
#The winner of the election based on popular vote.            
winner = max(Voter_count)        
















print("Election Results")
print("--------------------")
print("Total Votes:", votes)
print("--------------------")
print("Kahn"), (total_k), ":"
print("Correy"), (total_c), ":"
print("Li"), (total_li), ":"
print("O'Tooley"), (total_o), ":"
print("--------------------")
print("Winner :", winner) 
print("--------------------")


#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------



#write to .txt file, there has to be an easier way to do this
#with open(analysis.txt ,'w') as analysis.txt:
    #with open(csvpath, 'w') as csvbook:
    #print("Election Results", file=csvbook)
    #print("--------------------",file=csvbook)
    #print("Total Votes:", votes, file=csvbook)
    #print("--------------------", file=csvbook)
    #print(Candidates[0], ":",file=csvbook)
    #print(Candidates[1], ":", ),file=csvbook)
    #print(Candidates[2], ":", file=csvbook)
    #print(Candidates[3], ":", file=csvbook)
    #print("--------------------",file=csvbook)
    #print("Winner :", winner,file=csvbook)
    #print("--------------------",file=csvbook) 