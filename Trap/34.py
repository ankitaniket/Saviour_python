import re
frequency = {}
document_text = open('sample.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
most_frequent = dict(sorted(frequency.items(), key=lambda elem: elem[1], reverse=True))
most_frequent_count = most_frequent.keys()
 
for words in most_frequent_count:
    print(words, most_frequent[words])