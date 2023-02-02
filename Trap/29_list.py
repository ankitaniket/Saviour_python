def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

l=[]
n=int(input("Enter the size of the list: "))
for i in range(n):
    key=int(input("Enter val "))
    l.append(key)
print(unique_list(l)) 
