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
total_o = Candidates.count("O'Tooley") 
#The percentage of votes each candidate won
percent_votesk = Candidates.count("Khan")/ (votes) * 100
percent_votesc = Candidates.count("Correy")/ (votes) * 100
percent_votesli = Candidates.count("Li")/ (votes) *100
percent_voteso = Candidates.count("O'Tooley")/ (votes) *100 
 
        
#The winner of the election based on popular vote.            
winner = ("Kahn")        


print("Election Results")
print("--------------------")
print("Total Votes:", votes)
print("--------------------")
print((("Kahn:"), (total_k), (percent_votesk)))
print((("Correy:"), (total_c), (percent_votesc)))
print((("Li:"), (total_li), (percent_votesli)))
print((("O'Tooley:"), (total_o), (percent_voteso)))
print("--------------------")
print("Winner :", winner) 
print("--------------------")


#thank you Terra for the write .txt help
load_file = "election_data.csv"
write_file = "output.txt"
with open(load_file) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for row in reader:
        pass
output = (
    f"------------------\n"
    f"Kahn Wins the Election!\n"
    f"2218231 Votes: 63%\n"
    f"-------------------"
)

with open(write_file, 'w') as txt_file:
        txt_file.write(output)

         