try:
    def gcd(a, b):
        if(b == 0):
            return a
        else:
            return gcd(b, a%b)
    f = open("input.txt", 'r')
    create = f.readline()
    l1 = create.split(", ")
    list1 = []
    list2 = []
    for i in range(len(l1)):
        list1.append(int(l1[i]))
    print (list1, end = ' ')
    a = list1[0]
    for i in range(1,len(list1)):
        a = gcd(a, list1[i])
    print("\n",a)
except Exception as e:
    print(e)
