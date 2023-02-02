str=input("Enter string : ")

upper=0
lower=0
for char in str:
    if(char.isupper()):
        upper+=1
    if char.islower():
        lower+=1

print("No. of upper case: ",upper)
print("No. of lower case: ",lower)
    