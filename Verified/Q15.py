l1 = []
try:
    with open('input.txt','r') as f:
        string = f.readline()

    n = len(string)
    total = (n*(n+1)) // 2
    print('Total number of substrings are:')
    for i in range(n):
        for j in range(i, n):
           
            l1.append(string[i:j+1])

    print(l1)
except:
    print("Invalid Input")
