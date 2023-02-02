table = {'0': 0, '1': 1, '2': 2, '3': 3,
         '4': 4, '5': 5, '6': 6, '7': 7,
         '8': 8, '9': 9, 'A': 10, 'B': 11,
         'C': 12, 'D': 13, 'E': 14, 'F': 15}

def binaryToDecimal(binary):
    binary=int(binary)
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(num," in decimal -> ",decimal)


def hexaToDecimal(num):
    hexaVal=num.strip().upper()
# hexadecimal = input("Enter Hexadecimal Number: ").strip().upper()
    # computing max power value
    res = 0
    size = len(hexaVal) - 1
    
    for num in hexaVal:
        res = res + table[num]*16**size
        size = size - 1 
    
    print(num," in decimal -> ",res)
 
def OctalToDecimal(val):
    val=int(val)
    decimal_value = 0
    base = 1

    while (val):
        last_digit = val % 10
        val = int(val / 10)
        decimal_value += last_digit * base
        base = base * 8
    print("The decimal value is :",decimal_value)

# Driver code
if __name__ == '__main__':
    num = input("Enter  Number to convert : ")
    choice=int(input("Enter choice: "))
    if choice==1:
        OctalToDecimal(num)
    if choice==2:
        hexaToDecimal(num)
    if choice==3:
        binaryToDecimal(num)
    

    
    
    
