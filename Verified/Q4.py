f = open("input.txt", "r")
li1=f.readline()
li2=f.readline()
create1=li1.split(", ")
create2=li2.split(", ")
li3=[]
li4=[]
li5=[]
try:
    for i in create1:
        li3.append(int(i))
    for i in create2:
        li4.append(int(i))
    for i in li3:
        if i%2!=0:
            li5.append(int(i))
    for i in li4:
        if i%2==0:
            li5.append(int(i))
    print(li5)
except Exception:
	print("Invalid input")
