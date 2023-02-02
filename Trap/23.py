st=input()
lst1=st.split()
d={}
lst2=list(map(eval,input().split()))
for k,v in zip(lst2,lst1):
    d[k]=v
lst2.sort()
lst=[]
for i in lst2:
    lst.append(d[i])
print(lst)
