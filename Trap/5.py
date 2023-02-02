st=input()
ans1=""
ans2=""
for a in st:
    if a.islower():
        ans1=ans1+a
    if a.isupper():
        ans2=ans2+a
print(ans1+ans2)
