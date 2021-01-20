# import os and csv modules
import os
import csv


#variables
total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0

# define the csv path
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    row = next(csvreader)
    # print(row)

    # For loop rows
    for row in csvreader:

        # Get total votes
        total_votes += 1
        # print(total_votes)

        # Get candidate votes
        if (row[2] == "Khan"):
            Khan_votes += 1
            # print(Khan_votes)
        elif (row[2] == "Correy"):
            Correy_votes += 1
        elif (row[2] == "Li"):
            Li_votes += 1
        else:
            OTooley_votes += 1
        
    # Get percentage of votes
    Khan_percentage = Khan_votes / total_votes
    # print(Khan_percentage)
    Correy_percentage = Correy_votes / total_votes
    # print(Correy_percentage)
    Li_percentage = Li_votes / total_votes
    # print(Li_percentage)
    OTooley_percentage = OTooley_votes / total_votes
    # print(OTooley_percentage)

    # Get Winner
    winner = max(Khan_votes, Correy_votes, Li_votes, OTooley_votes)
    # print(winner)

    if winner == Khan_votes:
        winner_candidate = "Khan"
    elif winner == Correy_votes:
        winner_candidate = "Correy"
    elif winner == Li_votes:
        winner_candidate = "Li"
    else:
        winner_candidate = "O'Tooley"
    # print(winner_candidate)
            


#---------------------------------------------------------------------------
# print statements
print(f"Election Results")
print("-------------------------------")
print(f"Total Votes:  {total_votes}")
print("-------------------------------")
print(f"Khan:  {Khan_percentage:.3%}  ({Khan_votes})")
print(f"Correy:  {Correy_percentage:.3%}  ({Correy_votes})")
print(f"Li:  {Li_percentage:.3%}  ({Li_votes})")
print(f"O'Tooley:  {OTooley_percentage:.3%}  ({OTooley_votes})")
print("-------------------------------")
print(f"Winner:  {winner_candidate}")
print("-------------------------------")


# Write text file
output_file = os.path.join('Resources', 'election_data.text')

# Open Open Write File
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Election Results\n")
    txtfile.write(f"-------------------------------\n")
    txtfile.write(f"Total Votes:  {total_votes}\n")
    txtfile.write(f"-------------------------------\n")
    txtfile.write(f"Khan:  {Khan_percentage:.3%}  ({Khan_votes})\n")
    txtfile.write(f"Correy:  {Correy_percentage:.3%}  ({Correy_votes})\n")
    txtfile.write(f"Li:  {Li_percentage:.3%}  ({Li_votes})\n")
    txtfile.write(f"O'Tooley:  {OTooley_percentage:.3%}  ({OTooley_votes})\n")
    txtfile.write(f"-------------------------------\n")
    txtfile.write(f"Winner:  {winner_candidate}\n")
    txtfile.write(f"-------------------------------\n")