try:
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        n = int(file.readline().strip())
        print(sum([i**3 for i in range(1, n+1)]))
except Exception as e:
    print(e)
