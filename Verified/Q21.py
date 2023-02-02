def print_duplicates(numbers):
    duplicate_elements = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                duplicate_elements.add(numbers[i])
    return duplicate_elements

# test the function with a sample input
l1 = []
with open("input.txt","r") as f:
    numbers = f.read().split(", ")
    l1 = [int(i) for i in numbers]
    result = print_duplicates(l1)
    print(list(result))
