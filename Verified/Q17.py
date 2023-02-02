try:
    with open ("input.txt", "r") as f:
        p = int(f.readline())
        r = int(f.readline())
        t = int(f.readline())
    ci =  p * (pow((1 + r / 100), t)) 
    print("compound Interest : ", ci)
except:
    print("Invalid Input")
