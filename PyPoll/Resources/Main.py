#import modules
import os
import csv
#create csv path
csvpath = 'election_data.csv'
#defining variables

#read csv path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    print(header)
