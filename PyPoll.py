import csv
import os
# dir(csv)
# dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438})
# print(dir(str))

# file_to_load = 'Resources/election_results.csv'
# election_data = open(file_to_load, 'r')

file_to_load = os.path.join("Resources", "election_results.csv")

with open(file_to_load) as election_data:
    print(f"The filename object is {election_data}.")

    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)
    # for row in file_reader:
    #     print(row)


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
