list1 = [11, 21, 23, 73, 12, 16, 45, 19]
list2 = [17, 21, 73, 64, 35, 16]

for item in list1:
    if item not in list2:
        print(item,end=" ")