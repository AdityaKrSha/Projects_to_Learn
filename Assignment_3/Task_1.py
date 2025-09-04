def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact =fact*i
    return fact

a = int(input('Enter the number: '))
print('The Factorial of the number is:', factorial(a))
