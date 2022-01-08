import csv
import os
# dir(csv)
# dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438})
# print(dir(str))

# file_to_load = 'Resources/election_results.csv'
# election_data = open(file_to_load, 'r')

file_to_load = os.path.join("Resources", "election_results.csv")

total_votes = 0
candidate_options = []
candidate_votes = {}

with open(file_to_load) as election_data:
    print(f"The filename object is {election_data}.")

    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    # print(headers)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

print("Here are the total number of votes: ")
print(total_votes)
print("Here are the candidate options: ")
print(candidate_options)
print("Here is the candidate dictionary: ")
print(candidate_votes)

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Calculate vote percentages:
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# # Create a filename variable to a direct or indirect path to the file.
#     file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the with statement open the file as a text file.
#     with open(file_to_save, "w") as txt_file:
#         # Write some data to the file.
#         txt_file.write(
#             "Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

# Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")
# Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
# Close the file
# outfile.close()

# Python provides a submodule os.path that allows us to access files on different operating systems
# The join() function joins our file path components together when they are provided as separate strings;
# then, it returns a direct path with the appropriate operating system separator.
# Inside the join() function, we will add the folder and file to join together
# This is called chaining.

# We used the format dictionary_name[key] to get the value for the key.
# We can use this same format to create a key.
