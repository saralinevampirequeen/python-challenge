import csv

#Path to CSV
file_path = r'C:\Users\evilp\Documents\GitHub\python-challenge\PyPoll\Resources\election_data.csv'

#Define the variables
total_votes = 0
candidate_votes = {}
winner = ""

#Read the CSV
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip the header row
    header = next(csvreader)

    #Loop through each row in the CSV
    for row in csvreader:
        # Increment total votes
        total_votes += 1

        #Get the candidate name from the current row
        candidate = row[2]

        #If the candidate exists in the dict., increment their vote count
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        #Otherwise, initialize their vote count to 1
        else:
            candidate_votes[candidate] = 1

#Generate the output
analysis_output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""

#Calculate % of votes each candidate won
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    analysis_output += f"{candidate}: {percentage:.3f}% ({votes})\n"

    #Check if the current candidate is the winner
    if not winner or votes > candidate_votes[winner]:
        winner = candidate

analysis_output += f"""
-------------------------
Winner: {winner}
-------------------------
"""

#Print the analysis
print(analysis_output)

#Export to a text file
output_file = "election_results.txt"
with open(output_file, "w") as txtfile:
    txtfile.write(analysis_output)

print(f"The analysis has been saved to {output_file}.")