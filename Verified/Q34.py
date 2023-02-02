def word_frequency(file_name):
    with open(file_name, 'r') as file:
        text = file.read()

    # split the text into words
    words = text.split()

    # create a dictionary to store the frequency of each word
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

# call the function and print the result
file_name = 'input.txt' # replace with the actual file name
result = word_frequency(file_name)
print(result)
