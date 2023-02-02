try:
    with open('input.txt','r') as f:
        l1 = f.read().split(', ')
        sample_list = [int(i) for i in l1] 
    print("Original list ", sample_list)

    count_dict = dict()
    for item in sample_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    print("Printing count of each item  ", count_dict)
except:
    print("Invalid Input")
