res = 0
with open('source.txt', 'r') as infile:
    words = infile.read().split()
    max_len = len(max(words, key=len))
    res = [word for word in words if len(word) == max_len]
print(res)
