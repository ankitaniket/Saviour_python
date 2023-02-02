a=int(input("Enter lower limit: "))
b=int(input("Enter upper limit: "))

for i in range(a,b):
    if(i%7==0 and i%5!=0):
        print(i,end=" ")