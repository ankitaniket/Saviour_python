def Convert(tup, di):
	for a, b in tup:
		di.setdefault(a, []).append(b)
	return di

f = open("input.txt", "r")
tups = list(f.read().split(", "))
print(tups)
dictionary = {}
print (Convert(tups, dictionary))
