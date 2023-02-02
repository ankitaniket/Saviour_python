try:
    with open("input.txt", "r") as f:
        num = int(f.read())
    f.close()

    factorial = 1
    if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
       print("The factorial of 0 is 1")
    else:
       for i in range(1,num + 1):
           factorial = factorial*i
    if num>0:        
        print("The factorial of",num,"is : ",factorial)
except:
    print("Invalid Value")
