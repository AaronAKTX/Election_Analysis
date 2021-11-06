#first get thed data
#determine who was running
#count votes for each candidate
#calculate percentage of votes per candidate
#determine winner of popular vote.

import datetime as dt
now = dt.datetime.now()
print("The time right now is ", now)

#Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
 # Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
