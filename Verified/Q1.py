try:
    with open('input.txt', 'r') as infile:
        li = infile.read().split(", ")
        lst = [int(i) for i in li if i.isdigit() and len(li) == 2] 
    print((lst[0] + lst[1]) if lst[0] * lst[1] > 1000 else lst[0] * lst[1])
except:
    print("Invalid Input")
