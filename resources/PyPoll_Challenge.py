# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

#Add our dependencies.
import csv
import os
# Add a variable to load a file from a path.
file_to_load = os.path.join("resources/election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
#Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}
# 1: Create a couty list and county votes dictionary.
county_votes = {}
county_options = []

# Track the winning Candidate, vote count and percentage 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.

        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # 2. And begin tracking each candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count 
        candidate_votes[candidate_name] += 1

        #  4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:
            # 4b: Add the exisiting county to the list of counties.
            county_options.append(county_name)
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
        # 5 :Add a vote to that candidate's count as we iterate through rows.
        county_votes[county_name] += 1

        # Save the results to our text file.
with open(file_to_save, "w") as txt_file:
        # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end="")
    
    txt_file.write(election_results) 

    # 6a: Write a for loop to get the county from the county dictionary.
    for county in county_votes:
        # 6b. Retrieve the county vote count.
        votes = county_votes[county]
        # 6c. Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 6d: Print the county results to the terminal.
        county_election_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_election_results)
        # 6e: Save the candidate votes to a text file.
        txt_file.write(county_election_results)
  
        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > winning_county_count) and (vote_percentage > winning_county_percentage):
          
            winning_county_count = votes
            winning_county_percentage = vote_percentage
            winning_county = county
    txt_file.write("\n")
    # 7: Print the county with the largest turnout to the terminal.
    # 8: Save the county with the largest turnout to a text file.
    county_results = (
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(county_results, end="")
    txt_file.write(county_results)

    # Save the final candidate vote count to the text file.
    for candidate in candidate_votes:

        #  Retrieve vote count and percentage
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
        # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary) 