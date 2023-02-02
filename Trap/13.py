'''dict={}
n=int(input("Enter number of entries for dictionary. "))
print("Enter %d name and number for dictionary"%(n))
for i in range(n):
    pair=input().split()
    dict[pair[0]]=int(pair[1])'''

dict={'Jan':47, 'Feb':52, 'March':47, 'April':44, 'May':52, 'June':53,'July':54, 'Aug':44, 'Sept':54}
list=[]
for x in dict.values():
    if x not in list:
        list.append(x)
        
print(list)