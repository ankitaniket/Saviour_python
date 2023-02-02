with open('input.txt', 'r') as f:
    create = f.read().split(", ")
    int_list = []
    float_list = []

    try:
        for i in create:
            int_list.append(int(i))
        for i in int_list:
            if i % 5 == 0 and i % 3 == 0:
                print(i, end = ' ')
    except ValueError:
        try:
            for i in create:
                float_list.append(float(i))
            for i in float_list:
                if i % 5.0 == 0 and i % 3.0 == 0:
                    print(i, end = ' ')
        except Exception:
            print("Invalid Input", end = ' ')
