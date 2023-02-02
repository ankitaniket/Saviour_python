def remove_newline(file_name):
    with open(file_name, 'r') as file:
        text = file.read()

    # replace newline characters with spaces
    text = text.replace('\n', ' ')
    print(text)

# call the function
try:
    file_name = 'input.txt' # replace with the actual file name
    remove_newline(file_name)
except:
    print("File not open")
