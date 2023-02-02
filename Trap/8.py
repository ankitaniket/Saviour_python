l1 = []
with open("input.txt","r") as f:
   list1 = f.read().split(", ")
   list2 = f.read().split(", ")
   
list3=[int(x) for x in list1 if list1.index(x)%2]
list3.extend([int(x) for x in list2 if list2.index(x)%2==0])
print(list3)
