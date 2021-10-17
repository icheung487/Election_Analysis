
import datetime
from typing import ClassVar
now = datetime.datetime.now()
print("the time right now is", now)

#Direct Parth to the file 
file_to_load = 'Resources/election_results.csv'

#Open the election results and read the file: 
election_data = open(file_to_load, 'r')
#close the file 
election_data.close()
# Open the election results and read the file using "with"
with open(file_to_load) as election_data:
    print(election_data)
import os
dir(os)

import csv
import os
#VARIABLE TO OPEN THE CSV FILE AND CONNECT IT TO THE TXT FILE
file_to_load = os.path.join("Resources", "election_results.csv")
#VARIABLE TO SAVE THE RESULTS TO THE TXT FILE
file_to_save = os.path.join("analysis","election_analysis.txt")
#VARIABLE TO FIND THE TOTAL VOTES SINCE THIS IS WHAT YOUR LOOKING FOR
total_votes=0

#VARIABLE FOR CANDIDATION OPTIONS AND CANDIDATE VOTES
candidate_options = []
candidate_votes = {}

#TRACK THE WINNING CANDIDATE, VOTE COUNT AND PERCENTAGE. 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#OPEN THE ELECTION RESULTS AND READ THE FILE: 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #READ THE HEADER ROW. 
    headers = next(file_reader)
    #COMMAND AND CONDITIONALS START HERE:
    #PRINT EACH ROW IN THE CSV FILE:
    for row in file_reader:
        #ADD TO THE TOTAL VOTE COUNT
        total_votes +=1
        #GET THE CANDIDATE NAME FROM EACH ROW
        candidate_name = row[2]
        #IF THE CANDIDATE DOES NOT MATCH ANY EXISTING CANDIDATE ADD IT TO THE CANDIDATE OPTION LIST
        if candidate_name not in candidate_options:
            #ADD THE CANDIDATE NAME TO THE CANDIDATE OPTION LIST 
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
            #AND BEING TRACKING THAT CANDIDATE 'S VOTER COUNTER 
        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:
    #RETRIEVE VOTE COUNT AND PERCENTAGE: 
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100 
    #PRINT EACH CANDIDATE, THEIR VOTE COUNT, AND % TO THE TERMINAL
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #DETERMINE WINNING VOTE COUNT, WINNING PERCENTAGE AND CANDIDATE
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage

#PRINT THE SUMMARY
winning_candidate_summary = (
    f"------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f} %\n"
    f"-----------------------\n"
)
print(winning_candidate_summary)

