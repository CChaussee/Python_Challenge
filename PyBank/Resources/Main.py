import os
import csv

csvpath = 'budget_data.csv'

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    print(header)
