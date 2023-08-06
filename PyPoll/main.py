import os
import csv

# Creating a path to read the output Data:
PyPollpath = os.path.join('Resources', 'election_data.csv')

# Creating a path to write the output Data:
PyPollpath_output = os.path.join('Analysis', 'Election_results.txt')

# Creating a set of variables to store data in lists and dictionaries; and assign values 

total_votes = 0
candidate_votes = {}
candidate_list = []

# Assigning null values to the following variables, winning count is related to the number of votes
winning_candidate = ""
winning_count = 0


# Opening the following csv file to read specfic data, and using dictionary reader to utilize keys and value pairs
with open(PyPollpath, encoding='UTF-8') as csvfile:
    csvreader = csv.DictReader(csvfile)

    # Taking off the header from the 1st row if needed
    # csv_header = next(csvreader)  ; can elimiate the header info if needed, but not for this analysis

    # Begin Looping the data-set, to find relevant values
    for row in csvreader:
              
        # Counting the total # of votes
        total_votes = total_votes + 1

        # Extract the candidates names from each row in index 2 or column 3
        candidate_name = row["Candidate"]

               # Set a condition, is there is no matching value for an existing candidate:
        if candidate_name not in candidate_list:
            
            # Then add it to the list of candidates currently contesting
            candidate_list.append(candidate_name)

            # Proceed with tabulating the candidate's voter count
            candidate_votes[candidate_name] = 0

        # Proceed with adding an additional value to the candidate's voter count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    Candidate_total = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes:  {total_votes}\n"
        f"-------------------------\n"
        )
        
    print(Candidate_total)

    # Creating an output as a text file
with open (PyPollpath_output, 'w') as text:
    text.write(Candidate_total)

    # Find out the winner by Looping through the counts
    for candidate in candidate_votes:

        # Determine the voter count and the percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Set a condition to determine the winning vote count and candidate
        if (votes > winning_count):
            winning_count =  votes
            winning_candidate = candidate

        # Set a variable to print the voter output
        # voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})"  ; Note:- This can also be represented by an f-string
        voter_output = (str(candidate) + ": "+ str(round(vote_percentage,3)) +"% (" +str(votes)+ ")") 

        print(voter_output)
        text.write(voter_output +"\n")
    print("-------------------------")
    print("Winner: " + str(winning_candidate))
    print("-------------------------")

    text.write("-------------------------" + "\n")
    text.write("Winner: " + str(winning_candidate) +"\n")
    text.write("-------------------------" + "\n")
