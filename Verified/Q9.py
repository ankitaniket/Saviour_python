sample_list= []
try:
    with open('input.txt', 'r') as f:
        sample_list = f.read().split(", ") 
        element = sample_list.pop(4)
        sample_list.insert(2, element)
        sample_list.append(element)
        print(sample_list)
except:
    print("Invalid Input")
