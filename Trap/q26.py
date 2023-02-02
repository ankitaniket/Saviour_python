def Convert(tup, di):
	for a, b in tup:
		di.setdefault(a, []).append(b)
	return di

f = open("qwerty.txt", "r")
tups = list(f.read())
print(tups)
dictionary = {}
print (Convert(tups, dictionary))
