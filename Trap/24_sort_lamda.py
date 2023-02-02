dic = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]
print(dic)

print("\nSorting the List of dictionaries by according to name :")
sorted_name = sorted(dic, key = lambda x: x['name'])
print(sorted_name)

print("\nSorting the List of dictionaries by according to age :")
sorted_age = sorted(dic, key = lambda x: x['age'])
print(sorted_age)

