lst=list(map(eval,input().split()))
a=lst[4]
lst.pop(4)
lst.insert(2,a)
lst.append(a)
print(lst)
