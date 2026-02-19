'''1. Write a recursive function factorial(n) that returns the factorial of a number.'''

def factorial(n):
    if(n==0):
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


'''2. Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number'''

def sum_of_digits(n):
    if(n==0):
        return 1
    else: 
        return n+(n-1)
    
print(sum_of_digits(3))