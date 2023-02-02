try:
    with open('input.txt','r') as f:
        num = float(f.read())
        num2 = num
        rev = 0
        while(num2>0):
            c = num2%10
            rev = rev*10 + c
            num2 = num2//10
        if(num == rev):
            print("True", end = ' ')
        else:
            print("False", end = ' ')
except:
    print('Invalid Input')
