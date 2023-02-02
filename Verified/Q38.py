f = open("input.txt",'r')
l1=f.readline()
words = [word for word in l1.split(",")]
print(",".join(sorted(list(set(words)))))
