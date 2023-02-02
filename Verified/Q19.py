def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def print_prime_numbers_in_interval(lower, upper):
    for num in range(lower, upper + 1):
        if is_prime(num):
            print(num, end=' ')
    print()

def read_interval_from_file(file_name):
    with open(file_name, 'r') as file:
        lower = int(file.readline())
        upper = int(file.readline())
    return lower, upper

with open("input.txt", 'r') as file:
        lower = int(file.readline())
        upper = int(file.readline())

print_prime_numbers_in_interval(lower, upper)
