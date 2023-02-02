# Make a single variable to store the path of the file. This is a constant value.
# This value must be replaced with the file path from your own system in the example below.
givenFilename = "sample.txt"
# Open the file in read-only mode. In this case, we're simply reading the contents of the file.
with open(givenFilename, 'r') as givenfilecontent:
    # Get all the words in a file using the read(), split() functions
    # Store it in a variable
    wrds_lst = givenfilecontent.read().split()
# Calculate the maximum length of all words using the max(), len() functions
# by passing the above words list key= len as the arguments.
# Store it in another variable
max_len = len(max(wrds_lst, key=len))
# Get all the words which are having the maximum length
# using the list comprehension and store it in another variable
rslt = [word for word in wrds_lst if len(word) == max_len]
# Print the above result
print(*rslt)