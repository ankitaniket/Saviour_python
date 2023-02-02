from math import sqrt
MAX = 1000
def NthPrime(n) :
	
	count = 0
	for i in range(2, MAX + 1) :
		
		check = 0
		for j in range(2, int(sqrt(i)) + 1) :
			
			if i % j == 0 :
				check = 1
				break

		if check == 0 :
			count += 1

		if count == n :
			return i
			break
def NthFib(n) :

	f = [0] * (n + 2)
	f[0], f[1] = 0, 1

	for i in range(2, n + 1) :

		f[i] = f[i - 1] + f[i - 2]

	return f[n]
def findNthTerm(n) :

	if n % 2 == 0 :
		n //= 2
		n = NthPrime(n)
		print(n)

	else :
		n = (n // 2) + 1
		n = NthFib(n - 1)
		print(n)
if __name__ == "__main__" :

	f = open("input.txt","r")
	x = int(f.read())
	findNthTerm(X)
