lst1=list(map(eval,input().split()))
lst2=list(map(eval,input().split()))
lst=[]
for a in lst1:
    if a%2==1:
        lst.append(a)
for a in lst2:
    if a%2==0:
        lst.append(a)
print(lst)
