'''list=[int(x) for x in input("Enter elements for list: ").split()]'''
list=[4, 8, 12, 16, 2, 2, 4, 2, 8]
unique=[]
for x in list:
    if x not in unique:
        unique.append(x)
print('Original list: ', list)
print('Unique list: ', unique)
print('Tuple: ', tuple(unique))
print('Maximum number is: ', max(unique))
print('Minimum number is: ', min(unique))