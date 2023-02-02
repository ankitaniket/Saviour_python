try:
    with open('input.txt', 'r') as f:
        s = f.read()
        s1 = ''
        s2 = ''
        s3 = ''
        for i in s:
            if i.isupper() :
                s1=s1+i
            else:
                s2=s2+i
        s3=s2+s1
        print("Required Output: " , s3)
except:
    print("Invalid Input")
