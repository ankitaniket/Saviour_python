a=int(input())
b=int(input())
sta=str(bin(a).replace("0b", ""))
stb=str(bin(b).replace("0b", ""))
if sta.count('1')==stb.count('1'):
    print("YES")
else:
    print("NO")
