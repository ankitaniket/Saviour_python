try:
    with open('input.txt','r') as f:
        input_string = f.readline()
        l1 = []
        l2 = []
        print("The input string is:", input_string)
        mySet = set(input_string)
        for element in mySet:
            countOfChar = 0
            for character in input_string:
                if character == element:
                    countOfChar += 1

            l1.append(element)
            l2.append(countOfChar)
            res_dct = dict(zip(l1, l2))

        print(res_dct)
except:
    print("Invalid Input")    
