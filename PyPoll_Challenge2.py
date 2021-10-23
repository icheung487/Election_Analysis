
import csv
import os
#VARIABLE TO OPEN THE CSV FILE AND CONNECT IT TO THE TXT FILE
file_to_load = os.path.join("Resources", "election_results.csv")
#VARIABLE TO SAVE THE RESULTS TO THE TXT FILE
file_to_save = os.path.join("analysis","election_analysis.txt")
#Looking for voter turnout, percentage of votes and highest turnout 

with open(file_to_load) as election_data:
    print(election_data)
county_total = 0
total_votes = 0

#Variable for County Options: 
county_options = []
county_votes = {}
winning_county = ""
winning_number = 0
winning_percentage2 = 0


with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    for row in file_reader:
        county_total+=1
        county_name = row[1]
        if county_name not in county_options:
            county_options.append(county_name)

        #Finding the total number of county votes for each county. 
        #You need to first set the variable to only look for the keys in the dictionary.
            county_votes[county_name] = 0
    #YOU MUST INDENT SINCE YOU ARE ASKING FOR TOTAL NUMBER 
        county_votes[county_name] +=1

with open(file_to_load) as election_data:
    
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

with open(file_to_save,"w") as txt_file:

    election_results =(
        f"Election Results\n"
        f"-------------------\n"
        f"Total Votes:{county_total:,}\n"
        f"--------------------\n"
        f"County Votes:\n")
    print(election_results,end=" ")
    txt_file.write(election_results)


    for county_name in county_votes:
        votes = county_votes[county_name]
        vote_percentage = float(votes) / float(county_total) * 100
    
        county_results =(
        f"{county_name}:{vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        txt_file.write(county_results)
       

        if(votes > winning_number) and (vote_percentage > winning_percentage2):
            winning_county = votes
            winning_percentage2 = vote_percentage
            winning_county = county_name
    

    winning_county_summary1 = (
    f"-------------------------\n"
    f"Largest County Turnout: {winning_county}\n"
    f"--------------------------\n")
    print(winning_county_summary1)
    txt_file.write(winning_county_summary1)


##################################################################################################################
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
    #****SAVE THE RESULTS TO OUR TEXT FILE - IS THIS NEEDED IN THE MIDDLE OF CODE? 
    ###MAKE SURE TO APPEND IF YOU KEEP ADDING TO THE FILE INSTEAD OF "w" WHICH WOULD CAUSE IT TO OVERWRITE 
with open(file_to_save,"a") as txt_file:

    for candidate_name in candidate_votes:
   
    #RETRIEVE VOTE COUNT AND PERCENTAGE: 
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100 
    #PRINT EACH CANDIDATE, THEIR VOTE COUNT, AND % TO THE TERMINAL
        candidate_results = (f"{candidate_name}: {vote_percentage:1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

    #DETERMINE WINNING VOTE COUNT, WINNING PERCENTAGE AND CANDIDATE
    if (votes > winning_count) and (vote_percentage > winning_percentage):
                    winning_count = votes
                    winning_candidate = candidate_name
                    winning_percentage = vote_percentage

#PRINT THE SUMMARY
    winning_candidate_summary = (
                f"------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f} %\n"
                f"-----------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)







#####################################################################################
