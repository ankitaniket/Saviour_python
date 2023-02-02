
def Remove(tuple):
    x=filter(None,tuple)

    return x

l=[]
n=int(input("Enter the size of the List: "))
for i in range(n):
    m=int(input("Enter the size of the tuple: "))
    for j in range(m):
        a=input("Enter val: ")
    l.append(a)

x=tuple(l)
y=Remove(x)

print(y)