try:
    f = open("input.txt", 'r')
    n = int(f.read(1))
    print("Patter- I\n ")
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()
    for i in range(n):
        for j in range(n-i-1,0,-1):
            print("*", end="")
        print()
    print()
    count = 1
    print("Patter- II \n")
    for i in range(n):
        for j in range(i+1):
            print(count, end=" ")
            count = count + 1
        print()
except Exception as e:
    print(e)
