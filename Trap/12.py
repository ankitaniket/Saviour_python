'''list=[int(x) for x in input("Enter elements for list: ").split()]
dict={}
n=int(input("Enter number of entries for dictionary. "))
print("Enter %d name and number for dictionary"%(n))
for i in range(n):
    pair=input().split()
    dict[pair[0]]=int(pair[1])'''

list=[47, 64, 69, 37, 76, 83, 95, 97]
dict={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
newlist=[]

for x in list:
    if x in dict.values():
        newlist.append(x)

print(newlist)