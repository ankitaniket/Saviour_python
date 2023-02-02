a=int(input("Enter the first value : "))
b=int(input("Enter the second value : "))

prod=lambda a,b:a*b
div=lambda a,b:a/b

big=lambda a,b : max(a,b)
small=lambda a,b : min(a,b)


print(prod(a,b))
print(div(a,b))
print(big(a,b))
print(small(a,b))