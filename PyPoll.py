#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# PyPoll

# incorporated the dependencies 
import csv
import os 

# files to load and output
file_to_load = os.path.join("election_data.csv")
file_to_output = os.path.join("election_analysis.txt")

# total vote counter
total_votes = 0

# candidate options and vote counter 
candidate_options = []
candidate_votes = {}

# winning candidate and winning count tracker 
winning_candidate = ""
winning_count = 0

# read the csv and convert it into a list
with open (file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    # read header 
    header = next(reader)

    for row in reader: 
        #run the loader animation
        #print(". ", end = "")
        
        # add to total vote count 
        total_votes = total_votes + 1
        
        # extract the candidate name from each row 
        candidate_name = row[2]
        
        # if the candidate does not match any existing candidate
        # (in a way our loop is discovering candidates as it goes) 
        
        if candidate_name not in candidate_options:
            # add it to the list 
            candidate_options.append(candidate_name)
            # behind tracking that candidate voter count 
            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        
with open(file_to_output, "w") as txt_file:
    # print the final vote count 
    
    election_results = (
        f"\n\nElection Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes}\n"
        f"---------------------\n"
    )
    
    print(election_results, end="")
    
    # save the final vote count to text file
    txt_file.write(election_results)
    
    # determine the winner by looping through the counts for candidate in candidate-votes
    for candidate in candidate_votes:
        
        # Retrieve vote count and percentage 
        votes = candidate_votes.get(candidate)
        votes_percentage = float(votes) / float(total_votes) *100
        
        # determine winning vote count and candidate
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        
        # print each candidate's voter count and percentage
        voter_output = f"{candidate}: {votes_percentage:.3f}% ({votes}) \n"
        
        print(voter_output)
        
        txt_file.write(voter_output)
        
    # print the winning candidates 
    winning_candidate_summary = (
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-----------------------------\n"
    )
    
    print(winning_candidate_summary)
    
    #save the winning candidate name to txt file 
    txt_file.write(winning_candidate_summary)
    

