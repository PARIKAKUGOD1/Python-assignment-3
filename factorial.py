num = int(input("Enter a number: "))

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))

fac=factorial(num)
print ("factorial of", num, "is:", fac)