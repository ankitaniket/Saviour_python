st=input()
cnt1=0
cnt2=0
cnt3=0
for a in st:
    if a.isalpha():
        cnt1=cnt1+1
    elif a.isdigit():
        cnt2=cnt2+1
    else:
        cnt3=cnt3+1
print("Total counts of chars, digits, and symbols ")
print("Chars = ",cnt1,"Digit = ",cnt2,"Symbol = ",cnt3)

