st=input()
n=len(st)
lst=[]
for i in range(0,n):
    x=""
    for j in range(i,n):
        x+=st[j]
        lst.append(x)
print(lst)
        
