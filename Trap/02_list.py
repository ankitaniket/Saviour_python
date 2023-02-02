a=[]
n=int(input("Enter size of list: "))
for i in range(0,n):
    val=int(input("Enter value to push in the list: "))
    a.append(val)

for i in range(0,n):
    if(a[i]%5==0 and a[i]%3==0):
        print(a[i])