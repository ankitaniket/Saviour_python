try:
    with open('input.txt', 'r') as infile:
        str = infile.read()

        upper, lower, num, special=0,0,0,0;
        for i in range(len(str)):
          if(str[i].isupper()):
             upper+=1
          elif(str[i].islower()):
             lower+=1
          elif(str[i].isdigit()):
              num+=1
          else:
              special+=1
        print("Upper case letters: ",upper)
        print("\nLower case letters: ",lower)
        print("\nnumbers: ",num)
        print("\nSpecial characters: ",special)
except:
    print("Invalid Input")
