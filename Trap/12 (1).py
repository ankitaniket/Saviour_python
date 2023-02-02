lst=list(map(eval,input().split()))
d={}
st=input()
keys=st.split()
values=list(map(eval,input().split()))
for k,v in zip(keys,values):
    d[k]=v
print(lst)
print(d)
ans=[]
for x in lst:
    if x in values:
        ans.append(x)
print(ans)

